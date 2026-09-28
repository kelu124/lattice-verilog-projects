---
title: "Radio (FM/RDS, SDR)"
parent: "Cores by function"
nav_order: 27
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# Radio (FM/RDS, SDR)

FM/RDS transmitters, SDR receive chains, radio front ends.

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [1-bit AM transceiver chain (ULX3S-proven)](#core-jamesrosssharp-1bit-am) ★ | [jamesrosssharp__1_bit_am](https://github.com/jamesrosssharp/1_bit_AM) | Verilog | MIT (LICENSE.txt) | ECP5 | 1 |
| [DDS local oscillator](#core-nicocavallu-dds-lo) | [nicocavallu__rf-dds-lo](https://github.com/nicocavallu/rf-dds-lo) | Verilog | none found | any | 0 |
| [FM stereo transmitter with RDS](#core-emard-fm-rds) | [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc) | VHDL | BSD (`-- (c) Marko Zec` / `-- LICENSE=BSD` on… | any | 2 |
| [Standalone RDS DBPSK modulator](#core-emard-rdsfpga-rds) | [emard__rdsfpga](https://github.com/emard/rdsfpga) | VHDL | BSD in headers | any | 0 |
| [Superheterodyne AM/FM receive chain with per-block testbenches](#core-jamesrosssharp-mixer-pcb-superhet) | [jamesrosssharp__ulx3s_mixer_pcb](https://github.com/jamesrosssharp/ulx3s_mixer_pcb) | Verilog | MIT (hdl/LICENSE.txt) | ECP5 | 1 |
| [Digital down-converter + AM/FM demod chain (post-ADC)](#core-emeb-orangecrab-adc-ddc) | [emeb__orangecrab_adc](https://github.com/emeb/orangecrab_adc) | Verilog | none found | any | 0 |

## Cores

### 1-bit AM transceiver chain (ULX3S-proven) (best) {#core-jamesrosssharp-1bit-am}

Complete 1-bit AM transmit+receive chain (NCO, mixer, AM generator/demodulator, CIC decimation) with a real ULX3S top-level and LPF, taking RF in/out on GPIO pins and I2S audio out.

| | |
|---|---|
| Repository | [jamesrosssharp__1_bit_am](https://github.com/jamesrosssharp/1_bit_AM): jamesrosssharp/1_bit_AM: 1-bit oversampling-ADC AM radio transceiver experiment, targets ULX3S |
| Files | [`src/am_gen.v`](https://github.com/jamesrosssharp/1_bit_AM/blob/ce7e9fcc70fd98d23083b7ae7ae43111528c0e87/src/am_gen.v), [`src/am_demod.v`](https://github.com/jamesrosssharp/1_bit_AM/blob/ce7e9fcc70fd98d23083b7ae7ae43111528c0e87/src/am_demod.v), [`src/mixer.v`](https://github.com/jamesrosssharp/1_bit_AM/blob/ce7e9fcc70fd98d23083b7ae7ae43111528c0e87/src/mixer.v), [`src/nco.v`](https://github.com/jamesrosssharp/1_bit_AM/blob/ce7e9fcc70fd98d23083b7ae7ae43111528c0e87/src/nco.v), [`src/cic.v`](https://github.com/jamesrosssharp/1_bit_AM/blob/ce7e9fcc70fd98d23083b7ae7ae43111528c0e87/src/cic.v), [`impl/ulx3s/top.v`](https://github.com/jamesrosssharp/1_bit_AM/blob/ce7e9fcc70fd98d23083b7ae7ae43111528c0e87/impl/ulx3s/top.v), [`impl/ulx3s/ulx3s_v316.lpf`](https://github.com/jamesrosssharp/1_bit_AM/blob/ce7e9fcc70fd98d23083b7ae7ae43111528c0e87/impl/ulx3s/ulx3s_v316.lpf) |
| Top module | `top` |
| Language | Verilog |
| License | MIT (LICENSE.txt) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | none found (no tb/ directory found in this pass) |

**On ULX3S:** impl/ulx3s/top.v is a direct ULX3S build target (gp9 RF in, gp8 RF out, gp1-4 I2S); impl/ulx3s/Makefile builds it as-is.

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [jamesrosssharp__ulx3s_mixer_pcb](https://github.com/jamesrosssharp/ulx3s_mixer_pcb) (instantiates [`hdl/impl/ulx3s/top.v`](https://github.com/jamesrosssharp/ulx3s_mixer_pcb/blob/ec6d9fc0a8a5f6a189793a2a2638159c5705db75/hdl/impl/ulx3s/top.v))

### DDS local oscillator {#core-nicocavallu-dds-lo}

Generic phase-accumulator DDS core with a sine lookup table, intended as a local-oscillator source for an RF mixer front-end.

| | |
|---|---|
| Repository | [nicocavallu__rf-dds-lo](https://github.com/nicocavallu/rf-dds-lo): Direct Digital Synthesizer |
| Files | [`src/dds_top.v`](https://github.com/nicocavallu/rf-dds-lo/blob/e19c0ee4c40745aa5cae0fa349109d1ed5866e90/src/dds_top.v), [`src/phase_accumulator.v`](https://github.com/nicocavallu/rf-dds-lo/blob/e19c0ee4c40745aa5cae0fa349109d1ed5866e90/src/phase_accumulator.v), [`src/sine_lut.v`](https://github.com/nicocavallu/rf-dds-lo/blob/e19c0ee4c40745aa5cae0fa349109d1ed5866e90/src/sine_lut.v) |
| Top module | `dds_top` |
| Language | Verilog |
| License | none found (no LICENSE file) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Board-independent; repo ships a ulx3s.lpf but no explicit nextpnr device size was found.

### FM stereo transmitter with RDS {#core-emard-fm-rds}

Stereo FM transmitter with RDS (DBPSK) subcarrier generation, FIR/lowpass filters and RDS message RAM; demonstrated in the ULX3S fm example.

| | |
|---|---|
| Repository | [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc): ULX3S misc/advanced examples: EMARD's building-block library |
| Files | [`examples/fm/hdl/fm.vhd`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/fm/hdl/fm.vhd), [`examples/fm/hdl/fmgen.vhd`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/fm/hdl/fmgen.vhd), [`examples/fm/hdl/rds.vhd`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/fm/hdl/rds.vhd), [`examples/fm/hdl/fir.vhd`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/fm/hdl/fir.vhd), [`examples/fm/hdl/lowpass.vhd`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/fm/hdl/lowpass.vhd), [`examples/fm/hdl/bram_rds.vhd`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/fm/hdl/bram_rds.vhd), [`examples/fm/hdl/message_ps.vhd`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/fm/hdl/message_ps.vhd), [`examples/fm/hdl/message_ps_rt.vhd`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/fm/hdl/message_ps_rt.vhd) |
| Top module | `fm` |
| Language | VHDL |
| License | BSD (`-- (c) Marko Zec` / `-- LICENSE=BSD` on fmgen.vhd; other files in the set not individually re-checked) |
| FPGA / primitives | any: none (portable) |
| Tests | hdl/test/fmgen_test.vhd (VHDL testbench, waveform-only; not individually re-run here) |

**On ULX3S:** examples/fm/top/top_fm.v is the ULX3S-ready top; has its own hdl/test/fmgen_test.vhd (VHDL testbench, waveform-only per repo convention).

Full review: [emard__ulx3s-misc](../projects/emard__ulx3s-misc.md).

**Used by 2 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [emard__rdsfpga](https://github.com/emard/rdsfpga) (instantiates [`main.v`](https://github.com/emard/rdsfpga/blob/12a8b817f2bc8cabfb3d7d3cc4fb0ab1a95cfedf/main.v))
- [f32c__f32c](https://github.com/f32c/f32c) (instantiates [`rtl/soc/fm/fm.vhd`](https://github.com/f32c/f32c/blob/7dbf56d42a94ae599eabfd1e7fa15db14a10afd7/rtl/soc/fm/fm.vhd))

### Standalone RDS DBPSK modulator {#core-emard-rdsfpga-rds}

RDS modulator with DBPSK (by Davor Jadrijevic), circulates a memory address to fetch 8-bit RDS data words, MSB first.

| | |
|---|---|
| Repository | [emard__rdsfpga](https://github.com/emard/rdsfpga): RDS FM transmitter |
| Files | [`rds.vhd`](https://github.com/emard/rdsfpga/blob/12a8b817f2bc8cabfb3d7d3cc4fb0ab1a95cfedf/rds.vhd), [`fmgen.vhd`](https://github.com/emard/rdsfpga/blob/12a8b817f2bc8cabfb3d7d3cc4fb0ab1a95cfedf/fmgen.vhd) |
| Top module | `rds` |
| Language | VHDL |
| License | BSD in headers (`-- LICENSE=BSD`; no repo-level LICENSE file) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Per project memory this repo's board target is ULX2S-only; the rds.vhd/fmgen.vhd modules themselves are board-independent and match the ones bundled in ulx3s-misc's fm/ example.

### Superheterodyne AM/FM receive chain with per-block testbenches {#core-jamesrosssharp-mixer-pcb-superhet}

Mixer, AM/FM demodulators, 19kHz pilot bandpass filter and DPLL for a superheterodyne receiver, built against an external RF mixer add-on PCB on the ULX3S.

| | |
|---|---|
| Repository | [jamesrosssharp__ulx3s_mixer_pcb](https://github.com/jamesrosssharp/ulx3s_mixer_pcb): 100MHz PLL + RF mixer/demodulator PMOD board, with matching ULX3S SDR receiver HDL |
| Files | [`hdl/src/mixer.v`](https://github.com/jamesrosssharp/ulx3s_mixer_pcb/blob/ec6d9fc0a8a5f6a189793a2a2638159c5705db75/hdl/src/mixer.v), [`hdl/src/am_demod.v`](https://github.com/jamesrosssharp/ulx3s_mixer_pcb/blob/ec6d9fc0a8a5f6a189793a2a2638159c5705db75/hdl/src/am_demod.v), [`hdl/src/fm_demod.v`](https://github.com/jamesrosssharp/ulx3s_mixer_pcb/blob/ec6d9fc0a8a5f6a189793a2a2638159c5705db75/hdl/src/fm_demod.v), [`hdl/src/dpll.v`](https://github.com/jamesrosssharp/ulx3s_mixer_pcb/blob/ec6d9fc0a8a5f6a189793a2a2638159c5705db75/hdl/src/dpll.v), [`hdl/src/bandpass_19khz.v`](https://github.com/jamesrosssharp/ulx3s_mixer_pcb/blob/ec6d9fc0a8a5f6a189793a2a2638159c5705db75/hdl/src/bandpass_19khz.v), [`hdl/src/cic.v`](https://github.com/jamesrosssharp/ulx3s_mixer_pcb/blob/ec6d9fc0a8a5f6a189793a2a2638159c5705db75/hdl/src/cic.v), [`hdl/src/aud_cic.v`](https://github.com/jamesrosssharp/ulx3s_mixer_pcb/blob/ec6d9fc0a8a5f6a189793a2a2638159c5705db75/hdl/src/aud_cic.v), [`hdl/src/nco.v`](https://github.com/jamesrosssharp/ulx3s_mixer_pcb/blob/ec6d9fc0a8a5f6a189793a2a2638159c5705db75/hdl/src/nco.v), [`hdl/impl/ulx3s/top.v`](https://github.com/jamesrosssharp/ulx3s_mixer_pcb/blob/ec6d9fc0a8a5f6a189793a2a2638159c5705db75/hdl/impl/ulx3s/top.v) |
| Top module | `top` |
| Language | Verilog |
| License | MIT (hdl/LICENSE.txt) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | per-block testbenches under hdl/test/ (e.g. 001_NCO/tb.v, 008_DPLL/tb.v); waveform-dump only (`$dumpvars`/VCD), no self-checking assertions seen |

**On ULX3S:** hdl/impl/ulx3s/top.v is a real ULX3S target; each DSP block has its own testbench under hdl/test/<NNN_NAME>/tb.v.

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [jamesrosssharp__1_bit_am](https://github.com/jamesrosssharp/1_bit_AM) (instantiates [`impl/ulx3s/top.v`](https://github.com/jamesrosssharp/1_bit_AM/blob/ce7e9fcc70fd98d23083b7ae7ae43111528c0e87/impl/ulx3s/top.v))

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

## Other catalogued projects

Catalogued repos tagged `radio-tx` (3), `radio-rx` (6), `fm-transmitter` (1), `dsp-sdr` (21) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
