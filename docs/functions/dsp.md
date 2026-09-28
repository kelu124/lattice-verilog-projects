---
title: "DSP"
parent: "Cores by function"
nav_order: 27
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# DSP

FFT, CIC/FIR filters, NCOs, CORDIC.

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [Waveform-generator DDS sine core (AXI-Stream, cocotb-tested)](#core-semify-wfg-stim-sine) ★ | [semify-eda__waveform-generator](https://github.com/semify-eda/waveform-generator) | SystemVerilog | Apache-2.0 | ECP5 | 0 |
| [256-point radix-2 FFT core](#core-mebner86-fft256) | [mebner86__icesugar-pro_sound2fft](https://github.com/mebner86/icesugar-pro_sound2fft) | Verilog | MIT (LICENSE, repo root) | ECP5 | 0 |
| [CIC decimator + FIR decimation filter](#core-emeb-cic-fir-decimator) | [emeb__orangecrab_adc](https://github.com/emeb/orangecrab_adc) | Verilog | none found | any | 0 |
| [CORDIC sin/cos core](#core-osresearch-cordic) | [osresearch__up5k](https://github.com/osresearch/up5k) | Verilog | none found | iCE40 UP5K | 5 |
| [NCO + CIC building blocks (mixer_pcb)](#core-jamesrosssharp-nco-cic) | [jamesrosssharp__ulx3s_mixer_pcb](https://github.com/jamesrosssharp/ulx3s_mixer_pcb) | Verilog | MIT (hdl/LICENSE.txt) | ECP5 | 0 |
| [DDS local oscillator](#core-nicocavallu-dds-lo) | [nicocavallu__rf-dds-lo](https://github.com/nicocavallu/rf-dds-lo) | Verilog | none found | any | 0 |
| [Digital down-converter + AM/FM demod chain (post-ADC)](#core-emeb-orangecrab-adc-ddc) | [emeb__orangecrab_adc](https://github.com/emeb/orangecrab_adc) | Verilog | none found | any | 0 |

## Cores

### Waveform-generator DDS sine core (AXI-Stream, cocotb-tested) (best) {#core-semify-wfg-stim-sine}

Parametric NCO/DDS sine generator with AXI-Stream output (angular increment, gain, offset registers), part of a modular Wishbone waveform-generator SoC built for ULX3S.

| | |
|---|---|
| Repository | [semify-eda__waveform-generator](https://github.com/semify-eda/waveform-generator): Generic SystemVerilog waveform generator core |
| Files | [`design/wfg_stim_sine/rtl/wfg_stim_sine.sv`](https://github.com/semify-eda/waveform-generator/blob/3afa6c9c8eb7268c48bfb7fba8a825d9a69643f2/design/wfg_stim_sine/rtl/wfg_stim_sine.sv), [`design/wfg_stim_sine/rtl/wfg_stim_sine_top.sv`](https://github.com/semify-eda/waveform-generator/blob/3afa6c9c8eb7268c48bfb7fba8a825d9a69643f2/design/wfg_stim_sine/rtl/wfg_stim_sine_top.sv), [`design/wfg_stim_sine/testbench/test_wfg_stim_sine.py`](https://github.com/semify-eda/waveform-generator/blob/3afa6c9c8eb7268c48bfb7fba8a825d9a69643f2/design/wfg_stim_sine/testbench/test_wfg_stim_sine.py) |
| Top module | `wfg_stim_sine` |
| Language | SystemVerilog |
| License | Apache-2.0 (SPDX header in-file, semify) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | cocotb (design/wfg_stim_sine/testbench/test_wfg_stim_sine.py + sim/Makefile) |

**On ULX3S:** fpga/ulx3s_soc/ and fpga/ulx3s_barebones/ are real ULX3S build targets in this repo; each wfg_* subcore (wfg_core, wfg_subcore, wfg_interconnect, wfg_drive_spi, wfg_stim_mem, wfg_drive_pat) has its own cocotb testbench under the same pattern.

### 256-point radix-2 FFT core {#core-mebner86-fft256}

256-point radix-2 decimation-in-time FFT, streams in 16-bit signed samples, computes 8 butterfly stages and outputs magnitude for spectrum display; uses ECP5 EBR-inferring dual-port RAM.

| | |
|---|---|
| Repository | [mebner86__icesugar-pro_sound2fft](https://github.com/mebner86/icesugar-pro_sound2fft): iCESugar-Pro sound2fft: real-time audio spectrum analyzer |
| Files | [`rtl/fft256.v`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/rtl/fft256.v), [`rtl/fft_real512.v`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/rtl/fft_real512.v) |
| Top module | `fft256` |
| Language | Verilog |
| License | MIT (LICENSE, repo root) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | cocotb, bit-exact vs numpy (per repo README, not individually re-run here) |

**On ULX3S:** Requires a generated twiddle.hex (gen_twiddle.py in repo); part of a cocotb bit-exact-tested pipeline built for iCESugar-Pro (ECP5 25F), directly portable to ULX3S.

### CIC decimator + FIR decimation filter {#core-emeb-cic-fir-decimator}

4-stage pipelined CIC decimator (parametric stage count/growth/word sizes) followed by an 8-tap parallel FIR decimation filter; classic SDR sample-rate-reduction front end.

| | |
|---|---|
| Repository | [emeb__orangecrab_adc](https://github.com/emeb/orangecrab_adc): OrangeCrab ADC FeatherWing: AD9203 10-bit/40MSPS ADC + audio board, gateware for SDR tuning/AM demodulation |
| Files | [`gateware/verilog/src/cic_dec_4.v`](https://github.com/emeb/orangecrab_adc/blob/daa94e19abb11e3cee3bc1e97d87908b6da1e08a/gateware/verilog/src/cic_dec_4.v), [`gateware/verilog/src/fir8dec_par.v`](https://github.com/emeb/orangecrab_adc/blob/daa94e19abb11e3cee3bc1e97d87908b6da1e08a/gateware/verilog/src/fir8dec_par.v) |
| Top module | `cic_dec_4` |
| Language | Verilog |
| License | none found (no LICENSE file in repo) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Plain parametric Verilog, no vendor primitives seen; combine with an NCO/mixer from this collection for a full DDC.

### CORDIC sin/cos core {#core-osresearch-cordic}

Parametric CORDIC rotator producing sin/cos outputs; plain Verilog with no SB_* primitives.

| | |
|---|---|
| Repository | [osresearch__up5k](https://github.com/osresearch/up5k): UPduino v2: standalone iCE40 UltraPlus5K Verilog demos - blink, RGB pulse, UART serial/echo, SPRAM buffered… |
| Files | [`cordic.v`](https://github.com/osresearch/up5k/blob/2eef12a9659b8fc4ebf68656198b8840f6da2e0d/cordic.v) |
| Top module | `cordic` |
| Language | Verilog |
| License | none found (no LICENSE/COPYING file; README states none) |
| FPGA / primitives | iCE40 UP5K: none (portable) |
| Tests | none found |

**On ULX3S:** Standalone module, portable to ECP5 as-is; only the surrounding up5k board top-levels are iCE40-specific.

**Used by 5 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [badgeteam__mch2022-firmware-ice40](https://github.com/badgeteam/mch2022-firmware-ice40) (copies [`projects/Forth/rtl/common-verilog/cordic.v`](https://github.com/badgeteam/mch2022-firmware-ice40/blob/ce6473addcf6066cada7d80d8ba352f52173d01d/projects/Forth/rtl/common-verilog/cordic.v))
- [bornabiro__fpga_epaper](https://github.com/BornaBiro/FPGA_epaper) (instantiates [`epaper/_math_real.vhd`](https://github.com/BornaBiro/FPGA_epaper/blob/418985772b72d3113c8cac538c2334e60182e43a/epaper/_math_real.vhd))
- [marinsiric__ulx3s](https://github.com/marinsiric/ulx3s) (instantiates [`Diamond/passthru/ulx3s-v2.0-12f/._Real_._Math_.vhd`](https://github.com/marinsiric/ulx3s/blob/b807c99376c149c074b8c8bd51ee56eb95b3fcc9/Diamond/passthru/ulx3s-v2.0-12f/._Real_._Math_.vhd))
- [tarik-hamedovic__sdr-hls](https://github.com/tarik-hamedovic/SDR-HLS) (instantiates [`1.RTLImplementation/4.lattice/Version0-modified/sim/_math_real.vhd`](https://github.com/tarik-hamedovic/SDR-HLS/blob/334f7074eb51dc7d4910a439ba62c85c2668e706/1.RTLImplementation/4.lattice/Version0-modified/sim/_math_real.vhd))
- [tvelliott__dsp_ice](https://github.com/tvelliott/dsp_ice) (instantiates [`firmware/fpga/src/fpga_top.v`](https://github.com/tvelliott/dsp_ice/blob/3da0ddfb66823c326711484ff188eb53da962f46/firmware/fpga/src/fpga_top.v))

### NCO + CIC building blocks (mixer_pcb) {#core-jamesrosssharp-nco-cic}

Numerically-controlled oscillator (sin/cos outputs) and CIC decimators used as generic DSP building blocks in the ULX3S mixer-PCB SDR chain.

| | |
|---|---|
| Repository | [jamesrosssharp__ulx3s_mixer_pcb](https://github.com/jamesrosssharp/ulx3s_mixer_pcb): 100MHz PLL + RF mixer/demodulator PMOD board, with matching ULX3S SDR receiver HDL |
| Files | [`hdl/src/nco.v`](https://github.com/jamesrosssharp/ulx3s_mixer_pcb/blob/ec6d9fc0a8a5f6a189793a2a2638159c5705db75/hdl/src/nco.v), [`hdl/src/cic.v`](https://github.com/jamesrosssharp/ulx3s_mixer_pcb/blob/ec6d9fc0a8a5f6a189793a2a2638159c5705db75/hdl/src/cic.v), [`hdl/src/aud_cic.v`](https://github.com/jamesrosssharp/ulx3s_mixer_pcb/blob/ec6d9fc0a8a5f6a189793a2a2638159c5705db75/hdl/src/aud_cic.v), [`hdl/src/mult.v`](https://github.com/jamesrosssharp/ulx3s_mixer_pcb/blob/ec6d9fc0a8a5f6a189793a2a2638159c5705db75/hdl/src/mult.v) |
| Top module | `nco` |
| Language | Verilog |
| License | MIT (hdl/LICENSE.txt) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | per-block testbenches under hdl/test/ (waveform-dump only, no assertions) |

**On ULX3S:** Each block has a standalone testbench (hdl/test/001_NCO/tb.v etc., waveform-dump only); reusable independently of the radio-specific demod blocks.

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

Catalogued repos tagged `dsp` (1), `dsp-sdr` (21) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
