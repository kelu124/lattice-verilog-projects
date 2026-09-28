---
title: "DAC, PWM and sigma-delta"
parent: "Cores by function"
nav_order: 23
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# DAC, PWM and sigma-delta

Sigma-delta/PWM/PDM DACs and external DAC interfaces.

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [Sigma-delta PCM audio DAC (fpga-dac)](#core-machdyne-fpga-dac-audio) ★ | [machdyne__fpga-dac](https://github.com/machdyne/fpga-dac) | Verilog | 1-clause BSD-like | ECP5 | 0 |
| [PDM audio DAC (hadbadge2019 soc/audio)](#core-spritetm-hadbadge-pdm) | [spritetm__hadbadge2019_fpgasoc](https://github.com/Spritetm/hadbadge2019_fpgasoc) | Verilog | BSD-3-Clause | any | 0 |
| [Resistor+PWM hybrid DAC (dacpwm)](#core-emard-ulx3s-misc-dacpwm) | [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc) | Verilog, VHDL | none found | any | 7 |
| [Sigma-delta DAC (synthowheel)](#core-emard-synthowheel-sigmadelta) | [emard__synthowheel](https://github.com/emard/synthowheel) | VHDL | BSD (LICENSE.txt: AUTHOR=EMARD LICENSE=BSD) | any | 3 |
| [Sigma-delta DAC (up5k-demos)](#core-daveshah1-sigma-delta-dac) | [daveshah1__up5k-demos](https://github.com/daveshah1/up5k-demos) | Verilog | none found | iCE40 UP5K | 15 |

## Cores

### Sigma-delta PCM audio DAC (fpga-dac) (best) {#core-machdyne-fpga-dac-audio}

First-order sigma-delta stereo audio DAC that streams 48kHz 16-bit signed PCM from SPI flash; simple phase accumulator, no vendor primitives in audio.v itself.

| | |
|---|---|
| Repository | [machdyne__fpga-dac](https://github.com/machdyne/fpga-dac): Machdyne Konfekt/Lakritz/Noir: experimental sigma-delta PCM audio DAC/player that streams 48kHz 16-bit stereo… |
| Files | [`rtl/audio.v`](https://github.com/machdyne/fpga-dac/blob/cde03b40d8027412fae6616c2c0d23cf62f16f7a/rtl/audio.v) |
| Top module | `audio` |
| Language | Verilog |
| License | 1-clause BSD-like (LICENSE.md, Lone Dynamics Corporation) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | none found |

**On ULX3S:** Self-contained modulator (l_pwm_acc/r_pwm_acc); reuse just the sigma-delta block and drive it from any PCM source (SDRAM, ESP32, etc.) instead of SPI flash. rtl/pll.v is board-specific and needs re-deriving for 25 MHz ULX3S input.

### PDM audio DAC (hadbadge2019 soc/audio) {#core-spritetm-hadbadge-pdm}

First-order pulse-density-modulation DAC core with dither, used for the hadbadge2019 SoC's audio synth output.

| | |
|---|---|
| Repository | [spritetm__hadbadge2019_fpgasoc](https://github.com/Spritetm/hadbadge2019_fpgasoc): Hackaday Supercon 2019 badge: ECP5 SoC |
| Files | [`soc/audio/pdm.v`](https://github.com/Spritetm/hadbadge2019_fpgasoc/blob/6e706d52ecdc007e9179bda01d8eac60d55b7c45/soc/audio/pdm.v) |
| Top module | `pdm` |
| Language | Verilog |
| License | BSD-3-Clause (in-file header, `LICENSE.bsd`, Sylvain Munaut 2019) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Pairs well with soc/audio/synth_core.v in the same repo; plain Verilog, no ECP5-specific primitives.

Full review: [spritetm__hadbadge2019_fpgasoc](../projects/spritetm__hadbadge2019_fpgasoc.md).

### Resistor+PWM hybrid DAC (dacpwm) {#core-emard-ulx3s-misc-dacpwm}

Combines a coarse resistor-ladder DAC (upper bits) with a PWM output (lower bits) to raise effective DAC resolution from a small pin count.

| | |
|---|---|
| Repository | [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc): ULX3S misc/advanced examples: EMARD's building-block library |
| Files | [`examples/audio/hdl/dacpwm.v`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/audio/hdl/dacpwm.v), [`examples/audio/hdl/dacpwm_vhdl.vhd`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/audio/hdl/dacpwm_vhdl.vhd) |
| Top module | `dacpwm` |
| Language | Verilog, VHDL |
| License | none found (no header in file; repo has no LICENSE file) |
| FPGA / primitives | any: none (portable) |
| Tests | waveform-only (examples/audio/testbench/sinewave.c is a plain C reference model, not a Verilog tb) |

**On ULX3S:** Parametric C_pcm_bits/C_dac_bits; used in the ULX3S audio example (examples/audio/hdl/top_audio.v) with 25 MHz clock.

Full review: [emard__ulx3s-misc](../projects/emard__ulx3s-misc.md).

**Used by 7 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [dan-rodrigues__icestation-32](https://github.com/dan-rodrigues/icestation-32) (instantiates [`hardware/ulx3s/ics32_top_ulx3s.v`](https://github.com/dan-rodrigues/icestation-32/blob/55214d79f74a547dedb54f99cb2fad431b7ac277/hardware/ulx3s/ics32_top_ulx3s.v))
- [dan-rodrigues__ics-adpcm](https://github.com/dan-rodrigues/ics-adpcm) (instantiates [`demo/adpcm_demo_top.v`](https://github.com/dan-rodrigues/ics-adpcm/blob/32b6c6af789440734b8e6d144ffd01467ed152d6/demo/adpcm_demo_top.v))
- [dlobato__cps1-musicbox](https://github.com/dlobato/cps1-musicbox) (instantiates [`gateware/dacpwm.py`](https://github.com/dlobato/cps1-musicbox/blob/dc940ca9ecd5fa2685518fae2c92d701167fe4a0/gateware/dacpwm.py))
- [emard__ulx3s_c64](https://github.com/emard/ulx3s_c64) (instantiates [`rtl/top_ulx3s_v20_c64.vhd`](https://github.com/emard/ulx3s_c64/blob/cc412a9134ed42d4296f1afb523d556b68bb74ba/rtl/top_ulx3s_v20_c64.vhd))
- [f32c__f32c](https://github.com/f32c/f32c) (instantiates [`rtl/generic/glue_xram_vector.vhd`](https://github.com/f32c/f32c/blob/7dbf56d42a94ae599eabfd1e7fa15db14a10afd7/rtl/generic/glue_xram_vector.vhd))
- [lawrie__spinalulx3s](https://github.com/lawrie/SpinalULX3S) (instantiates [`src/main/scala/mylib/DacPwm.scala`](https://github.com/lawrie/SpinalULX3S/blob/7cb99e7f62c7abdc9210790d2d934e7e197ae627/src/main/scala/mylib/DacPwm.scala))
- [logoposeidon__ulx3sjukebox](https://github.com/LogoPoseidon/Ulx3sJukeBox) (instantiates [`audio_test.v`](https://github.com/LogoPoseidon/Ulx3sJukeBox/blob/0a4c0a6faf01a45ff74693e16087c25c686114d4/audio_test.v))

### Sigma-delta DAC (synthowheel) {#core-emard-synthowheel-sigmadelta}

Standalone sigma-delta modulator used to drive the audio output of the synthowheel ULX3S synth project.

| | |
|---|---|
| Repository | [emard__synthowheel](https://github.com/emard/synthowheel): Synthowheel: polyphonic additive synth, 128 gen x 9 harmonics, SPDIF + sigma-delta |
| Files | [`sigmadelta.vhd`](https://github.com/emard/synthowheel/blob/c2c6b2435418099f96397f2bd84bf87dcc4083e9/sigmadelta.vhd) |
| Top module | `sigmadelta` |
| Language | VHDL |
| License | BSD (LICENSE.txt: AUTHOR=EMARD LICENSE=BSD) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Pairs with synth.vhd in the same repo; single-bit output suitable for a simple RC lowpass to line-out.

**Used by 3 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [f32c__f32c](https://github.com/f32c/f32c) (instantiates [`rtl/generic/glue_xram.vhd`](https://github.com/f32c/f32c/blob/7dbf56d42a94ae599eabfd1e7fa15db14a10afd7/rtl/generic/glue_xram.vhd))
- [glasgowembedded__glasgow](https://github.com/GlasgowEmbedded/glasgow) (instantiates [`software/glasgow/applet/audio/dac/__init__.py`](https://github.com/GlasgowEmbedded/glasgow/blob/9b835612a323930c2e0641033fc95c2814a657b9/software/glasgow/applet/audio/dac/__init__.py))
- [tarik-hamedovic__sdr-hls](https://github.com/tarik-hamedovic/SDR-HLS) (instantiates [`3.Testing/1bitADCLattice/Lattice/First_Implementation/ADC_top_prim.v`](https://github.com/tarik-hamedovic/SDR-HLS/blob/334f7074eb51dc7d4910a439ba62c85c2668e706/3.Testing/1bitADCLattice/Lattice/First_Implementation/ADC_top_prim.v))

### Sigma-delta DAC (up5k-demos) {#core-daveshah1-sigma-delta-dac}

Tiny parametric-width sigma-delta DAC (delta/sigma adder pair) used for the NES APU audio output.

| | |
|---|---|
| Repository | [daveshah1__up5k-demos](https://github.com/daveshah1/up5k-demos): UPduino: UP5K demos - a buildable port of the MiST NES core to iCE40 UltraPlus |
| Files | [`nes/sigma_delta_dac.v`](https://github.com/daveshah1/up5k-demos/blob/d85f0516f013a6a026946afc386196b1b2ac1e4e/nes/sigma_delta_dac.v) |
| Top module | `sigma_delta_dac` |
| Language | Verilog |
| License | none found (repo has no LICENSE/COPYING file; nes.v claims GPL but no license text present) |
| FPGA / primitives | iCE40 UP5K: none (portable) |
| Tests | none found |

**On ULX3S:** Plain Verilog, no SB_* primitives; drops onto ECP5 unchanged, only the surrounding NES top-level is iCE40-specific.

**Used by 15 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [cheyao__nes_ecp5](https://github.com/cheyao/nes_ecp5) (copies [`sigma_delta_dac.v`](https://github.com/cheyao/nes_ecp5/blob/e8dd1eb7f9f440a552cd24c0b936e58705a272e7/sigma_delta_dac.v))
- [cheyao__sega-sms](https://github.com/cheyao/sega-sms) (instantiates [`src/sms.v`](https://github.com/cheyao/sega-sms/blob/c37e846d94f88eb9a95f44b15f2b23019aa25a26/src/sms.v))
- [danodus__ulx3s_sms](https://github.com/danodus/ulx3s_sms) (instantiates [`src/sms.v`](https://github.com/danodus/ulx3s_sms/blob/13c2361a5039d205de47857bab9201055ac9e566/src/sms.v))
- [darklife__darkriscv](https://github.com/darklife/darkriscv) (instantiates [`boards/de10nano_cyclonev_mister/sys/audio_out.v`](https://github.com/darklife/darkriscv/blob/974034aa8079039a36b89c14dcdfed575de183b7/boards/de10nano_cyclonev_mister/sys/audio_out.v))
- [emard__nes_ecp5](https://github.com/emard/nes_ecp5) (instantiates [`top.v`](https://github.com/emard/nes_ecp5/blob/fd421a13886cccc6da13be28a4a803a90b201e60/top.v))
- [emard__snes_mister_ulx3s](https://github.com/emard/SNES_MiSTer_ulx3s) (instantiates [`sys/audio_out.v`](https://github.com/emard/SNES_MiSTer_ulx3s/blob/bbb10d06a1c396d3784ff70033ecf7e941fd43fc/sys/audio_out.v))
- [gatecat__snes_mister_ulx3s](https://github.com/gatecat/SNES_MiSTer_ulx3s) (instantiates [`sys/audio_out.v`](https://github.com/gatecat/SNES_MiSTer_ulx3s/blob/a9ed2ceb422e1001cfbbcfc85359fb23bc35d798/sys/audio_out.v))
- [gojimmypi__z80386-ulx3s-doom](https://github.com/gojimmypi/z80386-ulx3s-doom) (instantiates [`third_party/z386_MiSTer/sys/audio_out.v`](https://github.com/gojimmypi/z80386-ulx3s-doom/blob/ccc2903c380b90d6e7ec3b5ffc3e5b5f6d23e6dc/third_party/z386_MiSTer/sys/audio_out.v))
- [ironsteel__nes_ecp5](https://github.com/ironsteel/nes_ecp5) (instantiates [`top.v`](https://github.com/ironsteel/nes_ecp5/blob/ff331d4b9c422e0b792560dd7b2b67a28622f67f/top.v))
- [lawrie__ulx3s_gamegear](https://github.com/lawrie/ulx3s_gamegear) (instantiates [`src/sms.v`](https://github.com/lawrie/ulx3s_gamegear/blob/17d6e6c9dd013fd9ff3f8586b6268b472b991f75/src/sms.v))
- [lawrie__ulx3s_mac128](https://github.com/lawrie/ulx3s_mac128) (instantiates [`src/mac128.v`](https://github.com/lawrie/ulx3s_mac128/blob/cd3ef1e92e4415b9955a8554a0ae253aae9850d7/src/mac128.v))
- [lawrie__ulx3s_sms](https://github.com/lawrie/ulx3s_sms) (instantiates [`src/sms.v`](https://github.com/lawrie/ulx3s_sms/blob/13c2361a5039d205de47857bab9201055ac9e566/src/sms.v))
- [machdyne__nes_ecp5](https://github.com/machdyne/nes_ecp5) (instantiates [`top.v`](https://github.com/machdyne/nes_ecp5/blob/ff331d4b9c422e0b792560dd7b2b67a28622f67f/top.v))
- [wifiboy__ok-ice40pro](https://github.com/WiFiBoy/OK-iCE40Pro) (instantiates [`ok-nes-vga-src/NES_okice40_pro.v`](https://github.com/WiFiBoy/OK-iCE40Pro/blob/01c99298f8b059da09a72dd4b3286d9b0a96fe95/ok-nes-vga-src/NES_okice40_pro.v))
- [wuxx__icesugar](https://github.com/wuxx/icesugar) (instantiates [`src/advanced/up5k-demos/nes/NES_ice40.v`](https://github.com/wuxx/icesugar/blob/1ebe71bf448e33a1bccfa2db6730d59eafb6c390/src/advanced/up5k-demos/nes/NES_ice40.v))

## Other catalogued projects

Catalogued repos tagged `audio-dac` (55) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
