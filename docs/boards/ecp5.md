---
title: "ECP5 boards"
parent: "Boards"
nav_order: 1
has_children: true
---
<!-- Generated from data/boards.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# ECP5 boards

Lattice ECP5 (LFE5U/LFE5UM): 12k–85k LUTs, DSP blocks, SERDES on 5G parts; open flow yosys + nextpnr-ecp5 + ecppack.

| Board | FPGA | Description |
|---|---|---|
| [ULX3S](ulx3s.md) | LFE5U-12F/25F/45F/85F, CABGA381 | The main board of this collection: 32 MB SDR SDRAM, GPDI (HDMI) port, ESP32, US1 FT231X + US2 direct USB, SD card, MAX11125 ADC, OLED header, 56 GPIO. |
| [ULX4M](ulx4m.md) | LFE5UM-85F (ECP5-5G) on the variants catalogued | ULX3S successor in Raspberry Pi CM4 module format; most ULX3S designs port with the ulx4m_v002.lpf constraint file. |
| [OrangeCrab](orangecrab.md) | LFE5U-25F or 85F, CSFBGA285 | Feather-format ECP5 board with DDR3 and native USB; DFU bootloader. |
| [Colorlight 5A-75B/E, i5, i9](colorlight.md) | LFE5U-25F (5A-75B/E, i5), LFE5U-45F (i9), CABGA256/CABGA381 | Cheap ECP5 boards with gigabit Ethernet PHYs and SDRAM, repurposed from LED-panel receivers. |
| [IcePi Zero](icepi-zero.md) | LFE5U-25F, CABGA256 | Raspberry Pi Zero-sized ECP5 board with HDMI, SDRAM and USB; many ULX3S retro ports target it. |
| [iCESugar-Pro](icesugar-pro.md) | LFE5U-25F, CABGA256 | SODIMM-format ECP5 module with SDRAM and HDMI on the carrier. |
{% endraw %}
