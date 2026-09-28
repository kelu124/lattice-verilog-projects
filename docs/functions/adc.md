---
title: "ADC"
parent: "Cores by function"
nav_order: 23
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# ADC

ADC interfaces (onboard MAX11125 and external ADCs).

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [MAX1112x ADC reader (ulx3s-misc)](#core-emard-max1112x-adc) ★ | [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc) | VHDL | BSD (`-- AUTHOR=EMARD` / `-- LICENSE=BSD` header) | any | 1 |
| [Digital down-converter + AM/FM demod chain (post-ADC)](#core-emeb-orangecrab-adc-ddc) | [emeb__orangecrab_adc](https://github.com/emeb/orangecrab_adc) | Verilog | none found | any | 0 |
| [MAX1112x ADC reader (ulx3s-emi copy)](#core-emard-max1112x-emi) | [emard__ulx3s-emi](https://github.com/emard/ulx3s-emi) | VHDL | BSD (`-- AUTHOR=EMARD` / `-- LICENSE=BSD` header) | any | 1 |
| [SPI ADC core (Bus Pirate Ultra HDL)](#core-buspirate-adc) | [dangerousprototypes__buspirateultrahdl](https://github.com/DangerousPrototypes/BusPirateUltraHDL) | Verilog | GPL-3.0 (repo LICENSE) | iCE40 HX8K | 0 |

## Cores

### MAX1112x ADC reader (ulx3s-misc) (best) {#core-emard-max1112x-adc}

Init+read core for the onboard MAX1112x (MAX11125-family) SPI ADC used on the ULX3S; shift and array register variants.

| | |
|---|---|
| Repository | [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc): ULX3S misc/advanced examples: EMARD's building-block library |
| Files | [`examples/adc/max1112x/hdl/max1112x_reader_shift.vhd`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/adc/max1112x/hdl/max1112x_reader_shift.vhd), [`examples/adc/max1112x/hdl/max1112x_reader_array.vhd`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/adc/max1112x/hdl/max1112x_reader_array.vhd), [`examples/adc/max1112x/hdl/max1112x_init_pack.vhd`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/adc/max1112x/hdl/max1112x_init_pack.vhd) |
| Top module | `max1112x_reader_shift` |
| Language | VHDL |
| License | BSD (`-- AUTHOR=EMARD` / `-- LICENSE=BSD` header) |
| FPGA / primitives | any: none (portable) |
| Tests | none found (repo-wide: only examples/audio/testbench/sinewave.c is a non-HDL C reference model) |

**On ULX3S:** Drop-in for the ULX3S onboard MAX11125 ADC pins; verified in docs/projects/emard__ulx3s-misc.md.

Full review: [emard__ulx3s-misc](../projects/emard__ulx3s-misc.md).

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [emard__ulx3s-emi](https://github.com/emard/ulx3s-emi) (copies [`hdl/max1112x_init_pack.vhd`](https://github.com/emard/ulx3s-emi/blob/8c93799e664c3d6ea5f7cbd427667c382f40927c/hdl/max1112x_init_pack.vhd))

### Digital down-converter + AM/FM demod chain (post-ADC) {#core-emeb-orangecrab-adc-ddc}

Digital down-converter, tuner NCO, AM/FM demodulators plus CIC decimator and FIR filter, fed from an external fast ADC on OrangeCrab 25F; no vendor primitives seen.

| | |
|---|---|
| Repository | [emeb__orangecrab_adc](https://github.com/emeb/orangecrab_adc): OrangeCrab ADC FeatherWing: AD9203 10-bit/40MSPS ADC + audio board, gateware for SDR tuning/AM demodulation |
| Files | [`gateware/verilog/src/ddc_14.v`](https://github.com/emeb/orangecrab_adc/blob/daa94e19abb11e3cee3bc1e97d87908b6da1e08a/gateware/verilog/src/ddc_14.v), [`gateware/verilog/src/demods.v`](https://github.com/emeb/orangecrab_adc/blob/daa94e19abb11e3cee3bc1e97d87908b6da1e08a/gateware/verilog/src/demods.v), [`gateware/verilog/src/tuner_2.v`](https://github.com/emeb/orangecrab_adc/blob/daa94e19abb11e3cee3bc1e97d87908b6da1e08a/gateware/verilog/src/tuner_2.v), [`gateware/verilog/src/cic_dec_4.v`](https://github.com/emeb/orangecrab_adc/blob/daa94e19abb11e3cee3bc1e97d87908b6da1e08a/gateware/verilog/src/cic_dec_4.v), [`gateware/verilog/src/fir8dec_par.v`](https://github.com/emeb/orangecrab_adc/blob/daa94e19abb11e3cee3bc1e97d87908b6da1e08a/gateware/verilog/src/fir8dec_par.v) |
| Top module | `ddc_14` |
| Language | Verilog |
| License | none found (no LICENSE file in repo) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Needs an external high-speed ADC on ULX3S (no onboard equivalent); the DSP chain itself (CIC/FIR/demod) is portable.

### MAX1112x ADC reader (ulx3s-emi copy) {#core-emard-max1112x-emi}

Same EMARD MAX1112x ADC init/read core vendored into the ulx3s-emi (12F) example board design.

| | |
|---|---|
| Repository | [emard__ulx3s-emi](https://github.com/emard/ulx3s-emi): emard/ulx3s-emi: ULX3S electromagnetic-interference |
| Files | [`hdl/max1112x_reader_array.vhd`](https://github.com/emard/ulx3s-emi/blob/8c93799e664c3d6ea5f7cbd427667c382f40927c/hdl/max1112x_reader_array.vhd), [`hdl/max1112x_init_pack.vhd`](https://github.com/emard/ulx3s-emi/blob/8c93799e664c3d6ea5f7cbd427667c382f40927c/hdl/max1112x_init_pack.vhd) |
| Top module | `max1112x_reader_array` |
| Language | VHDL |
| License | BSD (`-- AUTHOR=EMARD` / `-- LICENSE=BSD` header) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Same core as ulx3s-misc; use if you want the ulx3s-emi top-level wiring as a starting point.

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc) (copies [`examples/adc/max1112x/hdl/max1112x_init_pack.vhd`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/adc/max1112x/hdl/max1112x_init_pack.vhd))

### SPI ADC core (Bus Pirate Ultra HDL) {#core-buspirate-adc}

Standalone 14-bit SPI ADC read/calibration core for the Bus Pirate Ultra's onboard ADC channel.

| | |
|---|---|
| Repository | [dangerousprototypes__buspirateultrahdl](https://github.com/DangerousPrototypes/BusPirateUltraHDL): BusPirateUltraHDL: Bus Pirate Ultra FPGA gateware - SPI/UART/PWM/ADC engines + MCU parallel interface for the… |
| Files | [`hdl/adc.v`](https://github.com/DangerousPrototypes/BusPirateUltraHDL/blob/bb0d7cae74f799f710b8b0ff246a5080a96c9365/hdl/adc.v) |
| Top module | `adc` |
| Language | Verilog |
| License | GPL-3.0 (repo LICENSE) |
| FPGA / primitives | iCE40 HX8K: none (portable) |
| Tests | none found |

**On ULX3S:** adc.v itself is plain Verilog (no SB_* seen); the board's pll.v/buspirate.v use iCE40 SB_PLL40_CORE/SB_IO and would need ECP5 equivalents if reused wholesale.

## Other catalogued projects

Catalogued repos tagged `adc` (23) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
