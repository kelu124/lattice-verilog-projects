<!-- Generated from data/projects/smunaut__ice40-playground.json by .claude/skills/documentation/gen_pages.py; do not edit. -->

# no2fpga iCE40 core library (`smunaut__ice40-playground`)

| Field | Value |
|---|---|
| Upstream | https://github.com/smunaut/ice40-playground |
| Reviewed at | `d2fa005` (upstream date 2023-08-21), reviewed 2026-09-28 |
| License | No single top-level license (per-core `LICENSE` file); see the per-core table below. Root `LICENSE` states the general intent: CERN-OHL for HDL, MIT/GPL/LGPL for software |
| HDL / framework | Verilog (170 files across `cores/` + `projects/`) |
| Toolchain | `open`: yosys + `nextpnr-ice40` + `icepack`, driven by the `build/` submodule (`no2build`, **not fetched** in this shallow clone — `project-rules.mk` is only referenced, not present) |
| Programmer | not investigated (iCE40 boards only — iceprog/dfu-util typically) |
| Target FPGA(s) | **iCE40 UP5K only** (`SG48` package in every `projects/*/Makefile`, e.g. `DEVICE=up5k PACKAGE=sg48`) — **not ECP5, not ULX3S**. Catalogued here purely as a source of reusable core *logic* to port |
| Board revision(s) | iCEBreaker v1.0/Bitsy v0–v1, MCH2022 badge, ReDIP-SID — not applicable to ULX3S |
| Activity | single commit at the pinned clone depth (shallow, `--depth 1`); upstream date 2023-08-21; commit count/first commit unknown (`.claude/memory/history.tsv` has no entry) |

## What the gateware does

This is **not a ULX3S project** — it is Sylvain Munaut's "no2fpga" reusable IP-core
library for the iCE40 UP5K, plus example projects (`projects/memtest`, `hdmi_text`,
`rgb_panel`, `riscv_doom`, `riscv_usb`, `usb_amr`, `usb_audio`) that combine those cores
into working iCEBreaker/badge designs. It is catalogued here **only for its cores**
(`cores/no2*`), per the task brief: USB, HyperRAM, QPI PSRAM, memory cache, HUB75, and
misc bus utilities. The example `projects/` are not reviewed in this pass beyond
confirming what cores they pull in.

## Structure

- `cores/no2ice40/` — iCE40-specific IO/PLL/SPRAM/RGB-LED/SERDES primitive wrappers
  (the ECP5-porting bottleneck: see below).
- `cores/no2hyperbus/` — HyperRAM controller (memctrl + iCE40 PHY, cleanly split).
- `cores/no2qpimem/` — QPI SPI-PSRAM/flash controller (memctrl + 3 iCE40 PHY variants).
- `cores/no2memcache/` — N-way associative cache sitting in front of either PSRAM
  controller, memory-mapped to a PicoRV32/VexRiscv-style bus.
- `cores/no2usb/` — full USB 1.1 full-speed device core (submodule, own repo).
- `cores/no2hub75/` — HUB75 LED-panel driver with frame buffer + BCM dimming.
- `cores/no2misc/` — portable Wishbone bus utility cores (UART, I2C, PWM, FIFOs, glitch
  filter, `prims.v` FF/LUT primitive wrappers).
- `cores/no2muacm/` — **not present in this clone**: only `no2core.mk` and a `bin/`
  submodule pointer (prebuilt firmware binaries) exist at the pinned commit; the actual
  core RTL is not checked out here (confirmed via `git ls-tree -r HEAD -- cores/no2muacm`).
- `cores/spi_flash/`, `cores/spi_slave/`, `cores/video/` — smaller single-purpose cores
  (SPI flash reader, SPI-to-Wishbone slave bridge, simple HDMI text-mode video); their
  files carry a "Copyright (C) 2019 Sylvain Munaut ... All rights reserved" header
  followed by an explicit **`BSD 3-clause, see LICENSE.bsd`** grant line (e.g.
  `spi_flash/rtl/spi_flash_reader.v:9`, `spi_slave/rtl/spi_reg.v:9`,
  `video/rtl/hdmi_phy_4x.v:12` — verified by grep across all `.v` files in the three
  dirs). No `LICENSE.bsd` file ships inside those core directories themselves, but the
  full BSD-3-Clause text is at the repo-root `doc/LICENSE-BSD.txt`, matching the root
  `LICENSE` file's claim that "each file/project/core has the applicable license in its
  header".
- `build/` — `no2build` submodule (not fetched): holds `project-rules.mk`, the actual
  yosys/nextpnr/icepack invocation. Without it, no `projects/*/Makefile` here can be built
  as-is.

## How to build

Not run (iCE40-only, and the `build/` submodule providing `project-rules.mk` is not
fetched in this clone). For reference, `projects/memtest/Makefile` shows the pattern used
throughout: `PROJ_DEPS := no2misc no2ice40 no2muacm [+ no2qpimem|no2hyperbus] [+ video]`,
`BOARD ?= icebreaker`, `DEVICE = up5k`, `PACKAGE = sg48`,
`NEXTPNR_ARGS = --no-promote-globals --timing-allow-fail --pre-pack data/clocks.py
--pre-place $(CORE_no2ice40_DIR)/sw/serdes-nextpnr-place.py`, then
`include ../../build/project-rules.mk`. `memtest` in particular can be built with either
`MEM=spi` (QPI PSRAM, `no2qpimem`) or `MEM=hyperram` (`no2hyperbus`) — useful reference for
how these two memory cores are wired to a live design. Self-checking testbenches exist
under `cores/*/sim/` and `projects/*/sim/` (27 tb files total per the catalogue), not run
here.

## SB_* → ECP5 primitive porting map

| iCE40 primitive (in `no2ice40`) | Used for | ECP5 equivalent needed |
|---|---|---|
| `SB_IO` | General IO pad, incl. bit-banged DDR (`ice40_i2c_wb.v`, `ice40_spi_wb.v`, and every core's PHY: `hbus_phy_ice40.v`, `qpi_phy_ice40_*.v`, `usb_phy.v`, `hub75_phy*.v`) | `TRELLIS_IO` (generic tristate pad) + `ODDRX1F`/`IDDRX1F` for DDR in/out, `OFS1P3DX` for a plain registered output (the same pattern already used natively in `spritetm__hadbadge2019_fpgasoc` and `ultraembedded__orangecrab`'s PHYs) |
| `SB_GB` (global buffer, `ice40_serdes_crg.v`) | Clock buffering for the 1x/2x SERDES clock domains | ECP5 clock routing is usually automatic via nextpnr-ecp5 global promotion; for explicit edge-aligned clocking, `ECLKSYNCB`/`CLKDIVF` are the closer equivalents |
| `SB_LUT4` (`ice40_iserdes.v`, `ice40_serdes_sync.v`, `prims.v`, `no2memcache/mc_tag_match.v`) | Hand-placed LUT-based logic (fast comparators, custom SERDES bit-slip logic) | ECP5 `LUT4` primitive, or let synthesis re-infer the same behavioral logic (loses the hand-placement guarantee) |
| `SB_CARRY` (`prims.v`) | Explicit carry-chain adder | ECP5 `CCU2C` carry primitive |
| `SB_DFF`/`SB_DFFE`/`SB_DFFES`/`SB_DFFER`/`SB_DFFESS`/`SB_DFFESR` (`prims.v`) | Explicit FF variants with clock-enable/set/reset combinations | ECP5 FD1P3BX/FD1S3AX-family FFs, normally just inferred from plain `always @(posedge clk)` Verilog rather than instantiated |
| `SB_SPRAM256KA` (`ice40_spram_gen.v`, `no2hub75/hub75_framebuffer.v`) | 256Kbit×16 single-port SRAM (UltraPlus-only hard macro) | **No direct ECP5 equivalent** — ECP5 only has `DP16KD` (16 Kbit dual-port BRAM) blocks; a 256Kbit SPRAM must be rebuilt from multiple `DP16KD`s (or replaced with external SDRAM), changing the memory's address/data organization |
| `SB_RAM40_4K` (`no2usb/rtl/usb_ep_buf.v`, `usb_ep_status.v`, `usb_trans.v`) | 4 Kbit block RAM, directly instantiated (not inferred) for USB endpoint buffers | ECP5 `DP16KD`, different depth/width ratios (4Kbit vs 16Kbit blocks) — needs remapping of the `INIT_FILE`/address-width parameters, not a 1:1 swap |
| `SB_RGBA_DRV` + `SB_LEDDA_IP` (`ice40_rgb_wb.v`) | Constant-current RGB LED driver hard macro | **No ECP5 equivalent hard macro** — would need PWM-driven GPIO plus external current-limiting resistors |

## Reuse notes

### Reusable blocks

| Block | Path | Top module | Language | Vendor primitives | License |
|---|---|---|---|---|---|
| iCE40 IO/PLL/SPRAM/SERDES wrappers | `cores/no2ice40/rtl/` | `ice40_ebr`, `ice40_spram_gen`, `ice40_iserdes`, `ice40_oserdes`, `ice40_serdes_crg`, `ice40_rgb_wb`, `ice40_i2c_wb`, `ice40_spi_wb` | Verilog | `SB_IO`, `SB_GB`, `SB_LUT4`, `SB_SPRAM256KA`, `SB_RGBA_DRV` (see porting map) | CERN-OHL-P-2.0 |
| HyperRAM controller | `cores/no2hyperbus/rtl/hbus_memctrl.v` (logic) + `hbus_phy_ice40.v` (PHY) | `hbus_memctrl` / `hbus_phy_ice40` | Verilog | PHY only: `SB_IO` (DDR in/out + dynamic read-clock delay via `clk_rd_delay`) | CERN-OHL-P-2.0 |
| QPI SPI-PSRAM/flash controller | `cores/no2qpimem/rtl/qpi_memctrl.v` (logic) + `qpi_phy_ice40_{1x,2x,4x}.v` (PHY) | `qpi_memctrl` / `qpi_phy_ice40_1x`\|`_2x`\|`_4x` | Verilog | PHY only: `SB_IO` | CERN-OHL-P-2.0 |
| N-way memory cache (PSRAM/HyperBus front-end) | `cores/no2memcache/rtl/mc_core.v` | `mc_core` | Verilog | `SB_LUT4` only in `mc_tag_match.v` (fast tag comparator) | CERN-OHL-P-2.0 |
| USB 1.1 full-speed device | `cores/no2usb/rtl/usb.v` (+`usb_trans.v`, `usb_rx_*`, `usb_tx_*`, `usb_ep_buf.v`, `usb_ep_status.v`) | `usb` | Verilog | `usb_phy.v`: `SB_IO` (D+/D- bit-bang); `usb_ep_buf.v`/`usb_ep_status.v`/`usb_trans.v`: `SB_RAM40_4K` (explicit, not inferred) | CERN-OHL-P-2.0 |
| HUB75 LED-panel driver + framebuffer | `cores/no2hub75/rtl/hub75_top.v` | `hub75_top` | Verilog | `hub75_framebuffer.v`: `SB_SPRAM256KA`; `hub75_phy.v`/`hub75_phy_ddr.v`: `SB_IO` (incl. DDR variant) | **CERN-OHL-W-2.0** (Weakly Reciprocal — stronger copyleft than the other no2* cores, which are CERN-OHL-P) |
| Portable Wishbone bus utilities | `cores/no2misc/rtl/` | `uart_wb`, `i2c_master_wb`, `pwm`, `fifo_sync_ram`, `fifo_sync_shift`, `glitch_filter`, `stream2wb`, `xclk_wb`, `prims.v` (FF/LUT/carry wrappers) | Verilog | `prims.v` only: `SB_LUT4`, `SB_CARRY`, `SB_DFF*` family (everything else in `no2misc` is primitive-free, portable as-is) | CERN-OHL-P-2.0 |
| SPI flash reader / SPI-slave-to-Wishbone bridge / simple HDMI text video | `cores/spi_flash/rtl/`, `cores/spi_slave/rtl/`, `cores/video/rtl/` | `spi_flash_reader`, `spi_fast_core`, `hdmi_text_2x` | Verilog | `video/rtl/hdmi_phy_{1x,2x,4x}.v` are iCE40-DDR-style PHYs (not grepped for `SB_*` in this pass — assume porting work similar to the other PHYs above) | BSD-3-Clause (`BSD 3-clause, see LICENSE.bsd` header in every file; full text at `doc/LICENSE-BSD.txt`) |

- **HyperRAM (`no2hyperbus`) and QPI PSRAM (`no2qpimem`)** are the cleanest ports: both
  split cleanly into a primitive-free `*_memctrl.v` (the actual protocol/timing state
  machine, fully portable) and a small `*_phy_ice40.v`/`qpi_phy_ice40_*.v` file that is the
  only thing touching `SB_IO`. Porting to ECP5 means writing a new PHY file using
  `ODDRX1F`/`IDDRX1F` + `TRELLIS_IO`, following the exact same pattern already implemented
  natively for QPI-PSRAM in `spritetm__hadbadge2019_fpgasoc` (`soc/qpi_cache/qspi_phy_2x_ecp5.v`)
  and for DDR3 in `ultraembedded__orangecrab` (`ddr_test/src_v/ddr3_dfi_phy.v`) — both
  already reviewed in this repo. The HyperRAM PHY additionally exposes a `clk_rd_delay`
  input for read-clock calibration; on ECP5 the equivalent mechanism is the `DELAYF`
  primitive (not present in this iCE40 PHY, would need to be added).
- **`no2memcache`** sits on top of either memory core via a small Wishbone/Vex bus
  interface (`mc_bus_wb.v`/`mc_bus_vex.v`) and is almost entirely primitive-free — the
  easiest of the memory-adjacent cores to port (only `mc_tag_match.v`'s `SB_LUT4`
  hand-placement needs replacing, and it would work fine as plain synthesized logic).
- **`no2usb`**: architecturally similar to (and by the same author as) the from-scratch
  USB device PHY used in `spritetm__hadbadge2019_fpgasoc`'s `soc/usb/usb_phy.v`, which
  already has a working `TARGET="ECP5"` branch — a strong existing reference for porting
  this core's `usb_phy.v`. The bigger blocker here is `usb_ep_buf.v`/`usb_ep_status.v`/
  `usb_trans.v` directly instantiating `SB_RAM40_4K` (4 Kbit blocks) rather than inferring
  generic RAM — ECP5's `DP16KD` blocks are 16 Kbit and organized differently, so these
  three files need real rework, not just a primitive swap. License is CERN-OHL-P-2.0 for
  the RTL (the core's own `LICENSE.md` clarifies that only the *firmware*/software stack
  in `fw/` is LGPL-3.0+/MIT, not the HDL).
- **`no2hub75`**: upstream's own `README.md` says the author has **already run a modified
  version on ECP5** and describes the required changes as "fairly minor" — the strongest
  signal in this survey that a port is low-effort, though that ECP5 branch is not merged
  into this repo. Two things to replace: `hub75_framebuffer.v`'s `SB_SPRAM256KA` (see
  porting-map caveat above — no 1:1 ECP5 equivalent, must rebuild from `DP16KD`s) and
  `hub75_phy.v`/`hub75_phy_ddr.v`'s `SB_IO` pad instantiations. Note the **license is
  CERN-OHL-W-2.0** (Weakly Reciprocal), stronger copyleft than every other no2* core here
  (CERN-OHL-P-2.0, Permissive) — check compatibility with the rest of a target project
  before combining.
- **`no2ice40`** itself is not reusable as-is on ECP5 (it *is* the iCE40 abstraction
  layer) — it is the reference for what each higher-level core expects from its PHY layer,
  and the SB_* → ECP5 mapping table above is derived from reading it end to end.
- **`no2muacm`** cannot be assessed from this clone: its RTL is not checked out (only a
  `Makefile`-include stub and a submodule pointer to prebuilt firmware binaries exist at
  the pinned commit); would need re-cloning with `--recursive` (against this repo's
  shallow-clone policy) or fetching the `no2muacm` core repo directly to review it.
- Dependencies: every core here is a `no2build`-style module (`no2core.mk` +
  `CORE_<name>_DIR` convention) meant to be composed via the (unfetched) `build/`
  submodule; reusing a core standalone means extracting just its `rtl/*.v` files and
  writing new build glue, not reusing `no2core.mk`.

## Open questions

- `no2muacm` core RTL not available in this clone; portability/license unverified.
- `cores/video/rtl/hdmi_phy_{1x,2x,4x}.v` were not grepped for `SB_*` primitives in this
  pass (out of the brief's explicit scope of USB/HyperRAM/QPI-PSRAM/cache/HUB75); assume
  similar `SB_IO`-based DDR serialization to the other PHYs until checked.
- Whether `projects/memtest`'s `MEM=hyperram` build target (which does exercise
  `no2hyperbus` on real iCEBreaker hardware) actually passes hardware testing is not
  verified from source alone (no test log in this clone).
- Commit count / first-commit date for full-history stats not recorded in
  `.claude/memory/history.tsv`.
