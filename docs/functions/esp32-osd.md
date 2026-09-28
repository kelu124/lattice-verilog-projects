---
title: "ESP32 OSD and loading"
parent: "Cores by function"
nav_order: 5
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# ESP32 OSD and loading

On-screen display and ROM/disk loading driven by the ULX3S ESP32 over SPI.

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [ESP32 SPI OSD + spirw_slave ROM/disk loading stack](#core-lawrie-esp32-spi-osd) ★ | [lawrie__ulx3s_sms](https://github.com/lawrie/ulx3s_sms) | Verilog, MicroPython | osd.v and spi_osd.v: none found; | any | 31 |
| [esp32_spi_gamepad minimal ESP32 SPI state receiver](#core-danrodrigues-esp32-spi-gamepad) | [dan-rodrigues__ulx3s-bluetooth-gamepad](https://github.com/dan-rodrigues/ulx3s-bluetooth-gamepad) | Verilog | MIT (SPDX header, Copyright 2020 Dan Rodrigues) | any | 1 |
| [esp32ecp5 MicroPython FPGA loader package](#core-emard-esp32ecp5-loader) | [emard__esp32ecp5](https://github.com/emard/esp32ecp5) | MicroPython | MIT (pypi/LICENSE.txt, "AUTHOR=EMARD LICENSE=MIT") | any | 1 |
| [SPI RAM slave (ESP32 <-> FPGA memory-mapped link)](#core-emard-spi-ram-slave) | [emard__uk101onfpga](https://github.com/emard/UK101onFPGA) | VHDL | BSD ("AUTHOR=EMARD LICENSE=BSD") | any | 1 |

## Cores

### ESP32 SPI OSD + spirw_slave ROM/disk loading stack (best) {#core-lawrie-esp32-spi-osd}

Intercepts the video stream to draw a text OSD window (osd.v) driven by an SPI slave register interface (spi_osd.v) that the ESP32 writes into; a generic SPI RW slave (spirw_slave_v.v) is what the ESP32-side MicroPython (osd.py) uses to browse/select ROMs on SD and push them into FPGA BRAM.

| | |
|---|---|
| Repository | [lawrie__ulx3s_sms](https://github.com/lawrie/ulx3s_sms): Sega Master System / SG-1000: TV80, VDP, SN76489, SDRAM carts, ESP32 OSD |
| Files | [`src/osd/osd.v`](https://github.com/lawrie/ulx3s_sms/blob/13c2361a5039d205de47857bab9201055ac9e566/src/osd/osd.v), [`src/osd/spi_osd.v`](https://github.com/lawrie/ulx3s_sms/blob/13c2361a5039d205de47857bab9201055ac9e566/src/osd/spi_osd.v), [`src/osd/spirw_slave_v.v`](https://github.com/lawrie/ulx3s_sms/blob/13c2361a5039d205de47857bab9201055ac9e566/src/osd/spirw_slave_v.v), [`esp32/osd/osd.py`](https://github.com/lawrie/ulx3s_sms/blob/13c2361a5039d205de47857bab9201055ac9e566/esp32/osd/osd.py) |
| Top module | `osd` |
| Language | Verilog, MicroPython |
| License | osd.v and spi_osd.v: none found; spirw_slave_v.v: BSD ("AUTHOR=EMARD") |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** The de-facto ESP32<->FPGA OSD/loader stack, reused nearly verbatim across nes_ecp5, trs_80, apple2fpga, msx, sega-sms, sg_1000, ql, gamegear, vic_20; wire spi_osd into the video pipeline and spirw_slave_v to a SPI-mapped BRAM/register block.

Full review: [lawrie__ulx3s_sms](../projects/lawrie__ulx3s_sms.md).

**Used by 31 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [cheyao__icepi-zero](https://github.com/cheyao/icepi-zero) (instantiates [`gateware/third-party/dvi_osd/hdl/spi_osd_v.v`](https://github.com/cheyao/icepi-zero/blob/e01faa2bd35dcb7269827f8420b845d46c78c869/gateware/third-party/dvi_osd/hdl/spi_osd_v.v))
- [cheyao__nes_ecp5](https://github.com/cheyao/nes_ecp5) (instantiates [`osd/spi_osd.v`](https://github.com/cheyao/nes_ecp5/blob/e8dd1eb7f9f440a552cd24c0b936e58705a272e7/osd/spi_osd.v))
- [cheyao__sega-sms](https://github.com/cheyao/sega-sms) (instantiates [`src/osd/spi_osd.v`](https://github.com/cheyao/sega-sms/blob/c37e846d94f88eb9a95f44b15f2b23019aa25a26/src/osd/spi_osd.v))
- [danodus__ulx3s_68k](https://github.com/danodus/ulx3s_68k) (instantiates [`src/osd/spi_osd.v`](https://github.com/danodus/ulx3s_68k/blob/ee10339210d0c302143745d3cc584a21a4878ace/src/osd/spi_osd.v))
- [danodus__ulx3s_sms](https://github.com/danodus/ulx3s_sms) (instantiates [`src/osd/spi_osd.v`](https://github.com/danodus/ulx3s_sms/blob/13c2361a5039d205de47857bab9201055ac9e566/src/osd/spi_osd.v))
- [emard__apple2fpga](https://github.com/emard/apple2fpga) (instantiates [`rtl_emard/lattice/top/ulx3s_v20_apple2.vhd`](https://github.com/emard/apple2fpga/blob/0ad84ae2f9d9d5cc0e8db6128d630a9e16cdd6de/rtl_emard/lattice/top/ulx3s_v20_apple2.vhd))
- [emard__nes_ecp5](https://github.com/emard/nes_ecp5) (instantiates [`osd/spi_osd.v`](https://github.com/emard/nes_ecp5/blob/fd421a13886cccc6da13be28a4a803a90b201e60/osd/spi_osd.v))
- [emard__snes_mister_ulx3s](https://github.com/emard/SNES_MiSTer_ulx3s) (instantiates [`ulx3s/osd/spi_osd.v`](https://github.com/emard/SNES_MiSTer_ulx3s/blob/bbb10d06a1c396d3784ff70033ecf7e941fd43fc/ulx3s/osd/spi_osd.v))
- [emard__uk101onfpga](https://github.com/emard/UK101onFPGA) (instantiates [`rtl_emard/osd/spi_osd.v`](https://github.com/emard/UK101onFPGA/blob/7264146bca76c6f751039ab569824a59875fe976/rtl_emard/osd/spi_osd.v))
- [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc) (instantiates [`examples/adxl355/projbig/top/top_adxl355log.v`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/adxl355/projbig/top/top_adxl355log.v))
- [emard__ulx3s_c64](https://github.com/emard/ulx3s_c64) (instantiates [`rtl/osd/spi_osd_v.v`](https://github.com/emard/ulx3s_c64/blob/cc412a9134ed42d4296f1afb523d556b68bb74ba/rtl/osd/spi_osd_v.v))
- [emard__ulx3s_vic_20](https://github.com/emard/ulx3s_vic_20) (instantiates [`src/osd/spi_osd.v`](https://github.com/emard/ulx3s_vic_20/blob/c902419dcea50ec65f420f77a3f326a2bbde87a5/src/osd/spi_osd.v))
- [ironsteel__nes_ecp5](https://github.com/ironsteel/nes_ecp5) (instantiates [`osd/spi_osd.v`](https://github.com/ironsteel/nes_ecp5/blob/ff331d4b9c422e0b792560dd7b2b67a28622f67f/osd/spi_osd.v))
- [lawrie__ulx3s_68k](https://github.com/lawrie/ulx3s_68k) (instantiates [`src/osd/spi_osd.v`](https://github.com/lawrie/ulx3s_68k/blob/ee10339210d0c302143745d3cc584a21a4878ace/src/osd/spi_osd.v))
- [lawrie__ulx3s_altair_8800](https://github.com/lawrie/ulx3s_altair_8800) (instantiates [`src/osd/spi_osd.v`](https://github.com/lawrie/ulx3s_altair_8800/blob/e59889fb0b57b3e2606063fa2a86401be34986f6/src/osd/spi_osd.v))
- … and 16 more (see `data/core_usage.json`)

### esp32_spi_gamepad minimal ESP32 SPI state receiver {#core-danrodrigues-esp32-spi-gamepad}

Minimal SPI receiver decoding ESP32-side Bluetooth-gamepad button/axis state into FPGA registers; a smaller alternative pattern to the full OSD stack for simple ESP32->FPGA control-word links (no video overlay).

| | |
|---|---|
| Repository | [dan-rodrigues__ulx3s-bluetooth-gamepad](https://github.com/dan-rodrigues/ulx3s-bluetooth-gamepad): Bluetooth gamepad-to-LED demo: ESP32 |
| Files | [`esp32_spi_gamepad.v`](https://github.com/dan-rodrigues/ulx3s-bluetooth-gamepad/blob/03228b2b4048399e20b8f310f22ffff2aa9de1bb/esp32_spi_gamepad.v) |
| Top module | `esp32_spi_gamepad` |
| Language | Verilog |
| License | MIT (SPDX header, Copyright 2020 Dan Rodrigues) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Good template for any small ESP32->FPGA state link that doesn't need the OSD video overlay machinery.

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [dan-rodrigues__icestation-32](https://github.com/dan-rodrigues/icestation-32) (instantiates [`hardware/ulx3s/ulx3s_gamepad_state.v`](https://github.com/dan-rodrigues/icestation-32/blob/55214d79f74a547dedb54f99cb2fad431b7ac277/hardware/ulx3s/ulx3s_gamepad_state.v))

### esp32ecp5 MicroPython FPGA loader package {#core-emard-esp32ecp5-loader}

ESP32-side MicroPython package for loading ECP5 bitstreams over SPI (ecp5.py), a micro-FTP server for pushing files to ESP32 flash/SD (uftpd.py), and raw SD block read/write (sdraw.py) — the ESP32 half of the ULX3S ESP32<->FPGA loading path.

| | |
|---|---|
| Repository | [emard__esp32ecp5](https://github.com/emard/esp32ecp5): esp32ecp5: MicroPython JTAG programmer for ECP5 from onboard ESP32, FTP/SD/DFU |
| Files | [`pypi/ecp5.py`](https://github.com/emard/esp32ecp5/blob/f6cea2425d039bd7488f347bc4309f7be1c7ea01/pypi/ecp5.py), [`pypi/uftpd.py`](https://github.com/emard/esp32ecp5/blob/f6cea2425d039bd7488f347bc4309f7be1c7ea01/pypi/uftpd.py), [`pypi/sdraw.py`](https://github.com/emard/esp32ecp5/blob/f6cea2425d039bd7488f347bc4309f7be1c7ea01/pypi/sdraw.py) |
| Top module | n/a |
| Language | MicroPython |
| License | MIT (pypi/LICENSE.txt, "AUTHOR=EMARD LICENSE=MIT") |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Runs on the ULX3S's onboard ESP32; pairs with an FPGA-side SPI slave (e.g. spirw_slave_v.v) to receive the loaded data.

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [emard__ulx3s-bin](https://github.com/emard/ulx3s-bin) (copies [`esp32/micropython/sdraw.py`](https://github.com/emard/ulx3s-bin/blob/2a40f50e0142f2b2856bf0a7471a8741881ec427/esp32/micropython/sdraw.py))

### SPI RAM slave (ESP32 <-> FPGA memory-mapped link) {#core-emard-spi-ram-slave}

Presents FPGA BRAM as a Microchip-23K-style SPI RAM device to the ESP32 — an alternative transport (memory-mapped SPI RAM rather than the OSD register protocol) for ESP32-driven data/ROM loading.

| | |
|---|---|
| Repository | [emard__uk101onfpga](https://github.com/emard/UK101onFPGA): UK101 + ORAO |
| Files | [`rtl_emard/spi_ram/spi_ram_slave.vhd`](https://github.com/emard/UK101onFPGA/blob/7264146bca76c6f751039ab569824a59875fe976/rtl_emard/spi_ram/spi_ram_slave.vhd) |
| Top module | `spi_ram_slave` |
| Language | VHDL |
| License | BSD ("AUTHOR=EMARD LICENSE=BSD") |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Simpler than spirw_slave_v.v when the ESP32 only needs to fill/read a block of FPGA memory without an OSD protocol layer on top.

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc) (instantiates [`examples/spi_ram/hdl/top/ulx3s_spi_ram_oled.vhd`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/spi_ram/hdl/top/ulx3s_spi_ram_oled.vhd))

## Other catalogued projects

Catalogued repos tagged `esp32` (54) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
