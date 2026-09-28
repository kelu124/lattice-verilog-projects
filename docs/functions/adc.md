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
| [AD9629 12-bit parallel ADC capture (adc_receiver)](#core-lit3rick-ad9629-adc-receiver) | [kelu124__lit3rick](https://github.com/kelu124/lit3rick) | Verilog | GPL-3.0-or-later | any | 0 |
| [Digital down-converter + AM/FM demod chain (post-ADC)](#core-emeb-orangecrab-adc-ddc) | [emeb__orangecrab_adc](https://github.com/emeb/orangecrab_adc) | Verilog | none found | any | 3 |
| [MAX1112x ADC reader (ulx3s-emi copy)](#core-emard-max1112x-emi) | [emard__ulx3s-emi](https://github.com/emard/ulx3s-emi) | VHDL | BSD (`-- AUTHOR=EMARD` / `-- LICENSE=BSD` header) | any | 1 |
| [SPI ADC core (Bus Pirate Ultra HDL)](#core-buspirate-adc) | [dangerousprototypes__buspirateultrahdl](https://github.com/DangerousPrototypes/BusPirateUltraHDL) | Verilog | GPL-3.0 (repo LICENSE) | iCE40 HX8K | 0 |
| [InductIQ lock-in mixer + BRAM-LUT NCO](#core-makisness-inductiq-lockin) | [makisness__inductiq](https://github.com/Makisness/InductIQ) | SystemVerilog, Verilog | MIT (LICENSE) | any | 0 |

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

### AD9629 12-bit parallel ADC capture (adc_receiver) {#core-lit3rick-ad9629-adc-receiver}

Captures a fixed 8192-sample burst from a 12-bit parallel ADC (AD9629BCPZ-65, up to 65 Msps) on a start pulse, subtracts the ADC's 2048 mid-scale DC offset, and emits sample_num/DOUT_vld plus a finish flag for a downstream RAM writer.

| | |
|---|---|
| Repository | [kelu124__lit3rick](https://github.com/kelu124/lit3rick): lit3rick: single-channel ultrasound pulse-echo board - UP5K ADC/pulser, on-chip DFT envelope extraction,… |
| Files | [`verilog/src/rtl/adc_receiver.v`](https://github.com/kelu124/lit3rick/blob/ca4ad983046943fae0694a609154839e8c051283/verilog/src/rtl/adc_receiver.v) |
| Top module | `adc_receiver` |
| Language | Verilog |
| License | GPL-3.0-or-later (repo Readme.md ## License; no per-file SPDX header) |
| FPGA / primitives | any: none (portable) |
| Tests | exercised (not unit-tested standalone) by verilog/src/tb/tb_top.sv test_adc task through a behavioural AD9629 model, verilog/src/tb/ad9629.sv |

**On ULX3S:** No vendor primitives; a plain free-running counter and register pipeline, easily retargeted to any parallel ADC by changing the ADC_D width and the 2048 offset constant.

Full review: [kelu124__lit3rick](../projects/kelu124__lit3rick.md).

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

**Used by 3 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [emeb__iceradio](https://github.com/emeb/iceRadio) (copies [`FPGA/rxadc_2/verilog/src/tuner_2.v`](https://github.com/emeb/iceRadio/blob/632f8c14400ebfe5f82beb154f6df6d3e4bafd4e/FPGA/rxadc_2/verilog/src/tuner_2.v))
- [emeb__orangecrab-litex-adc](https://github.com/emeb/OrangeCrab-Litex-ADC) (copies [`hw/vsrc/cic_dec_4.v`](https://github.com/emeb/OrangeCrab-Litex-ADC/blob/6f3d6192d602dcf89b06d04617b87bc1e25ffa54/hw/vsrc/cic_dec_4.v))
- [emeb__rpi_rxadc](https://github.com/emeb/rpi_rxadc) (instantiates [`gateware/icehat_rxadc/icestorm/icehat_rxadc.v`](https://github.com/emeb/rpi_rxadc/blob/a44b5557ae7f6590998597ddaf960a34f29528e3/gateware/icehat_rxadc/icestorm/icehat_rxadc.v))

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

### InductIQ lock-in mixer + BRAM-LUT NCO {#core-makisness-inductiq-lockin}

Digital lock-in amplifier: multiplies a 12-bit ADC sample by 16-bit sine/cosine references from a BRAM quarter-wave-LUT NCO (32-bit phase accumulator), then accumulates I/Q over up to 2^15 samples in 48-bit accumulators for synchronous detection. No vendor primitives.

| | |
|---|---|
| Repository | [makisness__inductiq](https://github.com/Makisness/InductIQ): InductIQ: FPGA lock-in amplifier + impedance sweep instrument for eddy-current coil sensing |
| Files | [`hdl/rtl/lia/lia_core.sv`](https://github.com/Makisness/InductIQ/blob/347e4bebb2116c475fa541c2417ce16fa4b5f39d/hdl/rtl/lia/lia_core.sv), [`hdl/rtl/dds/configurable_nco.v`](https://github.com/Makisness/InductIQ/blob/347e4bebb2116c475fa541c2417ce16fa4b5f39d/hdl/rtl/dds/configurable_nco.v), [`hdl/rtl/dds/quarter_sine_lut_Q1_15.mem`](https://github.com/Makisness/InductIQ/blob/347e4bebb2116c475fa541c2417ce16fa4b5f39d/hdl/rtl/dds/quarter_sine_lut_Q1_15.mem) |
| Top module | `lia_core` |
| Language | SystemVerilog, Verilog |
| License | MIT (LICENSE) |
| FPGA / primitives | any: none (portable) |
| Tests | hdl/tb/top_tb.sv + hdl/tb/adc_model.sv present in the clone; no Makefile/runner found so self-checking could not be confirmed |

**On ULX3S:** Proven on ULX3S 85F via apio (board=ulx3s-85f); drop-in with any signed ADC sample stream and matching sine/cosine reference width. Fills a gap noted in reusable-cores.md: no lock-in amplifier core existed in the collection before this.

## Other catalogued projects

Catalogued repos tagged `adc` (37) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
