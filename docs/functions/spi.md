---
title: "SPI master / slave"
parent: "Cores by function"
nav_order: 13
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# SPI master / slave

Generic SPI master and slave cores.

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [APB SPI master (microSD)](#core-hazard3-apb-sd-spi) ★ | [ulx3s__hazard3](https://github.com/ulx3s/Hazard3) | Verilog | Apache-2.0 | ECP5 | 0 |
| [glasgow SPI controller (Amaranth)](#core-glasgow-spi) | [glasgowembedded__glasgow](https://github.com/GlasgowEmbedded/glasgow) | Python (Amaranth) | 0BSD OR Apache-2.0 | any | 5 |
| [llsdspi low-level SPI engine](#core-zipcpu-llsdspi) | [zipcpu__sdspi](https://github.com/ZipCPU/sdspi) | Verilog | GPL-3.0 (per-file header, no top-level LICENSE) | any | 0 |
| [OpenCores SPI slave (Santhosh G)](#core-lit3rick-opencores-spi-slave) | [kelu124__lit3rick](https://github.com/kelu124/lit3rick) | Verilog | unknown (no SPDX header; file credits OpenCores… | any | 0 |
| [SPI master (Bus Pirate NextGen Ultra)](#core-buspirateultrahdl-spimaster) | [dangerousprototypes__buspirateultrahdl](https://github.com/DangerousPrototypes/BusPirateUltraHDL) | Verilog | GPL-3.0 (repo LICENSE) | any | 10 |

## Cores

### APB SPI master (microSD) (best) {#core-hazard3-apb-sd-spi}

Small software-driven APB SPI master (mode 0, MSB-first, no FIFO/DMA) built for the ULX3S micro-SD socket.

| | |
|---|---|
| Repository | [ulx3s__hazard3](https://github.com/ulx3s/Hazard3): Hazard3 RV32IMACZb* CPU: ULX3S/ULX4M-LD fork with dedicated build docs, incl. |
| Files | [`example_soc/soc/apb_sd_spi.v`](https://github.com/ulx3s/Hazard3/blob/3c0aca063517bb7fdbe869019c984954c7dd5c97/example_soc/soc/apb_sd_spi.v) |
| Top module | `apb_sd_spi` |
| Language | Verilog |
| License | Apache-2.0 (repo LICENSE) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | none found |

**On ULX3S:** Actually wired into ulx3s__hazard3's example_soc for ULX3S 85F; CLKDIV register sets SCLK from clk/2*(CLKDIV+1).

### glasgow SPI controller (Amaranth) {#core-glasgow-spi}

Pure-Amaranth SPI controller core, part of Glasgow's gateware library; elaborates to plain Verilog with no vendor primitives.

| | |
|---|---|
| Repository | [glasgowembedded__glasgow](https://github.com/GlasgowEmbedded/glasgow): Glasgow Interface Explorer: multi-protocol USB debug/reverse-engineering tool - Amaranth-generated gateware… |
| Files | [`software/glasgow/gateware/spi.py`](https://github.com/GlasgowEmbedded/glasgow/blob/9b835612a323930c2e0641033fc95c2814a657b9/software/glasgow/gateware/spi.py) |
| Top module | n/a |
| Language | Python (Amaranth) |
| License | 0BSD OR Apache-2.0 (repo LICENSE-*.txt) |
| FPGA / primitives | any: none (portable) |
| Tests | software/tests (cocotb-style, not spi.py-specific in this pass) |

**On ULX3S:** Needs an Amaranth build flow (glasgow CLI / YoWASP toolchain) to elaborate; ECP5 platform support already exists in the repo.

**Used by 5 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [asinghani__pifive-cpu](https://github.com/asinghani/pifive-cpu) (copies [`soc/rtl/periphs/spi.py`](https://github.com/asinghani/pifive-cpu/blob/81ca4088242eeb29c56ddd31d2c53a61a047db53/soc/rtl/periphs/spi.py))
- [cheyao__icepi-zero](https://github.com/cheyao/icepi-zero) (copies [`gateware/spi/rpi/spi.py`](https://github.com/cheyao/icepi-zero/blob/e01faa2bd35dcb7269827f8420b845d46c78c869/gateware/spi/rpi/spi.py))
- [greatscottgadgets__hackrf](https://github.com/greatscottgadgets/hackrf) (copies [`firmware/fpga/interface/spi.py`](https://github.com/greatscottgadgets/hackrf/blob/7f96cc8e3fa625c4263a71ba8dd44d1f6110e4fa/firmware/fpga/interface/spi.py))
- [greatscottgadgets__luna](https://github.com/greatscottgadgets/luna) (copies [`luna/gateware/interface/spi.py`](https://github.com/greatscottgadgets/luna/blob/82a8f733296603b70ba56755206e13092609c6f0/luna/gateware/interface/spi.py))
- [markus-zzz__zzz-rv](https://github.com/markus-zzz/zzz-rv) (copies [`rtl/spi.py`](https://github.com/markus-zzz/zzz-rv/blob/0de728380a837eaae6fd3e8f85b69a695eebc65d/rtl/spi.py))

### llsdspi low-level SPI engine {#core-zipcpu-llsdspi}

Portable low-level SPI-mode engine (originally for SD cards) plus a byte/command-level sdspi wrapper; vendor-neutral, no synthesis flow bundled.

| | |
|---|---|
| Repository | [zipcpu__sdspi](https://github.com/ZipCPU/sdspi): SD-Card cores |
| Files | [`rtl/spi/llsdspi.v`](https://github.com/ZipCPU/sdspi/blob/dfb16c80781e8f3eaea9f9cdeb7042baa9e6fa0d/rtl/spi/llsdspi.v), [`rtl/spi/sdspi.v`](https://github.com/ZipCPU/sdspi/blob/dfb16c80781e8f3eaea9f9cdeb7042baa9e6fa0d/rtl/spi/sdspi.v) |
| Top module | `sdspi` |
| Language | Verilog |
| License | GPL-3.0 (per-file header, no top-level LICENSE) |
| FPGA / primitives | any: none (portable) |
| Tests | bench/formal/*.sby SymbiYosys proofs; bench/cpp verilator C++ tb (self-checking) |

**On ULX3S:** Heaviest formal verification of any SPI core in the collection (~60 SymbiYosys proofs); GPL-3.0 copyleft.

Full review: [zipcpu__sdspi](../projects/zipcpu__sdspi.md).

### OpenCores SPI slave (Santhosh G) {#core-lit3rick-opencores-spi-slave}

Classic OpenCores SPI-slave shift register (configurable bit order via mlb, tri-state output enable via ten), used in lit3rick to expose the acquired signal/FFT RAM over SPI to a Raspberry Pi host.

| | |
|---|---|
| Repository | [kelu124__lit3rick](https://github.com/kelu124/lit3rick): lit3rick: single-channel ultrasound pulse-echo board - UP5K ADC/pulser, on-chip DFT envelope extraction,… |
| Files | [`verilog/src/rtl/spi_slave.v`](https://github.com/kelu124/lit3rick/blob/ca4ad983046943fae0694a609154839e8c051283/verilog/src/rtl/spi_slave.v) |
| Top module | `spi_slave` |
| Language | Verilog |
| License | unknown (no SPDX header; file credits OpenCores project 'spi_verilog_master_slave', author Santhosh G <santhg@opencores.org>; opencores.org projects are commonly LGPL but that is not stated in this file) |
| FPGA / primitives | any: none (portable) |
| Tests | none found (exercised indirectly inside verilog/src/tb/tb_top.sv but no dedicated spi_slave testbench) |

**On ULX3S:** No vendor primitives; a generic byte-wide SPI slave, drop-in portable as-is.

Full review: [kelu124__lit3rick](../projects/kelu124__lit3rick.md).

### SPI master (Bus Pirate NextGen Ultra) {#core-buspirateultrahdl-spimaster}

Configurable SPI master written for the Bus Pirate NextGen Ultra debug probe; no vendor primitives in the file itself.

| | |
|---|---|
| Repository | [dangerousprototypes__buspirateultrahdl](https://github.com/DangerousPrototypes/BusPirateUltraHDL): BusPirateUltraHDL: Bus Pirate Ultra FPGA gateware - SPI/UART/PWM/ADC engines + MCU parallel interface for the… |
| Files | [`hdl/spimaster.v`](https://github.com/DangerousPrototypes/BusPirateUltraHDL/blob/bb0d7cae74f799f710b8b0ff246a5080a96c9365/hdl/spimaster.v) |
| Top module | `spimaster` |
| Language | Verilog |
| License | GPL-3.0 (repo LICENSE) |
| FPGA / primitives | any: none (portable) |
| Tests | components/spi has a standalone testbench, not wired into hdl/Makefile |

**On ULX3S:** Repo builds for iCE40 HX8K, but spimaster.v has no SB_* instantiation, so it drops onto ECP5 unmodified.

**Used by 10 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [assured__ct-key](https://github.com/Assured/CT-key) (instantiates [`ctkey_package/src/ctkey/targets/ctkey_ulx3s.py`](https://github.com/Assured/CT-key/blob/8a70cfeaf2a082874c693302d767636f63634b98/ctkey_package/src/ctkey/targets/ctkey_ulx3s.py))
- [egorxe__openglory](https://github.com/egorxe/openglory) (instantiates [`hw/litex/radiona_ulx3s.py`](https://github.com/egorxe/openglory/blob/84d642c609d599542f123847395999f853d8f804/hw/litex/radiona_ulx3s.py))
- [fusetim__rusty-soc](https://github.com/fusetim/rusty-soc) (instantiates [`hardware/lib/fusetim/spi/SpiMasterPeripheral.v`](https://github.com/fusetim/rusty-soc/blob/45a295bf14d9022ece944377e14d82baea5f41a2/hardware/lib/fusetim/spi/SpiMasterPeripheral.v))
- [litex-hub__linux-on-litex-vexriscv](https://github.com/litex-hub/linux-on-litex-vexriscv) (instantiates [`soc_linux.py`](https://github.com/litex-hub/linux-on-litex-vexriscv/blob/05fc5e43e579ac67769c2c930778901a1125f0b4/soc_linux.py))
- [litex-hub__litex-boards](https://github.com/litex-hub/litex-boards) (instantiates [`litex_boards/targets/radiona_ulx3s.py`](https://github.com/litex-hub/litex-boards/blob/d60f413bb0d32657e97b766d0c0fba146b667792/litex_boards/targets/radiona_ulx3s.py))
- [markus-zzz__zzz-rv](https://github.com/markus-zzz/zzz-rv) (instantiates [`rtl/soc.py`](https://github.com/markus-zzz/zzz-rv/blob/0de728380a837eaae6fd3e8f85b69a695eebc65d/rtl/soc.py))
- [mole99__tt05-one-sprite-pony](https://github.com/mole99/tt05-one-sprite-pony) (instantiates [`tb/tb_cocotb.py`](https://github.com/mole99/tt05-one-sprite-pony/blob/c13ca1598cee773d972c09e4f277baea89d14397/tb/tb_cocotb.py))
- [pablogs9__rocketfpga](https://github.com/pablogs9/RocketFPGA) (instantiates [`Software/FPGA Sample Code/Codec/configurator.v`](https://github.com/pablogs9/RocketFPGA/blob/dc2bdf7639637445c21d882d17f6c4dfb30a8447/Software/FPGA Sample Code/Codec/configurator.v))
- [spinalhdl__saxonsoc](https://github.com/SpinalHDL/SaxonSoc) (instantiates [`hardware/deprecated/blackice/BlackiceSocArduino.scala`](https://github.com/SpinalHDL/SaxonSoc/blob/227b8686b734c7995b10ce81e193a01b010d2407/hardware/deprecated/blackice/BlackiceSocArduino.scala))
- [w531t4__fpga_led_display](https://github.com/w531t4/fpga_led_display) (instantiates [`src/include/tb_spi_streamer.svh`](https://github.com/w531t4/fpga_led_display/blob/7ba06f8f6dd70ef95ebfeca1103158c1868886e0/src/include/tb_spi_streamer.svh))

## Other catalogued projects

Catalogued repos tagged `spi` (35) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
