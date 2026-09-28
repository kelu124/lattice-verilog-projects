---
title: "IcoBoard"
parent: "iCE40 HX8K / HX4K boards"
grand_parent: "Boards"
nav_order: 5
---
<!-- Generated from data/boards.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# IcoBoard

HX8K Raspberry Pi HAT with SRAM; icosoc SoC generator.

| | |
|---|---|
| Board | IcoBoard (Raspberry Pi HAT) |
| FPGA | iCE40 HX8K, CT256 |
| Evidence | catalogue rows (cliffordwolf__icotools) |
| Clock | unknown |
| Catalogued repos | 2 |

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
| [`examples/icezero/icezero.pcf`](https://github.com/cliffordwolf/icotools/blob/9c6185bad15323e5982b68e60923aaea22b074d4/examples/icezero/icezero.pcf) | cliffordwolf__icotools |

## Reusable cores seen on this board

Cores whose source repo, or a repo that copies/instantiates them, targets this board.

| Core | Function | Source repo |
|---|---|---|
| PicoRV32 RISC-V core | [cpu-riscv](https://github.com/kelu124/ulx3s-klod/blob/main/functions/cpu-riscv.md) | yosyshq__picorv32 |
| vga2dvid + tmds_encoder DVI/TMDS core (Mike Field / EMARD) | [hdmi-dvi](https://github.com/kelu124/ulx3s-klod/blob/main/functions/hdmi-dvi.md) | emard__ulx3s-misc |

## Projects targeting this board

- [alangarf__apple-one](https://github.com/alangarf/apple-one): Multi-board
- [cliffordwolf__icotools](https://github.com/cliffordwolf/icotools): icotools: IcoBoard toolset - icoprog programmer, icosoc PicoRV32 SoC generator, example designs
{% endraw %}
