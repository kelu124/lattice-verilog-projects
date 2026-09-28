---
title: "Retro CPUs"
parent: "Cores by function"
nav_order: 29
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# Retro CPUs

6502, Z80, 8080, 68000, 1802 and other classic CPUs.

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [cpu_6502 (Klaus Dormann-verified 6502 core)](#core-chrismoos-m6502) ★ | [chrismoos__m6502](https://github.com/chrismoos/m6502) | SystemVerilog | MIT (LICENSE) | any | 0 |
| [CDP1802-compatible core (SpinalHDL)](#core-cdp1802-fpgacosmacelf) | [lawrie__fpgacosmacelf](https://github.com/lawrie/FPGACosmacELF) | Scala (SpinalHDL) | GPL-3.0 | any | 0 |
| [fx68k 68000-compatible core (nullobject vendored copy)](#core-fx68k-m68k-ulx3s) | [nullobject__m68k-ulx3s](https://github.com/nullobject/m68k-ulx3s) | Verilog | GPL-3.0 (lib/fx68k/LICENSE) | ECP5 | 5 |
| [grom toy 8-bit CPU + computer (FPGA 101 original)](#core-mmicko-grom-cpu) | [mmicko__fpga101-workshop](https://github.com/mmicko/fpga101-workshop) | Verilog | MIT (repo LICENSE; files have no header) | any | 3 |
| [i8080-compatible core (Bashkiria-2M-derived)](#core-i8080-altair) | [lawrie__ulx3s_examples](https://github.com/lawrie/ulx3s_examples) | Verilog | modified BSD | ECP5 | 4 |
| [TMS9900-family CPU core (public domain)](#core-tms99000-ti99) | [pnru__ti99](https://gitlab.com/pnru/ti99) | Verilog | public domain | ECP5 | 1 |
| [TV80 Z80-compatible core (emard__ulx3s_galaksija copy)](#core-tv80-galaksija) | [emard__ulx3s_galaksija](https://github.com/emard/ulx3s_galaksija) | Verilog | MIT (OpenCores-style header, Copyright (c) 2004… | any | 24 |

## Cores

### cpu_6502 (Klaus Dormann-verified 6502 core) (best) {#core-chrismoos-m6502}

6502-compatible core, and the most reusable/tested CPU of any family in this collection: 9 cocotb test suites plus a Klaus Dormann full-opcode functional test, with ready-made ULX3S and Fomu targets/ dirs.

| | |
|---|---|
| Repository | [chrismoos__m6502](https://github.com/chrismoos/m6502): m6502: compact microcoded cycle-accurate 6502 in SystemVerilog + MCU wrapper |
| Files | [`rtl/cpu_6502.sv`](https://github.com/chrismoos/m6502/blob/447194414b4cb184d2d2b9ea77e3eff6b4e29cf6/rtl/cpu_6502.sv), [`rtl/cpu_6502_alu.sv`](https://github.com/chrismoos/m6502/blob/447194414b4cb184d2d2b9ea77e3eff6b4e29cf6/rtl/cpu_6502_alu.sv), [`rtl/cpu_6502_ir_decoder.sv`](https://github.com/chrismoos/m6502/blob/447194414b4cb184d2d2b9ea77e3eff6b4e29cf6/rtl/cpu_6502_ir_decoder.sv), [`rtl/cpu_6502_microcode.sv`](https://github.com/chrismoos/m6502/blob/447194414b4cb184d2d2b9ea77e3eff6b4e29cf6/rtl/cpu_6502_microcode.sv) |
| Top module | `cpu_6502` |
| Language | SystemVerilog |
| License | MIT (LICENSE) |
| FPGA / primitives | any: none (portable) |
| Tests | self-checking: make test (9 cocotb suites, python asserts) + make test-klaus (Klaus Dormann functional ROM) |

**On ULX3S:** targets/ulx3s/ is a direct ULX3S build; no porting needed.

Full review: [chrismoos__m6502](../projects/chrismoos__m6502.md).

### CDP1802-compatible core (SpinalHDL) {#core-cdp1802-fpgacosmacelf}

'Others' family pick #2: a COSMAC ELF (CDP1802 CPU + CDP1861 video) reimplementation in SpinalHDL, elaborated to Verilog/VHDL at build time; built for ULX3S 12F default (12-85 range).

| | |
|---|---|
| Repository | [lawrie__fpgacosmacelf](https://github.com/lawrie/FPGACosmacELF): Cosmac ELF: CDP1802 + CDP1861 in SpinalHDL, UART loader |
| Files | [`src/main/scala/Spinal1802/CDP1802.scala`](https://github.com/lawrie/FPGACosmacELF/blob/42a6a7355e32ea0a519f7aa54909319c78416b64/src/main/scala/Spinal1802/CDP1802.scala) |
| Top module | `CDP1802` |
| Language | Scala (SpinalHDL) |
| License | GPL-3.0 |
| FPGA / primitives | any: none (portable) |
| Tests | ./verification dir present; self-checking status not confirmed |

**On ULX3S:** Needs sbt+SpinalHDL to elaborate before synthesis, unlike the plain-HDL cores above.

### fx68k 68000-compatible core (nullobject vendored copy) {#core-fx68k-m68k-ulx3s}

The 68000-family pick: fx68k is used throughout the collection (also in lawrie__ulx3s_examples/test68, danodus__ulx3s_68k, lawrie__ulx3s_mac128/ql); this copy is the one with an explicit vendored LICENSE file, unlike the widely-copied lawrie__ulx3s_examples/test68/fx68k.v which carries none.

| | |
|---|---|
| Repository | [nullobject__m68k-ulx3s](https://github.com/nullobject/m68k-ulx3s): Motorola 68000 SoC on ULX3S using the fx68k core, with OLED display, framebuffer/GPU and ACIA serial |
| Files | [`lib/fx68k/fx68k.v`](https://github.com/nullobject/m68k-ulx3s/blob/761a95e944b4d1c8b196a1c42ef38a67e6d36088/lib/fx68k/fx68k.v), [`lib/fx68k/fx68kAlu.v`](https://github.com/nullobject/m68k-ulx3s/blob/761a95e944b4d1c8b196a1c42ef38a67e6d36088/lib/fx68k/fx68kAlu.v) |
| Top module | `fx68k` |
| Language | Verilog |
| License | GPL-3.0 (lib/fx68k/LICENSE) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | none found for fx68k itself (repo's make sim only exercises hdl/gpu.v) |

**On ULX3S:** Built for ULX3S 85F (Makefile DEVICE=85k) with a GPU/OLED SoC wrapped around it; the CPU files alone are reusable.

**Used by 5 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [danodus__ulx3s_68k](https://github.com/danodus/ulx3s_68k) (instantiates [`src/fx68k.sv`](https://github.com/danodus/ulx3s_68k/blob/ee10339210d0c302143745d3cc584a21a4878ace/src/fx68k.sv))
- [lawrie__ulx3s_68k](https://github.com/lawrie/ulx3s_68k) (instantiates [`src/fx68k.sv`](https://github.com/lawrie/ulx3s_68k/blob/ee10339210d0c302143745d3cc584a21a4878ace/src/fx68k.sv))
- [lawrie__ulx3s_examples](https://github.com/lawrie/ulx3s_examples) (instantiates [`test68/tb.v`](https://github.com/lawrie/ulx3s_examples/blob/b6ff00099265401fef4843e4e89c2ac54254c95f/test68/tb.v))
- [lawrie__ulx3s_mac128](https://github.com/lawrie/ulx3s_mac128) (instantiates [`src/fx68k/fx68k.sv`](https://github.com/lawrie/ulx3s_mac128/blob/cd3ef1e92e4415b9955a8554a0ae253aae9850d7/src/fx68k/fx68k.sv))
- [lawrie__ulx3s_ql](https://github.com/lawrie/ulx3s_ql) (instantiates [`src/fx68k/fx68k.sv`](https://github.com/lawrie/ulx3s_ql/blob/5a982274a1402dc8273799c5d8d76b6759086719/src/fx68k/fx68k.sv))

### grom toy 8-bit CPU + computer (FPGA 101 original) {#core-mmicko-grom-cpu}

Teaching CPU by Miodrag Milanović: 8-bit data, 12-bit address, small ISA, with RAM and a 'computer' wrapper driving LEDs. Original of the copies in lawrie's examples and FPGA Odysseus.

| | |
|---|---|
| Repository | [mmicko__fpga101-workshop](https://github.com/mmicko/fpga101-workshop): FPGA 101 workshop |
| Files | [`tutorials/10-CPU/grom_cpu.v`](https://github.com/mmicko/fpga101-workshop/blob/1f5d605bc158810148626df5261bf1dc87cf50a1/tutorials/10-CPU/grom_cpu.v), [`tutorials/10-CPU/alu.v`](https://github.com/mmicko/fpga101-workshop/blob/1f5d605bc158810148626df5261bf1dc87cf50a1/tutorials/10-CPU/alu.v), [`tutorials/10-CPU/grom_computer.v`](https://github.com/mmicko/fpga101-workshop/blob/1f5d605bc158810148626df5261bf1dc87cf50a1/tutorials/10-CPU/grom_computer.v), [`tutorials/10-CPU/grom_top.v`](https://github.com/mmicko/fpga101-workshop/blob/1f5d605bc158810148626df5261bf1dc87cf50a1/tutorials/10-CPU/grom_top.v), [`tutorials/10-CPU/grom_computer_tb.v`](https://github.com/mmicko/fpga101-workshop/blob/1f5d605bc158810148626df5261bf1dc87cf50a1/tutorials/10-CPU/grom_computer_tb.v) |
| Top module | `grom_top` |
| Language | Verilog |
| License | MIT (repo LICENSE; files have no header) |
| FPGA / primitives | any: none (portable) |
| Tests | waveform-only (tutorials/10-CPU/grom_computer_tb.v, $dumpvars/$finish) |

**On ULX3S:** Already ported: ulx3s__fpga-odysseus tutorials/06-CPU (identical grom_cpu.v) with ULX3S LPF.

Full review: [mmicko__fpga101-workshop](../projects/mmicko__fpga101-workshop.md).

**Used by 3 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [lawrie__ulx3s_examples](https://github.com/lawrie/ulx3s_examples) (instantiates [`cpu/grom_computer.v`](https://github.com/lawrie/ulx3s_examples/blob/b6ff00099265401fef4843e4e89c2ac54254c95f/cpu/grom_computer.v))
- [lawrie__ulx4m_examples](https://github.com/lawrie/ulx4m_examples) (instantiates [`softcore/grom/grom_computer.v`](https://github.com/lawrie/ulx4m_examples/blob/415ee5309545da06b1bda7bfe7ec3a1c65a5376c/softcore/grom/grom_computer.v))
- [ulx3s__fpga-odysseus](https://github.com/ulx3s/fpga-odysseus) (instantiates [`tutorials/06-CPU/grom_computer.v`](https://github.com/ulx3s/fpga-odysseus/blob/3f91fd255e07b6570616224f5c2389f29aac6b03/tutorials/06-CPU/grom_computer.v))

### i8080-compatible core (Bashkiria-2M-derived) {#core-i8080-altair}

8080-compatible core lifted from the Bashkiria-2M FPGA replica, wired here into an Altair 8800 emulator (computer/altair.v, computer/top_altair.v) built for ULX3S 25F/85F. Originates from mmicko__fpga101-workshop tutorials/11-Computer (identical i8080.v/altair.v).

| | |
|---|---|
| Repository | [lawrie__ulx3s_examples](https://github.com/lawrie/ulx3s_examples): Lawrie Griffiths Verilog examples: HDMI, displays, PS/2, SDRAM, USB host, CPUs |
| Files | [`computer/i8080.v`](https://github.com/lawrie/ulx3s_examples/blob/b6ff00099265401fef4843e4e89c2ac54254c95f/computer/i8080.v) |
| Top module | `i8080` |
| Language | Verilog |
| License | modified BSD (Copyright (C) 2010 Dmitry Tselikov, LICENSE.TXT referenced in-file) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | waveform-only tb present elsewhere in repo (test68/ps2send), none specific to i8080.v |

**On ULX3S:** computer/top_altair.v is the ready ULX3S top; no other i8080 core was found in the collection.

Full review: [lawrie__ulx3s_examples](../projects/lawrie__ulx3s_examples.md).

**Used by 4 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [lawrie__ulx3s_altair_8800](https://github.com/lawrie/ulx3s_altair_8800) (instantiates [`src/altair.v`](https://github.com/lawrie/ulx3s_altair_8800/blob/e59889fb0b57b3e2606063fa2a86401be34986f6/src/altair.v))
- [lawrie__ulx4m_examples](https://github.com/lawrie/ulx4m_examples) (instantiates [`softcore/altair/altair.v`](https://github.com/lawrie/ulx4m_examples/blob/415ee5309545da06b1bda7bfe7ec3a1c65a5376c/softcore/altair/altair.v))
- [mmicko__fpga101-workshop](https://github.com/mmicko/fpga101-workshop) (instantiates [`tutorials/11-Computer/altair.v`](https://github.com/mmicko/fpga101-workshop/blob/1f5d605bc158810148626df5261bf1dc87cf50a1/tutorials/11-Computer/altair.v))
- [ulx3s__fpga-odysseus](https://github.com/ulx3s/fpga-odysseus) (instantiates [`tutorials/07-Computer/altair.v`](https://github.com/ulx3s/fpga-odysseus/blob/3f91fd255e07b6570616224f5c2389f29aac6b03/tutorials/07-Computer/altair.v))

### TMS9900-family CPU core (public domain) {#core-tms99000-ti99}

'Others' family pick: a public-domain TMS99xxx CPU core (TI-99/4A lineage) built into a complete ULX3S 25F home-computer replica with HDMI, PS/2 and SD card.

| | |
|---|---|
| Repository | [pnru__ti99](https://gitlab.com/pnru/ti99): TI-99/2 in Verilog |
| Files | [`ti99_2/tms99000.v`](https://gitlab.com/pnru/ti99/-/blob/7f71082200736867263aa191d11a22e5d17c330b/ti99_2/tms99000.v) |
| Top module | `tms99000` |
| Language | Verilog |
| License | public domain (file header) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | 1 tb file present |

**On ULX3S:** speccery__icy99 is a second TMS9900-family repo (own core, license none found) if a different implementation is wanted.

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [emard__ti99_2](https://github.com/emard/ti99_2) (instantiates [`evmvdp.v`](https://github.com/emard/ti99_2/blob/f360148fd749bf6f6adc65cf62c37f4721f287d9/evmvdp.v))

### TV80 Z80-compatible core (emard__ulx3s_galaksija copy) {#core-tv80-galaksija}

The Z80-family pick: a Verilog port (TV80) of the well-known T80 VHDL Z80 core, no vendor primitives, and by far the most reused retro CPU in the collection (galaksija, jupiter_ace, msx_fpga, sms/sg-1000/gamegear, trs_80, yazsof...).

| | |
|---|---|
| Repository | [emard__ulx3s_galaksija](https://github.com/emard/ulx3s_galaksija): emard/ulx3s_galaksija: Galaksija Z80 retro-computer core ported to ULX3S |
| Files | [`tv80n.v`](https://github.com/emard/ulx3s_galaksija/blob/ddcbf3a622ad9a38e517b1a88c0b2f6566f59384/tv80n.v), [`tv80_alu.v`](https://github.com/emard/ulx3s_galaksija/blob/ddcbf3a622ad9a38e517b1a88c0b2f6566f59384/tv80_alu.v), [`tv80_reg.v`](https://github.com/emard/ulx3s_galaksija/blob/ddcbf3a622ad9a38e517b1a88c0b2f6566f59384/tv80_reg.v), [`tv80_mcode.v`](https://github.com/emard/ulx3s_galaksija/blob/ddcbf3a622ad9a38e517b1a88c0b2f6566f59384/tv80_mcode.v), [`tv80_core.v`](https://github.com/emard/ulx3s_galaksija/blob/ddcbf3a622ad9a38e517b1a88c0b2f6566f59384/tv80_core.v) |
| Top module | `tv80n` |
| Language | Verilog |
| License | MIT (OpenCores-style header, Copyright (c) 2004 Guy Hutchison, based on Daniel Wallner's VHDL T80) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** This copy already carries a standalone ULX3S build (FPGA_SIZE 12/25/45/85).

**Used by 24 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [cheyao__sega-sms](https://github.com/cheyao/sega-sms) (instantiates [`src/sms.v`](https://github.com/cheyao/sega-sms/blob/c37e846d94f88eb9a95f44b15f2b23019aa25a26/src/sms.v))
- [chriscamacho__yazsof](https://github.com/chriscamacho/YAZSOF) (instantiates [`Z80.v`](https://github.com/chriscamacho/YAZSOF/blob/3a8ff5dcf25dcf149683adf109ac3096caa0a786/Z80.v))
- [danodus__msx_fpga](https://github.com/danodus/msx_fpga) (instantiates [`src/msx.v`](https://github.com/danodus/msx_fpga/blob/f3266f78762094ab3eb5621279011efb504c69df/src/msx.v))
- [danodus__ulx3s_sms](https://github.com/danodus/ulx3s_sms) (instantiates [`src/sms.v`](https://github.com/danodus/ulx3s_sms/blob/13c2361a5039d205de47857bab9201055ac9e566/src/sms.v))
- [emard__galaksija](https://github.com/emard/galaksija) (instantiates [`galaksija.v`](https://github.com/emard/galaksija/blob/ddcbf3a622ad9a38e517b1a88c0b2f6566f59384/galaksija.v))
- [emard__jupiter_ace](https://github.com/emard/jupiter_ace) (instantiates [`src/fpga_ace.v`](https://github.com/emard/jupiter_ace/blob/b7a7b78e2adfe055b4966cbf0878e017b093e429/src/fpga_ace.v))
- [lawrie__jupiter_ace](https://github.com/lawrie/jupiter_ace) (instantiates [`src/fpga_ace.v`](https://github.com/lawrie/jupiter_ace/blob/ace1bce54b1497803d66905b79a083d76429c33e/src/fpga_ace.v))
- [lawrie__ulx3s_amstrad_cpc](https://github.com/lawrie/ulx3s_amstrad_cpc) (instantiates [`src/top.v`](https://github.com/lawrie/ulx3s_amstrad_cpc/blob/f2022b4a1b7153a61c5d7bd35f1f95f3dfe3751e/src/top.v))
- [lawrie__ulx3s_colecovision](https://github.com/lawrie/ulx3s_colecovision) (instantiates [`src/coleco.v`](https://github.com/lawrie/ulx3s_colecovision/blob/4b30cf5419fe201df922f4563c1ec7faa837b7cf/src/coleco.v))
- [lawrie__ulx3s_cpm_z80](https://github.com/lawrie/ulx3s_cpm_z80) (instantiates [`src/Microcomputer/Microcomputer.v`](https://github.com/lawrie/ulx3s_cpm_z80/blob/2ec96bec461c11ec51aee803500c0890ee632f65/src/Microcomputer/Microcomputer.v))
- [lawrie__ulx3s_gamegear](https://github.com/lawrie/ulx3s_gamegear) (instantiates [`src/sms.v`](https://github.com/lawrie/ulx3s_gamegear/blob/17d6e6c9dd013fd9ff3f8586b6268b472b991f75/src/sms.v))
- [lawrie__ulx3s_msx](https://github.com/lawrie/ulx3s_msx) (instantiates [`src/msx.v`](https://github.com/lawrie/ulx3s_msx/blob/9dfefefd181454d04bddcffabcb245d6aef42b48/src/msx.v))
- [lawrie__ulx3s_sg_1000](https://github.com/lawrie/ulx3s_sg_1000) (instantiates [`src/sg1000.v`](https://github.com/lawrie/ulx3s_sg_1000/blob/aabd4509bab9ce19fab11a43d8016c8d63ed49aa/src/sg1000.v))
- [lawrie__ulx3s_sms](https://github.com/lawrie/ulx3s_sms) (instantiates [`src/sms.v`](https://github.com/lawrie/ulx3s_sms/blob/13c2361a5039d205de47857bab9201055ac9e566/src/sms.v))
- [lawrie__ulx3s_trs_80](https://github.com/lawrie/ulx3s_trs_80) (instantiates [`src/trs80.v`](https://github.com/lawrie/ulx3s_trs_80/blob/1f8ec8b3b580bcb99b8459d78ee2602e8d4aa9eb/src/trs80.v))
- … and 9 more (see `data/core_usage.json`)

## Other catalogued projects

Catalogued repos tagged `retro-computer` (71), `retro-console` (20), `retro-arcade` (10) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
