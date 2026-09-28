---
title: "lawrie__ulx3s_examples"
parent: "Project reviews"
nav_order: 8
---
<!-- Generated from data/projects/lawrie__ulx3s_examples.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# Lawrie Griffiths' ULX3S examples (`lawrie__ulx3s_examples`)

| Field | Value |
|---|---|
| Upstream | https://github.com/lawrie/ulx3s_examples |
| Reviewed at | `b6ff000992` (upstream date 2022-05-05), reviewed 2026-09-28 |
| License | none stated: no `LICENSE`/`COPYING` file anywhere in the repo (verified with `find`). Individual files carry their own upstream headers — see Reuse notes table |
| HDL / framework | Verilog (194 `.v` files per `.claude/memory/catalogue.tsv`); one VHDL demo (`basics/sum_vhdl/top.vhd`, built through `yosys -m ghdl`) |
| Toolchain | `open`: `yosys -p "synth_ecp5 -abc9 ..."` → `nextpnr-ecp5 --${DEVICE} --package CABGA381 --freq 25"` → `ecppack --compress`. Root `ulx3s.mk` and most per-example `ulx3s.mk` copies are identical |
| Programmer | `ujprog` (`make prog` target in every `ulx3s.mk`) |
| Target FPGA(s) | Mixed per example: root `ulx3s.mk` defaults `DEVICE ?= 85k`, but most example `Makefile`s override it — `st7789/`, `cpu/`, `ps2/` set `DEVICE = 25k` (`cpu/Makefile`, `ps2/Makefile`, `st7789/Makefile`); `sdram16/`, `sdram8/`, `test68/`, `riscv/`, `basics/sum_vhdl/` keep `DEVICE = 85k`. No single answer for the whole repo — check each example's `Makefile` |
| Board revision(s) | `ulx3s_v20.lpf` — every example directory carries its own copy of the same LPF (confirmed identical size, 22.6K, across all `find`-listed copies) |
| Activity | Single commit reviewed: `b6ff000992` dated 2022-05-05 (`git -C original_sources/lawrie__ulx3s_examples log -1 --format=%cs`). `.claude/memory/history.tsv`: first commit 2020-01-02, 25 commits total (clone is shallow, no further history available) |

## What the gateware does

This is a **flat grab-bag of ~35 independent, self-contained example projects**, each with its own
`Makefile`/`ulx3s.mk` and `ulx3s_v20.lpf` — not one gateware. Grouped by topic:

- **Video, SPI display path** (`video/{text,terminal,sprite,tricolor,color,checkers,buffer}/`, `pong/*`,
  `ledpanel/`, `protocols/spidisplay/`): `spi_video.v` + `pll.v` driving a small SPI TFT; text, sprite,
  pong-style game, and checkerboard test-pattern demos, plus an LED matrix panel driver (`ledpanel/top.v`).
- **Video, HDMI/GPDI path** (`hdmi/{text,terminal,sprite,tricolor,color,checkers,menu}/`, `pong-hdmi/*`):
  the same demos re-targeted at TMDS/GPDI output via `hdmi/hdmi_video.v` (top `hdmi_video`), including a
  **PicoRV32-based SD-card game menu** in `hdmi/menu/` (top `top.v`, SoC `attosoc.v`).
- **Displays**: `st7789/`, `st7735/`, `oled/` — SPI ST7789/ST7735/generic-OLED XY-scan display cores
  (`oled_video.v`) with hex-digit and checkerboard test tops.
- **SDRAM**: `sdram16/`, `sdram8/` — 16-bit and 8-bit memory-test tops (`testram.v`) around a ported
  MiST-board `sdram.v` controller, clocked via `ecp5pll.sv`.
- **PS/2**: `ps2/` (input-only PS/2 keyboard decoder, `ps2_intf`), `ps2port/` (bidirectional PS/2 port,
  `ps2_port`), `ps2send/` (PS/2 host emulator that sends scancodes, `ps2_send`, with an iverilog testbench).
- **USB host**: `usbhost/`, `usbemard/` — USB 1.1 low-speed HID host test tops
  (`ulx3s_usbhost_test.v`, vhd2vl-translated) driving an SPI display readout; two near-duplicate copies
  with slightly different PHY file sizes.
- **CPUs / retro computers**: `cpu/` (toy 8-bit "grom" CPU + minimal computer, `grom_top.v`/`grom_cpu.v`/
  `grom_computer.v`); `computer/` (Intel 8080-compatible "Altair"-style machine, `altair.v` over
  `i8080.v`, boots Altair BASIC from `basic4k32.bin.mem`); `test68/` (Motorola 68000 core `fx68k.v` with
  an iverilog testbench, no synthesizable top — test/verification only); `riscv/` (PicoRV32 RV32I SoC,
  `attosoc.v`/`picorv32.v`, blinky + UART console variants).
- **Basics / education** (`basics/{button,counter,debounce,led,sum,sum_vhdl,trigger}/`): single-concept
  teaching demos, one of which (`sum_vhdl/`) is VHDL built through `yosys -m ghdl`.
- **Audio** (`audio/{piano,sound}/`): standalone `audio.v` tops, not yet inspected beyond top-level listing.
- **Protocols** (`protocols/{echo,serialtx,spidisplay}/`): small UART echo/serial-TX/SPI-display protocol demos.

## Structure

No shared top-level source tree: every directory under the repo root is an independent example with
its own `Makefile` (often `include ../ulx3s.mk` or a local `ulx3s.mk` copy) and its own
`ulx3s_v20.lpf`. The only shared files are the root `ulx3s.mk` (the build-rule template most examples
include) and `README.md` (one line: "Example Verilog code for Ulx3s"). Several directories duplicate
common helper files locally instead of importing them (`pll.v`, `spi_video.v`, `ecp5pll.sv`,
`fake_differential.v`, `clk_25_250_125_25.v`, `picorv32.v` all appear copy-pasted into multiple example
dirs — confirmed via `find`/`grep -l`).

## How to build

Generic pattern (root `ulx3s.mk`, and most per-example copies):

```
yosys -p "synth_ecp5 -abc9 -top top -json toplevel.json" <verilog files>
nextpnr-ecp5 --${DEVICE} --package CABGA381 --freq 25 --textcfg toplevel.config \
             --json toplevel.json --lpf ulx3s_v20.lpf
ecppack --compress toplevel.config toplevel.bit
ujprog toplevel.bit        # make prog
```

Run from inside the example directory, e.g. `make -C st7789 compile` (`st7789/Makefile`:
`DEVICE = 25k`, `IDCODE = 0x21111043`, top `TOP ?= top_checkered.v`). `sdram16/Makefile` and
`sdram8/Makefile` build with `synth_ecp5 -abc9 -top testram`; `test68/ulx3s.mk` builds
`-top test68` and adds `--debug --log nextpnr.log` to nextpnr. `basics/sum_vhdl/ulx3s.mk` instead runs
`yosys -m ghdl -p "ghdl --std=08 --ieee=synopsys top.vhd -e top" -p "hierarchy -top top" -p "synth_ecp5 -json ..."`.
Not run (read-only review).

**Testbenches** (verified, corrects catalogue.tsv's summary — see report below): `ps2send/Makefile` has
its own `tb: tb.v $(VERILOG)` → `iverilog -o tb tb.v ps2_send.v` (works: `ps2send/tb.v` exists, ends in
`$finish` after a fixed cycle count — waveform-dump only, no self-check). `test68/ulx3s.mk` also defines
`tb: test68.v $(VERILOG)` → `iverilog -o tb tb.v $(VERILOG)`, and `test68/tb.v` + `test68/test68.v` both
exist, so `make -C test68 sim` works (same pattern: `$finish` after a cycle count, no assertions).
`sdram16/ulx3s.mk` and `sdram8/ulx3s.mk` **also** define an identical `tb: test68.v $(VERILOG)` target
(copy-pasted from `test68/ulx3s.mk`) but neither directory contains a `test68.v` or `tb.v` — `make -C
sdram16 sim` / `make -C sdram8 sim` fail with a missing-file error. `basics/sum_vhdl/ulx3s.mk` has no
`tb`/`sim` target at all; `ghdl` there is invoked only for synthesis (`yosys -m ghdl`), not simulation.

## Reuse notes

| Block | Path | Top module | Language | Vendor primitives | License |
|---|---|---|---|---|---|
| PS/2 keyboard decoder (input-only) | `ps2/ps2.v` | `ps2_intf` | Verilog | none | none found (no header) |
| PS/2 bidirectional port | `ps2port/ps2_port.v` | `ps2_port` | Verilog (ISO-8859 encoded) | none | none found (no header) |
| PS/2 host-side sender (test/dev tool) | `ps2send/ps2_send.v` | `ps2_send` | Verilog | none | none found |
| ST7789/ST7735 SPI display XY-scan core | `st7789/oled_video.v`, `st7735/oled_video.v` | `oled_video` | Verilog | none | **BSD** (`// AUTHORS=EMARD,MMICKO and Lawrie Griffiths` / `// LICENSE=BSD` header in file) |
| SDRAM controller (16-bit) | `sdram16/sdram.v` | `sdram` | Verilog | none | **GPL-3.0-or-later** (Till Harbaum, MiST board — see header, `Copyright (c) 2013`) |
| SDRAM controller (8-bit) | `sdram8/sdram.v` | `sdram` | Verilog | none | **GPL-3.0-or-later** (same MiST-board origin, "adaptation of Ludde's NES core") |
| Parametric ECP5 PLL | `sdram16/ecp5pll.sv`, `sdram8/ecp5pll.sv` | `ecp5pll` | SystemVerilog | `EHXPLLL` (inside) | BSD (`// (c)EMARD` / `// License=BSD` header) |
| HDMI/DVI TMDS output | `hdmi/hdmi_video.v` + `vga2dvid.v` + `tmds_encoder.v` + `fake_differential.v` + `clk_25_250_125_25.v` | `hdmi_video` | Verilog (`tmds_encoder.v` is a vhd2vl VHDL→Verilog translation) | `EHXPLLL` (`clk_25_250_125_25.v`), `ODDRX1F` (`fake_differential.v`, comment: "DDR mode uses Lattice ECP5 vendor-specific module ODDRX1F") | `vga2dvid.v`: MIT (Mike Field, 2012 header); `tmds_encoder.v`/`fake_differential.v`: no explicit license comment found |
| PicoRV32 RISC-V SoC + SD-card menu | `hdmi/menu/{top.v,attosoc.v,picorv32.v,sdcard.v,spi_master.v}`, `riscv/{attosoc.v,picorv32.v}` | `top` (menu) / `top` (riscv) | Verilog | none | **ISC** (`picorv32.v`, `attosoc.v`: Clifford Wolf/David Shah header, "Permission to use, copy, modify...") |
| USB 1.1 low-speed HID host | `usbhost/{usbh_sie.v,usbh_host_hid.v,usb_phy.v,...}`, near-duplicate in `usbemard/` | `UsbhSie` / `ulx3s_usbhost_test` | Verilog (vhd2vl-translated from VHDL) | none found in the translated Verilog | **BSD** (vhd2vl header notes "License=BSD" for the underlying VHDL; the vhd2vl tool itself is separately GPLv2 but that covers only the translator, not this output) |
| Intel 8080-compatible CPU ("Altair" machine) | `computer/i8080.v`, `computer/altair.v` | `i8080` / `altair` | Verilog | none | **modified BSD** (`i8080.v` header: "Bashkiria-2M FPGA REPLICA... distributed under modified BSD license", Dmitry Tselikov; `LICENSE.TXT` it references is not included in this repo) |
| Motorola 68000 core (verification only, no top) | `test68/fx68k.v`, `fx68kAlu.v` | `fx68k` | Verilog | none | none found (no header in these files) |
| Toy 8-bit "grom" CPU + computer | `cpu/grom_cpu.v`, `grom_computer.v`, `grom_top.v` | `grom_top` | Verilog | none | MIT via its origin: identical to mmicko__fpga101-workshop tutorials/10-CPU/grom_cpu.v (Miodrag Milanović, 2018) |

To drop any of these into a new ULX3S design: keep the 25 MHz `clk_25mhz` input and instantiate the
board's standard `ulx3s_v20.lpf` port names (`btn`, `led`, `gpdi_dp`/`gpdi_dn`, `sd_*`, `gp`/`gn`, etc.);
the HDMI path needs the `EHXPLLL`-based 250/125/25 MHz clock generator (`hdmi/clk_25_250_125_25.v`) and
`ODDRX1F` output stage (`fake_differential.v`) unmodified since those are ECP5-specific; the SDRAM and
PS/2 cores are clock-domain-parametric Verilog with no vendor primitives and port directly.
**License caution**: the two `sdram.v` copies are GPL-3.0-or-later (copyleft) — this is a correction to
`catalogue.tsv`, which currently lists this repo's license as "none found" across the board; several
individual files (ST7789 display, ECP5 PLL, PicoRV32, i8080/Altair, USB host, MIT-licensed `vga2dvid.v`)
carry real per-file license headers even though there is no repo-level `LICENSE` file.

## Open questions

- Repo-level license is genuinely absent (verified, no `LICENSE`/`COPYING` anywhere), but several
  reused-from-elsewhere files carry GPL-3.0 (`sdram.v` ×2) or other copyleft-adjacent terms — anyone
  reusing those two files specifically should treat them as GPL-3.0-or-later, not "no license".
- Resolved 2026-09-28: the "grom" CPU (`cpu/grom_*.v`) is byte-identical to mmicko__fpga101-workshop
  `tutorials/10-CPU/grom_cpu.v` (Miodrag Milanović, MIT), via ulx3s__fpga-odysseus.
- `test68/fx68k.v` license is unknown (no header in this copy); the fx68k core is well-known upstream
  (originally by Jorge Cwik / aka "Torlus", historically used in MiSTer cores) but the specific licensing
  terms for this file were not verifiable from the file itself.
- `audio/piano/audio.v` and `audio/sound/audio.v` were not read in detail (out of scope: no reuse claim
  in the catalogue row for them); contents unverified beyond directory listing.
- `hdmi/tmds_encoder.v` and `fake_differential.v` have no explicit license comment (only `vga2dvid.v` in
  the same directory states MIT) — unclear whether they inherit the same terms.
{% endraw %}
