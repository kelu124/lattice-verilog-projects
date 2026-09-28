---
title: "Sound chips and synths"
parent: "Cores by function"
nav_order: 25
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# Sound chips and synths

Sound chip reimplementations (SID, SN76489, AY, YM) and synthesizers.

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [SN76489 PSG (sound chip)](#core-lawrie-sn76489) ★ | [lawrie__ulx3s_sms](https://github.com/lawrie/ulx3s_sms) | Verilog | none found | any | 10 |
| [JT51 (YM2151 FM synth core)](#core-jt51-ym2151) | [dlobato__cps1-musicbox](https://github.com/dlobato/cps1-musicbox) | Verilog | GPL-3.0 (gateware/rtl/jt51/LICENSE) | any | 0 |
| [JT89 (AY-3-8910-like PSG)](#core-danodus-jt89-ay8910) | [danodus__ulx3s_68k](https://github.com/danodus/ulx3s_68k) | Verilog | GPL-3.0-or-later | ECP5 | 0 |
| [SID (MOS 6581/8580) reimplementation, technology-independent](#core-daglem-redip-sid) | [daglem__redip-sid](https://github.com/daglem/reDIP-SID) | SystemVerilog | CERN-OHL-S-2.0 | iCE40 UP5K | 0 |
| [SID reimplementation (icesid)](#core-bithack-icesid) | [bit-hack__icesid](https://github.com/bit-hack/icesid) | Verilog | CERN-OHL-S-2.0 | iCE40 UP5K | 0 |

## Cores

### SN76489 PSG (sound chip) (best) {#core-lawrie-sn76489}

Texas Instruments SN76489 programmable sound generator (3 tone channels + noise), the Sega Master System/BBC Micro PSG; parametric AUDIO_RES output width.

| | |
|---|---|
| Repository | [lawrie__ulx3s_sms](https://github.com/lawrie/ulx3s_sms): Sega Master System / SG-1000: TV80, VDP, SN76489, SDRAM carts, ESP32 OSD |
| Files | [`src/sn76489.v`](https://github.com/lawrie/ulx3s_sms/blob/13c2361a5039d205de47857bab9201055ac9e566/src/sn76489.v) |
| Top module | `sn76489` |
| Language | Verilog |
| License | none found (no header in file; repo has no LICENSE/COPYING) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Proven on ULX3S 85F in lawrie__ulx3s_sms, cheyao__sega-sms and danodus__ulx3s_sms; feed audio_out into an I2S/DAC block from this same collection.

Full review: [lawrie__ulx3s_sms](../projects/lawrie__ulx3s_sms.md).

**Used by 10 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [cheyao__sega-sms](https://github.com/cheyao/sega-sms) (instantiates [`src/sms.v`](https://github.com/cheyao/sega-sms/blob/c37e846d94f88eb9a95f44b15f2b23019aa25a26/src/sms.v))
- [danodus__ulx3s_68k](https://github.com/danodus/ulx3s_68k) (instantiates [`src/test68.v`](https://github.com/danodus/ulx3s_68k/blob/ee10339210d0c302143745d3cc584a21a4878ace/src/test68.v))
- [danodus__ulx3s_sms](https://github.com/danodus/ulx3s_sms) (instantiates [`src/sms.v`](https://github.com/danodus/ulx3s_sms/blob/13c2361a5039d205de47857bab9201055ac9e566/src/sms.v))
- [hoglet67__ice40beeb](https://github.com/hoglet67/Ice40Beeb) (instantiates [`src/bbc.v`](https://github.com/hoglet67/Ice40Beeb/blob/e0fe38d9ab843e82e1d2676e977b47b7740d8d52/src/bbc.v))
- [lawrie__ulx3s_68k](https://github.com/lawrie/ulx3s_68k) (instantiates [`src/test68.v`](https://github.com/lawrie/ulx3s_68k/blob/ee10339210d0c302143745d3cc584a21a4878ace/src/test68.v))
- [lawrie__ulx3s_bbc_micro](https://github.com/lawrie/ulx3s_bbc_micro) (instantiates [`src/bbc.v`](https://github.com/lawrie/ulx3s_bbc_micro/blob/ea90cb6c75fbaef1b78df7f5cc7dbe2502967a22/src/bbc.v))
- [lawrie__ulx3s_colecovision](https://github.com/lawrie/ulx3s_colecovision) (instantiates [`src/coleco.v`](https://github.com/lawrie/ulx3s_colecovision/blob/4b30cf5419fe201df922f4563c1ec7faa837b7cf/src/coleco.v))
- [lawrie__ulx3s_gamegear](https://github.com/lawrie/ulx3s_gamegear) (instantiates [`src/sms.v`](https://github.com/lawrie/ulx3s_gamegear/blob/17d6e6c9dd013fd9ff3f8586b6268b472b991f75/src/sms.v))
- [lawrie__ulx3s_ql](https://github.com/lawrie/ulx3s_ql) (copies [`src/sn76489.v`](https://github.com/lawrie/ulx3s_ql/blob/5a982274a1402dc8273799c5d8d76b6759086719/src/sn76489.v))
- [lawrie__ulx3s_sg_1000](https://github.com/lawrie/ulx3s_sg_1000) (instantiates [`src/sg1000.v`](https://github.com/lawrie/ulx3s_sg_1000/blob/aabd4509bab9ce19fab11a43d8016c8d63ed49aa/src/sg1000.v))

### JT51 (YM2151 FM synth core) {#core-jt51-ym2151}

Jotego's cycle-accurate reimplementation of the Yamaha YM2151 FM synthesizer (used in many arcade boards incl. CPS1); ships its own `ver/` verification testbenches.

| | |
|---|---|
| Repository | [dlobato__cps1-musicbox](https://github.com/dlobato/cps1-musicbox): RISC-V (VexRiscv) + CPS1 arcade sound-chip (YM2151, MSM6295) emulation SoC built with LiteX/Migen, plays VGM… |
| Files | [`gateware/rtl/jt51/hdl`](https://github.com/dlobato/cps1-musicbox/tree/dc940ca9ecd5fa2685518fae2c92d701167fe4a0/gateware/rtl/jt51/hdl) |
| Top module | `jt51` |
| Language | Verilog |
| License | GPL-3.0 (gateware/rtl/jt51/LICENSE) |
| FPGA / primitives | any: none (portable) |
| Tests | ver/ directory with per-module testbenches (jotego JT-series standard test harness; not individually re-run here) |

**On ULX3S:** Used as the CPS1 music core over a LiteX SoC targeting ULX3S (radiona_ulx3s.py); GPL-3.0 copyleft applies.

### JT89 (AY-3-8910-like PSG) {#core-danodus-jt89-ay8910}

Jotego's AY-3-8910-compatible 3-channel PSG core (tone/noise/volume/mixer), used as the sound chip in the Atari ST-style ULX3S 68000 project.

| | |
|---|---|
| Repository | [danodus__ulx3s_68k](https://github.com/danodus/ulx3s_68k): 68000 CPU experiments |
| Files | [`src/jt89/jt89.v`](https://github.com/danodus/ulx3s_68k/blob/ee10339210d0c302143745d3cc584a21a4878ace/src/jt89/jt89.v), [`src/jt89/jt89_tone.v`](https://github.com/danodus/ulx3s_68k/blob/ee10339210d0c302143745d3cc584a21a4878ace/src/jt89/jt89_tone.v), [`src/jt89/jt89_vol.v`](https://github.com/danodus/ulx3s_68k/blob/ee10339210d0c302143745d3cc584a21a4878ace/src/jt89/jt89_vol.v), [`src/jt89/jt89_noise.v`](https://github.com/danodus/ulx3s_68k/blob/ee10339210d0c302143745d3cc584a21a4878ace/src/jt89/jt89_noise.v), [`src/jt89/jt89_mixer.v`](https://github.com/danodus/ulx3s_68k/blob/ee10339210d0c302143745d3cc584a21a4878ace/src/jt89/jt89_mixer.v) |
| Top module | `jt89` |
| Language | Verilog |
| License | GPL-3.0-or-later (in-file header, Jose Tejada / jotego) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | none found in this pass |

**On ULX3S:** Proven on ULX3S 85F alongside src/fx68k.sv (68000 core) in the same repo.

### SID (MOS 6581/8580) reimplementation, technology-independent {#core-daglem-redip-sid}

Reference-quality Commodore 64 SID sound chip DSP core (waveform/envelope/filter/voice/DAC), technology-independent with no SB_* primitives in the listed files.

| | |
|---|---|
| Repository | [daglem__redip-sid](https://github.com/daglem/reDIP-SID): reDIP SID: iCE40UP5K DIP-28 board running cycle-accurate MOS 6581/8580 SID chip emulation, with I2S/SGTL5000… |
| Files | [`gateware/sid_voice.sv`](https://github.com/daglem/reDIP-SID/blob/56608673b3a4e4f637afc026dca07ebdbf7d0769/gateware/sid_voice.sv), [`gateware/sid_waveform.sv`](https://github.com/daglem/reDIP-SID/blob/56608673b3a4e4f637afc026dca07ebdbf7d0769/gateware/sid_waveform.sv), [`gateware/sid_envelope.sv`](https://github.com/daglem/reDIP-SID/blob/56608673b3a4e4f637afc026dca07ebdbf7d0769/gateware/sid_envelope.sv), [`gateware/sid_filter.sv`](https://github.com/daglem/reDIP-SID/blob/56608673b3a4e4f637afc026dca07ebdbf7d0769/gateware/sid_filter.sv), [`gateware/sid_dac.sv`](https://github.com/daglem/reDIP-SID/blob/56608673b3a4e4f637afc026dca07ebdbf7d0769/gateware/sid_dac.sv), [`gateware/sid_api.sv`](https://github.com/daglem/reDIP-SID/blob/56608673b3a4e4f637afc026dca07ebdbf7d0769/gateware/sid_api.sv) |
| Top module | `sid_api` |
| Language | SystemVerilog |
| License | CERN-OHL-S-2.0 (LICENSE, root; matching header in gateware/*.sv, Dag Lem 2022-2023) |
| FPGA / primitives | iCE40 UP5K: none (portable) |
| Tests | none found in this pass |

**On ULX3S:** Core logic ports directly to ECP5; needs an I2S/sigma-delta output stage from this collection and the surrounding reDIP-SID board glue rewritten.

### SID reimplementation (icesid) {#core-bithack-icesid}

Alternate technology-independent Verilog SID core (dac/env/voice/filter/mult/output split into separate modules), no SB_* primitives.

| | |
|---|---|
| Repository | [bit-hack__icesid](https://github.com/bit-hack/icesid): reDIP-SID/iCESugar: open-source FPGA reimplementation of the MOS 6581/8580 SID chip audio synthesis, drop-in… |
| Files | [`icesid/sid.v`](https://github.com/bit-hack/icesid/blob/b126c46d25a6455914f218f83695d065efd9f961/icesid/sid.v), [`icesid/voice.v`](https://github.com/bit-hack/icesid/blob/b126c46d25a6455914f218f83695d065efd9f961/icesid/voice.v), [`icesid/env.v`](https://github.com/bit-hack/icesid/blob/b126c46d25a6455914f218f83695d065efd9f961/icesid/env.v), [`icesid/filter.v`](https://github.com/bit-hack/icesid/blob/b126c46d25a6455914f218f83695d065efd9f961/icesid/filter.v), [`icesid/dac.v`](https://github.com/bit-hack/icesid/blob/b126c46d25a6455914f218f83695d065efd9f961/icesid/dac.v) |
| Top module | `sid` |
| Language | Verilog |
| License | CERN-OHL-S-2.0 (LICENCE, root; matching SPDX header, Sylvain Munaut) |
| FPGA / primitives | iCE40 UP5K: none (portable) |
| Tests | none found in this pass |

**On ULX3S:** Same porting story as redip-sid: DSP core is portable, needs a ULX3S audio output stage.

## Other catalogued projects

Catalogued repos tagged `synth-audio` (28) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
