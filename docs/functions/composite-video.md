---
title: "Composite video (CVBS)"
parent: "Cores by function"
nav_order: 3
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# Composite video (CVBS)

PAL/NTSC composite video generation.

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [f32c PAL composite video (CVBS) generator](#core-f32c-cvbs) ★ | [f32c__f32c](https://github.com/f32c/f32c) | VHDL | BSD-2-Clause | any | 0 |
| [MiST composite/RGB scandoubler (composite-video input side)](#core-hoglet67-composite-scandoubler) | [hoglet67__ice40beeb](https://github.com/hoglet67/Ice40Beeb) | Verilog | GPL-3.0-or-later | iCE40 | 1 |

## Cores

### f32c PAL composite video (CVBS) generator (best) {#core-f32c-cvbs}

Generates PAL composite video (luma/chroma/sync encoding) from RGB framebuffer pixel data for direct resistor-DAC output; wired into f32c's own ULX3S top (rtl/lattice/ulx3s/top/top_ulx3s_12f_xram_sdram_tv.vhd).

| | |
|---|---|
| Repository | [f32c__f32c](https://github.com/f32c/f32c): f32c: retargetable RISC-V/MIPS 32-bit soft CPU + SoC library |
| Files | [`rtl/soc/cvbs.vhd`](https://github.com/f32c/f32c/blob/7dbf56d42a94ae599eabfd1e7fa15db14a10afd7/rtl/soc/cvbs.vhd) |
| Top module | `cvbs` |
| Language | VHDL |
| License | BSD-2-Clause (file header, Copyright 2013 Marko Zec / University of Zagreb) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** ULX3S has no dedicated composite DAC pin; needs a resistor-ladder DAC on spare GPIO exactly as f32c's own 12f_..._tv top does.

Full review: [f32c__f32c](../projects/f32c__f32c.md).

### MiST composite/RGB scandoubler (composite-video input side) {#core-hoglet67-composite-scandoubler}

Converts 15.7kHz composite/RGB-timed video (the format retro cores generate internally) up to 31.4kHz VGA timing; complementary to composite generation rather than a PAL/NTSC generator itself. No other true composite-out generator besides f32c's cvbs.vhd was found in this collection.

| | |
|---|---|
| Repository | [hoglet67__ice40beeb](https://github.com/hoglet67/Ice40Beeb): Ice40Beeb: BBC Micro Model B retro-computer core |
| Files | [`src/mist_scandoubler.v`](https://github.com/hoglet67/Ice40Beeb/blob/e0fe38d9ab843e82e1d2676e977b47b7740d8d52/src/mist_scandoubler.v) |
| Top module | `mist_scandoubler` |
| Language | Verilog |
| License | GPL-3.0-or-later (file header, Copyright 2015 Till Harbaum, MiST project) |
| FPGA / primitives | iCE40: none (portable) |
| Tests | none found |

**On ULX3S:** Useful when a retro core's internal video is composite-timed and needs converting for HDMI/VGA display rather than driven out as analog PAL/NTSC.

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [lawrie__ulx3s_bbc_micro](https://github.com/lawrie/ulx3s_bbc_micro) (instantiates [`src/beeb.v`](https://github.com/lawrie/ulx3s_bbc_micro/blob/ea90cb6c75fbaef1b78df7f5cc7dbe2502967a22/src/beeb.v))

## Other catalogued projects

Catalogued repos tagged `video-composite` (15) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
