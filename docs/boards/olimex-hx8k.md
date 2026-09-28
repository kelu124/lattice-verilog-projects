---
title: "Olimex iCE40HX8K-EVB"
parent: "iCE40 HX8K / HX4K boards"
grand_parent: "Boards"
nav_order: 4
---
<!-- Generated from data/boards.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# Olimex iCE40HX8K-EVB

Olimex HX8K evaluation board with SRAM; xv6 RISC-V computer and Apple-1 ports.

| | |
|---|---|
| Board | Olimex iCE40HX8K-EVB |
| FPGA | iCE40 HX8K, CT256 |
| Evidence | catalogue rows (x653__xv6-riscv-fpga, alangarf__apple-one) |
| Clock | unknown |
| Catalogued repos | 3 |

*The description is a short summary; FPGA facts come from the catalogue rows cited above.*

## Constraint files (PCF)

| PCF | Repository |
|---|---|
| [`boards/tinyfpga_b2/tinyfpga.pcf`](https://github.com/alangarf/apple-one/blob/0f15ef6d62c2f8820aa5a68b7f973eef4a78dd8d/boards/tinyfpga_b2/tinyfpga.pcf) | alangarf__apple-one |
| [`boards/tinyfpga_b2/yosys/tinyfpga.pcf`](https://github.com/alangarf/apple-one/blob/0f15ef6d62c2f8820aa5a68b7f973eef4a78dd8d/boards/tinyfpga_b2/yosys/tinyfpga.pcf) | alangarf__apple-one |
| [`boards/olimex_ice40hx8k_evb_ice40-io/ice40hx8k.pcf`](https://github.com/alangarf/apple-one/blob/0f15ef6d62c2f8820aa5a68b7f973eef4a78dd8d/boards/olimex_ice40hx8k_evb_ice40-io/ice40hx8k.pcf) | alangarf__apple-one |
| [`boards/olimex_ice40hx8k_evb_ice40-io/yosys/ice40hx8k.pcf`](https://github.com/alangarf/apple-one/blob/0f15ef6d62c2f8820aa5a68b7f973eef4a78dd8d/boards/olimex_ice40hx8k_evb_ice40-io/yosys/ice40hx8k.pcf) | alangarf__apple-one |
| [`boards/icoboard/yosys/icoboard.pcf`](https://github.com/alangarf/apple-one/blob/0f15ef6d62c2f8820aa5a68b7f973eef4a78dd8d/boards/icoboard/yosys/icoboard.pcf) | alangarf__apple-one |
| [`boards/ice40hx8k-b-evn/ice40hx8k.pcf`](https://github.com/alangarf/apple-one/blob/0f15ef6d62c2f8820aa5a68b7f973eef4a78dd8d/boards/ice40hx8k-b-evn/ice40hx8k.pcf) | alangarf__apple-one |
| [`boards/ice40hx8k-b-evn/icecube2/ice40hx8k.pcf`](https://github.com/alangarf/apple-one/blob/0f15ef6d62c2f8820aa5a68b7f973eef4a78dd8d/boards/ice40hx8k-b-evn/icecube2/ice40hx8k.pcf) | alangarf__apple-one |
| [`boards/ice40hx8k-b-evn/yosys/ice40hx8k.pcf`](https://github.com/alangarf/apple-one/blob/0f15ef6d62c2f8820aa5a68b7f973eef4a78dd8d/boards/ice40hx8k-b-evn/yosys/ice40hx8k.pcf) | alangarf__apple-one |
| [`boards/blackice2/yosys/blackice2.pcf`](https://github.com/alangarf/apple-one/blob/0f15ef6d62c2f8820aa5a68b7f973eef4a78dd8d/boards/blackice2/yosys/blackice2.pcf) | alangarf__apple-one |
| [`boards/upduino/yosys/ice40up5k.pcf`](https://github.com/alangarf/apple-one/blob/0f15ef6d62c2f8820aa5a68b7f973eef4a78dd8d/boards/upduino/yosys/ice40up5k.pcf) | alangarf__apple-one |
| [`boards/ice40updevboard/yosys/ice40updevboard.pcf`](https://github.com/alangarf/apple-one/blob/0f15ef6d62c2f8820aa5a68b7f973eef4a78dd8d/boards/ice40updevboard/yosys/ice40updevboard.pcf) | alangarf__apple-one |
| [`pinout.pcf`](https://github.com/ulx3s/galaksija/blob/9578934a1a42462b54dedcc2a05649091d41a447/pinout.pcf) | ulx3s__galaksija |

## Reusable cores seen on this board

Cores whose source repo, or a repo that copies/instantiates them, targets this board.

| Core | Function | Source repo |
|---|---|---|
| TV80 Z80-compatible core (emard__ulx3s_galaksija copy) | [cpu-retro](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-retro.md) | emard__ulx3s_galaksija |
| vga2dvid + tmds_encoder DVI/TMDS core (Mike Field / EMARD) | [hdmi-dvi](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/hdmi-dvi.md) | emard__ulx3s-misc |

## Projects targeting this board

- [alangarf__apple-one](https://github.com/alangarf/apple-one): Multi-board
- [ulx3s__galaksija](https://github.com/ulx3s/galaksija): Galaksija mirror + Olimex GateMate port
- [x653__xv6-riscv-fpga](https://github.com/x653/xv6-riscv-fpga): xv6-riscv-fpga: from-scratch RV32IA_Zicsr RISC-V CPU
{% endraw %}
