---
title: "Buses and interconnect"
parent: "Cores by function"
nav_order: 21
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# Buses and interconnect

Wishbone/AXI interconnects, arbiters, bridges.

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [wb_intercon Wishbone mux/arbiter (olofk)](#core-kulp-tenyr-wb-intercon) ★ | [kulp__tenyr](https://github.com/kulp/tenyr) | Verilog | ISC (file headers, Copyright Olof Kindgren) | any | 4 |
| [AHB-Lite crossbar/arbiter/APB bridge](#core-hazard3-ahbl-busfabric) | [ulx3s__hazard3](https://github.com/ulx3s/Hazard3) | Verilog | WTFPL (file headers, Copyright 2018 Luke Wren) | ECP5 | 3 |
| [wb_intercon (olofk), iCE40 copy](#core-rschlaikjer-wb-intercon) | [rschlaikjer__fpga-3-softcores](https://github.com/rschlaikjer/fpga-3-softcores) | Verilog | ISC (vendor/wb_intercon/LICENSE) | iCE40 | 0 |

## Cores

### wb_intercon Wishbone mux/arbiter (olofk) (best) {#core-kulp-tenyr-wb-intercon}

Standard olofk/wb_intercon Wishbone crossbar mux and round-robin arbiter, wired into tenyr's own CPU SoC.

| | |
|---|---|
| Repository | [kulp__tenyr](https://github.com/kulp/tenyr): tenyr: 32-bit orthogonal computer architecture + full software toolchain, with a hw/yosys ULX3S 12F build |
| Files | [`3rdparty/wb_intercon/rtl/verilog/wb_mux.v`](https://github.com/kulp/tenyr/blob/348605e985805dcbe00b8e3766662b343e991b78/3rdparty/wb_intercon/rtl/verilog/wb_mux.v), [`3rdparty/wb_intercon/rtl/verilog/wb_arbiter.v`](https://github.com/kulp/tenyr/blob/348605e985805dcbe00b8e3766662b343e991b78/3rdparty/wb_intercon/rtl/verilog/wb_arbiter.v) |
| Top module | `wb_mux` |
| Language | Verilog |
| License | ISC (file headers, Copyright Olof Kindgren) |
| FPGA / primitives | any: none (portable) |
| Tests | 3rdparty/wb_intercon/bench/{wb_mux_tb.v,wb_arbiter_tb.v} (iverilog) |

**On ULX3S:** Fetched as a git submodule; actually used in hw/verilog/top.v for a ULX3S 12F build (yosys+nextpnr-ecp5+ecppack).

**Used by 4 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [daveshah1__ulx3s](https://github.com/daveshah1/ulx3s) (instantiates [`rtl/verilog/wb_intercon.v`](https://github.com/daveshah1/ulx3s/blob/e72ed991d0e4911b1682792e3b2cd621f3d16ff3/rtl/verilog/wb_intercon.v))
- [machdyne__zeitlos](https://github.com/machdyne/zeitlos) (instantiates [`rtl/sysctl.v`](https://github.com/machdyne/zeitlos/blob/a7e7e85ee0ad1fd0cfff4129e24b2aa528d444e8/rtl/sysctl.v))
- [osmocom__osmo-e1-hardware](https://github.com/osmocom/osmo-e1-hardware) (instantiates [`gateware/common/rtl/soc_iobuf.v`](https://github.com/osmocom/osmo-e1-hardware/blob/85acea8b6d656add7c098d51f816f4ac34084fa2/gateware/common/rtl/soc_iobuf.v))
- [rschlaikjer__fpga-3-softcores](https://github.com/rschlaikjer/fpga-3-softcores) (instantiates [`rtl/gen/wb_intercon.v`](https://github.com/rschlaikjer/fpga-3-softcores/blob/6ccc8ac55f16ffcf17cef1d831714142ab64f27b/rtl/gen/wb_intercon.v))

### AHB-Lite crossbar/arbiter/APB bridge {#core-hazard3-ahbl-busfabric}

AHB-Lite crossbar, arbiter, splitter and an AHB-Lite-to-APB bridge, connecting the Hazard3 CPU to its peripherals.

| | |
|---|---|
| Repository | [ulx3s__hazard3](https://github.com/ulx3s/Hazard3): Hazard3 RV32IMACZb* CPU: ULX3S/ULX4M-LD fork with dedicated build docs, incl. |
| Files | [`example_soc/libfpga/busfabric/ahbl_crossbar.v`](https://github.com/ulx3s/Hazard3/blob/3c0aca063517bb7fdbe869019c984954c7dd5c97/example_soc/libfpga/busfabric/ahbl_crossbar.v), [`example_soc/libfpga/busfabric/ahbl_arbiter.v`](https://github.com/ulx3s/Hazard3/blob/3c0aca063517bb7fdbe869019c984954c7dd5c97/example_soc/libfpga/busfabric/ahbl_arbiter.v), [`example_soc/libfpga/busfabric/ahbl_to_apb.v`](https://github.com/ulx3s/Hazard3/blob/3c0aca063517bb7fdbe869019c984954c7dd5c97/example_soc/libfpga/busfabric/ahbl_to_apb.v), [`example_soc/libfpga/busfabric/ahbl_splitter.v`](https://github.com/ulx3s/Hazard3/blob/3c0aca063517bb7fdbe869019c984954c7dd5c97/example_soc/libfpga/busfabric/ahbl_splitter.v) |
| Top module | `ahbl_crossbar` |
| Language | Verilog |
| License | WTFPL (file headers, Copyright 2018 Luke Wren) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | no unit test of the crossbar/arbiter themselves; indirectly exercised by test/sim SoC-level cxxrtl tests (coremark, riscv-tests) |

**On ULX3S:** Actually instantiated in example_soc/soc/example_soc.v for the ULX3S 85F / ULX4M-LD build; fetched via the Hazard3-libfpga submodule.

**Used by 3 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [wren6991__hazard3](https://github.com/Wren6991/Hazard3) (instantiates [`example_soc/soc/example_soc.v`](https://github.com/Wren6991/Hazard3/blob/8af992930f71a69b0e06c38734c1094f41a05ca0/example_soc/soc/example_soc.v))
- [wren6991__hazard3-swd-soc](https://github.com/Wren6991/Hazard3-SWD-SoC) (instantiates [`hdl/soc/soc.v`](https://github.com/Wren6991/Hazard3-SWD-SoC/blob/6f3bfe190a9dd20185913ec8e97bd2eaea75a788/hdl/soc/soc.v))
- [wren6991__riscboy](https://github.com/Wren6991/RISCBoy) (instantiates [`hdl/libfpga/busfabric/ahbl_crossbar.v`](https://github.com/Wren6991/RISCBoy/blob/25f8bb6eaebee6ace509cecc9b3891f43fae5bf6/hdl/libfpga/busfabric/ahbl_crossbar.v))

### wb_intercon (olofk), iCE40 copy {#core-rschlaikjer-wb-intercon}

Same olofk/wb_intercon library as kulp__tenyr, vendored directly (not a submodule) alongside a VexRiscv SoC.

| | |
|---|---|
| Repository | [rschlaikjer__fpga-3-softcores](https://github.com/rschlaikjer/fpga-3-softcores): fpga-3-softcores: VexRiscv Wishbone SoC demo |
| Files | [`vendor/wb_intercon/rtl/verilog/wb_mux.v`](https://github.com/rschlaikjer/fpga-3-softcores/blob/6ccc8ac55f16ffcf17cef1d831714142ab64f27b/vendor/wb_intercon/rtl/verilog/wb_mux.v), [`vendor/wb_intercon/rtl/verilog/wb_arbiter.v`](https://github.com/rschlaikjer/fpga-3-softcores/blob/6ccc8ac55f16ffcf17cef1d831714142ab64f27b/vendor/wb_intercon/rtl/verilog/wb_arbiter.v) |
| Top module | `wb_mux` |
| Language | Verilog |
| License | ISC (vendor/wb_intercon/LICENSE) |
| FPGA / primitives | iCE40: none (portable) |
| Tests | vendor/wb_intercon/bench/{wb_mux_tb.v,wb_arbiter_tb.v} |

**On ULX3S:** Files contain no SB_* primitives; only the board's PCF/PLL needs porting, the bus logic is vendor-neutral.

## Other catalogued projects

Catalogued repos tagged `bus-fabric` (6), `wishbone-bus` (4) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
