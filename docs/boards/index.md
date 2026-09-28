---
title: "Boards"
nav_order: 3
has_children: true
permalink: "/boards/"
---
<!-- Generated from data/boards.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# Boards

The most relevant boards of the collection, in three FPGA families. Each page gives the FPGA, the constraint files found in the cloned repos, the reusable cores known to run on it and the projects that target it.

## [ECP5 boards](ecp5.md)

Lattice ECP5 (LFE5U/LFE5UM): 12k–85k LUTs, DSP blocks, SERDES on 5G parts; open flow yosys + nextpnr-ecp5 + ecppack.

| Board | FPGA | Catalogued repos |
|---|---|---|
| [ULX3S](ulx3s.md) | LFE5U-12F/25F/45F/85F, CABGA381 | 373 |
| [ULX4M](ulx4m.md) | LFE5UM-85F (ECP5-5G) on the variants catalogued | 21 |
| [OrangeCrab](orangecrab.md) | LFE5U-25F or 85F, CSFBGA285 | 13 |
| [Colorlight 5A-75B/E, i5, i9](colorlight.md) | LFE5U-25F (5A-75B/E, i5), LFE5U-45F (i9), CABGA256/CABGA381 | 10 |
| [IcePi Zero](icepi-zero.md) | LFE5U-25F, CABGA256 | 10 |
| [iCESugar-Pro](icesugar-pro.md) | LFE5U-25F, CABGA256 | 3 |
| [ECPIX-5](ecpix-5.md) | LFE5UM5G-45F or LFE5UM5G-85F (ECP5-5G, with SERDES), BG554 | 12 |
| [Cynthion](cynthion.md) | LFE5U-12F, BG256 | 8 |

## [iCE40 UP5K boards](up5k.md)

Lattice iCE40 UltraPlus UP5K: 5.3k LUTs, 128 KB SPRAM, DSP, RGB driver; open flow yosys + nextpnr-ice40 + icepack. Cores use SB_* primitives.

| Board | FPGA | Catalogued repos |
|---|---|---|
| [iCEBreaker](icebreaker.md) | iCE40 UP5K, SG48 | 32 |
| [UPduino](upduino.md) | iCE40 UP5K, SG48 | 8 |
| [iCESugar](icesugar.md) | iCE40 UP5K, SG48 | 5 |
| [Fomu](fomu.md) | iCE40 UP5K, UWG30 | 7 |
| [pico-ice](pico-ice.md) | iCE40 UP5K, SG48 | 4 |

## [iCE40 HX8K / HX4K boards](hx.md)

Lattice iCE40 HX8K/HX4K (HX4K is the HX8K die, built with --hx8k --package ...:4k): 7.7k LUTs; open flow yosys + nextpnr-ice40 (older designs: arachne-pnr).

| Board | FPGA | Catalogued repos |
|---|---|---|
| [iCE40-HX8K Breakout](hx8k-breakout.md) | iCE40 HX8K, CT256 | 7 |
| [BlackIce II / Mx](blackice.md) | iCE40 HX4K, TQ144 (built as --hx8k --package tq144:4k) | 7 |
| [iceFUN](icefun.md) | iCE40 HX8K, CB132 | 3 |
| [Olimex iCE40HX8K-EVB](olimex-hx8k.md) | iCE40 HX8K, CT256 | 3 |
| [IcoBoard](icoboard.md) | iCE40 HX8K, CT256 | 2 |
{% endraw %}
