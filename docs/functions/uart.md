---
title: "UART"
parent: "Cores by function"
nav_order: 12
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# UART

Serial transmit/receive cores and UART bridges.

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [wbuart Wishbone UART](#core-pifive-wbuart) ★ | [asinghani__pifive-cpu](https://github.com/asinghani/pifive-cpu) | SystemVerilog | Apache-2.0 | ECP5 | 1 |
| [f32c sio serial I/O](#core-f32c-sio) | [f32c__f32c](https://github.com/f32c/f32c) | VHDL | BSD-2-Clause | any | 0 |
| [SAO UART phy (minimal 8N1)](#core-hazard3-sao-uart-phy) | [ulx3s__hazard3](https://github.com/ulx3s/Hazard3) | Verilog | Apache-2.0 | ECP5 | 0 |
| [Solderpad uart_tx (Tom Verbeure)](#core-verilog-tomverbeure-uart-tx) | [lawrie__ulx3s_examples](https://github.com/lawrie/ulx3s_examples) | Verilog | Solderpad Hardware License v0.51 | any | 0 |
| [verilog-uart tx/rx](#core-volnirr-verilog-uart) | [volnirr__verilog-uart](https://github.com/Volnirr/verilog-uart) | Verilog | none found | any | 0 |

## Cores

### wbuart Wishbone UART (best) {#core-pifive-wbuart}

Wishbone-mapped 8N1 UART: separate tx/rx byte engines plus FIFOs behind a wbuart register-file wrapper. Built for the pifive-cpu SoC on ULX3S 85F.

| | |
|---|---|
| Repository | [asinghani__pifive-cpu](https://github.com/asinghani/pifive-cpu): 3-stage RV32I(+M) |
| Files | [`soc/rtl/verilog/wbuart.sv`](https://github.com/asinghani/pifive-cpu/blob/81ca4088242eeb29c56ddd31d2c53a61a047db53/soc/rtl/verilog/wbuart.sv), [`soc/rtl/verilog/uart_tx.sv`](https://github.com/asinghani/pifive-cpu/blob/81ca4088242eeb29c56ddd31d2c53a61a047db53/soc/rtl/verilog/uart_tx.sv), [`soc/rtl/verilog/uart_rx.sv`](https://github.com/asinghani/pifive-cpu/blob/81ca4088242eeb29c56ddd31d2c53a61a047db53/soc/rtl/verilog/uart_rx.sv), [`soc/rtl/verilog/uart_fifo.sv`](https://github.com/asinghani/pifive-cpu/blob/81ca4088242eeb29c56ddd31d2c53a61a047db53/soc/rtl/verilog/uart_fifo.sv) |
| Top module | `wbuart` |
| Language | SystemVerilog |
| License | Apache-2.0 (repo LICENSE; no per-file header) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | scripts/tests/test_uart.py, cpu/tests/legacy/test_uart.py (cocotb, self-checking) |

**On ULX3S:** Proven on ULX3S 85F via fpga/ulx3s/Makefile (yosys+nextpnr-ecp5+ecppack); wire wbuart into any Wishbone SoC.

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [zipcpu__icozip](https://github.com/ZipCPU/icozip) (instantiates [`rtl/uart/speechfifo.v`](https://github.com/ZipCPU/icozip/blob/4e7d8fda118e641865edcff41f1c61d23d1534f7/rtl/uart/speechfifo.v))

### f32c sio serial I/O {#core-f32c-sio}

f32c SoC's UART peripheral, memory-mapped, used across many f32c ULX3S/ECP5 boards for the boot loader console.

| | |
|---|---|
| Repository | [f32c__f32c](https://github.com/f32c/f32c): f32c: retargetable RISC-V/MIPS 32-bit soft CPU + SoC library |
| Files | [`rtl/soc/sio.vhd`](https://github.com/f32c/f32c/blob/7dbf56d42a94ae599eabfd1e7fa15db14a10afd7/rtl/soc/sio.vhd) |
| Top module | `sio` |
| Language | VHDL |
| License | BSD-2-Clause (file header, Copyright Marko Zec) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** VHDL, no vendor primitives; f32c's own build is Diamond-only but this file is portable to an open ghdl-yosys flow.

Full review: [f32c__f32c](../projects/f32c__f32c.md).

### SAO UART phy (minimal 8N1) {#core-hazard3-sao-uart-phy}

Minimal byte-oriented 8N1 UART interface used by the ULX3S example SoC's ESP32 SAO sideband link.

| | |
|---|---|
| Repository | [ulx3s__hazard3](https://github.com/ulx3s/Hazard3): Hazard3 RV32IMACZb* CPU: ULX3S/ULX4M-LD fork with dedicated build docs, incl. |
| Files | [`example_soc/soc/sao_uart_phy.v`](https://github.com/ulx3s/Hazard3/blob/3c0aca063517bb7fdbe869019c984954c7dd5c97/example_soc/soc/sao_uart_phy.v) |
| Top module | `sao_uart_phy` |
| Language | Verilog |
| License | Apache-2.0 (repo LICENSE) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | none found |

**On ULX3S:** Actually instantiated in ulx3s__hazard3's example_soc.v build for ULX3S 85F/ULX4M-LD; simplest place to start for a tiny UART.

### Solderpad uart_tx (Tom Verbeure) {#core-verilog-tomverbeure-uart-tx}

Simple UART transmitter copied across several lawrie ULX3S example/retro-computer repos alongside the PS/2 examples.

| | |
|---|---|
| Repository | [lawrie__ulx3s_examples](https://github.com/lawrie/ulx3s_examples): Lawrie Griffiths Verilog examples: HDMI, displays, PS/2, SDRAM, USB host, CPUs |
| Files | [`ps2/uart_tx.v`](https://github.com/lawrie/ulx3s_examples/blob/b6ff00099265401fef4843e4e89c2ac54254c95f/ps2/uart_tx.v) |
| Top module | `uart_tx` |
| Language | Verilog |
| License | Solderpad Hardware License v0.51 (file header, Copyright 2018 Tom Verbeure) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Weak-reciprocal license (Solderpad), not pure permissive; check terms before closed-source reuse.

Full review: [lawrie__ulx3s_examples](../projects/lawrie__ulx3s_examples.md).

### verilog-uart tx/rx {#core-volnirr-verilog-uart}

Small dedicated, board-independent UART tx/rx pair with a well-specified README (exact baud error, framing/noise handling).

| | |
|---|---|
| Repository | [volnirr__verilog-uart](https://github.com/Volnirr/verilog-uart): Standalone 8N1 UART transmitter/receiver core for ECP5/ULX3S, no vendor primitives, with iverilog testbenches |
| Files | [`rtl/uart_tx.v`](https://github.com/Volnirr/verilog-uart/blob/c32ebee910cadaebedec9d0c52542e7e3095c07e/rtl/uart_tx.v), [`rtl/uart_rx.v`](https://github.com/Volnirr/verilog-uart/blob/c32ebee910cadaebedec9d0c52542e7e3095c07e/rtl/uart_rx.v) |
| Top module | n/a |
| Language | Verilog |
| License | none found |
| FPGA / primitives | any: none (portable) |
| Tests | tb/receiver_tb.v, tb/transmitter_tb.v (iverilog, self-checking status not confirmed) |

**On ULX3S:** ulx3s.lpf present but no committed build script; drop the two files into a project and instantiate directly.

## Other catalogued projects

Catalogued repos tagged `uart` (195) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
