---
title: "PS/2 keyboard and mouse"
parent: "Cores by function"
nav_order: 20
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# PS/2 keyboard and mouse

PS/2 keyboard and mouse interfaces.

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [ps2_intf keyboard decoder](#core-lawrie-ps2-intf) ★ | [lawrie__ulx3s_examples](https://github.com/lawrie/ulx3s_examples) | Verilog | none found | any | 7 |
| [f32c ps2 VHDL core](#core-f32c-ps2) | [f32c__f32c](https://github.com/f32c/f32c) | VHDL | MIT (file header, Copyright 2015 Ken Jordan) | any | 0 |
| [ps2_port bidirectional PS/2](#core-lawrie-ps2-port) | [lawrie__ulx3s_examples](https://github.com/lawrie/ulx3s_examples) | Verilog | none found | any | 0 |
| [ps2kbd + ps2mouse (EMARD)](#core-emard-ps2kbd-ps2mouse) | [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc) | Verilog | BSD (ps2kbd.v header: AUTHOR=Paul Ruiz,… | any | 6 |

## Cores

### ps2_intf keyboard decoder (best) {#core-lawrie-ps2-intf}

Input-only PS/2 keyboard interface: clock filtering, 11-bit frame shift-in, byte-valid strobe. The most widely-copied PS/2 core in the collection.

| | |
|---|---|
| Repository | [lawrie__ulx3s_examples](https://github.com/lawrie/ulx3s_examples): Lawrie Griffiths Verilog examples: HDMI, displays, PS/2, SDRAM, USB host, CPUs |
| Files | [`ps2/ps2.v`](https://github.com/lawrie/ulx3s_examples/blob/b6ff00099265401fef4843e4e89c2ac54254c95f/ps2/ps2.v) |
| Top module | `ps2_intf` |
| Language | Verilog |
| License | none found |
| FPGA / primitives | any: none (portable) |
| Tests | ps2/ps2_test.v exists but is waveform-only, no PASS/FAIL |

**On ULX3S:** Same file copied verbatim into hoglet67__ice40beeb, hoglet67__ice40atom, lawrie__ulx3s_bbc_micro, lawrie__ulx3s_acorn_atom, lawrie__blackicemxbook, lawrie__verilog_examples.

Full review: [lawrie__ulx3s_examples](../projects/lawrie__ulx3s_examples.md).

**Used by 7 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [emard__uk101onfpga](https://github.com/emard/UK101onFPGA) (instantiates [`Components/PS2KB/UK101keyboard.vhd`](https://github.com/emard/UK101onFPGA/blob/7264146bca76c6f751039ab569824a59875fe976/Components/PS2KB/UK101keyboard.vhd))
- [hoglet67__ice40atom](https://github.com/hoglet67/Ice40Atom) (instantiates [`src/keyboard.v`](https://github.com/hoglet67/Ice40Atom/blob/28e4363ddff93487ad56b9215b87d008e8db8df8/src/keyboard.v))
- [hoglet67__ice40beeb](https://github.com/hoglet67/Ice40Beeb) (instantiates [`src/keyboard.v`](https://github.com/hoglet67/Ice40Beeb/blob/e0fe38d9ab843e82e1d2676e977b47b7740d8d52/src/keyboard.v))
- [lawrie__blackicemxbook](https://github.com/lawrie/blackicemxbook) (instantiates [`examples/input/ps2/ps2_test.v`](https://github.com/lawrie/blackicemxbook/blob/ff5fdb31c85d20eacbe24b1bf8f5ed2e0df0bb8f/examples/input/ps2/ps2_test.v))
- [lawrie__ulx3s_acorn_atom](https://github.com/lawrie/ulx3s_acorn_atom) (instantiates [`src/keyboard.v`](https://github.com/lawrie/ulx3s_acorn_atom/blob/8364160ee406e127ea9f82f8cd49803e51565112/src/keyboard.v))
- [lawrie__ulx3s_bbc_micro](https://github.com/lawrie/ulx3s_bbc_micro) (instantiates [`src/keyboard.v`](https://github.com/lawrie/ulx3s_bbc_micro/blob/ea90cb6c75fbaef1b78df7f5cc7dbe2502967a22/src/keyboard.v))
- [lawrie__verilog_examples](https://github.com/lawrie/verilog_examples) (instantiates [`fpga/computer/vga_test.v`](https://github.com/lawrie/verilog_examples/blob/ee8f0d2b44313b683a63ea6a0b151f454f8b9ddc/fpga/computer/vga_test.v))

### f32c ps2 VHDL core {#core-f32c-ps2}

PS/2 keyboard/mouse interface entity used in the f32c SoC library.

| | |
|---|---|
| Repository | [f32c__f32c](https://github.com/f32c/f32c): f32c: retargetable RISC-V/MIPS 32-bit soft CPU + SoC library |
| Files | [`rtl/soc/ps2.vhd`](https://github.com/f32c/f32c/blob/7dbf56d42a94ae599eabfd1e7fa15db14a10afd7/rtl/soc/ps2.vhd) |
| Top module | `ps2` |
| Language | VHDL |
| License | MIT (file header, Copyright 2015 Ken Jordan) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** VHDL, no vendor primitives; pair with f32c's own SoC memory map or lift standalone.

Full review: [f32c__f32c](../projects/f32c__f32c.md).

### ps2_port bidirectional PS/2 {#core-lawrie-ps2-port}

Bidirectional PS/2 port (adds host-to-device writes, e.g. keyboard LEDs) built on the same ps2_intf lineage.

| | |
|---|---|
| Repository | [lawrie__ulx3s_examples](https://github.com/lawrie/ulx3s_examples): Lawrie Griffiths Verilog examples: HDMI, displays, PS/2, SDRAM, USB host, CPUs |
| Files | [`ps2port/ps2_port.v`](https://github.com/lawrie/ulx3s_examples/blob/b6ff00099265401fef4843e4e89c2ac54254c95f/ps2port/ps2_port.v) |
| Top module | `ps2_port` |
| Language | Verilog |
| License | none found |
| FPGA / primitives | any: none (portable) |
| Tests | ps2port/ps2_test.v exists, waveform-only |

**On ULX3S:** Use when a design needs to set keyboard LEDs or otherwise talk back on the PS/2 bus, not just decode input.

Full review: [lawrie__ulx3s_examples](../projects/lawrie__ulx3s_examples.md).

### ps2kbd + ps2mouse (EMARD) {#core-emard-ps2kbd-ps2mouse}

Separate keyboard decoder and a full 3-byte PS/2 mouse controller with automatic power-up initialization.

| | |
|---|---|
| Repository | [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc): ULX3S misc/advanced examples: EMARD's building-block library |
| Files | [`examples/ps2/kbd/hdl/ps2kbd.v`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/ps2/kbd/hdl/ps2kbd.v), [`examples/ps2/mouse/hdl/ps2mouse.v`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/ps2/mouse/hdl/ps2mouse.v) |
| Top module | `ps2kbd` |
| Language | Verilog |
| License | BSD (ps2kbd.v header: AUTHOR=Paul Ruiz, LICENSE=BSD); ps2mouse.v: none found |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** ps2kbd.v reused in stuij__odyssey and danodus__xgsoc; ps2mouse.v reused in danodus__xgsoc and the emard/linuxjedi minimig_ecs forks.

Full review: [emard__ulx3s-misc](../projects/emard__ulx3s-misc.md).

**Used by 6 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [danodus__xgsoc](https://github.com/danodus/xgsoc) (instantiates [`rtl/soc_top.sv`](https://github.com/danodus/xgsoc/blob/8a4d9213e5ebe3abe42ba30fddb0bd4f9f4a843f/rtl/soc_top.sv))
- [emard__minimig_ecs](https://github.com/emard/Minimig_ECS) (instantiates [`source_emard/Userio.v`](https://github.com/emard/Minimig_ECS/blob/a0a94bfa0b8534f50be7b79086ad00a41184c266/source_emard/Userio.v))
- [linuxjedi__minimig_ecs](https://github.com/LinuxJedi/Minimig_ECS) (instantiates [`source_emard/Userio.v`](https://github.com/LinuxJedi/Minimig_ECS/blob/a0a94bfa0b8534f50be7b79086ad00a41184c266/source_emard/Userio.v))
- [pnru__ti99](https://gitlab.com/pnru/ti99) (instantiates [`ti99_2/ps2kb.v`](https://gitlab.com/pnru/ti99/-/blob/7f71082200736867263aa191d11a22e5d17c330b/ti99_2/ps2kb.v))
- [speccery__icy99](https://github.com/Speccery/icy99) (instantiates [`src/ps2kb.v`](https://github.com/Speccery/icy99/blob/512915b98e8088e6a23d63ffd55bed9a84c25634/src/ps2kb.v))
- [stuij__odyssey](https://github.com/stuij/odyssey) (instantiates [`verilog/odyssey_top.v`](https://github.com/stuij/odyssey/blob/e74caa83d9fb9e21f96ac63e0fdd0d7b945dbfe1/verilog/odyssey_top.v))

## Other catalogued projects

Catalogued repos tagged `ps2` (58) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
