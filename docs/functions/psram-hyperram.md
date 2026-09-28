---
title: "PSRAM and HyperRAM"
parent: "Cores by function"
nav_order: 9
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# PSRAM and HyperRAM

QSPI/QPI PSRAM and HyperBus controllers (add-on memories).

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [Hackaday badge QPI-PSRAM PHY + cache (ECP5-native)](#core-hadbadge-qpi-cache) ★ | [spritetm__hadbadge2019_fpgasoc](https://github.com/Spritetm/hadbadge2019_fpgasoc) | Verilog | BSD-3 (per-file headers, LICENSE.bsd) | ECP5 | 0 |
| [hbc portable HyperBus/HyperRAM controller](#core-gtjennings1-hbc) | [gtjennings1__hyperbus](https://github.com/gtjennings1/HyperBUS) | Verilog | MIT-style | any | 0 |
| [hyper_xface HyperRAM DWORD interface](#core-asinghani-hyper-xface) | [asinghani__pifive-cpu](https://github.com/asinghani/pifive-cpu) | Verilog | CERN-OHL-1.2 | any | 0 |
| [no2fpga HyperRAM controller (no2hyperbus)](#core-no2hyperbus) | [smunaut__ice40-playground](https://github.com/smunaut/ice40-playground) | Verilog | CERN-OHL-P-2.0 | iCE40 | 1 |

## Cores

### Hackaday badge QPI-PSRAM PHY + cache (ECP5-native) (best) {#core-hadbadge-qpi-cache}

Cleanly layered QPI-PSRAM stack for two interleaved Lyontek LY68L6400 8 MB QPI chips (16 MB total): only qspi_phy_2x_ecp5.v touches ECP5 DDR-IO primitives, qpimem_cache/arbiter/dma_rdr above it are portable logic. Ships on real 45F badge silicon.

| | |
|---|---|
| Repository | [spritetm__hadbadge2019_fpgasoc](https://github.com/Spritetm/hadbadge2019_fpgasoc): Hackaday Supercon 2019 badge: ECP5 SoC |
| Files | [`soc/qpi_cache/qspi_phy_2x_ecp5.v`](https://github.com/Spritetm/hadbadge2019_fpgasoc/blob/6e706d52ecdc007e9179bda01d8eac60d55b7c45/soc/qpi_cache/qspi_phy_2x_ecp5.v), [`soc/qpi_cache/qpimem_iface_2x2w.v`](https://github.com/Spritetm/hadbadge2019_fpgasoc/blob/6e706d52ecdc007e9179bda01d8eac60d55b7c45/soc/qpi_cache/qpimem_iface_2x2w.v), [`soc/qpi_cache/qpimem_cache.v`](https://github.com/Spritetm/hadbadge2019_fpgasoc/blob/6e706d52ecdc007e9179bda01d8eac60d55b7c45/soc/qpi_cache/qpimem_cache.v), [`soc/qpi_cache/qpimem_arbiter.v`](https://github.com/Spritetm/hadbadge2019_fpgasoc/blob/6e706d52ecdc007e9179bda01d8eac60d55b7c45/soc/qpi_cache/qpimem_arbiter.v), [`soc/qpi_cache/qpimem_dma_rdr.v`](https://github.com/Spritetm/hadbadge2019_fpgasoc/blob/6e706d52ecdc007e9179bda01d8eac60d55b7c45/soc/qpi_cache/qpimem_dma_rdr.v) |
| Top module | `qpimem_cache` |
| Language | Verilog |
| License | BSD-3 (per-file headers, LICENSE.bsd) |
| FPGA / primitives | ECP5: `ODDRX1F`, `IDDRX1F`, `TRELLIS_IO`, `OFS1P3DX` |
| Tests | self-checking iverilog testbenches: qpimem_cache_testbench.v, qpimem_iface_testbench.v, qpimem_interleave_testbench.v |

**On ULX3S:** ULX3S has no on-board QPI PSRAM; only useful pairing with a compatible add-on board. Runs at 48 MHz interleaved; new LPF and pin remap required either way.

Full review: [spritetm__hadbadge2019_fpgasoc](../projects/spritetm__hadbadge2019_fpgasoc.md).

### hbc portable HyperBus/HyperRAM controller {#core-gtjennings1-hbc}

Self-contained HyperBus/HyperRAM controller in plain Verilog with no vendor primitives in the core FSM (hbc.v); written for iCE40 UP5K boards but architecturally the most portable HyperRAM core in the collection.

| | |
|---|---|
| Repository | [gtjennings1__hyperbus](https://github.com/gtjennings1/HyperBUS): UPduino: HyperBus/HyperRAM controller plus a PicoRV32 RISC-V SoC demo for iCE40 UltraPlus |
| Files | [`standalone/hbc.v`](https://github.com/gtjennings1/HyperBUS/blob/37bf73d0f5f7884d007b5a20566508a292a3c11c/standalone/hbc.v), [`standalone/hbc_io.v`](https://github.com/gtjennings1/HyperBUS/blob/37bf73d0f5f7884d007b5a20566508a292a3c11c/standalone/hbc_io.v) |
| Top module | `hbc` |
| Language | Verilog |
| License | MIT-style (embedded header, Gnarly Grey LLC 2017; no repo LICENSE/COPYING file) |
| FPGA / primitives | any: none (portable) |
| Tests | self-checking testbench: sim/hbc_tb.v ($display PASS/FAIL per byte) |

**On ULX3S:** No ULX3S/ECP5 target exists; needs a new top-level with ECP5 tristate DQ IO and timing closure at the board's clock.

### hyper_xface HyperRAM DWORD interface {#core-asinghani-hyper-xface}

DWORD-granularity HyperRAM interface (targets Cypress S27KL0641), optimized for RTL portability over bandwidth; DRAM clock is fabric-clock/4. Vendored into the pifive-cpu SoC but its instance is commented out there.

| | |
|---|---|
| Repository | [asinghani__pifive-cpu](https://github.com/asinghani/pifive-cpu): 3-stage RV32I(+M) |
| Files | [`soc/third_party/hyperram/hyper_xface.v`](https://github.com/asinghani/pifive-cpu/blob/81ca4088242eeb29c56ddd31d2c53a61a047db53/soc/third_party/hyperram/hyper_xface.v), [`soc/third_party/hyperram/hyper_dword.v`](https://github.com/asinghani/pifive-cpu/blob/81ca4088242eeb29c56ddd31d2c53a61a047db53/soc/third_party/hyperram/hyper_dword.v) |
| Top module | `hyper_xface` |
| Language | Verilog |
| License | CERN-OHL-1.2 (claimed in-file header only, Kevin M. Hubbard 2018; not formalized at repo level) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Portable Verilog-2001, no vendor primitives; needs its own top-level pin mapping and has not been exercised end-to-end in the parent project (instantiation commented out).

### no2fpga HyperRAM controller (no2hyperbus) {#core-no2hyperbus}

Wishbone-facing HyperRAM controller from Sylvain Munaut's no2fpga library: hbus_memctrl.v and hbus_dline.v are primitive-free link-layer logic, only hbus_phy_ice40.v instantiates iCE40 SB_IO for the physical DQ/RWDS pins.

| | |
|---|---|
| Repository | [smunaut__ice40-playground](https://github.com/smunaut/ice40-playground): iCEBreaker: collection of iCE40 UP5K IP cores |
| Files | [`cores/no2hyperbus/rtl/hbus_memctrl.v`](https://github.com/smunaut/ice40-playground/blob/d2fa0050129c14a7fc42f64f115366f6f2a51669/cores/no2hyperbus/rtl/hbus_memctrl.v), [`cores/no2hyperbus/rtl/hbus_dline.v`](https://github.com/smunaut/ice40-playground/blob/d2fa0050129c14a7fc42f64f115366f6f2a51669/cores/no2hyperbus/rtl/hbus_dline.v), [`cores/no2hyperbus/rtl/hbus_phy_ice40.v`](https://github.com/smunaut/ice40-playground/blob/d2fa0050129c14a7fc42f64f115366f6f2a51669/cores/no2hyperbus/rtl/hbus_phy_ice40.v) |
| Top module | `hbus_memctrl` |
| Language | Verilog |
| License | CERN-OHL-P-2.0 (cores/no2hyperbus/LICENSE) |
| FPGA / primitives | iCE40: `SB_IO` |
| Tests | sim/hbus_memctrl_tb.v against a bundled sim/s27kl0642.v behavioral model |

**On ULX3S:** Only hbus_phy_ice40.v needs an ECP5 rewrite (TRELLIS_IO/ODDRX1F in place of SB_IO); memctrl/dline logic is vendor-neutral as-is.

Full review: [smunaut__ice40-playground](../projects/smunaut__ice40-playground.md).

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [smunaut__ice40linux](https://github.com/smunaut/iCE40linux) (instantiates [`gateware/riscv_linux/rtl/top.v`](https://github.com/smunaut/iCE40linux/blob/16bc38fd181ddba8074f68da162cc35a802ec84b/gateware/riscv_linux/rtl/top.v))

## Other catalogued projects

Catalogued repos tagged `psram` (5), `hyperram` (2) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
