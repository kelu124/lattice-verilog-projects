---
title: "PLLs and clocking"
parent: "Cores by function"
nav_order: 31
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# PLLs and clocking

ECP5 EHXPLLL wrappers and PLL parameter calculators.

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [ecp5pll parametric PLL](#core-emard-ecp5pll) ★ | [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc) | SystemVerilog, VHDL | BSD (// (c)EMARD / License=BSD, file header) | ECP5 | 74 |
| [blip nMigen ECP5 PLL wrapper](#core-bqqbarbhg-blip-pll) | [bqqbarbhg__blipv1](https://github.com/bqqbarbhg/blipv1) | Python (nMigen) | none found | ECP5 | 0 |
| [Glasgow ECP5 PLL parameter solver (Amaranth)](#core-glasgow-ecp5-pll) | [glasgowembedded__glasgow](https://github.com/GlasgowEmbedded/glasgow) | Python (Amaranth) | 0BSD OR Apache-2.0 | ECP5 | 0 |
| [hdl4fpga ecp5_videodcm / ecp5_sdramdcm clock generators](#core-hdl4fpga-ecp5-clockgen) | [hdl4fpga__hdl4fpga](https://github.com/hdl4fpga/hdl4fpga) | VHDL | MIT (LICENSE) | ECP5 | 0 |

## Cores

### ecp5pll parametric PLL (best) {#core-emard-ecp5pll}

Computes EHXPLLL divider/phase parameters from requested in/out frequencies at elaboration time; up to 4 outputs with independent phase, actual achieved frequency reported in the trellis/Diamond build log. Copied into dozens of other repos in this collection.

| | |
|---|---|
| Repository | [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc): ULX3S misc/advanced examples: EMARD's building-block library |
| Files | [`examples/ecp5pll/hdl/sv/ecp5pll.sv`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/ecp5pll/hdl/sv/ecp5pll.sv), [`examples/ecp5pll/hdl/vhd/ecp5pll.vhd`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/ecp5pll/hdl/vhd/ecp5pll.vhd) |
| Top module | `ecp5pll` |
| Language | SystemVerilog, VHDL |
| License | BSD (// (c)EMARD / License=BSD, file header) |
| FPGA / primitives | ECP5: `EHXPLLL` |
| Tests | none found |

**On ULX3S:** Drop-in on ULX3S: in_hz=25000000 (board oscillator); no other configuration needed.

Full review: [emard__ulx3s-misc](../projects/emard__ulx3s-misc.md).

**Used by 74 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [advikbahadur__ulx3s-superresolution-cnn](https://github.com/ADVIKBAHADUR/ULX3s-Superresolution-CNN) (instantiates [`src/top_module.v`](https://github.com/ADVIKBAHADUR/ULX3s-Superresolution-CNN/blob/7979af367cc20e4393071c718ab0e04dae12ad86/src/top_module.v))
- [bjonnh__ulx3s-synth](https://github.com/bjonnh/ulx3s-synth) (instantiates [`i2s.v`](https://github.com/bjonnh/ulx3s-synth/blob/b8448b602cb6a6772449059746ff5107dc78601a/i2s.v))
- [bqqbarbhg__blipv1](https://github.com/bqqbarbhg/blipv1) (instantiates [`blip/rtl/ecp5/io.py`](https://github.com/bqqbarbhg/blipv1/blob/e978a5aa368f4b24aebb8954a6cc75b39522f436/blip/rtl/ecp5/io.py))
- [cheyao__icepi-zero](https://github.com/cheyao/icepi-zero) (instantiates [`gateware/sdram/memtest/memtest.sv`](https://github.com/cheyao/icepi-zero/blob/e01faa2bd35dcb7269827f8420b845d46c78c869/gateware/sdram/memtest/memtest.sv))
- [cheyao__nes_ecp5](https://github.com/cheyao/nes_ecp5) (instantiates [`top.v`](https://github.com/cheyao/nes_ecp5/blob/e8dd1eb7f9f440a552cd24c0b936e58705a272e7/top.v))
- [cheyao__oberon](https://github.com/cheyao/oberon) (instantiates [`hdl/pnru_mix/Ulx3s_Top.v`](https://github.com/cheyao/oberon/blob/07511b33357a95d68db67fc9351c86a13d106ecf/hdl/pnru_mix/Ulx3s_Top.v))
- [cheyao__sega-sms](https://github.com/cheyao/sega-sms) (instantiates [`src/sms.v`](https://github.com/cheyao/sega-sms/blob/c37e846d94f88eb9a95f44b15f2b23019aa25a26/src/sms.v))
- [danodus__ulx3s_68k](https://github.com/danodus/ulx3s_68k) (instantiates [`src/test68.v`](https://github.com/danodus/ulx3s_68k/blob/ee10339210d0c302143745d3cc584a21a4878ace/src/test68.v))
- [danodus__ulx3s_sms](https://github.com/danodus/ulx3s_sms) (instantiates [`src/sms.v`](https://github.com/danodus/ulx3s_sms/blob/13c2361a5039d205de47857bab9201055ac9e566/src/sms.v))
- [danodus__xgsoc](https://github.com/danodus/xgsoc) (instantiates [`rtl/icepi-zero/icepi_zero_top.sv`](https://github.com/danodus/xgsoc/blob/8a4d9213e5ebe3abe42ba30fddb0bd4f9f4a843f/rtl/icepi-zero/icepi_zero_top.sv))
- [datanoisetv__colorlight-i9-aes67](https://github.com/DatanoiseTV/colorlight-i9-aes67) (instantiates [`litex/soc.py`](https://github.com/DatanoiseTV/colorlight-i9-aes67/blob/71420b772d48409ae8e3a70c3103828495687737/litex/soc.py))
- [dlobato__cps1-musicbox](https://github.com/dlobato/cps1-musicbox) (instantiates [`radiona_ulx3s.py`](https://github.com/dlobato/cps1-musicbox/blob/dc940ca9ecd5fa2685518fae2c92d701167fe4a0/radiona_ulx3s.py))
- [dschaefer__fpga-template](https://github.com/dschaefer/fpga-template) (instantiates [`top.sv`](https://github.com/dschaefer/fpga-template/blob/575a4b1cf43a325951bb3662020ffeec7f5b3bfc/top.sv))
- [dulatello08__litex-cpu-testing](https://github.com/dulatello08/litex-cpu-testing) (instantiates [`scripts/gen_soc.py`](https://github.com/dulatello08/litex-cpu-testing/blob/3b5d386971aedd6b98030c8db214ca888cb0929f/scripts/gen_soc.py))
- [egorxe__openglory](https://github.com/egorxe/openglory) (instantiates [`hw/litex/radiona_ulx3s.py`](https://github.com/egorxe/openglory/blob/84d642c609d599542f123847395999f853d8f804/hw/litex/radiona_ulx3s.py))
- … and 59 more (see `data/core_usage.json`)

### blip nMigen ECP5 PLL wrapper {#core-bqqbarbhg-blip-pll}

nMigen PLL wrapper (PllClock) with an ECP5-specific backend, built directly against nmigen_boards' ULX3S_85F_Platform for the blip engine's ULX3S target.

| | |
|---|---|
| Repository | [bqqbarbhg__blipv1](https://github.com/bqqbarbhg/blipv1): nMigen/Amaranth DVI |
| Files | [`blip/rtl/pll.py`](https://github.com/bqqbarbhg/blipv1/blob/e978a5aa368f4b24aebb8954a6cc75b39522f436/blip/rtl/pll.py), [`blip/rtl/ecp5/pll.py`](https://github.com/bqqbarbhg/blipv1/blob/e978a5aa368f4b24aebb8954a6cc75b39522f436/blip/rtl/ecp5/pll.py) |
| Top module | n/a |
| Language | Python (nMigen) |
| License | none found |
| FPGA / primitives | ECP5: `EHXPLLL` |
| Tests | none found |

**On ULX3S:** Requires the nMigen/Amaranth flow and nmigen-boards' ULX3S platform definition rather than plain Verilog/VHDL.

### Glasgow ECP5 PLL parameter solver (Amaranth) {#core-glasgow-ecp5-pll}

Amaranth-based EHXPLLL parameter solver derived from Project Trellis' PLL calculations, instantiating EHXPLLL plus an FD1S3AX loss-of-lock flop and reset-synchronizer flops; used by Glasgow revD which is itself an ECP5 25F board.

| | |
|---|---|
| Repository | [glasgowembedded__glasgow](https://github.com/GlasgowEmbedded/glasgow): Glasgow Interface Explorer: multi-protocol USB debug/reverse-engineering tool - Amaranth-generated gateware… |
| Files | [`software/glasgow/gateware/pll/ecp5.py`](https://github.com/GlasgowEmbedded/glasgow/blob/9b835612a323930c2e0641033fc95c2814a657b9/software/glasgow/gateware/pll/ecp5.py) |
| Top module | n/a |
| Language | Python (Amaranth) |
| License | 0BSD OR Apache-2.0 (LICENSE-0BSD.txt, LICENSE-Apache-2.0.txt) |
| FPGA / primitives | ECP5: `EHXPLLL`, `FD1S3AX` |
| Tests | software/glasgow/gateware/pll/bench.py (benchmark/consistency script, not a synthesis test) |

**On ULX3S:** Needs an Amaranth flow (not plain yosys/nextpnr from Verilog/VHDL sources); complements rather than replaces emard-ecp5pll for HDL-only designs.

### hdl4fpga ecp5_videodcm / ecp5_sdramdcm clock generators {#core-hdl4fpga-ecp5-clockgen}

Two purpose-built EHXPLLL wrappers (video pixel-clock and SDRAM clock) that all three ULX3S hdl4fpga apps instantiate from a single 25 MHz clk_25mhz input, confirmed against the real ulx3s_v20.lpf pin name.

| | |
|---|---|
| Repository | [hdl4fpga__hdl4fpga](https://github.com/hdl4fpga/hdl4fpga): hdl4fpga: portable VHDL library, ScopeIO oscilloscope, SDRAM graphics, eth/USB links |
| Files | [`library/apps/ecp5_videodcm.vhd`](https://github.com/hdl4fpga/hdl4fpga/blob/662986ba0f17b7ce3a066ddcb799d42fa1b24dea/library/apps/ecp5_videodcm.vhd), [`library/apps/ecp5_sdramdcm.vhd`](https://github.com/hdl4fpga/hdl4fpga/blob/662986ba0f17b7ce3a066ddcb799d42fa1b24dea/library/apps/ecp5_sdramdcm.vhd) |
| Top module | `ecp5_videodcm` |
| Language | VHDL |
| License | MIT (LICENSE) |
| FPGA / primitives | ECP5: `EHXPLLL` |
| Tests | none found |

**On ULX3S:** Ready-made for hdl4fpga-based designs; for a generic new design emard-ecp5pll is more self-contained (single generic module vs. two purpose-specific entities).

Full review: [hdl4fpga__hdl4fpga](../projects/hdl4fpga__hdl4fpga.md).
{% endraw %}
