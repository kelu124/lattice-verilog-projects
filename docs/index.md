---
title: "Home"
nav_order: 1
permalink: "/"
---
<!-- Generated from data/pages/index.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# ulx3s-klod: open gateware for the ULX3S and small Lattice boards

A knowledge base of **open gateware for the [ULX3S](https://github.com/emard/ulx3s) FPGA board** (Radiona, Lattice ECP5 LFE5U-12F/25F/45F/85F) and, for reuse, other small Lattice boards (ECP5, iCE40 UP5K, iCE40 HX8K/HX4K). It records which projects exist, what their gateware does, which FPGA and toolchain they target, their license, whether they have testbenches, and which blocks can be lifted into a new design.

Use it to **find prior art before writing a core**: a DVI encoder, a USB device, an SDRAM or HyperRAM controller, a RISC-V SoC, an ESP32 on-screen display, a retro computer… Start with the [reusable cores map](https://github.com/kelu124/ulx3s-klod/blob/main/.claude/memory/reusable-cores.md), then the catalogue and the project pages below.

Every page here is generated from JSON in [`data/`](https://github.com/kelu124/ulx3s-klod/tree/main/data) (do not edit `docs/` by hand); the repo also holds Claude's working memory, see the [README](https://github.com/kelu124/ulx3s-klod/blob/main/README.md).

## Browse

**153 reusable cores** in 33 functions, used by 189 of the 376 catalogued repos; 16 board pages; 18 in-depth reviews.

| Area | Functions |
|---|---|
| Video | [HDMI / DVI output](functions/hdmi-dvi.md), [VGA and video timing](functions/vga.md), [Composite video (CVBS)](functions/composite-video.md), [SPI OLED / LCD displays](functions/spi-display.md), [ESP32 OSD and loading](functions/esp32-osd.md), [Camera input](functions/camera.md) |
| Memory and storage | [SDRAM controllers](functions/sdram.md), [DDR3 memory](functions/ddr-memory.md), [PSRAM and HyperRAM](functions/psram-hyperram.md), [SD card](functions/sd-card.md), [SPI flash](functions/spi-flash.md) |
| Interfaces | [UART](functions/uart.md), [SPI master / slave](functions/spi.md), [I2C](functions/i2c.md), [USB device](functions/usb-device.md), [USB host](functions/usb-host.md), [Bootloaders and DFU](functions/bootloader-dfu.md), [Ethernet](functions/ethernet.md), [PS/2 keyboard and mouse](functions/ps2.md), [JTAG and debug](functions/jtag-debug.md), [Buses and interconnect](functions/bus-fabric.md) |
| Audio, analog and radio | [ADC](functions/adc.md), [DAC, PWM and sigma-delta](functions/dac.md), [I2S and S/PDIF](functions/audio-digital.md), [Sound chips and synths](functions/sound-chips.md), [Radio (FM/RDS, SDR)](functions/radio.md), [DSP](functions/dsp.md) |
| Processors and systems | [RISC-V CPUs and SoCs](functions/cpu-riscv.md), [Retro CPUs](functions/cpu-retro.md), [Linux-capable SoCs](functions/linux.md) |
| Clocks and misc | [PLLs and clocking](functions/pll-clock.md), [LED drivers](functions/led-drivers.md), [Crypto and hashing](functions/crypto.md) |

- [Boards](boards): [ULX3S](boards/ulx3s.md), [ULX4M](boards/ulx4m.md), [OrangeCrab](boards/orangecrab.md), [Colorlight 5A-75B/E, i5, i9](boards/colorlight.md), [IcePi Zero](boards/icepi-zero.md), [iCESugar-Pro](boards/icesugar-pro.md), [iCEBreaker](boards/icebreaker.md), [UPduino](boards/upduino.md), [iCESugar](boards/icesugar.md), [Fomu](boards/fomu.md), [pico-ice](boards/pico-ice.md), [iCE40-HX8K Breakout](boards/hx8k-breakout.md), [BlackIce II / Mx](boards/blackice.md), [iceFUN](boards/icefun.md), [Olimex iCE40HX8K-EVB](boards/olimex-hx8k.md), [IcoBoard](boards/icoboard.md)
- [Guides](guides): [Build and load](guides/toolchain.md), [Porting iCE40 to ECP5](guides/porting-ice40-to-ecp5.md), [USB DFU](guides/DFUs.md)
- [Project reviews](projects) · [Methodology and data](methodology)
{% endraw %}
