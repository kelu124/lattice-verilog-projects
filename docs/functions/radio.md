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
| [1-bit AM transceiver chain (ULX3S-proven)](#core-jamesrosssharp-1bit-am) ★ | [jamesrosssharp__1_bit_am](https://github.com/jamesrosssharp/1_bit_AM) | Verilog | MIT (LICENSE.txt) | ECP5 | 2 |
| [CORDICDemod I/Q amplitude/frequency/phase demodulator (Amalthea)](#core-amalthea-cordic-demod) | [greatscottgadgets__amalthea](https://github.com/greatscottgadgets/amalthea) | Python (Amaranth) | BSD-3-Clause | any | 0 |
| [DDS local oscillator](#core-nicocavallu-dds-lo) | [nicocavallu__rf-dds-lo](https://github.com/nicocavallu/rf-dds-lo) | Verilog | none found | any | 1 |
| [FM stereo transmitter with RDS](#core-emard-fm-rds) | [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc) | VHDL | BSD (`-- (c) Marko Zec` / `-- LICENSE=BSD` on… | any | 2 |
| [LoRa chirp-spread-spectrum modulator](#core-mehrdadh-lora-chirp) | [mehrdadh__lora-modulator](https://github.com/mehrdadh/lora-modulator) | Verilog | NC-AGPL-3.0 | any | 0 |
| [rf-sdr-frontend digital downconverter](#core-nicocavallu-sdr-ddc) | [nicocavallu__rf-sdr-frontend](https://github.com/nicocavallu/rf-sdr-frontend) | Verilog | none found | any | 0 |
| [Standalone RDS DBPSK modulator](#core-emard-rdsfpga-rds) | [emard__rdsfpga](https://github.com/emard/rdsfpga) | VHDL | BSD in headers | any | 0 |
| [Superheterodyne AM/FM receive chain with per-block testbenches](#core-jamesrosssharp-mixer-pcb-superhet) | [jamesrosssharp__ulx3s_mixer_pcb](https://github.com/jamesrosssharp/ulx3s_mixer_pcb) | Verilog | MIT (hdl/LICENSE.txt) | ECP5 | 4 |
| [WSPR 4-FSK beacon codec (message/FEC/interleave/symbols/modulator)](#core-whisperice-wspr-codec) | [agamez__whisperice](https://github.com/agamez/whisperice) | VHDL-93 | MIT (repo LICENSE; no per-file header) | any | 0 |
| [CORDIC-1 bit-serial CORDIC/DDS sine engine](#core-joaln27-cordic) | [joaln27__cordic](https://github.com/joaln27/CORDIC) | SystemVerilog | Apache-2.0 | ECP5 | 11 |
| [Digital down-converter + AM/FM demod chain (post-ADC)](#core-emeb-orangecrab-adc-ddc) | [emeb__orangecrab_adc](https://github.com/emeb/orangecrab_adc) | Verilog | none found | any | 3 |
| [Gage1999/fpga-sdr-receiver 256-pt iterative radix-2 FFT](#core-gage1999-fft256-iterative) | [gage1999__fpga-sdr-receiver](https://github.com/Gage1999/fpga-sdr-receiver) | SystemVerilog | MIT (LICENSE) | any | 1 |
| [HackRF Amaranth CIC/FIR/NCO/mixer DSP chain](#core-hackrf-amaranth-dsp-chain) | [greatscottgadgets__hackrf](https://github.com/greatscottgadgets/hackrf) | Python (Amaranth) | BSD-3-Clause | iCE40 | 0 |
| [ZipCPU SDR CORDIC + CIC + AM/FM demodulator chain](#core-zipcpu-sdr-cordic-demod) | [zipcpu__sdr](https://github.com/ZipCPU/sdr) | Verilog | GPL-3.0-or-later | any | 2 |

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

**Used by 2 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [alberto-grl__1bitsdr](https://github.com/alberto-grl/1bitSDR) (instantiates [`SDR_CycloneIII/am_receiver.sv`](https://github.com/alberto-grl/1bitSDR/blob/3e2e01da0357b38a9badff832c65a185b2fdcaf0/SDR_CycloneIII/am_receiver.sv))
- [jamesrosssharp__ulx3s_mixer_pcb](https://github.com/jamesrosssharp/ulx3s_mixer_pcb) (instantiates [`hdl/impl/ulx3s/top.v`](https://github.com/jamesrosssharp/ulx3s_mixer_pcb/blob/ec6d9fc0a8a5f6a189793a2a2638159c5705db75/hdl/impl/ulx3s/top.v))

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

**Used by 4 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [alberto-grl__1bitsdr](https://github.com/alberto-grl/1bitSDR) (instantiates [`SDR_CycloneIII/am_receiver.sv`](https://github.com/alberto-grl/1bitSDR/blob/3e2e01da0357b38a9badff832c65a185b2fdcaf0/SDR_CycloneIII/am_receiver.sv))
- [enjoy-digital__litedsp](https://github.com/enjoy-digital/litedsp) (instantiates [`impl/modules.py`](https://github.com/enjoy-digital/litedsp/blob/102e415425f60ba21b59972660d56c649612c080/impl/modules.py))
- [gage1999__fpga-sdr-receiver](https://github.com/Gage1999/fpga-sdr-receiver) (instantiates [`icesugar_pro/src/top.sv`](https://github.com/Gage1999/fpga-sdr-receiver/blob/f112a4c5f1d7769cb46d2b6fedbe32aefdd715aa/icesugar_pro/src/top.sv))
- [jamesrosssharp__1_bit_am](https://github.com/jamesrosssharp/1_bit_AM) (instantiates [`impl/ulx3s/top.v`](https://github.com/jamesrosssharp/1_bit_AM/blob/ce7e9fcc70fd98d23083b7ae7ae43111528c0e87/impl/ulx3s/top.v))

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

## Other catalogued projects

Catalogued repos tagged `radio-tx` (9), `radio-rx` (15), `fm-transmitter` (1), `dsp-sdr` (41) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
