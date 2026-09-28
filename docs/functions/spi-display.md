---
title: "SPI OLED / LCD displays"
parent: "Cores by function"
nav_order: 4
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# SPI OLED / LCD displays

Drivers for ST7789, SSD1331, SSD1351, SSD1306 and similar small SPI displays.

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [lcd_video / spi_display multi-panel SPI LCD driver](#core-emard-spi-display) ★ | [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc) | Verilog, VHDL | BSD (file headers: "AUTHORS=EMARD,MMICKO and… | any | 18 |
| [bit-bang SPI LCD driver (Apollo 11 FPGA)](#core-mikeakohn-display-spi) | [mikeakohn__apollo11_fpga](https://github.com/mikeakohn/apollo11_fpga) | Verilog | MIT (LICENSE, Copyright 2024 Michael Kohn) | iCE40 | 0 |
| [RasteriCEr SPI display controller](#core-rastericer-display-spi) | [toni3141__rastericer](https://github.com/ToNi3141/RasteriCEr) | Verilog | GPL-3.0-or-later | iCE40 | 0 |
| [Silice OLED drivers (ST7789/SSD1351/SSD1331)](#core-silice-oled-drivers) | [sylefeb__silice](https://github.com/sylefeb/Silice) | Silice | MIT (per-file header, "MIT license, see… | any | 0 |
| [SlabBoy ST7789 SpinalHDL LCD driver](#core-slabboy-st7789) | [lawrie__slabboy](https://github.com/lawrie/slabboy) | SpinalHDL | MIT (LICENSE, Copyright 2018 Craig Bishop) | ECP5 | 6 |
| [SSD1322 OLED framebuffer driver (m68k-ulx3s)](#core-nullobject-oled-ssd1322) | [nullobject__m68k-ulx3s](https://github.com/nullobject/m68k-ulx3s) | Verilog | none found | ECP5 | 4 |

## Cores

### lcd_video / spi_display multi-panel SPI LCD driver (best) {#core-emard-spi-display}

VGA-clocked-in, SPI-clocked-out display driver; swaps ST7789/SSD1331/SSD1351/SSD1306 panels via a selectable init byte-sequence .mem file, free-running or synced to hsync/vsync/blank.

| | |
|---|---|
| Repository | [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc): ULX3S misc/advanced examples: EMARD's building-block library |
| Files | [`examples/spi_display/hdl/spi_display_verilog/lcd_video.v`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/spi_display/hdl/spi_display_verilog/lcd_video.v), [`examples/spi_display/hdl/spi_display_vhdl/spi_display.vhd`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/spi_display/hdl/spi_display_vhdl/spi_display.vhd) |
| Top module | `lcd_video` |
| Language | Verilog, VHDL |
| License | BSD (file headers: "AUTHORS=EMARD,MMICKO and Lawrie Griffiths / LICENSE=BSD"; VHDL twin "AUTHOR=EMARD / LICENSE=BSD") |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Pick the matching *_linit*.mem for your panel/orientation; c_clk_spi_mhz up to 125 MHz for the ST7789 default parameters.

Full review: [emard__ulx3s-misc](../projects/emard__ulx3s-misc.md).

**Used by 18 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [cheyao__sega-sms](https://github.com/cheyao/sega-sms) (copies [`src/spi_display/lcd_video.v`](https://github.com/cheyao/sega-sms/blob/c37e846d94f88eb9a95f44b15f2b23019aa25a26/src/spi_display/lcd_video.v))
- [danodus__ulx3s_68k](https://github.com/danodus/ulx3s_68k) (instantiates [`src/test68.v`](https://github.com/danodus/ulx3s_68k/blob/ee10339210d0c302143745d3cc584a21a4878ace/src/test68.v))
- [danodus__ulx3s_sms](https://github.com/danodus/ulx3s_sms) (instantiates [`src/sms.v`](https://github.com/danodus/ulx3s_sms/blob/13c2361a5039d205de47857bab9201055ac9e566/src/sms.v))
- [emard__apple2fpga](https://github.com/emard/apple2fpga) (instantiates [`rtl_emard/lattice/top/ulx3s_v20_apple2.vhd`](https://github.com/emard/apple2fpga/blob/0ad84ae2f9d9d5cc0e8db6128d630a9e16cdd6de/rtl_emard/lattice/top/ulx3s_v20_apple2.vhd))
- [emard__ulx3s_c64](https://github.com/emard/ulx3s_c64) (instantiates [`rtl/top_ulx3s_v20_c64.vhd`](https://github.com/emard/ulx3s_c64/blob/cc412a9134ed42d4296f1afb523d556b68bb74ba/rtl/top_ulx3s_v20_c64.vhd))
- [emard__ulx3s_vic_20](https://github.com/emard/ulx3s_vic_20) (instantiates [`src/vic20.v`](https://github.com/emard/ulx3s_vic_20/blob/c902419dcea50ec65f420f77a3f326a2bbde87a5/src/vic20.v))
- [lawrie__fpga_pio](https://github.com/lawrie/fpga_pio) (instantiates [`src/top/uart_rx.v`](https://github.com/lawrie/fpga_pio/blob/f38be97cdfa86d4551c96bb98599e3443000628b/src/top/uart_rx.v))
- [lawrie__ulx3s_68k](https://github.com/lawrie/ulx3s_68k) (instantiates [`src/test68.v`](https://github.com/lawrie/ulx3s_68k/blob/ee10339210d0c302143745d3cc584a21a4878ace/src/test68.v))
- [lawrie__ulx3s_amstrad_cpc](https://github.com/lawrie/ulx3s_amstrad_cpc) (instantiates [`src/top.v`](https://github.com/lawrie/ulx3s_amstrad_cpc/blob/f2022b4a1b7153a61c5d7bd35f1f95f3dfe3751e/src/top.v))
- [lawrie__ulx3s_atari_2600](https://github.com/lawrie/ulx3s_atari_2600) (instantiates [`src/atari_2600.v`](https://github.com/lawrie/ulx3s_atari_2600/blob/9a9100a0e7281cc2dff10aafa6edf4e8e453c56b/src/atari_2600.v))
- [lawrie__ulx3s_examples](https://github.com/lawrie/ulx3s_examples) (instantiates [`sdram16/testram.v`](https://github.com/lawrie/ulx3s_examples/blob/b6ff00099265401fef4843e4e89c2ac54254c95f/sdram16/testram.v))
- [lawrie__ulx3s_gamegear](https://github.com/lawrie/ulx3s_gamegear) (instantiates [`src/sms.v`](https://github.com/lawrie/ulx3s_gamegear/blob/17d6e6c9dd013fd9ff3f8586b6268b472b991f75/src/sms.v))
- [lawrie__ulx3s_mac128](https://github.com/lawrie/ulx3s_mac128) (instantiates [`src/mac128.v`](https://github.com/lawrie/ulx3s_mac128/blob/cd3ef1e92e4415b9955a8554a0ae253aae9850d7/src/mac128.v))
- [lawrie__ulx3s_ql](https://github.com/lawrie/ulx3s_ql) (instantiates [`src/ql.v`](https://github.com/lawrie/ulx3s_ql/blob/5a982274a1402dc8273799c5d8d76b6759086719/src/ql.v))
- [lawrie__ulx3s_sms](https://github.com/lawrie/ulx3s_sms) (instantiates [`src/sms.v`](https://github.com/lawrie/ulx3s_sms/blob/13c2361a5039d205de47857bab9201055ac9e566/src/sms.v))
- … and 3 more (see `data/core_usage.json`)

### bit-bang SPI LCD driver (Apollo 11 FPGA) {#core-mikeakohn-display-spi}

Small bit-banged SPI LCD driver, plain Verilog with no vendor primitives; built for an iCE40 HX8K AGC (Apollo Guidance Computer) replica board.

| | |
|---|---|
| Repository | [mikeakohn__apollo11_fpga](https://github.com/mikeakohn/apollo11_fpga): Apollo Guidance Computer CPU reimplementation for iceFUN |
| Files | [`src/display_spi.v`](https://github.com/mikeakohn/apollo11_fpga/blob/7c7b76847c3916d7b3911d8a71ac08bead19f259/src/display_spi.v) |
| Top module | `display_spi` |
| Language | Verilog |
| License | MIT (LICENSE, Copyright 2024 Michael Kohn) |
| FPGA / primitives | iCE40: none (portable) |
| Tests | none found |

**On ULX3S:** No porting needed for the SPI logic itself; only clock/reset wiring needs adapting to ULX3S.

### RasteriCEr SPI display controller {#core-rastericer-display-spi}

Streams a rasterizer's pixel output to a small SPI LCD via a generic SPI-slave-to-parallel bridge (SPI_Slave.v) feeding DisplayControllerSpi.v; built for an iCE40 UP5K board but neither file instantiates vendor primitives.

| | |
|---|---|
| Repository | [toni3141__rastericer](https://github.com/ToNi3141/RasteriCEr): iCE40 UP5K |
| Files | [`rtl/Display/DisplayControllerSpi.v`](https://github.com/ToNi3141/RasteriCEr/blob/00831c58eb010db9a07abcb2a10292b0463469b7/rtl/Display/DisplayControllerSpi.v), [`rtl/3rdParty/SPI_Slave.v`](https://github.com/ToNi3141/RasteriCEr/blob/00831c58eb010db9a07abcb2a10292b0463469b7/rtl/3rdParty/SPI_Slave.v) |
| Top module | `DisplayControllerSpi` |
| Language | Verilog |
| License | GPL-3.0-or-later (LICENSE, repo root; per-file headers confirm GPLv3-or-later, Copyright 2021 ToNi3141) |
| FPGA / primitives | iCE40: none (portable) |
| Tests | none found |

**On ULX3S:** Portable logic; verify clock-domain assumptions before reuse on ECP5.

### Silice OLED drivers (ST7789/SSD1351/SSD1331) {#core-silice-oled-drivers}

Silice `algorithm oled(...)` SPI display drivers for three common OLED controllers, part of Silice's ULX3S board framework and used across several Silice projects (oled_test, oled_sdcard_test, doomchip).

| | |
|---|---|
| Repository | [sylefeb__silice](https://github.com/sylefeb/Silice): Silice HDL language/compiler + many ULX3S projects |
| Files | [`projects/common/oled_st7789.si`](https://github.com/sylefeb/Silice/blob/620487d6b83035dd98299734c8c8fccf8f636005/projects/common/oled_st7789.si), [`projects/common/oled_ssd1351.si`](https://github.com/sylefeb/Silice/blob/620487d6b83035dd98299734c8c8fccf8f636005/projects/common/oled_ssd1351.si), [`projects/common/oled_ssd1331.si`](https://github.com/sylefeb/Silice/blob/620487d6b83035dd98299734c8c8fccf8f636005/projects/common/oled_ssd1331.si) |
| Top module | `oled` |
| Language | Silice |
| License | MIT (per-file header, "MIT license, see LICENSE_MIT in Silice repo root") |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Requires the Silice compiler (compiles to Verilog); proven on ULX3S via Silice's own board support.

Full review: [sylefeb__silice](../projects/sylefeb__silice.md).

### SlabBoy ST7789 SpinalHDL LCD driver {#core-slabboy-st7789}

SpinalHDL SPI driver component for an ST7789 LCD, part of the SlabBoy Game Boy core (idcode 12F, ULX3S-class ECP5 board).

| | |
|---|---|
| Repository | [lawrie__slabboy](https://github.com/lawrie/slabboy): SlabBoy: Game Boy in SpinalHDL on ST7789/SSD1331 |
| Files | [`src/main/scala/slabboy/ST7789.scala`](https://github.com/lawrie/slabboy/blob/51fae53eb8adf6b13b0ce03a2898138001fba32a/src/main/scala/slabboy/ST7789.scala) |
| Top module | `ST7789` |
| Language | SpinalHDL (Scala) |
| License | MIT (LICENSE, Copyright 2018 Craig Bishop) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | none found |

**On ULX3S:** Requires the SpinalHDL/Scala toolchain to elaborate to Verilog; check its bus/register interface against your design.

**Used by 6 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [emard__st7789py_mpy](https://github.com/emard/st7789py_mpy) (instantiates [`st7789py.py`](https://github.com/emard/st7789py_mpy/blob/8c424f16c4b0eae68b3f8b82977267d02472dadb/st7789py.py))
- [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc) (instantiates [`examples/lcd_st7789/micropython/st7789_240x240/esp32/st7789py.py`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/lcd_st7789/micropython/st7789_240x240/esp32/st7789py.py))
- [emard__ulx3s_vic_20](https://github.com/emard/ulx3s_vic_20) (instantiates [`src/vic20.v`](https://github.com/emard/ulx3s_vic_20/blob/c902419dcea50ec65f420f77a3f326a2bbde87a5/src/vic20.v))
- [lawrie__spinalulx3s](https://github.com/lawrie/SpinalULX3S) (instantiates [`src/main/scala/mylib/ST7789.scala`](https://github.com/lawrie/SpinalULX3S/blob/7cb99e7f62c7abdc9210790d2d934e7e197ae627/src/main/scala/mylib/ST7789.scala))
- [lawrie__ulx3s-nmigen-examples](https://github.com/lawrie/ulx3s-nmigen-examples) (instantiates [`image/st7789.py`](https://github.com/lawrie/ulx3s-nmigen-examples/blob/ad5f433e3c154b8fb11d1c116f087a6ba4ebdf5e/image/st7789.py))
- [lawrie__ulx4m_amaranth_examples](https://github.com/lawrie/ulx4m_amaranth_examples) (instantiates [`st7789/gamepi15.py`](https://github.com/lawrie/ulx4m_amaranth_examples/blob/89bff9e64ecb9726f70b078c065545f64db232af/st7789/gamepi15.py))

### SSD1322 OLED framebuffer driver (m68k-ulx3s) {#core-nullobject-oled-ssd1322}

SSD1322 grayscale OLED driver: on reset runs the panel init sequence, then continually copies the framebuffer to the display via a small SPI-like tx sub-module (oled_tx).

| | |
|---|---|
| Repository | [nullobject__m68k-ulx3s](https://github.com/nullobject/m68k-ulx3s): Motorola 68000 SoC on ULX3S using the fx68k core, with OLED display, framebuffer/GPU and ACIA serial |
| Files | [`hdl/oled.v`](https://github.com/nullobject/m68k-ulx3s/blob/761a95e944b4d1c8b196a1c42ef38a67e6d36088/hdl/oled.v) |
| Top module | `oled` |
| Language | Verilog |
| License | none found (no repo-level LICENSE; only the vendored lib/fx68k CPU core has its own separate LICENSE) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | none found |

**On ULX3S:** Proven on ULX3S 85F (Makefile DEVICE=85k); targets SSD1322 rather than ST7789/SSDxxx1/1331 — adapt init bytes for other panels.

**Used by 4 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [brunolevy__learn-fpga](https://github.com/BrunoLevy/learn-fpga) (copies [`Basic/ICESTICK/Oled/oled.v`](https://github.com/BrunoLevy/learn-fpga/blob/5c08c870315c09ccd9ec64ccde20ab3375b3f273/Basic/ICESTICK/Oled/oled.v))
- [nullobject__riscv-ulx3s](https://github.com/nullobject/riscv-ulx3s) (copies [`hdl/oled.v`](https://github.com/nullobject/riscv-ulx3s/blob/f344cef2a29b795cfd3ef4596277d61df9954ab9/hdl/oled.v))
- [nusgreyhats__greybadge25](https://github.com/NUSGreyhats/greybadge25) (copies [`firmware/ecp5/tests/pmod_oled_test/src/oled/oled.v`](https://github.com/NUSGreyhats/greybadge25/blob/3ce9bfbf0061ee36e17dca1274c2f65ae9a5bb07/firmware/ecp5/tests/pmod_oled_test/src/oled/oled.v))
- [osresearch__up5k](https://github.com/osresearch/up5k) (copies [`oled.v`](https://github.com/osresearch/up5k/blob/2eef12a9659b8fc4ebf68656198b8840f6da2e0d/oled.v))

## Other catalogued projects

Catalogued repos tagged `oled-lcd` (42) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
