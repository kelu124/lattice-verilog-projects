---
title: "UPduino"
parent: "iCE40 UP5K boards"
grand_parent: "Boards"
nav_order: 2
---
<!-- Generated from data/boards.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# UPduino

Low-cost UP5K board in DIP format.

| | |
|---|---|
| Board | UPduino v2/v3 (tinyVision.ai) |
| FPGA | iCE40 UP5K, SG48 |
| Evidence | catalogue rows (osresearch__up5k, daveshah1__up5k-demos) |
| Clock | unknown |
| Catalogued repos | 8 |

*The description is a short summary; FPGA facts come from the catalogue rows cited above.*

## Constraint files (PCF)

| PCF | Repository |
|---|---|
| [`boards/upduino/yosys/ice40up5k.pcf`](https://github.com/alangarf/apple-one/blob/0f15ef6d62c2f8820aa5a68b7f973eef4a78dd8d/boards/upduino/yosys/ice40up5k.pcf) | alangarf__apple-one |
| [`work/hwtst/max_upduino2/up5k.pcf`](https://github.com/bnossum/midgetv/blob/f05ade6b088d6c714120a2a61c1606567bd940f0/work/hwtst/max_upduino2/up5k.pcf) | bnossum__midgetv |
| [`work/hwtst/max_upduino2/for_iCEcube2/ice.pcf`](https://github.com/bnossum/midgetv/blob/f05ade6b088d6c714120a2a61c1606567bd940f0/work/hwtst/max_upduino2/for_iCEcube2/ice.pcf) | bnossum__midgetv |
| [`upduino_v2.pcf`](https://github.com/osresearch/up5k/blob/2eef12a9659b8fc4ebf68656198b8840f6da2e0d/upduino_v2.pcf) | osresearch__up5k |
| [`11-sim/upduino_v2.pcf`](https://github.com/ranzbak/fpga-workshop/blob/d63a53e4fe6410d124ddbdf504f5c2b1ff2dda9b/11-sim/upduino_v2.pcf) | ranzbak__fpga-workshop |
| [`12-detect/upduino_v2.pcf`](https://github.com/ranzbak/fpga-workshop/blob/d63a53e4fe6410d124ddbdf504f5c2b1ff2dda9b/12-detect/upduino_v2.pcf) | ranzbak__fpga-workshop |
| [`08-function/upduino_v2.pcf`](https://github.com/ranzbak/fpga-workshop/blob/d63a53e4fe6410d124ddbdf504f5c2b1ff2dda9b/08-function/upduino_v2.pcf) | ranzbak__fpga-workshop |
| [`03a-blink/upduino_v2.pcf`](https://github.com/ranzbak/fpga-workshop/blob/d63a53e4fe6410d124ddbdf504f5c2b1ff2dda9b/03a-blink/upduino_v2.pcf) | ranzbak__fpga-workshop |
| [`10-io/upduino_v2.pcf`](https://github.com/ranzbak/fpga-workshop/blob/d63a53e4fe6410d124ddbdf504f5c2b1ff2dda9b/10-io/upduino_v2.pcf) | ranzbak__fpga-workshop |
| [`06-dim/upduino_v2.pcf`](https://github.com/ranzbak/fpga-workshop/blob/d63a53e4fe6410d124ddbdf504f5c2b1ff2dda9b/06-dim/upduino_v2.pcf) | ranzbak__fpga-workshop |
| [`09-case/upduino_v2.pcf`](https://github.com/ranzbak/fpga-workshop/blob/d63a53e4fe6410d124ddbdf504f5c2b1ff2dda9b/09-case/upduino_v2.pcf) | ranzbak__fpga-workshop |
| [`07-task/upduino_v2.pcf`](https://github.com/ranzbak/fpga-workshop/blob/d63a53e4fe6410d124ddbdf504f5c2b1ff2dda9b/07-task/upduino_v2.pcf) | ranzbak__fpga-workshop |

## Reusable cores seen on this board

Cores whose source repo, or a repo that copies/instantiates them, targets this board.

| Core | Function | Source repo |
|---|---|---|
| TinyFPGA USB Bootloader (USB-serial-to-SPI-flash bridge) | [bootloader-dfu](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/bootloader-dfu.md) | tinyfpga__tinyfpga-bootloader |
| FPGA 101 PicoSoC with LCD text console and MicroPython | [cpu-riscv](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-riscv.md) | mmicko__fpga101-workshop |
| PicoRV32 RISC-V core | [cpu-riscv](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-riscv.md) | yosyshq__picorv32 |
| Sigma-delta DAC (up5k-demos) | [dac](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/dac.md) | daveshah1__up5k-demos |
| 512-point SDF FFT core (E155 Tuner Project) | [dsp](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/dsp.md) | dylansebastianheredia__e155_tuner_project |
| 64-point iterative radix-2 FFT/IFFT (OFDM PHY) | [dsp](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/dsp.md) | meharbaan2__systemverilog-ofdm-phy-core |
| Amaranth radix-2 fixed-point FFT (FFT/Butterfly/TwiddleFactors) | [dsp](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/dsp.md) | greatscottgadgets__amalthea |
| CORDIC sin/cos core | [dsp](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/dsp.md) | osresearch__up5k |
| CORDIC-1 bit-serial CORDIC/DDS sine engine | [dsp](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/dsp.md) | joaln27__cordic |
| ipmgroup/fftd 1024-pt radix-2 DIT FFT core | [dsp](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/dsp.md) | ipmgroup__fftd |
| vga2dvid + tmds_encoder DVI/TMDS core (Mike Field / EMARD) | [hdmi-dvi](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/hdmi-dvi.md) | emard__ulx3s-misc |
| hbc portable HyperBus/HyperRAM controller | [psram-hyperram](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/psram-hyperram.md) | gtjennings1__hyperbus |
| SSD1322 OLED framebuffer driver (m68k-ulx3s) | [spi-display](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/spi-display.md) | nullobject__m68k-ulx3s |
| spimemio SPI/QSPI flash XIP controller | [spi-flash](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/spi-flash.md) | yosyshq__picorv32 |

## Projects targeting this board

- [alangarf__apple-one](https://github.com/alangarf/apple-one): Multi-board
- [bnossum__midgetv](https://github.com/bnossum/midgetv): iCEBreaker/UPduino2: midgetv - compact Wishbone-B4 RV32I RISC-V core
- [daveshah1__up5k-demos](https://github.com/daveshah1/up5k-demos): UPduino: UP5K demos - a buildable port of the MiST NES core to iCE40 UltraPlus
- [dylansebastianheredia__e155_tuner_project](https://github.com/DylanSebastianHeredia/E155_Tuner_Project): E155 Tuner Project: 512-pt 16-bit FFT
- [gtjennings1__hyperbus](https://github.com/gtjennings1/HyperBUS): UPduino: HyperBus/HyperRAM controller plus a PicoRV32 RISC-V SoC demo for iCE40 UltraPlus
- [meharbaan2__systemverilog-ofdm-phy-core](https://github.com/meharbaan2/systemverilog-ofdm-phy-core): systemverilog-ofdm-phy-core: fixed-point 64-subcarrier OFDM TX/RX PHY with 64-pt radix-2 FFT/IFFT, QAM mapper, LS…
- [osresearch__up5k](https://github.com/osresearch/up5k): UPduino v2: standalone iCE40 UltraPlus5K Verilog demos - blink, RGB pulse, UART serial/echo, SPRAM buffered echo,…
- [ranzbak__fpga-workshop](https://github.com/ranzbak/fpga-workshop): UPDuino v2.0: 14-lesson Verilog workshop curriculum
{% endraw %}
