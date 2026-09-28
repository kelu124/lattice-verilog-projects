---
title: "SDRAM controllers"
parent: "Cores by function"
nav_order: 7
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# SDRAM controllers

SDR SDRAM controllers (the ULX3S has 32 MB SDR SDRAM).

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [hdl4fpga generation-generic SDRAM controller](#core-hdl4fpga-sdram-ctlr) ★ | [hdl4fpga__hdl4fpga](https://github.com/hdl4fpga/hdl4fpga) | VHDL | MIT (LICENSE) | ECP5 | 0 |
| [c-elegans ULX3S SDRAM controller](#core-c-elegans-sdram-controller3) | [c-elegans__ulx3s_sdram](https://github.com/C-Elegans/ulx3s_sdram) | Verilog | none found | ECP5 | 0 |
| [f32c generic SDR SDRAM controller](#core-f32c-sdram-vhdl) | [f32c__f32c](https://github.com/f32c/f32c) | VHDL | MIT (Mike Field, file header) | any | 0 |
| [KianV mt48lc16m16a2_ctrl SDRAM controller](#core-kianriscv-mt48lc16m16a2-ctrl) | [splinedrive__kianriscv](https://github.com/splinedrive/kianRiscV) | Verilog | ISC-style | ECP5 | 2 |
| [Oberon SDRAM_16bit controller + cache](#core-emard-oberon-sdram-cache) | [emard__oberon](https://github.com/emard/oberon) | Verilog | LGPL-2.1-or-later | ECP5 | 3 |
| [sdram_pnru simplistic SDRAM controller](#core-emard-misc-sdram-pnru) | [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc) | Verilog | public domain | ECP5 | 1 |

## Cores

### hdl4fpga generation-generic SDRAM controller (best) {#core-hdl4fpga-sdram-ctlr}

Chip-table-driven SDR/DDR/DDR2/DDR3 controller; ULX3S apps (graphics, scopeio) instantiate it with chip_data="MT48LC16M16MA2-7E", the ULX3S's real SDR chip, paired with the ecp5_sdrphy gearbox PHY.

| | |
|---|---|
| Repository | [hdl4fpga__hdl4fpga](https://github.com/hdl4fpga/hdl4fpga): hdl4fpga: portable VHDL library, ScopeIO oscilloscope, SDRAM graphics, eth/USB links |
| Files | [`library/sdram/sdram_ctlr.vhd`](https://github.com/hdl4fpga/hdl4fpga/blob/662986ba0f17b7ce3a066ddcb799d42fa1b24dea/library/sdram/sdram_ctlr.vhd), [`library/latticesemi/ecp5/ecp5_sdrphy.vhd`](https://github.com/hdl4fpga/hdl4fpga/blob/662986ba0f17b7ce3a066ddcb799d42fa1b24dea/library/latticesemi/ecp5/ecp5_sdrphy.vhd) |
| Top module | `sdram_ctlr` |
| Language | VHDL |
| License | MIT (LICENSE) |
| FPGA / primitives | ECP5: `oddrx1f`, `fd1s3ax` |
| Tests | waveform-only: boards/ULX3S/testbenches/graphics.vhd + graphics_structure.do (ModelSim) |

**On ULX3S:** Use chip_data="MT48LC16M16MA2-7E"; only the SDR path applies. Needs hdo/base + sdrampkg package dependencies.

Full review: [hdl4fpga__hdl4fpga](../projects/hdl4fpga__hdl4fpga.md).

### c-elegans ULX3S SDRAM controller {#core-c-elegans-sdram-controller3}

Standalone ULX3S SDRAM controller derived from the hamsterworks DE0-Nano FSM design, built and simulated with an IS42S16160.v chip model specifically for the ULX3S board.

| | |
|---|---|
| Repository | [c-elegans__ulx3s_sdram](https://github.com/C-Elegans/ulx3s_sdram): Small SDRAM controller experiments/testbed for ULX3S |
| Files | [`sdram_controller3.v`](https://github.com/C-Elegans/ulx3s_sdram/blob/a4bd4cd54128104c3bf9542acb5726482c3378d2/sdram_controller3.v) |
| Top module | `sdram_controller3` |
| Language | Verilog |
| License | none found |
| FPGA / primitives | ECP5: none (portable) |
| Tests | waveform-only: testbench.v, driver_tb.v (no $display/assert pass-fail found) |

**On ULX3S:** Direct ULX3S reference controller; repo has no LICENSE file, treat as all-rights-reserved unless clarified.

### f32c generic SDR SDRAM controller {#core-f32c-sdram-vhdl}

Generic SDR SDRAM command sequencer with a C_ports-generic multi-port arbiter, no vendor primitives; used across all f32c ULX3S SoC targets (12F/25F/45F/85F).

| | |
|---|---|
| Repository | [f32c__f32c](https://github.com/f32c/f32c): f32c: retargetable RISC-V/MIPS 32-bit soft CPU + SoC library |
| Files | [`rtl/soc/sdram.vhd`](https://github.com/f32c/f32c/blob/7dbf56d42a94ae599eabfd1e7fa15db14a10afd7/rtl/soc/sdram.vhd) |
| Top module | `sdram` |
| Language | VHDL |
| License | MIT (Mike Field, file header) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Plain clk/reset + C_clk_freq generic; drop-in SDRAM controller for a new ULX3S design.

Full review: [f32c__f32c](../projects/f32c__f32c.md).

### KianV mt48lc16m16a2_ctrl SDRAM controller {#core-kianriscv-mt48lc16m16a2-ctrl}

SDRAM controller for the MT48LC16M16A2 chip used by the Linux-capable KianV RISC-V SoC (85F default, 12k..um-85k targets); part of a maintained, actively used Linux-on-ULX3S project.

| | |
|---|---|
| Repository | [splinedrive__kianriscv](https://github.com/splinedrive/kianRiscV): KianV RV32IMA SV32 Linux SoCs |
| Files | [`linux_socs/kianv_harris_mcycle_edition/sdram/mt48lc16m16a2_ctrl.v`](https://github.com/splinedrive/kianRiscV/blob/da994e6c25b0667d6579922f4bab8d800d19e944/linux_socs/kianv_harris_mcycle_edition/sdram/mt48lc16m16a2_ctrl.v) |
| Top module | `mt48lc16m16a2_ctrl` |
| Language | Verilog |
| License | ISC-style (LICENSE.md, Hirosh Dabui, permissive notice matching ISC wording) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | none found |

**On ULX3S:** Designed for the exact SDR chip ULX3S ships with; check icache/dcache wiring in the same sdram/ directory if reusing the whole memory subsystem.

**Used by 2 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [darklife__darkriscv](https://github.com/darklife/darkriscv) (instantiates [`rtl/darksocv.v`](https://github.com/darklife/darkriscv/blob/974034aa8079039a36b89c14dcdfed575de183b7/rtl/darksocv.v))
- [fpgawars__flix-v](https://github.com/FPGAwars/FLIX-V) (instantiates [`Hardware/KianV-Apio/soc-top.v`](https://github.com/FPGAwars/FLIX-V/blob/d8c229dc90be4a3b2e37252a53767d06c394f755/Hardware/KianV-Apio/soc-top.v))

### Oberon SDRAM_16bit controller + cache {#core-emard-oberon-sdram-cache}

Next186-derived 16-bit SDRAM controller paired with a direct-mapped cache_controller.v, used by the Project Oberon RISC5 ULX3S build (85F trellis / 12F diamond).

| | |
|---|---|
| Repository | [emard__oberon](https://github.com/emard/oberon): Project Oberon RISC5 |
| Files | [`hdl/sdram.v`](https://github.com/emard/oberon/blob/ced69d7e0150c34ad4e0acc55519a421fa9f8e37/hdl/sdram.v), [`hdl/cache_controller.v`](https://github.com/emard/oberon/blob/ced69d7e0150c34ad4e0acc55519a421fa9f8e37/hdl/cache_controller.v) |
| Top module | `SDRAM_16bit` |
| Language | Verilog |
| License | LGPL-2.1-or-later (Next186/opencores.org, Nicolae Dumitrache, file header) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | none found |

**On ULX3S:** Copyleft (LGPL-2.1+): fine to link against, modifications to the file itself must stay LGPL.

**Used by 3 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [cheyao__oberon](https://github.com/cheyao/oberon) (instantiates [`hdl/RISC5Top.OStation.v`](https://github.com/cheyao/oberon/blob/07511b33357a95d68db67fc9351c86a13d106ecf/hdl/RISC5Top.OStation.v))
- [danodus__xgsoc](https://github.com/danodus/xgsoc) (instantiates [`rtl/soc_top.sv`](https://github.com/danodus/xgsoc/blob/8a4d9213e5ebe3abe42ba30fddb0bd4f9f4a843f/rtl/soc_top.sv))
- [emard__next186](https://github.com/emard/Next186) (instantiates [`emard/replace/ddr_186.v`](https://github.com/emard/Next186/blob/cfd9550f7aa4f126839692755d4eb3793ea5e40e/emard/replace/ddr_186.v))

### sdram_pnru simplistic SDRAM controller {#core-emard-misc-sdram-pnru}

Simplistic public-domain SDR SDRAM controller for 4x4Mx16 chips (e.g. MT48LC16M16A2): one access per system access, all 4 banks kept open, distributed refresh; part of EMARD's ULX3S example library.

| | |
|---|---|
| Repository | [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc): ULX3S misc/advanced examples: EMARD's building-block library |
| Files | [`examples/sdram/sdram_pnru/sdram_pnru.v`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/sdram/sdram_pnru/sdram_pnru.v) |
| Top module | `sdram_pnru` |
| Language | Verilog |
| License | public domain (explicit header statement) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | none found |

**On ULX3S:** Smallest/simplest of the seven sdram/ variants in ulx3s-misc; good starting point when a full-featured controller is overkill.

Full review: [emard__ulx3s-misc](../projects/emard__ulx3s-misc.md).

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [mcejp__poly94](https://github.com/mcejp/Poly94) (instantiates [`rtl/top.sv`](https://github.com/mcejp/Poly94/blob/e2fa3d9406ee09760004d1ff97d4125825c2d345/rtl/top.sv))

## Other catalogued projects

Catalogued repos tagged `sdram` (63) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
