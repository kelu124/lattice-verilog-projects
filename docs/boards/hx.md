---
title: "iCE40 HX8K / HX4K boards"
parent: "Boards"
nav_order: 3
has_children: true
---
<!-- Generated from data/boards.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# iCE40 HX8K / HX4K boards

Lattice iCE40 HX8K/HX4K (HX4K is the HX8K die, built with --hx8k --package ...:4k): 7.7k LUTs; open flow yosys + nextpnr-ice40 (older designs: arachne-pnr).

| Board | FPGA | Description |
|---|---|---|
| [iCE40-HX8K Breakout](hx8k-breakout.md) | iCE40 HX8K, CT256 | Lattice's HX8K evaluation board, target of many IceStorm-era examples. |
| [BlackIce II / Mx](blackice.md) | iCE40 HX4K, TQ144 (built as --hx8k --package tq144:4k) | HX4K + STM32 board (the MCU loads the FPGA); retro computers by hoglet67 and lawrie's examples. |
| [iceFUN](icefun.md) | iCE40 HX8K, CB132 | Small HX8K board used by mikeakohn's CPU projects. |
| [Olimex iCE40HX8K-EVB](olimex-hx8k.md) | iCE40 HX8K, CT256 | Olimex HX8K evaluation board with SRAM; xv6 RISC-V computer and Apple-1 ports. |
| [IcoBoard](icoboard.md) | iCE40 HX8K, CT256 | HX8K Raspberry Pi HAT with SRAM; icosoc SoC generator. |
{% endraw %}
