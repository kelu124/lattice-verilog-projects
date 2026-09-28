---
title: "DDR3 memory"
parent: "Cores by function"
nav_order: 8
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# DDR3 memory

DDR3 controllers and PHYs for ECP5 boards that have DDR3.

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [Lightweight DDR3 AXI4 memory controller (ECP5)](#core-orangecrab-ddr3-axi) ★ | [ultraembedded__orangecrab](https://github.com/ultraembedded/orangecrab) | Verilog | Apache-2.0 | ECP5 | 2 |
| [Lightweight AXI-4 DDR3 controller + ECP5 PHY](#core-ultraembedded-core-ddr3-controller) | [ultraembedded__core_ddr3_controller](https://github.com/ultraembedded/core_ddr3_controller) | Verilog | Apache-2.0 | any | 1 |
| [UberDDR3 controller + ECP5 PHY](#core-uberddr3-controller) | [remyciterin__3driscv](https://github.com/RemyCiterin/3DRiscV) | Verilog | GPL-3.0 (UberDDR3/LICENSE) | ECP5 | 1 |

## Cores

### Lightweight DDR3 AXI4 memory controller (ECP5) (best) {#core-orangecrab-ddr3-axi}

Complete AXI4 DDR3 controller (Ultra-Embedded.com) proven on OrangeCrab r0.2 (ECP5): JEDEC DFI sequencer + plain-IO PHY (no DQSBUFM/DELAYF hardware read-training). Not for stock ULX3S (SDR SDRAM only), only for ECP5 boards/add-ons with DDR3.

| | |
|---|---|
| Repository | [ultraembedded__orangecrab](https://github.com/ultraembedded/orangecrab): OrangeCrab: DDR3 128MB read/write memory test gateware |
| Files | [`ddr_test/src_v/ddr3_axi.v`](https://github.com/ultraembedded/orangecrab/blob/685d601556deb8bfa4c0a24bf47b96ae60819c04/ddr_test/src_v/ddr3_axi.v), [`ddr_test/src_v/ddr3_axi_core.v`](https://github.com/ultraembedded/orangecrab/blob/685d601556deb8bfa4c0a24bf47b96ae60819c04/ddr_test/src_v/ddr3_axi_core.v), [`ddr_test/src_v/ddr3_axi_retime.v`](https://github.com/ultraembedded/orangecrab/blob/685d601556deb8bfa4c0a24bf47b96ae60819c04/ddr_test/src_v/ddr3_axi_retime.v), [`ddr_test/src_v/ddr3_dfi_seq.v`](https://github.com/ultraembedded/orangecrab/blob/685d601556deb8bfa4c0a24bf47b96ae60819c04/ddr_test/src_v/ddr3_dfi_seq.v), [`ddr_test/src_v/ddr3_dfi_phy.v`](https://github.com/ultraembedded/orangecrab/blob/685d601556deb8bfa4c0a24bf47b96ae60819c04/ddr_test/src_v/ddr3_dfi_phy.v) |
| Top module | `ddr3_axi` |
| Language | Verilog |
| License | Apache-2.0 (LICENSE) |
| FPGA / primitives | ECP5: `ODDRX1F`, `IDDRX1F`, `BB` |
| Tests | none found (no build script or testbench in this clone) |

**On ULX3S:** Demonstrated only at a conservative 24 MHz DDR clock; re-tune DQ_IN_DELAY_INIT/TPHY_RDLAT for production speed. Needs a full LPF rewrite for any other board's DDR3 pinout.

Full review: [ultraembedded__orangecrab](../projects/ultraembedded__orangecrab.md).

**Used by 2 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [maxhpc__ecpix-5](https://github.com/maxhpc/ecpix-5) (instantiates [`libs/ddr3/ddr3_top.sv`](https://github.com/maxhpc/ecpix-5/blob/dbd64a102aa9aaa8403c7c408fdfd5beef625eb1/libs/ddr3/ddr3_top.sv))
- [ultraembedded__core_ddr3_controller](https://github.com/ultraembedded/core_ddr3_controller) (instantiates [`examples/arty_a7/top.v`](https://github.com/ultraembedded/core_ddr3_controller/blob/a03492a6000ca0185c615060b171bda64806a7bb/examples/arty_a7/top.v))

### Lightweight AXI-4 DDR3 controller + ECP5 PHY {#core-ultraembedded-core-ddr3-controller}

Compact 32-bit AXI-4 DDR3 memory controller run in DLL-off mode (<=125MHz), standardized DFI interface to a swappable PHY; ECP5 PHY plus Xilinx 7-series PHY both included. Smaller than vendor DDR3 MIGs (README: 9% vs 33% LUTs on the same design).

| | |
|---|---|
| Repository | [ultraembedded__core_ddr3_controller](https://github.com/ultraembedded/core_ddr3_controller): Lightweight AXI-4 DDR3 memory controller |
| Files | [`src_v/ddr3_axi.v`](https://github.com/ultraembedded/core_ddr3_controller/blob/a03492a6000ca0185c615060b171bda64806a7bb/src_v/ddr3_axi.v), [`src_v/ddr3_axi_pmem.v`](https://github.com/ultraembedded/core_ddr3_controller/blob/a03492a6000ca0185c615060b171bda64806a7bb/src_v/ddr3_axi_pmem.v), [`src_v/ddr3_axi_retime.v`](https://github.com/ultraembedded/core_ddr3_controller/blob/a03492a6000ca0185c615060b171bda64806a7bb/src_v/ddr3_axi_retime.v), [`src_v/ddr3_core.v`](https://github.com/ultraembedded/core_ddr3_controller/blob/a03492a6000ca0185c615060b171bda64806a7bb/src_v/ddr3_core.v), [`src_v/ddr3_dfi_seq.v`](https://github.com/ultraembedded/core_ddr3_controller/blob/a03492a6000ca0185c615060b171bda64806a7bb/src_v/ddr3_dfi_seq.v), [`src_v/phy/ecp5/ddr3_dfi_phy.v`](https://github.com/ultraembedded/core_ddr3_controller/blob/a03492a6000ca0185c615060b171bda64806a7bb/src_v/phy/ecp5/ddr3_dfi_phy.v) |
| Top module | `ddr3_axi` |
| Language | Verilog |
| License | Apache-2.0 (file headers, e.g. src_v/ddr3_axi.v) |
| FPGA / primitives | any: none (portable) |
| Tests | none found (tb/ddr3_core_xc7 needs proprietary Xilinx Vivado xsim/xelab, no open-source sim included) |

**On ULX3S:** No SDRAM on ULX3S, so not directly usable there; targets ECP5 boards with DDR3 (ECPIX-5, tested at 100MHz sys clk / 50MHz DDR with a 90deg phase-shifted clock via ecp5pll). Up to 8 open rows, AXI-4 INCR bursts only (no WRAP).

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [ultraembedded__orangecrab](https://github.com/ultraembedded/orangecrab) (instantiates [`ddr_test/src_v/ddr3_axi.v`](https://github.com/ultraembedded/orangecrab/blob/685d601556deb8bfa4c0a24bf47b96ae60819c04/ddr_test/src_v/ddr3_axi.v))

### UberDDR3 controller + ECP5 PHY {#core-uberddr3-controller}

DDR3 controller with a dedicated ecp5_phy/ddr3_phy_ecp5.v PHY (fabric-clocked BB/DELAYG, no PLL in-file); wired into the 3driscv RV32IMA SoC's Wishbone DDR3 path via a Blarney (Core.hs) wrapper.

| | |
|---|---|
| Repository | [remyciterin__3driscv](https://github.com/RemyCiterin/3DRiscV): 3DRiscV: RV32IMA CPU + custom RISC-V GPGPU SoC |
| Files | [`UberDDR3/rtl/ddr3_controller.v`](https://github.com/RemyCiterin/3DRiscV/blob/23d3422609d3d44e4e05b90189f5ff7a25dce8f7/UberDDR3/rtl/ddr3_controller.v), [`UberDDR3/rtl/ddr3_phy.v`](https://github.com/RemyCiterin/3DRiscV/blob/23d3422609d3d44e4e05b90189f5ff7a25dce8f7/UberDDR3/rtl/ddr3_phy.v), [`UberDDR3/rtl/ecp5_phy/ddr3_phy_ecp5.v`](https://github.com/RemyCiterin/3DRiscV/blob/23d3422609d3d44e4e05b90189f5ff7a25dce8f7/UberDDR3/rtl/ecp5_phy/ddr3_phy_ecp5.v) |
| Top module | `ddr3_controller` |
| Language | Verilog |
| License | GPL-3.0 (UberDDR3/LICENSE) |
| FPGA / primitives | ECP5: `BB`, `DELAYG` |
| Tests | formal (SymbiYosys, UberDDR3/formal/*.sby) + icarus/vivado regression scripts (UberDDR3/testbench/) |

**On ULX3S:** GPL-3.0 copyleft vs. the parent project's MIT; check compatibility before reuse. Has SymbiYosys formal proofs and icarus/vivado regression tests, unlike most other DDR3 options here.

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [machdyne__zeitlos](https://github.com/machdyne/zeitlos) (instantiates [`rtl/mem/ddr3.v`](https://github.com/machdyne/zeitlos/blob/a7e7e85ee0ad1fd0cfff4129e24b2aa528d444e8/rtl/mem/ddr3.v))

## Other catalogued projects

Catalogued repos tagged `ddr3` (5) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
