---
title: "Linux-capable SoCs"
parent: "Cores by function"
nav_order: 31
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# Linux-capable SoCs

SoCs that boot Linux.

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [linux-on-litex-vexriscv (ULX3S board target)](#core-litex-vexriscv-linux) ★ | [litex-hub__linux-on-litex-vexriscv](https://github.com/litex-hub/linux-on-litex-vexriscv) | Python (LiteX board description) | BSD-2-Clause | any | 0 |
| [flix-v KianV-Apio (ULX3S-12F, apio flow)](#core-flix-v-kianv-apio) | [fpgawars__flix-v](https://github.com/FPGAwars/FLIX-V) | Verilog | LGPL-2.1 | ECP5 | 0 |
| [KianV Linux/XV6 SoC](#core-kianriscv-linux-soc) | [splinedrive__kianriscv](https://github.com/splinedrive/kianRiscV) | Verilog | mixed: ISC | ECP5 | 0 |
| [Koti RV32IMA+MMU SoC (mainline Linux 6.12 on ULX3S 85F)](#core-koti-linux-soc) | [joaln27__koti](https://github.com/joaln27/koti) | SystemVerilog | Apache-2.0 | ECP5 | 0 |
| [SaxonSoc Linux/U-Boot BSP for ULX3S](#core-saxonsoc-radiona-ulx3s) | [spinalhdl__saxonsoc](https://github.com/SpinalHDL/SaxonSoc) | Scala (SpinalHDL SoC generator) +… | MIT (LICENSE) | ECP5 | 0 |
| [Vernier-RV32 RV32IMA Linux-capable Wishbone SoC](#core-vernier-rv32-linux-soc) | [aravindrajeshkanna__vernier-rv32](https://github.com/AravindRajeshkanna/vernier-rv32) | Verilog | Apache-2.0 WITH SHL-2.1 | ECP5 | 3 |

## Cores

### linux-on-litex-vexriscv (ULX3S board target) (best) {#core-litex-vexriscv-linux}

The de-facto standard 'Linux on an FPGA' project: boards.py's ULX3S class wires LiteX's VexRiscv SoC generator to litex_boards' radiona_ulx3s target via make.py --board=ulx3s, with a buildroot Linux image in the wider LiteX ecosystem.

| | |
|---|---|
| Repository | [litex-hub__linux-on-litex-vexriscv](https://github.com/litex-hub/linux-on-litex-vexriscv): Linux on LiteX-VexRiscv |
| Files | [`boards.py`](https://github.com/litex-hub/linux-on-litex-vexriscv/blob/05fc5e43e579ac67769c2c930778901a1125f0b4/boards.py) |
| Top module | n/a |
| Language | Python (LiteX board description) |
| License | BSD-2-Clause (LICENSE) |
| FPGA / primitives | any: none (portable) |
| Tests | 2 tb files in ./test (scope unclear, likely LiteX-side unit tests, not ULX3S-specific) |

**On ULX3S:** Needs the external litex/litex-boards/migen toolchain (not vendored here); 45F/85F in practice for enough BRAM/SDRAM.

### flix-v KianV-Apio (ULX3S-12F, apio flow) {#core-flix-v-kianv-apio}

KianV RV32 core (Harris multicycle edition) plus SDRAM controller and UART, packaged as an apio project targeting ulx3s-12f directly (apio.ini board = ulx3s-12f), a lighter-weight alternative to the 85F Linux SoCs.

| | |
|---|---|
| Repository | [fpgawars__flix-v](https://github.com/FPGAwars/FLIX-V): FLIX-V: KianV RISC-V SoC running Linux |
| Files | [`Hardware/KianV-Apio`](https://github.com/FPGAwars/FLIX-V/tree/d8c229dc90be4a3b2e37252a53767d06c394f755/Hardware/KianV-Apio) |
| Top module | `kianv_harris_mc_edition` |
| Language | Verilog |
| License | LGPL-2.1 |
| FPGA / primitives | ECP5: none (portable) |
| Tests | none found |

**On ULX3S:** apio.ini already selects ulx3s-12f; verify current Linux-boot capability, as 12F apio flows are typically limited to bare-metal by BRAM size.

### KianV Linux/XV6 SoC {#core-kianriscv-linux-soc}

Full SoC around kianv_sv32.v (SDRAM controllers, icache/dcache, CLINT/PLIC, QSPI, UART) built to run Linux and XV6, with board targets from 12k up to um-85k.

| | |
|---|---|
| Repository | [splinedrive__kianriscv](https://github.com/splinedrive/kianRiscV): KianV RV32IMA SV32 Linux SoCs |
| Files | [`linux_socs/LinuxSoC_v2`](https://github.com/splinedrive/kianRiscV/tree/da994e6c25b0667d6579922f4bab8d800d19e944/linux_socs/LinuxSoC_v2) |
| Top module | n/a |
| Language | Verilog |
| License | mixed: ISC (LICENSE.md), Apache-2.0/BSD-2/GPL-2.0 per-file SPDX; kianv_sv32.v itself Apache-2.0 |
| FPGA / primitives | ECP5: none (portable) |
| Tests | 1 tb file present |

**On ULX3S:** 85F default; the standalone kianv_sv32.v core alone is catalogued separately under cpu-riscv.

### Koti RV32IMA+MMU SoC (mainline Linux 6.12 on ULX3S 85F) {#core-koti-linux-soc}

RV32IMA core with TLB/icache/dcache/MMU that the repo documents booting mainline Linux 6.12 (buildroot, busybox) to a userspace console on a ULX3S 85F, with vendored USB HID host, SD-SPI and DVI TX peripherals.

| | |
|---|---|
| Repository | [joaln27__koti](https://github.com/joaln27/koti): Koti: RV32IMA Linux-capable SoC |
| Files | [`src/koti_core.sv`](https://github.com/joaln27/koti/blob/9fb88761388653c3c18f70edd0deae74f2f6e94c/src/koti_core.sv) |
| Top module | `koti_core` |
| Language | SystemVerilog |
| License | Apache-2.0 |
| FPGA / primitives | ECP5: none (portable) |
| Tests | 23 cocotb tb files in ./test, including a full Linux boot simulated on every push (per README) |

**On ULX3S:** README shows a boot-log screenshot; single-author project, verify current build status before depending on it.

### SaxonSoc Linux/U-Boot BSP for ULX3S {#core-saxonsoc-radiona-ulx3s}

Board support package wiring SpinalHDL's SaxonSoc BMB-bus generator to the ULX3S, with minimal and smp U-Boot/Linux configs; lawrie__spinalulx3s ships prebuilt saxon-bin/ bitstreams from the same generator (minimal/sdram/linux variants).

| | |
|---|---|
| Repository | [spinalhdl__saxonsoc](https://github.com/SpinalHDL/SaxonSoc): SaxonSoc: SpinalHDL SoC framework |
| Files | [`bsp/radiona/ulx3s`](https://github.com/SpinalHDL/SaxonSoc/tree/227b8686b734c7995b10ce81e193a01b010d2407/bsp/radiona/ulx3s) |
| Top module | n/a |
| Language | Scala (SpinalHDL SoC generator) + C/config |
| License | MIT (LICENSE) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | tb dirs present (./test, ./software/standalone/test); no self-checking make target found |

**On ULX3S:** 12F for minimal (--12k), 25F for smp (FPGA_KS=25k); dok3r__ulx3s-saxonsoc/ulx3s__ulx3s-saxonsoc hold the build.sh/buildsmp.sh recipes.

### Vernier-RV32 RV32IMA Linux-capable Wishbone SoC {#core-vernier-rv32-linux-soc}

5-stage RV32IMA + Zicsr pipeline with Sv32 MMU, CLINT/PLIC, boot ROM, UART, GPIO, SPI/SD and a Wishbone SoC fabric; boots mainline-style Linux to userspace on a real ULX3S LFE5U-85F (fpga/README.md logs SOC-TEST: PASS and a full Linux boot).

| | |
|---|---|
| Repository | [aravindrajeshkanna__vernier-rv32](https://github.com/AravindRajeshkanna/vernier-rv32): Vernier-RV32: RV32IMA 5-stage pipelined SoC |
| Files | [`rtl/top.v`](https://github.com/AravindRajeshkanna/vernier-rv32/blob/3284906e237a8b9b9ff1ebf198869ef9dc20885b/rtl/top.v), [`rtl/soc/soc_top.v`](https://github.com/AravindRajeshkanna/vernier-rv32/blob/3284906e237a8b9b9ff1ebf198869ef9dc20885b/rtl/soc/soc_top.v), [`fpga/ulx3s_top.v`](https://github.com/AravindRajeshkanna/vernier-rv32/blob/3284906e237a8b9b9ff1ebf198869ef9dc20885b/fpga/ulx3s_top.v), [`fpga/constraints/ulx3s.lpf`](https://github.com/AravindRajeshkanna/vernier-rv32/blob/3284906e237a8b9b9ff1ebf198869ef9dc20885b/fpga/constraints/ulx3s.lpf) |
| Top module | `ulx3s_top` |
| Language | Verilog |
| License | Apache-2.0 WITH SHL-2.1 (Solderpad Hardware License 2.1; SPDX header in LICENSE) |
| FPGA / primitives | ECP5: `EHXPLLL`, `ODDRX1F`, `ODDRX2F`, `DELAYG`, `DQSBUFM` |
| Tests | sim/ and tests/ dirs, 65 tb/test files, verilator+iverilog (scan_tests.sh); riscv-tests + Spike co-simulation per README badges |

**On ULX3S:** Real, hardware-verified pin-out (fpga/constraints/ulx3s.lpf, every pin placed); Fmax margin is thin (23-26 MHz vs the board's 25 MHz, 4/6 seeds close) - see fpga/README.md before reusing at full clock. Also has an ECPIX5 DDR3 variant (rtl/soc/ddr3_*_ecp5.v) and an unrun Xilinx/Vivado path.

**Used by 3 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [danodus__xgsoc](https://github.com/danodus/xgsoc) (instantiates [`rtl/icepi-zero/icepi_zero_top.sv`](https://github.com/danodus/xgsoc/blob/8a4d9213e5ebe3abe42ba30fddb0bd4f9f4a843f/rtl/icepi-zero/icepi_zero_top.sv))
- [evansm7__arcdvi](https://github.com/evansm7/ArcDVI) (instantiates [`tb/tb_top.v`](https://github.com/evansm7/ArcDVI/blob/6640691c6862ca8949a7f2bb37b2ce00c18f90ab/tb/tb_top.v))
- [markus-zzz__myc64](https://github.com/markus-zzz/myc64) (instantiates [`rtl/myc64-soc/myc64-soc-top.v`](https://github.com/markus-zzz/myc64/blob/7ab3c5414caf193b0979b322d94e71cf6c8f8405/rtl/myc64-soc/myc64-soc-top.v))

## Other catalogued projects

Catalogued repos tagged `linux` (22) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
