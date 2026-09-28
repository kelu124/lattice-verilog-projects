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
| [ECPIX-5](ecpix-5.md) | LFE5UM5G-45F or LFE5UM5G-85F (ECP5-5G, with SERDES), BG554 | ECP5-5G board with DDR3, RGMII Ethernet, HDMI (IT6613), a SATA port driven by LiteSATA over the SERDES, SD, ULPI USB and 8 PMODs; programmed with openFPGALoader -b ecpix5. |
| [Cynthion](cynthion.md) | LFE5U-12F, BG256 | USB 2.0 test instrument: three ULPI high-speed USB PHYs, HyperRAM, 2 PMODs; programmed through the Apollo debug MCU. Home of the LUNA USB gateware (analyzer, Facedancer, USB host experiments). |
{% endraw %}
