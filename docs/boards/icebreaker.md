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
| Catalogued repos | 32 |

*The description is a short summary; FPGA facts come from the catalogue rows cited above.*

## Constraint files (PCF)

| PCF | Repository |
|---|---|
| [`constraints/icebreaker.pcf`](https://github.com/agamez/whisperice/blob/970e0802d9e3e5a96c4dfb55adf069bd22555793/constraints/icebreaker.pcf) | agamez__whisperice |
| [`docs/hardware/icebreaker-examples_cb9e674c.pcf`](https://github.com/agamez/whisperice/blob/970e0802d9e3e5a96c4dfb55adf069bd22555793/docs/hardware/icebreaker-examples_cb9e674c.pcf) | agamez__whisperice |
| [`gateware/boards/icebreaker/pinmap.pcf`](https://github.com/apfaudio/eurorack-pmod/blob/ddb9aa92fab7f74783f7ed3bf248eec56a6ceb00/gateware/boards/icebreaker/pinmap.pcf) | apfaudio__eurorack-pmod |
| [`work/hwtst/icebreaker/icebreaker.pcf`](https://github.com/bnossum/midgetv/blob/f05ade6b088d6c714120a2a61c1606567bd940f0/work/hwtst/icebreaker/icebreaker.pcf) | bnossum__midgetv |
| [`work/hwtst/icebreaker/icecube_icebreaker.pcf`](https://github.com/bnossum/midgetv/blob/f05ade6b088d6c714120a2a61c1606567bd940f0/work/hwtst/icebreaker/icecube_icebreaker.pcf) | bnossum__midgetv |
| [`hardware/icebreaker/icebreaker.pcf`](https://github.com/dan-rodrigues/icestation-32/blob/55214d79f74a547dedb54f99cb2fad431b7ac277/hardware/icebreaker/icebreaker.pcf) | dan-rodrigues__icestation-32 |
| [`lcd_test_icebreaker/icebreaker.pcf`](https://github.com/daveshah1/pmods/blob/1631e86be4c181c19dd5bab44565895bb488db37/lcd_test_icebreaker/icebreaker.pcf) | daveshah1__pmods |
| [`examples/icebreaker/pmod_7seg9_1/icebreaker.pcf`](https://github.com/fm4dd/pmod-7seg9/blob/cbb13936851b4dc347c57e458461bcb4013c49d3/examples/icebreaker/pmod_7seg9_1/icebreaker.pcf) | fm4dd__pmod-7seg9 |
| [`examples/icebreaker/pmod_7seg9_2/icebreaker.pcf`](https://github.com/fm4dd/pmod-7seg9/blob/cbb13936851b4dc347c57e458461bcb4013c49d3/examples/icebreaker/pmod_7seg9_2/icebreaker.pcf) | fm4dd__pmod-7seg9 |
| [`examples/ulx3s/display/icebreaker.pcf`](https://github.com/fm4dd/pmod-charlcd/blob/5e0ee0a37d8395f72ac5764c1a0e4d6af37b010b/examples/ulx3s/display/icebreaker.pcf) | fm4dd__pmod-charlcd |
| [`examples/icebreaker/pmod_charlcd/icebreaker.pcf`](https://github.com/fm4dd/pmod-charlcd/blob/5e0ee0a37d8395f72ac5764c1a0e4d6af37b010b/examples/icebreaker/pmod_charlcd/icebreaker.pcf) | fm4dd__pmod-charlcd |
| [`examples/icebreaker/display/icebreaker.pcf`](https://github.com/fm4dd/pmod-charlcd/blob/5e0ee0a37d8395f72ac5764c1a0e4d6af37b010b/examples/icebreaker/display/icebreaker.pcf) | fm4dd__pmod-charlcd |

## Reusable cores seen on this board

Cores whose source repo, or a repo that copies/instantiates them, targets this board.

| Core | Function | Source repo |
|---|---|---|
| AK4619 audio codec driver + PMOD I2C master | [audio-digital](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/audio-digital.md) | apfaudio__eurorack-pmod |
| S/PDIF transmitter (synthowheel) | [audio-digital](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/audio-digital.md) | emard__synthowheel |
| TinyFPGA USB Bootloader (USB-serial-to-SPI-flash bridge) | [bootloader-dfu](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/bootloader-dfu.md) | tinyfpga__tinyfpga-bootloader |
| no2bootloader (Nitro) iCE40 UP5K DFU bootloader | [bootloader-dfu](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/bootloader-dfu.md) | no2fpga__no2bootloader |
| no2usb DFU runtime + dfu_helper.v (iCE40) | [bootloader-dfu](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/bootloader-dfu.md) | smunaut__ice40-playground |
| AHB-Lite crossbar/arbiter/APB bridge | [bus-fabric](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/bus-fabric.md) | ulx3s__hazard3 |
| wb_intercon Wishbone mux/arbiter (olofk) | [bus-fabric](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/bus-fabric.md) | kulp__tenyr |
| PicoRV32 RISC-V core | [cpu-riscv](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-riscv.md) | yosyshq__picorv32 |
| VexRiscv (SpinalHDL-generated Verilog) | [cpu-riscv](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-riscv.md) | rschlaikjer__fpga-3-softcores |
| Resistor+PWM hybrid DAC (dacpwm) | [dac](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/dac.md) | emard__ulx3s-misc |
| CORDIC sin/cos core | [dsp](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/dsp.md) | osresearch__up5k |
| CORDIC-1 bit-serial CORDIC/DDS sine engine | [dsp](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/dsp.md) | joaln27__cordic |
| ZipCPU SDR CORDIC + CIC + AM/FM demodulator chain | [dsp](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/dsp.md) | zipcpu__sdr |
| esp32_spi_gamepad minimal ESP32 SPI state receiver | [esp32-osd](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/esp32-osd.md) | dan-rodrigues__ulx3s-bluetooth-gamepad |
| smoldvi small portable DVI core | [hdmi-dvi](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/hdmi-dvi.md) | wren6991__smoldvi |
| vga2dvid + tmds_encoder DVI/TMDS core (Mike Field / EMARD) | [hdmi-dvi](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/hdmi-dvi.md) | emard__ulx3s-misc |
| ORBTrace SWD/JTAG debug + parallel TRACE core (legacy plain-Verilog flow) | [jtag-debug](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/jtag-debug.md) | orbcode__orbtrace |
| PWM/PDM gamma-corrected LED brightness drivers | [led-drivers](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/led-drivers.md) | kbob__icebreaker-candy |
| no2hub75 HUB75 panel core (no2fpga library) | [led-drivers](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/led-drivers.md) | smunaut__ice40-playground |
| ecp5pll parametric PLL | [pll-clock](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/pll-clock.md) | emard__ulx3s-misc |
| no2fpga HyperRAM controller (no2hyperbus) | [psram-hyperram](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/psram-hyperram.md) | smunaut__ice40-playground |
| WSPR 4-FSK beacon codec (message/FEC/interleave/symbols/modulator) | [radio](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/radio.md) | agamez__whisperice |
| LAYR_AUDIO SID6581 sound chip core | [sound-chips](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/sound-chips.md) | thorkn__layr_audio |
| SPI master (Bus Pirate NextGen Ultra) | [spi](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/spi.md) | dangerousprototypes__buspirateultrahdl |
| PMOD CharLCD HD44780 driver (debounce + transmit) | [spi-display](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/spi-display.md) | fm4dd__pmod-charlcd |
| RasteriCEr SPI display controller | [spi-display](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/spi-display.md) | toni3141__rastericer |
| SSD1322 OLED framebuffer driver (m68k-ulx3s) | [spi-display](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/spi-display.md) | nullobject__m68k-ulx3s |
| spimemio SPI/QSPI flash XIP controller | [spi-flash](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/spi-flash.md) | yosyshq__picorv32 |
| hdl4fpga USB 1.1 device core | [usb-device](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/usb-device.md) | hdl4fpga__hdl4fpga |
| no2usb-derived ECP5 USB FS device core (had2019 bootloader) | [usb-device](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/usb-device.md) | emard__had2019-playground |
| Ultra-Embedded USB FS host (ulx3s-misc copy) | [usb-host](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/usb-host.md) | emard__ulx3s-misc |
| vga_core / vga_timing portable VGA generator (Black Mesa Labs) | [vga](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/vga.md) | icebreaker-fpga__icebreaker-verilog-examples |

## Projects targeting this board

32 catalogued repos target this board; see the [full catalogue](https://github.com/kelu124/lattice-verilog-projects/blob/main/methodology/catalogue.md). Those with a full review:

- [smunaut__ice40-playground](https://github.com/kelu124/lattice-verilog-projects/blob/main/projects/smunaut__ice40-playground.md): iCEBreaker: collection of iCE40 UP5K IP cores
- [wren6991__smoldvi](https://github.com/kelu124/lattice-verilog-projects/blob/main/projects/wren6991__smoldvi.md): iCEBreaker/iCEstick/iCESugar/TinyFPGA-BX: SmolDVI, a small direct DVI/TMDS output core
- [yosyshq__picorv32](https://github.com/kelu124/lattice-verilog-projects/blob/main/projects/yosyshq__picorv32.md): PicoRV32: size-optimized RISC-V
{% endraw %}
