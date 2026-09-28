---
title: "DSP"
parent: "Cores by function"
nav_order: 28
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# DSP

FFT, CIC/FIR filters, NCOs, CORDIC.

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [Waveform-generator DDS sine core (AXI-Stream, cocotb-tested)](#core-semify-wfg-stim-sine) ★ | [semify-eda__waveform-generator](https://github.com/semify-eda/waveform-generator) | SystemVerilog | Apache-2.0 | ECP5 | 0 |
| [2048-point block-floating-point FFT + Welch PSD feature extractor](#core-ox-computing-fft-bfp-2048) | [ox-computing__real-time-analytics-fpga](https://github.com/ox-computing/Real-Time-Analytics-FPGA) | SystemVerilog | Apache-2.0 | ECP5 | 0 |
| [256-point radix-2 FFT core](#core-mebner86-fft256) | [mebner86__icesugar-pro_sound2fft](https://github.com/mebner86/icesugar-pro_sound2fft) | Verilog | MIT (LICENSE, repo root) | ECP5 | 1 |
| [512-point dblclockfft-generated FFT (longwave SDR)](#core-mbsat-dblclockfft-512) | [mb-sat__ulx3s-longwave-sdr](https://github.com/mb-sat/ulx3s-longwave-sdr) | Verilog | LGPL-3.0 | ECP5 | 0 |
| [512-point SDF FFT core (E155 Tuner Project)](#core-dylansebastianheredia-fft512) | [dylansebastianheredia__e155_tuner_project](https://github.com/DylanSebastianHeredia/E155_Tuner_Project) | SystemVerilog | none found | iCE40 UP5K (unverified device, README only) | 0 |
| [64-point iterative radix-2 FFT/IFFT (OFDM PHY)](#core-meharbaan2-ofdm-fft64) | [meharbaan2__systemverilog-ofdm-phy-core](https://github.com/meharbaan2/systemverilog-ofdm-phy-core) | SystemVerilog | none found | iCE40 UP5K (unverified board bring-up) | 0 |
| [8-band parallel Goertzel spectrum analyzer](#core-hariharan6307-goertzel-spectrum) | [hariharan6307-coder__verilog-goertzel-audio-visualizer](https://github.com/Hariharan6307-coder/verilog-goertzel-audio-visualizer) | Verilog | none found | any | 1 |
| [alhusseingamal/r2sdf-fft radix-2 DIF SDF streaming FFT](#core-alhusseingamal-r2sdf-fft) | [alhusseingamal__r2sdf-fft](https://github.com/alhusseingamal/r2sdf-fft) | Verilog | none found | any | 0 |
| [Amaranth radix-2 fixed-point FFT (FFT/Butterfly/TwiddleFactors)](#core-amalthea-fft) | [greatscottgadgets__amalthea](https://github.com/greatscottgadgets/amalthea) | Python (Amaranth) | BSD-3-Clause | any | 16 |
| [CIC decimator + FIR decimation filter](#core-emeb-cic-fir-decimator) | [emeb__orangecrab_adc](https://github.com/emeb/orangecrab_adc) | Verilog | none found | any | 2 |
| [CORDIC sin/cos core](#core-osresearch-cordic) | [osresearch__up5k](https://github.com/osresearch/up5k) | Verilog | none found | iCE40 UP5K | 12 |
| [CORDIC-1 bit-serial CORDIC/DDS sine engine](#core-joaln27-cordic) | [joaln27__cordic](https://github.com/joaln27/CORDIC) | SystemVerilog | Apache-2.0 | ECP5 | 11 |
| [dblclockfft pipelined FFT/IFFT generator (C++ -> Verilog)](#core-zipcpu-dblclockfft-generator) | [zipcpu__dblclockfft](https://github.com/ZipCPU/dblclockfft) | C++ (generator), Verilog (generated… | none found | any | 1 |
| [fir_filt pipelined FIR/RBW decimation filter (VNA_FPGA_DSP)](#core-mysteriouswolf-fir-rbw) | [mysteriouswolf__vna_fpga_dsp](https://github.com/MysteriousWolf/VNA_FPGA_DSP) | Verilog | none found | any | 0 |
| [fulig/TinyFPGA_FFT single-butterfly-stage FFT](#core-fulig-fft-single-stage) | [fulig__tinyfpga_fft](https://github.com/fulig/TinyFPGA_FFT) | Verilog | none found | any | 0 |
| [Gage1999/fpga-sdr-receiver 256-pt iterative radix-2 FFT](#core-gage1999-fft256-iterative) | [gage1999__fpga-sdr-receiver](https://github.com/Gage1999/fpga-sdr-receiver) | SystemVerilog | MIT (LICENSE) | any | 1 |
| [HackRF Amaranth CIC/FIR/NCO/mixer DSP chain](#core-hackrf-amaranth-dsp-chain) | [greatscottgadgets__hackrf](https://github.com/greatscottgadgets/hackrf) | Python (Amaranth) | BSD-3-Clause | iCE40 | 0 |
| [InductIQ lock-in mixer + BRAM-LUT NCO](#core-makisness-inductiq-lockin) | [makisness__inductiq](https://github.com/Makisness/InductIQ) | SystemVerilog, Verilog | MIT (LICENSE) | any | 0 |
| [ipmgroup/fftd 1024-pt radix-2 DIT FFT core](#core-ipmgroup-fft1024-radix2) | [ipmgroup__fftd](https://github.com/ipmgroup/fftd) | Verilog | MIT (LICENSE) | any | 1 |
| [LiteDSP radix-2 SDF FFT/IFFT (Migen/LiteX)](#core-litedsp-fft-sdf) | [enjoy-digital__litedsp](https://github.com/enjoy-digital/litedsp) | Python (Migen/LiteX) | BSD-2-Clause | any | 1 |
| [Lock-in amplifier DSP chain (DDS + mixer + CIC/IIR + CORDIC)](#core-nkrackow-lockin-dsp-chain) | [nkrackow__singularitysurfer-fpga-lock-in-amplifier](https://github.com/nkrackow/SingularitySurfer-FPGA-Lock-In-Amplifier) | Verilog (+ Python RIIR_migen.py… | MIT (LICENSE) | iCE40 UP5K | 0 |
| [MAC units for exotic number formats (int8/bf16/fp16/posit8/mxfp8/lns8)](#core-uttamcoomar-mac-int8) | [uttamcoomar__mac-units-for-various-number-formats](https://github.com/uttamcoomar/MAC-units-for-various-number-formats) | Verilog, Python | none found | ECP5 | 0 |
| [mattvenn/fpga-sdft sliding DFT core](#core-mattvenn-sliding-dft) | [mattvenn__fpga-sdft](https://github.com/mattvenn/fpga-sdft) | Verilog | none found | any | 1 |
| [MaxZischka1/FastFourierTransformProject 16-pt radix-2 SDF FFT](#core-maxzischka1-sdf16-fft) | [maxzischka1__fastfouriertransformproject](https://github.com/MaxZischka1/FastFourierTransformProject) | SystemVerilog | none found | iCE40 | 0 |
| [NCO + CIC building blocks (mixer_pcb)](#core-jamesrosssharp-nco-cic) | [jamesrosssharp__ulx3s_mixer_pcb](https://github.com/jamesrosssharp/ulx3s_mixer_pcb) | Verilog | MIT (hdl/LICENSE.txt) | ECP5 | 0 |
| [Self-checking CIC anti-alias decimator (Skywave SDR)](#core-amin005-skywave-cic) | [amin005__skywave_sdr](https://github.com/amin005/skywave_SDR) | Verilog | BSD-3-Clause | any | 1 |
| [Sliding-window DFT envelope extractor + A-law compressor](#core-lit3rick-sliding-dft-envelope) | [kelu124__lit3rick](https://github.com/kelu124/lit3rick) | Verilog | GPL-3.0-or-later | any | 0 |
| [versatile_fft dual-port-RAM FFT engine (opencores, W. Zabolotny)](#core-ckdur-versatile-fft) | [ckdur__riscvconsole](https://github.com/ckdur/RISCVConsole) | VHDL | BSD (file headers 'License: BSD'; credits.txt:… | any | 2 |
| [Vyges configurable 256-4096pt FFT accelerator IP](#core-vyges-fft-ip) | [vyges__fast-fourier-transform-ip](https://github.com/vyges/fast-fourier-transform-ip) | SystemVerilog | Apache-2.0 | any (iCE40/ECP5/Xilinx open flows provided) | 0 |
| [ZipCPU SDR CORDIC + CIC + AM/FM demodulator chain](#core-zipcpu-sdr-cordic-demod) | [zipcpu__sdr](https://github.com/ZipCPU/sdr) | Verilog | GPL-3.0-or-later | any | 2 |
| [CORDICDemod I/Q amplitude/frequency/phase demodulator (Amalthea)](#core-amalthea-cordic-demod) | [greatscottgadgets__amalthea](https://github.com/greatscottgadgets/amalthea) | Python (Amaranth) | BSD-3-Clause | any | 0 |
| [DDS local oscillator](#core-nicocavallu-dds-lo) | [nicocavallu__rf-dds-lo](https://github.com/nicocavallu/rf-dds-lo) | Verilog | none found | any | 1 |
| [Digital down-converter + AM/FM demod chain (post-ADC)](#core-emeb-orangecrab-adc-ddc) | [emeb__orangecrab_adc](https://github.com/emeb/orangecrab_adc) | Verilog | none found | any | 3 |
| [LoRa chirp-spread-spectrum modulator](#core-mehrdadh-lora-chirp) | [mehrdadh__lora-modulator](https://github.com/mehrdadh/lora-modulator) | Verilog | NC-AGPL-3.0 | any | 0 |
| [rf-sdr-frontend digital downconverter](#core-nicocavallu-sdr-ddc) | [nicocavallu__rf-sdr-frontend](https://github.com/nicocavallu/rf-sdr-frontend) | Verilog | none found | any | 0 |
| [WSPR 4-FSK beacon codec (message/FEC/interleave/symbols/modulator)](#core-whisperice-wspr-codec) | [agamez__whisperice](https://github.com/agamez/whisperice) | VHDL-93 | MIT (repo LICENSE; no per-file header) | any | 0 |

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

### 2048-point block-floating-point FFT + Welch PSD feature extractor {#core-ox-computing-fft-bfp-2048}

2048-point in-place FFT: detrend+Hann preprocessing, one complex_butterfly time-shared across stages, address_generator, block-floating-point exponent tracking (fft_scratch_* SPRAM-style memories, fft_twiddle_rom, hann_rom); feeds psd_features.sv for a 13-value Welch PSD feature set (centroid, entropy, rolloff, 6 band powers).

| | |
|---|---|
| Repository | [ox-computing__real-time-analytics-fpga](https://github.com/ox-computing/Real-Time-Analytics-FPGA): Real-Time-Analytics-FPGA: 2048-pt BFP FFT/Welch-PSD feature extractor driving a weightless-NN |
| Files | [`wesad/rtl/feature_engine/fft_engine.sv`](https://github.com/ox-computing/Real-Time-Analytics-FPGA/blob/efe7cbd831ee8d0fad88adf57d7294798041b9d6/wesad/rtl/feature_engine/fft_engine.sv), [`wesad/rtl/feature_engine/psd_features.sv`](https://github.com/ox-computing/Real-Time-Analytics-FPGA/blob/efe7cbd831ee8d0fad88adf57d7294798041b9d6/wesad/rtl/feature_engine/psd_features.sv) |
| Top module | `fft_engine` |
| Language | SystemVerilog |
| License | Apache-2.0 (LICENSE) |
| FPGA / primitives | ECP5: `MULT18X18D` |
| Tests | wesad/tb/tb_fft_engine.sv (self-checking: runs a segment, checks every bin's power against a golden transform, counts errors); wesad/tb/tb_psd_calc.sv, tb_psd_memory.sv |

**On ULX3S:** Built for ECP5 LFE5UM5G-85F in this repo (rtl/constraints/ECP5); shares 2 MULT18X18D DSPs with the time-domain path. A sibling iCE40 UP5K build exists for a different (non-FFT) design in the same repo.

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

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [gage1999__fpga-sdr-receiver](https://github.com/Gage1999/fpga-sdr-receiver) (instantiates [`icesugar_pro/src/top.sv`](https://github.com/Gage1999/fpga-sdr-receiver/blob/f112a4c5f1d7769cb46d2b6fedbe32aefdd715aa/icesugar_pro/src/top.sv))

### 512-point dblclockfft-generated FFT (longwave SDR) {#core-mbsat-dblclockfft-512}

ZipCPU dblclockfft-generated pipelined complex FFT, fixed at 512 points, 16-bit in/out (IWIDTH=OWIDTH=16), one complex sample/clock in, bit-reversed output stage; drives the longwave/VLF SDR's spectrum display.

| | |
|---|---|
| Repository | [mb-sat__ulx3s-longwave-sdr](https://github.com/mb-sat/ulx3s-longwave-sdr): mb-sat/ulx3s-longwave-sdr: longwave/VLF direct-conversion SDR receiver for ULX3S 85F |
| Files | [`logic/ulx3s-stream-verilog/fft-core/fftmain.v`](https://github.com/mb-sat/ulx3s-longwave-sdr/blob/1c2609dd20997b93c40331148adf972b99e33265/logic/ulx3s-stream-verilog/fft-core/fftmain.v), [`logic/ulx3s-stream-verilog/fft-core/fftstage.v`](https://github.com/mb-sat/ulx3s-longwave-sdr/blob/1c2609dd20997b93c40331148adf972b99e33265/logic/ulx3s-stream-verilog/fft-core/fftstage.v), [`logic/ulx3s-stream-verilog/fft-core/hwbfly.v`](https://github.com/mb-sat/ulx3s-longwave-sdr/blob/1c2609dd20997b93c40331148adf972b99e33265/logic/ulx3s-stream-verilog/fft-core/hwbfly.v), [`logic/ulx3s-stream-verilog/fft-core/butterfly.v`](https://github.com/mb-sat/ulx3s-longwave-sdr/blob/1c2609dd20997b93c40331148adf972b99e33265/logic/ulx3s-stream-verilog/fft-core/butterfly.v), [`logic/ulx3s-stream-verilog/fft-core/qtrstage.v`](https://github.com/mb-sat/ulx3s-longwave-sdr/blob/1c2609dd20997b93c40331148adf972b99e33265/logic/ulx3s-stream-verilog/fft-core/qtrstage.v), [`logic/ulx3s-stream-verilog/fft-core/laststage.v`](https://github.com/mb-sat/ulx3s-longwave-sdr/blob/1c2609dd20997b93c40331148adf972b99e33265/logic/ulx3s-stream-verilog/fft-core/laststage.v), [`logic/ulx3s-stream-verilog/fft-core/bitreverse.v`](https://github.com/mb-sat/ulx3s-longwave-sdr/blob/1c2609dd20997b93c40331148adf972b99e33265/logic/ulx3s-stream-verilog/fft-core/bitreverse.v) |
| Top module | `fftmain` |
| Language | Verilog |
| License | LGPL-3.0 (file headers, Gisselquist Technology LLC); repo-level GPL-3.0 (LICENSE) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | none found in this subtree (generator's own bench/ tests are not vendored into this clone) |

**On ULX3S:** Built and run on ULX3S 85F (nextpnr-ecp5 --85k) in this repo - a concrete, board-proven instantiation of the zipcpu__dblclockfft generator at a specific size/width.

### 512-point SDF FFT core (E155 Tuner Project) {#core-dylansebastianheredia-fft512}

512-point (M=9), 16-bit fixed-point FFT: ping-pong dual-RAM banks (ram0/ram1) and a single butterfly unit reused sequentially across all 9 stages under fft_control_unit's address generator; twiddle ROM read per stage.

| | |
|---|---|
| Repository | [dylansebastianheredia__e155_tuner_project](https://github.com/DylanSebastianHeredia/E155_Tuner_Project): E155 Tuner Project: 512-pt 16-bit FFT |
| Files | [`fpga/fft_src_v2/fft.sv`](https://github.com/DylanSebastianHeredia/E155_Tuner_Project/blob/8515eba371f88ad08556c100a8904b842d1b950e/fpga/fft_src_v2/fft.sv), [`fpga/fft_src_v2/fft_control.sv`](https://github.com/DylanSebastianHeredia/E155_Tuner_Project/blob/8515eba371f88ad08556c100a8904b842d1b950e/fpga/fft_src_v2/fft_control.sv), [`fpga/fft_src_v2/fft_agu.sv`](https://github.com/DylanSebastianHeredia/E155_Tuner_Project/blob/8515eba371f88ad08556c100a8904b842d1b950e/fpga/fft_src_v2/fft_agu.sv), [`fpga/fft_src_v2/math.sv`](https://github.com/DylanSebastianHeredia/E155_Tuner_Project/blob/8515eba371f88ad08556c100a8904b842d1b950e/fpga/fft_src_v2/math.sv), [`fpga/fft_src_v2/memory.sv`](https://github.com/DylanSebastianHeredia/E155_Tuner_Project/blob/8515eba371f88ad08556c100a8904b842d1b950e/fpga/fft_src_v2/memory.sv) |
| Top module | `fft` |
| Language | SystemVerilog |
| License | none found |
| FPGA / primitives | iCE40 UP5K (unverified device, README only): none (portable) |
| Tests | fpga/sim/tb_fft_agu*.sv, tb_fft_butterfly.sv, tb_fft_control_unit.sv (Verilator/iverilog, not confirmed self-checking from a Makefile - none in repo) |

**On ULX3S:** Pure SV, no vendor primitives seen; core-only (fft.sv), separate from the SPI/I2S MCU wrapper (fft_master.sv). No pin constraints in repo.

### 64-point iterative radix-2 FFT/IFFT (OFDM PHY) {#core-meharbaan2-ofdm-fft64}

64-point iterative in-place radix-2 FFT/IFFT over an unpacked array (work[]/next_work[]), bit-reversed addressing, 24-bit Q8.16 fixed-point twiddle ROM (case-table); shared forward/inverse via an `inverse` control input.

| | |
|---|---|
| Repository | [meharbaan2__systemverilog-ofdm-phy-core](https://github.com/meharbaan2/systemverilog-ofdm-phy-core): systemverilog-ofdm-phy-core: fixed-point 64-subcarrier OFDM TX/RX PHY with 64-pt radix-2 FFT/IFFT, QAM… |
| Files | [`rtl/ofdm_fft64.sv`](https://github.com/meharbaan2/systemverilog-ofdm-phy-core/blob/4cd42f4311e5f1dc68a9b5d9e4c50d53c966a352/rtl/ofdm_fft64.sv) |
| Top module | `ofdm_fft64` |
| Language | SystemVerilog |
| License | none found |
| FPGA / primitives | iCE40 UP5K (unverified board bring-up): none (portable) |
| Tests | tb/ofdm_basic_tb.sv, tb/ofdm_scoreboard_tb.sv (Verilator, vectors/fft_roundtrip_q16.txt) - README reports PASS locally |

**On ULX3S:** Plain SV, no vendor primitives, portable; sized specifically for a 64-subcarrier OFDM PHY (this repo) rather than as a standalone general FFT.

### 8-band parallel Goertzel spectrum analyzer {#core-hariharan6307-goertzel-spectrum}

8 parallel single-bin Goertzel IIR detectors (100 Hz-12.8 kHz, Q2.14 coefficients, N=480 block) with peak-hold/decay smoothing and a bit-scan log2 bar-height scaler; no FFT, targeted frequencies only.

| | |
|---|---|
| Repository | [hariharan6307-coder__verilog-goertzel-audio-visualizer](https://github.com/Hariharan6307-coder/verilog-goertzel-audio-visualizer): verilog-goertzel-audio-visualizer: 8-band Goertzel spectrum analyzer with peak-hold + log bar scaler, fully… |
| Files | [`goertzel.v`](https://github.com/Hariharan6307-coder/verilog-goertzel-audio-visualizer/blob/fea3e8d108bc4ec038128370265a2a63c0898f05/goertzel.v), [`spectrum.v`](https://github.com/Hariharan6307-coder/verilog-goertzel-audio-visualizer/blob/fea3e8d108bc4ec038128370265a2a63c0898f05/spectrum.v), [`peak_hold.v`](https://github.com/Hariharan6307-coder/verilog-goertzel-audio-visualizer/blob/fea3e8d108bc4ec038128370265a2a63c0898f05/peak_hold.v), [`bar_scaler.v`](https://github.com/Hariharan6307-coder/verilog-goertzel-audio-visualizer/blob/fea3e8d108bc4ec038128370265a2a63c0898f05/bar_scaler.v) |
| Top module | `spectrum` |
| Language | Verilog |
| License | none found |
| FPGA / primitives | any: none (portable) |
| Tests | SubFolder/{goertzel_tb,bar_scaler_tb,peak_hold_tb,spectrum_tb}.v + visualiser_core_tb.v; no Makefile to confirm pass/fail automatically |

**On ULX3S:** Plain portable Verilog, no vendor primitives - drops onto ECP5 unmodified. Cheaper than a full FFT when only a handful of fixed target frequencies matter.

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [enjoy-digital__litedsp](https://github.com/enjoy-digital/litedsp) (instantiates [`impl/modules.py`](https://github.com/enjoy-digital/litedsp/blob/102e415425f60ba21b59972660d56c649612c080/impl/modules.py))

### alhusseingamal/r2sdf-fft radix-2 DIF SDF streaming FFT {#core-alhusseingamal-r2sdf-fft}

Parametric radix-2 DIF single-delay-feedback (SDF) streaming FFT; N=8 uses hardcoded stages, N>8 (up to 512, checked in as a prebuilt iCE40 bitstream) uses a generate loop; W=16, F=14 fixed point (Q1.14). Bit-accurate numpy model in python_model/.

| | |
|---|---|
| Repository | [alhusseingamal__r2sdf-fft](https://github.com/alhusseingamal/r2sdf-fft): r2sdf-fft: radix-2 DIF SDF streaming FFT, parametric N |
| Files | [`rtl/top_level.v`](https://github.com/alhusseingamal/r2sdf-fft/blob/2345c2f4c81739068f1aa215738603fa3b76659f/rtl/top_level.v), [`rtl/sdf_stage.v`](https://github.com/alhusseingamal/r2sdf-fft/blob/2345c2f4c81739068f1aa215738603fa3b76659f/rtl/sdf_stage.v), [`rtl/sdf_stage_d1.v`](https://github.com/alhusseingamal/r2sdf-fft/blob/2345c2f4c81739068f1aa215738603fa3b76659f/rtl/sdf_stage_d1.v), [`rtl/sdf_stage_d2.v`](https://github.com/alhusseingamal/r2sdf-fft/blob/2345c2f4c81739068f1aa215738603fa3b76659f/rtl/sdf_stage_d2.v), [`rtl/sdf_stage_d4.v`](https://github.com/alhusseingamal/r2sdf-fft/blob/2345c2f4c81739068f1aa215738603fa3b76659f/rtl/sdf_stage_d4.v), [`rtl/butterfly.v`](https://github.com/alhusseingamal/r2sdf-fft/blob/2345c2f4c81739068f1aa215738603fa3b76659f/rtl/butterfly.v), [`rtl/twiddle_rom.v`](https://github.com/alhusseingamal/r2sdf-fft/blob/2345c2f4c81739068f1aa215738603fa3b76659f/rtl/twiddle_rom.v) |
| Top module | `top_level` |
| Language | Verilog |
| License | none found |
| FPGA / primitives | any: none (portable) |
| Tests | top-level Makefile:run (verilator, TOP=tb_fft_top): tb/tb_fft_top.v - self-checking (prints SQNR in dB vs data/golden/expected_output.txt, no hard pass/fail assert) |

**On ULX3S:** Plain Verilog, no vendor primitives; resynthesize with yosys synth_ecp5 + nextpnr-ecp5 for ECP5/ULX3S reuse.

### Amaranth radix-2 fixed-point FFT (FFT/Butterfly/TwiddleFactors) {#core-amalthea-fft}

Parametrised in-place radix-2 FFT (any power-of-two size) built from a Butterfly unit, bit-reversed AddressGenerator and a TwiddleFactors ROM, using Q fixed-point/Complex helper types; single dual-port memory holds the working buffer.

| | |
|---|---|
| Repository | [greatscottgadgets__amalthea](https://github.com/greatscottgadgets/amalthea): Amalthea: experimental Amaranth SDR gateware |
| Files | [`amalthea/gateware/fft.py`](https://github.com/greatscottgadgets/amalthea/blob/2d43c7706e2fc2aa581dd58e6348c42cdaf8f230/amalthea/gateware/fft.py), [`amalthea/gateware/types/complex.py`](https://github.com/greatscottgadgets/amalthea/blob/2d43c7706e2fc2aa581dd58e6348c42cdaf8f230/amalthea/gateware/types/complex.py), [`amalthea/gateware/types/fixed_point.py`](https://github.com/greatscottgadgets/amalthea/blob/2d43c7706e2fc2aa581dd58e6348c42cdaf8f230/amalthea/gateware/types/fixed_point.py) |
| Top module | `FFT` |
| Language | Python (Amaranth) |
| License | BSD-3-Clause (LICENSE) |
| FPGA / primitives | any: none (portable) |
| Tests | tests/test_fft.py (pytest, amaranth.sim.Simulator): drives a 32-point FFT and asserts each output bin against numpy's np.fft.fft within 0.02 - self-checking |

**On ULX3S:** Pure Amaranth, no vendor primitives; elaborates to plain Verilog via amaranth.back for any FPGA including ECP5. Needs the amaranth toolchain (yosys+nextpnr-ecp5) in the build flow.

**Used by 16 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [alhusseingamal__r2sdf-fft](https://github.com/alhusseingamal/r2sdf-fft) (instantiates [`python_model/scripts/run_simulation.py`](https://github.com/alhusseingamal/r2sdf-fft/blob/2345c2f4c81739068f1aa215738603fa3b76659f/python_model/scripts/run_simulation.py))
- [ckdur__riscvconsole](https://github.com/ckdur/RISCVConsole) (instantiates [`hardware/riscvconsole/src/main/resources/versatile_fft/fft_engine.vhd`](https://github.com/ckdur/RISCVConsole/blob/7fca231af14bcf7fdcec8b15cb25000238122152/hardware/riscvconsole/src/main/resources/versatile_fft/fft_engine.vhd))
- [dylansebastianheredia__e155_tuner_project](https://github.com/DylanSebastianHeredia/E155_Tuner_Project) (instantiates [`fpga/fft_src_v2/fft_agu.sv`](https://github.com/DylanSebastianHeredia/E155_Tuner_Project/blob/8515eba371f88ad08556c100a8904b842d1b950e/fpga/fft_src_v2/fft_agu.sv))
- [emeb__iceradio](https://github.com/emeb/iceRadio) (instantiates [`FPGA/rxadc_2/python/tst_cic.py`](https://github.com/emeb/iceRadio/blob/632f8c14400ebfe5f82beb154f6df6d3e4bafd4e/FPGA/rxadc_2/python/tst_cic.py))
- [emeb__rpi_rxadc](https://github.com/emeb/rpi_rxadc) (instantiates [`system/plot_freq.py`](https://github.com/emeb/rpi_rxadc/blob/a44b5557ae7f6590998597ddaf960a34f29528e3/system/plot_freq.py))
- [enjoy-digital__litedsp](https://github.com/enjoy-digital/litedsp) (instantiates [`char/metrics.py`](https://github.com/enjoy-digital/litedsp/blob/102e415425f60ba21b59972660d56c649612c080/char/metrics.py))
- [fulig__tinyfpga_fft](https://github.com/fulig/TinyFPGA_FFT) (instantiates [`FFT_stage/top.v`](https://github.com/fulig/TinyFPGA_FFT/blob/77ce2db9af8ea74a1a935ebdb7821d95937528fd/FFT_stage/top.v))
- [gage1999__fpga-sdr-receiver](https://github.com/Gage1999/fpga-sdr-receiver) (instantiates [`icesugar_pro/src/fft256.sv`](https://github.com/Gage1999/fpga-sdr-receiver/blob/f112a4c5f1d7769cb46d2b6fedbe32aefdd715aa/icesugar_pro/src/fft256.sv))
- [ipmgroup__fftd](https://github.com/ipmgroup/fftd) (instantiates [`hardware/rtl/fft_core.v`](https://github.com/ipmgroup/fftd/blob/9049b16114c2e8fcc6545026489fb734f0e0c4ce/hardware/rtl/fft_core.v))
- [kelu124__lit3rick](https://github.com/kelu124/lit3rick) (instantiates [`verilog/src/rtl/top.v`](https://github.com/kelu124/lit3rick/blob/ca4ad983046943fae0694a609154839e8c051283/verilog/src/rtl/top.v))
- [mb-sat__ulx3s-longwave-sdr](https://github.com/mb-sat/ulx3s-longwave-sdr) (instantiates [`logic/ulx3s-stream-verilog/fft-core/fftstage.v`](https://github.com/mb-sat/ulx3s-longwave-sdr/blob/1c2609dd20997b93c40331148adf972b99e33265/logic/ulx3s-stream-verilog/fft-core/fftstage.v))
- [mebner86__icesugar-pro_sound2fft](https://github.com/mebner86/icesugar-pro_sound2fft) (instantiates [`projects/06_live_fft/live_fft.v`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/projects/06_live_fft/live_fft.v))
- [mit-plv__koika](https://github.com/mit-plv/koika) (instantiates [`examples/fft.v`](https://github.com/mit-plv/koika/blob/8921e30434d9e351c49df84c9aa14e72b0456ad0/examples/fft.v))
- [ox-computing__real-time-analytics-fpga](https://github.com/ox-computing/Real-Time-Analytics-FPGA) (instantiates [`wesad/rtl/feature_engine/fft_engine.sv`](https://github.com/ox-computing/Real-Time-Analytics-FPGA/blob/efe7cbd831ee8d0fad88adf57d7294798041b9d6/wesad/rtl/feature_engine/fft_engine.sv))
- [vyges__fast-fourier-transform-ip](https://github.com/vyges/fast-fourier-transform-ip) (instantiates [`flow/synthesis/memory_interface_synth.sv`](https://github.com/vyges/fast-fourier-transform-ip/blob/030b006443d4f77d9373c31d22aa2830d3d03b6a/flow/synthesis/memory_interface_synth.sv))
- … and 1 more (see `data/core_usage.json`)

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

**Used by 2 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [emeb__orangecrab-litex-adc](https://github.com/emeb/OrangeCrab-Litex-ADC) (instantiates [`hw/vsrc/ddc_14.v`](https://github.com/emeb/OrangeCrab-Litex-ADC/blob/6f3d6192d602dcf89b06d04617b87bc1e25ffa54/hw/vsrc/ddc_14.v))
- [emeb__rpi_rxadc](https://github.com/emeb/rpi_rxadc) (instantiates [`gateware/icehat_rxadc/src/ddc_14.v`](https://github.com/emeb/rpi_rxadc/blob/a44b5557ae7f6590998597ddaf960a34f29528e3/gateware/icehat_rxadc/src/ddc_14.v))

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

**Used by 12 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [alberto-grl__1bitsdr](https://github.com/alberto-grl/1bitSDR) (instantiates [`._Real_._Math_.vhd`](https://github.com/alberto-grl/1bitSDR/blob/3e2e01da0357b38a9badff832c65a185b2fdcaf0/._Real_._Math_.vhd))
- [badgeteam__mch2022-firmware-ice40](https://github.com/badgeteam/mch2022-firmware-ice40) (copies [`projects/Forth/rtl/common-verilog/cordic.v`](https://github.com/badgeteam/mch2022-firmware-ice40/blob/ce6473addcf6066cada7d80d8ba352f52173d01d/projects/Forth/rtl/common-verilog/cordic.v))
- [bornabiro__fpga_epaper](https://github.com/BornaBiro/FPGA_epaper) (instantiates [`epaper/_math_real.vhd`](https://github.com/BornaBiro/FPGA_epaper/blob/418985772b72d3113c8cac538c2334e60182e43a/epaper/_math_real.vhd))
- [enjoy-digital__litedsp](https://github.com/enjoy-digital/litedsp) (instantiates [`char/specs.py`](https://github.com/enjoy-digital/litedsp/blob/102e415425f60ba21b59972660d56c649612c080/char/specs.py))
- [greatscottgadgets__amalthea](https://github.com/greatscottgadgets/amalthea) (instantiates [`amalthea/gateware/demod.py`](https://github.com/greatscottgadgets/amalthea/blob/2d43c7706e2fc2aa581dd58e6348c42cdaf8f230/amalthea/gateware/demod.py))
- [joaln27__cordic](https://github.com/joaln27/CORDIC) (instantiates [`formal/f_top.sv`](https://github.com/joaln27/CORDIC/blob/2d169a54caa2b8d72cab4d1ef23b9cd4b3d7219a/formal/f_top.sv))
- [marinsiric__ulx3s](https://github.com/marinsiric/ulx3s) (instantiates [`Diamond/passthru/ulx3s-v2.0-12f/._Real_._Math_.vhd`](https://github.com/marinsiric/ulx3s/blob/b807c99376c149c074b8c8bd51ee56eb95b3fcc9/Diamond/passthru/ulx3s-v2.0-12f/._Real_._Math_.vhd))
- [mysteriouswolf__vna_fpga_dsp](https://github.com/MysteriousWolf/VNA_FPGA_DSP) (instantiates [`._Real_._Math_.vhd`](https://github.com/MysteriousWolf/VNA_FPGA_DSP/blob/c551dceada56e6e8f182f0657a88bc9459074aeb/._Real_._Math_.vhd))
- [nkrackow__singularitysurfer-fpga-lock-in-amplifier](https://github.com/nkrackow/SingularitySurfer-FPGA-Lock-In-Amplifier) (instantiates [`FPGA/HDL/cordic/fullcordic.v`](https://github.com/nkrackow/SingularitySurfer-FPGA-Lock-In-Amplifier/blob/9f7be5b3397ab9c71a1b2c4c0d3f37ebbfccb4a0/FPGA/HDL/cordic/fullcordic.v))
- [pat-pgt__multifrequenciesdetector](https://github.com/pat-pgt/MultiFrequenciesDetector) (instantiates [`VHDL/Cordic_E2E_DC_bundle.vhdl`](https://github.com/pat-pgt/MultiFrequenciesDetector/blob/e30ae531a2c444c8868026fcc41fe7b761547396/VHDL/Cordic_E2E_DC_bundle.vhdl))
- [tarik-hamedovic__sdr-hls](https://github.com/tarik-hamedovic/SDR-HLS) (instantiates [`1.RTLImplementation/4.lattice/Version0-modified/sim/_math_real.vhd`](https://github.com/tarik-hamedovic/SDR-HLS/blob/334f7074eb51dc7d4910a439ba62c85c2668e706/1.RTLImplementation/4.lattice/Version0-modified/sim/_math_real.vhd))
- [tvelliott__dsp_ice](https://github.com/tvelliott/dsp_ice) (instantiates [`firmware/fpga/src/fpga_top.v`](https://github.com/tvelliott/dsp_ice/blob/3da0ddfb66823c326711484ff188eb53da962f46/firmware/fpga/src/fpga_top.v))

### CORDIC-1 bit-serial CORDIC/DDS sine engine {#core-joaln27-cordic}

Bit-serial 16-iteration CORDIC (rotate+vector modes) using a 20-bit shift-register datapath, 3 full adders and fixed-tap bit-muxing instead of barrel shifters; constant 359-cycle op, no vendor primitives.

| | |
|---|---|
| Repository | [joaln27__cordic](https://github.com/joaln27/CORDIC): CORDIC-1: bit-serial CORDIC engine |
| Files | [`src/cordic.sv`](https://github.com/joaln27/CORDIC/blob/2d169a54caa2b8d72cab4d1ef23b9cd4b3d7219a/src/cordic.sv) |
| Top module | `cordic` |
| Language | SystemVerilog |
| License | Apache-2.0 (LICENSE; SPDX header in file) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | cocotb, self-checking (test/test.py + unit_cordic.py vs a Python reference CORDIC/atan2 model); also exhaustive 65536-angle sim and SymbiYosys formal proof outside this repo's test/ dir |

**On ULX3S:** Instantiated unchanged in fpga/ulx3s_top.sv on a real ULX3S 85F; hardware output matches RTL sim bit-exact (389/389 CRC-32 signatures, fpga/meter/, 2026-09-25).

**Used by 11 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [alberto-grl__1bitsdr](https://github.com/alberto-grl/1bitSDR) (instantiates [`._Real_._Math_.vhd`](https://github.com/alberto-grl/1bitSDR/blob/3e2e01da0357b38a9badff832c65a185b2fdcaf0/._Real_._Math_.vhd))
- [bornabiro__fpga_epaper](https://github.com/BornaBiro/FPGA_epaper) (instantiates [`epaper/_math_real.vhd`](https://github.com/BornaBiro/FPGA_epaper/blob/418985772b72d3113c8cac538c2334e60182e43a/epaper/_math_real.vhd))
- [enjoy-digital__litedsp](https://github.com/enjoy-digital/litedsp) (instantiates [`char/specs.py`](https://github.com/enjoy-digital/litedsp/blob/102e415425f60ba21b59972660d56c649612c080/char/specs.py))
- [greatscottgadgets__amalthea](https://github.com/greatscottgadgets/amalthea) (instantiates [`amalthea/gateware/demod.py`](https://github.com/greatscottgadgets/amalthea/blob/2d43c7706e2fc2aa581dd58e6348c42cdaf8f230/amalthea/gateware/demod.py))
- [marinsiric__ulx3s](https://github.com/marinsiric/ulx3s) (instantiates [`Diamond/passthru/ulx3s-v2.0-12f/._Real_._Math_.vhd`](https://github.com/marinsiric/ulx3s/blob/b807c99376c149c074b8c8bd51ee56eb95b3fcc9/Diamond/passthru/ulx3s-v2.0-12f/._Real_._Math_.vhd))
- [mysteriouswolf__vna_fpga_dsp](https://github.com/MysteriousWolf/VNA_FPGA_DSP) (instantiates [`._Real_._Math_.vhd`](https://github.com/MysteriousWolf/VNA_FPGA_DSP/blob/c551dceada56e6e8f182f0657a88bc9459074aeb/._Real_._Math_.vhd))
- [nkrackow__singularitysurfer-fpga-lock-in-amplifier](https://github.com/nkrackow/SingularitySurfer-FPGA-Lock-In-Amplifier) (instantiates [`FPGA/HDL/cordic/fullcordic.v`](https://github.com/nkrackow/SingularitySurfer-FPGA-Lock-In-Amplifier/blob/9f7be5b3397ab9c71a1b2c4c0d3f37ebbfccb4a0/FPGA/HDL/cordic/fullcordic.v))
- [osresearch__up5k](https://github.com/osresearch/up5k) (instantiates [`cordic.v`](https://github.com/osresearch/up5k/blob/2eef12a9659b8fc4ebf68656198b8840f6da2e0d/cordic.v))
- [pat-pgt__multifrequenciesdetector](https://github.com/pat-pgt/MultiFrequenciesDetector) (instantiates [`VHDL/Cordic_E2E_DC_bundle.vhdl`](https://github.com/pat-pgt/MultiFrequenciesDetector/blob/e30ae531a2c444c8868026fcc41fe7b761547396/VHDL/Cordic_E2E_DC_bundle.vhdl))
- [tarik-hamedovic__sdr-hls](https://github.com/tarik-hamedovic/SDR-HLS) (instantiates [`1.RTLImplementation/4.lattice/Version0-modified/sim/_math_real.vhd`](https://github.com/tarik-hamedovic/SDR-HLS/blob/334f7074eb51dc7d4910a439ba62c85c2668e706/1.RTLImplementation/4.lattice/Version0-modified/sim/_math_real.vhd))
- [tvelliott__dsp_ice](https://github.com/tvelliott/dsp_ice) (instantiates [`firmware/fpga/src/fpga_top.v`](https://github.com/tvelliott/dsp_ice/blob/3da0ddfb66823c326711484ff188eb53da962f46/firmware/fpga/src/fpga_top.v))

### dblclockfft pipelined FFT/IFFT generator (C++ -> Verilog) {#core-zipcpu-dblclockfft-generator}

Portable C++ generator (fftgen) that emits a customizable pipelined radix-2 FFT/IFFT core: size, bit widths (in/out/twiddle), forward/inverse and 1-2 samples/clock throughput are all command-line parameters; rtl/ ships a demo 512-point, 16-bit build.

| | |
|---|---|
| Repository | [zipcpu__dblclockfft](https://github.com/ZipCPU/dblclockfft): dblclockfft: ZipCPU's portable C++ generator for a configurable pipelined radix-2 FFT/IFFT core; |
| Files | [`sw/fftgen.cpp`](https://github.com/ZipCPU/dblclockfft/blob/3378b77d83a98b06184656a5cb9b54e50dfe4485/sw/fftgen.cpp), [`sw/fftlib.cpp`](https://github.com/ZipCPU/dblclockfft/blob/3378b77d83a98b06184656a5cb9b54e50dfe4485/sw/fftlib.cpp), [`sw/bldstage.cpp`](https://github.com/ZipCPU/dblclockfft/blob/3378b77d83a98b06184656a5cb9b54e50dfe4485/sw/bldstage.cpp), [`sw/butterfly.cpp`](https://github.com/ZipCPU/dblclockfft/blob/3378b77d83a98b06184656a5cb9b54e50dfe4485/sw/butterfly.cpp), [`sw/bitreverse.cpp`](https://github.com/ZipCPU/dblclockfft/blob/3378b77d83a98b06184656a5cb9b54e50dfe4485/sw/bitreverse.cpp), [`rtl/fftmain.v`](https://github.com/ZipCPU/dblclockfft/blob/3378b77d83a98b06184656a5cb9b54e50dfe4485/rtl/fftmain.v), [`rtl/fftstage.v`](https://github.com/ZipCPU/dblclockfft/blob/3378b77d83a98b06184656a5cb9b54e50dfe4485/rtl/fftstage.v), [`rtl/hwbfly.v`](https://github.com/ZipCPU/dblclockfft/blob/3378b77d83a98b06184656a5cb9b54e50dfe4485/rtl/hwbfly.v), [`rtl/butterfly.v`](https://github.com/ZipCPU/dblclockfft/blob/3378b77d83a98b06184656a5cb9b54e50dfe4485/rtl/butterfly.v), [`rtl/laststage.v`](https://github.com/ZipCPU/dblclockfft/blob/3378b77d83a98b06184656a5cb9b54e50dfe4485/rtl/laststage.v), [`rtl/bitreverse.v`](https://github.com/ZipCPU/dblclockfft/blob/3378b77d83a98b06184656a5cb9b54e50dfe4485/rtl/bitreverse.v) |
| Top module | `fftmain` |
| Language | C++ (generator), Verilog (generated core) |
| License | none found (no LICENSE); GPL-3.0 header on sw/ generator, LGPL-3.0 header on rtl/ generated Verilog |
| FPGA / primitives | any: none (portable) |
| Tests | bench/formal/*.sby (SymbiYosys, formal proofs, PASS) + bench/cpp/fft_tb.cpp/ifft_tb.cpp vs. Octave golden vectors (self-checking) |

**On ULX3S:** No vendor primitives; the single most-reused FFT source in this collection (used, regenerated to size, by mb-sat__ulx3s-longwave-sdr at 512-pt/ECP5-85F and C-Elegans__single_sdr at 256-pt/ECP5-45F).

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [mb-sat__ulx3s-longwave-sdr](https://github.com/mb-sat/ulx3s-longwave-sdr) (instantiates [`logic/ulx3s-stream-verilog/axis/axisfourier.v`](https://github.com/mb-sat/ulx3s-longwave-sdr/blob/1c2609dd20997b93c40331148adf972b99e33265/logic/ulx3s-stream-verilog/axis/axisfourier.v))

### fir_filt pipelined FIR/RBW decimation filter (VNA_FPGA_DSP) {#core-mysteriouswolf-fir-rbw}

Parametrised 16-tap, 4-stage pipelined-MAC FIR used as the resolution-bandwidth/decimation filter for two ADC channels (A/B); coefficients and result shift are runtime-loadable over an addr/coef bus.

| | |
|---|---|
| Repository | [mysteriouswolf__vna_fpga_dsp](https://github.com/MysteriousWolf/VNA_FPGA_DSP): VNA_FPGA_DSP: phase/amplitude detector and RBW |
| Files | [`source/dsp.v`](https://github.com/MysteriousWolf/VNA_FPGA_DSP/blob/c551dceada56e6e8f182f0657a88bc9459074aeb/source/dsp.v) |
| Top module | `fir_filt` |
| Language | Verilog |
| License | none found (no LICENSE/COPYING; no source header) |
| FPGA / primitives | any: none (portable) |
| Tests | none found (no isolated fir_filt tb; the repo's testbench/VNA_FPGA_DSP_tf.v only exercises the full dsp_core via $display, no assert/simulator run confirmed - Radiant-only project) |

**On ULX3S:** No vendor primitives, drop-in on ECP5; note it has no self-checking testbench of its own and no license header (ask before reuse).

### fulig/TinyFPGA_FFT single-butterfly-stage FFT {#core-fulig-fft-single-stage}

Resource-saving FFT variant: one reusable butterfly-processor stage (fft_stage.v, instantiating bfprocessor.v N/2 times via generate) is reloaded iteratively for each of the log2(N) FFT stages under a small FSM (fft.v: IDLE/DATA_IN/CALC_FFT/DATA_OUT), instead of unrolling every stage as the sibling 8FFT/ design does.

| | |
|---|---|
| Repository | [fulig__tinyfpga_fft](https://github.com/fulig/TinyFPGA_FFT): TinyFPGA_FFT: bachelor-thesis 8-pt FFT, TinyFPGA BX - full-unrolled 8FFT/ plus a single-butterfly-stage… |
| Files | [`FFT_stage/fft.v`](https://github.com/fulig/TinyFPGA_FFT/blob/77ce2db9af8ea74a1a935ebdb7821d95937528fd/FFT_stage/fft.v), [`FFT_stage/fft_stage.v`](https://github.com/fulig/TinyFPGA_FFT/blob/77ce2db9af8ea74a1a935ebdb7821d95937528fd/FFT_stage/fft_stage.v), [`FFT_stage/bfprocessor.v`](https://github.com/fulig/TinyFPGA_FFT/blob/77ce2db9af8ea74a1a935ebdb7821d95937528fd/FFT_stage/bfprocessor.v) |
| Top module | `fft` |
| Language | Verilog |
| License | none found |
| FPGA / primitives | any: none (portable) |
| Tests | no self-checking testbench found in FFT_stage/ |

**On ULX3S:** Plain Verilog, parametric N/MSB, but only exercised at N=8 on a TinyFPGA BX (iCE40 LP8K); no vendor primitives, portable to ECP5.

### Gage1999/fpga-sdr-receiver 256-pt iterative radix-2 FFT {#core-gage1999-fft256-iterative}

Iterative in-place 256-pt radix-2 FFT: one butterfly module reused across all 8 stages via a ping-pong BRAM bank, 128-entry inline cos/sin LUT, bit-reversed output; 16-bit signed I/Q in, 8-bit log-magnitude + 8-bit bin index out. Feeds an SDR spectrum/waterfall display in this repo.

| | |
|---|---|
| Repository | [gage1999__fpga-sdr-receiver](https://github.com/Gage1999/fpga-sdr-receiver): fpga-sdr-receiver: ECP5 iCESugar-Pro SDR |
| Files | [`icesugar_pro/src/fft256.sv`](https://github.com/Gage1999/fpga-sdr-receiver/blob/f112a4c5f1d7769cb46d2b6fedbe32aefdd715aa/icesugar_pro/src/fft256.sv), [`icesugar_pro/src/butterfly.sv`](https://github.com/Gage1999/fpga-sdr-receiver/blob/f112a4c5f1d7769cb46d2b6fedbe32aefdd715aa/icesugar_pro/src/butterfly.sv), [`icesugar_pro/src/twiddle_rom.sv`](https://github.com/Gage1999/fpga-sdr-receiver/blob/f112a4c5f1d7769cb46d2b6fedbe32aefdd715aa/icesugar_pro/src/twiddle_rom.sv) |
| Top module | `fft256` |
| Language | SystemVerilog |
| License | MIT (LICENSE) |
| FPGA / primitives | any: none (portable) |
| Tests | icesugar_pro/Makefile:sim_fft (iverilog): tb/tb_fft256.sv - self-checking (PASS/FAIL, DC-bin and single-tone peak checks) |

**On ULX3S:** Built for ECP5 (iCESugar Pro LFE5U-25F) but no vendor primitives instantiated in these 3 files; drop-in on ULX3S ECP5 designs.

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [mebner86__icesugar-pro_sound2fft](https://github.com/mebner86/icesugar-pro_sound2fft) (instantiates [`projects/06_live_fft/live_fft.v`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/projects/06_live_fft/live_fft.v))

### HackRF Amaranth CIC/FIR/NCO/mixer DSP chain {#core-hackrf-amaranth-dsp-chain}

Amaranth CIC interpolator/decimator (cic.py), half-band FIR decimator/interpolator (fir.py), a 1/8-wave-LUT NCO (nco.py) and a complex mixer built on 4 iCE40 SB_MAC16 DSP blocks (mixer.py) forming the HackRF Pro baseband RX/TX chain. Unit-tested against numpy reference models.

| | |
|---|---|
| Repository | [greatscottgadgets__hackrf](https://github.com/greatscottgadgets/hackrf): HackRF firmware/fpga: Amaranth DSP gateware for the HackRF Pro |
| Files | [`firmware/fpga/dsp/cic.py`](https://github.com/greatscottgadgets/hackrf/blob/7f96cc8e3fa625c4263a71ba8dd44d1f6110e4fa/firmware/fpga/dsp/cic.py), [`firmware/fpga/dsp/fir.py`](https://github.com/greatscottgadgets/hackrf/blob/7f96cc8e3fa625c4263a71ba8dd44d1f6110e4fa/firmware/fpga/dsp/fir.py), [`firmware/fpga/dsp/nco.py`](https://github.com/greatscottgadgets/hackrf/blob/7f96cc8e3fa625c4263a71ba8dd44d1f6110e4fa/firmware/fpga/dsp/nco.py), [`firmware/fpga/dsp/mixer.py`](https://github.com/greatscottgadgets/hackrf/blob/7f96cc8e3fa625c4263a71ba8dd44d1f6110e4fa/firmware/fpga/dsp/mixer.py), [`firmware/fpga/dsp/dc_block.py`](https://github.com/greatscottgadgets/hackrf/blob/7f96cc8e3fa625c4263a71ba8dd44d1f6110e4fa/firmware/fpga/dsp/dc_block.py), [`firmware/fpga/dsp/sb_mac16.py`](https://github.com/greatscottgadgets/hackrf/blob/7f96cc8e3fa625c4263a71ba8dd44d1f6110e4fa/firmware/fpga/dsp/sb_mac16.py) |
| Top module | n/a |
| Language | Python (Amaranth) |
| License | BSD-3-Clause (SPDX header in each file, e.g. dsp/nco.py); repo-wide COPYING is GPL-2.0 |
| FPGA / primitives | iCE40: `SB_MAC16` |
| Tests | firmware/fpga/test/test_{cic,fir,fir_mac16,mixer,fixed}.py (Amaranth Simulator + numpy models): self-checking (assertEqual/assert against a Python reference model) |

**On ULX3S:** cic.py/fir.py/nco.py/dc_block.py instantiate no vendor primitives and elaborate to plain Verilog via Amaranth+yosys, so they are portable to ECP5 with the standard Amaranth ECP5 platform. mixer.py's ComplexMultiplier instantiates SB_MAC16 directly (dsp/sb_mac16.py) and needs an ECP5 MULT18X18D rewrite to reuse there.

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

### ipmgroup/fftd 1024-pt radix-2 DIT FFT core {#core-ipmgroup-fft1024-radix2}

Parametric radix-2 DIT FFT (N_LOG2, WIDTH=16) with a BRAM twiddle ROM and a block-floating-point exponent output; instantiated as N=1024 by the SPI-wrapped hardware/rtl/fft_top.v. Plain Verilog, BRAM inferred via a (* syn_ramstyle = "block_ram" *) attribute, not an explicit primitive.

| | |
|---|---|
| Repository | [ipmgroup__fftd](https://github.com/ipmgroup/fftd): ice40-fft: SPI-attached 1024-point radix-2 DIT FFT accelerator for a Raspberry Pi HAT |
| Files | [`hardware/rtl/fft_core.v`](https://github.com/ipmgroup/fftd/blob/9049b16114c2e8fcc6545026489fb734f0e0c4ce/hardware/rtl/fft_core.v), [`hardware/rtl/twiddle_rom.v`](https://github.com/ipmgroup/fftd/blob/9049b16114c2e8fcc6545026489fb734f0e0c4ce/hardware/rtl/twiddle_rom.v) |
| Top module | `fft_core` |
| Language | Verilog |
| License | MIT (LICENSE) |
| FPGA / primitives | any: none (portable) |
| Tests | hardware/sim/tb_fft_core.v - waveform/print-only, no assert |

**On ULX3S:** No ECP5 build in this repo (built for iCE40 HX4K); the fft_core.v module itself has no vendor primitives so it should synthesize on ECP5 as-is. fft_top.v additionally instantiates an ICE40 SB_PLL40_2F_PAD, not included here.

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [dylansebastianheredia__e155_tuner_project](https://github.com/DylanSebastianHeredia/E155_Tuner_Project) (instantiates [`fpga/fft_src_v2/fft.sv`](https://github.com/DylanSebastianHeredia/E155_Tuner_Project/blob/8515eba371f88ad08556c100a8904b842d1b950e/fpga/fft_src_v2/fft.sv))

### LiteDSP radix-2 SDF FFT/IFFT (Migen/LiteX) {#core-litedsp-fft-sdf}

Streaming radix-2 single-path delay-feedback (SDF) DIF FFT/IFFT, any power-of-two N (default 64), Q1.15 by default, 'scaled' (1/N) or block-floating-point scaling with a per-frame 5-bit exponent param, classic (1 sample/clk) or folded (1 sample/2clk) architecture.

| | |
|---|---|
| Repository | [enjoy-digital__litedsp](https://github.com/enjoy-digital/litedsp): litedsp: Migen/LiteX portable RF/DSP block library incl. |
| Files | [`litedsp/analysis/fft.py`](https://github.com/enjoy-digital/litedsp/blob/102e415425f60ba21b59972660d56c649612c080/litedsp/analysis/fft.py) |
| Top module | `LiteDSPFFT` |
| Language | Python (Migen/LiteX) |
| License | BSD-2-Clause (SPDX header) |
| FPGA / primitives | any: none (portable) |
| Tests | test/test_fft.py, test/test_fft_bfp.py (unittest, NumPy golden model, bit-exact/SNR-checked in CI) |

**On ULX3S:** Pure Migen HDL generator (no vendor primitives); ECP5 out-of-context flow verified in impl/ecp5.py (LFE5UM5G-85F: 4387 LUT/28 DSP at N=64). Use as a LiteX submodule or export Verilog via litedsp/verilog.py.

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [greatscottgadgets__amalthea](https://github.com/greatscottgadgets/amalthea) (copies [`amalthea/gateware/fft.py`](https://github.com/greatscottgadgets/amalthea/blob/2d43c7706e2fc2aa581dd58e6348c42cdaf8f230/amalthea/gateware/fft.py))

### Lock-in amplifier DSP chain (DDS + mixer + CIC/IIR + CORDIC) {#core-nkrackow-lockin-dsp-chain}

Full lock-in signal chain: 1/4-sine-LUT DDS/NCO reference (16-bit amplitude, 18-bit phase), SB_MAC16-based 16x16 mixer, single-stage CIC decimator, multiplier-less shift-based IIR lowpass (RIIR, Migen-generated), and a 9-iteration CORDIC for rect->polar (magnitude/phase) readout.

| | |
|---|---|
| Repository | [nkrackow__singularitysurfer-fpga-lock-in-amplifier](https://github.com/nkrackow/SingularitySurfer-FPGA-Lock-In-Amplifier): SingularitySurfer: FPGA lock-in amplifier |
| Files | [`FPGA/HDL/dds.v`](https://github.com/nkrackow/SingularitySurfer-FPGA-Lock-In-Amplifier/blob/9f7be5b3397ab9c71a1b2c4c0d3f37ebbfccb4a0/FPGA/HDL/dds.v), [`FPGA/HDL/mult16x16.v`](https://github.com/nkrackow/SingularitySurfer-FPGA-Lock-In-Amplifier/blob/9f7be5b3397ab9c71a1b2c4c0d3f37ebbfccb4a0/FPGA/HDL/mult16x16.v), [`FPGA/HDL/filter/CIC.v`](https://github.com/nkrackow/SingularitySurfer-FPGA-Lock-In-Amplifier/blob/9f7be5b3397ab9c71a1b2c4c0d3f37ebbfccb4a0/FPGA/HDL/filter/CIC.v), [`FPGA/HDL/filter/RIIR.v`](https://github.com/nkrackow/SingularitySurfer-FPGA-Lock-In-Amplifier/blob/9f7be5b3397ab9c71a1b2c4c0d3f37ebbfccb4a0/FPGA/HDL/filter/RIIR.v), [`FPGA/HDL/cordic/cordic.v`](https://github.com/nkrackow/SingularitySurfer-FPGA-Lock-In-Amplifier/blob/9f7be5b3397ab9c71a1b2c4c0d3f37ebbfccb4a0/FPGA/HDL/cordic/cordic.v), [`FPGA/HDL/cordic/fullcordic.v`](https://github.com/nkrackow/SingularitySurfer-FPGA-Lock-In-Amplifier/blob/9f7be5b3397ab9c71a1b2c4c0d3f37ebbfccb4a0/FPGA/HDL/cordic/fullcordic.v) |
| Top module | n/a |
| Language | Verilog (+ Python RIIR_migen.py generator for RIIR.v) |
| License | MIT (LICENSE) |
| FPGA / primitives | iCE40 UP5K: `SB_MAC16` |
| Tests | waveform-only: CIC_tb.v/top_tb.v only print a placeholder ($display "hallu world"), tb_cordic.v prints computed angle/sin/cos/error via $display but has no assert/PASS-FAIL (see catalogue make_tests for the verbatim Makefile targets) |

**On ULX3S:** mult16x16.v's SB_MAC16 instance must be replaced by a plain '*' multiply (or let yosys infer ECP5 DSP) for ECP5; dds.v/CIC.v/RIIR.v/cordic.v/fullcordic.v carry no vendor primitives and port directly. Full chain is wired together in FPGA/HDL/filter/filterdemo.v (board-specific top with LCD UI, not included here).

### MAC units for exotic number formats (int8/bf16/fp16/posit8/mxfp8/lns8) {#core-uttamcoomar-mac-int8}

MyHDL-generated multiply-accumulate unit wrapped in a UART command/readback shell, built and tested on ULX3S ECP5-85F; the same layout repeats for bf16, fp16, lns8 (log number system), mxfp8 (microscaling FP8) and posit8 formats in sibling directories.

| | |
|---|---|
| Repository | [uttamcoomar__mac-units-for-various-number-formats](https://github.com/uttamcoomar/MAC-units-for-various-number-formats): MAC Units for ULX3S: multiply-accumulate units in six number formats |
| Files | [`int8/mac_int8.v`](https://github.com/uttamcoomar/MAC-units-for-various-number-formats/blob/1861c092fe5e2327ff3b1addcbdd6e5f9ed415bc/int8/mac_int8.v), [`int8/top.v`](https://github.com/uttamcoomar/MAC-units-for-various-number-formats/blob/1861c092fe5e2327ff3b1addcbdd6e5f9ed415bc/int8/top.v), [`int8/uart_rx.v`](https://github.com/uttamcoomar/MAC-units-for-various-number-formats/blob/1861c092fe5e2327ff3b1addcbdd6e5f9ed415bc/int8/uart_rx.v), [`int8/uart_tx.v`](https://github.com/uttamcoomar/MAC-units-for-various-number-formats/blob/1861c092fe5e2327ff3b1addcbdd6e5f9ed415bc/int8/uart_tx.v) |
| Top module | `top` |
| Language | Verilog, Python (MyHDL sources) |
| License | none found |
| FPGA / primitives | ECP5: none (portable) |
| Tests | int8/tb_mac_int8.v + int8/test_mac_int8.py (12 tb/test files total across all six formats, per scan_tests.sh) |

**On ULX3S:** No vendor primitives; each format's mac_<fmt>.v is a separate small core (not parametrized), pick the directory matching the number format needed. Each has its own tb_mac_<fmt>.v and a Python UART host test.

### mattvenn/fpga-sdft sliding DFT core {#core-mattvenn-sliding-dft}

Sliding DFT (not a classic FFT): computes an arbitrary number of frequency bins continuously, 3 clocks/bin; parametric data_width/freq_bins/freq_w; twiddle ROM loaded via $readmemh from files generated by python/gen_twiddle.py; validated against numpy in python/sdft.py.

| | |
|---|---|
| Repository | [mattvenn__fpga-sdft](https://github.com/mattvenn/fpga-sdft): fpga-sdft: sliding DFT |
| Files | [`hdl/sdft.v`](https://github.com/mattvenn/fpga-sdft/blob/93c9361fb596fc29b3753e10efc4e6148b5a3b93/hdl/sdft.v), [`hdl/twiddle_rom.v`](https://github.com/mattvenn/fpga-sdft/blob/93c9361fb596fc29b3753e10efc4e6148b5a3b93/hdl/twiddle_rom.v) |
| Top module | `sdft` |
| Language | Verilog |
| License | none found |
| FPGA / primitives | any: none (portable) |
| Tests | tests/sdft_tb.v - waveform-only (no PASS/FAIL in-sim); python/read_vcd.py + `make model-sdft` compares to numpy externally |

**On ULX3S:** Plain Verilog, portable to ECP5 as-is. Regenerate twiddle_real.list/twiddle_imag.list for a different freq_bins/data_width via python/gen_twiddle.py before reuse.

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [kelu124__lit3rick](https://github.com/kelu124/lit3rick) (instantiates [`py_fpga/dft.py`](https://github.com/kelu124/lit3rick/blob/ca4ad983046943fae0694a609154839e8c051283/py_fpga/dft.py))

### MaxZischka1/FastFourierTransformProject 16-pt radix-2 SDF FFT {#core-maxzischka1-sdf16-fft}

16-point radix-2 single-delay-feedback FFT chaining 4 SDFCell/SDFCell0 stages (sizes 16/8/4/2); SBM16.sv wraps 4x SB_MAC16 for the complex twiddle multiply. Q1.15 fixed point (see inputsGen.py/twiddleGen.py).

| | |
|---|---|
| Repository | [maxzischka1__fastfouriertransformproject](https://github.com/MaxZischka1/FastFourierTransformProject): FastFourierTransformProject: 16-point radix-2 single-delay-feedback FFT IP |
| Files | [`TopLevel.sv`](https://github.com/MaxZischka1/FastFourierTransformProject/blob/590a2ad46fc62ceeaa775ab27bde1fd5d9ab83ca/TopLevel.sv), [`SDFCell.sv`](https://github.com/MaxZischka1/FastFourierTransformProject/blob/590a2ad46fc62ceeaa775ab27bde1fd5d9ab83ca/SDFCell.sv), [`SDFCell0.sv`](https://github.com/MaxZischka1/FastFourierTransformProject/blob/590a2ad46fc62ceeaa775ab27bde1fd5d9ab83ca/SDFCell0.sv), [`SBM16.sv`](https://github.com/MaxZischka1/FastFourierTransformProject/blob/590a2ad46fc62ceeaa775ab27bde1fd5d9ab83ca/SBM16.sv) |
| Top module | `TopLevel` |
| Language | SystemVerilog |
| License | none found |
| FPGA / primitives | iCE40: `SB_MAC16` |
| Tests | waveform-only (tb_TopLevel.cpp dumps a VCD; no PASS/FAIL/assert found) |

**On ULX3S:** SB_MAC16 is iCE40-only; port SBM16.sv to an ECP5 multiplier (e.g. the MULT18X18D wrappers in c-elegans__single_sdr rtl/mult18x18_*c.v) to reuse the SDFCell chain on ECP5/ULX3S.

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

### Self-checking CIC anti-alias decimator (Skywave SDR) {#core-amin005-skywave-cic}

Parametric Hogenauer CIC decimator (WIDTH/STAGES/R): wrapping two's-complement integrators with comb cancellation give exact renormalization for power-of-two decimation; ships with a self-checking testbench that PASS/FAILs on in-band-pass vs out-of-band-rejection.

| | |
|---|---|
| Repository | [amin005__skywave_sdr](https://github.com/amin005/skywave_SDR): Skywave SDR: direct-sampling HF receiver, AD9226 12-bit/32MSPS ADC -> CIC decimate-by-4 -> own ULPI USB-HS… |
| Files | [`fpga/cic_decim.v`](https://github.com/amin005/skywave_SDR/blob/15c6b23c460bd667293480f35393573e3d24449b/fpga/cic_decim.v), [`fpga/tb_cic.v`](https://github.com/amin005/skywave_SDR/blob/15c6b23c460bd667293480f35393573e3d24449b/fpga/tb_cic.v) |
| Top module | `cic_decim` |
| Language | Verilog |
| License | BSD-3-Clause (LICENSE) |
| FPGA / primitives | any: none (portable) |
| Tests | fpga/tb_cic.v (iverilog, self-checking: PASS/FAIL on in-band-pass vs out-of-band-rejection; run manually per README, no Makefile target) |

**On ULX3S:** No vendor primitives; plain parametric Verilog, drop-in on ECP5/ULX3S. Currently decimates a real (not I/Q) ADC stream 32MSPS->8MSPS on an ECP5 25F board; per its own header comment the same block doubles as the post-mixer channel filter in an I/Q DDC.

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [enjoy-digital__litedsp](https://github.com/enjoy-digital/litedsp) (instantiates [`char/specs.py`](https://github.com/enjoy-digital/litedsp/blob/102e415425f60ba21b59972660d56c649612c080/char/specs.py))

### Sliding-window DFT envelope extractor + A-law compressor {#core-lit3rick-sliding-dft-envelope}

16-point sliding-window (non-overlapped) DFT computing 3 frequency bins over an 8192-sample 12-bit acquisition, magnitude via dft_complex_abs+dft_sqrt, then G.711 A-law compressed 15->8 bit; used as an on-chip envelope/backscatter-amplitude extractor for ultrasound echoes rather than a full-spectrum FFT (sibling verilog/sigprocessing/code_fourrier/README.md calls it a 'Fourier (envelope extraction) IP-core').

| | |
|---|---|
| Repository | [kelu124__lit3rick](https://github.com/kelu124/lit3rick): lit3rick: single-channel ultrasound pulse-echo board - UP5K ADC/pulser, on-chip DFT envelope extraction,… |
| Files | [`verilog/src/rtl/fft/dft.v`](https://github.com/kelu124/lit3rick/blob/ca4ad983046943fae0694a609154839e8c051283/verilog/src/rtl/fft/dft.v), [`verilog/src/rtl/fft/dft_core.v`](https://github.com/kelu124/lit3rick/blob/ca4ad983046943fae0694a609154839e8c051283/verilog/src/rtl/fft/dft_core.v), [`verilog/src/rtl/fft/dft_preproc.v`](https://github.com/kelu124/lit3rick/blob/ca4ad983046943fae0694a609154839e8c051283/verilog/src/rtl/fft/dft_preproc.v), [`verilog/src/rtl/fft/dft_postproc.v`](https://github.com/kelu124/lit3rick/blob/ca4ad983046943fae0694a609154839e8c051283/verilog/src/rtl/fft/dft_postproc.v), [`verilog/src/rtl/fft/dft_complex_abs.v`](https://github.com/kelu124/lit3rick/blob/ca4ad983046943fae0694a609154839e8c051283/verilog/src/rtl/fft/dft_complex_abs.v), [`verilog/src/rtl/fft/dft_sqrt.v`](https://github.com/kelu124/lit3rick/blob/ca4ad983046943fae0694a609154839e8c051283/verilog/src/rtl/fft/dft_sqrt.v), [`verilog/src/rtl/alaw_coder.v`](https://github.com/kelu124/lit3rick/blob/ca4ad983046943fae0694a609154839e8c051283/verilog/src/rtl/alaw_coder.v) |
| Top module | `dft` |
| Language | Verilog |
| License | GPL-3.0-or-later (repo Readme.md ## License, covers gateware generically; no per-file SPDX header in dft*.v/alaw_coder.v) |
| FPGA / primitives | any: none (portable) |
| Tests | self-checking: verilog/src/tb/tb_top.sv test_fft task (run via ModelSim, verilog/modelsim/tb_top.do) drives the DFT through the I2C register interface and reads back bins with $error on mismatch; standalone per-module testbenches (tb_dft.v, tb_dft_core.v, tb_dft_postproc.v, ...) live in the sibling verilog/sigprocessing/code_fourrier/sim/{icarus,modelsim}/ |

**On ULX3S:** No vendor primitives in dft*.v/alaw_coder.v themselves; the surrounding sc_fifo/ebr_dp memory wrappers (verilog/src/rtl/ip_cores/) are UP5K Radiant IP-catalog cores and would need porting to ECP5 DP16KD/PDP16K. DFT_N and FREQ_BINS_USED are compile-time localparams in dft_core.v.

Full review: [kelu124__lit3rick](../projects/kelu124__lit3rick.md).

### versatile_fft dual-port-RAM FFT engine (opencores, W. Zabolotny) {#core-ckdur-versatile-fft}

Single-butterfly, dual-port-RAM-based FFT processor (opencores versatile_fft), size fixed at compile time by LOG2_FFT_LEN in fft_len.vhd (1024-point in this clone); fft_wrapper.vhd exposes a Verilog-friendly boundary for integration as a Chipyard/RocketChip MMIO peripheral.

| | |
|---|---|
| Repository | [ckdur__riscvconsole](https://github.com/ckdur/RISCVConsole): RISCVConsole: Chipyard-based RISC-V SoC aiming to run Linux and drive HDMI graphics, framed as an attempted… |
| Files | [`hardware/riscvconsole/src/main/resources/versatile_fft/fft_engine.vhd`](https://github.com/ckdur/RISCVConsole/blob/7fca231af14bcf7fdcec8b15cb25000238122152/hardware/riscvconsole/src/main/resources/versatile_fft/fft_engine.vhd), [`hardware/riscvconsole/src/main/resources/versatile_fft/fft_wrapper.vhd`](https://github.com/ckdur/RISCVConsole/blob/7fca231af14bcf7fdcec8b15cb25000238122152/hardware/riscvconsole/src/main/resources/versatile_fft/fft_wrapper.vhd), [`hardware/riscvconsole/src/main/resources/versatile_fft/butterfly.vhd`](https://github.com/ckdur/RISCVConsole/blob/7fca231af14bcf7fdcec8b15cb25000238122152/hardware/riscvconsole/src/main/resources/versatile_fft/butterfly.vhd), [`hardware/riscvconsole/src/main/resources/versatile_fft/dpram_inf.vhd`](https://github.com/ckdur/RISCVConsole/blob/7fca231af14bcf7fdcec8b15cb25000238122152/hardware/riscvconsole/src/main/resources/versatile_fft/dpram_inf.vhd), [`hardware/riscvconsole/src/main/resources/versatile_fft/icpxram.vhd`](https://github.com/ckdur/RISCVConsole/blob/7fca231af14bcf7fdcec8b15cb25000238122152/hardware/riscvconsole/src/main/resources/versatile_fft/icpxram.vhd), [`hardware/riscvconsole/src/main/resources/versatile_fft/icpx_pkg.vhd`](https://github.com/ckdur/RISCVConsole/blob/7fca231af14bcf7fdcec8b15cb25000238122152/hardware/riscvconsole/src/main/resources/versatile_fft/icpx_pkg.vhd), [`hardware/riscvconsole/src/main/resources/versatile_fft/fft_len.vhd`](https://github.com/ckdur/RISCVConsole/blob/7fca231af14bcf7fdcec8b15cb25000238122152/hardware/riscvconsole/src/main/resources/versatile_fft/fft_len.vhd) |
| Top module | `fft_wrapper` |
| Language | VHDL |
| License | BSD (file headers 'License: BSD'; credits.txt: opencores.org versatile_fft, (c) 2014 Wojciech Zabolotny) |
| FPGA / primitives | any: none (portable) |
| Tests | none found in this subtree |

**On ULX3S:** Plain VHDL, no vendor primitives; wired up here as devices/fft/fft.scala + fft_peripheral.scala in a RocketChip SoC targeted (among other boards) at fpga/ULX3S in this repo.

**Used by 2 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [ox-computing__real-time-analytics-fpga](https://github.com/ox-computing/Real-Time-Analytics-FPGA) (instantiates [`wesad/rtl/wesad_dwn_top.sv`](https://github.com/ox-computing/Real-Time-Analytics-FPGA/blob/efe7cbd831ee8d0fad88adf57d7294798041b9d6/wesad/rtl/wesad_dwn_top.sv))
- [vyges__fast-fourier-transform-ip](https://github.com/vyges/fast-fourier-transform-ip) (instantiates [`rtl/fft_fft_top.sv`](https://github.com/vyges/fast-fourier-transform-ip/blob/030b006443d4f77d9373c31d22aa2830d3d03b6a/rtl/fft_fft_top.sv))

### Vyges configurable 256-4096pt FFT accelerator IP {#core-vyges-fft-ip}

Configurable radix-2 DIF FFT/IFFT accelerator, 256-4096 points (FFT_MAX_LENGTH_LOG2 param), 16-bit data/twiddle width, APB register interface + optional AXI/bus-master DMA, automatic per-stage rescale with overflow tracking.

| | |
|---|---|
| Repository | [vyges__fast-fourier-transform-ip](https://github.com/vyges/fast-fourier-transform-ip): fast-fourier-transform-ip: configurable 256-4096pt radix-2 DIF FFT accelerator IP |
| Files | [`rtl/fft_fft_top.sv`](https://github.com/vyges/fast-fourier-transform-ip/blob/030b006443d4f77d9373c31d22aa2830d3d03b6a/rtl/fft_fft_top.sv), [`rtl/fft_fft_engine.sv`](https://github.com/vyges/fast-fourier-transform-ip/blob/030b006443d4f77d9373c31d22aa2830d3d03b6a/rtl/fft_fft_engine.sv), [`rtl/fft_fft_control.sv`](https://github.com/vyges/fast-fourier-transform-ip/blob/030b006443d4f77d9373c31d22aa2830d3d03b6a/rtl/fft_fft_control.sv), [`rtl/fft_rescale_unit.sv`](https://github.com/vyges/fast-fourier-transform-ip/blob/030b006443d4f77d9373c31d22aa2830d3d03b6a/rtl/fft_rescale_unit.sv), [`rtl/fft_scale_factor_tracker.sv`](https://github.com/vyges/fast-fourier-transform-ip/blob/030b006443d4f77d9373c31d22aa2830d3d03b6a/rtl/fft_scale_factor_tracker.sv), [`rtl/fft_twiddle_rom.sv`](https://github.com/vyges/fast-fourier-transform-ip/blob/030b006443d4f77d9373c31d22aa2830d3d03b6a/rtl/fft_twiddle_rom.sv), [`rtl/fft_memory_interface.sv`](https://github.com/vyges/fast-fourier-transform-ip/blob/030b006443d4f77d9373c31d22aa2830d3d03b6a/rtl/fft_memory_interface.sv) |
| Top module | `fft_top` |
| Language | SystemVerilog |
| License | Apache-2.0 (LICENSE, file headers) |
| FPGA / primitives | any (iCE40/ECP5/Xilinx open flows provided): none (portable) |
| Tests | tb/sv_tb/tb_fft_top.sv + tb/cocotb/test_fft_*.py written but currently broken (stale rtl filenames in the Makefiles; see catalogue notes) |

**On ULX3S:** Pure SV, no vendor primitives; ECP5 flow present (flow/fpga/Makefile FPGA_FAMILY=ecp5, nextpnr-ecp5 --25k) but several of its own test/cocotb Makefiles reference stale filenames post-rename - verify manually before relying on `make test`.

### ZipCPU SDR CORDIC + CIC + AM/FM demodulator chain {#core-zipcpu-sdr-cordic-demod}

Sequential (one sample/cycle) CORDIC vector rotator feeding a CIC integrate-and-dump decimator and a generic filter-then-downsample block; amdemod.v and fmdemod.v compose these into AM and FM demodulators (fmdemod recovers phase via an I+Q PLL then differentiates it). No vendor primitives, formally-flavoured ZipCPU coding style.

| | |
|---|---|
| Repository | [zipcpu__sdr](https://github.com/ZipCPU/sdr): ZipCPU/sdr: 'Gateware Defined Radio' - AM/FM/QPSK transmitter and receiver designs for an iCEBreaker + SX1257… |
| Files | [`rtl/seqcordic.v`](https://github.com/ZipCPU/sdr/blob/f143194d096579168e1c33c02713b0c44260c234/rtl/seqcordic.v), [`rtl/cicfil.v`](https://github.com/ZipCPU/sdr/blob/f143194d096579168e1c33c02713b0c44260c234/rtl/cicfil.v), [`rtl/subfildown.v`](https://github.com/ZipCPU/sdr/blob/f143194d096579168e1c33c02713b0c44260c234/rtl/subfildown.v), [`rtl/amdemod.v`](https://github.com/ZipCPU/sdr/blob/f143194d096579168e1c33c02713b0c44260c234/rtl/amdemod.v), [`rtl/fmdemod.v`](https://github.com/ZipCPU/sdr/blob/f143194d096579168e1c33c02713b0c44260c234/rtl/fmdemod.v) |
| Top module | `fmdemod` |
| Language | Verilog |
| License | GPL-3.0-or-later (file headers, e.g. rtl/cicfil.v; no LICENSE file in this clone) |
| FPGA / primitives | any: none (portable) |
| Tests | sim/ (Verilator, main_tb.cpp): builds an interactive simulator, no automated pass/fail check found (README: 'isn't very useful at present' without the -d VCD switch) |

**On ULX3S:** Board-independent Verilog, originally paired with an SX1257 RF PMod on an iCEBreaker. Good reference for a CORDIC-based FM discriminator or AM envelope detector on ECP5.

**Used by 2 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [alberto-grl__1bitsdr](https://github.com/alberto-grl/1bitSDR) (instantiates [`impl1/source/top.v`](https://github.com/alberto-grl/1bitSDR/blob/3e2e01da0357b38a9badff832c65a185b2fdcaf0/impl1/source/top.v))
- [tarik-hamedovic__sdr-hls](https://github.com/tarik-hamedovic/SDR-HLS) (instantiates [`1.RTLImplementation/1.hw/systemverilog/top.sv`](https://github.com/tarik-hamedovic/SDR-HLS/blob/334f7074eb51dc7d4910a439ba62c85c2668e706/1.RTLImplementation/1.hw/systemverilog/top.sv))

### CORDICDemod I/Q amplitude/frequency/phase demodulator (Amalthea) {#core-amalthea-cordic-demod}

Pipelined multi-iteration CORDIC rotator that converts a streamed I/Q sample into amplitude, frequency and phase output streams; iteration count is parametrised (default 9), with a precomputed CORDIC angle table and gain correction.

| | |
|---|---|
| Repository | [greatscottgadgets__amalthea](https://github.com/greatscottgadgets/amalthea): Amalthea: experimental Amaranth SDR gateware |
| Files | [`amalthea/gateware/demod.py`](https://github.com/greatscottgadgets/amalthea/blob/2d43c7706e2fc2aa581dd58e6348c42cdaf8f230/amalthea/gateware/demod.py), [`amalthea/gateware/stream.py`](https://github.com/greatscottgadgets/amalthea/blob/2d43c7706e2fc2aa581dd58e6348c42cdaf8f230/amalthea/gateware/stream.py) |
| Top module | `CORDICDemod` |
| Language | Python (Amaranth) |
| License | BSD-3-Clause (LICENSE) |
| FPGA / primitives | any: none (portable) |
| Tests | none found (no test_demod.py in tests/; only test_complex.py, test_fft.py, test_fixed_point.py exist) |

**On ULX3S:** Pure Amaranth, no vendor primitives, feeds from an IQStream (amalthea/gateware/stream.py); pairs with amalthea's radio.py IQReceiver (which does use ECP5-only DELAYG/IDDRX1F for the AT86RF215 link, not needed if you supply I/Q another way).

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

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [nicocavallu__rf-sdr-frontend](https://github.com/nicocavallu/rf-sdr-frontend) (instantiates [`modules/rf-dds-lo/sim/dds_top_tb.v`](https://github.com/nicocavallu/rf-sdr-frontend/blob/c0d2e41644aab4f8fa59370ea2f118216810cd25/modules/rf-dds-lo/sim/dds_top_tb.v))

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

### LoRa chirp-spread-spectrum modulator {#core-mehrdadh-lora-chirp}

Parametric LoRa chirp generator: phase accumulator + sin/cos LUT produce upchirp/downchirp/quarter-downchirp I/Q symbols for selectable BW (31.25-500kHz) and SF (6-12); the only LoRa modulator core in the collection.

| | |
|---|---|
| Repository | [mehrdadh__lora-modulator](https://github.com/mehrdadh/lora-modulator): LoRa modulator: chirp-spread-spectrum LoRa TX |
| Files | [`source/rtl/loRaModulator.v`](https://github.com/mehrdadh/lora-modulator/blob/0f1016567d8551649a295c49cdabd43b2a610f74/source/rtl/loRaModulator.v), [`source/rtl/chirpGenerator.v`](https://github.com/mehrdadh/lora-modulator/blob/0f1016567d8551649a295c49cdabd43b2a610f74/source/rtl/chirpGenerator.v), [`source/rtl/accInc.v`](https://github.com/mehrdadh/lora-modulator/blob/0f1016567d8551649a295c49cdabd43b2a610f74/source/rtl/accInc.v), [`source/rtl/phaseInc.v`](https://github.com/mehrdadh/lora-modulator/blob/0f1016567d8551649a295c49cdabd43b2a610f74/source/rtl/phaseInc.v), [`source/rtl/initialPhase.v`](https://github.com/mehrdadh/lora-modulator/blob/0f1016567d8551649a295c49cdabd43b2a610f74/source/rtl/initialPhase.v), [`source/rtl/sinIdeal.v`](https://github.com/mehrdadh/lora-modulator/blob/0f1016567d8551649a295c49cdabd43b2a610f74/source/rtl/sinIdeal.v), [`source/rtl/cosIdeal.v`](https://github.com/mehrdadh/lora-modulator/blob/0f1016567d8551649a295c49cdabd43b2a610f74/source/rtl/cosIdeal.v) |
| Top module | `loraModulator` |
| Language | Verilog |
| License | NC-AGPL-3.0 (custom Non-Commercial AGPL, LICENSE) - not an OSI/permissive license |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** No vendor primitives; portable to ECP5/ULX3S as-is. Only built/tested on ECP5 25F (tinySDR board) via Lattice Diamond; needs a yosys/nextpnr-ecp5 top-level and .lpf for ULX3S.

### rf-sdr-frontend digital downconverter {#core-nicocavallu-sdr-ddc}

Full SDR DDC chain: 2-stage CDC, complex mixer against an 18-bit DDS LO, 3-stage CIC decimate-by-64, 31-tap FIR (Hamming), TPDF dither+truncate to 18-bit signed I/Q. Plain Verilog, no vendor primitives.

| | |
|---|---|
| Repository | [nicocavallu__rf-sdr-frontend](https://github.com/nicocavallu/rf-sdr-frontend): RF-SDR-Frontend: LoRa-dechirp digital downconverter |
| Files | [`src/digital_downconvert.v`](https://github.com/nicocavallu/rf-sdr-frontend/blob/c0d2e41644aab4f8fa59370ea2f118216810cd25/src/digital_downconvert.v), [`src/complex_mixer.v`](https://github.com/nicocavallu/rf-sdr-frontend/blob/c0d2e41644aab4f8fa59370ea2f118216810cd25/src/complex_mixer.v), [`src/cic_filt.v`](https://github.com/nicocavallu/rf-sdr-frontend/blob/c0d2e41644aab4f8fa59370ea2f118216810cd25/src/cic_filt.v), [`src/fir_filter.v`](https://github.com/nicocavallu/rf-sdr-frontend/blob/c0d2e41644aab4f8fa59370ea2f118216810cd25/src/fir_filter.v), [`src/tpdf_dither.v`](https://github.com/nicocavallu/rf-sdr-frontend/blob/c0d2e41644aab4f8fa59370ea2f118216810cd25/src/tpdf_dither.v), [`src/dither_truncate.v`](https://github.com/nicocavallu/rf-sdr-frontend/blob/c0d2e41644aab4f8fa59370ea2f118216810cd25/src/dither_truncate.v), [`src/sdr_frontend_top.v`](https://github.com/nicocavallu/rf-sdr-frontend/blob/c0d2e41644aab4f8fa59370ea2f118216810cd25/src/sdr_frontend_top.v) |
| Top module | `sdr_frontend_top` |
| Language | Verilog |
| License | none found |
| FPGA / primitives | any: none (portable) |
| Tests | sim/sdr_frontend_top_tb.v (iverilog+gtkwave): waveform-only, no PASS/FAIL or assert found |

**On ULX3S:** No board-level Makefile/lpf of its own; only the rf-dds-lo submodule ships an ulx3s.lpf. Sim-only in this clone (iverilog+gtkwave).

### WSPR 4-FSK beacon codec (message/FEC/interleave/symbols/modulator) {#core-whisperice-wspr-codec}

Full WSPR protocol chain: packs callsign/locator/power to bits, convolutional-encodes, interleaves, maps to the 162 4-FSK symbols (with sync vector), then emits a continuous-phase 4-FSK tone stream with exact Bresenham-distributed symbol timing.

| | |
|---|---|
| Repository | [agamez__whisperice](https://github.com/agamez/whisperice): wspr-icebreaker: autonomous VHDL-93 WSPR |
| Files | [`src/wspr/wspr_message.vhd`](https://github.com/agamez/whisperice/blob/970e0802d9e3e5a96c4dfb55adf069bd22555793/src/wspr/wspr_message.vhd), [`src/wspr/wspr_fec.vhd`](https://github.com/agamez/whisperice/blob/970e0802d9e3e5a96c4dfb55adf069bd22555793/src/wspr/wspr_fec.vhd), [`src/wspr/wspr_interleave.vhd`](https://github.com/agamez/whisperice/blob/970e0802d9e3e5a96c4dfb55adf069bd22555793/src/wspr/wspr_interleave.vhd), [`src/wspr/wspr_symbols.vhd`](https://github.com/agamez/whisperice/blob/970e0802d9e3e5a96c4dfb55adf069bd22555793/src/wspr/wspr_symbols.vhd), [`src/wspr/wspr_sync.vhd`](https://github.com/agamez/whisperice/blob/970e0802d9e3e5a96c4dfb55adf069bd22555793/src/wspr/wspr_sync.vhd), [`src/wspr/wspr_modulator.vhd`](https://github.com/agamez/whisperice/blob/970e0802d9e3e5a96c4dfb55adf069bd22555793/src/wspr/wspr_modulator.vhd) |
| Top module | `wspr_modulator` |
| Language | VHDL-93 |
| License | MIT (repo LICENSE; no per-file header) |
| FPGA / primitives | any: none (portable) |
| Tests | make sim (ghdl --std=93): sim/tb_wspr_{message,fec,interleave,symbols,sync,modulator,top}.vhd - self-checking (VHDL asserts, --assert-level=error, Makefile:145) |

**On ULX3S:** Pure VHDL-93, no vendor primitives; only needs a clock and a 1-bit rf_out pin plus external filtering. Built/tested for iCE40UP5K @ 12 MHz but portable to ECP5 at any clock (recompute NCO increments with tools/calculate_nco.py).

## Other catalogued projects

Catalogued repos tagged `dsp` (31), `dsp-sdr` (41) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
