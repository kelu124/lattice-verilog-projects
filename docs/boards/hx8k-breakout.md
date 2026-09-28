---
title: "iCE40-HX8K Breakout"
parent: "iCE40 HX8K / HX4K boards"
grand_parent: "Boards"
nav_order: 1
---
<!-- Generated from data/boards.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# iCE40-HX8K Breakout

Lattice's HX8K evaluation board, target of many IceStorm-era examples.

| | |
|---|---|
| Board | Lattice iCE40-HX8K Breakout Board |
| FPGA | iCE40 HX8K, CT256 |
| Evidence | catalogue rows (nesl__ice40_examples, msinger__iceboy) |
| Clock | 12 MHz (catalogue notes) |
| Catalogued repos | 7 |

*The description is a short summary; FPGA facts come from the catalogue rows cited above.*

## Constraint files (PCF)

| PCF | Repository |
|---|---|
| [`tutorial/ICE40-HX8K_Breakout_Board/T02-Fport/Fport.pcf`](https://github.com/Obijuan/open-fpga-verilog-tutorial/blob/b13890217359e1e1153501c1be278347ee5e7e24/tutorial/ICE40-HX8K_Breakout_Board/T02-Fport/Fport.pcf) | obijuan__open-fpga-verilog-tutorial |
| [`tutorial/ICE40-HX8K_Breakout_Board/T04-counter/counter.pcf`](https://github.com/Obijuan/open-fpga-verilog-tutorial/blob/b13890217359e1e1153501c1be278347ee5e7e24/tutorial/ICE40-HX8K_Breakout_Board/T04-counter/counter.pcf) | obijuan__open-fpga-verilog-tutorial |
| [`tutorial/ICE40-HX8K_Breakout_Board/T05-prescaler/prescaler.pcf`](https://github.com/Obijuan/open-fpga-verilog-tutorial/blob/b13890217359e1e1153501c1be278347ee5e7e24/tutorial/ICE40-HX8K_Breakout_Board/T05-prescaler/prescaler.pcf) | obijuan__open-fpga-verilog-tutorial |
| [`tutorial/ICE40-HX8K_Breakout_Board/T03-inv/inv.pcf`](https://github.com/Obijuan/open-fpga-verilog-tutorial/blob/b13890217359e1e1153501c1be278347ee5e7e24/tutorial/ICE40-HX8K_Breakout_Board/T03-inv/inv.pcf) | obijuan__open-fpga-verilog-tutorial |
| [`tutorial/ICE40-HX8K_Breakout_Board/T01-setbit/T01-setbit.pcf`](https://github.com/Obijuan/open-fpga-verilog-tutorial/blob/b13890217359e1e1153501c1be278347ee5e7e24/tutorial/ICE40-HX8K_Breakout_Board/T01-setbit/T01-setbit.pcf) | obijuan__open-fpga-verilog-tutorial |

## Reusable cores seen on this board

Cores whose source repo, or a repo that copies/instantiates them, targets this board.

| Core | Function | Source repo |
|---|---|---|
| PicoRV32 RISC-V core | [cpu-riscv](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-riscv.md) | yosyshq__picorv32 |
| Amaranth radix-2 fixed-point FFT (FFT/Butterfly/TwiddleFactors) | [dsp](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/dsp.md) | greatscottgadgets__amalthea |
| alhusseingamal/r2sdf-fft radix-2 DIF SDF streaming FFT | [dsp](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/dsp.md) | alhusseingamal__r2sdf-fft |
| mattvenn/fpga-sdft sliding DFT core | [dsp](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/dsp.md) | mattvenn__fpga-sdft |
| vga2dvid + tmds_encoder DVI/TMDS core (Mike Field / EMARD) | [hdmi-dvi](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/hdmi-dvi.md) | emard__ulx3s-misc |
| spimemio SPI/QSPI flash XIP controller | [spi-flash](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/spi-flash.md) | yosyshq__picorv32 |
| VgaSyncGen SpinalHDL VGA timing generator | [vga](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/vga.md) | thorkn__vga_clock_1 |

## Projects targeting this board

- [alhusseingamal__r2sdf-fft](https://github.com/alhusseingamal/r2sdf-fft): r2sdf-fft: radix-2 DIF SDF streaming FFT, parametric N
- [daveshah1__pmods](https://github.com/daveshah1/pmods): pmods: David Shah's collection of PMOD daughterboard hardware designs
- [jamesbowman__swapforth](https://github.com/jamesbowman/swapforth): swapforth: cross-platform ANS Forth;
- [mattvenn__fpga-sdft](https://github.com/mattvenn/fpga-sdft): fpga-sdft: sliding DFT
- [nesl__ice40_examples](https://github.com/nesl/ice40_examples): NESL iCE40 HX8K breakout-board example projects: blank, blinky, buttons_bounce/debounce/nopullup, fsm_simple,…
- [obijuan__open-fpga-verilog-tutorial](https://github.com/Obijuan/open-fpga-verilog-tutorial): Digital Design for FPGAs
- [rxrbln__picorv32](https://github.com/rxrbln/picorv32): PicoRV32 fork
{% endraw %}
