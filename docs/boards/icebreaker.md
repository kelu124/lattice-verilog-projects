---
title: "iCEBreaker"
parent: "iCE40 UP5K boards"
grand_parent: "Boards"
nav_order: 1
---
<!-- Generated from data/boards.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# iCEBreaker

The reference open-source UP5K board, with PMOD ports and many workshop examples.

| | |
|---|---|
| Board | iCEBreaker (1BitSquared) |
| FPGA | iCE40 UP5K, SG48 |
| Evidence | catalogue rows (icebreaker-fpga__*) |
| Clock | 12 MHz (catalogue notes) |
| Catalogued repos | 20 |

*The description is a short summary; FPGA facts come from the catalogue rows cited above.*

## Constraint files (PCF)

| PCF | Repository |
|---|---|
| [`gateware/boards/icebreaker/pinmap.pcf`](https://github.com/apfaudio/eurorack-pmod/blob/ddb9aa92fab7f74783f7ed3bf248eec56a6ceb00/gateware/boards/icebreaker/pinmap.pcf) | apfaudio__eurorack-pmod |
| [`work/hwtst/icebreaker/icebreaker.pcf`](https://github.com/bnossum/midgetv/blob/f05ade6b088d6c714120a2a61c1606567bd940f0/work/hwtst/icebreaker/icebreaker.pcf) | bnossum__midgetv |
| [`work/hwtst/icebreaker/icecube_icebreaker.pcf`](https://github.com/bnossum/midgetv/blob/f05ade6b088d6c714120a2a61c1606567bd940f0/work/hwtst/icebreaker/icecube_icebreaker.pcf) | bnossum__midgetv |
| [`hardware/icebreaker/icebreaker.pcf`](https://github.com/dan-rodrigues/icestation-32/blob/55214d79f74a547dedb54f99cb2fad431b7ac277/hardware/icebreaker/icebreaker.pcf) | dan-rodrigues__icestation-32 |
| [`icebreaker/icebreaker.pcf`](https://codeberg.org/icebreaker-fpga/icebreaker-verilog-examples/src/commit/8d0892bf62dd5d8ae59c48c882d9ebebd1cab9c2/icebreaker/icebreaker.pcf) | icebreaker-fpga__icebreaker-verilog-examples |
| [`stopwatch-dual/icebreaker.pcf`](https://codeberg.org/icebreaker-fpga/icebreaker-workshop/src/commit/0ccd1f27c0bcdd81d9c15961a2bccd0a4d81a761/stopwatch-dual/icebreaker.pcf) | icebreaker-fpga__icebreaker-workshop |
| [`stopwatch/icebreaker.pcf`](https://codeberg.org/icebreaker-fpga/icebreaker-workshop/src/commit/0ccd1f27c0bcdd81d9c15961a2bccd0a4d81a761/stopwatch/icebreaker.pcf) | icebreaker-fpga__icebreaker-workshop |
| [`soc/ice-twang/data/top-icebreaker.pcf`](https://codeberg.org/icebreaker-fpga/icetwang/src/commit/a4915ff538be621d8cab4a9d82c555ee8627e0c3/soc/ice-twang/data/top-icebreaker.pcf) | icebreaker-fpga__icetwang |
| [`data/icebreaker.pcf`](https://github.com/jamchamb/cojiro/blob/e00438f6ec90ab3adf61e3a405557a37a3d9e827/data/icebreaker.pcf) | jamchamb__cojiro |
| [`icebreaker.pcf`](https://github.com/kbob/icebreaker-candy/blob/e3c09f357b5f4862751aba7ea337a82cfa4f20e0/icebreaker.pcf) | kbob__icebreaker-candy |
| [`hw/icebreaker_spi.pcf`](https://github.com/nickmqb/fpga_craft/blob/d77083d5771385a92807ce3a34750e23b8e03ee4/hw/icebreaker_spi.pcf) | nickmqb__fpga_craft |
| [`gateware/icE1usb-proto/data/top-icebreaker.pcf`](https://github.com/osmocom/osmo-e1-hardware/blob/85acea8b6d656add7c098d51f816f4ac34084fa2/gateware/icE1usb-proto/data/top-icebreaker.pcf) | osmocom__osmo-e1-hardware |

## Reusable cores seen on this board

Cores whose source repo, or a repo that copies/instantiates them, targets this board.

| Core | Function | Source repo |
|---|---|---|
| AK4619 audio codec driver + PMOD I2C master | [audio-digital](https://github.com/kelu124/ulx3s-klod/blob/main/functions/audio-digital.md) | apfaudio__eurorack-pmod |
| S/PDIF transmitter (synthowheel) | [audio-digital](https://github.com/kelu124/ulx3s-klod/blob/main/functions/audio-digital.md) | emard__synthowheel |
| no2usb DFU runtime + dfu_helper.v (iCE40) | [bootloader-dfu](https://github.com/kelu124/ulx3s-klod/blob/main/functions/bootloader-dfu.md) | smunaut__ice40-playground |
| AHB-Lite crossbar/arbiter/APB bridge | [bus-fabric](https://github.com/kelu124/ulx3s-klod/blob/main/functions/bus-fabric.md) | ulx3s__hazard3 |
| wb_intercon Wishbone mux/arbiter (olofk) | [bus-fabric](https://github.com/kelu124/ulx3s-klod/blob/main/functions/bus-fabric.md) | kulp__tenyr |
| PicoRV32 RISC-V core | [cpu-riscv](https://github.com/kelu124/ulx3s-klod/blob/main/functions/cpu-riscv.md) | yosyshq__picorv32 |
| VexRiscv (SpinalHDL-generated Verilog) | [cpu-riscv](https://github.com/kelu124/ulx3s-klod/blob/main/functions/cpu-riscv.md) | rschlaikjer__fpga-3-softcores |
| Resistor+PWM hybrid DAC (dacpwm) | [dac](https://github.com/kelu124/ulx3s-klod/blob/main/functions/dac.md) | emard__ulx3s-misc |
| CORDIC sin/cos core | [dsp](https://github.com/kelu124/ulx3s-klod/blob/main/functions/dsp.md) | osresearch__up5k |
| esp32_spi_gamepad minimal ESP32 SPI state receiver | [esp32-osd](https://github.com/kelu124/ulx3s-klod/blob/main/functions/esp32-osd.md) | dan-rodrigues__ulx3s-bluetooth-gamepad |
| smoldvi small portable DVI core | [hdmi-dvi](https://github.com/kelu124/ulx3s-klod/blob/main/functions/hdmi-dvi.md) | wren6991__smoldvi |
| vga2dvid + tmds_encoder DVI/TMDS core (Mike Field / EMARD) | [hdmi-dvi](https://github.com/kelu124/ulx3s-klod/blob/main/functions/hdmi-dvi.md) | emard__ulx3s-misc |
| ORBTrace SWD/JTAG debug + parallel TRACE core (legacy plain-Verilog flow) | [jtag-debug](https://github.com/kelu124/ulx3s-klod/blob/main/functions/jtag-debug.md) | orbcode__orbtrace |
| PWM/PDM gamma-corrected LED brightness drivers | [led-drivers](https://github.com/kelu124/ulx3s-klod/blob/main/functions/led-drivers.md) | kbob__icebreaker-candy |
| no2hub75 HUB75 panel core (no2fpga library) | [led-drivers](https://github.com/kelu124/ulx3s-klod/blob/main/functions/led-drivers.md) | smunaut__ice40-playground |
| ecp5pll parametric PLL | [pll-clock](https://github.com/kelu124/ulx3s-klod/blob/main/functions/pll-clock.md) | emard__ulx3s-misc |
| no2fpga HyperRAM controller (no2hyperbus) | [psram-hyperram](https://github.com/kelu124/ulx3s-klod/blob/main/functions/psram-hyperram.md) | smunaut__ice40-playground |
| RasteriCEr SPI display controller | [spi-display](https://github.com/kelu124/ulx3s-klod/blob/main/functions/spi-display.md) | toni3141__rastericer |
| SSD1322 OLED framebuffer driver (m68k-ulx3s) | [spi-display](https://github.com/kelu124/ulx3s-klod/blob/main/functions/spi-display.md) | nullobject__m68k-ulx3s |
| spimemio SPI/QSPI flash XIP controller | [spi-flash](https://github.com/kelu124/ulx3s-klod/blob/main/functions/spi-flash.md) | yosyshq__picorv32 |
| hdl4fpga USB 1.1 device core | [usb-device](https://github.com/kelu124/ulx3s-klod/blob/main/functions/usb-device.md) | hdl4fpga__hdl4fpga |
| no2usb-derived ECP5 USB FS device core (had2019 bootloader) | [usb-device](https://github.com/kelu124/ulx3s-klod/blob/main/functions/usb-device.md) | emard__had2019-playground |
| Ultra-Embedded USB FS host (ulx3s-misc copy) | [usb-host](https://github.com/kelu124/ulx3s-klod/blob/main/functions/usb-host.md) | emard__ulx3s-misc |
| vga_core / vga_timing portable VGA generator (Black Mesa Labs) | [vga](https://github.com/kelu124/ulx3s-klod/blob/main/functions/vga.md) | icebreaker-fpga__icebreaker-verilog-examples |

## Projects targeting this board

- [apfaudio__eurorack-pmod](https://github.com/apfaudio/eurorack-pmod): Eurorack PMOD: AK4619 audio-codec PMOD gateware
- [bnossum__midgetv](https://github.com/bnossum/midgetv): iCEBreaker/UPduino2: midgetv - compact Wishbone-B4 RV32I RISC-V core
- [dan-rodrigues__icestation-32](https://github.com/dan-rodrigues/icestation-32): icestation-32: compact retro FPGA game console, secondary port to ULX3S
- [emeb__up5k_osc](https://github.com/emeb/up5k_osc): iCE40 UP5K custom Eurorack module
- [icebreaker-fpga__icebreaker-verilog-examples](https://codeberg.org/icebreaker-fpga/icebreaker-verilog-examples): iCEBreaker: collection of small Verilog examples
- [icebreaker-fpga__icebreaker-workshop](https://codeberg.org/icebreaker-fpga/icebreaker-workshop): iCEBreaker: self-directed educational workshop building a BCD stopwatch/counter driven onto a 7-segment Pmod display,…
- [icebreaker-fpga__icetwang](https://codeberg.org/icebreaker-fpga/icetwang): iCEBreaker-bitsy: iCEtwang, a TWANG-inspired 1D LED-strip game console SoC
- [jamchamb__cojiro](https://github.com/jamchamb/cojiro): iCEBreaker: Nintendo JoyBus device emulator - simulates an N64 controller with ephemeral Controller Pak, a Pokemon Snap…
- [kbob__icebreaker-candy](https://github.com/kbob/icebreaker-candy): iCEBreaker: eye-candy demos driving a 64x64 HUB75 RGB LED panel
- [lawrie__hdmi_examples](https://github.com/lawrie/hdmi_examples): iCE40 open-source HDMI/DVI examples for BlackIce II: hdmi_test/_ibr/_mx
- [nickmqb__fpga_craft](https://github.com/nickmqb/fpga_craft): iCE40 UP5K
- [orbcode__orbtrace](https://github.com/orbcode/orbtrace): ORBTrace: Cortex-M SWD/JTAG debug + parallel TRACE probe gateware
- [osmocom__osmo-e1-hardware](https://github.com/osmocom/osmo-e1-hardware): icE1usb / osmo-e1-tracer: E1/T1 telecom interface product family gateware for iCE40 UP5K boards - icE1usb USB-E1 dongle
- [osresearch__up5k](https://github.com/osresearch/up5k): UPduino v2: standalone iCE40 UltraPlus5K Verilog demos - blink, RGB pulse, UART serial/echo, SPRAM buffered echo,…
- [smunaut__ice40-playground](https://github.com/smunaut/ice40-playground): iCEBreaker: collection of iCE40 UP5K IP cores ([review](https://github.com/kelu124/ulx3s-klod/blob/main/projects/smunaut__ice40-playground.md))
- [smunaut__ice40linux](https://github.com/smunaut/iCE40linux): iCEBreaker: Linux-on-RISC-V SoC gateware
- [toni3141__rastericer](https://github.com/ToNi3141/RasteriCEr): iCE40 UP5K
- [wren6991__riscboy](https://github.com/Wren6991/RISCBoy): RISCBoy: portable games console SoC - Hazard5 RV32IMC CPU, PPU graphics pipeline, AHB-Lite bus fabric, UART/GPIO;
- [wren6991__smoldvi](https://github.com/Wren6991/SmolDVI): iCEBreaker/iCEstick/iCESugar/TinyFPGA-BX: SmolDVI, a small direct DVI/TMDS output core ([review](https://github.com/kelu124/ulx3s-klod/blob/main/projects/wren6991__smoldvi.md))
- [yosyshq__picorv32](https://github.com/YosysHQ/picorv32): PicoRV32: size-optimized RISC-V ([review](https://github.com/kelu124/ulx3s-klod/blob/main/projects/yosyshq__picorv32.md))
{% endraw %}
