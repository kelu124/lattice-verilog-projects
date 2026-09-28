---
title: "lawrie__ulx3s_sms"
parent: "Project reviews"
nav_order: 9
---
<!-- Generated from data/projects/lawrie__ulx3s_sms.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# Sega Master System / SG-1000 for ULX3S (`lawrie__ulx3s_sms`)

| Field | Value |
|---|---|
| Upstream | https://github.com/lawrie/ulx3s_sms |
| Reviewed at | `13c2361a50` (upstream date 2023-05-19), reviewed 2026-09-28 |
| License | No repo-level `LICENSE` file (verified with `find`). Per-file: mostly no header (own code, `src/sms.v`, `src/video.v`, `sn76489.v`); imported cores carry their own terms — TV80 Z80 core is **MIT** (`src/Z80/tv80_core.v`), SDRAM controller is **GPL-3.0-or-later** (Till Harbaum/MiST), OSD/SPI helper cores are **BSD** (EMARD). The included Sega **BIOS ROM is proprietary Sega firmware**, not open-source — see Open questions |
| HDL / framework | Verilog only (`.claude/memory/catalogue.tsv`) |
| Toolchain | `open`: `yosys -p "synth_ecp5 -json ..."` (ULX3S) / `yosys -p "read -sv ...; hierarchy -top sms; synth_ecp5 -abc9 -json ..."` (ULX4M) → `nextpnr-ecp5 --<device> --package CABGA381 --timing-allow-fail --freq 25` → `ecppack --compress` |
| Programmer | `ujprog` (ULX3S, `ulx3s/ulx3s.mk` `prog` target); `fujprog` / `dfu-util -a 0 -D ... -R` (ULX4M, `ulx4m/ulx4m.mk`) |
| Target FPGA(s) | **85F default** (README: "It currently defaults to an 85F board. To use a 12F add `DEVICE = 12k` to the Makefile"); `ulx3s/ulx3s.mk` sets `DEVICE ?= 85k`; ULX4M build (`ulx4m/ulx4m.mk`) targets `um-45k` |
| Board revision(s) | `ulx3s/ulx3s_v20.lpf` (ULX3S), `ulx4m/ulx4m_v002.lpf` (ULX4M) |
| Activity | Single commit reviewed: `13c2361a50` dated 2023-05-19 (`git -C original_sources/lawrie__ulx3s_sms log -1 --format=%cs`). `.claude/memory/history.tsv`: first commit 2020-12-25, 46 commits total (clone is shallow, no further history) |

## What the gateware does

A **Sega Master System (and SG-1000-compatible) games console**, entirely in Verilog, with HDMI (+
optional VGA) output at 640×480@60Hz and joypad-1 input mapped to the board buttons:

- `src/sms.v` (top for ULX3S build) / `src/ulx4m_sms.v` (ULX4M variant, adds `src/flash_loader.v` +
  `src/flashmem.v` for flash-resident ROM loading) — top-level module `sms`, wires together the CPU,
  VDP, SDRAM cartridge store, audio and OSD.
- **CPU**: `src/Z80/tv80_*.v` — the TV80 Z80-compatible core (`tv80_core.v`, `tv80n.v`, `tv80_mcode.v`,
  `tv80_reg.v`, `tv80_alu.v`), MIT-licensed (Guy Hutchison, opencores, based on Daniel Wallner's VHDL T80).
- **Video/VDP**: `src/video.v` — a from-scratch TMS9918-compatible VDP implementation (legacy modes for
  SG-1000 compatibility; does not reproduce original VDP timing, per README), feeding `src/hdmi.v`
  (top `HDMI_out`) for GPDI/TMDS output.
- **Audio**: `src/sn76489.v` (SN76489 PSG, no license header found), `src/tone_generator.v`,
  `src/sigmadelta.v` (sigma-delta DAC for `audio_l`/`audio_r` outputs).
- **Cartridge storage**: `src/sdram.v` — MiST-board SDRAM controller (Till Harbaum, GPL-3.0-or-later,
  same file family as in `lawrie__ulx3s_examples`); ROM cartridge is loaded into SDRAM and executed from
  there using the Sega memory mapper (README: "the few games that do not use the Sega mapper will not
  work"). `src/ram.v`/`src/vram.v`/`src/rom.v` provide BRAM for 8 KB console RAM, 16 KB VRAM, and the
  32 KB BIOS ROM.
- **On-screen display / game loading — `src/osd/`** (the block this page focuses on, reused by many
  retro ports): an ESP32-driven SPI OSD stack overlaid on the HDMI output, triggered by pressing all
  four direction buttons; browses SD-card/flash `.sms` files and streams the selected ROM into SDRAM.
  MicroPython side lives in `esp32/osd/osd.py` (generic multi-platform file browser/loader shared across
  ports — it dispatches to per-console loaders such as `ld_nes.py`, `ld_ti99_4a.py`, `ld_msx.py`,
  `ld_zxspectrum.py`, `ld_orao.py`, `ld_vic20.py`, `ld_trs80.py`; **only `ld_nes.py` ships in this
  repo's `esp32/osd/` — no `.sms`-specific loader is present**, `.sms` files are matched directly by
  extension at `esp32/osd/osd.py:183` and streamed generically).
- **Displays**: `src/spi_display/lcd_video.v` (top `lcd_video`, ST7789 SPI display core, same file as in
  `emard__ulx3s-misc`/`lawrie__ulx3s_examples`) + `hex_decoder_v.v`, used for optional LCD/hex diagnostics
  (`c_lcd_hex` parameter).
- **Clocking**: `src/lattice/ecp5pll.sv` (top `ecp5pll`), identical BSD-licensed EMARD parametric PLL
  seen throughout the other two repos in this review batch.

Known issues (from `README.md`): audio needs improving, joypad 1 has problems, a vertical colour bar
appears on the left in some games, VDP edge cases are wrong, and roughly 15 named games hang, crash, or
show screen corruption (Asterix, Baku Baku Animal, Chop Lifter, Dracula, Fantastic Dizzy, Jungle Book,
Lemmings, Lion King, Miracle World, Ms Pacman, Outrun, Space Harrier, Spell Caster, Wanted, Zaxxon 3D).

## Structure

```
src/            core RTL (sms.v top, video.v VDP, sdram.v, sn76489.v, hdmi.v, ...)
src/Z80/        TV80 Z80-compatible CPU core (MIT)
src/osd/        ESP32 SPI OSD stack: osd.v, spi_osd.v, spirw_slave_v.v, spi_ram_btn.v (+ font/mem files)
src/spi_display/ SPI ST7789 display core (shared with ulx3s-misc/ulx3s_examples)
src/lattice/    ecp5pll.sv (shared EMARD PLL)
ulx3s/          ULX3S build: Makefile, ulx3s.mk, ulx3s_v20.lpf
ulx4m/          ULX4M build: Makefile, ulx4m.mk, ulx4m_v002.lpf
esp32/osd/      MicroPython OSD client (osd.py, ld_nes.py)
roms/           bios.mem (readmem-format BIOS init), bios13fx.sms (Sega Europe/USA v1.3 BIOS binary,
                proprietary), hello_world.asm/.sms (test cartridge), tomem.py (bin→mem converter)
```

## How to build

Not run (read-only review). From README + `ulx3s/Makefile`/`ulx3s.mk`:

```
cd ulx3s
make prog          # DEVICE defaults to 85k; add "DEVICE = 12k" to ulx3s/Makefile for a 12F board
```

Internally: `yosys -p "synth_ecp5 -json toplevel.json" $(VERILOG)` →
`nextpnr-ecp5 --85k --package CABGA381 --timing-allow-fail --freq 25 --textcfg ... --lpf ulx3s_v20.lpf`
→ `ecppack --compress` → `ujprog`. `VERILOG` in `ulx3s/Makefile` lists `sms.v`, `ram.v`, `vram.v`,
`rom.v`, the five `Z80/tv80_*.v` files, `video.v`, `hdmi.v`, `sn76489.v`, `tone_generator.v`,
`sigmadelta.v`, `lattice/ecp5pll.sv`, `sdram.v`, `spi_display/{lcd_video.v,hex_decoder_v.v}`, and
`osd/{osd.v,spi_osd.v,spi_ram_btn.v,spirw_slave_v.v}`. ULX4M build (`ulx4m/Makefile` + `ulx4m.mk`) adds
`flash_loader.v`/`flashmem.v`, uses `ulx4m_sms.v` as top, targets `um-45k`, and programs with
`fujprog`/`dfu-util`. Python files from `esp32/osd/` must be uploaded separately to the ESP32
(MicroPython) side. No testbenches found in this repo (`find . -iname "*tb*.v"` and directory listing
show none; `.claude/memory/catalogue.tsv` records "none found" for tests, confirmed).

## Reuse notes

| Block | Path | Top module | Language | Vendor primitives | License |
|---|---|---|---|---|---|
| **OSD video overlay (windowing)** | `src/osd/osd.v` | `osd` | Verilog | none | no header found |
| **OSD SPI text-window controller** | `src/osd/spi_osd.v` | `spi_osd` | Verilog | none | no header found |
| **Generic SPI R/W BRAM slave** | `src/osd/spirw_slave_v.v` | `spirw_slave_v` | Verilog | none | **BSD** (`// AUTHOR=EMARD` / `// LICENSE=BSD`) |
| **SPI RAM slave + debounced BTN IRQ** | `src/osd/spi_ram_btn.v` | `spi_ram_btn` | Verilog | none | **BSD** (`// AUTHOR=EMARD` / `// LICENSE=BSD`) |
| ESP32 MicroPython OSD client (generic loader) | `esp32/osd/osd.py` | class `osd` | MicroPython | n/a | **BSD** (`# AUTHOR=EMARD` / `# LICENSE=BSD`) |
| TV80 Z80-compatible CPU | `src/Z80/tv80_core.v` + `tv80n.v`/`tv80_mcode.v`/`tv80_reg.v`/`tv80_alu.v` | `tv80n` | Verilog | none | **MIT** (Guy Hutchison 2004, opencores; based on Daniel Wallner's VHDL T80) |
| SDRAM controller (MiST-board port) | `src/sdram.v` | `sdram` | Verilog | none | **GPL-3.0-or-later** (Till Harbaum, "MiST board adaptation of Ludde's NES core") |
| SPI ST7789 display core | `src/spi_display/lcd_video.v` | `lcd_video` | Verilog | none | **BSD** (`// AUTHORS=EMARD,MMICKO and Lawrie Griffiths`) |
| Parametric ECP5 PLL | `src/lattice/ecp5pll.sv` | `ecp5pll` | SystemVerilog | `EHXPLLL` | **BSD** (`// (c)EMARD`) |
| SN76489 PSG | `src/sn76489.v` | `sn76489` | Verilog | none | no header found |

**Reuse guidance for the OSD stack** (the primary reason this repo is catalogued): `spirw_slave_v.v` is
a generic clocked SPI slave exposing `rd`/`wr`/`addr[c_addr_bits-1:0]`/`data_in`/`data_out` onto a
byte-addressed bus (protocol: `00 <addr_hi> <addr_lo> <data...>` to write, `01 <addr_hi> <addr_lo>
<dummy> <data...>` to read; parametrized `c_addr_bits` and `c_sclk_capable_pin` — set the latter to 1
only if `sclk` is routed to a clock-capable pin). `spi_ram_btn.v` wraps it to also expose debounced
button state and an edge-triggered IRQ flag at fixed high-address bytes (`c_addr_btn=0xFB`,
`c_addr_irq=0xF1`, both overridable parameters) — this is the piece the ESP32 polls to detect button
presses and wake into OSD mode. `spi_osd.v` wraps another `spirw_slave_v` instance to expose a
character tile map (`c_char_file`) and font bitmap (`c_font_file`, default `font_bizcat8x16.mem`,
8×16 px glyphs) at `c_addr_display=0xFD`/`c_addr_enable=0xFE`, and instantiates `osd.v` to key the
rendered text window over the live video stream at `(c_start_x, c_start_y)` sized `c_chars_x×c_chars_y`
tiles, with optional per-pixel `c_transparency`. `osd.v` itself is a clock-domain-pure video-timing
windower (`clk_pixel`/`clk_pixel_ena`, `i_hsync`/`i_vsync`/`i_blank` in, same out plus muxed RGB) — no
board-specific ports, drops into any RGB888 pixel pipeline unmodified. To reuse in a new ULX3S design:
route the ESP32's `wifi_gpio*`/SPI pins (see `src/sms.v` ports `wifi_txd`, `wifi_rxd`, `wifi_gpio16`,
`wifi_gpio5`, `wifi_gpio0` and the `ulx3s_v20.lpf` names for them) to `spi_osd`'s `i_csn`/`i_sclk`/
`i_mosi`/`o_miso`, tap the video pipeline's RGB/hsync/vsync/blank into `spi_osd`'s `i_*` and take
`o_*` onward to the DAC/HDMI stage, and give the ESP32-side `osd.py` a console-specific loader module
(`ld_<console>.py`) that streams the selected file over the same SPI link into cartridge SDRAM/BRAM —
this repo demonstrates the pattern but ships no `ld_sms.py`. None of the OSD-stack Verilog files use
ECP5 vendor primitives, so the whole stack (`osd.v`, `spi_osd.v`, `spirw_slave_v.v`, `spi_ram_btn.v`)
is vendor-portable; only the surrounding PLL (`ecp5pll.sv`) and HDMI serializer are ECP5-specific.

## Open questions

- `osd.v` and `spi_osd.v` carry no license header at all (only the BSD-headed `spirw_slave_v.v` and
  `spi_ram_btn.v` in the same directory do) — unclear if they're meant to inherit the same BSD terms as
  the rest of EMARD's OSD stack or are unlicensed Lawrie Griffiths code; `unknown`.
  This nuances `.claude/memory/reusable-cores.md`'s blanket description of `src/osd/` as "the standard
  ESP32 SPI OSD stack" — two of its four files have no stated license.
  `.claude/memory/catalogue.tsv` records this repo's license as "none found" for the whole repo, which is
  consistent for the repo's own code but should not be read as clearing the imported MIT/GPL/BSD files.
- `sn76489.v` has no license header — origin/terms unknown; this PSG core is common in the retro-FPGA
  community but the specific provenance of this copy was not identified.
- `roms/bios13fx.sms` is a **Sega Master System v1.3 BIOS binary** (proprietary Sega firmware) committed
  directly into the repo; `roms/bios.mem` is presumably a `$readmemh`-format conversion of it. Anyone
  redistributing this repo or a fork should be aware this file is not open-source, matching the
  catalogue's "Sega BIOS in repo" note.
- Why `esp32/osd/` ships `ld_nes.py` but no SMS-specific loader is unverified — possibly an
  upload/packaging oversight, or `.sms` files are handled generically by `osd.py` without a dedicated
  `ld_*` module (the `.endswith(".sms")` check at `esp32/osd/osd.py:183` was found, but the actual
  transfer/load code path for `.sms` was not traced end-to-end in this pass).
- No testbenches exist in this repo; correctness (beyond the README's own known-bugs list) is unverified.
{% endraw %}
