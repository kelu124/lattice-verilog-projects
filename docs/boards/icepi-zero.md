---
title: "IcePi Zero"
parent: "ECP5 boards"
grand_parent: "Boards"
nav_order: 5
---
<!-- Generated from data/boards.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# IcePi Zero

Raspberry Pi Zero-sized ECP5 board with HDMI, SDRAM and USB; many ULX3S retro ports target it.

| | |
|---|---|
| Board | IcePi Zero (Raspberry Pi Zero format) |
| FPGA | LFE5U-25F, CABGA256 |
| Evidence | catalogue rows (cheyao__icepi-zero) |
| Clock | 50 MHz (catalogue notes) |
| Catalogued repos | 10 |

*The description is a short summary; FPGA facts come from the catalogue rows cited above.*

## Constraint files (LPF)

Most-copied distinct LPFs for this board in the cloned repos (from the [LPF catalogue](https://github.com/kelu124/lattice-verilog-projects/blob/main/methodology/lpf-catalogue.md)).

| LPF | Revision | Copies | Peripherals constrained |
|---|---|---|---|
| [`icepi-zero.lpf`](https://github.com/cheyao/icepi-zero/blob/e01faa2bd35dcb7269827f8420b845d46c78c869/gateware/blinky/icepi-zero.lpf) (cheyao__icepi-zero) | unknown | 17 | button, gpio-header, hdmi-dvi, led, sdcard, sdram, spi-flash, usb |
| [`icepi-zero.lpf`](https://github.com/bonfireprocessor/bonfire-core/blob/5a797587e6d1d051fa56ede0a5c61c113431b745/fusesoc-cores/fpga/icepizero/icepi-zero.lpf) (bonfireprocessor__bonfire-core) | unknown | 5 | button, gpio-header, hdmi-dvi, led, sdcard, sdram, spi-flash, usb |
| [`icepi-zero.lpf`](https://github.com/cheyao/sega-sms/blob/c37e846d94f88eb9a95f44b15f2b23019aa25a26/icepi-zero/icepi-zero.lpf) (cheyao__sega-sms) | unknown | 3 | button, gpio-header, hdmi-dvi, led, sdcard, sdram, spi-flash, usb |
| [`icepi-zero-v1_2.lpf`](https://github.com/splinedrive/kianRiscV/blob/da994e6c25b0667d6579922f4bab8d800d19e944/linux_socs/LinuxSoC_v2/engineering/boards/icepi-zero/icepi-zero-v1_2.lpf) (splinedrive__kianriscv) | unknown | 2 | button, ftdi-uart, gpio-header, hdmi-dvi, led, sdcard, sdram, spi-flash, usb |
| [`icepi-zero-v1_3.lpf`](https://github.com/splinedrive/kianRiscV/blob/da994e6c25b0667d6579922f4bab8d800d19e944/linux_socs/LinuxSoC_v2/engineering/boards/icepi-zero/icepi-zero-v1_3.lpf) (splinedrive__kianriscv) | unknown | 2 | button, ftdi-uart, gpio-header, hdmi-dvi, led, sdcard, sdram, spi-flash, usb |
| [`board.lpf`](https://github.com/bonfireprocessor/bonfire-core/blob/5a797587e6d1d051fa56ede0a5c61c113431b745/fusesoc-cores/fpga/icepizero/board.lpf) (bonfireprocessor__bonfire-core) | unknown | 1 | ftdi-uart, jtag, led |
| [`board.lpf`](https://github.com/bonfireprocessor/bonfire-ecp5-jtagg-led-demo/blob/7e26a6800684a8f55d6e208c48bb0c2e7970f076/fusesoc/fpga/icepizero/board.lpf) (bonfireprocessor__bonfire-ecp5-jtagg-led-demo) | unknown | 1 | ftdi-uart, led |
| [`icepi-zero-v1_0.lpf`](https://github.com/cheyao/icepi-zero/blob/e01faa2bd35dcb7269827f8420b845d46c78c869/gateware/v1.0/icepi-zero-v1_0.lpf) (cheyao__icepi-zero) | unknown | 1 | button, gpio-header, hdmi-dvi, led, sdcard, sdram, spi-flash, usb |
| [`icepi-zero-v1_1.lpf`](https://github.com/cheyao/icepi-zero/blob/e01faa2bd35dcb7269827f8420b845d46c78c869/gateware/v1.1/icepi-zero-v1_1.lpf) (cheyao__icepi-zero) | unknown | 1 | button, gpio-header, hdmi-dvi, led, sdcard, sdram, spi-flash, usb |
| [`icepi-zero-v1_2.lpf`](https://github.com/cheyao/icepi-zero/blob/e01faa2bd35dcb7269827f8420b845d46c78c869/gateware/v1.2/icepi-zero-v1_2.lpf) (cheyao__icepi-zero) | unknown | 1 | button, gpio-header, hdmi-dvi, led, sdcard, sdram, spi-flash, usb |
| [`icepi-zero.lpf`](https://github.com/alangarf/apple-one/blob/0f15ef6d62c2f8820aa5a68b7f973eef4a78dd8d/boards/icepi_zero/yosys/icepi-zero.lpf) (alangarf__apple-one) | unknown | 1 | button, gpio-header, hdmi-dvi, led, sdcard, sdram, spi-flash, usb |
| [`icepi-zero.lpf`](https://github.com/cheyao/icepi-zero/blob/e01faa2bd35dcb7269827f8420b845d46c78c869/gateware/third-party/dvi/hdl/icepi-zero.lpf) (cheyao__icepi-zero) | unknown | 1 | button, ftdi-uart, gpio-header, hdmi-dvi, led, sdcard, sdram, spi-flash, usb |

## Reusable cores seen on this board

Cores whose source repo, or a repo that copies/instantiates them, targets this board.

| Core | Function | Source repo |
|---|---|---|
| no2bootloader (Nitro) iCE40 UP5K DFU bootloader | [bootloader-dfu](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/bootloader-dfu.md) | no2fpga__no2bootloader |
| no2usb DFU runtime + dfu_helper.v (iCE40) | [bootloader-dfu](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/bootloader-dfu.md) | smunaut__ice40-playground |
| TV80 Z80-compatible core (emard__ulx3s_galaksija copy) | [cpu-retro](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-retro.md) | emard__ulx3s_galaksija |
| PicoRV32 RISC-V core | [cpu-riscv](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-riscv.md) | yosyshq__picorv32 |
| Sigma-delta DAC (up5k-demos) | [dac](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/dac.md) | daveshah1__up5k-demos |
| ESP32 SPI OSD + spirw_slave ROM/disk loading stack | [esp32-osd](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/esp32-osd.md) | lawrie__ulx3s_sms |
| HDMI TX with audio (danodus ecp5_hdmi_audio_video) | [hdmi-dvi](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/hdmi-dvi.md) | danodus__ecp5_hdmi_audio_video |
| vga2dvid + tmds_encoder DVI/TMDS core (Mike Field / EMARD) | [hdmi-dvi](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/hdmi-dvi.md) | emard__ulx3s-misc |
| Bonfire ECP5 JTAGG bridge + MyHDL LED demo | [jtag-debug](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/jtag-debug.md) | bonfireprocessor__bonfire-ecp5-jtagg-led-demo |
| Vernier-RV32 RV32IMA Linux-capable Wishbone SoC | [linux](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/linux.md) | aravindrajeshkanna__vernier-rv32 |
| ecp5pll parametric PLL | [pll-clock](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/pll-clock.md) | emard__ulx3s-misc |
| ps2kbd + ps2mouse (EMARD) | [ps2](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/ps2.md) | emard__ulx3s-misc |
| Oberon SDRAM_16bit controller + cache | [sdram](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/sdram.md) | emard__oberon |
| LAYR_AUDIO SID6581 sound chip core | [sound-chips](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/sound-chips.md) | thorkn__layr_audio |
| SN76489 PSG (sound chip) | [sound-chips](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/sound-chips.md) | lawrie__ulx3s_sms |
| glasgow SPI controller (Amaranth) | [spi](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/spi.md) | glasgowembedded__glasgow |
| lcd_video / spi_display multi-panel SPI LCD driver | [spi-display](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/spi-display.md) | emard__ulx3s-misc |
| no2usb-derived ECP5 USB FS device core (had2019 bootloader) | [usb-device](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/usb-device.md) | emard__had2019-playground |
| Ultra-Embedded USB FS host (ulx3s-misc copy) | [usb-host](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/usb-host.md) | emard__ulx3s-misc |
| emard USB host + gamepad report decoders | [usb-host](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/usb-host.md) | emard__nes_ecp5 |

## Projects targeting this board

- [alangarf__apple-one](https://github.com/alangarf/apple-one): Multi-board
- [bonfireprocessor__bonfire-ecp5-jtagg-led-demo](https://github.com/bonfireprocessor/bonfire-ecp5-jtagg-led-demo): Standalone MyHDL/FuseSoC demo wrapping the ECP5 JTAGG primitive to shift an LED pattern via the JTAG USER1/2 data…
- [cheyao__icepi-zero](https://github.com/cheyao/icepi-zero): Icepi Zero: Raspberry-Pi-Zero-form-factor ECP5-25F board explicitly inspired by ULX3S;
- [cheyao__nes_ecp5](https://github.com/cheyao/nes_ecp5): NES (MiST-derived core) for ULX3S/ULX4M/icepi-zero via open toolchain, with ESP32 SD-card OSD loader
- [cheyao__oberon](https://github.com/cheyao/oberon): Project Oberon
- [cheyao__sega-sms](https://github.com/cheyao/sega-sms): Sega Master System core;
- [danodus__ecp5_hdmi_audio_video](https://github.com/danodus/ecp5_hdmi_audio_video): ULX3S/IcePi Zero: HDMI audio+video transmitter core ([review](https://github.com/kelu124/lattice-verilog-projects/blob/main/projects/danodus__ecp5_hdmi_audio_video.md))
- [danodus__onramp-fpga](https://github.com/danodus/onramp-fpga): Onramp-FPGA: 32-bit \"Onramp\" processor SoC
- [danodus__xgsoc](https://github.com/danodus/xgsoc): XGSoC: RISC-V
- [no2fpga__no2bootloader](https://github.com/no2fpga/no2bootloader): Nitro Bootloader: iCE40 UP5K DFU bootloader
{% endraw %}
