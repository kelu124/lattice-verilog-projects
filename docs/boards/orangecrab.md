---
title: "OrangeCrab"
parent: "ECP5 boards"
grand_parent: "Boards"
nav_order: 3
---
<!-- Generated from data/boards.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# OrangeCrab

Feather-format ECP5 board with DDR3 and native USB; DFU bootloader.

| | |
|---|---|
| Board | OrangeCrab (Feather format) |
| FPGA | LFE5U-25F or 85F, CSFBGA285 |
| Evidence | catalogue rows (orangecrab-fpga__orangecrab-examples, emeb__orangecrab_adc) |
| Clock | unknown |
| Catalogued repos | 9 |

*The description is a short summary; FPGA facts come from the catalogue rows cited above.*

## Constraint files (LPF)

Most-copied distinct LPFs for this board in the cloned repos (from the [LPF catalogue](https://github.com/kelu124/ulx3s-klod/blob/main/methodology/lpf-catalogue.md)).

| LPF | Revision | Copies | Peripherals constrained |
|---|---|---|---|
| [`orangecrab.lpf`](https://github.com/hsa-ees/piconut/blob/826460dc12cd22c2b6e177182b9d63abdc1eabe0/boards/orangecrab/orangecrab.lpf) (hsa-ees__piconut) | unknown | 2 | ftdi-uart |
| [`OrangeCrab.lpf`](https://github.com/stnolting/neorv32-setups/blob/57f86d5ad3fa54f6919165b7bcc61fad9a5cae0a/osflow/constraints/OrangeCrab.lpf) (stnolting__neorv32-setups) | unknown | 1 | spi-flash |
| [`ocadc.lpf`](https://github.com/emeb/orangecrab_adc/blob/daa94e19abb11e3cee3bc1e97d87908b6da1e08a/gateware/verilog/trellis/ocadc.lpf) (emeb__orangecrab_adc) | unknown | 1 | adc, button, led, usb |
| [`orangecrab.lpf`](https://github.com/hdl4fpga/hdl4fpga/blob/662986ba0f17b7ce3a066ddcb799d42fa1b24dea/boards/orangecrab/diamond/orangecrab.lpf) (hdl4fpga__hdl4fpga) | unknown | 1 | ddr3, gpio-header, led, usb |
| [`orangecrab_r02.lpf`](https://github.com/fusesoc/blinky/blob/496eae5e447151c1ca720f995d292e2e99349b22/orangecrab/orangecrab_r02.lpf) (fusesoc__blinky) | unknown | 1 | button |
| [`pinout.lpf`](https://github.com/sylefeb/Silice/blob/620487d6b83035dd98299734c8c8fccf8f636005/frameworks/boards/orangecrab/pinout.lpf) (sylefeb__silice) | unknown | 1 | led |

## Reusable cores seen on this board

Cores whose source repo, or a repo that copies/instantiates them, targets this board.

| Core | Function | Source repo |
|---|---|---|
| Digital down-converter + AM/FM demod chain (post-ADC) | [adc](https://github.com/kelu124/ulx3s-klod/blob/main/functions/adc.md) | emeb__orangecrab_adc |
| I2S receiver (orangecrab-usb) | [audio-digital](https://github.com/kelu124/ulx3s-klod/blob/main/functions/audio-digital.md) | mangelajo__orangecrab-usb |
| Lightweight AXI-4 DDR3 controller + ECP5 PHY | [ddr-memory](https://github.com/kelu124/ulx3s-klod/blob/main/functions/ddr-memory.md) | ultraembedded__core_ddr3_controller |
| Lightweight DDR3 AXI4 memory controller (ECP5) | [ddr-memory](https://github.com/kelu124/ulx3s-klod/blob/main/functions/ddr-memory.md) | ultraembedded__orangecrab |
| CIC decimator + FIR decimation filter | [dsp](https://github.com/kelu124/ulx3s-klod/blob/main/functions/dsp.md) | emeb__orangecrab_adc |
| glasgow I2C core (Amaranth) | [i2c](https://github.com/kelu124/ulx3s-klod/blob/main/functions/i2c.md) | glasgowembedded__glasgow |
| ecp5pll parametric PLL | [pll-clock](https://github.com/kelu124/ulx3s-klod/blob/main/functions/pll-clock.md) | emard__ulx3s-misc |
| katsuo.pcie ECP5 SERDES PHY + PCIe endpoint stack | [serdes-links](https://github.com/kelu124/ulx3s-klod/blob/main/functions/serdes-links.md) | zyp__katsuo-pcie |
| glasgow SPI controller (Amaranth) | [spi](https://github.com/kelu124/ulx3s-klod/blob/main/functions/spi.md) | glasgowembedded__glasgow |
| hdl4fpga USB 1.1 device core | [usb-device](https://github.com/kelu124/ulx3s-klod/blob/main/functions/usb-device.md) | hdl4fpga__hdl4fpga |

## Projects targeting this board

- [emeb__orangecrab_adc](https://github.com/emeb/orangecrab_adc): OrangeCrab ADC FeatherWing: AD9203 10-bit/40MSPS ADC + audio board, gateware for SDR tuning/AM demodulation
- [fdarling__orangecrab-usb-cdc-demo](https://github.com/fdarling/orangecrab-usb-cdc-demo): OrangeCrab: minimal USB CDC
- [greatscottgadgets__luna](https://github.com/greatscottgadgets/luna): LUNA: Amaranth USB 2.0/3.0 gateware framework
- [hsa-ees__piconut](https://github.com/hsa-ees/piconut): PicoNut: minimal, extensible RISC-V
- [mangelajo__orangecrab-usb](https://github.com/mangelajo/orangecrab-usb): OrangeCrab: two USB device examples
- [openconcepts-ar__accel2d](https://github.com/openconcepts-ar/accel2d): accel2d: C-to-Verilog
- [orangecrab-fpga__orangecrab-examples](https://github.com/orangecrab-fpga/orangecrab-examples): OrangeCrab: example projects - RISC-V/VexRiscv firmware, plain Verilog
- [tallenintegsys__hdmi-orangecrab](https://github.com/tallenintegsys/hdmi-orangecrab): OrangeCrab: HDMI video+audio transmitter, porting Sameer Puri's hdl-util/hdmi IP to Lattice ECP5 via yosys+synlig…
- [ultraembedded__orangecrab](https://github.com/ultraembedded/orangecrab): OrangeCrab: DDR3 128MB read/write memory test gateware ([review](https://github.com/kelu124/ulx3s-klod/blob/main/projects/ultraembedded__orangecrab.md))
{% endraw %}
