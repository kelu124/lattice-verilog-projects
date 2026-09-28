---
title: "iceFUN"
parent: "iCE40 HX8K / HX4K boards"
grand_parent: "Boards"
nav_order: 3
---
<!-- Generated from data/boards.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# iceFUN

Small HX8K board used by mikeakohn's CPU projects.

| | |
|---|---|
| Board | Devantech iceFUN |
| FPGA | iCE40 HX8K, CB132 |
| Evidence | catalogue rows (mikeakohn__riscv_fpga, mikeakohn__apollo11_fpga) |
| Clock | unknown |
| Catalogued repos | 3 |

*The description is a short summary; FPGA facts come from the catalogue rows cited above.*

## Constraint files (PCF)

| PCF | Repository |
|---|---|
| [`iceFUN.pcf`](https://github.com/MichaelBell/nanoV/blob/e1a405edd9af2cb56c3f54bae2316a29c9bcd2d9/iceFUN.pcf) | michaelbell__nanov |
| [`pico_ice/pico_ice.pcf`](https://github.com/MichaelBell/nanoV/blob/e1a405edd9af2cb56c3f54bae2316a29c9bcd2d9/pico_ice/pico_ice.pcf) | michaelbell__nanov |
| [`icefun.pcf`](https://github.com/mikeakohn/apollo11_fpga/blob/7c7b76847c3916d7b3911d8a71ac08bead19f259/icefun.pcf) | mikeakohn__apollo11_fpga |
| [`icefun.pcf`](https://github.com/mikeakohn/riscv_fpga/blob/def2d90ed133fc0c052478dcbe6663295cdf8c21/icefun.pcf) | mikeakohn__riscv_fpga |

## Reusable cores seen on this board

Cores whose source repo, or a repo that copies/instantiates them, targets this board.

| Core | Function | Source repo |
|---|---|---|
| 64x64 LED panel scanner (ledscan) | [led-drivers](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/led-drivers.md) | goran-mahovlic__prjtrellis-led64x64 |
| bit-bang SPI LCD driver (Apollo 11 FPGA) | [spi-display](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/spi-display.md) | mikeakohn__apollo11_fpga |

## Projects targeting this board

- [michaelbell__nanov](https://github.com/MichaelBell/nanoV): NanoV: minimal-area bit-serial RISC-V
- [mikeakohn__apollo11_fpga](https://github.com/mikeakohn/apollo11_fpga): Apollo Guidance Computer CPU reimplementation for iceFUN
- [mikeakohn__riscv_fpga](https://github.com/mikeakohn/riscv_fpga): RISC-V CPU
{% endraw %}
