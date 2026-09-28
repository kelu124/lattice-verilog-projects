---
title: "RF and DSP on Lattice survey"
parent: "Methodology"
nav_order: 8
---
<!-- Generated from data/pages/rf-dsp-survey.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# RF and signal-processing gateware on Lattice FPGAs

Survey date: 2026-09-28. Scope: SDR receivers and transmitters, radio front-ends, GNSS, LoRa/ISM, radar, RF test gear (VNA, TDR, signal generators), ultrasound and sonar, lock-in amplifiers, analog capture, on Lattice ECP5 / iCE40 / MachXO2/3 / Nexus. FFT-centred repos were left to the FFT survey.

## Method

- **GitHub repository search API** (no login, `sort=updated`, `per_page=100`, 7–8 s between calls, retried after 30 s on rate-limit errors; other agents were using the same IP, so many calls had to be retried). The queries were:
  - `sdr ecp5`, `sdr ice40`, `sdr ulx3s`, `sdr icebreaker`, `sdr orangecrab`, `sdr lattice`, `sdr colorlight`, `sdr up5k`, `sdr tinyfpga`, `sdr icestorm`, `sdr amaranth`, `sdr litex`, `sdr nmigen`, `iceSDR`
  - `ddc ecp5`, `ddc verilog`, `nco ice40`, `dds ice40`, `dds ecp5`, `cic filter ecp5`, `cic decimator verilog`
  - `radio ice40`, `radio ecp5`, `radio ulx3s`, `radio orangecrab`, `radio upduino`, `radio yosys`, `machxo2 sdr`, `machxo2 radio`, `crosslink-nx`, `ecp5 rf`, `ice40 rf`
  - `fm ice40`, `fm receiver ice40`, `fm transmitter ecp5`, `fm radio fpga`, `am radio fpga`, `ssb fpga`, `fpga direct sampling`, `sdr fpga verilog`, `hackrf`
  - `gnss ice40`, `gnss ecp5`, `gnss fpga`, `gps ecp5`, `gps ice40`, `gps icebreaker`, `gps receiver fpga`, `correlator ice40`
  - `lora ice40`, `lora fpga`, `radar ecp5`, `radar ice40`, `radar fpga verilog`, `fmcw lattice`, `fmcw fpga`
  - `vna ecp5`, `vna ice40`, `vna fpga`, `tdr fpga`, `spectrum analyzer fpga`, `signal generator ice40`, `oscilloscope ice40`, `oscilloscope ecp5`
  - `lock-in ice40`, `lock-in ulx3s`, `lock-in amplifier fpga`, `ultrasound ice40`, `ultrasound ecp5`, `ultrasound up5k`, `ultrasound fpga`, `sonar fpga`
  - `ecp5 adc`, `ice40 adc`, `adc ulx3s`, `ecp5 dsp`, `ice40 dsp`

  These queries returned 523 unique repositories. A name/description filter (lattice, ice40, ecp5, up5k, icebreaker, orangecrab, ulx3s, machxo, colorlight, …) plus a manual pass over the generic-query hits produced the shortlist.

- **Web search** (Hackaday, blogs, CNX, crowd-funding pages) and the owner's `kelu124/awesome-latticeFPGAs` list, used for leads such as iceRadio, 1bitSDR, HackRF Pro, LimeSDR Mini v2, whisperice, the SingularitySurfer lock-in, TART, NUT2NT+, Pico Dev-iCE and ZipCPU/sdr.
- **Evidence check**: for each candidate, a blobless shallow clone (`--depth 1 --filter=blob:none --no-checkout`, in the scratchpad) listed the files, and individual build files were read from `raw.githubusercontent.com`. The part number was taken from the `.ldf`/`.rdf`/iCEcube2 project, the `nextpnr-* --<size>` flags, `board.py` or the LiteX platform. Repos whose only constraints are Xilinx/Altera were excluded.
- **Diff** against `.claude/memory/sources.tsv` (459 rows) and against the `data/catalogue.json` functions `dsp-sdr`, `radio-rx`, `radio-tx`, `fm-transmitter`, `adc`.
- Limits: code search (`filename:*.pcf` plus DSP terms) needs a logged-in `gh`, so it was not run. Star and push dates come from the API on 2026-09-28. `jared-s/icefm` now redirects to `jdspdx/icefm`.

## Already in the collection (RF / signal-processing)

| slug | FPGA | what it is |
|---|---|---|
| mb-sat__ulx3s-longwave-sdr | ECP5 85F (ULX3S) | Longwave SDR receiver with DVI waterfall |
| jamesrosssharp__1_bit_am | ECP5 85F (+ iCE40 target) | 1-bit (comparator) AM receiver and transmitter; derived from alberto-grl/1bitSDR |
| jamesrosssharp__ulx3s_mixer_pcb | ECP5 85F | Mixer PCB + receiver gateware |
| tarik-hamedovic__sdr-hls | LFE5U-85F (Diamond .ldf) | HLS SDR master's thesis on ULX3S |
| nicocavallu__rf-dds-lo / rf-sdr-frontend / fpga-lora-receiver / rf-fft-engine | ULX3S lpf (sim-focused) | DDS LO, SDR front-end, LoRa receiver blocks |
| emard__flearadio | XP2-8E, MachXO2-7000HE | FM receiver built from an RLC network and the on-chip LVDS comparator |
| emard__rdsfpga, f32c__f32c | ECP5 | FM/RDS transmitter |
| emeb__orangecrab_adc | ECP5 25F (OrangeCrab) | ADC + audio FeatherWing for SDR |
| gojimmypi__ulx3s-adda, ulx3s__ulx3s-adda | ECP5 12F | AD/DA board interface ("primitive SDR") |
| kbeckmann__pergola_projects | ECP5 12F | nMigen examples incl. radio-tx |
| hdl4fpga__hdl4fpga | ECP5 12F | Oscilloscope/instrument from ADC |
| emard__ulx3s-misc, pietptr__ulx3s-dsp, semify-eda__waveform-generator, thorkn__spinalsynth_ulx3s | ECP5 | Various DSP / ADC / DAC / waveform experiments |
| blazra__tdr | ECP5-5G SERDES | TDR using the high-speed transceivers |
| cbalint13__e-verest | ECP5 | EVEREST research stick |
| tvelliott__dsp_ice | iCE40 HX8K | STM32F4 + iCE40 SDR development system |
| emeb__up5k_osc, osresearch__up5k, wuxx__icesugar, damdoy__ice40_ultraplus_examples | iCE40 UP5K | Oscilloscope / DSP examples |
| kelu124__un0rick, kelu124__lit3rick | iCE40 HX4K / UP5K | Ultrasound pulse-echo acquisition |
| mebner86__icesugar-pro_sound2fft | ECP5 25F | Audio spectrum (FFT survey's scope) |

## New candidates (not in sources.tsv)

Evidence: **A** = Lattice constraint or project file plus a Lattice build command were found; **B** = Lattice named in the README or code, but the board platform lives outside the repo; **–** = no HDL committed, or not Lattice.

| repo | FPGA / board | application | blocks | HDL | toolchain | license | last push | ★ | evidence / status | cloned? |
|---|---|---|---|---|---|---|---|---|---|---|
| [Makisness/InductIQ](https://github.com/Makisness/InductIQ) | ECP5 85F / **ULX3S** | Lock-in amplifier + impedance sweep (eddy-current coil) | NCO (¼-sine LUT), DDS SPI, lock-in core, ADC SPI, sweep FSM | SystemVerilog/Verilog | apio (`board = ulx3s-85f`), `ulx3s_v20.lpf` | MIT | 2026-09-15 | 1 | A, recommended | no |
| [greatscottgadgets/hackrf](https://github.com/greatscottgadgets/hackrf) (`firmware/fpga`) | iCE40UP5K-SG48 / HackRF Pro | SDR baseband DSP | CIC, FIR, FIR on SB_MAC16, NCO, mixer, quarter-shift, DC block | Amaranth | Amaranth → yosys/nextpnr-ice40 | GPL-2.0 | 2026-09-24 | 8131 | A (`board.py`), recommended | no |
| [ZipCPU/sdr](https://github.com/ZipCPU/sdr) | iCE40UP5K / iCEBreaker + SX1257 PMod | AM/FM/QPSK transmitters and receivers | CIC, subfilter decimators, CORDIC, PLL/quad-PLL, AM/FM demod, IIR, wbscope | Verilog | yosys + nextpnr-ice40, Verilator | none detected | 2024-01-18 | 105 | A (`sdr.pcf`), recommended | no |
| [emeb/rpi_rxadc](https://github.com/emeb/rpi_rxadc) | iCE40UP5K / icehat + rxadc | HF direct-sampling SDR receiver for Raspberry Pi | DDC, NCO tuner, CIC, FIR decimator, I2S / WM8731 | Verilog | icestorm + nextpnr-ice40 | MIT | 2020-07-19 | 36 | A, recommended | no |
| [emeb/iceRadio](https://github.com/emeb/iceRadio) | iCE5LP4K SG48 / iceRadio | HF/VHF SDR receiver | DDC, NCO tuner, CIC, FIR decimator, I2S | Verilog | iCEcube2 (`.project`) + `.pcf` | MIT | 2017-03-22 | 82 | A, recommended | no |
| [emeb/OrangeCrab-Litex-ADC](https://github.com/emeb/OrangeCrab-Litex-ADC) | ECP5 25F / OrangeCrab | LiteX SoC SDR (companion of emeb__orangecrab_adc) | DDC, CIC, FIR, demodulators, CORDIC r2p, DC block | Verilog + LiteX | LiteX/Trellis | MIT | 2020-09-17 | 3 | A (LiteX OrangeCrab target), recommended (GitHub fork flag) | no |
| [alberto-grl/1bitSDR](https://github.com/alberto-grl/1bitSDR) | MachXO2 LCMXO2-7000HE | 1-bit MW/SW AM SDR (+ Cyclone III port) | NCO, mixer, CIC, AM demod | Verilog/VHDL | Lattice Diamond (`.ldf`/`.lpf`) | Apache-2.0 | 2020-05-21 | 110 | A, recommended | no |
| [mehrdadh/lora-modulator](https://github.com/mehrdadh/lora-modulator) | ECP5 LFE5U-25F BG256 / tinySDR | LoRa modulator for AT86RF215 I/Q | chirp generator, phase accumulator, sin/cos LUT, I/Q serialiser | Verilog | Diamond | NOASSERTION | 2025-02-20 | 48 | A, recommended | no |
| [amin005/skywave_SDR](https://github.com/amin005/skywave_SDR) | ECP5 25F CABGA256 / custom AD9226 + USB3300 | Direct-sampling HF SDR over USB 2.0 HS | ADC capture, CIC decimator, own ULPI USB-HS stack | Verilog | yosys + nextpnr-ecp5 | BSD-3-Clause | 2026-07-17 | 0 | A, recommended | no |
| [romavis/lwdo-sdr-fw](https://github.com/romavis/lwdo-sdr-fw) | iCE40HX4K TQ144 / LWDO-SDR | LF/VLF SDR timing receiver | AD7357 ADC pipeline, TDC, PPS, DAC8551, FT245 | Verilog | yosys + nextpnr-ice40 | MIT | 2025-03-25 | 11 | A, recommended | no |
| [nkrackow/SingularitySurfer-FPGA-Lock-In-Amplifier](https://github.com/nkrackow/SingularitySurfer-FPGA-Lock-In-Amplifier) | iCE40UP5K / custom | Lock-in amplifier with LCD | CIC, CORDIC, DDS, IIR (migen), sigma-delta | Verilog (+migen) | nextpnr-ice40 --up5k | MIT | 2023-05-11 | 79 | A, recommended | no |
| [agamez/whisperice](https://github.com/agamez/whisperice) | iCE40UP5K / iCEBreaker + PmodGPS | WSPR beacon transmitter | NCO, 4-FSK modulator, FEC/interleave, GPS/PPS clock calibration | VHDL-93 | ghdl-yosys + nextpnr-ice40 | MIT | 2026-09-28 | 0 | A, recommended | no |
| [MysteriousWolf/VNA_FPGA_DSP](https://github.com/MysteriousWolf/VNA_FPGA_DSP) | iCE40UP5K-SG48I / custom VNA | VNA receiver DSP | RBW filter / detector, ADC counter, measurement RAM | Verilog | Lattice Radiant (`.rdf`, `.pdc`) | none | 2025-03-02 | 0 | A, recommended | no |
| [greatscottgadgets/amalthea](https://github.com/greatscottgadgets/amalthea) | ECP5 + AT86RF215 / Amalthea | Experimental SDR, GNU Radio integration | radio stream, demod, FFT, fixed-point types | Amaranth | LUNA platform (yosys/nextpnr) | BSD-3-Clause | 2023-02-08 | 45 | B (README "Lattice ECP5"; platform in LUNA), recommended | no |
| [cariboulabs/cariboulite](https://github.com/cariboulabs/cariboulite) | iCE40LP1K QN84 / CaribouLite HAT | 6 GHz SDR HAT: I/Q LVDS to RPi SMI bridge | LVDS rx/tx, SMI, complex FIFO (DSP happens in the RF chip) | Verilog | nextpnr-ice40 --lp1k | none detected | 2025-07-24 | 1335 | A, recommended | no |
| [myriadrf/LimeSDR_GW](https://github.com/myriadrf/LimeSDR_GW) | ECP5 45F MG285 / LimeSDR Mini v2 (+ Xilinx boards) | LiteX gateware for LimeSDR | LMS7002M I/Q, FT601, VexRiscv | Verilog/LiteX | LiteX, Diamond default | Apache-2.0 | 2026-09-28 | 22 | A (platform file), candidate | no |
| [myriadrf/LimeSDR-Mini-v2_GW](https://github.com/myriadrf/LimeSDR-Mini-v2_GW) | ECP5 45F MG285 | Official Mini v2 gateware | LMS7002M TRX, FT601, Mico32 | VHDL/Verilog | Diamond | Apache-2.0 | 2024-11-28 | 25 | A, candidate (superseded) | no |
| [mehrdadh/fsk-modulator](https://github.com/mehrdadh/fsk-modulator) | ECP5 25F / tinySDR | BLE/FSK modulator | GFSK, packet memory, PLL | Verilog | Diamond | NOASSERTION | 2025-02-20 | 11 | A, candidate | no |
| [C-Elegans/single_sdr](https://github.com/C-Elegans/single_sdr) | ECP5 45F CABGA381 | One SDR channel | real-to-IQ, IQ decimator, FFT | Chisel + Verilog | nextpnr-ecp5 --45k (no `.lpf`) | none | 2019-10-28 | 1 | A−, candidate | no |
| [chiralhat/fpga-pulses](https://github.com/chiralhat/fpga-pulses) | ECP5-5G 85F, iCE40 HX8K/HX1K | ESR pulse generator | pulse sequencer, PLL | Verilog | nextpnr-ecp5/ice40 | MIT | 2026-05-05 | 2 | A, candidate | no |
| [r4d10n/iCEstick-hacks](https://github.com/r4d10n/iCEstick-hacks) | iCE40HX1K / iCEstick | iCEfm CW FM transmitter | PLL + phase accumulator | Verilog | icestorm | MIT | 2025-11-24 | 18 | A, candidate (tiny) | no |
| [jdspdx/icefm](https://github.com/jdspdx/icefm) (ex jared-s) | iCE40HX1K / iCEstick | FM transmitter PoC | PLL/NCO | SpinalHDL | yosys + nextpnr-ice40 | none | 2020-01-22 | ? | A, candidate (tiny) | no |
| [oshablue/fpga-rs104-up5k](https://github.com/oshablue/fpga-rs104-up5k) | iCE40UP5K SG48 / HDL-0104-RS104 | 4-channel ultrasound NDT sequencing | pulse/one-shot timing, FIFO | Verilog | apio | NOASSERTION | 2020-12-24 | 0 | A, candidate | no |
| [oshablue/fpga-rscpt-up5k](https://github.com/oshablue/fpga-rscpt-up5k) | iCE40UP5K SG48 / HDL-0108-RSCPT | Ultrasound pulser/receiver (NDT) | as above | Verilog | apio | NOASSERTION | 2020-06-01 | 1 | A, candidate | no |
| [totalanni/nilm-monitor](https://github.com/totalanni/nilm-monitor) | ECP5 BG256 | 8-ch 500 kSPS ADC capture (energy monitor) | ADC capture | Verilog | nextpnr-ecp5 | NOASSERTION | 2026-08-05 | 1 | A, low priority | no |
| [Norman-w/fpga-ecp5-sine-wave](https://github.com/Norman-w/fpga-ecp5-sine-wave) | ECP5 25F / Colorlight i5 | DDS sine demo | DDS | Verilog | nextpnr-ecp5 | none | 2025-11-30 | 0 | A, low priority | no |
| [Askelo-Bond/iceStick_nco](https://github.com/Askelo-Bond/iceStick_nco) | iCE40HX1K / iCEstick | NCO over UART | NCO | Verilog | iCEcube2 | none | 2019-02-03 | 0 | A, low priority | no |
| [supriya-penki/lattice_sdr_code](https://github.com/supriya-penki/lattice_sdr_code) | ECP5 (Diamond) | Student SDR FIR | raised-cosine FIR (vendor IP) | Verilog | Diamond | none | 2026-05-09 | 0 | A, low priority | no |
| [frohro/pico-dev-ice](https://github.com/frohro/pico-dev-ice) | iCE40UP5K SG48 / Pico Dev-iCE | HF DDC/DUC transceiver + VNA | (planned) | none yet | pcf + prebuilt `.bin` only | none | 2026-09-28 | 2 | –, watch | no |
| [dpavlin/trilby-hat-fpga](https://github.com/dpavlin/trilby-hat-fpga) | ECP5 45F / Trilby HAT (LTC2226 + TDA18219) | RPi SDR HAT bring-up | blinky, SPI, I2C only | Verilog/SV | nextpnr-ecp5 | none | 2022-01-23 | 2 | A, watch (no DSP) | no |

Excluded after the evidence check: `uw-x/tinysdr` (bitstreams only), `gromas/ecp5r` (hardware only), `kelu124/echomods` (owner's docs; its gateware is already in un0rick/lit3rick), `vankxr/icyradio` (Artix-7), `tmolteno/TART` (Spartan/Zynq), `dawsonjon/FPGA-TX` (Artix-7), `enjoy-digital/litex_m2sdr` (Artix-7), `SchwarzerBlitz/IQModem` (Zybo), `natanvotre/fm-transmitter` (Altera), `BellssGit/FPGA-SDR-FM-RADIO`, `jks-prv/KiwiSDR` (Artix), `ckflight/FMCW3` (Artix), `LaboratoryOfPlasmaPhysics/STicky` (PCB only), `darkstar007/ULX3S_ADC` (README only), `Guilherme-07062002/fpga-lora-bridge` (LiteX SoC driving an RFM95 module; no RF DSP). Audio-only DSP (apfaudio/sandflat, D-elly/Audio-DSP-FPGA, schilkp/PmodADC) was left out.

## Findings

1. **Only one new ULX3S RF/DSP project turned up: Makisness/InductIQ.** It targets the ULX3S-85F through apio and carries its own `ulx3s_v20.lpf`. It combines an NCO, a lock-in core and a sweep engine, and it fills a gap: the collection has no lock-in amplifier on ECP5.
2. **Most open Lattice SDR gateware is on iCE40UP5K:** HackRF Pro, ZipCPU/sdr, rpi_rxadc, the lock-ins, the VNA DSP, WSPR and Pico Dev-iCE. The UP5K's 8 SB_MAC16 blocks and 1 Mbit SPRAM are enough for a narrowband DDC (NCO → mixer → CIC → FIR). These designs are good sources of reusable blocks for a ULX3S port.
3. **emeb (Eric Brombaugh) has a coherent DDC lineage:** iceRadio (iCE5LP4K, 2017) → rpi_rxadc (UP5K, 2020) → OrangeCrab-Litex-ADC (ECP5, 2020). The same `tuner_2`/`cic_dec`/`fir8dec`/`ddc_14` modules run through all three. The collection already has the OrangeCrab hardware repo but not the gateware repos.
4. **The 1-bit SDR family has an upstream outside the collection.** alberto-grl/1bitSDR (MachXO2, Diamond) is the ancestor of jamesrosssharp__1_bit_am and a sibling idea to emard__flearadio. Cloning it closes the lineage.
5. **HackRF Pro has moved from a Xilinx CPLD to an iCE40UP5K running Amaranth DSP** (`firmware/fpga/dsp/{cic,fir,fir_mac16,nco,mixer}.py`, with unit tests). It is the best-maintained open Lattice SDR DSP code found (8.1k★, active 2026-09).
6. **The ECP5 radio platforms mostly use a transceiver chip, so their gateware is plumbing** (I/Q serial links, USB): LimeSDR Mini v2 (LMS7002M), tinySDR and Amalthea (AT86RF215), CaribouLite (iCE40LP1K + AT86RF215). The real DSP is in mehrdadh's LoRa/FSK modulators (tinySDR) and Amalthea's Amaranth demodulators.
7. **Direct-sampling HF on ECP5 without a transceiver chip:** amin005/skywave_SDR (AD9226 + its own ULPI USB-HS stack, BSD-3, 2026) is the notable new one. dpavlin/trilby-hat-fpga never got past bring-up.
8. **Gaps: no open GNSS/GPS correlator, FMCW/pulse radar or LoRa demodulator for Lattice parts was found.** GNSS hits were Xilinx (TART, gnss-m2sdr) or PolarFire. Radar hits were Xilinx/Red Pitaya. The LoRa receiver in the collection (nicocavallu) remains the only one. NUT2NT+ (ECP5 + NT1065) is a commercial board whose gateware was not found on GitHub.
9. **Ultrasound on Lattice outside kelu124's repos:** only the oshablue UP5K NDT demos (rough, 2020).

## Recommended to clone

All have HDL, Lattice evidence and no row in `sources.tsv`. Ordered by relevance to this collection.

1. `Makisness/InductIQ`: ULX3S-85F lock-in/NCO, A-level ULX3S evidence.
2. `greatscottgadgets/hackrf`: for `firmware/fpga` (iCE40UP5K Amaranth CIC/FIR/NCO/mixer). The repo is large, so clone shallow and prune everything outside `firmware/fpga`.
3. `ZipCPU/sdr`: AM/FM/QPSK tx/rx on iCEBreaker, with formally verified blocks.
4. `emeb/rpi_rxadc`: UP5K HF DDC receiver.
5. `emeb/OrangeCrab-Litex-ADC`: ECP5 gateware for the already-cloned emeb__orangecrab_adc.
6. `emeb/iceRadio`: first generation of the emeb DDC (iCE5LP4K, iCEcube2).
7. `alberto-grl/1bitSDR`: MachXO2 upstream of 1_bit_am.
8. `amin005/skywave_SDR`: ECP5 direct-sampling HF + USB-HS.
9. `mehrdadh/lora-modulator`: ECP5 LoRa chirp modulator (tinySDR).
10. `nkrackow/SingularitySurfer-FPGA-Lock-In-Amplifier`: UP5K lock-in (CIC/CORDIC/DDS/IIR).
11. `romavis/lwdo-sdr-fw`: HX4K LF/VLF timing receiver.
12. `agamez/whisperice`: UP5K WSPR transmitter in VHDL through ghdl-yosys.
13. `greatscottgadgets/amalthea`: ECP5 + AT86RF215 Amaranth SDR (B-level evidence).
14. `MysteriousWolf/VNA_FPGA_DSP`: UP5K VNA DSP (Radiant).
15. `cariboulabs/cariboulite`: iCE40LP1K SDR HAT, a popular reference for I/Q LVDS↔SMI.

Next in line: `myriadrf/LimeSDR_GW`, `mehrdadh/fsk-modulator`, `C-Elegans/single_sdr`, `chiralhat/fpga-pulses`. Watch: `frohro/pico-dev-ice` (its HDL is not published yet).

Before cloning, check free disk space: `/` was 94 % full (13 GB free) on 2026-09-28. HackRF and LimeSDR_GW are the only large repos in this list.
{% endraw %}
