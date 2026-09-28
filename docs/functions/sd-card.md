---
title: "SD card"
parent: "Cores by function"
nav_order: 10
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# SD card

SD card controllers (SPI mode, SDIO) and FAT helpers.

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [ZipCPU sdspi SPI-mode SD controller](#core-zipcpu-sdspi) ★ | [zipcpu__sdspi](https://github.com/ZipCPU/sdspi) | Verilog | GPL-3.0 (per-file headers) | any | 0 |
| [MiSTer sd_card.sv (Harbaum/Sorgelig)](#core-gojimmypi-mister-sd-card) | [gojimmypi__z80386-ulx3s-doom](https://github.com/gojimmypi/z80386-ulx3s-doom) | SystemVerilog | LGPL-3.0-or-later | any | 0 |
| [sd_controller (Searle/Edwards derived) SD reader](#core-lawrie-cpm-sd-controller) | [lawrie__ulx3s_cpm_z80](https://github.com/lawrie/ulx3s_cpm_z80) | Verilog | custom permissive | any | 1 |
| [SDKarte SD card reader](#core-logoposeidon-sdkarte) | [logoposeidon__ulx3sjukebox](https://github.com/LogoPoseidon/Ulx3sJukeBox) | Verilog | none found | ECP5 | 0 |
| [Silice sdcard SPI controller](#core-silice-sdcard) | [sylefeb__silice](https://github.com/sylefeb/Silice) | Silice | MIT (file header + LICENSE_MIT) | any | 0 |

## Cores

### ZipCPU sdspi SPI-mode SD controller (best) {#core-zipcpu-sdspi}

Wishbone-B4 SPI-mode SD/MMC controller, no vendor primitives, ~60 SymbiYosys formal proofs. "Silicon proven" per the author. Maps directly onto the ULX3S sd_clk/sd_cmd/sd_d[0]/sd_d[3] pins (shared with the ESP32).

| | |
|---|---|
| Repository | [zipcpu__sdspi](https://github.com/ZipCPU/sdspi): SD-Card cores |
| Files | [`rtl/spi/sdspi.v`](https://github.com/ZipCPU/sdspi/blob/dfb16c80781e8f3eaea9f9cdeb7042baa9e6fa0d/rtl/spi/sdspi.v), [`rtl/spi/llsdspi.v`](https://github.com/ZipCPU/sdspi/blob/dfb16c80781e8f3eaea9f9cdeb7042baa9e6fa0d/rtl/spi/llsdspi.v), [`rtl/spi/spicmd.v`](https://github.com/ZipCPU/sdspi/blob/dfb16c80781e8f3eaea9f9cdeb7042baa9e6fa0d/rtl/spi/spicmd.v), [`rtl/spi/spirxdata.v`](https://github.com/ZipCPU/sdspi/blob/dfb16c80781e8f3eaea9f9cdeb7042baa9e6fa0d/rtl/spi/spirxdata.v), [`rtl/spi/spitxdata.v`](https://github.com/ZipCPU/sdspi/blob/dfb16c80781e8f3eaea9f9cdeb7042baa9e6fa0d/rtl/spi/spitxdata.v) |
| Top module | `sdspi` |
| Language | Verilog |
| License | GPL-3.0 (per-file headers) |
| FPGA / primitives | any: none (portable) |
| Tests | formal (SymbiYosys, ~60 proofs in bench/formal/); Verilator/Icarus models in bench/cpp, bench/verilog |

**On ULX3S:** Wire o_sck->sd_clk, o_mosi->sd_cmd, i_miso<-sd_d[0], o_cs_n->sd_d[3] per ulx3s_v20.lpf; ESP32 firmware must release these pins first.

Full review: [zipcpu__sdspi](../projects/zipcpu__sdspi.md).

### MiSTer sd_card.sv (Harbaum/Sorgelig) {#core-gojimmypi-mister-sd-card}

The well-known MiSTer-framework SD-card core (WIDE/OCTAL parameters), vendored as part of the ao486-derived PC-SoC peripheral set; not yet wired into the ULX3S probe top in this repo (CPU-only today).

| | |
|---|---|
| Repository | [gojimmypi__z80386-ulx3s-doom](https://github.com/gojimmypi/z80386-ulx3s-doom): CPU-only bring-up of the z386 |
| Files | [`third_party/z386_MiSTer/sys/sd_card.sv`](https://github.com/gojimmypi/z80386-ulx3s-doom/blob/ccc2903c380b90d6e7ec3b5ffc3e5b5f6d23e6dc/third_party/z386_MiSTer/sys/sd_card.sv) |
| Top module | `sd_card` |
| Language | SystemVerilog |
| License | LGPL-3.0-or-later (Till Harbaum 2014 / Sorgelig 2015-2018, file header) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Widely used and battle-tested across the MiSTer ecosystem; LGPL-3.0+ copyleft on modifications to the file itself.

### sd_controller (Searle/Edwards derived) SD reader {#core-lawrie-cpm-sd-controller}

Single-block SD read/write stream controller adapted from Steven Merrifield's design via the Apple II emulator (Stephen Edwards) and Grant Searle's Z80 boards; used to load CP/M disk images on the ULX3S CP/M-Z80 build.

| | |
|---|---|
| Repository | [lawrie__ulx3s_cpm_z80](https://github.com/lawrie/ulx3s_cpm_z80): CP/M on Z80 |
| Files | [`src/Components/SDCARD/sd_controller.v`](https://github.com/lawrie/ulx3s_cpm_z80/blob/2ec96bec461c11ec51aee803500c0890ee632f65/src/Components/SDCARD/sd_controller.v) |
| Top module | `sd_controller` |
| Language | Verilog |
| License | custom permissive (Grant Searle acknowledgement clause: free to use, must credit, must not charge) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** License requires attribution to Grant Searle and forbids charging for the file; simple enough to read/port in an afternoon.

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [logoposeidon__ulx3sjukebox](https://github.com/LogoPoseidon/Ulx3sJukeBox) (instantiates [`SDKartenLeser.v`](https://github.com/LogoPoseidon/Ulx3sJukeBox/blob/0a4c0a6faf01a45ff74693e16087c25c686114d4/SDKartenLeser.v))

### SDKarte SD card reader {#core-logoposeidon-sdkarte}

Standalone SD card reader feeding a FIFO for a ULX3S MP3/audio jukebox project (song selection via buttons); small, single-purpose block.

| | |
|---|---|
| Repository | [logoposeidon__ulx3sjukebox](https://github.com/LogoPoseidon/Ulx3sJukeBox): SD-card PCM jukebox / audio player for ULX3S |
| Files | [`SDKartenLeser.v`](https://github.com/LogoPoseidon/Ulx3sJukeBox/blob/0a4c0a6faf01a45ff74693e16087c25c686114d4/SDKartenLeser.v) |
| Top module | `SDKarte` |
| Language | Verilog |
| License | none found |
| FPGA / primitives | ECP5: none (portable) |
| Tests | none found |

**On ULX3S:** No license header; treat as all-rights-reserved until clarified with the author before reuse.

### Silice sdcard SPI controller {#core-silice-sdcard}

SDHC/SDXC-only SD controller written in Silice, kept in slow-transfer mode throughout; author reports it tested working at 25, 50 and 100 MHz. Part of the ULX3S-supporting Silice board framework.

| | |
|---|---|
| Repository | [sylefeb__silice](https://github.com/sylefeb/Silice): Silice HDL language/compiler + many ULX3S projects |
| Files | [`projects/common/sdcard.si`](https://github.com/sylefeb/Silice/blob/620487d6b83035dd98299734c8c8fccf8f636005/projects/common/sdcard.si) |
| Top module | `sdcard` |
| Language | Silice |
| License | MIT (file header + LICENSE_MIT) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Requires the Silice compiler (yosys+nextpnr-ecp5 backend, GPL-3.0) rather than being usable as plain Verilog/VHDL.

Full review: [sylefeb__silice](../projects/sylefeb__silice.md).

## Other catalogued projects

Catalogued repos tagged `sdcard` (48) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
