---
title: "Cores by function"
nav_order: 2
has_children: true
permalink: "/functions/"
---
<!-- Generated from data/functions.json, data/cores.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# Cores by function

Every reusable core found in the collection, grouped by function. Each function page lists the best core first, then alternatives, with links to the original files upstream (at the commit that was reviewed) and the other projects that copy or instantiate the core.

## Video

| Function | Best core | Alternatives | Projects using these cores |
|---|---|---|---|
| [HDMI / DVI output](hdmi-dvi.md) | vga2dvid + tmds_encoder DVI/TMDS core (Mike Field / EMARD) (emard__ulx3s-misc) | 5 | 106 |
| [VGA and video timing](vga.md) | Apple 1 VGA text-mode framebuffer core (vga/vram/font_rom) (lawrie__apple-one) | 5 | 5 |
| [Composite video (CVBS)](composite-video.md) | f32c PAL composite video (CVBS) generator (f32c__f32c) | 1 | 1 |
| [SPI OLED / LCD displays](spi-display.md) | lcd_video / spi_display multi-panel SPI LCD driver (emard__ulx3s-misc) | 5 | 27 |
| [ESP32 OSD and loading](esp32-osd.md) | ESP32 SPI OSD + spirw_slave ROM/disk loading stack (lawrie__ulx3s_sms) | 3 | 33 |
| [Camera input](camera.md) | OV7670 camera capture + SCCB config core (msrraju07__iop) | 4 | 4 |

## Memory and storage

| Function | Best core | Alternatives | Projects using these cores |
|---|---|---|---|
| [SDRAM controllers](sdram.md) | hdl4fpga generation-generic SDRAM controller (hdl4fpga__hdl4fpga) | 5 | 6 |
| [DDR3 memory](ddr-memory.md) | Lightweight DDR3 AXI4 memory controller (ECP5) (ultraembedded__orangecrab) | 2 | 4 |
| [PSRAM and HyperRAM](psram-hyperram.md) | Hackaday badge QPI-PSRAM PHY + cache (ECP5-native) (spritetm__hadbadge2019_fpgasoc) | 3 | 1 |
| [SD card](sd-card.md) | ZipCPU sdspi SPI-mode SD controller (zipcpu__sdspi) | 4 | 1 |
| [SPI flash](spi-flash.md) | spimemio SPI/QSPI flash XIP controller (yosyshq__picorv32) | 4 | 9 |

## Interfaces

| Function | Best core | Alternatives | Projects using these cores |
|---|---|---|---|
| [UART](uart.md) | wbuart Wishbone UART (asinghani__pifive-cpu) | 4 | 1 |
| [SPI master / slave](spi.md) | APB SPI master (microSD) (ulx3s__hazard3) | 3 | 8 |
| [I2C](i2c.md) | verilog-i2c (alexforencich) (asinghani__pifive-cpu) | 3 | 2 |
| [USB device](usb-device.md) | no2usb-derived ECP5 USB FS device core (had2019 bootloader) (emard__had2019-playground) | 5 | 20 |
| [USB host](usb-host.md) | Ultra-Embedded USB FS host (ulx3s-misc copy) (emard__ulx3s-misc) | 7 | 17 |
| [Bootloaders and DFU](bootloader-dfu.md) | ULX3S/ULX4M USB DFU bootloader (had2019-playground) (emard__had2019-playground) | 2 | 3 |
| [Ethernet](ethernet.md) | mii_ipoe ARP/IP/UDP/DHCP stack (hdl4fpga__hdl4fpga) | 4 | 3 |
| [PCIe, SATA and SERDES links](serdes-links.md) | LiteSATA ECP5 SATA PHY + core (enjoy-digital__litesata) | 8 | 7 |
| [PS/2 keyboard and mouse](ps2.md) | ps2_intf keyboard decoder (lawrie__ulx3s_examples) | 3 | 13 |
| [JTAG and debug](jtag-debug.md) | OpenCores JTAG TAP + JTAGG bridge (emard__ulx3s-misc) | 6 | 0 |
| [Buses and interconnect](bus-fabric.md) | wb_intercon Wishbone mux/arbiter (olofk) (kulp__tenyr) | 2 | 7 |

## Audio, analog and radio

| Function | Best core | Alternatives | Projects using these cores |
|---|---|---|---|
| [ADC](adc.md) | MAX1112x ADC reader (ulx3s-misc) (emard__ulx3s-misc) | 3 | 2 |
| [DAC, PWM and sigma-delta](dac.md) | Sigma-delta PCM audio DAC (fpga-dac) (machdyne__fpga-dac) | 4 | 24 |
| [I2S and S/PDIF](audio-digital.md) | I2S audio interface (ulx3s-misc) (emard__ulx3s-misc) | 6 | 12 |
| [Sound chips and synths](sound-chips.md) | SN76489 PSG (sound chip) (lawrie__ulx3s_sms) | 4 | 10 |
| [Radio (FM/RDS, SDR)](radio.md) | 1-bit AM transceiver chain (ULX3S-proven) (jamesrosssharp__1_bit_am) | 5 | 4 |
| [DSP](dsp.md) | Waveform-generator DDS sine core (AXI-Stream, cocotb-tested) (semify-eda__waveform-generator) | 6 | 5 |

## Processors and systems

| Function | Best core | Alternatives | Projects using these cores |
|---|---|---|---|
| [RISC-V CPUs and SoCs](cpu-riscv.md) | PicoRV32 RISC-V core (yosyshq__picorv32) | 7 | 40 |
| [Retro CPUs](cpu-retro.md) | cpu_6502 (Klaus Dormann-verified 6502 core) (chrismoos__m6502) | 6 | 33 |
| [Linux-capable SoCs](linux.md) | linux-on-litex-vexriscv (ULX3S board target) (litex-hub__linux-on-litex-vexriscv) | 4 | 0 |

## Clocks and misc

| Function | Best core | Alternatives | Projects using these cores |
|---|---|---|---|
| [PLLs and clocking](pll-clock.md) | ecp5pll parametric PLL (emard__ulx3s-misc) | 3 | 82 |
| [LED drivers](led-drivers.md) | HUB75(e) LED matrix driver (fpga_led_display) (w531t4__fpga_led_display) | 4 | 7 |
| [Crypto and hashing](crypto.md) | yaaes AES core (VHDL, cocotb/vunit tested) (marph91__yaaes) | 3 | 0 |
{% endraw %}
