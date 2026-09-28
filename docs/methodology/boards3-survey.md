---
title: "TinyFPGA EX, ECPIX-5, Cynthion survey"
parent: "Methodology"
nav_order: 1
---
<!-- Generated from data/pages/boards3-survey.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# TinyFPGA EX, ECPIX-5 and Cynthion gateware survey

Survey date: 2026-09-28. Research only: nothing cloned. Scope: three Lattice ECP5 boards (TinyFPGA EX,
LambdaConcept ECPIX-5, Great Scott Gadgets Cynthion). Extends the "ECPIX-5", "LUNA / Cynthion" and
"TinyFPGA EX" rows of `docs/methodology/ecp5-boards-survey.md` (2026-09-27).

## Method

- GitHub repository search API, unauthenticated, 7 s sleep between calls, `sort=updated`, `per_page=100`
  (34 queries, listed below). No HTTP 403 on search.
- Evidence check from the full recursive file list at HEAD (github.com `tree/HEAD` + `tree-list/<oid>` JSON
  endpoints, which do not use the 60/h core API budget), plus up to 3 Makefiles / `build.sh` and the README read
  from raw.githubusercontent.com. The commit prefix shown is the HEAD at check time.
- Board facts come from the framework board files read on 2026-09-28: `litex-hub/litex-boards`
  (`litex_boards/platforms/lambdaconcept_ecpix5.py` @d60f413bb0), `amaranth-lang/amaranth-boards`
  (`amaranth_boards/ecpix5.py` @f270d210e3), `greatscottgadgets/cynthion`
  (`cynthion/python/src/gateware/platform/cynthion_r1_4.py` @dd2340e20d), `FPGAwars/apio-definitions`
  (`definitions/boards.jsonc`), `trabucayre/openFPGALoader` (`src/board.hpp`), and the TinyFPGA EX KiCad
  netlist (`tinyfpga/TinyFPGA-EX` `board/TinyFPGA-EX.net` @88fb9d455a).
- Diff against `.claude/memory/sources.tsv`: only `ultraembedded__ecpix-5`, `greatscottgadgets__luna` and
  `gregdavill__luna-usb-serial-acm` (plus `ecp5-pcie__ecp5-pcie`) are already cloned.

**Evidence column** (same meaning as the ECP5 boards survey)

- `verified (...)`: file list read; it has a `.lpf` for the board and HDL sources.
- `partial`: Python/Amaranth/LiteX sources seen, pins come from a framework platform file (normal for Amaranth/LiteX).
- `unverified`: name / README only, or no constraints and no HDL.

**Queries (result counts)**: `tinyfpga ex`(7), `tinyfpga-ex`(6), `tinyfpga_ex`(6), `tinyfpga ecp5`(1),
`user:tinyfpga`(13), `tinyfpga ex in:readme`(12), `tinyfpga-ex in:readme`(12), `ecpix-5`(7), `ecpix5`(6),
`ecpix`(7), `ecpix5 in:readme`(21), `ecpix-5 in:readme`(25), `user:lambdaconcept`(30),
`ecpix5 language:verilog`(3), `ecpix5 amaranth`(0), `ecpix5 litex`(1), `ecpix5 language:python`(2),
`ecpix5 fork:only`(0), `cynthion`(29), `cynthion in:readme`(93), `topic:cynthion`(1),
`cynthion in:description`(22), `cynthion gateware`(3), `cynthion verilog`(0), `cynthion fork:only`(159),
`facedancer`(32), `facedancer cynthion`(1), `moondancer`(16, all unrelated), `luna usb`(19),
`luna amaranth usb`(3), `luna-soc`(34, mostly unrelated), `user:greatscottgadgets`(46),
`apollo greatscottgadgets`(0), `cynthion amaranth`(0).

## TinyFPGA EX (Luke Valenty / TinyFPGA)

**Status: never shipped (as far as can be verified).** The Crowd Supply page
<https://www.crowdsupply.com/tinyfpga/tinyfpga-ex> still reads "This project is launching soon. Coming Soon",
with a single update dated 2019-03-17 ("New Prototypes and Updated Variants"). The hardware repo was last
pushed 2019-06-02. <https://tinyfpga.com/> still lists the EX in its comparison table. zeldin/TinyCartridgeEX
(a C64 cartridge carrier for the EX, 2020-03-01) says in its README "the TinyFPGA EX is not actually
available yet".

| fact | value | source |
|---|---|---|
| FPGA (announced variants) | EX25 = LFE5U-25F, EX85 = LFE5U-85F, EX85-5G = LFE5UM5G-85F (2 SERDES + 200 MHz ref. clock) | Crowd Supply page |
| FPGA (prototype netlist) | symbol value `LFE5UM-285`, footprint `csfBGA 285` (MG285 package) | TinyFPGA-EX.net @88fb9d455a (netlist dated 2019-04-28) |
| FPGA (apio) | `tinyfpga-ex-rev1` = lfe5u-85f-6mg285c, `tinyfpga-ex-rev2` = lfe5um5g-85f-8mg285c | apio-definitions `boards.jsonc` |
| Clock | Crowd Supply: 48 MHz MEMS oscillator. Prototype netlist: `DSC6001CI2A-016.0000T` (16 MHz). Conflicting, **unverified** which one a final board would use | Crowd Supply; netlist |
| Memory | 64 Mbit HyperRAM (`S27KS0641DPBHI020` in netlist), SPI flash (128 Mbit per Crowd Supply; netlist part `S25FL064L` = 64 Mbit), microSD (Hirose DM3AT) | Crowd Supply; netlist |
| I/O | 49 dedicated + 7 shared user IO, 0.7 x 2.4 in, 2 x 24-pin edges (DIL-48 per TinyCartridgeEX), USB-C, JTAG header | Crowd Supply; netlist |
| Programming | USB via the TinyFPGA bootloader (`tinyprog`, VID:PID 1d50:6130) or JTAG | Crowd Supply; apio-definitions |
| Constraint / platform files | **none** in litex-boards, amaranth-boards or openFPGALoader (checked file lists / board.hpp on 2026-09-28). Only apio has board entries (no example gateware) | framework file lists |
| Links | <https://github.com/tinyfpga/TinyFPGA-EX> (KiCad only), <https://www.crowdsupply.com/tinyfpga/tinyfpga-ex>, <https://tinyfpga.com/> |  |

| repo | language/HDL | stars | last push | license | toolchain | what it is | evidence | in sources.tsv |
|---|---|---|---|---|---|---|---|---|
| [tinyfpga/TinyFPGA-EX](https://github.com/tinyfpga/TinyFPGA-EX) | KiCad | 78 | 2019-06-02 | NOASSERTION | n/a | Board hardware (KiCad sch/pcb/netlist), README is one line | unverified (50 files, no lpf/HDL) @88fb9d455a | no |
| [zeldin/TinyCartridgeEX](https://github.com/zeldin/TinyCartridgeEX) | KiCad | 7 | 2020-03-01 | none | n/a | C64 cartridge carrier PCB for the EX module, "completely untested" | unverified (23 files, no lpf/HDL) @ba2ced37d0 | no |

No gateware targeting the TinyFPGA EX was found: every other `tinyfpga ex` hit is TinyFPGA BX (iCE40) code
(lawrie/tinyfpga_examples, lawrie/tiny_usb_examples, clayton-rogers/CR-CPU, JimKnowler/tinyfpga-verilog-exercises).
Code search (`filename:*.lpf tinyfpga`) needs authentication and was not run.

## ECPIX-5 (LambdaConcept, ECP5-5G 45F/85F)

**Status: shipped** (sold by LambdaConcept, <https://shop.lambdaconcept.com/home/46-ecpix-5.html> as linked from
openconcepts-ar/accel2d README; current availability **unverified**). Two board revisions are known to
openFPGALoader: `ecpix5` (cable `ecpix5-debug`) and `ecpix5_r03` (cable `ft4232`).

| fact | value | source |
|---|---|---|
| FPGA / package | LFE5UM5G-45F or LFE5UM5G-85F, `-8BG554I` (CABGA554) | litex-boards platform; amaranth-boards (`package = "BG554"`, `speed = "8"`) |
| Clocks | `clk100` 100 MHz (K23, default), `clk26` (N22), `clk_aux` (H26), `serdes_clk100` differential (AF12/AF13) | litex-boards platform |
| DDR3 | 16-bit DDR3, LiteX target uses `MT41K256M16` (512 MB), SSTL15 | litex-boards platform + target |
| Ethernet | RGMII PHY, 125 MHz rx clock constraint (PHY part **unverified**) | litex-boards platform |
| Video | HDMI via an external parallel-RGB transmitter (24 data + de/hs/vs + I2C + I2S audio pins); ultraembedded/ecpix-5 names it IT6613 | litex-boards platform; ultraembedded/ecpix-5 README |
| Storage | SD card (4-bit), SPI / QSPI flash, SATA (SERDES; LiteX target `with_sata` uses LiteSATA) | litex-boards platform + target |
| USB | ULPI USB 2.0 PHY, USB-C with power control and a mux (`usbc_cfg`, `usbc_mux`), FTDI UART (`serial`) | litex-boards platform |
| User I/O | 4 RGB LEDs, 8 PMOD connectors (`pmod0`..`pmod7`) | litex-boards platform |
| Programming | FTDI (FT2232-class `ecpix5-debug` on early revisions, FT4232 on r03) JTAG: `openFPGALoader -b ecpix5` / `-b ecpix5_r03`; OpenOCD cfg in litex-boards (`prog/openocd_ecpix5.cfg`) | openFPGALoader `board.hpp`; litex-boards |
| Platform files | `litex_boards/platforms/lambdaconcept_ecpix5.py` + `targets/lambdaconcept_ecpix5.py` (DDR3, Ethernet/Etherbone, SATA, video terminal/framebuffer); `amaranth_boards/ecpix5.py` (`ECPIX545Platform`, `ECPIX585Platform`); `greatscottgadgets/luna-boards` `luna_boards/ecpix5.py` (LUNA on the ULPI PHY; repo marked UNMAINTAINED) | framework file lists |
| Docs | <https://github.com/lambdaconcept/ecpix5-readthedocs> (sources for the ReadTheDocs site; schematics `SCH_ECPIX-5_R02.PDF`, `SCH_ECPIX-5_R04.PDF`, blinky SVFs for 45/85) | file list @1246b57c89 |

| repo | language/HDL | stars | last push | license | toolchain | what the gateware does | evidence | in sources.tsv |
|---|---|---|---|---|---|---|---|---|
| [ultraembedded/ecpix-5](https://github.com/ultraembedded/ecpix-5) | Verilog | 15 | 2020-07-05 | none | open (lpf + Verilog; no Makefile) | RISC-V AXI4 SoC + DVI framebuffer via IT6613; submodules core_soc / dbg_bridge / riscv | verified (1 lpf, 19 v/sv) @17c1f633f1 | **yes** |
| [ultraembedded/core_ddr3_controller](https://github.com/ultraembedded/core_ddr3_controller) | Verilog | 637 | 2021-10-10 | none (API) | open | Small AXI4 DDR3 controller (DLL-off, <=125 MHz) with ECP5 DFI PHY; `examples/ecpix_ecp5/` top + lpf | verified (1 lpf, 15 v/sv) @a03492a600 | no |
| [ultraembedded/ecpix5-test](https://github.com/ultraembedded/ecpix5-test) | Verilog | 9 | 2020-08-20 | Apache-2.0 | open (no Makefile) | DDR3 test bitstream (same DDR3 core) | verified (1 lpf, 12 v/sv) @2eaf689c60 | no |
| [maxhpc/ecpix-5](https://github.com/maxhpc/ecpix-5) | SystemVerilog | 0 | 2025-02-09 | none | open (build.mk + per-dir Makefiles) | LEDs, UART, DDR3 top (`libs/ddr3/ddr3_top.sv`), dual-clock FIFO/DPRAM libs, `vx` design with Verilator testbench | verified (1 lpf, 11 v/sv) @dbd64a102a | no |
| [Baldanos/ecpix5-blinky](https://github.com/Baldanos/ecpix5-blinky) | Verilog | 2 | 2021-02-10 | none | open (yosys/nextpnr/ecppack/openFPGALoader) | Blinky + OpenOCD cfg | verified (1 lpf, 1 v) @b3f6104d74 | no |
| [goran-mahovlic/ECPIX5_blink](https://github.com/goran-mahovlic/ECPIX5_blink) | Verilog | 5 | 2020-12-18 | none | open (build.sh) | Blinky | verified (1 lpf, 1 v) @0d9567fda2 | no |
| [apfaudio/eurorack-pmod](https://github.com/apfaudio/eurorack-pmod) | SystemVerilog, Verilog | 239 | 2026-01-29 | NOASSERTION | open (openFPGALoader) | AK4619 audio-codec PMOD gateware (DSP cores, multi-board); `gateware/boards/ecpix5/` pinmap.lpf + sysmgr.v + Makefile (also Colorlight i5/i9, Tiliqua, iCEBreaker) | verified (6 lpf/pcf, 30 v/sv) @ddb9aa92fa | no |
| [apfaudio/eurorack-pmod-litex](https://github.com/apfaudio/eurorack-pmod-litex) | Python (LiteX), Rust fw | 19 | 2025-10-07 | none | litex | eurorack-pmod audio DSP SoC; `example-ecpix-5.py` | partial (7 .py) @61a8e4d537 | no |
| [apfaudio/eurorack-pmod-usb-soundcard](https://github.com/apfaudio/eurorack-pmod-usb-soundcard) | Python (Amaranth/LUNA) | 13 | 2025-11-18 | BSD-3-Clause | amaranth | 8-channel USB UAC2 sound card on LUNA; `rtl/ecpix5.py` | partial (7 .py) @a7a3a00cc9 | no |
| [orbcode/orbtrace](https://github.com/orbcode/orbtrace) | Python (Amaranth/LiteX) | 181 | 2026-02-06 | NOASSERTION | open (yosys/nextpnr-ecp5/ecppack/ecpprog) | Cortex-M debug + parallel TRACE probe; README: runs on ORBTrace mini and on ECPIX-5 (+ breakout board); `orbtrace/platforms/ecpix5.py` | partial (64 .py, 9 v) @e416cd5b07 | no |
| [openconcepts-ar/accel2d](https://github.com/openconcepts-ar/accel2d) | C, Verilog (generated), LiteX | 1 | 2026-09-18 | NOASSERTION | litex (trellis; `make BOARD=lambdaconcept_ecpix5`) | C-to-Verilog 2D graphics accelerators (ellipse/fill...) attached to DRAM in a LiteX SoC, MicroPython demos; `lambdaconcept_ecpix5.py` | partial (29 v, 14 py, no lpf) @1170d39af9 | no |
| [openconceptslabs/gpu2d](https://github.com/openconceptslabs/gpu2d) | C, Verilog, LiteX | 0 | 2025-04-24 | NOASSERTION | litex | Earlier version of accel2d (same layout) | partial (29 v, 9 py) @7321337ce1 | no |
| [AravindRajeshkanna/vernier-rv32](https://github.com/AravindRajeshkanna/vernier-rv32) | Verilog | 1 | 2026-09-28 | NOASSERTION | open (yosys/nextpnr-ecp5) | RV32IMA SoC, runs on ULX3S 85F; ECPIX-5 is a second target for a hand-written DDR3 PHY, README: "no ECPIX-5 hardware has been touched" (simulation / P&R only). Already listed in the ULX3S github-survey | verified (ecpix5.lpf, ecpix5_ddr3.lpf, ulx3s.lpf, 141 v) @3284906e23 | no |
| [lambdaconcept/ecpix5-bitsofcode](https://github.com/lambdaconcept/ecpix5-bitsofcode) | Python | 1 | 2020-07-07 | none | litex | Vendor code snippets | partial (3 .py) @83b4e04e7f | no |
| [hinzundcode/reboot](https://github.com/hinzundcode/reboot) | C, Python (LiteX) | 0 | 2021-01-01 | none | litex | "random ecpix5 and litex experiments, unmaintained" | partial (4 .py) @3ab5a7c2d7 | no |
| [AndrewD/litecan](https://github.com/AndrewD/litecan) | Python (LiteX) | 7 | 2023-01-16 | none | litex | CAN core for LiteX, bench target `bench/ecpix5.py` | partial (7 .py) @a641bda2f2 | no |
| [Fredrik-Reinholdsen/Amaranth-Minute-Timer](https://github.com/Fredrik-Reinholdsen/Amaranth-Minute-Timer) | Python (Amaranth) | 1 | 2024-03-25 | none | amaranth | 60 s timer on two 7-segment PMODs, ECPIX-5 | partial (3 .py) @31f3756cfc | no |
| [enjoy-digital/mquickjs-on-litex](https://github.com/enjoy-digital/mquickjs-on-litex) | C, LiteX | 2 | 2026-05-11 | NOASSERTION | litex | JavaScript engine on a LiteX SoC; ECPIX-5 live demo photo (software-centric) | partial (8 .py) @2500e71e88 | no |
| [antoinevg/cynthion-tutorials](https://github.com/antoinevg/cynthion-tutorials) | Python (Amaranth) | 4 | 2025-01-13 | BSD-3-Clause | amaranth | Also has `platform/ecpix5.py`, `ecpix5_luna.py` (see Cynthion) | partial | no |
| [aesc-silicon/ElemRV](https://github.com/aesc-silicon/ElemRV) | Scala (SpinalHDL) | 147 | 2026-09-16 | none | SpinalHDL | Open-source RISC-V MCU for IHP SG13 ASIC; ECPIX-5 is the FPGA prototype target (`.../ECPIX5/ECPIX5.scala`); same for aesc-silicon/i2c-gpio-expander (45 stars) | partial (Scala, no lpf) @9b7c6e2add | no |

Copies of core_ddr3_controller with the same `examples/ecpix_ecp5` (not forks on GitHub, identical tree size):
maxhpc/core_ddr3_controller, obr2021/core_ddr3_controller, lazzzz18/DDR3_Controller. Not listed separately.

SERDES/SATA/PCIe on ECPIX-5 (noted only, another survey covers them): LiteX target `with_sata` (LiteSATA);
`liteiclink/bench/serdes/ecpix5.py` and `liteiclink/bench/serwb/demo/ecpix5.py` (seen inside greent0r/my_litex, a
vendored LiteX tree); ECP5-PCIe/ECP5-PCIe is already cloned.

Off-target: kwadwoz/ecp5-ethernet-soc mentions ECPIX-5 only in `openFPGALoader -b ecpix5` lines, but its README
names the ECP5 Evaluation Board (LFE5UM5G-85F-8BG381) + LAN8720 as the hardware; not an ECPIX-5 design.

## Cynthion (Great Scott Gadgets, ECP5 LFE5U-12F, the LUNA hardware)

**Status: shipped** (Crowd Supply campaign 2023, hardware r1.x in production; from memory, **unverified** here).
Hardware: <https://github.com/greatscottgadgets/cynthion-hardware> (CERN-OHL-P-2.0, KiCad). Gateware platform files
for every revision r0.1 .. r1.4 live in the `cynthion` repo, not in litex-boards or amaranth-boards.

| fact | value | source |
|---|---|---|
| FPGA / package | LFE5U-12F, BG256 (CABGA256); speed grade from `ECP5_SPEED_GRADE`, default "8" (apio uses lfe5u-12f-6bg256c) | cynthion_r1_4.py @dd2340e20d; apio-definitions |
| Clock | `clk_60MHz` 60 MHz on A8 | cynthion_r1_4.py |
| USB | three ULPI USB 2.0 HS PHYs: `control_phy`, `aux_phy`, `target_phy`; target D+/D- also wired to FPGA pins (`target_usb_diff`, chirp pins) for passive sniffing; Type-C controllers for target and aux; VBUS switching / discharge | cynthion_r1_4.py |
| Memory | HyperRAM (`ram`: diff clock, 8-bit dq, rwds); SPI and QSPI flash | cynthion_r1_4.py |
| Other I/O | 2 user PMODs, `user_mezzanine` connector, user button, UART to debug MCU, `power_monitor` (I2C V/I monitor) | cynthion_r1_4.py |
| Programming | Apollo: a SAMD11 (r1.x, `cynthion_d11`) or SAMD21 (`cynthion_d21`) debug MCU acting as JTAG programmer; platform `toolchain_program()` uses `apollo_fpga.ECP5_JTAGProgrammer` (SRAM configure or flash). `self_program` pin lets gateware hand the port back. apio programmer id `apollo`. Apollo firmware = <https://github.com/greatscottgadgets/apollo> (C, 90 stars, BSD-3-Clause, 2026-05-08): MCU firmware, **not gateware** | core.py; apollo file list @04507dfaee |
| Platform files | `cynthion/python/src/gateware/platform/cynthion_r0_1.py` .. `cynthion_r1_4.py` (Amaranth, `CynthionPlatform(LUNAApolloPlatform, LatticeECP5Platform)`); LiteX platform in antoinevg/cynthion-litex `soc/platforms/gsg_cynthion.py`; Verilog `.lpf` in VoltCyclone/HurricaneFPGA `HDL/hardware/constraints/cynthion_pins.lpf` and awtoau/cynthion-workspace | file lists |

| repo | language/HDL | stars | last push | license | toolchain | what the gateware does | evidence | in sources.tsv |
|---|---|---|---|---|---|---|---|---|
| [greatscottgadgets/luna](https://github.com/greatscottgadgets/luna) | Python (Amaranth) | 1140 | 2026-08-19 | BSD-3-Clause | amaranth | USB 2.0/3.0 device/host/analyzer gateware framework | verified @82a8f73329 (previous survey) | **yes** |
| [greatscottgadgets/cynthion](https://github.com/greatscottgadgets/cynthion) | Python (Amaranth), Rust | 199 | 2026-05-22 | BSD-3-Clause | amaranth (yosys/nextpnr-ecp5) | Official gateware: `gateware/analyzer` (USB analyzer used by Packetry), `gateware/facedancer` (Moondancer SoC for Facedancer), `gateware/selftest`; platform files r0.1-r1.4; gateware tutorials (blinky, USB device 01-04); host tools | partial (75 .py, no lpf) @dd2340e20d | no |
| [greatscottgadgets/luna-soc](https://github.com/greatscottgadgets/luna-soc) | Python (Amaranth) + bundled Verilog | 31 | 2025-10-31 | BSD-3-Clause | amaranth | SoC library (Wishbone/CSR, SRAM, GPIO, UART, USB) with VexRiscv `vexriscv_cynthion.v`; `provider/cynthion.py` | partial (36 .py, 5 v) @7fa1cc16dd | no |
| [greatscottgadgets/cynthion-uac](https://github.com/greatscottgadgets/cynthion-uac) | Python (Amaranth) | 1 | 2025-07-15 | BSD-3-Clause | amaranth | USB Audio Class 2 example gateware (uac2, stream, NCO, DSP, DAC, VU meter) + talk slides | partial (10 .py) @0dfc418618 | no |
| [greatscottgadgets/cynthion-analyzer](https://github.com/greatscottgadgets/cynthion-analyzer) | Makefile | 6 | 2025-05-13 | none | amaranth/apollo | Integration repo for analyzer mode (submodules) | partial (1 .py) @2924a83070 | no |
| [greatscottgadgets/cynthion-test](https://github.com/greatscottgadgets/cynthion-test) | Python | 10 | 2026-08-21 | BSD-3-Clause | amaranth/apollo/dfu-util | Factory test software (drives selftest gateware) | partial (15 .py) @385ff43667 | no |
| [greatscottgadgets/facedancer](https://github.com/greatscottgadgets/facedancer) | Python | 1021 | 2026-05-22 | BSD-3-Clause | n/a (host) | Host-side Python USB-device emulation library; the Cynthion backend talks to the Moondancer gateware in the `cynthion` repo. No gateware here | unverified as gateware (57 .py, no HDL) @9f1298856e | no |
| [greatscottgadgets/luna-boards](https://github.com/greatscottgadgets/luna-boards) | Python (Amaranth) | 2 | 2023-08-07 | BSD-3-Clause | amaranth | Old LUNA board files (incl. ECPIX-5), UNMAINTAINED | partial (20 .py) @fda761ced6 | no |
| [antoinevg/cynthion-tutorials](https://github.com/antoinevg/cynthion-tutorials) | Python (Amaranth) | 4 | 2025-01-13 | BSD-3-Clause | amaranth (apollo / openFPGALoader) | Tutorials: I2S (`cynthion_i2s.py`), SoC with VexRiscv, platforms for Cynthion and ECPIX-5 (+ ECPIX-5 with LUNA) | partial (54 .py, 5 v) @8b711adb4c | no |
| [antoinevg/cynthion-litex](https://github.com/antoinevg/cynthion-litex) | Python (LiteX), Rust | 1 | 2023-05-15 | none | litex (yosys, apollo) | LiteX platform/target `gsg_cynthion` + Rust hello firmware | partial (8 .py) @fba84fef4a | no |
| [VoltCyclone/HurricaneFPGA](https://github.com/VoltCyclone/HurricaneFPGA) | Verilog (+ legacy Amaranth) | 8 | 2026-04-23 | MIT | open (yosys/nextpnr-ecp5/ecppack; dfu-util/openFPGALoader) | Plain-Verilog USB FS/LS passthrough TARGET<->CONTROL, monitoring, USB host mode (enumeration + HID keyboard), HID injection over UART; legacy LUNA version. README claims working (CI badge points to ramseymcgrath/HurricaneFPGA, the previous owner) | verified (`cynthion_pins.lpf`, 31 v/sv) @6f0b109cf0 | no |
| [VoltCyclone/hurra-fpga](https://github.com/VoltCyclone/hurra-fpga) | Python (Amaranth on LUNA) | 2 | 2026-09-25 | MIT | open (yosys/nextpnr-ecp5/ecppack) | HS USB HID relay: host on TARGET-A (chirp, enumeration, interrupt IN polling), device clone on AUX, report mutation, debug registers | partial (64 .py) @0a050ad254 | no |
| [KarpelesLab/usbmagic-gateware](https://github.com/KarpelesLab/usbmagic-gateware) | Python (Amaranth) | 0 | 2026-06-25 | NOASSERTION | amaranth (Docker oss-cad-suite) | Goal USB 2.0 host controller; currently Phase-0 blinky only (WIP) | partial (4 .py) @338ab88d73 | no |
| [nchie/cynthionwhisperer](https://github.com/nchie/cynthionwhisperer) | Python, Rust | 0 | 2026-03-27 | none | amaranth | Modified analyzer protocol/gateware exposing a Python API | partial (26 .py) @e77b99598d | no |
| [awtoau/cynthion-workspace](https://github.com/awtoau/cynthion-workspace) | Verilog, Python | 0 | 2026-08-14 | none | mixed (incl. Diamond script) | Workspace with submodules, CPU-probe Verilog gateware with lpf, forks of cynthion/facedancer/luna-soc (awtoau/awto-*) | verified (5 lpf, 49 v/sv) @6e46cd267c | no |
| [apfaudio/guh](https://github.com/apfaudio/guh) | Python (Amaranth) | 12 | 2026-09-07 | BSD-3-Clause | amaranth | USB2 HS/FS **host engine** library (SIE, enumeration, mass-storage / HID / MIDI hosts); built for Tiliqua, README mentions Cynthion | partial (31 .py) @9aa0fd3511 | no |
| [apfaudio/tiliqua](https://github.com/apfaudio/tiliqua) | Python (Amaranth) | 165 | 2026-09-23 | CERN-OHL-S-2.0 | amaranth | Eurorack audio multitool on its own ECP5 SoM (soldiercrab), LUNA-based; README mentions Cynthion (not a Cynthion target) | partial (111 .py) @ec9bf46022 | no |
| [key2/luna-ss](https://github.com/key2/luna-ss) | Python (Amaranth) | 0 | 2026-09-07 | BSD-3-Clause | amaranth | LUNA fork: SuperSpeed Gen1/Gen2 device stack on a Gowin USB3 PHY (not ECP5 / not Cynthion) | partial | no |

Host-side only (no gateware, noted for completeness): greatscottgadgets/packetry (Rust analyzer UI, 290 stars),
Oliver0804/cynthion-mcp, jsdratm/CynthionScripts, compr00t/Cynthion, epozzobon/cynthion-dump, graynode/packetty,
da1sy/USBForge, ma-tcha/hid-waterfall, terrafirma2021/kmboxetry, icewind1991/cynthion-flake,
greatscottgadgets/tycho (production test jig hardware), greatscottgadgets/saturn-v (SAMD bootloader for Apollo).
`cynthion fork:only` returned 159 forks of cynthion/facedancer/packetry/cynthion-hardware; none showed own gateware
by name/description (Shadytel/cynthion is a fork with a policy note; not checked further).

## Findings

1. **TinyFPGA EX never reached customers.** Crowd Supply still says "launching soon" (last update 2019-03-17);
   only KiCad files and apio board stubs exist. No gateware, no litex-boards / amaranth-boards / openFPGALoader
   support. Nothing to clone.
2. **ECPIX-5 is well supported by frameworks** (LiteX platform+target with DDR3/RGMII/SATA/video; Amaranth
   platform 45F/85F; openFPGALoader r02/r03), but plain-Verilog gateware is thin: ultraembedded (SoC + DDR3),
   maxhpc (SV DDR3/UART) and blinkies. Most other ECPIX-5 use is as a *secondary* target of bigger projects
   (eurorack-pmod, orbtrace, accel2d, ElemRV, litecan).
3. **The best reusable ECPIX-5 block is ultraembedded/core_ddr3_controller** (637 stars): a small DDR3
   controller + ECP5 PHY with a ready ECPIX-5 example. Not cloned yet (only its user ecpix5-test / ecpix-5 is).
4. **Cynthion gateware is almost all Amaranth on LUNA.** The official `greatscottgadgets/cynthion` repo (analyzer,
   Moondancer/Facedancer SoC, selftest, platform files r0.1-r1.4) is the key missing clone. Facedancer itself is a
   host library; Apollo is MCU firmware.
5. **Community USB-host gateware is the active area in 2026**: HurricaneFPGA (plain Verilog, has a Cynthion
   `.lpf`), hurra-fpga (HS host + device relay on LUNA), apfaudio/guh (HS/FS host engine library),
   usbmagic-gateware (WIP).
6. Several ULX3S-relevant blocks show up: vernier-rv32 (ULX3S + ECPIX-5, already in the ULX3S survey), LUNA-based
   UAC2 (cynthion-uac, eurorack-pmod-usb-soundcard), guh (USB host on ULPI).

## Recommended to clone

Gateware only, none already in `sources.tsv`. 12 repos.

| # | repo | board | reason | status |
|---|---|---|---|---|
| 1 | [ultraembedded/core_ddr3_controller](https://github.com/ultraembedded/core_ddr3_controller) | ECPIX-5 | Reusable Verilog DDR3 controller + ECP5 PHY, ECPIX-5 example with lpf; 637 stars | working (example verified by file list) |
| 2 | [maxhpc/ecpix-5](https://github.com/maxhpc/ecpix-5) | ECPIX-5 | Plain SV designs (UART, DDR3 top, FIFOs) with open-flow Makefiles and a Verilator testbench | unverified (file list only) |
| 3 | [apfaudio/eurorack-pmod](https://github.com/apfaudio/eurorack-pmod) | ECPIX-5 | Verilog audio-codec + DSP cores, multi-board with an ECPIX-5 lpf; 239 stars | working (per README) |
| 4 | [orbcode/orbtrace](https://github.com/orbcode/orbtrace) | ECPIX-5 | Cortex-M SWD/TRACE probe gateware; ECPIX-5 platform in-tree; 181 stars | working (per README) |
| 5 | [openconcepts-ar/accel2d](https://github.com/openconcepts-ar/accel2d) | ECPIX-5 | C-to-Verilog 2D graphics accelerators on DRAM in LiteX, ECPIX-5 default target, active 2026-09 | WIP |
| 6 | [greatscottgadgets/cynthion](https://github.com/greatscottgadgets/cynthion) | Cynthion | Official gateware (USB analyzer, Moondancer/Facedancer SoC, selftest) + all platform revisions | working |
| 7 | [greatscottgadgets/luna-soc](https://github.com/greatscottgadgets/luna-soc) | Cynthion | Amaranth SoC library used by Moondancer; bundled VexRiscv Verilog | working |
| 8 | [greatscottgadgets/cynthion-uac](https://github.com/greatscottgadgets/cynthion-uac) | Cynthion | Small official USB Audio Class 2 gateware example (NCO, DSP, DAC) | unverified (example) |
| 9 | [antoinevg/cynthion-tutorials](https://github.com/antoinevg/cynthion-tutorials) | Cynthion + ECPIX-5 | Amaranth tutorials (I2S, SoC) with platforms for both boards | working (per README) |
| 10 | [VoltCyclone/HurricaneFPGA](https://github.com/VoltCyclone/HurricaneFPGA) | Cynthion | Plain-Verilog USB passthrough + USB host with a Cynthion lpf; reusable without Amaranth | working (per README) |
| 11 | [VoltCyclone/hurra-fpga](https://github.com/VoltCyclone/hurra-fpga) | Cynthion | HS USB host + device relay on LUNA, active 2026-09 | WIP |
| 12 | [apfaudio/guh](https://github.com/apfaudio/guh) | Cynthion (Tiliqua) | Amaranth USB2 HS/FS host engine library (MSC/HID/MIDI) | WIP (per README) |

Not recommended: tinyfpga/TinyFPGA-EX and zeldin/TinyCartridgeEX (hardware only); ultraembedded/ecpix5-test
(duplicate of the DDR3 example in #1); greatscottgadgets/facedancer and apollo (host library / MCU firmware);
KarpelesLab/usbmagic-gateware (blinky only so far).

## Gaps

- Code search (`extension:lpf` + board pin names) needs authentication; repos that never name the board in
  name/description/README are missed.
- TinyFPGA EX "never shipped" rests on the Crowd Supply page state on 2026-09-28; no statement from the author was found.
- ECPIX-5 Ethernet PHY part and HDMI transmitter part were not read from the schematic PDFs.
- Status "working" for Amaranth/LiteX repos is from READMEs; nothing was built.
{% endraw %}
