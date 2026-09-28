---
title: "ECPIX-5"
parent: "ECP5 boards"
grand_parent: "Boards"
nav_order: 7
---
<!-- Generated from data/boards.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# ECPIX-5

ECP5-5G board with DDR3, RGMII Ethernet, HDMI (IT6613), a SATA port driven by LiteSATA over the SERDES, SD, ULPI USB and 8 PMODs; programmed with openFPGALoader -b ecpix5.

| | |
|---|---|
| Board | LambdaConcept ECPIX-5 |
| FPGA | LFE5UM5G-45F or LFE5UM5G-85F (ECP5-5G, with SERDES), BG554 |
| Evidence | LiteX / Amaranth board files, see the TinyFPGA EX / ECPIX-5 / Cynthion survey |
| Clock | 100 MHz (board files) |
| Catalogued repos | 10 |

*The description is a short summary; FPGA facts come from the catalogue rows cited above.*

## Constraint files (LPF)

Most-copied distinct LPFs for this board in the cloned repos (from the [LPF catalogue](https://github.com/kelu124/lattice-verilog-projects/blob/main/methodology/lpf-catalogue.md)).

| LPF | Revision | Copies | Peripherals constrained |
|---|---|---|---|
| [`ecpix5.lpf`](https://github.com/sylefeb/Silice/blob/620487d6b83035dd98299734c8c8fccf8f636005/frameworks/boards/ecpix5/ecpix5.lpf) (sylefeb__silice) | unknown | 1 | ftdi-uart, led |
| [`fpga.lpf`](https://github.com/ultraembedded/core_ddr3_controller/blob/a03492a6000ca0185c615060b171bda64806a7bb/examples/ecpix_ecp5/fpga.lpf) (ultraembedded__core_ddr3_controller) | unknown | 1 | ddr3 |
| [`pinmap.lpf`](https://github.com/apfaudio/eurorack-pmod/blob/ddb9aa92fab7f74783f7ed3bf248eec56a6ceb00/gateware/boards/ecpix5/pinmap.lpf) (apfaudio__eurorack-pmod) | unknown | 1 | ftdi-uart, gpio-header, i2c |

## Reusable cores seen on this board

Cores whose source repo, or a repo that copies/instantiates them, targets this board.

| Core | Function | Source repo |
|---|---|---|
| AK4619 audio codec driver + PMOD I2C master | [audio-digital](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/audio-digital.md) | apfaudio__eurorack-pmod |
| Cynthion USB Audio Class 2.0 example | [audio-digital](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/audio-digital.md) | greatscottgadgets__cynthion-uac |
| LUNA-SoC VexRiscv SoC framework (Moondancer's CPU) | [cpu-riscv](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-riscv.md) | greatscottgadgets__luna-soc |
| VexRiscv (SpinalHDL-generated Verilog) | [cpu-riscv](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-riscv.md) | rschlaikjer__fpga-3-softcores |
| Lightweight AXI-4 DDR3 controller + ECP5 PHY | [ddr-memory](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/ddr-memory.md) | ultraembedded__core_ddr3_controller |
| Lightweight DDR3 AXI4 memory controller (ECP5) | [ddr-memory](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/ddr-memory.md) | ultraembedded__orangecrab |
| glasgow I2C core (Amaranth) | [i2c](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/i2c.md) | glasgowembedded__glasgow |
| ORBTrace SWD/JTAG debug + parallel TRACE core (legacy plain-Verilog flow) | [jtag-debug](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/jtag-debug.md) | orbcode__orbtrace |
| ecp5pll parametric PLL | [pll-clock](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/pll-clock.md) | emard__ulx3s-misc |
| LiteICLink ECP5 SERDES (DCUA) wrapper | [serdes-links](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/serdes-links.md) | enjoy-digital__liteiclink |
| LiteSATA ECP5 SATA PHY + core | [serdes-links](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/serdes-links.md) | enjoy-digital__litesata |
| katsuo.pcie ECP5 SERDES PHY + PCIe endpoint stack | [serdes-links](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/serdes-links.md) | zyp__katsuo-pcie |
| glasgow SPI controller (Amaranth) | [spi](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/spi.md) | glasgowembedded__glasgow |
| hdl4fpga USB 1.1 device core | [usb-device](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/usb-device.md) | hdl4fpga__hdl4fpga |

## Projects targeting this board

- [antoinevg__cynthion-tutorials](https://github.com/antoinevg/cynthion-tutorials): cynthion-tutorials: Amaranth tutorials for Cynthion/ECPIX-5
- [apfaudio__eurorack-pmod](https://github.com/apfaudio/eurorack-pmod): Eurorack PMOD: AK4619 audio-codec PMOD gateware
- [enjoy-digital__liteiclink](https://github.com/enjoy-digital/liteiclink): LiteICLink: Migen/LiteX inter-chip link cores - generic ECP5 SerDes
- [enjoy-digital__litesata](https://github.com/enjoy-digital/litesata): LiteSATA: Migen/LiteX SATA host core
- [greatscottgadgets__luna](https://github.com/greatscottgadgets/luna): LUNA: Amaranth USB 2.0/3.0 gateware framework
- [maxhpc__ecpix-5](https://github.com/maxhpc/ecpix-5): ECPIX-5 gateware collection: LEDs, UART, DDR3 top
- [openconcepts-ar__accel2d](https://github.com/openconcepts-ar/accel2d): accel2d: C-to-Verilog
- [orbcode__orbtrace](https://github.com/orbcode/orbtrace): ORBTrace: Cortex-M SWD/JTAG debug + parallel TRACE probe gateware
- [ultraembedded__core_ddr3_controller](https://github.com/ultraembedded/core_ddr3_controller): Lightweight AXI-4 DDR3 memory controller
- [ultraembedded__ecpix-5](https://github.com/ultraembedded/ecpix-5): ECPiX-5: RISC-V TCM SoC with AXI4 interconnect and IT6613-based HDMI/DVI framebuffer output
{% endraw %}
