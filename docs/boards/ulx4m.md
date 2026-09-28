---
title: "ULX4M"
parent: "ECP5 boards"
grand_parent: "Boards"
nav_order: 2
---
<!-- Generated from data/boards.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# ULX4M

ULX3S successor in Raspberry Pi CM4 module format; most ULX3S designs port with the ulx4m_v002.lpf constraint file.

| | |
|---|---|
| Board | Radiona ULX4M (CM4-format ECP5 module) |
| FPGA | LFE5UM-85F (ECP5-5G) on the variants catalogued |
| Evidence | catalogue rows (e.g. lawrie__ulx4m_examples) |
| Clock | unknown |
| Catalogued repos | 18 |

*The description is a short summary; FPGA facts come from the catalogue rows cited above.*

## Constraint files (LPF)

Most-copied distinct LPFs for this board in the cloned repos (from the [LPF catalogue](https://github.com/kelu124/lattice-verilog-projects/blob/main/methodology/lpf-catalogue.md)).

| LPF | Revision | Copies | Peripherals constrained |
|---|---|---|---|
| [`ulx4m_v002.lpf`](https://github.com/lawrie/apple-one/blob/40412e90909378db3bd84b7537196ed8799fa477/boards/ulx4m/yosys/ulx4m_v002.lpf) (lawrie__apple-one) | v0.0.2 (file name) | 6 | button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, rtc-power, sdcard, sdram, spi-flash, switch, usb |
| [`ulx4m_v002.lpf`](https://github.com/danodus/ulx3s_sms/blob/13c2361a5039d205de47857bab9201055ac9e566/ulx4m/ulx4m_v002.lpf) (danodus__ulx3s_sms) | v0.0.2 (file name) | 2 | button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, rtc-power, sdcard, sdram, spi-flash, switch, usb |
| [`fpga_ulx4m_ld.lpf`](https://github.com/ulx3s/Hazard3/blob/3c0aca063517bb7fdbe869019c984954c7dd5c97/example_soc/synth/fpga_ulx4m_ld.lpf) (ulx3s__hazard3) | unknown | 1 | ddr3, ftdi-uart, hdmi-dvi, led, sdcard |
| [`fpga_ulx4m_ld_blinky.lpf`](https://github.com/ulx3s/Hazard3/blob/3c0aca063517bb7fdbe869019c984954c7dd5c97/example_soc/synth/fpga_ulx4m_ld_blinky.lpf) (ulx3s__hazard3) | unknown | 1 | led |
| [`fpga_ulx4m_ld_v002.lpf`](https://github.com/ulx3s/Hazard3/blob/3c0aca063517bb7fdbe869019c984954c7dd5c97/example_soc/synth/fpga_ulx4m_ld_v002.lpf) (ulx3s__hazard3) | v0.0.2 (file name) | 1 | ddr3, ftdi-uart, hdmi-dvi, led |
| [`fpga_ulx4m_ls.lpf`](https://github.com/ulx3s/Hazard3/blob/3c0aca063517bb7fdbe869019c984954c7dd5c97/example_soc/synth/fpga_ulx4m_ls.lpf) (ulx3s__hazard3) | unknown | 1 | ftdi-uart, hdmi-dvi, led, sdram |
| [`top-ulx4m-v002.lpf`](https://github.com/emard/had2019-playground/blob/0723f2a536b20f26ec1b2d5cf1dcc2b5355b6808/projects/bootloader/data/top-ulx4m-v002.lpf) (emard__had2019-playground) | v0.0.2 (file name) | 1 | button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, rtc-power, sdcard, sdram, spi-flash, switch, usb |
| [`top-ulx4m-v002.lpf`](https://github.com/ulx3s/Hazard3-Doom/blob/42621599f78f7ce3bd51fcc6b95a56ba83e31279/bootloader/data/top-ulx4m-v002.lpf) (ulx3s__hazard3-doom) | v0.0.2 (file name) | 1 | button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, rtc-power, sdcard, sdram, spi-flash, switch, usb |
| [`top_passthru-ulx4m-v002.lpf`](https://github.com/emard/had2019-playground/blob/0723f2a536b20f26ec1b2d5cf1dcc2b5355b6808/projects/bootloader/data/top_passthru-ulx4m-v002.lpf) (emard__had2019-playground) | v0.0.2 (file name) | 1 | button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, rtc-power, sdcard, sdram, spi-flash, switch, usb |
| [`top_passthru-ulx4m-v002.lpf`](https://github.com/ulx3s/Hazard3-Doom/blob/42621599f78f7ce3bd51fcc6b95a56ba83e31279/bootloader/data/top_passthru-ulx4m-v002.lpf) (ulx3s__hazard3-doom) | v0.0.2 (file name) | 1 | button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, rtc-power, sdcard, sdram, spi-flash, switch, usb |
| [`ulx4m_ld.lpf`](https://github.com/hdl4fpga/hdl4fpga/blob/662986ba0f17b7ce3a066ddcb799d42fa1b24dea/boards/ULX4M_LD/diamond/ulx4m_ld.lpf) (hdl4fpga__hdl4fpga) | unknown | 1 | button, ddr3, ethernet, ftdi-uart, hdmi-dvi, i2c, led, rtc-power, sdcard, usb |
| [`ulx4m_ls.lpf`](https://github.com/hdl4fpga/hdl4fpga/blob/662986ba0f17b7ce3a066ddcb799d42fa1b24dea/boards/ULX4M_LS/diamond/ulx4m_ls.lpf) (hdl4fpga__hdl4fpga) | unknown | 1 | button, camera, ethernet, ftdi-uart, gpio-header, hdmi-dvi, i2c, led, rtc-power, sdcard, sdram, spi-flash, switch, usb |

## Reusable cores seen on this board

Cores whose source repo, or a repo that copies/instantiates them, targets this board.

| Core | Function | Source repo |
|---|---|---|
| MAX1112x ADC reader (ulx3s-emi copy) | [adc](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/adc.md) | emard__ulx3s-emi |
| MAX1112x ADC reader (ulx3s-misc) | [adc](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/adc.md) | emard__ulx3s-misc |
| I2S audio interface (ulx3s-misc) | [audio-digital](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/audio-digital.md) | emard__ulx3s-misc |
| S/PDIF transmitter (synthowheel) | [audio-digital](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/audio-digital.md) | emard__synthowheel |
| Hazard3-Doom vendored DFU bootloader (ULX4M-LD validated) | [bootloader-dfu](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/bootloader-dfu.md) | ulx3s__hazard3-doom |
| ULX3S/ULX4M USB DFU bootloader (had2019-playground) | [bootloader-dfu](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/bootloader-dfu.md) | emard__had2019-playground |
| AHB-Lite crossbar/arbiter/APB bridge | [bus-fabric](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/bus-fabric.md) | ulx3s__hazard3 |
| TV80 Z80-compatible core (emard__ulx3s_galaksija copy) | [cpu-retro](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-retro.md) | emard__ulx3s_galaksija |
| grom toy 8-bit CPU + computer (FPGA 101 original) | [cpu-retro](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-retro.md) | mmicko__fpga101-workshop |
| i8080-compatible core (Bashkiria-2M-derived) | [cpu-retro](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-retro.md) | lawrie__ulx3s_examples |
| Hazard3 RV32IMAC core | [cpu-riscv](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-riscv.md) | wren6991__hazard3 |
| PicoRV32 RISC-V core | [cpu-riscv](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-riscv.md) | yosyshq__picorv32 |
| VexRiscv (SpinalHDL-generated Verilog) | [cpu-riscv](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-riscv.md) | rschlaikjer__fpga-3-softcores |
| Resistor+PWM hybrid DAC (dacpwm) | [dac](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/dac.md) | emard__ulx3s-misc |
| Sigma-delta DAC (up5k-demos) | [dac](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/dac.md) | daveshah1__up5k-demos |
| ESP32 SPI OSD + spirw_slave ROM/disk loading stack | [esp32-osd](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/esp32-osd.md) | lawrie__ulx3s_sms |
| SPI RAM slave (ESP32 <-> FPGA memory-mapped link) | [esp32-osd](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/esp32-osd.md) | emard__uk101onfpga |
| RMII hex-dump packet sniffer | [ethernet](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/ethernet.md) | emard__ulx3s-misc |
| smoldvi small portable DVI core | [hdmi-dvi](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/hdmi-dvi.md) | wren6991__smoldvi |
| vga2dvid + tmds_encoder DVI/TMDS core (Mike Field / EMARD) | [hdmi-dvi](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/hdmi-dvi.md) | emard__ulx3s-misc |
| SAO I2C command engine | [i2c](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/i2c.md) | ulx3s__hazard3 |
| OpenCores JTAG TAP + JTAGG bridge | [jtag-debug](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/jtag-debug.md) | emard__ulx3s-misc |
| 64x64 LED panel scanner (ledscan) | [led-drivers](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/led-drivers.md) | goran-mahovlic__prjtrellis-led64x64 |
| ecp5pll parametric PLL | [pll-clock](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/pll-clock.md) | emard__ulx3s-misc |
| ps2_intf keyboard decoder | [ps2](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/ps2.md) | lawrie__ulx3s_examples |
| ps2kbd + ps2mouse (EMARD) | [ps2](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/ps2.md) | emard__ulx3s-misc |
| FM stereo transmitter with RDS | [radio](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/radio.md) | emard__ulx3s-misc |
| sdram_pnru simplistic SDRAM controller | [sdram](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/sdram.md) | emard__ulx3s-misc |
| SN76489 PSG (sound chip) | [sound-chips](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/sound-chips.md) | lawrie__ulx3s_sms |
| APB SPI master (microSD) | [spi](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/spi.md) | ulx3s__hazard3 |
| SlabBoy ST7789 SpinalHDL LCD driver | [spi-display](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/spi-display.md) | lawrie__slabboy |
| lcd_video / spi_display multi-panel SPI LCD driver | [spi-display](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/spi-display.md) | emard__ulx3s-misc |
| Wishbone Quad-SPI flash controller (Gisselquist-derived) | [spi-flash](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/spi-flash.md) | emard__ulx3s-misc |
| qspi_phy_ecp5 QSPI flash PHY (ECP5-native) | [spi-flash](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/spi-flash.md) | emard__had2019-playground |
| SAO UART phy (minimal 8N1) | [uart](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/uart.md) | ulx3s__hazard3 |
| circuit-killer USB FS serial device (VHDL, ULX3S-built) | [usb-device](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/usb-device.md) | circuit-killer__fpga-usbserial |
| f32c USB CDC-ACM device + soft PHY | [usb-device](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/usb-device.md) | f32c__f32c |
| no2usb-derived ECP5 USB FS device core (had2019 bootloader) | [usb-device](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/usb-device.md) | emard__had2019-playground |
| ulx3s-misc USB CDC-ACM device (VHDL) | [usb-device](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/usb-device.md) | emard__ulx3s-misc |
| Ultra-Embedded USB FS host (ulx3s-misc copy) | [usb-host](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/usb-host.md) | emard__ulx3s-misc |

## Projects targeting this board

- [alangarf__apple-one](https://github.com/alangarf/apple-one): Multi-board
- [cheyao__nes_ecp5](https://github.com/cheyao/nes_ecp5): NES (MiST-derived core) for ULX3S/ULX4M/icepi-zero via open toolchain, with ESP32 SD-card OSD loader
- [danodus__ulx3s_sms](https://github.com/danodus/ulx3s_sms): Sega Master System core for ULX3S and ULX4M, HDMI/VGA out, ESP32 OSD ROM loader
- [emard__had2019-playground](https://github.com/emard/had2019-playground): HAD2019 badge playground
- [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc): ULX3S misc/advanced examples: EMARD's building-block library ([review](https://github.com/kelu124/lattice-verilog-projects/blob/main/projects/emard__ulx3s-misc.md))
- [lawrie__apple-one](https://github.com/lawrie/apple-one): Apple 1 Verilog, ULX3S HDMI + PS/2 + UART
- [lawrie__jupiter_ace](https://github.com/lawrie/jupiter_ace): Jupiter Ace
- [lawrie__ulx3s_acorn_atom](https://github.com/lawrie/ulx3s_acorn_atom): Acorn Atom 8-bit home computer core ported to ULX3S
- [lawrie__ulx3s_amstrad_cpc](https://github.com/lawrie/ulx3s_amstrad_cpc): Amstrad CPC 664 emulation
- [lawrie__ulx3s_atari_2600](https://github.com/lawrie/ulx3s_atari_2600): Atari 2600
- [lawrie__ulx3s_colecovision](https://github.com/lawrie/ulx3s_colecovision): ColecoVision game console core for ULX3S, also ported to a distinct 'ulx4m' board variant
- [lawrie__ulx3s_sms](https://github.com/lawrie/ulx3s_sms): Sega Master System / SG-1000: TV80, VDP, SN76489, SDRAM carts, ESP32 OSD ([review](https://github.com/kelu124/lattice-verilog-projects/blob/main/projects/lawrie__ulx3s_sms.md))
- [lawrie__ulx3s_zx81](https://github.com/lawrie/ulx3s_zx81): ZX80/ZX81: TV80, HDMI scandoubler, PS/2, ear/audio
- [lawrie__ulx4m_amaranth_examples](https://github.com/lawrie/ulx4m_amaranth_examples): Amaranth HDL examples for the ULX4M board: blinky, DVI, SDRAM16, Conway life, mitecpu, PS/2, OLED, audio
- [lawrie__ulx4m_examples](https://github.com/lawrie/ulx4m_examples): Verilog examples for the ULX4M board: blinky, HDMI/DVI, SDRAM, softcore CPUs, GPI2 game demos
- [trabucayre__openfpgaloader](https://github.com/trabucayre/openFPGALoader): openFPGALoader universal programmer ([review](https://github.com/kelu124/lattice-verilog-projects/blob/main/projects/trabucayre__openfpgaloader.md))
- [ulx3s__hazard3](https://github.com/ulx3s/Hazard3): Hazard3 RV32IMACZb* CPU: ULX3S/ULX4M-LD fork with dedicated build docs, incl.
- [ulx3s__hazard3-doom](https://github.com/ulx3s/Hazard3-Doom): ulx3s/Hazard3-Doom: Doom
{% endraw %}
