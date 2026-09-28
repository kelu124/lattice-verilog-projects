---
title: "FFT on Lattice survey"
parent: "Methodology"
nav_order: 3
---
<!-- Generated from data/pages/fft-survey.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# FFT gateware on Lattice FPGAs

Survey date: **2026-09-28**. Scope: open FFT gateware and closely related designs (sliding DFT, Goertzel,
spectrum analyzers, spectrogram/waterfall, FFT-based audio/SDR) that target Lattice FPGAs
(ECP5, iCE40 UP5K/HX/LP, MachXO2/3, CrossLink-NX/Certus-NX).

## Method

1. **Local scan** of `original_sources/` (494 clones on 2026-09-28, some added by a parallel session):
   `grep -rliE "fft|butterfly|radix-?2|twiddle"` over `*.v *.sv *.vhd *.vhdl *.py *.si *.hs *.scala`
   (`.git` excluded), then each hit checked by hand to drop false positives (`butterflylogic`
   in lawrie/ice40logicsniffer, `fftw`/`numpy.fft` in host scripts, etc.).
2. **GitHub search API** (`/search/repositories`, unauthenticated, `sort=updated`, 7–10 s sleeps,
   retried after rate-limit errors). 57 queries:
   - by name/description: `fft ice40`, `fft ecp5`, `fft icebreaker`, `fft ulx3s`, `fft upduino`,
     `fft lattice`, `fft machxo2`, `fft machxo3`, `fft crosslink-nx`, `fft certus`,
     `fft verilog lattice`, `fft orangecrab`, `fft colorlight`, `fft icestick`, `fft tinyfpga`,
     `fft fomu`, `fft icesugar`, `fft yosys`, `fft nextpnr`, `spectrum analyzer ecp5`,
     `spectrum analyzer ice40`, `spectrum analyzer fpga lattice`, `spectrum analyzer icebreaker`,
     `spectrogram fpga`, `spectrogram ice40`, `waterfall fpga sdr`, `sdr ice40`, `sdr ecp5`,
     `fft amaranth`, `fft litex`, `fft fpga audio`, `dblclockfft`, `fft butterfly verilog`,
     `fft radix-2 fpga`, `fft spinalhdl`, `sliding dft fpga`, `goertzel fpga`;
   - README-scoped (`in:readme`): `fft ice40`, `fft ecp5`, `fft icebreaker`, `fft ulx3s`,
     `fft upduino`, `fft nextpnr`, `fft machxo2`, `fft crosslink`, `fft orangecrab`,
     `fft colorlight`, `fft iCE40UP5K`, `spectrum analyzer ice40`, `spectrum analyzer ecp5`,
     `spectrum ulx3s`, `fft tinyfpga`, `fft icestick`, `fft apio`, `waterfall ecp5`,
     `fft lattice fpga`, `spectrum icebreaker`.
     ~420 unique repos returned; the vast majority are Xilinx/Intel class projects, ASIC flows or
     unrelated ("lattice" in physics/cryptography).
3. **Web search** (hackaday/blog/GitHub topics): added `almighty-bungholio/fpga-fft`
   (= old name of `mattvenn/fpga-sdft`, same tree), `yoonisi/R2FFT`, `nanamake/r22sdf`,
   `ZipCPU/sdr`, `ZipCPU/fftdemo`, `damdoy/ice40_ultraplus_examples`.
4. **Evidence check** for ~50 plausible candidates: tarball listing from `codeload.github.com`
   (no API quota) searched for (a) an HDL FFT/DFT/Goertzel file and (b) Lattice build evidence:
   `.pcf`/`.lpf`/`.pdc`/`apio.ini`/Radiant `.rdf`/`.sty`, `nextpnr-ice40|ecp5`, `synth_ice40|ecp5`,
   `icepack`/`ecppack`, a LiteX/Amaranth Lattice platform. README/Makefile excerpts fetched from
   `raw.githubusercontent.com` to confirm device and FFT size.
5. **Diff** against `.claude/memory/sources.tsv` (working-tree version, 2026-09-28).

Limits: no code search (needs auth, e.g. `filename:*.pcf fft`); core API quota was exhausted by
parallel sessions, so stars/push dates come from search results (snapshot 2026-09-28).
"License: none" means GitHub detected no license file (not verified by reading the tree).

## FFT cores already in the collection

| Repo (clone) | FFT file(s) | What it is | Target FPGA (catalogue / source) | Catalogued? |
|---|---|---|---|---|
| `mebner86__icesugar-pro_sound2fft` | `rtl/fft256.v`, `rtl/fft_real512.v`, `projects/06_live_fft`, `07_live_real_fft`, `13_fft_uart` (+`gen_twiddle.py`) | 256-point radix-2 DIT complex FFT, real-512 wrapper (`localparam N = 256`), magnitude output to HDMI spectrum display; cocotb bit-exact vs numpy | ECP5 LFE5U-25F CABGA256 (iCESugar-Pro), yosys/nextpnr-ecp5 | yes; `data/cores.json` id `mebner86-fft256` (`dsp`) |
| `mb-sat__ulx3s-longwave-sdr` | `logic/ulx3s-stream-verilog/fft-core/*` (`fftmain.v`, `butterfly.v`, `hwbfly.v`, `qtrstage.v`, `laststage.v`, `bitreverse.v`, `cmem_*.hex`) | ZipCPU **dblclockfft**-generated pipelined FFT, 512-point, 16-bit in/out; longwave SDR spectrum | ECP5 85F (`nextpnr-ecp5 --85k`), ULX3S | yes (repo); no `cores.json` entry for the FFT |
| `nicocavallu__rf-fft-engine` | `src/radix2_fft.v`, `ping_pong_buffer.v`, `peak_finder.v` | Iterative radix-2, 128-point, single butterfly reused over 7 stages, twiddle ROM; LoRa SF7 de-chirp peak finder | ULX3S LFE5U-85F (README) | cloned (uncommitted in sources.tsv), **not yet catalogued** |
| `ckdur__riscvconsole` | `hardware/riscvconsole/src/main/resources/versatile_fft/*.vhd` + `devices/fft/fft.scala` | Chipyard/RocketChip SoC with an FFT MMIO peripheral wrapping W. Zabołotny's opencores **versatile_fft** (VHDL, `LOG2_FFT_LEN = 10` → 1024-point) | multi-board incl. `fpga/ULX3S` (Chipyard `SUB_PROJECT=ulx3s`) | cloned, **not yet catalogued** |
| `kelu124__lit3rick` | `verilog/sigprocessing/code_fourrier/rtl/dft*.v` | Windowed (non-overlapped) sliding-DFT core, `CORE_DFT_N = 16`, twiddle ROM, complex abs/sqrt | iCE40UP5K (Lattice Radiant project `verilog/radiant/fft_adc`) | cloned, **not in catalogue.json** (non-ULX3S board) |
| `pietptr__ulx3s-dsp` | `fft/Main.hs`, `Recursive.hs`, `TowardsHW.hs` (Clash) | Clash (Haskell) FFT experiments → generated Verilog; host plot scripts | ECP5 85F, ULX3S | yes (`dsp-sdr`) |
| `mit-plv__koika` | `examples/fft.v` (Kôika source), `examples/fft.v.etc/mkfft.v` | Kôika rule-based FFT example compiled to Verilog; not board-specific | unknown (generic example; repo has a ULX3S RV target) | yes |
| `tarik-hamedovic__sdr-hls` | only Python notebooks (`numpy.fft`) | No HDL FFT; SDR CIC/CORDIC in HLS | ECP5 85F (Diamond) | yes |
| `tvelliott__dsp_ice` | `firmware/bh_fft_win.c` | FFT runs on the STM32F4 (CMSIS-DSP); FPGA only captures ADC data | iCE40 HX8K | yes |

False positives dropped: `lawrie__ice40logicsniffer` (`butterflylogic` vendor name), `fpgawars__flix-v`,
`machdyne__zeitlos`, `kelu124__un0rick`, `emeb__orangecrab_adc`, `mkvenkit__learn_fpga`,
`google__cfu-playground`, `kholia__colorlight-5a-75b`, `hdl4fpga__hdl4fpga`, `gonsolo__borg`,
`jderobot__fpga-robotics`, `im-tomu__fomu-workshop` (host-side numpy/kissfft or unrelated identifiers).

## New candidates (not in sources.tsv)

Status: **R** = recommended to clone; **rel** = related, lower priority; **no** = no Lattice evidence or no gateware FFT.

| Repo | FPGA / board | FFT size / architecture | HDL | License | Last push | ★ | Lattice evidence | Status |
|---|---|---|---|---|---|---|---|---|
| [ipmgroup/fftd](https://github.com/ipmgroup/fftd) | iCE40HX4K, Trenz ICEZero (RPi HAT) | 1024-pt radix-2 DIT (param), Q1.15, block floating point; SPI + Linux driver + libfft | Verilog | MIT | 2026-06-04 | 2 | `hardware/synth/fft_top.pcf`, icestorm Makefile | R |
| [mattvenn/fpga-sdft](https://github.com/mattvenn/fpga-sdft) | iCE40 HX1K (icestick) / HX8K | Sliding DFT, twiddle ROM, python model | Verilog | none | 2020-04-24 | 76 | `hdl/icestick.pcf`, `hdl/8k.pcf`, Makefile | R |
| [Gage1999/fpga-sdr-receiver](https://github.com/Gage1999/fpga-sdr-receiver) | ECP5-25F iCESugar-Pro (+ PlutoSDR) | `fft256.sv` + butterfly/twiddle ROM → spectrum + waterfall on 800×480 LCD | SystemVerilog | MIT | 2026-09-08 | 0 | `icesugar_pro/top.lpf`, Makefile | R |
| [C-Elegans/single_sdr](https://github.com/C-Elegans/single_sdr) | ECP5 LFE5U-45F CABGA381 | dblclockfft 256-pt (generated), SpinalHDL BlackBox + IQ decimator | SpinalHDL/Verilog | none | 2019-10-28 | 1 | `nextpnr-ecp5 --45k` in Makefile, `MULT18X18D` | R |
| [fulig/TinyFPGA_FFT](https://github.com/fulig/TinyFPGA_FFT) | iCE40LP8K, TinyFPGA-BX | Full 8-point FFT + single-butterfly-stage variant, SPI out | Verilog | none | 2022-08-29 | 0 | `apio.ini`, `pins.pcf` | R |
| [alhusseingamal/r2sdf-fft](https://github.com/alhusseingamal/r2sdf-fft) | iCE40 HX8K | Radix-2 DIF SDF streaming, N-point (8-pt checked in), bit-accurate python model | Verilog | none | 2026-09-22 | 0 | `fpga/LatticeiCE40HX8K.pcf`, Makefile | R |
| [MaxZischka1/FastFourierTransformProject](https://github.com/MaxZischka1/FastFourierTransformProject) | iCE40UP5K | Radix-2 SDF pipeline (SDFCell, SBM16), UART I/O, Verilator tb | SystemVerilog | none | 2026-09-28 | 0 | Makefile `synth_ice40`, `nextpnr-ice40 --up5k`, `top.asc` | R |
| [DylanSebastianHeredia/E155_Tuner_Project](https://github.com/DylanSebastianHeredia/E155_Tuner_Project) | iCE40UP5K, UPduino v3.1 (+STM32L432) | 512-pt 16-bit fixed-point FFT (AGU/control unit/butterfly) → pitch detection | SystemVerilog | none | 2025-12-08 | 1 | Lattice Radiant (README); no constraint file seen at root | R (README-level evidence) |
| [Hariharan6307-coder/verilog-goertzel-audio-visualizer](https://github.com/Hariharan6307-coder/verilog-goertzel-audio-visualizer) | iCE40UP5K | 8 parallel Goertzel bands, peak-hold, log bar scaler | Verilog | none | 2026-07-30 | 0 | `apio.ini` | R |
| [ox-computing/Real-Time-Analytics-FPGA](https://github.com/ox-computing/Real-Time-Analytics-FPGA) | iCE40UP5K-SG48 (+ ECP5 lpf) | 2048-pt integer FFT, Hann, Welch PSD, BFP exponent (spectral features for ML) | SystemVerilog | Apache-2.0 | 2026-08-31 | 0 | `rtl/constraints/UP5K/*.pcf`, `ECP5/*.lpf`, Radiant power reports | R |
| [vyges/fast-fourier-transform-ip](https://github.com/vyges/fast-fourier-transform-ip) | generic; open flow for iCE40 HX8K/UP5K, ECP5 | Pipelined radix-2 DIF, configurable, TL-UL/APB control | SystemVerilog | Apache-2.0 | 2026-08-08 | 7 | `flow/fpga/openfpga/constraints/hx8k-ct256.pcf`, nextpnr flow | R (mirror: vyges-ip/…) |
| [enjoy-digital/litedsp](https://github.com/enjoy-digital/litedsp) | generic LiteX; impl flow on ECP5 LFE5UM5G-85F | `LiteDSPFFT` radix-2 SDF (+inverse), iterative FFT, parallel FFT, PSD/Welch, Goertzel, PFB channelizer | Migen/LiteX (Python) | BSD-2-Clause (SPDX in files) | 2026-09-24 | 15 | `impl/ecp5.py` (synth_ecp5 + nextpnr-ecp5) | R |
| [meharbaan2/systemverilog-ofdm-phy-core](https://github.com/meharbaan2/systemverilog-ofdm-phy-core) | iCE40UP5K SG48 (synth estimate) | `ofdm_fft64.sv` 64-pt FFT/IFFT in an OFDM PHY | SystemVerilog | none | 2026-06-10 | 1 | `synth/run_synth.sh` (synth_ice40, nextpnr-ice40 --up5k) | R (synthesis only, no board) |
| [pat-pgt/MultiFrequenciesDetector](https://github.com/pat-pgt/MultiFrequenciesDetector) | iCE40 / ECP5 (Makefile targets) | Time → logarithmic-frequency converter (log-spaced bins, "polyphase-FFT-like") | VHDL (GHDL) | AGPL-3.0 | 2026-09-24 | 4 | `VHDL/Makefile` (nextpnr-ice40, nextpnr-ecp5) | R (related) |
| [kazkojima/tinyfft-fpga](https://github.com/kazkojima/tinyfft-fpga) | none stated (author's radio display) | VFFT fixed-point FFT, Amaranth | Amaranth | BSD-2-Clause | 2023-01-23 | 3 | none (5 files, no platform) | rel |
| [ZipCPU/dblclockfft](https://github.com/ZipCPU/dblclockfft) | generic generator | Pipelined FFT generator (C++ → Verilog) | C++/Verilog | none detected (GPL/LGPL per headers, unverified) | 2024-04-18 | 267 | none in repo; **used on ECP5** by mb-sat/ulx3s-longwave-sdr and C-Elegans/single_sdr | rel (upstream of cloned core) |
| [ZipCPU/sdr](https://github.com/ZipCPU/sdr) | iCE40UP5K iCEBreaker | SDR (AM/FM/…); no FFT RTL found | Verilog | none | 2024-01-18 | 105 | `rtl/sdr.pcf`, `gdr.pcf` | rel (SDR, not FFT) |
| [ZipCPU/fftdemo](https://github.com/ZipCPU/fftdemo) | simulation / Xilinx | Spectrogram demo with dblclockfft | Verilog | none | 2024-04-15 | 48 | none | no |
| [frohro/pico-dev-ice](https://github.com/frohro/pico-dev-ice) | iCE40UP5K-SG48 + RPi Pico | README claims "FPGA-accelerated FFTs"; only DDC/CIC RTL found, FFT RTL not found | Verilog/C | none | 2026-09-28 | 2 | `fpga/ddc_sdr.pcf` | rel (recheck later) |
| [amin005/skywave_SDR](https://github.com/amin005/skywave_SDR) | ECP5 + AD9226 + USB3300 | FFT only host-side (`adc_analyze.py`) | Verilog | BSD-3-Clause | 2026-07-17 | 0 | `fpga/usb_adc_hs.lpf` | rel (SDR front-end, no FFT) |
| [romavis/lwdo-sdr-fw](https://github.com/romavis/lwdo-sdr-fw) | iCE40 | LF/VLF SDR, no FFT | Verilog | MIT | 2025-03-25 | 11 | `fpga/top.pcf` | rel (SDR, no FFT) |
| [dpavlin/trilby-hat-fpga](https://github.com/dpavlin/trilby-hat-fpga) | ECP5 Trilby HAT | SDR, no FFT | SystemVerilog | none | 2022-01-23 | 2 | `trilby.lpf` | rel (SDR, no FFT) |
| [NizarZar/FFT-Lattice](https://github.com/NizarZar/FFT-Lattice) | unknown | README: "FFT Engine not implemented yet" | SV/Verilog | none | 2026-03-06 | 0 | none | no |
| [damdoy/ice40_ultraplus_examples](https://github.com/damdoy/ice40_ultraplus_examples) | iCE40UP5K | DSP (SB_MAC16) examples, no FFT | Verilog | MPL-2.0 | 2024-02-11 | 301 | `common/io.pcf` | no (no FFT) |
| [nanamake/r22sdf](https://github.com/nanamake/r22sdf) | generic | Radix-2² SDF pipelined FFT (64/128/1024) | Verilog | MIT | 2019-04-14 | 177 | none (reused by 7echkilla on Quartus) | no (generic, portable) |
| [yoonisi/R2FFT](https://github.com/yoonisi/R2FFT) | generic | Radix-2 in-place FFT w/ BFP | SystemVerilog | BSD-3-Clause | 2019-04-30 | 22 | none | no (generic, portable) |
| [4fr1n/radix-2-fft-verilog](https://github.com/4fr1n/radix-2-fft-verilog) | unknown | Iterative in-place radix-2 | Verilog | MIT | 2026-06-23 | 0 | none | no |
| [wswslzp/SpinalFFT](https://github.com/wswslzp/SpinalFFT) | generic | SpinalHDL FFT generator | SpinalHDL | none | 2020-05-24 | 8 | none | no |
| [kamejoko80/litex-pdm2pcm](https://github.com/kamejoko80/litex-pdm2pcm) | iCE40 icestick (LiteX platform) | PDM→PCM only, no FFT | LiteX | MIT | 2023-09-15 | 9 | `custom_boards/platforms/icestick.py` | no (no FFT) |
| [LodeStarCyber/GNU-Radio-FM-Radio-FFT](https://github.com/LodeStarCyber/GNU-Radio-FM-Radio-FFT) | — | GNU Radio flowgraph (Python) | Python | none | 2025-10-26 | 0 | none | no |
| [SouzaLuisH/goertzel_spectrum_analyser_FPGA](https://github.com/SouzaLuisH/goertzel_spectrum_analyser_FPGA) | unknown | Goertzel spectrum analyser | unknown | none | 2026-05-14 | 0 | tarball download failed (empty repo?) | unknown |

Other hits (Basys3/Artix-7, Zynq, Cyclone/DE-series, Gowin, ASIC-only): e.g. ZakriyaParacha46,
rparysz/FFT_FPGA, delhatch/Spectrum, filipamator/vu_meter, 7echkilla/live-concert-vfx (Quartus),
leoo-c1/FPGA-Audio-Visualiser (Intel FFT IP), hukenovs/intfftk (Xilinx), watermeko/FFTonRiscV (Gowin),
vankxr/icyradio (Artix-7 A200T), mhbbParsa/acoustic_camera (Vivado), jduanen/Acoustic-Camera — **no Lattice evidence**, excluded.

## Findings

- Open FFT gateware on Lattice is **rare and mostly small**: iCE40 designs are 8–64-point or
  iterative/sliding DFTs because of the few BRAMs and 8 SB_MAC16s; only ipmgroup/fftd (HX4K, 1024-pt,
  BFP) and ox-computing (UP5K, 2048-pt Welch) do large transforms, both via iterative in-place
  architectures using EBR/SPRAM.
- On **ECP5** the recurring pattern is a 256/512-point FFT driving a spectrum/waterfall display
  (mebner86 sound2fft, Gage1999 SDR, mb-sat longwave SDR, C-Elegans single_sdr). Two of those four
  use ZipCPU **dblclockfft**-generated cores, which have no Lattice build in their own repo.
- **Nothing found for MachXO2/3, CrossLink-NX or Certus-NX**: `fft machxo2/3`, `fft crosslink-nx`,
  `fft certus` returned 0 repo hits; readme searches only surfaced unrelated physics/biology repos.
- Reusable, board-agnostic FFT libraries with a Lattice open flow: **enjoy-digital/litedsp**
  (LiteX, ECP5 implementation flow, broad DSP incl. PSD/Welch/Goertzel/PFB) and
  **vyges/fast-fourier-transform-ip** (iCE40/ECP5 open flow). Good `dsp` core candidates for `cores.json`.
- Already-cloned but uncatalogued FFT cores: `nicocavallu__rf-fft-engine` (ULX3S, 128-pt),
  `ckdur__riscvconsole` (versatile_fft 1024-pt peripheral, ULX3S) and `kelu124__lit3rick` (UP5K DFT).
  They should get `dsp` rows in `cores.json` when catalogued.
- Candidate core rows for `data/cores.json` from existing clones: dblclockfft 512-pt in
  mb-sat/ulx3s-longwave-sdr (`fft-core/fftmain.v`), versatile_fft in ckdur/riscvconsole,
  radix2_fft in nicocavallu/rf-fft-engine, `dft_core` in kelu124/lit3rick.
- Evidence gaps: DylanSebastianHeredia (Radiant project stated in README, no constraint file at root
  seen), meharbaan2 (synthesis-only estimate, no board), pat-pgt (Makefile targets only).

## Recommended to clone

All have an HDL FFT/DFT/Goertzel file **and** a Lattice build artefact, and none is in `sources.tsv`:

1. ipmgroup/fftd — iCE40HX4K ICEZero, 1024-pt radix-2 + Linux driver
2. mattvenn/fpga-sdft — iCE40 HX1K/HX8K sliding DFT (most-starred Lattice FFT repo, 76★)
3. Gage1999/fpga-sdr-receiver — ECP5-25F iCESugar-Pro, fft256 spectrum/waterfall SDR
4. C-Elegans/single_sdr — ECP5-45F, dblclockfft 256-pt SDR channel (SpinalHDL)
5. fulig/TinyFPGA_FFT — TinyFPGA-BX (iCE40LP8K), 8-pt FFT + single-stage variant
6. alhusseingamal/r2sdf-fft — iCE40HX8K radix-2 SDF with bit-accurate model
7. MaxZischka1/FastFourierTransformProject — iCE40UP5K radix-2 SDF
8. DylanSebastianHeredia/E155_Tuner_Project — UPduino v3.1 (UP5K), 512-pt FFT tuner (Radiant)
9. Hariharan6307-coder/verilog-goertzel-audio-visualizer — UP5K 8-band Goertzel visualizer
10. ox-computing/Real-Time-Analytics-FPGA — UP5K 2048-pt FFT / Welch PSD
11. vyges/fast-fourier-transform-ip — configurable FFT IP with iCE40/ECP5 open flow
12. enjoy-digital/litedsp — LiteX DSP library with FFT/PSD, ECP5 impl flow
13. meharbaan2/systemverilog-ofdm-phy-core — 64-pt FFT OFDM PHY, UP5K synthesis
14. pat-pgt/MultiFrequenciesDetector — log-frequency spectrum (VHDL), nextpnr-ice40/ecp5 targets

Optional (no Lattice build in repo, but upstream of cloned code): ZipCPU/dblclockfft.

Sources: GitHub search API (2026-09-28); web search results incl.
[almighty-bungholio/fpga-fft](https://github.com/almighty-bungholio/fpga-fft),
[frohro/pico-dev-ice](https://github.com/frohro/pico-dev-ice),
[yoonisi/R2FFT](https://github.com/yoonisi/R2FFT),
[damdoy/ice40_ultraplus_examples](https://github.com/damdoy/ice40_ultraplus_examples),
[tvelliott/dsp_ice](https://github.com/tvelliott/dsp_ice).
{% endraw %}
