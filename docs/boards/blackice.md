---
title: "BlackIce II / Mx"
parent: "iCE40 HX8K / HX4K boards"
grand_parent: "Boards"
nav_order: 2
---
<!-- Generated from data/boards.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# BlackIce II / Mx

HX4K + STM32 board (the MCU loads the FPGA); retro computers by hoglet67 and lawrie's examples.

| | |
|---|---|
| Board | myStorm BlackIce II and BlackIce Mx |
| FPGA | iCE40 HX4K, TQ144 (built as --hx8k --package tq144:4k) |
| Evidence | catalogue rows (mystorm-org__blackice-ii, hoglet67__ice40atom) |
| Clock | unknown |
| Catalogued repos | 7 |

*The description is a short summary; FPGA facts come from the catalogue rows cited above.*

## Constraint files (PCF)

| PCF | Repository |
|---|---|
| [`boards/blackice2/yosys/blackice2.pcf`](https://github.com/alangarf/apple-one/blob/0f15ef6d62c2f8820aa5a68b7f973eef4a78dd8d/boards/blackice2/yosys/blackice2.pcf) | alangarf__apple-one |
| [`blackice/blackice.pcf`](https://github.com/hoglet67/Ice40Atom/blob/28e4363ddff93487ad56b9215b87d008e8db8df8/blackice/blackice.pcf) | hoglet67__ice40atom |
| [`blackice2/blackice.pcf`](https://github.com/hoglet67/Ice40Atom/blob/28e4363ddff93487ad56b9215b87d008e8db8df8/blackice2/blackice.pcf) | hoglet67__ice40atom |
| [`target/blackice/Src/blackice.pcf`](https://github.com/hoglet67/Ice40Atom/blob/28e4363ddff93487ad56b9215b87d008e8db8df8/target/blackice/Src/blackice.pcf) | hoglet67__ice40atom |
| [`blackice/blackice.pcf`](https://github.com/hoglet67/Ice40Beeb/blob/e0fe38d9ab843e82e1d2676e977b47b7740d8d52/blackice/blackice.pcf) | hoglet67__ice40beeb |
| [`blackice2/blackice.pcf`](https://github.com/hoglet67/Ice40Beeb/blob/e0fe38d9ab843e82e1d2676e977b47b7740d8d52/blackice2/blackice.pcf) | hoglet67__ice40beeb |
| [`target/blackice/Src/blackice.pcf`](https://github.com/hoglet67/Ice40Beeb/blob/e0fe38d9ab843e82e1d2676e977b47b7740d8d52/target/blackice/Src/blackice.pcf) | hoglet67__ice40beeb |
| [`fpga/qspiplay/fpga/blackice.pcf`](https://github.com/lawrie/verilog_examples/blob/ee8f0d2b44313b683a63ea6a0b151f454f8b9ddc/fpga/qspiplay/fpga/blackice.pcf) | lawrie__verilog_examples |
| [`fpga/oscilloscope/blackice.pcf`](https://github.com/lawrie/verilog_examples/blob/ee8f0d2b44313b683a63ea6a0b151f454f8b9ddc/fpga/oscilloscope/blackice.pcf) | lawrie__verilog_examples |
| [`fpga/voice/blackice.pcf`](https://github.com/lawrie/verilog_examples/blob/ee8f0d2b44313b683a63ea6a0b151f454f8b9ddc/fpga/voice/blackice.pcf) | lawrie__verilog_examples |
| [`fpga/flashy/blackice.pcf`](https://github.com/lawrie/verilog_examples/blob/ee8f0d2b44313b683a63ea6a0b151f454f8b9ddc/fpga/flashy/blackice.pcf) | lawrie__verilog_examples |
| [`firmware/Src/blackice.pcf`](https://github.com/mystorm-org/BlackIce-II/blob/77474a3cd72b149cc86b580e151d85ec93c7e440/firmware/Src/blackice.pcf) | mystorm-org__blackice-ii |

## Reusable cores seen on this board

Cores whose source repo, or a repo that copies/instantiates them, targets this board.

| Core | Function | Source repo |
|---|---|---|
| MiST composite/RGB scandoubler (composite-video input side) | [composite-video](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/composite-video.md) | hoglet67__ice40beeb |
| vga2dvid + tmds_encoder DVI/TMDS core (Mike Field / EMARD) | [hdmi-dvi](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/hdmi-dvi.md) | emard__ulx3s-misc |
| HUB75e LED panel driver (colorlight-led-cube) | [led-drivers](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/led-drivers.md) | lucysrausch__colorlight-led-cube |
| ps2_intf keyboard decoder | [ps2](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/ps2.md) | lawrie__ulx3s_examples |
| LAYR_AUDIO SID6581 sound chip core | [sound-chips](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/sound-chips.md) | thorkn__layr_audio |
| SN76489 PSG (sound chip) | [sound-chips](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/sound-chips.md) | lawrie__ulx3s_sms |
| MiST composite/RGB scandoubler (15kHz to VGA) | [vga](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/vga.md) | hoglet67__ice40beeb |
| vga_core / vga_timing portable VGA generator (Black Mesa Labs) | [vga](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/vga.md) | icebreaker-fpga__icebreaker-verilog-examples |

## Projects targeting this board

- [alangarf__apple-one](https://github.com/alangarf/apple-one): Multi-board
- [hoglet67__ice40atom](https://github.com/hoglet67/Ice40Atom): Ice40Atom: Acorn Atom 6502 retro-computer core
- [hoglet67__ice40beeb](https://github.com/hoglet67/Ice40Beeb): Ice40Beeb: BBC Micro Model B retro-computer core
- [lawrie__blackicemxbook](https://github.com/lawrie/blackicemxbook): BlackIce Mx open-source-FPGA book
- [lawrie__hdmi_examples](https://github.com/lawrie/hdmi_examples): iCE40 open-source HDMI/DVI examples for BlackIce II: hdmi_test/_ibr/_mx
- [lawrie__verilog_examples](https://github.com/lawrie/verilog_examples): Lawrie Griffiths Verilog examples for BlackIce II: ~157 files across ebook
- [mystorm-org__blackice-ii](https://github.com/mystorm-org/BlackIce-II): BlackIce II: myStorm board repo - Verilog example designs
{% endraw %}
