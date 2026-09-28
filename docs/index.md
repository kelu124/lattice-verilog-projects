---
title: "Home"
nav_order: 1
permalink: "/"
---
<!-- Generated from data/pages/index.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# ulx3s-klod: open gateware for the ULX3S and small Lattice boards

Reusable **open gateware for the [ULX3S](https://github.com/emard/ulx3s) FPGA board** (Radiona, Lattice ECP5 LFE5U-12F/25F/45F/85F) and other small Lattice boards (ECP5, iCE40 UP5K, iCE40 HX8K/HX4K), organised **by function**. For each function (HDMI, VGA, SDRAM, SD card, USB, UART, SPI, I2C, ADC, DAC, audio, radio, CPUs…) it gives the best core found in 376 open-source repos, the alternatives, links to the original files at the reviewed commit, their license and FPGA primitives, and the other projects that use them.

Use it to **find prior art before writing a core**. Start from [Cores by function](functions/index.md); check the [board page](boards/index.md) for pin maps; read the [guides](guides/index.md) to build, load and port; the [in-depth reviews](projects/index.md) document the richest repos block by block.

Facts cite the upstream file at a pinned commit; nothing was built or simulated, and anything not verified is marked `unknown`. Check each core's license before reusing it. Every page is generated from the JSON in [`data/`](https://github.com/kelu124/ulx3s-klod/tree/main/data) by the scripts described in the [methodology](methodology/index.md).

## Browse

**155 reusable cores** in 33 functions, used by 191 of the 377 catalogued repos; 16 board pages; 19 in-depth reviews.

| Area | Functions |
|---|---|
| Video | [HDMI / DVI output](functions/hdmi-dvi.md), [VGA and video timing](functions/vga.md), [Composite video (CVBS)](functions/composite-video.md), [SPI OLED / LCD displays](functions/spi-display.md), [ESP32 OSD and loading](functions/esp32-osd.md), [Camera input](functions/camera.md) |
| Memory and storage | [SDRAM controllers](functions/sdram.md), [DDR3 memory](functions/ddr-memory.md), [PSRAM and HyperRAM](functions/psram-hyperram.md), [SD card](functions/sd-card.md), [SPI flash](functions/spi-flash.md) |
| Interfaces | [UART](functions/uart.md), [SPI master / slave](functions/spi.md), [I2C](functions/i2c.md), [USB device](functions/usb-device.md), [USB host](functions/usb-host.md), [Bootloaders and DFU](functions/bootloader-dfu.md), [Ethernet](functions/ethernet.md), [PS/2 keyboard and mouse](functions/ps2.md), [JTAG and debug](functions/jtag-debug.md), [Buses and interconnect](functions/bus-fabric.md) |
| Audio, analog and radio | [ADC](functions/adc.md), [DAC, PWM and sigma-delta](functions/dac.md), [I2S and S/PDIF](functions/audio-digital.md), [Sound chips and synths](functions/sound-chips.md), [Radio (FM/RDS, SDR)](functions/radio.md), [DSP](functions/dsp.md) |
| Processors and systems | [RISC-V CPUs and SoCs](functions/cpu-riscv.md), [Retro CPUs](functions/cpu-retro.md), [Linux-capable SoCs](functions/linux.md) |
| Clocks and misc | [PLLs and clocking](functions/pll-clock.md), [LED drivers](functions/led-drivers.md), [Crypto and hashing](functions/crypto.md) |

- [Boards](boards/index.md): [ULX3S](boards/ulx3s.md), [ULX4M](boards/ulx4m.md), [OrangeCrab](boards/orangecrab.md), [Colorlight 5A-75B/E, i5, i9](boards/colorlight.md), [IcePi Zero](boards/icepi-zero.md), [iCESugar-Pro](boards/icesugar-pro.md), [iCEBreaker](boards/icebreaker.md), [UPduino](boards/upduino.md), [iCESugar](boards/icesugar.md), [Fomu](boards/fomu.md), [pico-ice](boards/pico-ice.md), [iCE40-HX8K Breakout](boards/hx8k-breakout.md), [BlackIce II / Mx](boards/blackice.md), [iceFUN](boards/icefun.md), [Olimex iCE40HX8K-EVB](boards/olimex-hx8k.md), [IcoBoard](boards/icoboard.md)
- [Guides](guides/index.md): [Build and load](guides/toolchain.md), [Porting iCE40 to ECP5](guides/porting-ice40-to-ecp5.md), [USB DFU](guides/DFUs.md)
- [Project reviews](projects/index.md) · [Methodology and data](methodology/index.md) · [Contribute](contributing.md)
{% endraw %}
