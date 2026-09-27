---
name: reusable-cores
description: Cross-project map of the reusable ULX3S building blocks (PLL, DVI/HDMI, ESP32 OSD, USB host, SDRAM, displays, CPUs) and which repo has the best copy — first stop when helping someone build a new design.
metadata:
  type: reference
---

From the 2026-09-27 survey of 226 repos (details in `docs/catalogue.md`, source `catalogue.tsv`).
Paths are relative to `original_sources/<slug>/`. Licenses matter; see [[catalogue-fields]].

| Need | Best source (language, license) | Also |
|---|---|---|
| Parametric ECP5 PLL | emard__ulx3s-misc `examples/ecp5pll/hdl/{sv,vhd}/ecp5pll` (SV/VHDL, BSD header) | copied into many lawrie/splinedrive repos |
| DVI/HDMI out (TMDS) | emard__ulx3s-misc `examples/dvi/hdl/{vga2dvid,tmds_encoder}.vhd` + `fake_differential.v` (BSD) | Verilog: lawrie__apple-one `rtl/boards/ulx3s/` (Apache-2.0), splinedrive__my_hdmi_device (ISC), doctorwkt tic-tac-toe `HDMI/` (GPL-3.0), Silice `projects/common/hdmi.si` (MIT) |
| HDMI with audio | emard__papilio-arcade `scramble_rel001_papilio/source/vga/` av_hdmi (VHDL) | — |
| ESP32 SPI OSD + ROM/disk loading | lawrie__ulx3s_sms `src/osd/` (osd.v, spi_osd.v, spirw_slave_v.v) + `esp32/osd` MicroPython; same stack in nes_ecp5, trs_80, apple2fpga | the de-facto way to load games/disks from SD via the ESP32 |
| ESP32 ↔ FPGA SPI RAM | emard__uk101onfpga `rtl_emard/spi_ram/spi_ram_slave.vhd`; ulx3s-misc `examples/spi_ram` | — |
| USB 1.1 HID host (US2: keyboard/gamepad) | emard__ulx3s-misc `examples/usb/usbhost` (usbh_sie.v, usbh_host_hid) (mixed, GPL/MIT parts) | Verilog + gamepad decoders: emard__nes_ecp5 `usb/`; VHDL: hdl4fpga `library/usb` |
| USB device (CDC serial) | ulx3s-misc `examples/usb/usbcdc` (VHDL); osresearch__spispy `verilog/usb/` (TinyFPGA stack, Verilog) | f32c `rtl/soc/usb_serial` |
| SDRAM controller | ulx3s-misc `examples/sdram/` (pnru, mist, 16bit, memtest_mister); lawrie__ulx3s_examples `sdram16/sdram.v` (none found) | Linux-grade: splinedrive__kianriscv `engineering/sdram/` (ISC/Apache); cache: emard__oberon `hdl/cache_controller.v`; VHDL: f32c `rtl/soc/sdram*.vhd` (BSD-2) |
| ST7789 / SSD1331 / SSD1351 displays | ulx3s-misc `examples/spi_display/hdl` (Verilog+VHDL) | lawrie__ulx3s_examples `st7789/`; Silice `oled_*.si`; SpinalHDL: lawrie__slabboy `ST7789.scala` |
| PS/2 keyboard/mouse | lawrie__ulx3s_examples `ps2/`, `ps2port/` | ulx3s-misc `examples/ps2` |
| Audio | SPDIF: f32c `rtl/soc/spdif_tx.vhd` (BSD-2); I2S: ulx3s-misc `examples/audio`; PSG: lawrie__ulx3s_sms `src/sn76489.v` | synth: emard__synthowheel (BSD) |
| FM / RDS transmitter | ulx3s-misc `examples/fm/hdl`; f32c `rtl/soc/fm/` | emard__rdsfpga is ULX2S-only |
| Ethernet (LAN8720 RMII on GP/GN 9–13) | ulx3s-misc `examples/eth/rmii`; hdl4fpga `library/mii` (full ARP/IP/UDP/DHCP stack, VHDL, Diamond) | — |
| Onboard ADC MAX11125 | ulx3s-misc `examples/adc` | hdl4fpga ScopeIO oscilloscope |
| CPUs | Z80 tv80 (many); 6502: chrismoos__m6502 (SV, MIT, verified by tests); RISC-V: picorv32 (fpga-odysseus), kianV (Linux), Silice fire-v/ice-v, NEORV32 (VHDL, BSD-3, no ULX3S target in repo), VexRiscv via LiteX; RISC-V/MIPS: f32c (BSD-2); 68000 fx68k (lawrie examples); TMS99000 (pnru__ti99, public domain); CDP1802 SpinalHDL | — |
| Linux on ULX3S | linux-on-litex-vexriscv (`./make.py --board=ulx3s`); kianV (85F); SaxonSoc (docker recipes stale since 2020) | — |

Cross-project facts:
- **The emard "universal make" build system** (`scripts/trellis_main.mk` + `diamond_main.mk`, `FPGA_SIZE=12|25|45|85`)
  appears in ulx3s-misc, galaksija, oberon, apple2fpga, papilio-arcade, etc. It often hard-codes tool paths
  (`/mt/scratch/tmp/openfpga`), so override `TRELLIS`/path variables when building.
- **Diamond-only historical ports**: f32c, minimig, papilio-arcade, vhdl_phoenix, next186, uk101, hdl4fpga, bonfire, synthowheel.
  Porting them to the open flow usually means ghdl-yosys-plugin (VHDL). f32c's own trellis attempts are marked not working.
- **`--25k` + `--idcode 0x21111043`** is a common trick: build for 25k and load it on a 12F (same die).
- Many ulx3s.github.io entries have two copies; the preferred ones are recorded in `catalogue.tsv` `fork_of`.

**How to apply:** when a user wants to build X, look up X here first, check its license, then open the repo's
row in `docs/catalogue.md`. Add rows here whenever a review finds a better or new reusable block.
