---
title: "Colorlight 5A-75B/E, i5, i9"
parent: "ECP5 boards"
grand_parent: "Boards"
nav_order: 4
---
<!-- Generated from data/boards.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# Colorlight 5A-75B/E, i5, i9

Cheap ECP5 boards with gigabit Ethernet PHYs and SDRAM, repurposed from LED-panel receivers.

| | |
|---|---|
| Board | Colorlight LED-receiver cards and SODIMM modules |
| FPGA | LFE5U-25F (5A-75B/E, i5), LFE5U-45F (i9), CABGA256/CABGA381 |
| Evidence | catalogue rows (wuxx__colorlight-fpga-projects, datanoisetv__colorlight-i9-aes67) |
| Clock | 25 MHz (catalogue notes) |
| Catalogued repos | 7 |

*The description is a short summary; FPGA facts come from the catalogue rows cited above.*

## Constraint files (LPF)

Most-copied distinct LPFs for this board in the cloned repos (from the [LPF catalogue](https://github.com/kelu124/ulx3s-klod/blob/main/methodology/lpf-catalogue.md)).

| LPF | Revision | Copies | Peripherals constrained |
|---|---|---|---|
| [`blink.lpf`](https://github.com/kholia/Colorlight-5A-75B/blob/9d4433be7c9a719af739fa958889c98b05a91515/blink/blink.lpf) (kholia__colorlight-5a-75b) | unknown | 2 | led |
| [`colorlighti5.lpf`](https://github.com/splinedrive/kianRiscV/blob/da994e6c25b0667d6579922f4bab8d800d19e944/linux_socs/kianv_mc_rv32ima_sv32/engineering/boards/colorlighti5/colorlighti5.lpf) (splinedrive__kianriscv) | unknown | 2 | adc, button, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, psram, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb |
| [`darksocv.lpf`](https://github.com/darklife/darkriscv/blob/974034aa8079039a36b89c14dcdfed575de183b7/boards/colorlighti5/darksocv.lpf) (darklife__darkriscv) | unknown | 2 | ftdi-uart, led |
| [`dds.lpf`](https://github.com/kholia/Colorlight-5A-75B/blob/9d4433be7c9a719af739fa958889c98b05a91515/dds_ssb_docker/dds.lpf) (kholia__colorlight-5a-75b) | unknown | 2 | led, radio-antenna |
| [`blink.lpf`](https://github.com/kholia/Colorlight-5A-75B/blob/9d4433be7c9a719af739fa958889c98b05a91515/blink_docker/blink.lpf) (kholia__colorlight-5a-75b) | unknown | 1 | led |
| [`blink.lpf`](https://github.com/wuxx/Colorlight-FPGA-Projects/blob/5042201f6ae848d4269680cc289c7bde3ab8cf71/src/i5/blink/blink.lpf) (wuxx__colorlight-fpga-projects) | unknown | 1 | led |
| [`blink.lpf`](https://github.com/wuxx/Colorlight-FPGA-Projects/blob/5042201f6ae848d4269680cc289c7bde3ab8cf71/src/i9/blink/blink.lpf) (wuxx__colorlight-fpga-projects) | unknown | 1 | led |
| [`blinky.lpf`](https://github.com/fusesoc/blinky/blob/496eae5e447151c1ca720f995d292e2e99349b22/colorlight_5a75b/blinky.lpf) (fusesoc__blinky) | unknown | 1 |  |
| [`colorlight-i5.lpf`](https://github.com/racerxdl/colorlight-picorv32/blob/73daf2842c5c1fc147bc59c4589d2150a260fe6b/constraints/colorlight-i5.lpf) (racerxdl__colorlight-picorv32) | unknown | 1 | ftdi-uart, gpio-header, led, sdram |
| [`colorlight_5A-75B.lpf`](https://github.com/antonblanchard/chiselwatt/blob/61a07a99046f8ffe56f33918c8f9685ab7a75fb5/constraints/colorlight_5A-75B.lpf) (antonblanchard__chiselwatt) | unknown | 1 |  |
| [`colorlight_i9_v7.2.lpf`](https://github.com/DatanoiseTV/colorlight-i9-aes67/blob/71420b772d48409ae8e3a70c3103828495687737/constraints/colorlight_i9_v7.2.lpf) (datanoisetv__colorlight-i9-aes67) | unknown | 1 | audio, ethernet, led, sdram, spi-flash |
| [`colorlight_i9_v7.2.lpf`](https://github.com/sylefeb/Silice/blob/620487d6b83035dd98299734c8c8fccf8f636005/frameworks/boards/colorlight/colorlight_i9_v7.2.lpf) (sylefeb__silice) | unknown | 1 | ftdi-uart, hdmi-dvi, led, rtc-power, sdram, spi-flash |

## Reusable cores seen on this board

Cores whose source repo, or a repo that copies/instantiates them, targets this board.

| Core | Function | Source repo |
|---|---|---|
| PicoRV32 RISC-V core | [cpu-riscv](https://github.com/kelu124/ulx3s-klod/blob/main/functions/cpu-riscv.md) | yosyshq__picorv32 |
| Gigabit RGMII MAC | [ethernet](https://github.com/kelu124/ulx3s-klod/blob/main/functions/ethernet.md) | datanoisetv__colorlight-i9-aes67 |
| MDIO Clause-22 management controller | [ethernet](https://github.com/kelu124/ulx3s-klod/blob/main/functions/ethernet.md) | sefbkn__versa-ecp5-demo |
| vga2dvid + tmds_encoder DVI/TMDS core (Mike Field / EMARD) | [hdmi-dvi](https://github.com/kelu124/ulx3s-klod/blob/main/functions/hdmi-dvi.md) | emard__ulx3s-misc |
| ECP5 JTAGG demo (Ecp5JtagDemo) | [jtag-debug](https://github.com/kelu124/ulx3s-klod/blob/main/functions/jtag-debug.md) | tomverbeure__ecp5_jtag |
| HUB75e LED panel driver (colorlight-led-cube) | [led-drivers](https://github.com/kelu124/ulx3s-klod/blob/main/functions/led-drivers.md) | lucysrausch__colorlight-led-cube |
| ecp5pll parametric PLL | [pll-clock](https://github.com/kelu124/ulx3s-klod/blob/main/functions/pll-clock.md) | emard__ulx3s-misc |

## Projects targeting this board

- [datanoisetv__colorlight-i9-aes67](https://github.com/DatanoiseTV/colorlight-i9-aes67): AES67/RAVENNA audio-over-IP bridge for Colorlight i9 v7.2: hardware PTP
- [hassan2203__system-on-chip-soc-design-and-verification](https://github.com/Hassan2203/System-On-Chip-SOC-Design-and-verification): RV32I single-cycle CPU + Wishbone bus SoC teaching project, built for Colorlight i5
- [kholia__colorlight-5a-75b](https://github.com/kholia/Colorlight-5A-75B): Colorlight 5A-75B: notes + example projects
- [lucysrausch__colorlight-led-cube](https://github.com/lucysrausch/colorlight-led-cube): Colorlight 5A-75B "LED cube" hack: HUB75e RGB panel driver
- [racerxdl__colorlight-picorv32](https://github.com/racerxdl/colorlight-picorv32): Colorlight I5 PicoRV32 example: minimal RV32I SoC
- [tomverbeure__ecp5_jtag](https://github.com/tomverbeure/ecp5_jtag): Colorlight i5: reverse-engineering notes plus a SpinalHDL/Verilog example demonstrating the Lattice ECP5 JTAGG…
- [wuxx__colorlight-fpga-projects](https://github.com/wuxx/Colorlight-FPGA-Projects): Colorlight i5/i9/i9plus/5a-75b: vendor example collection
{% endraw %}
