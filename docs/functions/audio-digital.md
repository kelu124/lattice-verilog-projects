---
title: "I2S and S/PDIF"
parent: "Cores by function"
nav_order: 24
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# I2S and S/PDIF

Digital audio interfaces: I2S, S/PDIF, PDM microphones.

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [I2S audio interface (ulx3s-misc)](#core-emard-ulx3s-misc-i2s) ★ | [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc) | VHDL (wrapper), Verilog | BSD (`-- AUTHOR=EMARD` / `-- LICENSE=BSD` header) | any | 1 |
| [I2S receiver (orangecrab-usb)](#core-orangecrab-usb-i2s-rx) | [mangelajo__orangecrab-usb](https://github.com/mangelajo/orangecrab-usb) | Verilog | none found | any | 0 |
| [I2S RX/TX + PDM/CIC mic front-end (sound2fft)](#core-icesugar-pro-i2s-pdm) | [mebner86__icesugar-pro_sound2fft](https://github.com/mebner86/icesugar-pro_sound2fft) | Verilog | MIT (LICENSE, repo root) | ECP5 | 0 |
| [S/PDIF transmitter (f32c)](#core-f32c-spdif-tx) | [f32c__f32c](https://github.com/f32c/f32c) | VHDL | BSD-2-Clause | any | 0 |
| [S/PDIF transmitter (synthowheel)](#core-emard-synthowheel-spdif) | [emard__synthowheel](https://github.com/emard/synthowheel) | VHDL | BSD (LICENSE.txt: AUTHOR=EMARD LICENSE=BSD) | any | 11 |

## Cores

### I2S audio interface (ulx3s-misc) (best) {#core-emard-ulx3s-misc-i2s}

Parametric I2S transmit core (fmt/clk_hz/lrck_hz generics) demonstrated in the ULX3S audio example, VHDL wrapper over a Verilog core.

| | |
|---|---|
| Repository | [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc): ULX3S misc/advanced examples: EMARD's building-block library |
| Files | [`examples/audio/hdl/i2s.vhd`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/audio/hdl/i2s.vhd), [`examples/audio/hdl/i2s_v.v`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/audio/hdl/i2s_v.v) |
| Top module | `i2s` |
| Language | VHDL (wrapper), Verilog |
| License | BSD (`-- AUTHOR=EMARD` / `-- LICENSE=BSD` header) |
| FPGA / primitives | any: none (portable) |
| Tests | waveform-only (testbench/sinewave.c is a non-HDL C reference model) |

**On ULX3S:** clk_hz=25000000 matches the ULX3S board oscillator; see examples/audio/hdl/top_audio.v for a complete instantiation.

Full review: [emard__ulx3s-misc](../projects/emard__ulx3s-misc.md).

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [f32c__f32c](https://github.com/f32c/f32c) (copies [`rtl/soc/i2s_v.v`](https://github.com/f32c/f32c/blob/7dbf56d42a94ae599eabfd1e7fa15db14a10afd7/rtl/soc/i2s_v.v))

### I2S receiver (orangecrab-usb) {#core-orangecrab-usb-i2s-rx}

Small I2S receiver: deserializes left/right 32-bit channel data from an external I2S codec given a 64fs input clock.

| | |
|---|---|
| Repository | [mangelajo__orangecrab-usb](https://github.com/mangelajo/orangecrab-usb): OrangeCrab: two USB device examples |
| Files | [`hdl/i2s/i2s.v`](https://github.com/mangelajo/orangecrab-usb/blob/c4a8293fcd37a9a3c05a4e4217fdfdfa83e9911b/hdl/i2s/i2s.v) |
| Top module | `i2s` |
| Language | Verilog |
| License | none found (repo has no LICENSE/COPYING file) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Plain Verilog, portable; pairs with hdl/clkdiv/clkdiv.v in the same repo for MCLK/BCLK generation.

### I2S RX/TX + PDM/CIC mic front-end (sound2fft) {#core-icesugar-pro-i2s-pdm}

I2S receiver/transmitter plus a PDM-microphone CIC decimator and PDM modulator, part of a cocotb bit-exact-tested audio+FFT+HDMI pipeline for iCESugar-Pro (ECP5 25F).

| | |
|---|---|
| Repository | [mebner86__icesugar-pro_sound2fft](https://github.com/mebner86/icesugar-pro_sound2fft): iCESugar-Pro sound2fft: real-time audio spectrum analyzer |
| Files | [`rtl/i2s_rx.v`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/rtl/i2s_rx.v), [`rtl/i2s_tx.v`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/rtl/i2s_tx.v), [`rtl/pdm_cic.v`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/rtl/pdm_cic.v), [`rtl/pdm_modulator.v`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/rtl/pdm_modulator.v) |
| Top module | `i2s_rx` |
| Language | Verilog |
| License | MIT (LICENSE, repo root) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | cocotb, bit-exact vs numpy (per repo README; test scripts not individually re-verified here) |

**On ULX3S:** Portable front-end; only the TMDS serializer elsewhere in the repo needs ECP5 ODDRX1F, not these audio blocks.

### S/PDIF transmitter (f32c) {#core-f32c-spdif-tx}

Same ackspace.nl-derived S/PDIF transmitter as synthowheel's, vendored into the f32c SoC's peripheral set.

| | |
|---|---|
| Repository | [f32c__f32c](https://github.com/f32c/f32c): f32c: retargetable RISC-V/MIPS 32-bit soft CPU + SoC library |
| Files | [`rtl/soc/spdif_tx.vhd`](https://github.com/f32c/f32c/blob/7dbf56d42a94ae599eabfd1e7fa15db14a10afd7/rtl/soc/spdif_tx.vhd) |
| Top module | `spdif_tx` |
| Language | VHDL |
| License | BSD-2-Clause (repo-level per docs/projects/f32c__f32c.md; file itself carries no SPDX header, same ackspace.nl/EMARD-derived source) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Used from the f32c SoC's audio/CPU bus glue; can be lifted standalone like the synthowheel copy.

Full review: [f32c__f32c](../projects/f32c__f32c.md).

### S/PDIF transmitter (synthowheel) {#core-emard-synthowheel-spdif}

S/PDIF biphase-mark transmitter, derived from the ackspace.nl SPDIF project with EMARD's clock-divider modification; 24-bit signed PCM in, 25 MHz/48 kHz defaults.

| | |
|---|---|
| Repository | [emard__synthowheel](https://github.com/emard/synthowheel): Synthowheel: polyphonic additive synth, 128 gen x 9 harmonics, SPDIF + sigma-delta |
| Files | [`spdif_tx.vhd`](https://github.com/emard/synthowheel/blob/c2c6b2435418099f96397f2bd84bf87dcc4083e9/spdif_tx.vhd) |
| Top module | `spdif_tx` |
| Language | VHDL |
| License | BSD (LICENSE.txt: AUTHOR=EMARD LICENSE=BSD) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** C_clk_freq=25000000 matches the ULX3S oscillator directly; single-bit spdif_out needs a coax/TOSLINK line driver off-board.

**Used by 11 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [dan-rodrigues__icestation-32](https://github.com/dan-rodrigues/icestation-32) (instantiates [`hardware/ulx3s/ics32_top_ulx3s.v`](https://github.com/dan-rodrigues/icestation-32/blob/55214d79f74a547dedb54f99cb2fad431b7ac277/hardware/ulx3s/ics32_top_ulx3s.v))
- [dan-rodrigues__ics-adpcm](https://github.com/dan-rodrigues/ics-adpcm) (instantiates [`demo/adpcm_demo_top.v`](https://github.com/dan-rodrigues/ics-adpcm/blob/32b6c6af789440734b8e6d144ffd01467ed152d6/demo/adpcm_demo_top.v))
- [emard__minimig_ecs](https://github.com/emard/Minimig_ECS) (instantiates [`proj/altera/ffm-c5a4-sd-lcdif/top/amiga_ffm_c5a4_sd.vhd`](https://github.com/emard/Minimig_ECS/blob/a0a94bfa0b8534f50be7b79086ad00a41184c266/proj/altera/ffm-c5a4-sd-lcdif/top/amiga_ffm_c5a4_sd.vhd))
- [emard__papilio-arcade](https://github.com/emard/Papilio-Arcade) (instantiates [`pacman_rel004_sp3e_papilio/proj/lattice/ulx3s/pacman_ulx3s_v20_12f/top/pacman_ulx3s.vhd`](https://github.com/emard/Papilio-Arcade/blob/4f91f938c200f1b0d80f03f835bdadcc5f21aa58/pacman_rel004_sp3e_papilio/proj/lattice/ulx3s/pacman_ulx3s_v20_12f/top/pacman_ulx3s.vhd))
- [emard__uk101onfpga](https://github.com/emard/UK101onFPGA) (copies [`rtl_emard/spdif/spdif_tx.vhd`](https://github.com/emard/UK101onFPGA/blob/7264146bca76c6f751039ab569824a59875fe976/rtl_emard/spdif/spdif_tx.vhd))
- [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc) (instantiates [`examples/audio/hdl/top_audio.v`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/audio/hdl/top_audio.v))
- [emard__ulx3s_c64](https://github.com/emard/ulx3s_c64) (instantiates [`rtl/top_ulx3s_v20_c64.vhd`](https://github.com/emard/ulx3s_c64/blob/cc412a9134ed42d4296f1afb523d556b68bb74ba/rtl/top_ulx3s_v20_c64.vhd))
- [emard__vhdl_c64_c1541_sd](https://github.com/emard/vhdl_c64_c1541_sd) (instantiates [`proj/lattice/ulx3s/top/c64_ulx3s.vhd`](https://github.com/emard/vhdl_c64_c1541_sd/blob/e9e79b06d830d850d7415af20406bff8c3962214/proj/lattice/ulx3s/top/c64_ulx3s.vhd))
- [emard__vhdl_phoenix](https://github.com/emard/vhdl_phoenix) (instantiates [`proj/lattice/ulx3s/top/phoenix_ulx3s.vhd`](https://github.com/emard/vhdl_phoenix/blob/43f3b39cc87f71835844d200c83f3c7735eaec68/proj/lattice/ulx3s/top/phoenix_ulx3s.vhd))
- [f32c__f32c](https://github.com/f32c/f32c) (instantiates [`rtl/generic/glue_xram.vhd`](https://github.com/f32c/f32c/blob/7dbf56d42a94ae599eabfd1e7fa15db14a10afd7/rtl/generic/glue_xram.vhd))
- [linuxjedi__minimig_ecs](https://github.com/LinuxJedi/Minimig_ECS) (instantiates [`proj/altera/ffm-c5a4-sd-lcdif/top/amiga_ffm_c5a4_sd.vhd`](https://github.com/LinuxJedi/Minimig_ECS/blob/a0a94bfa0b8534f50be7b79086ad00a41184c266/proj/altera/ffm-c5a4-sd-lcdif/top/amiga_ffm_c5a4_sd.vhd))

## Other catalogued projects

Catalogued repos tagged `audio-i2s` (13), `audio-spdif` (8) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
