# GitHub survey of ULX3S repositories (2026-09-27)

Candidates found by a GitHub-wide search that were **not yet** in `.claude/memory/sources.tsv`
on 2026-09-27. Produced with unauthenticated GitHub API repo search plus the root file listing of each repo,
with recursive trees checked for the top 47 repos. Not cloned yet unless listed in `sources.tsv`.
Method, limits and how to repeat it: `.claude/memory/source-lists.md`.

Evidence: `tree:` = path found in the recursive file tree; `root:` = found in the top-level listing only.

### A. Verified ULX3S gateware (ULX3S constraint/top/board dir found in repo tree or root listing) — 155 repos

| full_name | lang/HDL | stars | last push | license | what it is | evidence |
|---|---|---|---|---|---|---|
| [BrunoLevy/learn-fpga](https://github.com/BrunoLevy/learn-fpga) | Verilog | 3701 | 2025-11-18 | BSD-3-Clause | Learning FPGA, yosys, nextpnr, and RISC-V  | tree: Basic/ULX3S/ULX3S_SDRAM_hdmi/ulx3s.lpf |
| [darklife/darkriscv](https://github.com/darklife/darkriscv) | Verilog | 2613 | 2026-09-04 | BSD-3-Clause | opensouce RISC-V cpu core implemented in Verilog from scratc | tree: boards/ulx3s |
| [Wren6991/Hazard3](https://github.com/Wren6991/Hazard3) | Verilog | 1115 | 2026-08-29 | Apache-2.0 | 3-stage RV32IMACZb* processor with debug | tree: example_soc/synth/fpga_ulx3s.lpf |
| [wuxx/Colorlight-FPGA-Projects](https://github.com/wuxx/Colorlight-FPGA-Projects) | Verilog | 366 | 2026-09-15 | Apache-2.0 | current focus on Colorlight i5 and i9 & i9plus module | tree: src/i5/hdmi_test_pattern/ULX3S_25F.json |
| [lawrie/fpga_pio](https://github.com/lawrie/fpga_pio) | Verilog | 321 | 2024-06-06 | BSD-2-Clause | An attempt to recreate the RP2040 PIO in an FPGA | tree: ulx3s/ulx3s_v20.lpf |
| [sylefeb/a5k](https://github.com/sylefeb/a5k) | Silice | 293 | 2023-10-06 | none | Another World on a chip | tree: BITSTREAMs/ulx3s |
| [fusesoc/blinky](https://github.com/fusesoc/blinky) | Tcl | 198 | 2026-02-28 | MIT | Example LED blinking project for your FPGA dev board of choi | tree: ulx3s |
| [mit-plv/koika](https://github.com/mit-plv/koika) | Kôika→Verilog | 187 | 2025-12-10 | LGPL-2.1 | A core language for rule-based hardware design 🦑 | tree: examples/rv/etc/ulx3s_v20.lpf |
| [dan-rodrigues/icestation-32](https://github.com/dan-rodrigues/icestation-32) | Verilog | 168 | 2023-11-14 | MIT | Compact FPGA game console | tree: hardware/ulx3s/ulx3s_v20.lpf |
| [SpinalHDL/SaxonSoc](https://github.com/SpinalHDL/SaxonSoc) | SpinalHDL | 165 | 2025-03-16 | MIT | SoC based on VexRiscv and ICE40 UP5K | tree: hardware/synthesis/deprecated/ulx3s/ulx3s_v20_hdmi.lpf |
| [antonblanchard/chiselwatt](https://github.com/antonblanchard/chiselwatt) | Chisel | 117 | 2023-02-13 | NOASSERTION | A tiny POWER Open ISA soft processor written in Chisel | tree: constraints/ecp5-ulx3s.lpf |
| [carlosedp/chiselv](https://github.com/carlosedp/chiselv) | Chisel | 109 | 2026-09-14 | MIT | A RISC-V Core (RV32I) written in Chisel HDL | tree: constraints/ecp5-ulx3s.lpf |
| [stnolting/neorv32-setups](https://github.com/stnolting/neorv32-setups) | VHDL | 100 | 2026-09-12 | BSD-3-Clause | 📁 NEORV32 projects and exemplary setups for various FPGAs, b | tree: osflow/constraints/ULX3S.lpf |
| [JdeRobot/FPGA-robotics](https://github.com/JdeRobot/FPGA-robotics) | VHDL | 83 | 2024-07-14 | GPL-3.0 | Verilog library for developing robotics applications using F | tree: phys_fpga/ulx3s/apio/ov7670_rgb_yuv_320x240_colorfilter/ulx3s_v20.lpf |
| [BrunoLevy/TordBoyau](https://github.com/BrunoLevy/TordBoyau) | Verilog | 65 | 2023-12-01 | BSD-3-Clause | A pipelined RISC-V processor | tree: BOARDS/ulx3s.lpf |
| [machdyne/zeitlos](https://github.com/machdyne/zeitlos) | Verilog | 55 | 2026-09-27 | NOASSERTION | Zeitlos SOC/OS | tree: boards/ulx3s.lpf |
| [FPGAwars/FLIX-V](https://github.com/FPGAwars/FLIX-V) | Verilog | 42 | 2023-11-05 | LGPL-2.1 | FLIX-V: FPGA, Linux and RISC-V | tree: Hardware/KianV-Apio/ulx3s_v20.lpf |
| [StereoNinja/StereoNinjaFPGA](https://github.com/StereoNinja/StereoNinjaFPGA) | Verilog | 34 | 2023-05-15 | none | Experimental FPGA project for streaming two MIPI CSI camera  | root: DOCS_ULX3S |
| [egorxe/openglory](https://github.com/egorxe/openglory) | VHDL + LiteX | 33 | 2025-02-25 | Apache-2.0 | Open source GPU in VHDL | tree: hw/litex/radiona_ulx3s.py |
| [kulp/tenyr](https://github.com/kulp/tenyr) | C | 28 | 2026-08-15 | NOASSERTION | Simple, orthogonal 32-bit computer architecture and environm | tree: hw/yosys/ulx3s_v20.lpf |
| [dan-rodrigues/ics-adpcm](https://github.com/dan-rodrigues/ics-adpcm) | Verilog | 26 | 2020-12-28 | MIT | Programmable multichannel ADPCM decoder for FPGA | tree: demo/ulx3s_v20.lpf |
| [AngeloJacobo/ULX3S_FPGA_Camera_Streaming](https://github.com/AngeloJacobo/ULX3S_FPGA_Camera_Streaming) | Verilog (Icestudio) | 25 | 2021-11-17 | MIT | Verilog design files and Icestudio file for streaming the OV | root: OV7670_ULX3S.ice |
| [Speccery/icy99](https://github.com/Speccery/icy99) | Verilog | 22 | 2025-11-29 | none | TI-99/4A FPGA implementation for the Icestorm toolchain | tree: ulx3s.lpf |
| [AngeloJacobo/ULX3S_FPGA_Sobel_Edge_Detection_OV7670](https://github.com/AngeloJacobo/ULX3S_FPGA_Sobel_Edge_Detection_OV7670) | Verilog (Icestudio) | 21 | 2021-11-17 | MIT | Verilog design files and Icestudio file for Sobel Edge Detec | root: ULX3S_SOBEL.ice |
| [dan-rodrigues/mobile-fpga-bluetooth-demo](https://github.com/dan-rodrigues/mobile-fpga-bluetooth-demo) | Swift | 17 | 2020-12-12 | MIT | Simple BLE demo using an iOS app (SwiftUI), an ESP32 (Python | tree: rtl/ulx3s_v20.lpf |
| [daveshah1/prjtrellis-dvi](https://github.com/daveshah1/prjtrellis-dvi) | VHDL | 17 | 2019-01-20 | none | DVI video out example for prjtrellis | tree: constraints/ulx3s_v20_segpdi.lpf |
| [Circuit-killer/fpga-usbhid-host](https://github.com/Circuit-killer/fpga-usbhid-host) | VHDL | 15 | 2022-08-27 | none | FPGA state machine for minimalistic USB HID device hosting | tree: proj/lattice/constraints/ulx3s_v17patch.lpf |
| [ulx3s/blink](https://github.com/ulx3s/blink) | Makefile | 15 | 2022-05-16 | GPL-3.0 | Repository containing ULX3S blink LED binaries | root: ulx3s_v20.lpf |
| [q3k/ulx3s-foss-blinky](https://github.com/q3k/ulx3s-foss-blinky) | Verilog | 14 | 2018-11-11 | none | A template project for the ULX3S ECP5 FPGA board using only  | root: ulx3s |
| [mkvenkit/learn_fpga](https://github.com/mkvenkit/learn_fpga) | Verilog | 13 | 2026-07-19 | MIT | A collection of my FPGA projects and experiments. | tree: ecp5_ulx3s/uart_tx/ulx3s_v20.lpf |
| [rob-ng15/PAWSv2](https://github.com/rob-ng15/PAWSv2) | Silice | 13 | 2025-11-29 | MIT | — | tree: Programming Guide/Graphics/ULX3S-PAWSv2.gif |
| [lawrie/ulx3s_zx_spectrum](https://github.com/lawrie/ulx3s_zx_spectrum) | Verilog | 12 | 2020-05-07 | none | Minimal ZX Spectrum for Ulx3s ECP5 board | root: ulx3s |
| [semify-eda/waveform-generator](https://github.com/semify-eda/waveform-generator) | SystemVerilog | 12 | 2022-07-18 | Apache-2.0 | Waveform Generator | tree: fpga/ulx3s_barebones/ulx3s_v20.lpf |
| [asinghani/pifive-cpu](https://github.com/asinghani/pifive-cpu) | SystemVerilog + Migen | 11 | 2021-12-29 | Apache-2.0 | RISC-V CPU in SystemVerilog & Custom Migen-based SoC Generat | tree: fpga/ulx3s/constraints.lpf |
| [hsa-ees/piconut](https://github.com/hsa-ees/piconut) | C | 11 | 2026-09-01 | BSD-2-Clause | The PicoNut project provides a minimal and at the same time  | tree: boards/ulx3s/ulx3s.lpf |
| [lawrie/ulx3s_mac128](https://github.com/lawrie/ulx3s_mac128) | Verilog | 11 | 2022-08-08 | none | Macintosh 128 on the Ulx3s ECP5 FPGA | root: ulx3s |
| [Wren6991/Hazard3-SWD-SoC](https://github.com/Wren6991/Hazard3-SWD-SoC) | Verilog | 11 | 2023-04-20 | Apache-2.0 | Example Hazard3 + OpenDAP RISC-V SWD SoC integration | tree: synth/fpga_ulx3s.lpf |
| [YoWASP/toolchain-demo](https://github.com/YoWASP/toolchain-demo) | Amaranth | 11 | 2024-01-01 | ISC | Demonstration of the YoWASP toolchain being used with Visual | root: top.lpf |
| [dan-rodrigues/ulx3s-bluetooth-gamepad](https://github.com/dan-rodrigues/ulx3s-bluetooth-gamepad) | Verilog | 10 | 2020-10-24 | none | Bluetooth gamepad receiver demo using ULX3S FPGA board + ESP | root: ulx3s_v20.lpf |
| [daveshah1/ulx3s](https://github.com/daveshah1/ulx3s) | Verilog | 10 | 2018-11-06 | none | — | root: ulx3s.core |
| [lawrie/ulx3s_68k](https://github.com/lawrie/ulx3s_68k) | Verilog | 10 | 2020-07-13 | none | Experiments with the 68000 CPU on the Ulx3s ECP5 board | root: ulx3s |
| [RemyCiterin/AdventOfFPGA](https://github.com/RemyCiterin/AdventOfFPGA) | Bluespec | 9 | 2026-01-14 | Apache-2.0 | — | root: ulx3s.lpf |
| [danodus/xgsoc](https://github.com/danodus/xgsoc) | C | 8 | 2026-08-13 | MIT | FPGA-based system-on-chip | tree: rtl/ulx3s/ulx3s_v31.lpf |
| [lawrie/ulx3s_msx](https://github.com/lawrie/ulx3s_msx) | Verilog | 8 | 2023-05-14 | none | MSX 8-bit computers on the Ulx3s ECP5 board | root: ulx3s |
| [markus-zzz/myc64](https://github.com/markus-zzz/myc64) | Verilog | 8 | 2024-04-09 | none | My C64 implementation in Verilog | tree: syn/ulx3s.lpf |
| [marph91/yaaes](https://github.com/marph91/yaaes) | VHDL | 8 | 2021-08-08 | LGPL-3.0 | Yet Another AES implementation in hardware. | tree: syn/constraints/ulx3s_v20.lpf |
| [victor-fisyuk/voodoo-fpga-public](https://github.com/victor-fisyuk/voodoo-fpga-public) | SystemVerilog | 8 | 2026-09-13 | none | 3dfx Voodoo Graphics implementation in SystemVerilog for FPG | tree: screenshots/ulx3s.jpg |
| [marph91/pocket-bnn](https://github.com/marph91/pocket-bnn) | Python (Amaranth/LiteX) | 7 | 2021-07-16 | MPL-2.0 | BNN-to-FPGA framework, written in VHDL and Python | tree: syn/ulx3s_v20.lpf |
| [C-Elegans/ulx3s_sdram](https://github.com/C-Elegans/ulx3s_sdram) | Verilog | 6 | 2021-02-08 | none | SDRAM experiments on the ULX3S | root: ulx3s_v20.lpf |
| [lawrie/SpinalULX3S](https://github.com/lawrie/SpinalULX3S) | SpinalHDL | 6 | 2020-03-29 | none | SpinalHDL ULX3S examples | root: ulx3s_hdmi.lpf |
| [lawrie/ulx3s_altair_8800](https://github.com/lawrie/ulx3s_altair_8800) | Verilog | 6 | 2021-04-28 | none | Altair 8800 on the Ulx3s ECP5 FPGA board | root: ulx3s |
| [lawrie/ulx3s_colecovision](https://github.com/lawrie/ulx3s_colecovision) | Verilog | 6 | 2023-05-15 | none | ColecoVision console for the Ulx3s ECP5 board | root: ulx3s |
| [cheyao/oberon](https://github.com/cheyao/oberon) | Verilog | 5 | 2026-06-23 | none | Oberon recreated on the Icepi Zero | root: proj_pnru/lattice/ulx3s/ulx3s-v20 |
| [dlobato/cps1-musicbox](https://github.com/dlobato/cps1-musicbox) | LiteX (Migen) | 5 | 2022-04-07 | none | RiscV + CPS1 sound chips SoC based on litex | root: radiona_ulx3s.py |
| [evansm7/ArcDVI](https://github.com/evansm7/ArcDVI) | Verilog | 5 | 2021-12-04 | none | ****DEPRECATED PROTOTYPE**** FPGA design and firmware for Ac | tree: platform/ulx3s/ulx3s_v20.lpf |
| [lawrie/ulx3s_amstrad_cpc](https://github.com/lawrie/ulx3s_amstrad_cpc) | Verilog | 5 | 2022-05-04 | none | The Amstrad CPC on the Ulx3s Ecp5 FPGA board | root: ulx3s |
| [lawrie/ulx3s_bbc_micro](https://github.com/lawrie/ulx3s_bbc_micro) | Verilog | 5 | 2023-02-05 | none | Version of Ice40Beeb for Ulx3s ECP5 board | root: ulx3s |
| [lawrie/ulx3s_ql](https://github.com/lawrie/ulx3s_ql) | Verilog | 5 | 2020-09-07 | none | Sinclair QL for the Ulx3s ECP5 board | root: ulx3s |
| [mcejp/Poly94](https://github.com/mcejp/Poly94) | Verilog | 5 | 2024-03-03 | GPL-3.0 | Yet another faux-retro game system | root: ulx3s_v20.lpf |
| [robinsonb5/EightThirtyTwoDemos](https://github.com/robinsonb5/EightThirtyTwoDemos) | VHDL/Verilog | 5 | 2026-09-15 | GPL-3.0 | Demo projects for the EightThirtyTwo CPU | tree: Board/ulx3s_85f |
| [bjonnh/ulx3s-synth](https://github.com/bjonnh/ulx3s-synth) | Verilog | 4 | 2022-12-11 | none | Playing with FPGAs to make a midi-synth | root: ulx3s_v20.lpf |
| [dstrbad/janestreet-advent-fpga](https://github.com/dstrbad/janestreet-advent-fpga) | Hardcaml | 4 | 2026-01-15 | MIT | — | root: synth/ulx3s |
| [emard/cortex](https://github.com/emard/cortex) | Verilog | 4 | 2020-08-19 | none | fork of mini-cortex FPGA project - ancient unix with tns99xx | tree: ulx3s.lpf |
| [lawrie/jupiter_ace](https://github.com/lawrie/jupiter_ace) | Verilog | 4 | 2022-05-04 | none | Jupiter Ace for the Ulx3s | root: ulx3s |
| [lawrie/ulx3s_atari_2600](https://github.com/lawrie/ulx3s_atari_2600) | Assembly | 4 | 2022-05-08 | none | Atari 2600 for the Ulx3s Ecp5 FPGA board | root: ulx3s |
| [lawrie/ulx3s_ay_3_8500](https://github.com/lawrie/ulx3s_ay_3_8500) | Verilog | 4 | 2020-05-01 | none | The  AY-3-8500 Pong-on-a-chip for the Ulx3s ECP5 board | root: ulx3s |
| [lawrie/ulx3s_vic_20](https://github.com/lawrie/ulx3s_vic_20) | Verilog | 4 | 2020-05-14 | none | Minimal Commodore Vic 20 core for the Ulx3s ECP5 board | root: ulx3s |
| [ThorKn/vexriscv-ulx3s-simple-plugin](https://github.com/ThorKn/vexriscv-ulx3s-simple-plugin) | SpinalHDL | 4 | 2020-10-02 | none | A simple custom instruction for the vexriscv, deploy- and de | root: ulx3s |
| [acairncross/clash-ulx3s-examples](https://github.com/acairncross/clash-ulx3s-examples) | Clash | 3 | 2023-04-26 | MIT | Collection of Clash examples | root: ulx3s_v20.lpf |
| [danodus/ecp5_hdmi_audio_video](https://github.com/danodus/ecp5_hdmi_audio_video) | Verilog | 3 | 2026-05-19 | MIT | ECP5 HDMI Audio + Video Transmitter | tree: boards/ulx3s/ulx3s_v316.lpf |
| [fedy0/neo](https://github.com/fedy0/neo) | VHDL | 3 | 2024-06-07 | MIT | NEORV32 on ULX3S | root: ULX3S.lpf |
| [jamon/jspcpu](https://github.com/jamon/jspcpu) | Verilog | 3 | 2021-07-16 | none | — | root: ulx3s.lpf |
| [lawrie/ulx3s_cpm_z80](https://github.com/lawrie/ulx3s_cpm_z80) | Verilog | 3 | 2020-04-18 | none | A port of the Ice40CPMZ80 project to the Ulx3s ECP5 board | root: ulx3s |
| [lawrie/ulx3s_vhdl_examples](https://github.com/lawrie/ulx3s_vhdl_examples) | VHDL | 3 | 2022-05-07 | none | VHDL examples for the Ulx3s ECP5 FPGA | root: ulx3s_v20.lpf |
| [lawrie/ulx3s_z80_template](https://github.com/lawrie/ulx3s_z80_template) | Verilog | 3 | 2021-02-27 | none | Template for Z80 computer on the Ulx3s FPGA board | root: ulx3s |
| [lawrie/ulx3s_z80_trs80](https://github.com/lawrie/ulx3s_z80_trs80) | Verilog | 3 | 2021-02-27 | none | The TRS-80 Model 1 for the Ulx3s FPGA Ecp5 board, created fr | root: ulx3s |
| [lfglabs-dev/lean-silicon](https://github.com/lfglabs-dev/lean-silicon) | Python (Amaranth/LiteX) | 3 | 2026-09-08 | Apache-2.0 | A formally verified physical scalar coprocessor for leanVM-b | root: fpga/ulx3s |
| [rj45/vdp](https://github.com/rj45/vdp) | SystemVerilog | 3 | 2026-01-25 | NOASSERTION | A Verilog Retro-Inspired Video Display Processor for FPGA. | root: ulx3s |
| [zipotron/neorv32-complex-setups](https://github.com/zipotron/neorv32-complex-setups) | VHDL | 3 | 2021-12-04 | none | — | root: hardware_dependent/ulx3s |
| [emard/tinyfpga-bootloader-ulx3s](https://github.com/emard/tinyfpga-bootloader-ulx3s) | Makefile | 2 | 2021-10-01 | none | Attempt to compile for ulx3s | root: boards/ulx3s |
| [emard/usb_host](https://github.com/emard/usb_host) | Verilog | 2 | 2024-03-31 | none | — | tree: soc/ulx3s_v20.lpf |
| [emard/vhdl_c64_c1541_sd](https://github.com/emard/vhdl_c64_c1541_sd) | VHDL | 2 | 2018-01-29 | none | Adaptation attempt of DarFPGA's C64 for HDMI output | tree: proj/lattice/ulx3s/constraints/ulx3s_v18.lpf |
| [lawrie/ulx3s_acorn_atom](https://github.com/lawrie/ulx3s_acorn_atom) | Verilog | 2 | 2022-04-20 | none | Ulx3s port of Ice40Atom | root: ulx3s |
| [lawrie/ulx3s_sg_1000](https://github.com/lawrie/ulx3s_sg_1000) | Verilog | 2 | 2020-07-02 | none | Sega SG-1000 console for the Ulx3s ECP5 board | root: ulx3s |
| [RemyCiterin/DOoOM](https://github.com/RemyCiterin/DOoOM) | Bluespec | 2 | 2026-01-01 | GPL-2.0 | DOoOM Out-Of-Order Machine | root: ulx3s.lpf |
| [zipotron/ziposoc](https://github.com/zipotron/ziposoc) | Verilog | 2 | 2022-08-10 | none | — | root: ulx3s_v20.lpf |
| [acairncross/euphrates](https://github.com/acairncross/euphrates) | Clash | 1 | 2020-12-31 | BSD-3-Clause | Maximum flow accelerator in Clash | root: ulx3s_v20.lpf |
| [ADVIKBAHADUR/ULX3s-Superresolution-CNN](https://github.com/ADVIKBAHADUR/ULX3s-Superresolution-CNN) | bitstream + notebooks | 1 | 2024-08-15 | MIT | This project is funded and made possible by the Laidlaw Foun | root: ulx3s_85f_CSI.bit |
| [asinghani/ulx3s-vga-example](https://github.com/asinghani/ulx3s-vga-example) | SystemVerilog | 1 | 2024-03-25 | MIT | Example project for using ULX3S with VGA PMOD | root: constraints.lpf |
| [cronokirby/ck-snes](https://github.com/cronokirby/ck-snes) | Rust | 1 | 2026-04-06 | none | SNES Emulator | root: platform/ulx3s |
| [dulatello08/neocore-fx](https://github.com/dulatello08/neocore-fx) | SystemVerilog | 1 | 2026-06-08 | Apache-2.0 | — | root: ulx3s-85f-min.lpf |
| [gojimmypi/ttgf0p3-analog-UART-FSM-TRNG-Lab](https://github.com/gojimmypi/ttgf0p3-analog-UART-FSM-TRNG-Lab) | Verilog | 1 | 2026-07-02 | Apache-2.0 | ANALOG EXPERIMENTAL ttgf0p3 UART/SPI-controlled ASIC lab for | root: ulx3s |
| [gornjas/dvi_test](https://github.com/gornjas/dvi_test) | VHDL | 1 | 2025-03-02 | BSD-2-Clause | Playground for ULX3S video | root: ulx3s_fer.lpf |
| [jamesrosssharp/ulx3s_mixer_pcb](https://github.com/jamesrosssharp/ulx3s_mixer_pcb) | Verilog | 1 | 2024-08-25 | none | PCB for implementing a 100MHz PLL and mixer for ULX3s | root: ulx3s_mixer |
| [jlopezr/mini-gpu](https://github.com/jlopezr/mini-gpu) | Verilog | 1 | 2026-09-25 | none | Simple GPU implemented on ULX3S FPGA | root: 7.ulx3s_w9825g6kh_test |
| [joaln27/koti](https://github.com/joaln27/koti) | SystemVerilog | 1 | 2026-08-20 | Apache-2.0 | A home computer built from the CPU up: an RV32IMA core with  | root: fpga/ulx3s |
| [lawrie/ulx3s_gamegear](https://github.com/lawrie/ulx3s_gamegear) | Verilog | 1 | 2021-01-16 | none | Segs Game Gear for the Ulx3s ECP5 FPGA board | root: ulx3s |
| [LogoPoseidon/Ulx3sJukeBox](https://github.com/LogoPoseidon/Ulx3sJukeBox) | Verilog | 1 | 2024-10-19 | none | — | root: ulx3s_v20.lpf |
| [nklabs/libnklabs-ulx3s](https://github.com/nklabs/libnklabs-ulx3s) | C | 1 | 2022-08-13 | none | libnklabs example for PicoRV32 (RISC-V) running on ULX3S (La | root: ulx3s.lpf |
| [RemyCiterin/3DRiscV](https://github.com/RemyCiterin/3DRiscV) | Clash | 1 | 2026-01-11 | MIT | Some experimentations with the blarney DSL for hardware synt | root: ulx3s.lpf |
| [td0034/fpga](https://github.com/td0034/fpga) | HTML | 1 | 2026-03-05 | none | icesugar v1.5  | root: ulx3s |
| [thata/td4-ulx3s](https://github.com/thata/td4-ulx3s) | Verilog | 1 | 2024-12-06 | none | ULX3SでTD4を動かしてみる | root: ulx3s_v20.lpf |
| [ThePerfectComputer/learn-clash](https://github.com/ThePerfectComputer/learn-clash) | Clash | 1 | 2024-04-17 | none | My first efforts to use clash lang that other will hopefully | root: ulx3s |
| [ThePerfectComputer/MannaChip](https://github.com/ThePerfectComputer/MannaChip) | Bluespec | 1 | 2025-11-22 | none | — | root: ulx3s_fpga |
| [ThorKn/vexriscv-ulx3s-helloworld](https://github.com/ThorKn/vexriscv-ulx3s-helloworld) | Assembly | 1 | 2020-09-28 | none | Vexriscv CPU on ULX3S FPGA-Board with hello_world exmaple in | root: ulx3s |
| [adrmcintyre/vixen](https://github.com/adrmcintyre/vixen) | Assembly | 0 | 2026-09-09 | none | 16-bit computer on an FPGA | root: ulx3s |
| [ahamidi87/simpleblinky](https://github.com/ahamidi87/simpleblinky) | Verilog | 0 | 2024-11-01 | none | — | root: ulx3s_v20.lpf |
| [AndrewCapon/SpinalTemplateSbtUlx3s](https://github.com/AndrewCapon/SpinalTemplateSbtUlx3s) | SpinalHDL | 0 | 2020-12-22 | none | — | root: ulx3s_v20.lpf |
| [ChipDesign-BV/cdriscv-32s-20](https://github.com/ChipDesign-BV/cdriscv-32s-20) | SystemVerilog | 0 | 2026-09-18 | Apache-2.0 | A 32-bit RISC-V core subsystem for safety-critical mixed-sig | root: fpga/ulx3s |
| [Circuit-killer/fpga-usbserial](https://github.com/Circuit-killer/fpga-usbserial) | VHDL | 0 | 2019-02-23 | none | Second attempt to get usb-serial from opencores | root: lattice/ulx3s |
| [danodus/msx_fpga](https://github.com/danodus/msx_fpga) | Verilog | 0 | 2025-05-03 | MIT | — | root: ulx3s |
| [DFiantWorks/interactive-sim](https://github.com/DFiantWorks/interactive-sim) | C++ | 0 | 2026-07-23 | MIT | Interactive Hardware Simulation Component (DPI/VHPI/VPI) | root: ulx3s_demo |
| [diegob94/ulx3s_blink](https://github.com/diegob94/ulx3s_blink) | Verilog | 0 | 2022-09-29 | Apache-2.0 | Example project | root: ulx3s_v20.lpf |
| [dman2021/blink](https://github.com/dman2021/blink) | Makefile | 0 | 2025-08-01 | none | Test the ulx3s functions | root: clk_blink.lpf |
| [dman2021/fpga_count](https://github.com/dman2021/fpga_count) | Verilog | 0 | 2025-07-16 | none | — | root: top.lpf |
| [dman2021/uart_echo](https://github.com/dman2021/uart_echo) | Verilog | 0 | 2025-07-17 | none | — | root: uart_echo.lpf |
| [dschaefer/fpga-template](https://github.com/dschaefer/fpga-template) | SystemVerilog | 0 | 2022-11-06 | none | Project template for FPGA dev | root: ulx3s_v20.lpf |
| [dschaefer/ulx3s-ghdl-adder](https://github.com/dschaefer/ulx3s-ghdl-adder) | VHDL | 0 | 2021-09-19 | none | Adder example written in VHDL | root: ulx3s_v20.lpf |
| [dulatello08/litex-cpu-testing](https://github.com/dulatello08/litex-cpu-testing) | Verilog | 0 | 2025-12-18 | none | — | root: ulx3s_v316.lpf |
| [dulatello08/neocorefx-dram](https://github.com/dulatello08/neocorefx-dram) | Verilog | 0 | 2026-05-12 | none | — | root: ulx3s-85f-min.lpf |
| [dulatello08/ulx3s-tests](https://github.com/dulatello08/ulx3s-tests) | SystemVerilog | 0 | 2025-10-16 | GPL-3.0 | Tests for my ULX3S FPGA board, to then start working on NeoC | root: ulx3s_85f.lpf |
| [gojimmypi/nextpnr-issue235](https://github.com/gojimmypi/nextpnr-issue235) | C++ | 0 | 2019-02-25 | GPL-3.0 | supplement to nextpnr issue #235 | root: ulx3s_v20.lpf |
| [gojimmypi/ttgf-UART-FSM-TRNG-Lab](https://github.com/gojimmypi/ttgf-UART-FSM-TRNG-Lab) | Verilog | 0 | 2026-09-08 | Apache-2.0 | Tiny Tapeout GF180 (wafer.space) shuttles - Verilog HDL Proj | root: ulx3s |
| [gojimmypi/ttgf0p3-UART-FSM-TRNG-Lab](https://github.com/gojimmypi/ttgf0p3-UART-FSM-TRNG-Lab) | Verilog | 0 | 2026-06-27 | Apache-2.0 | EXPERIMENTAL ttgf0p3 UART/SPI-controlled ASIC lab for explor | root: ulx3s |
| [gojimmypi/ttsky-UART-FSM-TRNG-Lab](https://github.com/gojimmypi/ttsky-UART-FSM-TRNG-Lab) | Verilog | 0 | 2026-07-01 | Apache-2.0 | Tiny Tapeout SKY130 (ChipFoundry) shuttles: Universal Asynch | root: ulx3s |
| [goran-mahovlic/odysseus_sprites](https://github.com/goran-mahovlic/odysseus_sprites) | Makefile | 0 | 2024-07-29 | MIT | — | root: ulx3s_v20.lpf |
| [hanseo03/ulx3s-custom-riscv-cpu](https://github.com/hanseo03/ulx3s-custom-riscv-cpu) | Verilog | 0 | 2026-07-06 | none | — | root: ulx3s_12k.lpf |
| [hanseo03/ulx3s-vexriscv-soc](https://github.com/hanseo03/ulx3s-vexriscv-soc) | Verilog | 0 | 2026-06-04 | none | VexRiscv-based SoC on ULX3S 12K (ECP5) | root: ulx3s_12k.lpf |
| [Hassan2203/System-On-Chip-SOC-Design-and-verification](https://github.com/Hassan2203/System-On-Chip-SOC-Design-and-verification) | Verilog | 0 | 2026-06-19 | none | System-on-Chip (SoC) Design: Designed a 32-bit RISC-V single | root: build_wishbone_ulx3s.bat |
| [jadephilipoom/ulx3s-experiments](https://github.com/jadephilipoom/ulx3s-experiments) | Verilog | 0 | 2026-06-05 | none | learning stuff about hardware | root: ulx3s_v20.lpf |
| [krishkc5/trng-ring-oscillator](https://github.com/krishkc5/trng-ring-oscillator) | TeX | 0 | 2026-02-08 | none | FPGA-based True Random Number Generator using ring oscillato | root: ulx3s_v20.lpf |
| [l0r3m1psum/videogame_verilog](https://github.com/l0r3m1psum/videogame_verilog) | Verilog | 0 | 2025-07-22 | none | — | root: ulx3s_v20.lpf |
| [lcausevic/ULX3S_FPGA_Logic_Structures](https://github.com/lcausevic/ULX3S_FPGA_Logic_Structures) | ? | 0 | 2026-09-22 | none | — | root: ULX3S-85F.zip |
| [mpardalos/clash-blinky](https://github.com/mpardalos/clash-blinky) | Clash | 0 | 2025-04-13 | none | Programming the ulx3s with Clash | root: ulx3s_v20.lpf |
| [MSRRaju07/IOP](https://github.com/MSRRaju07/IOP) | Verilog (Icestudio) | 0 | 2024-03-27 | MIT | — | root: ULX3S_SOBEL.ice |
| [nicocavallu/rf-dds-lo](https://github.com/nicocavallu/rf-dds-lo) | Verilog | 0 | 2026-08-06 | none | FGPA Direct Digital Synthesis  | root: ulx3s.lpf |
| [nullobject/counter-ulx3s](https://github.com/nullobject/counter-ulx3s) | Makefile | 0 | 2025-02-01 | none | — | root: ulx3s_v20.lpf |
| [nullobject/m68k-ulx3s](https://github.com/nullobject/m68k-ulx3s) | Verilog | 0 | 2025-06-07 | none | — | root: ulx3s_v20.lpf |
| [nullobject/riscv-ulx3s](https://github.com/nullobject/riscv-ulx3s) | Verilog | 0 | 2025-07-13 | none | — | root: ulx3s_v20.lpf |
| [punchthatface/tinyDMA](https://github.com/punchthatface/tinyDMA) | SystemVerilog | 0 | 2026-04-29 | none | TinyDMA-2C is a programmable two-channel direct memory acces | root: constraints.lpf |
| [RichardEGeorge/ULX3S-Chase](https://github.com/RichardEGeorge/ULX3S-Chase) | Verilog | 0 | 2021-02-11 | GPL-3.0 | — | root: ulx3s_v20.lpf |
| [RichardEGeorge/ULX3S-Flipflop](https://github.com/RichardEGeorge/ULX3S-Flipflop) | Verilog | 0 | 2021-02-13 | none | A D-type flip-flop for the ULX3S board | root: ulx3s_v20.lpf |
| [RichardEGeorge/ULX3S-Passthru](https://github.com/RichardEGeorge/ULX3S-Passthru) | Verilog | 0 | 2021-02-13 | none | — | root: ulx3s_v20.lpf |
| [SeMinLim/bluerv32](https://github.com/SeMinLim/bluerv32) | Bluespec | 0 | 2026-08-14 | none | Boilerplate codebase for synthesizable RV32 soft processor v | root: ulx3s |
| [StefanHaslhofer/HardwareDesign](https://github.com/StefanHaslhofer/HardwareDesign) | VHDL | 0 | 2024-12-26 | none | — | root: ulx3s_v20.lpf |
| [stuij/odyssey](https://github.com/stuij/odyssey) | Makefile | 0 | 2023-02-03 | none | odyssey | root: ulx3s_v20_segpdi.lpf |
| [TechPrototyper/trs80-rev-z](https://github.com/TechPrototyper/trs80-rev-z) | Verilog | 0 | 2026-08-27 | NOASSERTION | TRS-80 Model 1 (Rev G) as open, verified hardware on ULX3S/E | root: boards/ulx3s |
| [thata/ulx3s-uart-loopback](https://github.com/thata/ulx3s-uart-loopback) | Verilog | 0 | 2024-11-19 | none | ULX3SでUARTをループバックさせてみた | root: ulx3s_v20.lpf |
| [ThorKn/vga_clock_1](https://github.com/ThorKn/vga_clock_1) | Scala (SpinalHDL/Chisel) | 0 | 2023-06-02 | Apache-2.0 | Hardware circuit with an VGA output that displays a simple c | root: ulx3s |
| [ThorKn/vga_pong](https://github.com/ThorKn/vga_pong) | Verilog | 0 | 2023-11-27 | GPL-3.0 | Pong game on a VGA display. HDL for FPGA and ASIC. | root: ulx3s |
| [tommythorn/bluespec_blink](https://github.com/tommythorn/bluespec_blink) | Bluespec | 0 | 2025-03-09 | none | Blink LEDs on ULX3S using Bluespec | root: ulx3s_v20.lpf |
| [vladov3000/ulx3s](https://github.com/vladov3000/ulx3s) | C++ | 0 | 2026-03-15 | none | — | root: ulx3s.lpf |
| [Volnirr/verilog-uart](https://github.com/Volnirr/verilog-uart) | Verilog | 0 | 2026-08-15 | none | UART transceiver written in Verilog | root: ulx3s.lpf |
| [yope/cpuv2](https://github.com/yope/cpuv2) | Verilog | 0 | 2021-03-17 | none | A very simple 32bit CPU design in verilog | root: ulx3s_v20.lpf |
| [zipotron/ulx3s_sdram8](https://github.com/zipotron/ulx3s_sdram8) | SystemVerilog | 0 | 2021-10-12 | none | — | root: ulx3s_v20.lpf |

### B. ULX3S-dedicated repos (name/description/topic = ULX3S, HDL sources present, no .lpf at root) — 51 repos

| full_name | lang/HDL | stars | last push | license | what it is | evidence |
|---|---|---|---|---|---|---|
| [emard/ulx3s_galaksija](https://github.com/emard/ulx3s_galaksija) | Verilog | 18 | 2025-07-06 | none | Galaksija computer for FPGA | name/desc (unverified) |
| [GuzTech/ulx3s-nmigen-examples](https://github.com/GuzTech/ulx3s-nmigen-examples) | Amaranth | 16 | 2020-11-30 | none | nMigen examples for the ULX3S board | name/desc (unverified) |
| [sangwoojun/ulx3s_bsv](https://github.com/sangwoojun/ulx3s_bsv) | Bluespec | 15 | 2025-03-09 | none | Bluespec environment for working with the ulx3s board and it | name/desc (unverified) |
| [gojimmypi/ulx3s-examples](https://github.com/gojimmypi/ulx3s-examples) | Python (Amaranth/LiteX) | 12 | 2020-10-05 | none | Collection of various ulx3s examples | name/desc (unverified) |
| [mkvenkit/ulx3s_examples](https://github.com/mkvenkit/ulx3s_examples) | ? | 11 | 2022-04-25 | none | Beginner-friendly Verilog based examples for the ULX3S FPGA  | name/desc (unverified) |
| [pepijndevos/rust-litex-example](https://github.com/pepijndevos/rust-litex-example) | LiteX + Rust | 11 | 2022-06-16 | Apache-2.0 | An example application that demonstrates litex-hal on the UL | name/desc (unverified) |
| [dstrbad/fpga-soc-ml-accelerator](https://github.com/dstrbad/fpga-soc-ml-accelerator) | LiteX | 5 | 2026-08-04 | none | FPGA SoC learning project: soft RISC-V CPU, Linux, and hardw | name/desc (unverified) |
| [emard/ulx3s-emi](https://github.com/emard/ulx3s-emi) | Verilog | 5 | 2021-10-22 | none | demo core for electromagnetic interference measurement | name/desc (unverified) |
| [emard/ulx3s_c64](https://github.com/emard/ulx3s_c64) | VHDL | 5 | 2024-04-04 | none | Attempt porting parts of mister C64 to ULX3S | name/desc (unverified) |
| [jamesrosssharp/1_bit_AM](https://github.com/jamesrosssharp/1_bit_AM) | Verilog | 5 | 2024-09-28 | MIT | 1 bit AM Radio for ULX3S | name/desc (unverified) |
| [mb-sat/ulx3s-longwave-sdr](https://github.com/mb-sat/ulx3s-longwave-sdr) | Verilog | 5 | 2025-06-18 | GPL-3.0 | A longwave software defined radio receiver for the Radiona U | name/desc (unverified) |
| [tarik-hamedovic/SDR-HLS](https://github.com/tarik-hamedovic/SDR-HLS) | Verilog (HLS) | 5 | 2024-10-31 | none | SDR-HLS is a Master Thesis focused on the implementation and | name/desc (unverified) |
| [fedy0/zta](https://github.com/fedy0/zta) | Verilog | 3 | 2024-07-12 | MIT | Ztachip on ULX3S | name/desc (unverified) |
| [lawrie/ulx3s_pdp_11](https://github.com/lawrie/ulx3s_pdp_11) | ? | 3 | 2022-03-21 | none | Experiments with the PDP 11 instruction set on the Ulx3s Ecp | name/desc (unverified) |
| [BornaBiro/FPGA_epaper](https://github.com/BornaBiro/FPGA_epaper) | HTML | 2 | 2023-03-03 | MIT | FPGA code/implementation for driving epaper with ULX3S board | name/desc (unverified) |
| [Detegr/ulx3s-projects](https://github.com/Detegr/ulx3s-projects) | Verilog | 2 | 2019-02-27 | CC-BY-4.0 | My projects for ULX3S FPGA | name/desc (unverified) |
| [emard/ulx3s-jtagthru](https://github.com/emard/ulx3s-jtagthru) | Makefile | 2 | 2019-01-28 | none | ULX3S JTAG pass-thru | name/desc (unverified) |
| [Ruebenschus/Atari-FPCartridge](https://github.com/Ruebenschus/Atari-FPCartridge) | Verilog | 2 | 2026-06-25 | none | Use an ULX3s FPGA to emulate an Atari ST cartridge | name/desc (unverified) |
| [tucanae47/ulx3s-experiments](https://github.com/tucanae47/ulx3s-experiments) | Verilog | 2 | 2022-11-30 | none | — | name/desc (unverified) |
| [ulx3s/Hazard3-Doom](https://github.com/ulx3s/Hazard3-Doom) | C (+Hazard3 Verilog) | 2 | 2026-09-21 | NOASSERTION | Educational Doom Generic on the ULX3S and ULX4M for the Haza | name/desc (unverified) |
| [w531t4/fpga_led_display](https://github.com/w531t4/fpga_led_display) | SystemVerilog | 2 | 2026-07-12 | MIT | Use FPGA to drive large LED matrixes at high speeds! | name/desc (unverified) |
| [JohnAZoidberg/ulx3s-espi-analyzer](https://github.com/JohnAZoidberg/ulx3s-espi-analyzer) | Verilog | 1 | 2026-03-08 | none | — | name/desc (unverified) |
| [mithro/asus-d16-ulx3s-interface](https://github.com/mithro/asus-d16-ulx3s-interface) | LiteX | 1 | 2026-07-20 | Apache-2.0 | ULX3S LiteX bench controller for the ASUS KGPE-D16 (SPI-flas | name/desc (unverified) |
| [mmicko/ulx3s-examples](https://github.com/mmicko/ulx3s-examples) | Verilog | 1 | 2019-02-21 | none | — | name/desc (unverified) |
| [nh428/ULX3S-TFT-Display-Sobel-Object-Detection](https://github.com/nh428/ULX3S-TFT-Display-Sobel-Object-Detection) | Verilog | 1 | 2026-07-27 | none | Verilog source code to implement Sobel image detection utili | name/desc (unverified) |
| [pcotret/ULX3S-examples](https://github.com/pcotret/ULX3S-examples) | VHDL | 1 | 2020-11-13 | none | — | name/desc (unverified) |
| [PietPtr/ULX3S-DSP](https://github.com/PietPtr/ULX3S-DSP) | Clash | 1 | 2022-06-17 | none | — | name/desc (unverified) |
| [ThorKn/spinalSynth_ULX3S](https://github.com/ThorKn/spinalSynth_ULX3S) | SpinalHDL→Verilog | 1 | 2026-06-11 | none | — | name/desc (unverified) |
| [bqqbarbhg/blipv1](https://github.com/bqqbarbhg/blipv1) | Python (Amaranth/LiteX) | 0 | 2020-12-25 | none | Something for ULX3S | name/desc (unverified) |
| [CarlRaymond/ulx3s-container](https://github.com/CarlRaymond/ulx3s-container) | PowerShell | 0 | 2026-03-23 | none | Experiments with ULX3S toolchain in a Docker container | name/desc (unverified) |
| [chiplet/acorechip-ulx3s](https://github.com/chiplet/acorechip-ulx3s) | Python (Amaranth/LiteX) | 0 | 2024-11-16 | Apache-2.0 | ACoreChip RISC-V soft core implementation on ULX3S FPGA deve | name/desc (unverified) |
| [chiplet/ulx3s-blinky](https://github.com/chiplet/ulx3s-blinky) | Makefile | 0 | 2024-03-26 | none | — | name/desc (unverified) |
| [dpks2003/my_ulx3s_repo](https://github.com/dpks2003/my_ulx3s_repo) | Verilog | 0 | 2024-01-15 | none | This repository contains all of my project implemented on ul | name/desc (unverified) |
| [dpks2003/Dice_crap_game](https://github.com/dpks2003/Dice_crap_game) | Verilog | 0 | 2024-03-10 | none | This repo contains Verilog Implementation of Dice Crap Game  | name/desc (unverified) |
| [EmbeddedDojo/ULX3S_Examples](https://github.com/EmbeddedDojo/ULX3S_Examples) | Verilog | 0 | 2022-01-18 | Apache-2.0 | ULX3S Lattice board examples | name/desc (unverified) |
| [flyingoverclouds/flocs-ulx3s-samples](https://github.com/flyingoverclouds/flocs-ulx3s-samples) | Verilog | 0 | 2020-12-31 | MIT | My samples and tests on the FGPA ULX3S board and opensource  | name/desc (unverified) |
| [fywc/ulx3s_rv32i_processor](https://github.com/fywc/ulx3s_rv32i_processor) | Bluespec | 0 | 2023-03-15 | none | a simple 4-stages pipelined rv32i processor  | name/desc (unverified) |
| [ghaworth/ulx3s-bldc-foc](https://github.com/ghaworth/ulx3s-bldc-foc) | Makefile | 0 | 2026-06-15 | none | Open-source FPGA FOC core and three-phase driver board for B | name/desc (unverified) |
| [ghaworth/ulx3s-tinyai](https://github.com/ghaworth/ulx3s-tinyai) | Verilog | 0 | 2026-07-16 | NOASSERTION | — | name/desc (unverified) |
| [gmejiamtz/ulx3s-components](https://github.com/gmejiamtz/ulx3s-components) | SystemVerilog | 0 | 2025-08-20 | MIT | A repo dedicated to getting various components on the ULX3S  | name/desc (unverified) |
| [gojimmypi/z80386-ulx3s-doom](https://github.com/gojimmypi/z80386-ulx3s-doom) | Verilog | 0 | 2026-07-29 | none | — | name/desc (unverified) |
| [John-K/spinose](https://github.com/John-K/spinose) | LiteX | 0 | 2020-04-11 | BSD-2-Clause | Litex based SPI NOR dumping gateware for ULX3S | name/desc (unverified) |
| [marinsiric/ulx3s](https://github.com/marinsiric/ulx3s) | HTML | 0 | 2020-01-23 | none | — | name/desc (unverified) |
| [p-kraszewski/CS-ULX3S-03](https://github.com/p-kraszewski/CS-ULX3S-03) | C++ | 0 | 2023-08-22 | GPL-3.0 | Materials for FPGA devboard ULX3S v3.1.8 (sold by Mouser, Ap | name/desc (unverified) |
| [Pfontvilanova/pfforthMACHINE](https://github.com/Pfontvilanova/pfforthMACHINE) | ? | 0 | 2026-01-17 | none | Hardware Forth stack machine implementation for ULX3S FPGA w | name/desc (unverified) |
| [RiltonF/Thermal_camera_ulx3s](https://github.com/RiltonF/Thermal_camera_ulx3s) | SystemVerilog | 0 | 2025-07-01 | GPL-3.0 | — | name/desc (unverified) |
| [saul-rodriguez/ulx3s](https://github.com/saul-rodriguez/ulx3s) | Assembly | 0 | 2021-05-16 | none | — | name/desc (unverified) |
| [thata/ulx3s-playground](https://github.com/thata/ulx3s-playground) | SystemVerilog | 0 | 2024-12-18 | NOASSERTION | — | name/desc (unverified) |
| [Thewbi/ULX3S](https://github.com/Thewbi/ULX3S) | HTML | 0 | 2025-09-15 | none | ULX3S Projects | name/desc (unverified) |
| [tom7980/ulxws](https://github.com/tom7980/ulxws) | Verilog | 0 | 2026-04-04 | none | Workspace for playing with the ulx3s | name/desc (unverified) |
| [tristanitschner/ulx3s-examples](https://github.com/tristanitschner/ulx3s-examples) | C | 0 | 2022-10-01 | GPL-2.0 | My experiments with the ULX3S FPGA board. | name/desc (unverified) |

### C. Multi-board / other projects whose README states a ULX3S target — 69 repos

| full_name | lang/HDL | stars | last push | license | what it is | evidence |
|---|---|---|---|---|---|---|
| [google/CFU-Playground](https://github.com/google/CFU-Playground) | Verilog + LiteX | 567 | 2026-02-26 | Apache-2.0 | Want a faster ML processor? Do it yourself! -- A framework f | README (unverified) |
| [vmware-archive/cascade](https://github.com/vmware-archive/cascade) | Verilog JIT (C++) | 446 | 2021-07-01 | NOASSERTION | A Just-In-Time Compiler for Verilog from VMware Research | README (unverified) |
| [sylefeb/tinygpus](https://github.com/sylefeb/tinygpus) | Silice | 178 | 2026-01-24 | GPL-3.0 | TinyGPUs, making graphics hardware for 1990s games | README (unverified) |
| [gonsolo/Borg](https://github.com/gonsolo/Borg) | Chisel/Scala | 32 | 2026-09-26 | none | Foundational workflow for an open-source GPU | README (unverified) |
| [uttamcoomar/NN_Digits](https://github.com/uttamcoomar/NN_Digits) | Verilog | 31 | 2026-03-22 | MIT | — | README (unverified) |
| [zyedidia/riscinator](https://github.com/zyedidia/riscinator) | Chisel | 18 | 2023-04-14 | MIT | A tiny 3-stage RISC-V core written in Chisel. | README (unverified) |
| [asinghani/advent-of-hardcaml-2024](https://github.com/asinghani/advent-of-hardcaml-2024) | Hardcaml | 17 | 2025-02-26 | MIT | Solving 2024 Advent of Code entirely on an FPGA using Hardca | README (unverified) |
| [carlosedp/chisel-fpga-pinfinder](https://github.com/carlosedp/chisel-fpga-pinfinder) | Chisel | 17 | 2024-09-24 | NOASSERTION | A Chisel implementation for an FPGA Pin Finder thru UART | README (unverified) |
| [asinghani/advent-of-hardcaml-2025](https://github.com/asinghani/advent-of-hardcaml-2025) | Hardcaml | 11 | 2026-01-01 | none | My attempts at solving Advent of Code 2025 in an FPGA | README (unverified) |
| [jerry-D/SYMPL_IEEE754-2019_ISA](https://github.com/jerry-D/SYMPL_IEEE754-2019_ISA) | Assembly | 7 | 2023-12-08 | NOASSERTION | SYMPL IEEE 754-2019 Instruction Set Architecture Compute Eng | README (unverified) |
| [dlobato/tfmicro-on-litex-vexriscv](https://github.com/dlobato/tfmicro-on-litex-vexriscv) | C++ | 7 | 2021-04-26 | BSD-2-Clause | PoC running tfmicro on LiteX/VexRiscv | README (unverified) |
| [ckdur/RISCVConsole](https://github.com/ckdur/RISCVConsole) | Chisel (Chipyard) | 6 | 2026-09-24 | MIT | An attempt to do a RISCV videogame console. | README (unverified) |
| [mole99/tt05-one-sprite-pony](https://github.com/mole99/tt05-one-sprite-pony) | Verilog | 6 | 2025-02-09 | Apache-2.0 | This SVGA Verilog design has exactly one trick up its sleeve | README (unverified) |
| [HeiChips/heichips25-template](https://github.com/HeiChips/heichips25-template) | Tcl | 6 | 2026-03-01 | Apache-2.0 | The template for the HeiChips 2025 hackathon | README (unverified) |
| [ChipFlow/example-socs](https://github.com/ChipFlow/example-socs) | Amaranth | 5 | 2025-01-16 | BSD-2-Clause | — | README (unverified) |
| [fm4dd/pmod-7seg9](https://github.com/fm4dd/pmod-7seg9) | Verilog | 5 | 2026-02-14 | NOASSERTION | Single-row PMOD with nine multiplexed seven-segment LED digi | README (unverified) |
| [SeMinLim/blueyosys](https://github.com/SeMinLim/blueyosys) | Bluespec | 5 | 2026-09-23 | none | Boilerplate codebase for Embedded FPGA kernel development vi | README (unverified) |
| [srjilarious/fpga_start](https://github.com/srjilarious/fpga_start) | C++ | 5 | 2026-02-28 | none | — | README (unverified) |
| [NoxHarmonium/sirc](https://github.com/NoxHarmonium/sirc) | Rust | 4 | 2026-09-26 | GPL-3.0 | The best retro console that never existed | README (unverified) |
| [dicethrow/amaram](https://github.com/dicethrow/amaram) | Amaranth | 3 | 2022-04-13 | none | A HDL library providing a max-bandwidth, n-async-FIFO interf | README (unverified) |
| [secworks/CrypTkey](https://github.com/secworks/CrypTkey) | Verilog | 2 | 2025-02-25 | BSD-2-Clause | HSM based on Cryptech and Tillitis Tkey. Implemented on the  | README (unverified) |
| [danodus/onramp-fpga](https://github.com/danodus/onramp-fpga) | C | 2 | 2026-05-26 | MIT | FPGA-based system-on-chip with a 32-bit Onramp processor | README (unverified) |
| [gergoerdi/advent-of-clash-2025](https://github.com/gergoerdi/advent-of-clash-2025) | Clash | 2 | 2026-01-13 | GPL-3.0 | Advent of Clash 2025 | README (unverified) |
| [cgarryZA/advent-of-camel-2025](https://github.com/cgarryZA/advent-of-camel-2025) | Hardcaml | 2 | 2026-01-19 | MIT | A hardware-first exploration of Advent of Code 2025, impleme | README (unverified) |
| [dibyx/Flux](https://github.com/dibyx/Flux) | Python (Amaranth/LiteX) | 2 | 2026-02-09 | NOASSERTION | Educational GPU platform - Democratizing GPU building with c | README (unverified) |
| [fm4dd/pmod-charlcd](https://github.com/fm4dd/pmod-charlcd) | Verilog | 1 | 2024-02-24 | NOASSERTION | PMOD module for connecting a HD44780-compatible character LC | README (unverified) |
| [AravindRajeshkanna/vernier-rv32](https://github.com/AravindRajeshkanna/vernier-rv32) | Verilog | 1 | 2026-09-27 | NOASSERTION | vernier-rv32 is an open-source FPGA SoC design project cente | README (unverified) |
| [gildobjanschi/RISCV_PROCESSOR](https://github.com/gildobjanschi/RISCV_PROCESSOR) | Assembly | 1 | 2024-09-06 | MIT | 32-bit RISC-V Processor Verilog code | README (unverified) |
| [johngannon4/riscv-cpu-portfolio](https://github.com/johngannon4/riscv-cpu-portfolio) | ? | 1 | 2026-09-24 | none | RV32IM 6-stage pipelined RISC-V core in SystemVerilog with a | README (unverified) |
| [TadeoRoboticsGroup/AxiomaCore-328](https://github.com/TadeoRoboticsGroup/AxiomaCore-328) | Verilog | 1 | 2026-09-26 | Apache-2.0 | AxiomaCore-328, un microcontrolador de arquitectura abierta  | README (unverified) |
| [titouanc/fpga-scratchpad](https://github.com/titouanc/fpga-scratchpad) | LiteX | 1 | 2021-03-25 | none | Fiddling with FPGAs, Migen, LiteX and stuffs | README (unverified) |
| [uttamcoomar/MAC-units-for-various-number-formats](https://github.com/uttamcoomar/MAC-units-for-various-number-formats) | Verilog | 1 | 2026-03-13 | none | This project contains MAC units in Verilog for BF16, FP16, I | README (unverified) |
| [pepijndevos/litedhrystone](https://github.com/pepijndevos/litedhrystone) | LiteX | 1 | 2024-10-30 | none | Run the Dhrystone benchmark on LiteX | README (unverified) |
| [bhouvana/AEGIS-X86-Processor](https://github.com/bhouvana/AEGIS-X86-Processor) | Python (Amaranth/LiteX) | 1 | 2026-09-10 | none | Research-grade synthesizable x86-64 out-of-order core in Sys | README (unverified) |
| [SeMinLim/sway](https://github.com/SeMinLim/sway) | Bluespec | 0 | 2026-09-26 | none | — | README (unverified) |
| [SeMinLim/zfpe](https://github.com/SeMinLim/zfpe) | Bluespec | 0 | 2021-08-20 | none | Neural Network Compression for Embedded Accelerators | README (unverified) |
| [dicethrow/amtest](https://github.com/dicethrow/amtest) | Amaranth | 0 | 2022-03-11 | none | My tests for learning how to work with the Amaranth HDL | README (unverified) |
| [bonfireprocessor/bonfire-core](https://github.com/bonfireprocessor/bonfire-core) | Amaranth/VHDL (FuseSoC) | 0 | 2026-09-21 | NOASSERTION | — | README (unverified) |
| [bonfireprocessor/bonfire-ecp5-jtagg-led-demo](https://github.com/bonfireprocessor/bonfire-ecp5-jtagg-led-demo) | Amaranth (FuseSoC) | 0 | 2026-07-20 | NOASSERTION | — | README (unverified) |
| [businessmanraduc/Doggo-V6](https://github.com/businessmanraduc/Doggo-V6) | SystemVerilog | 0 | 2026-07-12 | NOASSERTION | 6th variant of the Doggo-CPU series - PHANTOM-32 | README (unverified) |
| [chrislikescisco/nes-fpga](https://github.com/chrislikescisco/nes-fpga) | SystemVerilog | 0 | 2026-04-14 | none | NES FPGA project for CEN3907 | README (unverified) |
| [danielh186/6502-Tapeout](https://github.com/danielh186/6502-Tapeout) | Verilog | 0 | 2025-04-15 | none | Open-Source 6502, designed for OpenROAD toolchain and IHP SG | README (unverified) |
| [fusetim/rusty-soc](https://github.com/fusetim/rusty-soc) | Rust | 0 | 2026-02-08 | NOASSERTION | System On Chip made from scratch (SoC/Hardware on FPGA, Firm | README (unverified) |
| [harrowm/mackerel_030f](https://github.com/harrowm/mackerel_030f) | Verilog | 0 | 2026-09-23 | MIT | My attempt at building a mackerel 030 board in verilog for a | README (unverified) |
| [jeli180/Shape-Inference-SOC](https://github.com/jeli180/Shape-Inference-SOC) | SystemVerilog | 0 | 2026-09-09 | none | SOC for Shape Inference | README (unverified) |
| [joaln27/CORDIC](https://github.com/joaln27/CORDIC) | Python (Amaranth/LiteX) | 0 | 2026-09-25 | Apache-2.0 | A 16-iteration CORDIC sine generator on one TinyTapeout tile | README (unverified) |
| [LucasEBSkora/wav-player](https://github.com/LucasEBSkora/wav-player) | Silice | 0 | 2025-02-07 | MIT | Wav file player SoC written in the silice language | README (unverified) |
| [markus-zzz/hyperram-test](https://github.com/markus-zzz/hyperram-test) | Verilog | 0 | 2021-12-30 | none | Testbench for my HyperRAM board | README (unverified) |
| [markus-zzz/max9850-test](https://github.com/markus-zzz/max9850-test) | Verilog | 0 | 2022-01-30 | none | — | README (unverified) |
| [markus-zzz/zzz-rv](https://github.com/markus-zzz/zzz-rv) | Assembly | 0 | 2024-09-04 | CERN-OHL-P-2.0 | — | README (unverified) |
| [nicocavallu/fpga-LoRa-Receiver](https://github.com/nicocavallu/fpga-LoRa-Receiver) | ? | 0 | 2026-08-18 | GPL-3.0 | FPGA project to decode LoRa messages on custom RISC-V Archit | README (unverified) |
| [nicocavallu/rf-fft-engine](https://github.com/nicocavallu/rf-fft-engine) | Verilog | 0 | 2026-08-21 | GPL-3.0 | Hardware FFT engine for LoRa Dechirper project. Provides ins | README (unverified) |
| [nicocavallu/rf-sdr-frontend](https://github.com/nicocavallu/rf-sdr-frontend) | Verilog | 0 | 2026-08-18 | none | RF Frontend for LoRa Dechirper project | README (unverified) |
| [quigleyj97/nesgate](https://github.com/quigleyj97/nesgate) | VHDL | 0 | 2025-04-20 | NOASSERTION | VHDL implementation of the Nintendo Entertainment System for | README (unverified) |
| [rainbow1128/VHDL-AES-Master](https://github.com/rainbow1128/VHDL-AES-Master) | VHDL | 0 | 2023-05-02 | LGPL-3.0 | — | README (unverified) |
| [RedDocMD/klaus](https://github.com/RedDocMD/klaus) | Hardcaml | 0 | 2026-01-16 | none | AoC 2025 Hardcaml solutions | README (unverified) |
| [Seth16225/riscv-core-portfolio](https://github.com/Seth16225/riscv-core-portfolio) | C | 0 | 2026-08-19 | MIT | — | README (unverified) |
| [ThorKn/LAYR_AUDIO](https://github.com/ThorKn/LAYR_AUDIO) | Verilog | 0 | 2026-05-14 | none | — | README (unverified) |
| [tucanae47/litex_etpu](https://github.com/tucanae47/litex_etpu) | LiteX | 0 | 2022-12-22 | none | — | README (unverified) |
| [williamsharkey/Pruned-SHA256-Miner](https://github.com/williamsharkey/Pruned-SHA256-Miner) | SystemVerilog | 0 | 2026-08-13 | none | — | README (unverified) |
| [lazardjurovic/edulent_rtl](https://github.com/lazardjurovic/edulent_rtl) | SystemVerilog | 0 | 2025-03-26 | none | Implementation of Edulent educational CPU in SystemVerilog | README (unverified) |
| [Assured/CT-key](https://github.com/Assured/CT-key) | Python (Amaranth/LiteX) | 0 | 2025-05-20 | BSD-2-Clause | — | README (unverified) |
| [eringr/nmigen_fibonacci](https://github.com/eringr/nmigen_fibonacci) | Amaranth | 0 | 2021-10-13 | none | HDL and program for a "processor" that computes fibonacci se | README (unverified) |
| [micki0271/maeri](https://github.com/micki0271/maeri) | Amaranth | 0 | 2020-12-07 | none | 100% FOSS end to end implementation of an ML accelerator com | README (unverified) |
| [anmho/ulx3_bsv](https://github.com/anmho/ulx3_bsv) | Bluespec | 0 | 2024-03-26 | none | 32-Bit RISC-V CPU implemented in Bluespec with pipelining, r | README (unverified) |
| [htfab/asicle2](https://github.com/htfab/asicle2) | SystemVerilog | 0 | 2025-10-30 | Apache-2.0 | Wordle clone for Tiny Tapeout | README (unverified) |
| [abhinavputhran/ttysky-raycast-test](https://github.com/abhinavputhran/ttysky-raycast-test) | SystemVerilog | 0 | 2026-05-01 | Apache-2.0 | — | README (unverified) |
| [antoinevg/hello-ethernet](https://github.com/antoinevg/hello-ethernet) | Amaranth | 0 | 2023-02-19 | none | — | README (unverified) |
| [callummcduff-droid/CPU](https://github.com/callummcduff-droid/CPU) | SystemVerilog | 0 | 2026-09-19 | none | — | README (unverified) |

### D. Forks with substantial own commits (ULX3S ports) — 11 repos

| full_name | lang/HDL | stars | last push | license | what it is | evidence |
|---|---|---|---|---|---|---|
| [gatecat/SNES_MiSTer_ulx3s](https://github.com/gatecat/SNES_MiSTer_ulx3s) | VHDL/Verilog | 16 | 2025-09-05 | GPL-3.0 | SNES for MiSTer | fork, pushed 1959 d after fork (unverified) |
| [emard/SNES_MiSTer_ulx3s](https://github.com/emard/SNES_MiSTer_ulx3s) | VHDL | 1 | 2020-10-25 | GPL-3.0 | SNES for MiSTer | fork, pushed 154 d after fork (unverified) |
| [lawrie/ulx3s-nmigen-examples](https://github.com/lawrie/ulx3s-nmigen-examples) | Amaranth | 12 | 2022-05-05 | none | nMigen examples for the ULX3S board | fork, pushed 563 d after fork (unverified) |
| [LinuxJedi/Minimig_ECS](https://github.com/LinuxJedi/Minimig_ECS) | VHDL | 3 | 2022-05-18 | none | Minimig project example for ULX3S | fork, pushed 21 d after fork (unverified) |
| [cheyao/nes_ecp5](https://github.com/cheyao/nes_ecp5) | SystemVerilog | 2 | 2025-07-27 | none | NES FPGA implementation synthesized for the ulx3s ecp5 based | fork, pushed 35 d after fork (unverified) |
| [machdyne/nes_ecp5](https://github.com/machdyne/nes_ecp5) | SystemVerilog | 0 | 2026-07-22 | none | NES FPGA implementation synthesized for the ulx3s ecp5 based | fork, pushed 349 d after fork (unverified) |
| [cheyao/sega-sms](https://github.com/cheyao/sega-sms) | Verilog | 2 | 2025-09-15 | none | Sega Master System for Ulx3s ECP5 FPGA | fork, pushed 25 d after fork (unverified) |
| [ulx3s/Hazard3](https://github.com/ulx3s/Hazard3) | Verilog | 1 | 2026-09-05 | Apache-2.0 | 3-stage RV32IMACZb* processor with debug, with additional up | fork, pushed 46 d after fork (unverified) |
| [emard/ulx3s_vic_20](https://github.com/emard/ulx3s_vic_20) | Verilog | 1 | 2023-01-22 | none | Minimal Commodore Vic 20 core for the Ulx3s ECP5 board | fork, pushed 991 d after fork (unverified) |
| [danodus/ulx3s_68k](https://github.com/danodus/ulx3s_68k) | ? | 0 | 2024-10-29 | none | Experiments with the 68000 CPU on the Ulx3s ECP5 board | fork, pushed 259 d after fork (unverified) |
| [danodus/ulx3s_sms](https://github.com/danodus/ulx3s_sms) | Verilog | 0 | 2023-06-02 | none | Sega Master System for Ulx3s ECP5 FPGA | fork, pushed 17 d after fork (unverified) |

### E. Repos linked from RadionaOrg/ulx3s-links not otherwise found (ULX3S relevance to check) — 11 repos

| full_name | lang/HDL | stars | last push | license | what it is | evidence |
|---|---|---|---|---|---|---|
| [cbalint13/e-verest](https://github.com/cbalint13/e-verest) | Verilog | 37 | 2023-04-12 | Apache-2.0 | EVEREST: e-Versatile Research Stick for peoples | in ulx3s-links (unverified) |
| [EvgenyMuryshkin/QuokkaEvaluation](https://github.com/EvgenyMuryshkin/QuokkaEvaluation) | Verilog | 37 | 2026-03-04 | none | Example projects for Quokka FPGA toolkit | in ulx3s-links (unverified) |
| [ibm2030/IBM2030](https://github.com/ibm2030/IBM2030) | Rich Text Format | 32 | 2025-11-25 | GPL-3.0 | An IBM System/360 Model 30 in VHDL | in ulx3s-links (unverified) |
| [cube1us/IBM1410FPGA](https://github.com/cube1us/IBM1410FPGA) | VHDL | 3 | 2026-08-21 | none | VHDL Implementation of the IBM 1410 Data Processing System | in ulx3s-links (unverified) |
| [daveshah1/pmods](https://github.com/daveshah1/pmods) | Verilog | 9 | 2019-09-19 | none | PMODs primarily for demo usage with icestorm | in ulx3s-links (unverified) |
| [emard/fpga_snake_game](https://github.com/emard/fpga_snake_game) | VHDL | 6 | 2019-05-06 | none | Simple example of vhdl-verilog mix with vga to hdmi converte | in ulx3s-links (unverified) |
| [emard/prjtrellis-picorv32](https://github.com/emard/prjtrellis-picorv32) | Verilog | 7 | 2019-01-18 | none | attempt to get picorv32 running | in ulx3s-links (unverified) |
| [emard/ledstrip](https://github.com/emard/ledstrip) | VHDL | 3 | 2016-02-10 | none | Example VHDL driver for WS2812 RGB LED pixel strip | in ulx3s-links (unverified) |
| [lawrie/ulx4m_examples](https://github.com/lawrie/ulx4m_examples) | Verilog | 10 | 2022-04-22 | none | Verilog examples for the Ulx4M FPGA board | in ulx3s-links (unverified) |
| [lawrie/ulx4m_amaranth_examples](https://github.com/lawrie/ulx4m_amaranth_examples) | Python (Amaranth/LiteX) | 6 | 2022-05-11 | none | Amaranth HDL examples for the Ulx4m FPGA board | in ulx3s-links (unverified) |
| [rhobbie/Library704](https://github.com/rhobbie/Library704) | C# | 1 | 2026-09-06 | MIT | Verilog simulation of an IBM 704 | in ulx3s-links (unverified) |