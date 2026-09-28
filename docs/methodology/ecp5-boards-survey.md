---
title: "ECP5 boards survey"
parent: "Methodology"
nav_order: 2
---
<!-- Generated from data/pages/ecp5-boards-survey.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# ECP5 (non-ULX3S) gateware survey on GitHub

Survey date: 2026-09-27. Research only: nothing cloned. Scope: Lattice ECP5 boards other than
ULX3S / ULX4M / ULX5M (those are in `docs/github-survey.md`); iCE40, Gowin and Xilinx-only repos excluded.
702 unique repos came back from 53 searches. After removing forks, empty repos, off-topic matches
and ULX*/iCE40/Gowin/Xilinx hits, **114 repos** are listed below.

**Evidence column**

- `verified (...)`: the full recursive file list was read at the shown commit. It contains a
  `.lpf` constraint file (or the `.pcf`-named LPF used by OrangeCrab/ButterStick) and HDL sources.
  When a Makefile was found, its build commands were read for `yosys` / `nextpnr-ecp5` / `ecppack`.
- `partial`: Python/Amaranth/LiteX sources were seen but no `.lpf` file. Pins come from a framework
  board file, so this is normal for LiteX and Amaranth.
- `unverified`: name or README only, or the file list shows no constraints or HDL.
- Toolchain `open` means the Makefile, build.sh or README calls yosys + nextpnr-ecp5 + ecppack.
  `(README flow)` means the README states it but no Makefile was found.

**Framework board files (noted once, not counted as projects)**

- `litex-hub/litex-boards` (BSD-2-Clause, pushed 2026-09-24), platforms: `gsd_orangecrab`, `gsd_butterstick`,
  `hackaday_hadbadge`, `muselab_icesugar_pro`, `colorlight_5a_75b`, `colorlight_5a_75e`, `colorlight_i5`,
  `colorlight_i5a_907`, `colorlight_i9plus`, `lambdaconcept_ecpix5`, `logicbone`, `lattice_ecp5_evn`,
  `lattice_ecp5_vip`, `lattice_versa_ecp5`, `trellisboard`, `icepi_zero` (verified by file list).
- `amaranth-lang/amaranth-boards`: `orangecrab_r0_1`, `orangecrab_r0_2`, `butterstick`, `supercon19badge`,
  `icesugar_pro`, `colorlight_5a75b_r7_0`, `ecpix5`, `logicbone`, `versa_ecp5`, `versa_ecp5_5g`,
  `ecp5_5g_evn`, `icepi_zero` (verified by file list).
- `greatscottgadgets/luna-boards` (LUNA/Cynthion board definitions, Amaranth).
- Hardware-only repos (no gateware), for reference: orangecrab-fpga/orangecrab-hardware (546 stars),
  butterstick-fpga/butterstick-hardware, greatscottgadgets/cynthion-hardware, oskirby/logicbone,
  tinyfpga/TinyFPGA-EX, Spritetm/hadbadge2019_pcb, joshajohnson/ecp5-mini, pergola-fpga/pergola.
- Bootloaders: gregdavill/foboot is a **fork** (OrangeCrab DFU bootloader branch, LiteX), so it is not listed.

## OrangeCrab (gregdavill / orangecrab-fpga, ECP5 25F/85F)

| repo | language/HDL | stars | last push | license | toolchain | what the gateware does | evidence |
|---|---|---|---|---|---|---|---|
| [orangecrab-fpga/orangecrab-examples](https://github.com/orangecrab-fpga/orangecrab-examples) | Verilog, C | 111 | 2024-05-07 | MIT | open | Official examples: Verilog blink/PWM/USB-ACM + LiteX/RISC-V C examples (constraints as orangecrab_r0.x .pcf) | verified (3 lpf/pcf, 10 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @eefbafa872 |
| [ultraembedded/orangecrab](https://github.com/ultraembedded/orangecrab) | Verilog | 9 | 2020-08-21 | Apache-2.0 | open (lpf+Verilog; no Makefile found) | DDR3 test: ultraembedded DDR3 AXI controller + DFI PHY for ECP5, ram tester | verified (1 lpf/pcf, 12 v/sv) @685d601556 |
| [emeb/orangecrab_simple_6502](https://github.com/emeb/orangecrab_simple_6502) | Verilog | 7 | 2020-07-17 | MIT | open | Minimal 6502 system (CPU, RAM/ROM, ACIA) on OrangeCrab | verified (1 lpf/pcf, 6 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @4abeb827a6 |
| [emeb/orangecrab_adc](https://github.com/emeb/orangecrab_adc) | Verilog, Python | 7 | 2020-08-18 | none | open | ADC/audio FeatherWing gateware for SDR experiments (verilog/trellis flow) | verified (1 lpf/pcf, 16 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @daa94e19ab |
| [fdarling/orangecrab-usb-cdc-demo](https://github.com/fdarling/orangecrab-usb-cdc-demo) | Verilog | 3 | 2022-10-03 | Apache-2.0 | open | USB CDC-ACM virtual COM port open core on OrangeCrab | verified (1 lpf/pcf, 3 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @36a88f010f |
| [mangelajo/orangecrab-usb](https://github.com/mangelajo/orangecrab-usb) | Verilog | 1 | 2024-02-25 | none | open | USB device examples based on FPGA-USB-Device core | verified (1 lpf/pcf, 4 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @c4a8293fcd |
| [tallenintegsys/hdmi-orangecrab](https://github.com/tallenintegsys/hdmi-orangecrab) | SystemVerilog | 1 | 2024-07-07 | none | open | Port of Sameer Puri HDMI IP (video) to OrangeCrab 85F | verified (1 lpf/pcf, 14 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @59436568a4 |
| [tallenintegsys/usbTim](https://github.com/tallenintegsys/usbTim) | Verilog | 0 | 2023-07-01 | none | open | Base USB peripheral implementation (OrangeCrab pcf) | verified (1 lpf/pcf, 14 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @bfee3fcacd |
| [tommythorn/OrangeCrab_Hello](https://github.com/tommythorn/OrangeCrab_Hello) | Verilog | 2 | 2020-03-19 | Unlicense | open | Hello world: LED + serial IO | verified (1 lpf/pcf, 3 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @ffb42ed5a9 |
| [samblenny/ocfpga](https://github.com/samblenny/ocfpga) | SystemVerilog/Verilog | 2 | 2024-05-03 | none | open | Experiments series (blink, UART, picorv32, low-power) | verified (2 lpf/pcf, 8 v/sv, Makefile: ecppack/nextpnr-ecp5/py/yosys) @376719c98a |
| [FormerLab/ck37-core](https://github.com/FormerLab/ck37-core) | Verilog | 12 | 2026-09-10 | MIT | open | Soft-core replica of the Saab CK37 airborne computer on OrangeCrab | verified (2 lpf/pcf, 9 v/sv, Makefile: ecppack/nextpnr-ecp5/py/yosys) @6579d0da8e |
| [Moonnight1027/Eyeriss-ECP5](https://github.com/Moonnight1027/Eyeriss-ECP5) | SystemVerilog | 0 | 2026-09-19 | MIT | open (build.sh) | Eyeriss row-stationary CNN accelerator on OrangeCrab | verified (1 lpf/pcf, 37 v/sv) @890465b570 |
| [fdarling/orangecrab-bad-reset-timer](https://github.com/fdarling/orangecrab-bad-reset-timer) | Verilog | 0 | 2025-03-20 | none | open | Small reset-timer utility design | verified (1 lpf/pcf, 4 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @91cf09fce4 |
| [onsdagens/orangecrab-ecp5-dram](https://github.com/onsdagens/orangecrab-ecp5-dram) | Verilog | 0 | 2025-05-20 | none | open | DRAM template/experiment (lpf + 1 Verilog file) | verified (1 lpf/pcf, 1 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @f5516c7aa2 |
| [onsdagens/orangecrab-ecp5-example](https://github.com/onsdagens/orangecrab-ecp5-example) | n/a | 0 | 2025-04-22 | none | open | Template project (lpf + Makefile, HDL not in .v) | verified-constraints (1 lpf, no HDL files) @1be111df3d |
| [LuFore/OrangeCrab-VHDL-Blinky](https://github.com/LuFore/OrangeCrab-VHDL-Blinky) | VHDL | 1 | 2025-05-10 | CERN-OHL-S-2.0 | open (ghdl-yosys) | VHDL blinky | verified (1 lpf/pcf, 0 v/sv, 1 vhd, Makefile: ecppack/nextpnr-ecp5/yosys) @4c3bd577cc |
| [orangecrab-fpga/production-test-sw](https://github.com/orangecrab-fpga/production-test-sw) | Python | 10 | 2024-02-28 | MIT | litex | Production test gateware/firmware (ATE) | partial (6 .py, 0 HDL, no lpf) @70eaca4e4a |
| [cr1901/orangecrab-feather](https://github.com/cr1901/orangecrab-feather) | Python | 0 | 2022-03-08 | none | litex | LiteX SoC using the Feather pins | partial (6 .py, 0 HDL, no lpf) @9784b14106 |
| [ASukhanov/OrangeCrab_gateware](https://github.com/ASukhanov/OrangeCrab_gateware) | Python | 0 | 2022-11-28 | MIT | litex | Unofficial LiteX gateware projects | partial (4 .py, 0 HDL, no lpf) @7dd994d840 |
| [azzeloof/orangecrab-litex-blink](https://github.com/azzeloof/orangecrab-litex-blink) | Python | 0 | 2020-10-25 | none | litex | LiteX blink | partial (7 .py, 0 HDL, no lpf) @ed53ee8fb4 |
| [TiltMeSenpai/orangecrab_sketches](https://github.com/TiltMeSenpai/orangecrab_sketches) | Python | 0 | 2020-08-03 | none | amaranth/litex (py only) | Sketches in Python HDL | partial (12 .py, 0 HDL, no lpf) @cc621f7ff4 |
| [google/CFU-Playground](https://github.com/google/CFU-Playground) | Verilog, Python | 568 | 2026-02-26 | Apache-2.0 | litex | ML custom-function-unit framework; OrangeCrab is one supported target (many course forks exist, ignored) | unverified |
| [antonblanchard/microwatt](https://github.com/antonblanchard/microwatt) | VHDL | 725 | 2026-08-12 | NOASSERTION | open (ghdl-yosys) | OpenPOWER VHDL softcore; OrangeCrab among supported boards | unverified |

## LUNA / Cynthion (Great Scott Gadgets, ECP5 LFE5U-12F)

| repo | language/HDL | stars | last push | license | toolchain | what the gateware does | evidence |
|---|---|---|---|---|---|---|---|
| [greatscottgadgets/luna](https://github.com/greatscottgadgets/luna) | Python (Amaranth) | 1140 | 2026-08-19 | BSD-3-Clause | amaranth | USB 2.0/3.0 device/host/analyzer gateware framework; includes one plain-Verilog blinky example with .lpf | verified (1 lpf/pcf, 1 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @82a8f73329 |
| [greatscottgadgets/cynthion](https://github.com/greatscottgadgets/cynthion) | Python (Amaranth), Rust | 199 | 2026-05-22 | BSD-3-Clause | amaranth | Cynthion gateware (analyzer, facedancer, SoC) + host tools | partial (75 .py, 0 HDL, no lpf) @dd2340e20d |
| [greatscottgadgets/luna-soc](https://github.com/greatscottgadgets/luna-soc) | Python (Amaranth) | 31 | 2025-10-31 | BSD-3-Clause | amaranth | Amaranth library for USB-capable SoC designs (VexRiscv Verilog bundled) | partial (36 .py, 5 HDL, no lpf) @7fa1cc16dd |
| [antoinevg/cynthion-tutorials](https://github.com/antoinevg/cynthion-tutorials) | Python (Amaranth) | 4 | 2025-01-13 | BSD-3-Clause | amaranth | Cynthion gateware tutorials | partial (54 .py, 5 HDL, no lpf) @8b711adb4c |
| [gregdavill/luna-usb-serial-acm](https://github.com/gregdavill/luna-usb-serial-acm) | Verilog (generated) | 3 | 2026-06-04 | BSD-2-Clause | amaranth-generated | LUNA USB serial ACM exported as a standalone Verilog module (reusable in plain-Verilog designs) | partial (3 .py, 1 HDL, no lpf) @ef1d7dcb0d |
| [awtoau/cynthion-workspace](https://github.com/awtoau/cynthion-workspace) | Verilog, Python | 0 | 2026-08-14 | none | mixed | Workspace with submodules + Verilog CPU-probe gateware with .lpf for Cynthion | verified (5 lpf/pcf, 49 v/sv) @6e46cd267c |
| [KarpelesLab/usbmagic-gateware](https://github.com/KarpelesLab/usbmagic-gateware) | Python | 0 | 2026-06-25 | NOASSERTION | amaranth | USB 2.0 host controller gateware for Cynthion ECP5 (early phase) | partial (4 .py, 0 HDL, no lpf) @338ab88d73 |
| [nchie/cynthionwhisperer](https://github.com/nchie/cynthionwhisperer) | Python | 0 | 2026-03-27 | none | amaranth | Modified analyzer gateware exposing a Python API | partial (26 .py, 0 HDL, no lpf) @e77b99598d |
| [greatscottgadgets/cynthion-analyzer](https://github.com/greatscottgadgets/cynthion-analyzer) | Makefile | 6 | 2025-05-13 | none | amaranth | Integration repo for the analyzer mode | partial (1 .py, 0 HDL, no lpf) @2924a83070 |

## iCESugar-Pro (Muse Lab, ECP5 LFE5U-25F SODIMM module)

| repo | language/HDL | stars | last push | license | toolchain | what the gateware does | evidence |
|---|---|---|---|---|---|---|---|
| [wuxx/icesugar-pro](https://github.com/wuxx/icesugar-pro) | Verilog | 217 | 2025-09-16 | none | open | Vendor repo: blink, HDMI test pattern, SDRAM etc. examples + docs | verified (5 lpf/pcf, 13 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @087e48d9e0 |
| [yodalee/icesugar-playground](https://github.com/yodalee/icesugar-playground) | SystemVerilog/Verilog | 7 | 2026-09-14 | NOASSERTION | open | Personal projects: blink, UART, HDMI, ... (7 Makefiles) | verified (5 lpf/pcf, 32 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @9d1416b6a2 |
| [mebner86/icesugar-pro_sound2fft](https://github.com/mebner86/icesugar-pro_sound2fft) | Verilog | 1 | 2026-04-03 | MIT | open | I2S mic -> FFT spectrum analyzer on HDMI, step-by-step project series (17 .lpf) | verified (17 lpf/pcf, 56 v/sv, Makefile: py) @9b513e33c6 |
| [mebner86/icesugar-pro_diy-anc](https://github.com/mebner86/icesugar-pro_diy-anc) | Verilog | 0 | 2026-02-24 | MIT | open | Active noise cancellation with PDM mics/amps (early: blinky) | verified (1 lpf/pcf, 3 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @f30a0d27ff |
| [UCR-CS122A/icesugar-pro-framebuffer](https://github.com/UCR-CS122A/icesugar-pro-framebuffer) | Verilog | 0 | 2026-05-27 | none | open | SDRAM-backed framebuffer with test pattern (course repo; Joashy7/icesugar-pro-framebuffer_device is a derivative) | verified (1 lpf/pcf, 8 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @f1dd998219 |
| [robinsonb5/IceSugar-Pro_Tests](https://github.com/robinsonb5/IceSugar-Pro_Tests) | VHDL | 6 | 2022-05-31 | GPL-3.0 | open (ghdl-yosys) | Test/demo projects exploring Yosys/Trellis | verified (1 lpf/pcf, 1 v/sv, 9 vhd, Makefile: ecppack/nextpnr-ecp5/yosys) @3518d8d29b |
| [robinsonb5/Minimig_Lattice](https://github.com/robinsonb5/Minimig_Lattice) | Verilog, VHDL | 4 | 2026-07-18 | GPL-3.0 | diamond + open (per README Diamond) | MiST Minimig (Amiga) core ported to iCESugar-Pro and FleaFPGA Ohm | verified (2 lpf/pcf, 207 v/sv, 74 vhd) @c1e7280f12 |
| [jmio/ECP5_Brieysoc](https://github.com/jmio/ECP5_Brieysoc) | Verilog (generated) | 9 | 2022-03-26 | none | open (SpinalHDL-generated) | SpinalHDL Briey SoC (VexRiscv) generated Verilog on iCESugar-Pro | verified (1 lpf/pcf, 2 v/sv, Makefile: py) @c4ac18d810 |
| [fabbrimichele/rt68ice](https://github.com/fabbrimichele/rt68ice) | VHDL, Verilog | 0 | 2026-09-27 | MIT | open | RT68 (68000 retro computer) iCESugar-Pro version | verified (1 lpf/pcf, 7 v/sv, 6 vhd, Makefile: ecppack/nextpnr-ecp5/py/yosys) @da6b496018 |
| [Raptor-X102-embd/FPGA-led-buttons-test](https://github.com/Raptor-X102-embd/FPGA-led-buttons-test) | SystemVerilog | 0 | 2026-08-24 | none | open | First LED/button test | verified (1 lpf/pcf, 6 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @1344b89eb3 |

## Hackaday Supercon 2019 badge (ECP5 LFE5U-45F)

| repo | language/HDL | stars | last push | license | toolchain | what the gateware does | evidence |
|---|---|---|---|---|---|---|---|
| [Spritetm/hadbadge2019_fpgasoc](https://github.com/Spritetm/hadbadge2019_fpgasoc) | Verilog, C | 167 | 2023-11-30 | NOASSERTION | open | Official badge SoC: dual PicoRV32, video/LCD, audio synth, PSRAM, USB; apps (27 Makefiles) | verified (6 lpf/pcf, 95 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @6e706d52ec |
| [hexagon5un/hackaday_supercon_2019_logic_noise_FPGA_workshop](https://github.com/hexagon5un/hackaday_supercon_2019_logic_noise_FPGA_workshop) | Verilog | 29 | 2019-11-20 | none | open | Logic Noise audio synthesis workshop (oscillators, filters, DAC) | verified (3 lpf/pcf, 22 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @1297ac5f31 |
| [esden/hadbadge2019_workshops](https://github.com/esden/hadbadge2019_workshops) | Verilog, C | 49 | 2019-12-07 | none | open | Workshop materials incl. advanced SoC exercise | verified (1 lpf/pcf, 2 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @b3abb63e56 |
| [esden/hadbadge2019_fpga](https://github.com/esden/hadbadge2019_fpga) | Verilog | 3 | 2019-11-24 | none | open | Small HDL examples: RGB LED, 7-seg PMOD | verified (2 lpf/pcf, 2 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @646b8838df |
| [gregdavill/linux-on-litex-hadbadge](https://github.com/gregdavill/linux-on-litex-hadbadge) | n/a | 7 | 2020-03-24 | none | litex | Prebuilt linux-on-litex images (binaries only) | unverified (6 files, no lpf/HDL) @259e20bc98 |

## Colorlight 5A-75B / 5A-75E / i5 / i9 (ECP5 25F/45F)

| repo | language/HDL | stars | last push | license | toolchain | what the gateware does | evidence |
|---|---|---|---|---|---|---|---|
| [wuxx/Colorlight-FPGA-Projects](https://github.com/wuxx/Colorlight-FPGA-Projects) | Verilog | 366 | 2026-09-15 | Apache-2.0 | open | Vendor-style examples for 5A-75B v7.0, i5, i9, i9plus (blink, UART, ...) + docs | verified (13 lpf/pcf, 34 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @5042201f6a |
| [kholia/Colorlight-5A-75B](https://github.com/kholia/Colorlight-5A-75B) | Verilog | 58 | 2026-02-26 | none | open | Notes + projects: blink, DDS/SSB radio, Docker build flow | verified (6 lpf/pcf, 18 v/sv, Makefile: ecppack/nextpnr-ecp5/py/yosys) @9d4433be7c |
| [sam210723/fpga](https://github.com/sam210723/fpga) | Verilog, VHDL | 48 | 2024-05-13 | MIT | open | Multi-board collection; Colorlight 5A-75B projects (also iCE40 boards) | verified (12 lpf/pcf, 75 v/sv, 8 vhd, Makefile: nextpnr-ecp5/yosys) @b157047ddc |
| [Martoni/MartoniColorlight](https://github.com/Martoni/MartoniColorlight) | Verilog | 8 | 2020-08-21 | none | open | 5A-75B projects: blink, servo, pads (7 designs) | verified (7 lpf/pcf, 13 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @1461fa3823 |
| [lucysrausch/colorlight-led-cube](https://github.com/lucysrausch/colorlight-led-cube) | Verilog | 112 | 2023-01-11 | GPL-3.0 | open + liteeth | 64x64 LED cube driver (HUB75) over Ethernet with LiteEth core | verified (2 lpf/pcf, 6 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @ebac05e1fa |
| [polprog/my8051](https://github.com/polprog/my8051) | Verilog | 3 | 2022-09-27 | none | open | 8051 CPU implementation on 5A-75B | verified (1 lpf/pcf, 9 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @8e0b71ae6e |
| [polprog/colorlight_hello](https://github.com/polprog/colorlight_hello) | Verilog | 8 | 2023-03-25 | none | open | Hello-world blink for 5A-75B | verified (1 lpf/pcf, 1 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @eb2ef36bc7 |
| [racerxdl/colorlight-picorv32](https://github.com/racerxdl/colorlight-picorv32) | Verilog | 1 | 2021-02-28 | none | open | PicoRV32 SoC example for Colorlight i5 (+HUB75) | verified (1 lpf/pcf, 3 v/sv, Makefile: ecppack/nextpnr-ecp5/py/yosys) @73daf2842c |
| [DatanoiseTV/colorlight-i9-aes67](https://github.com/DatanoiseTV/colorlight-i9-aes67) | Verilog | 1 | 2026-04-06 | MIT | open | Hardware-offloaded AES67 audio-over-IP + management softcore (i9) | verified (1 lpf/pcf, 37 v/sv, Makefile: ecppack/nextpnr-ecp5/py/yosys) @71420b772d |
| [dvcirilo/colorlight-i9-examples](https://github.com/dvcirilo/colorlight-i9-examples) | Verilog | 4 | 2025-11-20 | none | open | i9 examples: blink, matrix keyboard, pinout identifier, ... | verified (6 lpf/pcf, 31 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @73179526f1 |
| [nickspiker/colorlight-5a-75b](https://github.com/nickspiker/colorlight-5a-75b) | Verilog | 0 | 2026-06-19 | none | open (no Makefile; README flow) | 5A-75B v8 drivers/tools, OLED framebuffer test | verified (5 lpf/pcf, 22 v/sv) @79e67b64f6 |
| [nickspiker/colorlight-ecp5-tools](https://github.com/nickspiker/colorlight-ecp5-tools) | Verilog | 0 | 2026-03-22 | none | open (no Makefile; README flow) | RTL tools/demos incl. pin scan (sibling of the above) | verified (3 lpf/pcf, 18 v/sv) @b27de91f40 |
| [kittennbfive/5A-75B-tools](https://github.com/kittennbfive/5A-75B-tools) | Verilog | 23 | 2023-10-20 | AGPL-3.0 | open (README flow) | Tools/notes for 5A-75B v7.0: hello world, inputs, SDRAM | verified (3 lpf/pcf, 2 v/sv) @e544577255 |
| [tvlad1234/violet](https://github.com/tvlad1234/violet) | Verilog | 6 | 2025-02-22 | none | open | Virtual I/O for FPGAs (host-controlled I/O), Colorlight example | verified (1 lpf/pcf, 5 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @17bbe1675c |
| [Keksgesicht/Colorlight-i5-FPGA-Projects](https://github.com/Keksgesicht/Colorlight-i5-FPGA-Projects) | Verilog | 2 | 2022-04-17 | GPL-3.0 | open | i5 projects incl. HDMI Tetris | verified (1 lpf/pcf, 7 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @ab146869e3 |
| [Norman-w/fpga-ecp5-sine-wave](https://github.com/Norman-w/fpga-ecp5-sine-wave) | Verilog | 0 | 2025-11-30 | none | open | DDS sine generator on i5 | verified (1 lpf/pcf, 5 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @21e286bfa0 |
| [wel97459/Colorlight_v8.0_ECP5_Make](https://github.com/wel97459/Colorlight_v8.0_ECP5_Make) | Verilog | 0 | 2023-03-28 | Apache-2.0 | open | Basic Makefile template for 5A-75B v8.0 | verified (1 lpf/pcf, 2 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @be188eae7f |
| [roby2014/ecp5-ft232rl-example](https://github.com/roby2014/ecp5-ft232rl-example) | Verilog, VHDL | 3 | 2023-01-12 | none | open | 5A-75E: Verilog/VHDL/SpinalHDL LED examples, JTAG via FT232RL | verified (3 lpf/pcf, 1 v/sv, 1 vhd, Makefile: ecppack/nextpnr-ecp5/yosys) @6cfd8e04e7 |
| [Javier97sm/Colorlight-i9-v7.2](https://github.com/Javier97sm/Colorlight-i9-v7.2) | Verilog | 0 | 2022-10-29 | none | open | Trivial designs on i9 v7.2 | verified (1 lpf/pcf, 1 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @3888eb89d3 |
| [Open-Change/Colorlight-5A-75E_IO_test](https://github.com/Open-Change/Colorlight-5A-75E_IO_test) | Verilog | 0 | 2025-08-03 | none | litex? | 5A-75E IO test gateware (FoXCNC) | verified (1 lpf/pcf, 1 v/sv) @bde99e71f8 |
| [FPiorski/colorlight-i5-vhdl-examples](https://github.com/FPiorski/colorlight-i5-vhdl-examples) | VHDL | 2 | 2025-08-21 | CERN-OHL-W-2.0 | open (ghdl-yosys) | VHDL examples for i5 | verified (2 lpf/pcf, 0 v/sv, 32 vhd) @f894a90556 |
| [trabucayre/litexOnColorlightLab004](https://github.com/trabucayre/litexOnColorlightLab004) | Python | 38 | 2023-01-11 | none | litex | LiteX lab on 5A-75B (fpga_101 lab004) | partial (3 .py, 0 HDL, no lpf) @428bf89d74 |
| [siegeld/ledwall](https://github.com/siegeld/ledwall) | Python, Rust | 1 | 2026-09-21 | BSD-2-Clause | litex | LED video-wall driver: ECP5 gateware + no_std Rust | partial (74 .py, 0 HDL, no lpf) @8080b1f852 |
| [anarkiwi/reefervole](https://github.com/anarkiwi/reefervole) | Python | 0 | 2026-09-18 | Apache-2.0 | litex | 5A-75B v8.2 dev framework | partial (26 .py, 0 HDL, no lpf) @939286889b |
| [manoel-serafim/phantom](https://github.com/manoel-serafim/phantom) | Verilog | 1 | 2024-04-14 | MIT | unknown | 5-stage pipelined CPU with branch predictors (no .lpf in tree) | unverified (6 files, no lpf/HDL) @22ef79ac22 |

## ButterStick (gregdavill, ECP5 LFE5UM5G-85F)

| repo | language/HDL | stars | last push | license | toolchain | what the gateware does | evidence |
|---|---|---|---|---|---|---|---|
| [butterstick-fpga/verilog-examples](https://github.com/butterstick-fpga/verilog-examples) | Verilog | 1 | 2021-12-22 | none | open | Blink example (pcf/lpf + Makefile) | verified (1 lpf/pcf, 1 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @e0d2b76841 |
| [butterstick-fpga/butterstick-bootloader](https://github.com/butterstick-fpga/butterstick-bootloader) | Python, C | 14 | 2023-03-13 | BSD-2-Clause | litex | DFU bootloader SoC | partial (8 .py, 0 HDL, no lpf) @616e1be3c5 |
| [butterstick-fpga/example-litex-gpdi](https://github.com/butterstick-fpga/example-litex-gpdi) | Python | 6 | 2021-11-20 | BSD-2-Clause | litex | LiteX GPDI/HDMI example | partial (10 .py, 0 HDL, no lpf) @28dfa64e6a |
| [butterstick-fpga/dfu-runtime-soc](https://github.com/butterstick-fpga/dfu-runtime-soc) | Python | 2 | 2021-11-11 | BSD-2-Clause | litex | LiteX SoC with TinyUSB + LUNA DFU runtime | partial (8 .py, 0 HDL, no lpf) @3407f80497 |
| [gregdavill/ButterStick-projects](https://github.com/gregdavill/ButterStick-projects) | Python | 5 | 2020-08-28 | NOASSERTION | litex | Personal projects | partial (18 .py, 0 HDL, no lpf) @7c3a714b6e |
| [bboydt/ecp5-soc](https://github.com/bboydt/ecp5-soc) | Verilog | 0 | 2024-03-16 | none | open? (no Makefile) | Small SoC with ButterStick r1.0 constraints | verified (1 lpf/pcf, 11 v/sv, 1 vhd) @c630ae7568 |

## ECPIX-5 (LambdaConcept, ECP5 45F/85F)

| repo | language/HDL | stars | last push | license | toolchain | what the gateware does | evidence |
|---|---|---|---|---|---|---|---|
| [ultraembedded/ecpix-5](https://github.com/ultraembedded/ecpix-5) | Verilog | 15 | 2020-07-05 | none | open (lpf+Verilog; no Makefile found) | RISC-V (riscv_tcm_top) AXI4 SoC + DVI framebuffer via IT6613 HDMI transmitter; C drivers; submodules (.gitmodules) | verified (1 lpf/pcf, 19 v/sv) @17c1f633f1 |
| [ultraembedded/ecpix5-test](https://github.com/ultraembedded/ecpix5-test) | Verilog | 9 | 2020-08-20 | Apache-2.0 | open (lpf+Verilog; no Makefile found) | DDR3 test bitstream (ultraembedded DDR3 core) | verified (1 lpf/pcf, 12 v/sv) @2eaf689c60 |
| [maxhpc/ecpix-5](https://github.com/maxhpc/ecpix-5) | SystemVerilog | 0 | 2025-02-09 | none | open | ECPIX-5 designs (11 SV/V files, 6 Makefiles) | verified (1 lpf/pcf, 11 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @dbd64a102a |
| [Baldanos/ecpix5-blinky](https://github.com/Baldanos/ecpix5-blinky) | Verilog | 2 | 2021-02-10 | none | open | Blinky | verified (1 lpf/pcf, 1 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @b3f6104d74 |
| [goran-mahovlic/ECPIX5_blink](https://github.com/goran-mahovlic/ECPIX5_blink) | Verilog | 5 | 2020-12-18 | none | open (build.sh) | Blinky | verified (1 lpf/pcf, 1 v/sv) @0d9567fda2 |
| [lambdaconcept/ecpix5-bitsofcode](https://github.com/lambdaconcept/ecpix5-bitsofcode) | Python | 1 | 2020-07-07 | none | litex | Vendor code snippets | partial (3 .py, 0 HDL, no lpf) @83b4e04e7f |

## TinyFPGA EX / Logicbone / ECP5-EVN / Versa ECP5

| repo | language/HDL | stars | last push | license | toolchain | what the gateware does | evidence |
|---|---|---|---|---|---|---|---|
| [oskirby/logicbone-tests](https://github.com/oskirby/logicbone-tests) | Verilog, Python | 0 | 2020-07-19 | none | open | Logicbone test projects (Verilog + LiteX) | verified (1 lpf/pcf, 3 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @b8254bc7a1 |
| [xtrinch/fpga-bitcoin-miner](https://github.com/xtrinch/fpga-bitcoin-miner) | Verilog | 8 | 2022-04-02 | MIT | open | Bitcoin miner (SHA-256) for ECP5-EVN | verified (1 lpf/pcf, 12 v/sv, Makefile: ecppack/nextpnr-ecp5/py/yosys) @7c9ca1c377 |
| [gromero/ecp5](https://github.com/gromero/ecp5) | Verilog | 3 | 2021-04-20 | none | open | ECP5-EVN code: UART passthrough, raw serial | verified (4 lpf/pcf, 9 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @424ddf5c51 |
| [kazkojima/sha3-fpga](https://github.com/kazkojima/sha3-fpga) | Verilog | 2 | 2020-11-07 | MIT | open | SHA3 digest on ECP5-EVN (freecores/sha3) | verified (1 lpf/pcf, 3 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @471825dfb6 |
| [perillamint/ecp5-hd44780](https://github.com/perillamint/ecp5-hd44780) | Verilog | 0 | 2018-12-02 | BSD-3-Clause | open | HD44780 LCD driver on ECP5-EVN | verified (1 lpf/pcf, 5 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @36d612b143 |
| [ikskuh/ecp5-quickstart](https://github.com/ikskuh/ecp5-quickstart) | Verilog | 1 | 2021-12-31 | none | open (build.sh) | Blinky template w/ simulation, synthesis, programming (EVN) | verified (1 lpf/pcf, 5 v/sv) @ca20d3a1f5 |
| [onsdagens/lattice-ecp5-template](https://github.com/onsdagens/lattice-ecp5-template) | n/a | 0 | 2025-04-17 | none | open | EVN template (lpf + Makefile) | verified-constraints (1 lpf, no HDL files) @810b6dd779 |
| [sefbkn/versa-ecp5-demo](https://github.com/sefbkn/versa-ecp5-demo) | Verilog | 0 | 2026-03-14 | NOASSERTION | open | Gigabit Ethernet passthrough (RGMII/SGMII) on Versa ECP5 | verified (2 lpf/pcf, 31 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @1d6d4cb535 |
| [C-Elegans/ethernet](https://github.com/C-Elegans/ethernet) | Verilog | 3 | 2019-02-01 | none | open | Ethernet experiments on Versa ECP5 | verified (1 lpf/pcf, 14 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @da342f5cea |
| [gsomlo/yoloRISC](https://github.com/gsomlo/yoloRISC) | Verilog | 27 | 2019-08-23 | ISC | open | RocketChip rv64imac blinky on Versa ECP5 (yosys/nextpnr/trellis) | verified (1 lpf/pcf, 4 v/sv, Makefile: ecppack/nextpnr-ecp5/py/yosys) @d794a3625f |
| [kazkojima/litex-lattice-ecp5-evn](https://github.com/kazkojima/litex-lattice-ecp5-evn) | Python | 8 | 2021-05-25 | none | litex | LiteX files for EVN + SDRAM add-on + SGMII | partial (1 .py, 0 HDL, no lpf) @6c526658a7 |
| [tinyfpga/TinyFPGA-EX](https://github.com/tinyfpga/TinyFPGA-EX) | n/a | 78 | 2019-06-02 | NOASSERTION | n/a (hardware) | Board hardware only, no gateware | unverified (50 files, no lpf/HDL) @88fb9d455a |

## Other ECP5 boards / board-agnostic ECP5 cores

| repo | language/HDL | stars | last push | license | toolchain | what the gateware does | evidence |
|---|---|---|---|---|---|---|---|
| [cheyao/icepi-zero](https://github.com/cheyao/icepi-zero) | Verilog, VHDL | 827 | 2026-09-18 | NOASSERTION | open | IcePi Zero (Pi-Zero form ECP5 board): 24 gateware examples (blinky, HDMI, SDRAM, ...) | verified (24 lpf/pcf, 77 v/sv, 9 vhd, Makefile: ecppack/nextpnr-ecp5/yosys) @e01faa2bd3 |
| [m1nl/icepi-zero-minimig](https://github.com/m1nl/icepi-zero-minimig) | Verilog, VHDL | 8 | 2026-09-21 | GPL-3.0 | diamond/open | MiST Minimig AGA core for IcePi Zero (fork-lineage of robinsonb5/Minimig_Lattice) | verified (3 lpf/pcf, 225 v/sv, 74 vhd) @2c668725d5 |
| [danodus/ecp5_hdmi_audio_video](https://github.com/danodus/ecp5_hdmi_audio_video) | Verilog | 3 | 2026-05-19 | MIT | open | ECP5 HDMI audio+video transmitter (IcePi Zero, also ULX3S lpf) | verified (2 lpf/pcf, 21 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @a4710f9e79 |
| [joshajohnson/ecp5-mini-projects](https://github.com/joshajohnson/ecp5-mini-projects) | Verilog | 3 | 2021-08-29 | NOASSERTION | open | ECP5-Mini board projects (40 Verilog files) | verified (2 lpf/pcf, 40 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @4e8622882b |
| [tomverbeure/ecp5_jtag](https://github.com/tomverbeure/ecp5_jtag) | Verilog | 33 | 2021-07-23 | none | open | Use the ECP5 JTAG port (JTAGG) to talk to user logic (Colorlight i5 example) | verified (1 lpf/pcf, 5 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @6a2302e079 |
| [MichaelBell/tt-ecp5](https://github.com/MichaelBell/tt-ecp5) | Verilog | 2 | 2026-02-26 | Apache-2.0 | open | Tiny Tapeout ECP5 carrier-board gateware (many designs) | verified (11 lpf/pcf, 36 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @93873c629e |
| [cbalint13/e-verest](https://github.com/cbalint13/e-verest) | Verilog | 37 | 2023-04-12 | Apache-2.0 | open | EVEREST research stick (ECP5) test firmware | verified (1 lpf/pcf, 9 v/sv, Makefile: ecppack/nextpnr-ecp5/py/yosys) @a976e3954c |
| [dpavlin/trilby-hat-fpga](https://github.com/dpavlin/trilby-hat-fpga) | SystemVerilog | 2 | 2022-01-23 | none | open | Trilby HAT ECP5 SDR for Raspberry Pi | verified (1 lpf/pcf, 6 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @dd49ae9b84 |
| [robotique-ecam/ViveTracker](https://github.com/robotique-ecam/ViveTracker) | Verilog | 5 | 2022-05-07 | none | open | Lighthouse 2.0 tracking receivers | verified (1 lpf/pcf, 34 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @4ff899c38d |
| [badaboombox/SS-Handheld-Console](https://github.com/badaboombox/SS-Handheld-Console) | Verilog | 5 | 2026-08-19 | NOASSERTION | open (README flow) | Handheld game console with custom GPU | verified (1 lpf/pcf, 21 v/sv) @bc5a7680fc |
| [amin005/skywave_SDR](https://github.com/amin005/skywave_SDR) | Verilog | 0 | 2026-07-17 | BSD-3-Clause | open (README flow) | Direct-sampling HF SDR: AD9226 ADC + ULPI USB | verified (1 lpf/pcf, 17 v/sv) @15c6b23c46 |
| [mattvenn/basic-ecp5-pcb](https://github.com/mattvenn/basic-ecp5-pcb) | Verilog | 142 | 2021-07-17 | CC0-1.0 | open | Reference ECP5 PCB + test gateware | verified (1 lpf/pcf, 1 v/sv, Makefile: ecppack/nextpnr-ecp5/yosys) @f5ee05d1fb |
| [krynentechnology/sr2cb](https://github.com/krynentechnology/sr2cb) | Verilog | 2 | 2026-02-10 | NOASSERTION | unknown | Synchronous redundant ring channel bus; ECP5U/UM lpf | verified (2 lpf/pcf, 18 v/sv) @4ae58677c3 |
| [mehrdadh/lora-modulator](https://github.com/mehrdadh/lora-modulator) | Verilog | 48 | 2025-02-20 | NOASSERTION | diamond | LoRa modulator for AT86RF215 I/Q radio (TinySDR) | verified (5 lpf/pcf, 18 v/sv) @0f1016567d |
| [mehrdadh/fsk-modulator](https://github.com/mehrdadh/fsk-modulator) | Verilog | 11 | 2025-02-20 | NOASSERTION | diamond | FSK/BLE modulator for AT86RF215 (TinySDR) | verified (5 lpf/pcf, 32 v/sv, 5 vhd) @d5a6565710 |
| [jsloan256/titan_wiggle](https://github.com/jsloan256/titan_wiggle) | Verilog | 3 | 2015-10-07 | BSD-3-Clause | diamond | Titan PCIe card validation | verified (1 lpf/pcf, 5 v/sv) @98e6e468a7 |
| [C-Elegans/single_sdr](https://github.com/C-Elegans/single_sdr) | Verilog | 1 | 2019-10-28 | none | open | Single SDR channel on ECP5 (no lpf in tree) | unverified (15 files, no lpf/HDL) @018c83a7a9 |
| [ECP5-PCIe/ECP5-PCIe](https://github.com/ECP5-PCIe/ECP5-PCIe) | Python | 103 | 2023-05-16 | none | amaranth | PCIe core for ECP5 SERDES (mirror of Codeberg) | partial (71 .py, 0 HDL, no lpf) @c511d2eafa |

## Recommended to clone first (24)

**Status 2026-09-28:** all 24 are cloned and in the [catalogue](catalogue.md). Items 1–14 on 2026-09-27 (items 2 and 11 were already there from the ULX3S survey), item 21 (joshajohnson/ecp5-mini-projects) on request with kbeckmann/pergola_projects (its upstream), items 15–20 and 22–24 on 2026-09-28.

Priority goes to plain Verilog, the open toolchain, reusable cores and good board examples.

1. **Spritetm/hadbadge2019_fpgasoc**: the largest open-flow ECP5 SoC seen. Dual PicoRV32, LCD/video,
   audio synth, PSRAM (QSPI) controller and USB, with 27 Makefiles. The blocks can be reused on ULX3S.
2. **wuxx/Colorlight-FPGA-Projects**: vendor examples for 5A-75B, i5 and i9 (13 lpf). The most popular cheap ECP5 boards.
3. **wuxx/icesugar-pro**: vendor examples for iCESugar-Pro (HDMI, SDRAM, blink).
4. **orangecrab-fpga/orangecrab-examples**: official OrangeCrab examples in Verilog, including USB-ACM.
5. **ultraembedded/orangecrab**: standalone Verilog DDR3 AXI controller + DFI PHY for ECP5 (reusable).
6. **ultraembedded/ecpix-5**: ultraembedded RISC-V AXI4 SoC + DVI framebuffer (IT6613) on ECPIX-5, all Verilog.
7. **fdarling/orangecrab-usb-cdc-demo**: small pure-Verilog USB CDC-ACM core (reusable without LiteX).
8. **gregdavill/luna-usb-serial-acm**: LUNA USB-ACM exported as one Verilog module (reusable anywhere).
9. **mangelajo/orangecrab-usb**: Verilog USB device examples (FPGA-USB-Device).
10. **tallenintegsys/hdmi-orangecrab**: HDMI IP port for ECP5 in SystemVerilog.
11. **danodus/ecp5_hdmi_audio_video**: ECP5 HDMI transmitter with audio, active 2026.
12. **sefbkn/versa-ecp5-demo**: open-flow Gigabit Ethernet with RGMII + SGMII (rare SGMII on nextpnr).
13. **tomverbeure/ecp5_jtag**: JTAGG user-logic access, a reusable debug block.
14. **cheyao/icepi-zero**: 24 open-flow gateware examples for a popular new ECP5 board (827 stars, active).
15. **hexagon5un/hackaday_supercon_2019_logic_noise_FPGA_workshop**: Verilog audio/synth building blocks.
16. **emeb/orangecrab_adc**: ADC/audio SDR gateware on the open flow.
17. **mebner86/icesugar-pro_sound2fft**: I2S → FFT → HDMI in a step-by-step series (17 projects, 2026).
18. **DatanoiseTV/colorlight-i9-aes67**: AES67 audio-over-Ethernet on i9 (37 Verilog files, 2026).
19. **lucysrausch/colorlight-led-cube**: HUB75 LED driver + LiteEth core on 5A-75B (112 stars).
20. **kholia/Colorlight-5A-75B**: DDS/SSB radio + Docker open-flow recipes.
21. **joshajohnson/ecp5-mini-projects**: 40 Verilog files of open-flow examples.
22. **xtrinch/fpga-bitcoin-miner**: pipelined SHA-256 on ECP5-EVN (reusable hash core).
23. **greatscottgadgets/luna**: the reference USB framework (Amaranth). Ranked lower because it is not plain
    Verilog, but it is the only complete open USB 2.0/3.0 gateware stack for ECP5.
24. **racerxdl/colorlight-picorv32**: minimal PicoRV32 SoC + HUB75 on Colorlight i5.

## Queries run and gaps

Repository search API, unauthenticated, 7 s sleep between calls, per_page=100. The two largest result
sets (`orangecrab in:readme`, `project trellis`) also got page 2.
`orangecrab`(30), `topic:orangecrab`(2), `orangecrab in:readme`(132), `orangecrab verilog`(2),
`orangecrab language:verilog`(8), `orange crab fpga`(3), `icesugar-pro`(14), `icesugar_pro`(14),
`icesugarpro`(3), `icesugar pro ecp5`(3), `luna usb ecp5`(0), `luna greatscottgadgets`(1), `cynthion`(29),
`user:greatscottgadgets`(46), `user:gregdavill`(76), `user:orangecrab-fpga`(3), `user:butterstick-fpga`(10),
`hadbadge`(11), `supercon 2019 badge ecp5`(0), `hackaday badge ecp5`(0), `supercon badge fpga`(4),
`2019 badge fpga`(4), `colorlight 5a-75b`(27), `colorlight 5a-75e`(6), `colorlight i5`(21),
`colorlight i9`(23), `colorlight ecp5`(19), `topic:colorlight`(13), `5a-75b language:verilog`(8),
`butterstick`(8), `ecpix-5`(7), `ecpix5`(6), `tinyfpga ex`(7), `logicbone`(2), `versa ecp5`(5),
`ecp5 evaluation board`(5), `ecp5-evn`(5), `ecp5 verilog`(24), `nextpnr-ecp5`(18), `topic:ecp5`(59),
`topic:lattice-ecp5`(1), `ecp5 yosys`(28), `project trellis`(118, mostly the unrelated Roots "Trellis" PHP stack),
`ecp5 language:verilog`(80), `ecp5 language:systemverilog`(18), `lfe5u-25f`(0), `lfe5u-45f`(0),
`lfe5u-85f`(2), `ecp5 fpga`(158), `ecp5 hdmi`(8), `ecp5 sdram`(3), `ecp5 riscv`(8), `ecp5 usb verilog`(0).

Gaps and notes:

- No rate-limit errors (HTTP 403) on search. The core API was hardly used. File lists came from github.com's
  `tree/HEAD` + `tree-list/<oid>` JSON endpoints, which do not count against the 60/h API budget.
  Makefiles and READMEs came from raw.githubusercontent.com.
- Only the first 3 Makefiles of each repo were read for toolchain calls. A repo that builds from a
  script with another name shows no toolchain and is marked from its README.
- Code search (`extension:lpf`) was not used because it needs authentication. Repos whose name,
  description and README never mention the board are therefore missed.
- Forks that carry their own work were dropped along with trivial forks. Examples are the many
  CFU-Playground and microwatt forks, and gregdavill/foboot.
- Dropped as out of scope: lawrie/tinyfpga_examples (TinyFPGA BX, iCE40 `.pcf`),
  gmejiamtz/ecp5-project-template (ULX3S target), and any ULX3S/ULX4M/ULX5M(-GS) repos.
{% endraw %}
