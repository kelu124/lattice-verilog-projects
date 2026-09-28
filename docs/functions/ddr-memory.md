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
| [Lightweight DDR3 AXI4 memory controller (ECP5)](#core-orangecrab-ddr3-axi) ★ | [ultraembedded__orangecrab](https://github.com/ultraembedded/orangecrab) | Verilog | Apache-2.0 | ECP5 | 0 |
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

Catalogued repos tagged `ddr3` (2) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
