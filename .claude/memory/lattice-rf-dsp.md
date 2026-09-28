---
name: lattice-rf-dsp
description: What open RF / signal-processing / FFT gateware exists on Lattice FPGAs (surveys 2026-09-28) — best cores, gaps (no GNSS/radar/LoRa demod), where each lineage comes from
metadata:
  type: project
---

Surveys 2026-09-28: `data/pages/rf-dsp-survey.json` (≈75 queries, 15 repos cloned) and `data/pages/fft-survey.json`
(57 queries, 14 repos + ZipCPU dblclockfft cloned); all catalogued, cores in `data/cores.json` functions `radio`/`dsp`.
- **Most open Lattice SDR DSP is iCE40 UP5K**: HackRF Pro `firmware/fpga` (Amaranth CIC/FIR/NCO/mixer, numpy-tested,
  BSD-3), ZipCPU/sdr (AM/FM/QPSK, CORDIC), emeb rpi_rxadc; lock-ins (nkrackow SingularitySurfer, Makisness InductIQ =
  the only new **ULX3S** RF design, apio `ulx3s-85f`), VNA DSP (MysteriousWolf), WSPR TX (agamez whisperice, VHDL,
  self-checking GHDL).
- **ECP5**: amin005 skywave_SDR (AD9226 → CIC → own ULPI USB2-HS, BSD-3, self-checking tbs), emeb OrangeCrab-Litex-ADC
  (gateware behind emeb__orangecrab_adc), mehrdadh lora-modulator (tinySDR, NC-AGPL non-commercial), GSG amalthea
  (Amaranth FFT + CORDIC demod, board def via LUNA), nicocavallu rf-sdr-frontend (DDS mixer → CIC/64 → 31-tap FIR).
- **Lineages**: emeb iceRadio (iCE5LP4K) → rpi_rxadc (UP5K) → OrangeCrab-Litex-ADC (ECP5); alberto-grl 1bitSDR
  (MachXO2, Diamond) → jamesrosssharp 1_bit_am (ULX3S); ZipCPU dblclockfft generator → mb-sat longwave SDR, C-Elegans single_sdr.
- **FFT**: iCE40 designs are small or sliding (mattvenn sdft, Goertzel); 1024+ only ipmgroup fftd (HX4K) and
  ox-computing (2048-pt BFP + Welch, ECP5-5G EVN). ECP5 pattern: 256/512-pt FFT → spectrum/waterfall display
  (gage1999 iCESugar-Pro, mebner86 sound2fft). vyges FFT IP (256–4096, iCE40/ECP5 open flows) has broken cocotb paths.
- **Gaps**: no open Lattice GNSS correlator, FMCW/pulse radar or LoRa *demodulator*; nothing on MachXO2/3 (except 1bitSDR)
  or CrossLink-NX/Certus-NX. nicocavallu fpga-lora-receiver has no HDL and rf-fft-engine's FFT files are empty stubs.

**How to apply:** for RF/DSP requests start from these cores; say clearly which are iCE40-only (SB_MAC16 mixers) and which
are license-restricted (lora-modulator NC). See [[reusable-cores]], [[ecp5-serdes-storage]].
