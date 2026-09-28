---
name: reusable-cores
description: Where the reusable ULX3S/ECP5/iCE40 gateware cores are recorded (data/cores.json by function, with usage) and the cross-project facts that don't fit a core record — first stop when helping someone build a new design.
metadata:
  type: reference
---

Since 2026-09-28 the map of reusable cores is **data**, not this file:
- [`data/cores.json`](../../data/cores.json): 155 cores in 33 functions ([`data/functions.json`](../../data/functions.json)),
  one `best` per function plus alternatives; each with repo, file paths (verified in the clone), top module,
  language, license, FPGA/primitives, tests, ULX3S notes. Researched by 5 agents from the clones, the 18 reviews
  and the catalogue.
- [`data/core_usage.json`](../../data/core_usage.json): which other repos copy or instantiate each core
  (`make usage`, heuristic on distinctive file/module names). Most reused: emard vga2dvid/tmds_encoder (~100 repos),
  ecp5pll (~74), lawrie ESP32 SPI OSD (~31), picorv32 (~25), tv80 (~23).
- Rendered per function on the site: `docs/functions/<id>.md` (see [[data-docs-layout]]).

Quick picks (best per function, 2026-09-28): DVI = emard__ulx3s-misc vga2dvid (MIT/BSD); PLL = emard ecp5pll;
SDRAM = hdl4fpga sdram_ctlr (MIT) or ulx3s-misc sdram_pnru (public domain); SD = zipcpu__sdspi (GPL-3.0, formal);
USB device = had2019-playground USB core (LGPL, ECP5 PHY); USB host = ulx3s-misc usbhost (GPL); UART/I2C =
asinghani__pifive-cpu (Apache-2.0 / MIT alexforencich); RISC-V = picorv32 (ISC); retro 6502 = chrismoos__m6502;
Ethernet = hdl4fpga mii_ipoe (MIT); OSD = lawrie__ulx3s_sms src/osd. Check `data/cores.json` before answering.

Cross-project facts:
- **The emard "universal make" build system** (`scripts/trellis_main.mk` + `diamond_main.mk`, `FPGA_SIZE=12|25|45|85`)
  appears in ulx3s-misc, galaksija, oberon, apple2fpga, papilio-arcade, etc. It often hard-codes tool paths
  (`/mt/scratch/tmp/openfpga`), so override `TRELLIS`/path variables when building.
- **Diamond-only historical ports**: f32c, minimig, papilio-arcade, vhdl_phoenix, next186, uk101, hdl4fpga, bonfire, synthowheel.
  Porting them to the open flow usually means ghdl-yosys-plugin (VHDL). f32c's own trellis attempts are marked not working.
- **`--25k` + `--idcode 0x21111043`** is a common trick: build for 25k and load it on a 12F (same die).
- Many ulx3s.github.io entries have two copies; the preferred ones are recorded in `data/catalogue.json` `fork_of`.
- Licensing: the richest sound-chip cores (JT51/JT89, SID) are copyleft; several popular cores have no license header
  (lawrie sn76489, ulx3s-misc dacpwm, osd.v/spi_osd.v): ask the author before reusing.
- The same `usb_serial.vhd` CDC core is BSD-2 by default in f32c but GPL-2.0+ per its README in ulx3s-misc.

**How to apply:** when a user wants to build X, open the matching function in `data/cores.json` (or the site page),
check the license, then the repo's catalogue row. When a review finds a better or new block, add/update its core
record (`files` must exist in the clone), then `make check usage docs`.
