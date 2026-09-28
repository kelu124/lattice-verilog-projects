---
title: "VGA and video timing"
parent: "Cores by function"
nav_order: 2
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# VGA and video timing

VGA timing generators, framebuffers and text modes; 6845 CRTC, scandoublers.

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [Apple 1 VGA text-mode framebuffer core (vga/vram/font_rom)](#core-lawrie-apple1-vga) ★ | [lawrie__apple-one](https://github.com/lawrie/apple-one) | Verilog | Apache-2.0 | any | 0 |
| [6845 CRTC reimplementation (Graphics Gremlin)](#core-schlae-crtc6845) | [schlae__graphics-gremlin](https://github.com/schlae/graphics-gremlin) | Verilog | CC-BY-SA-4.0 | any | 0 |
| [f32c VGA timing + hardware text-mode overlay](#core-f32c-vga-textmode) | [f32c__f32c](https://github.com/f32c/f32c) | VHDL | MIT-style permissive header | any | 0 |
| [MiST composite/RGB scandoubler (15kHz to VGA)](#core-hoglet67-mist-scandoubler) | [hoglet67__ice40beeb](https://github.com/hoglet67/Ice40Beeb) | Verilog | GPL-3.0-or-later | iCE40 | 1 |
| [vga_core / vga_timing portable VGA generator (Black Mesa Labs)](#core-icebreaker-vga-core) | [icebreaker-fpga__icebreaker-verilog-examples](https://codeberg.org/icebreaker-fpga/icebreaker-verilog-examples) | Verilog | CERN-OHL v1.2 | iCE40 | 3 |
| [VgaSyncGen SpinalHDL VGA timing generator](#core-thorkn-vgasyncgen) | [thorkn__vga_clock_1](https://github.com/ThorKn/vga_clock_1) | SpinalHDL | Apache-2.0 | ECP5 | 1 |

## Cores

### Apple 1 VGA text-mode framebuffer core (vga/vram/font_rom) (best) {#core-lawrie-apple1-vga}

VGA timing generator driving a character-cell text framebuffer (vram.v) and 8x8 font ROM (font_rom.v); board-agnostic core wired to ULX3S GPDI via the sibling rtl/boards/ulx3s/vga2dvid.v.

| | |
|---|---|
| Repository | [lawrie__apple-one](https://github.com/lawrie/apple-one): Apple 1 Verilog, ULX3S HDMI + PS/2 + UART |
| Files | [`rtl/vga/vga.v`](https://github.com/lawrie/apple-one/blob/40412e90909378db3bd84b7537196ed8799fa477/rtl/vga/vga.v), [`rtl/vga/vram.v`](https://github.com/lawrie/apple-one/blob/40412e90909378db3bd84b7537196ed8799fa477/rtl/vga/vram.v), [`rtl/vga/font_rom.v`](https://github.com/lawrie/apple-one/blob/40412e90909378db3bd84b7537196ed8799fa477/rtl/vga/font_rom.v), [`rtl/boards/ulx3s/vga2dvid.v`](https://github.com/lawrie/apple-one/blob/40412e90909378db3bd84b7537196ed8799fa477/rtl/boards/ulx3s/vga2dvid.v) |
| Top module | `vga` |
| Language | Verilog |
| License | Apache-2.0 (LICENSE, root; core inherited unchanged from upstream alangarf/apple-one) |
| FPGA / primitives | any: none (portable) |
| Tests | iverilog tb, no self-checking pass/fail: tools/iverilog/vga_tb.v (run via run_vga_tb.sh, not `make`) |

**On ULX3S:** Already targets ULX3S 25F (boards/ulx3s/yosys/, ulx3s_v20.lpf, prebuilt bitstream committed); feed vga.v output into rtl/boards/ulx3s/vga2dvid.v for GPDI.

### 6845 CRTC reimplementation (Graphics Gremlin) {#core-schlae-crtc6845}

Cycle-accurate Motorola 6845 CRTC reimplementation with an ISA-bus register interface, generating MDA/CGA-style character-cell video timing (hsync/vsync/cursor); board-agnostic, no vendor primitives.

| | |
|---|---|
| Repository | [schlae__graphics-gremlin](https://github.com/schlae/graphics-gremlin): Graphics Gremlin: ISA video card FPGA logic emulating IBM MDA |
| Files | [`verilog/crtc6845.v`](https://github.com/schlae/graphics-gremlin/blob/709f624a88ad0fcc28c9d35fa2edae3fe0859ef6/verilog/crtc6845.v) |
| Top module | `crtc6845` |
| Language | Verilog |
| License | CC-BY-SA-4.0 (LICENSE; file header confirms) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Replace the ISA-bus register shim with a simple MMIO/CPU interface; the timing-generator half is directly usable standalone.

### f32c VGA timing + hardware text-mode overlay {#core-f32c-vga-textmode}

VGA timing generator (vga.vhd) plus a full color text-mode overlay with selectable font ROM and optional SRAM/SDRAM bitmap plane (VGA_textmode.vhd), designed for the f32c SoC bus.

| | |
|---|---|
| Repository | [f32c__f32c](https://github.com/f32c/f32c): f32c: retargetable RISC-V/MIPS 32-bit soft CPU + SoC library |
| Files | [`rtl/soc/vgahdmi/vga.vhd`](https://github.com/f32c/f32c/blob/7dbf56d42a94ae599eabfd1e7fa15db14a10afd7/rtl/soc/vgahdmi/vga.vhd), [`rtl/soc/vgahdmi/VGA_textmode.vhd`](https://github.com/f32c/f32c/blob/7dbf56d42a94ae599eabfd1e7fa15db14a10afd7/rtl/soc/vgahdmi/VGA_textmode.vhd) |
| Top module | `VGA_textmode` |
| Language | VHDL |
| License | MIT-style permissive header (vga.vhd: Copyright 2015 Davor Jadrijevic, LICENSE=BSD; VGA_textmode.vhd: Copyright 2015 Ken Jordan, MIT-text) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Not self-contained: expects f32c's video_cache_d/videofifo signal conventions; proven on ULX3S 12F/25F/45F/85F via rtl/lattice/ulx3s/top/top_ulx3s_12f_xram_sdram_tv.vhd and siblings.

Full review: [f32c__f32c](../projects/f32c__f32c.md).

### MiST composite/RGB scandoubler (15kHz to VGA) {#core-hoglet67-mist-scandoubler}

Converts 15.7kHz composite/RGB-timed video into standard 31.4kHz VGA timing; vendored from the MiST project into an iCE40 HX4K design but the file itself instantiates no vendor primitives.

| | |
|---|---|
| Repository | [hoglet67__ice40beeb](https://github.com/hoglet67/Ice40Beeb): Ice40Beeb: BBC Micro Model B retro-computer core |
| Files | [`src/mist_scandoubler.v`](https://github.com/hoglet67/Ice40Beeb/blob/e0fe38d9ab843e82e1d2676e977b47b7740d8d52/src/mist_scandoubler.v) |
| Top module | `mist_scandoubler` |
| Language | Verilog |
| License | GPL-3.0-or-later (file header, Copyright 2015 Till Harbaum, MiST project) |
| FPGA / primitives | iCE40: none (portable) |
| Tests | none found |

**On ULX3S:** Portable structural Verilog; should synthesize unchanged for ECP5 with no primitive porting.

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [lawrie__ulx3s_bbc_micro](https://github.com/lawrie/ulx3s_bbc_micro) (instantiates [`src/beeb.v`](https://github.com/lawrie/ulx3s_bbc_micro/blob/ea90cb6c75fbaef1b78df7f5cc7dbe2502967a22/src/beeb.v))

### vga_core / vga_timing portable VGA generator (Black Mesa Labs) {#core-icebreaker-vga-core}

Portable VGA timing generator (vga_timing.v) and test-pattern/framebuffer core (vga_core.v), originally written for Xilinx then ported to iCE40 without vendor primitives per the repo README.

| | |
|---|---|
| Repository | [icebreaker-fpga__icebreaker-verilog-examples](https://codeberg.org/icebreaker-fpga/icebreaker-verilog-examples): iCEBreaker: collection of small Verilog examples |
| Files | [`icebreaker/dvi-24bit/vga_core.v`](https://codeberg.org/icebreaker-fpga/icebreaker-verilog-examples/src/commit/8d0892bf62dd5d8ae59c48c882d9ebebd1cab9c2/icebreaker/dvi-24bit/vga_core.v), [`icebreaker/dvi-24bit/vga_timing.v`](https://codeberg.org/icebreaker-fpga/icebreaker-verilog-examples/src/commit/8d0892bf62dd5d8ae59c48c882d9ebebd1cab9c2/icebreaker/dvi-24bit/vga_timing.v) |
| Top module | `vga_core` |
| Language | Verilog |
| License | CERN-OHL v1.2 (file header, Copyright 2017 Kevin M. Hubbard / Black Mesa Labs) |
| FPGA / primitives | iCE40: none (portable) |
| Tests | none found |

**On ULX3S:** No porting needed for this pair of files; only the separate DVI serializer stage (not included) is board-specific.

**Used by 3 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [dan-rodrigues__icestation-32](https://github.com/dan-rodrigues/icestation-32) (instantiates [`hardware/vdp/vdp.v`](https://github.com/dan-rodrigues/icestation-32/blob/55214d79f74a547dedb54f99cb2fad431b7ac277/hardware/vdp/vdp.v))
- [joaln27__koti](https://github.com/joaln27/koti) (instantiates [`src/vga_text.sv`](https://github.com/joaln27/koti/blob/9fb88761388653c3c18f70edd0deae74f2f6e94c/src/vga_text.sv))
- [lawrie__verilog_examples](https://github.com/lawrie/verilog_examples) (instantiates [`fpga4fun/ponghdmi/pong.v`](https://github.com/lawrie/verilog_examples/blob/ee8f0d2b44313b683a63ea6a0b151f454f8b9ddc/fpga4fun/ponghdmi/pong.v))

### VgaSyncGen SpinalHDL VGA timing generator {#core-thorkn-vgasyncgen}

SpinalHDL VGA sync-timing generator and clock-cycle counter components, proven on ULX3S 85F (ulx3s/Makefile CHIP:=85k); reused unchanged in the author's vga_pong project.

| | |
|---|---|
| Repository | [thorkn__vga_clock_1](https://github.com/ThorKn/vga_clock_1): VGA digital clock display, hardware described in SpinalHDL/Scala and generated to Verilog for ULX3S 85k |
| Files | [`spinalHDL/src/spinal/vgaclock/VgaSyncGen.scala`](https://github.com/ThorKn/vga_clock_1/blob/5708288299b1cb3c59c2ed22bc5ad2b13b91caf7/spinalHDL/src/spinal/vgaclock/VgaSyncGen.scala), [`spinalHDL/src/spinal/vgaclock/ClockCounters.scala`](https://github.com/ThorKn/vga_clock_1/blob/5708288299b1cb3c59c2ed22bc5ad2b13b91caf7/spinalHDL/src/spinal/vgaclock/ClockCounters.scala) |
| Top module | `VgaSyncGen` |
| Language | SpinalHDL (Scala, elaborates to Verilog) |
| License | Apache-2.0 (LICENSE) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | none found |

**On ULX3S:** Requires the SpinalHDL/Scala toolchain to elaborate to Verilog before synthesis; generator parameters cover standard VGA modes.

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [thorkn__vga_pong](https://github.com/ThorKn/vga_pong) (instantiates [`spinalHDL/VgaPong.v`](https://github.com/ThorKn/vga_pong/blob/8b4ca37f15691097d54a445a799b38c7a3901e3c/spinalHDL/VgaPong.v))

## Other catalogued projects

Catalogued repos tagged `video-vga` (14), `vga` (1) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
