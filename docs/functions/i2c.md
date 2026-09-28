---
title: "I2C"
parent: "Cores by function"
nav_order: 14
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# I2C

I2C master/slave cores (RTC, HDMI DDC, sensors).

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [verilog-i2c (alexforencich)](#core-pifive-verilog-i2c) ★ | [asinghani__pifive-cpu](https://github.com/asinghani/pifive-cpu) | Verilog | MIT (submodule COPYING, Alex Forencich) | ECP5 | 0 |
| [BeagleWire i2c-master](#core-beaglewire-i2c-master) | [pmezydlo__beaglewire](https://github.com/pmezydlo/BeagleWire) | Verilog | GPL-2.0 (repo LICENSE; note pcf header claims… | iCE40 | 0 |
| [glasgow I2C core (Amaranth)](#core-glasgow-i2c) | [glasgowembedded__glasgow](https://github.com/GlasgowEmbedded/glasgow) | Python (Amaranth) | 0BSD OR Apache-2.0 | any | 2 |
| [I2C-slave-to-AXI-Lite-master bridge (verilog-i2c integration)](#core-lit3rick-i2c-axil-master) | [kelu124__lit3rick](https://github.com/kelu124/lit3rick) | Verilog | MIT ((c) 2017/2019 Alex Forencich, in-file header) | any | 1 |
| [SAO I2C command engine](#core-hazard3-sao-i2c-engine) | [ulx3s__hazard3](https://github.com/ulx3s/Hazard3) | Verilog | Apache-2.0 | ECP5 | 0 |

## Cores

### verilog-i2c (alexforencich) (best) {#core-pifive-verilog-i2c}

Well-known alexforencich I2C master/slave IP with ready-made Wishbone and AXI-Lite register wrappers and an init sequencer.

| | |
|---|---|
| Repository | [asinghani__pifive-cpu](https://github.com/asinghani/pifive-cpu): 3-stage RV32I(+M) |
| Files | [`soc/third_party/verilog-i2c/rtl/i2c_master.v`](https://github.com/asinghani/pifive-cpu/blob/81ca4088242eeb29c56ddd31d2c53a61a047db53/soc/third_party/verilog-i2c/rtl/i2c_master.v), [`soc/third_party/verilog-i2c/rtl/i2c_master_wbs_8.v`](https://github.com/asinghani/pifive-cpu/blob/81ca4088242eeb29c56ddd31d2c53a61a047db53/soc/third_party/verilog-i2c/rtl/i2c_master_wbs_8.v), [`soc/third_party/verilog-i2c/rtl/i2c_master_wbs_16.v`](https://github.com/asinghani/pifive-cpu/blob/81ca4088242eeb29c56ddd31d2c53a61a047db53/soc/third_party/verilog-i2c/rtl/i2c_master_wbs_16.v), [`soc/third_party/verilog-i2c/rtl/i2c_slave.v`](https://github.com/asinghani/pifive-cpu/blob/81ca4088242eeb29c56ddd31d2c53a61a047db53/soc/third_party/verilog-i2c/rtl/i2c_slave.v), [`soc/third_party/verilog-i2c/rtl/i2c_slave_wbm.v`](https://github.com/asinghani/pifive-cpu/blob/81ca4088242eeb29c56ddd31d2c53a61a047db53/soc/third_party/verilog-i2c/rtl/i2c_slave_wbm.v), [`soc/third_party/verilog-i2c/rtl/i2c_init.v`](https://github.com/asinghani/pifive-cpu/blob/81ca4088242eeb29c56ddd31d2c53a61a047db53/soc/third_party/verilog-i2c/rtl/i2c_init.v) |
| Top module | `i2c_master` |
| Language | Verilog |
| License | MIT (submodule COPYING, Alex Forencich) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | soc/third_party/verilog-i2c/tb/test_i2c_master.py + friends (cocotb, self-checking) |

**On ULX3S:** Vendored as a git submodule in a repo whose fpga/ulx3s/Makefile targets ULX3S 85F (yosys+nextpnr-ecp5+ecppack); pick the wbs_8/16 wrapper for a Wishbone SoC.

### BeagleWire i2c-master {#core-beaglewire-i2c-master}

Self-contained I2C master for the BeagleWire cape, using two SB_IO instances for the open-drain SDA/SCL pads.

| | |
|---|---|
| Repository | [pmezydlo__beaglewire](https://github.com/pmezydlo/BeagleWire): BeagleWire: GSoC-2017 open Verilog example/peripheral collection for the iCE40HX4K BeagleBone cape |
| Files | [`components/i2c-master.v`](https://github.com/pmezydlo/BeagleWire/blob/85833474dc34c7760fe3aeac904d7d7fa6cc5d4c/components/i2c-master.v) |
| Top module | `i2c_master` |
| Language | Verilog |
| License | GPL-2.0 (repo LICENSE; note pcf header claims gplv3, inconsistent) |
| FPGA / primitives | iCE40: `SB_IO` |
| Tests | none found |

**On ULX3S:** Replace the two SB_IO tristate instances with ECP5 BB/TRISTATE_IO primitives; the FSM logic itself is portable.

### glasgow I2C core (Amaranth) {#core-glasgow-i2c}

Pure-Amaranth I2C controller/target gateware; part of Glasgow's actively maintained protocol library.

| | |
|---|---|
| Repository | [glasgowembedded__glasgow](https://github.com/GlasgowEmbedded/glasgow): Glasgow Interface Explorer: multi-protocol USB debug/reverse-engineering tool - Amaranth-generated gateware… |
| Files | [`software/glasgow/gateware/i2c.py`](https://github.com/GlasgowEmbedded/glasgow/blob/9b835612a323930c2e0641033fc95c2814a657b9/software/glasgow/gateware/i2c.py) |
| Top module | n/a |
| Language | Python (Amaranth) |
| License | 0BSD OR Apache-2.0 (repo LICENSE-*.txt) |
| FPGA / primitives | any: none (portable) |
| Tests | software/tests (not i2c.py-specific in this pass) |

**On ULX3S:** Needs the Amaranth/glasgow build flow; ECP5 platform support already present (rev D board).

**Used by 2 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [asinghani__pifive-cpu](https://github.com/asinghani/pifive-cpu) (copies [`soc/rtl/periphs/i2c.py`](https://github.com/asinghani/pifive-cpu/blob/81ca4088242eeb29c56ddd31d2c53a61a047db53/soc/rtl/periphs/i2c.py))
- [greatscottgadgets__luna](https://github.com/greatscottgadgets/luna) (copies [`luna/gateware/interface/i2c.py`](https://github.com/greatscottgadgets/luna/blob/82a8f733296603b70ba56755206e13092609c6f0/luna/gateware/interface/i2c.py))

### I2C-slave-to-AXI-Lite-master bridge (verilog-i2c integration) {#core-lit3rick-i2c-axil-master}

Alex Forencich's verilog-i2c i2c_slave core wrapped as an AXI-Lite master, letting an external I2C host (Raspberry Pi) read/write lit3rick's register file and signal/FFT RAM directly; a second, near-duplicate wrapper ships alongside as i2c_wrapper.v.

| | |
|---|---|
| Repository | [kelu124__lit3rick](https://github.com/kelu124/lit3rick): lit3rick: single-channel ultrasound pulse-echo board - UP5K ADC/pulser, on-chip DFT envelope extraction,… |
| Files | [`verilog/src/rtl/i2c_slave_axil_master.v`](https://github.com/kelu124/lit3rick/blob/ca4ad983046943fae0694a609154839e8c051283/verilog/src/rtl/i2c_slave_axil_master.v), [`verilog/src/rtl/i2c_slave.v`](https://github.com/kelu124/lit3rick/blob/ca4ad983046943fae0694a609154839e8c051283/verilog/src/rtl/i2c_slave.v) |
| Top module | `i2c_slave_axil_master` |
| Language | Verilog |
| License | MIT ((c) 2017/2019 Alex Forencich, in-file header) |
| FPGA / primitives | any: none (portable) |
| Tests | exercised by verilog/src/tb/tb_top.sv (bus-functional model verilog/src/tb/i2c_if.sv) across all test_* tasks; no standalone unit test for this file |

**On ULX3S:** Same upstream library as this collection's 'best' i2c core (pifive-verilog-i2c, which shows the Wishbone wrappers); this repo instead shows the AXI-Lite-master wrapper variant. No vendor primitives, ECP5-portable as-is.

Full review: [kelu124__lit3rick](../projects/kelu124__lit3rick.md).

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [asinghani__pifive-cpu](https://github.com/asinghani/pifive-cpu) (instantiates [`soc/third_party/verilog-i2c/tb/test_i2c_slave_axil_master.v`](https://github.com/asinghani/pifive-cpu/blob/81ca4088242eeb29c56ddd31d2c53a61a047db53/soc/third_party/verilog-i2c/tb/test_i2c_slave_axil_master.v))

### SAO I2C command engine {#core-hazard3-sao-i2c-engine}

Low-level I2C command engine with open-drain SDA/SCL controls, driving the ULX3S example SoC's SAO bridge.

| | |
|---|---|
| Repository | [ulx3s__hazard3](https://github.com/ulx3s/Hazard3): Hazard3 RV32IMACZb* CPU: ULX3S/ULX4M-LD fork with dedicated build docs, incl. |
| Files | [`example_soc/soc/sao_i2c_engine.v`](https://github.com/ulx3s/Hazard3/blob/3c0aca063517bb7fdbe869019c984954c7dd5c97/example_soc/soc/sao_i2c_engine.v) |
| Top module | `sao_i2c_engine` |
| Language | Verilog |
| License | Apache-2.0 (SPDX header + repo LICENSE) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | none found |

**On ULX3S:** Actually built into ulx3s__hazard3's example_soc for ULX3S 85F; board-level wrapper supplies the tri-state I/O.

## Other catalogued projects

Catalogued repos tagged `i2c` (10) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
