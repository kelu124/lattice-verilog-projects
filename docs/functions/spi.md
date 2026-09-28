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
| [glasgow SPI controller (Amaranth)](#core-glasgow-spi) | [glasgowembedded__glasgow](https://github.com/GlasgowEmbedded/glasgow) | Python (Amaranth) | 0BSD OR Apache-2.0 | any | 3 |
| [llsdspi low-level SPI engine](#core-zipcpu-llsdspi) | [zipcpu__sdspi](https://github.com/ZipCPU/sdspi) | Verilog | GPL-3.0 (per-file header, no top-level LICENSE) | any | 0 |
| [SPI master (Bus Pirate NextGen Ultra)](#core-buspirateultrahdl-spimaster) | [dangerousprototypes__buspirateultrahdl](https://github.com/DangerousPrototypes/BusPirateUltraHDL) | Verilog | GPL-3.0 (repo LICENSE) | any | 5 |

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

**Used by 3 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [asinghani__pifive-cpu](https://github.com/asinghani/pifive-cpu) (copies [`soc/rtl/periphs/spi.py`](https://github.com/asinghani/pifive-cpu/blob/81ca4088242eeb29c56ddd31d2c53a61a047db53/soc/rtl/periphs/spi.py))
- [cheyao__icepi-zero](https://github.com/cheyao/icepi-zero) (copies [`gateware/spi/rpi/spi.py`](https://github.com/cheyao/icepi-zero/blob/e01faa2bd35dcb7269827f8420b845d46c78c869/gateware/spi/rpi/spi.py))
- [greatscottgadgets__luna](https://github.com/greatscottgadgets/luna) (copies [`luna/gateware/interface/spi.py`](https://github.com/greatscottgadgets/luna/blob/82a8f733296603b70ba56755206e13092609c6f0/luna/gateware/interface/spi.py))

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

**Used by 5 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [egorxe__openglory](https://github.com/egorxe/openglory) (instantiates [`hw/litex/radiona_ulx3s.py`](https://github.com/egorxe/openglory/blob/84d642c609d599542f123847395999f853d8f804/hw/litex/radiona_ulx3s.py))
- [litex-hub__linux-on-litex-vexriscv](https://github.com/litex-hub/linux-on-litex-vexriscv) (instantiates [`soc_linux.py`](https://github.com/litex-hub/linux-on-litex-vexriscv/blob/05fc5e43e579ac67769c2c930778901a1125f0b4/soc_linux.py))
- [pablogs9__rocketfpga](https://github.com/pablogs9/RocketFPGA) (instantiates [`Software/FPGA Sample Code/Codec/configurator.v`](https://github.com/pablogs9/RocketFPGA/blob/dc2bdf7639637445c21d882d17f6c4dfb30a8447/Software/FPGA Sample Code/Codec/configurator.v))
- [spinalhdl__saxonsoc](https://github.com/SpinalHDL/SaxonSoc) (instantiates [`hardware/deprecated/blackice/BlackiceSocArduino.scala`](https://github.com/SpinalHDL/SaxonSoc/blob/227b8686b734c7995b10ce81e193a01b010d2407/hardware/deprecated/blackice/BlackiceSocArduino.scala))
- [w531t4__fpga_led_display](https://github.com/w531t4/fpga_led_display) (instantiates [`src/include/tb_spi_streamer.svh`](https://github.com/w531t4/fpga_led_display/blob/7ba06f8f6dd70ef95ebfeca1103158c1868886e0/src/include/tb_spi_streamer.svh))

## Other catalogued projects

Catalogued repos tagged `spi` (20) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
