---
title: "Cynthion"
parent: "ECP5 boards"
grand_parent: "Boards"
nav_order: 8
---
<!-- Generated from data/boards.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# Cynthion

USB 2.0 test instrument: three ULPI high-speed USB PHYs, HyperRAM, 2 PMODs; programmed through the Apollo debug MCU. Home of the LUNA USB gateware (analyzer, Facedancer, USB host experiments).

| | |
|---|---|
| Board | Great Scott Gadgets Cynthion |
| FPGA | LFE5U-12F, BG256 |
| Evidence | cynthion board files (r0.1–r1.4), see the TinyFPGA EX / ECPIX-5 / Cynthion survey |
| Clock | 60 MHz (board files) |
| Catalogued repos | 8 |

*The description is a short summary; FPGA facts come from the catalogue rows cited above.*

## Constraint files (LPF)

Most-copied distinct LPFs for this board in the cloned repos (from the [LPF catalogue](https://github.com/kelu124/lattice-verilog-projects/blob/main/methodology/lpf-catalogue.md)).

| LPF | Revision | Copies | Peripherals constrained |
|---|---|---|---|
| [`cynthion_pins.lpf`](https://github.com/VoltCyclone/HurricaneFPGA/blob/6f0b109cf0ab1ad77ee7670693e3d1a6aa11cab5/HDL/hardware/constraints/cynthion_pins.lpf) (voltcyclone__hurricanefpga) | unknown | 1 | ftdi-uart, led, usb |

## Reusable cores seen on this board

Cores whose source repo, or a repo that copies/instantiates them, targets this board.

| Core | Function | Source repo |
|---|---|---|
| Cynthion USB Audio Class 2.0 example | [audio-digital](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/audio-digital.md) | greatscottgadgets__cynthion-uac |
| LUNA-SoC VexRiscv SoC framework (Moondancer's CPU) | [cpu-riscv](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-riscv.md) | greatscottgadgets__luna-soc |
| VexRiscv (SpinalHDL-generated Verilog) | [cpu-riscv](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-riscv.md) | rschlaikjer__fpga-3-softcores |
| glasgow I2C core (Amaranth) | [i2c](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/i2c.md) | glasgowembedded__glasgow |
| Cynthion USB analyzer (used by Packetry) | [jtag-debug](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/jtag-debug.md) | greatscottgadgets__cynthion |
| katsuo.pcie ECP5 SERDES PHY + PCIe endpoint stack | [serdes-links](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/serdes-links.md) | zyp__katsuo-pcie |
| glasgow SPI controller (Amaranth) | [spi](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/spi.md) | glasgowembedded__glasgow |
| hdl4fpga USB 1.1 device core | [usb-device](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/usb-device.md) | hdl4fpga__hdl4fpga |
| HurricaneFPGA plain-Verilog USB host engine | [usb-host](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/usb-host.md) | voltcyclone__hurricanefpga |
| guh USB2 HS/FS host SIE + enumerator | [usb-host](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/usb-host.md) | apfaudio__guh |
| hdl4fpga USB 1.1 host core | [usb-host](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/usb-host.md) | hdl4fpga__hdl4fpga |
| hurra-fpga bounded USB FS mouse host | [usb-host](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/usb-host.md) | voltcyclone__hurra-fpga |

## Projects targeting this board

- [antoinevg__cynthion-tutorials](https://github.com/antoinevg/cynthion-tutorials): cynthion-tutorials: Amaranth tutorials for Cynthion/ECPIX-5
- [apfaudio__guh](https://github.com/apfaudio/guh): guh: Amaranth USB2 HS/FS host engine library
- [greatscottgadgets__cynthion](https://github.com/greatscottgadgets/cynthion): Cynthion: official GSG gateware
- [greatscottgadgets__cynthion-uac](https://github.com/greatscottgadgets/cynthion-uac): cynthion-uac: official USB Audio Class 2.0 example gateware for Cynthion
- [greatscottgadgets__luna](https://github.com/greatscottgadgets/luna): LUNA: Amaranth USB 2.0/3.0 gateware framework
- [greatscottgadgets__luna-soc](https://github.com/greatscottgadgets/luna-soc): LUNA-SoC: Amaranth Wishbone/CSR SoC framework
- [voltcyclone__hurra-fpga](https://github.com/VoltCyclone/hurra-fpga): hurra-fpga: Amaranth bounded USB FS mouse host+device-clone relay for Cynthion r1.4, with report injection and…
- [voltcyclone__hurricanefpga](https://github.com/VoltCyclone/HurricaneFPGA): HurricaneFPGA: plain-Verilog Cynthion gateware - USB FS/LS sniffer/passthrough, USB host mode
{% endraw %}
