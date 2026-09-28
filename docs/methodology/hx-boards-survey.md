---
title: "HX8K/HX4K survey"
parent: "Methodology"
nav_order: 3
---
<!-- Generated from data/pages/hx-boards-survey.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# iCE40 HX4K / HX8K gateware survey (from awesome-latticeFPGAs)

**Status 2026-09-28:** owner approved adding HX4K/HX8K gateware and demos to the catalogue; 19 of the 20 recommended repos were cloned and catalogued on 2026-09-28 (abnoname/iceZ0mb1e skipped: already present as the wuxx__icesugar submodule), and the 8 honourable mentions the same day. See the [catalogue](catalogue.md).

Date: 2026-09-28. Source list: `kelu124/awesome-latticeFPGAs` Readme.md (HEAD), sections `## HX4K`, `## HX8K`
and `Other commercial products / HX8K`. HX4K is the same die as HX8K (yosys/nextpnr use `--hx8k`).

Method: GitHub REST search (unauthenticated, 13 search calls, 0 core calls, no rate-limit hit) +
tarball listing via codeload (`tar tz`, nothing extracted to disk) + grep of Makefiles/.pcf/.sh/apio.ini inside
the tarball for `hx8k|hx4k|tq144|ct256|bg121|arachne-pnr|nextpnr-ice40|icepack|icecube`.
Stars / last push / license are from the GitHub search API on 2026-09-28.

**Evidence**: `verified` = .pcf + HDL seen in the tarball (build keywords noted);
`partial` = HDL or pcf only, or proprietary flow; `unverified` = README claim only / no HDL.
Repos already in `sources.tsv` are excluded from tables (one-line note per board).

Toolchain abbreviations: `Y+N` = yosys + nextpnr-ice40 + icepack; `Y+A` = yosys + arachne-pnr + icepack;
`iCEcube2` = Lattice proprietary.

---

## HX4K boards

### 2057-ICE40HX4K-TQ144-breakout — iCE40HX4K-TQ144 — https://github.com/johnwinans/2057-ICE40HX4K-TQ144-breakout

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| johnwinans/2057-ICE40HX4K-TQ144-breakout | Verilog | 25 | 2025-12-28 | none | Y+N (hx4k tq144) | Board repo + `verilog/{minimal,blinky,blinky2}` examples | verified (3 pcf, 7 .v) |

### Alhambra II — iCE40HX4K-TQ144 — https://github.com/FPGAwars/Alhambra-II-FPGA

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| Obijuan/open-fpga-verilog-tutorial | Verilog | 872 | 2020-04-15 | GPL-2.0 | Y+A / Y+N (apio) | Large Spanish Verilog course, `tutorial/Alhambra_II/T01..` (also iCEstick) | verified (99 pcf, 277 .v) |
| FPGAwars/Alhambra-II-FPGA | Verilog | 97 | 2024-10-29 | LGPL-3.0 | Y+A / Y+N (hx8k tq144) | Board repo; `examples/picorv32/picosoc` | verified (1 pcf, 7 .v) |
| FPGAwars/apio-examples | Verilog/SV | 37 | 2026-09-12 | GPL-3.0 | apio (Y+N) | Multi-board apio examples incl. `alhambra-ii/*` and `alchitry-cu/*` | verified (57 pcf, 201 .v) |
| adumont/ad6502 | Verilog | 1 | 2021-03-29 | none | Y+A / Y+N | 6502 CPU; pcf for Alhambra and HX8K breakout | verified (2 pcf) |
| Werni2A/Valhalla-II | VHDL | 6 | 2025-01-19 | GPL-3.0 | ghdl-yosys + N (hx4k) | Open-source VHDL synthesis template for Alhambra II | verified (VHDL, not Verilog) |

### Azukar FPGA — iCE40HX4K — https://github.com/maxisimonazzi/Azukar-FPGA

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| maxisimonazzi/Azukar-FPGA | none | 86 | 2026-09-17 | NOASSERTION | n/a | Board hardware + `docs/pinout/pinout.pcf` only | partial (pcf, no HDL) |

### BeagleWire — iCE40HX4K-TQ144 — https://www.crowdsupply.com/qwerty-embedded-design/beaglewire

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| pmezydlo/BeagleWire | Verilog | 46 | 2018-10-10 | GPL-2.0 | Y+A (hx4k tq144) | Examples (blink, gpio, SDRAM, PMOD...) + BeagleBone kernel drivers (GSoC 2017) | verified (13 pcf, 23 .v) |

### BlackIce II — iCE40HX4K-TQ144 — https://github.com/mystorm-org/BlackIce-II

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| mystorm-org/BlackIce-II | Verilog | 72 | 2020-12-29 | none | Y+A (tq144) | Official examples (pll, sram, common pcf) + STM32 firmware | verified (6 pcf, 52 .v) |
| lawrie/verilog_examples | Verilog | 33 | 2019-09-08 | none | Y+A (tq144) | ~60 examples from the BlackIce ebook (audio, video, sensors...) | verified (62 pcf, 157 .v) |
| mattvenn/fpga-sram | Verilog | 30 | 2017-09-12 | none | Y+A (hx8k tq144) | BlackIce SRAM test | verified |
| mmicko/enigmaFPGA | Verilog | 29 | 2019-05-18 | MIT | Y+A | Enigma machine (BlackIce + Go Board pcf) | verified |
| mattvenn/fpga-virtual-graf | Verilog | 25 | 2019-01-16 | none | Y+A | Virtual graffiti (camera tracking + video) on BlackIce / iCEstick | verified |
| uXeBoy/GBA | Verilog | 18 | 2019-02-13 | GPL-3.0 | unknown | Experimental GBA cartridge in FPGA | partial (pcf + 1 .v, no build script) |
| hoglet67/Ice40Atom | Verilog (+T65) | 17 | 2019-06-01 | none | Y+A (hx8k tq144) | Acorn Atom | verified |
| hoglet67/Ice40CPMZ80 | Verilog | 17 | 2018-04-23 | none | Y+A (hx8k tq144) | Multicomp Z80 CP/M | verified |
| hoglet67/Ice40Beeb | Verilog | 12 | 2017-12-18 | none | Y+A (hx8k tq144) | BBC Micro Model B | verified |
| hoglet67/Ice40JupiterAce | Verilog | 12 | 2018-01-28 | none | Y+A (hx8k tq144) | Jupiter Ace | verified |
| lawrie/hdmi_examples | Verilog | 12 | 2022-05-12 | none | Y+A / Y+N (hx8k tq144) | HDMI/DVI examples (pong, ball/paddle) | verified (9 pcf) |
| lawrie/pico_ram_soc | Verilog | 12 | 2019-10-26 | none | Y+N (hx8k tq144) | PicoSoC running from BRAM with extra peripherals | verified |
| hoglet67/Ice40LogicSniffer | Verilog | 10 | 2018-04-23 | none | Y+A | OpenBench Logic Sniffer port | verified; `lawrie__ice40logicsniffer` already in collection (likely same code) |
| Obijuan/blackice-examples | Verilog | 5 | 2017-08-29 | LGPL-3.0 | Y+A | Blink examples | verified (trivial) |
| piersh/opensourcefpgas | none | 8 | 2018-10-29 | none | n/a | Write-up, no HDL | unverified — drop |

Already in collection: `speccery__icy99` (TI-99/4A, BlackIce target).

### BlackIce MX / IceCore — iCE40HX4K-TQ144 — https://www.tindie.com/products/Folknology/blackice-mx/ , https://github.com/folknology/IceCore

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| folknology/IceCore | Verilog | 46 | 2021-01-23 | none | Y+A (tq144) | IceCore module + STM32 firmware, `Examples/blink`, `trail` | verified (3 pcf, 4 .v) |
| lawrie/blackicemxbook | Verilog | 28 | 2019-11-15 | none | Y+N (hx8k tq144) | BlackIce MX book examples: audio, video, actuators, sensors... | verified (33 pcf, 60 .v) |
| lawrie/blackicemx_nmigen_examples | nMigen/Amaranth | 12 | 2022-06-01 | BSD-2-Clause | nMigen → Y+N | Same kind of examples in nMigen | verified (224 .py, no pcf by design) |
| folknology/BlackIceMx | none | 17 | 2019-09-02 | none | n/a | Carrier board hardware only | unverified — drop |

### Bus Pirate Ultra — iCE40HX (HX4K per list) — https://github.com/DangerousPrototypes/BusPirateUltraHardware

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| DangerousPrototypes/BusPirateUltraHDL | Verilog | 26 | 2019-12-12 | GPL-3.0 | Y+A (`hx8k ct256` in Makefile) | Bus Pirate Ultra FPGA: SPI/UART engines, MCU interface | verified (5 pcf, 26 .v) |

### Eis — iCE40 (HX4K per list) — https://github.com/machdyne/eis

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| machdyne/eis | Verilog | 16 | 2023-04-26 | NOASSERTION | Y+N (`--hx8k bg121`) | Board repo + blinky; runs the Machdyne Zeitlos SoC | verified (1 pcf, 1 .v) |

Already in collection: `machdyne__zeitlos` (SoC supporting Eis/Riegel/Kröte/Kolibri/Kuchen).

### first-fpga-pcb — iCE40 HX8K/HX4K — https://github.com/mattvenn/first-fpga-pcb

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| mattvenn/first-fpga-pcb | Verilog | 83 | 2020-08-03 | none | Y+N (hx8k tq144) | Board + `test/` bring-up gateware | verified |

### Glasgow Interface Explorer (revC) — iCE40HX8K-BG121 (listed in HX4K and HX8K) — https://github.com/GlasgowEmbedded/glasgow

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| GlasgowEmbedded/glasgow | Amaranth | 2216 | 2026-09-25 | 0BSD | Amaranth → Y+N (YoWASP) | Multi-tool: ~46 gateware applets (SPI/I2C/JTAG/UART/logic analyzer...) | verified (Amaranth .py, pcf generated) — ranked lower (not Verilog) |

### Graphics Gremlin — iCE40HX4K-TQ144 — https://github.com/schlae/graphics-gremlin

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| schlae/graphics-gremlin | Verilog | 578 | 2024-10-24 | CC-BY-SA-4.0 | Y+N (`--hx8k` tq144) | ISA video card emulating IBM MDA + CGA | verified (1 pcf, 21 .v) |

### HX4k PMOD Breakout — iCE40HX4K-TQ144 — https://github.com/rschlaikjer/hx4k-pmod

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| rschlaikjer/fpga-3-softcores | Verilog | 13 | 2020-08-24 | MIT | Y+N (hx8k tq144) | VexRiscv SoC + custom peripherals + bare-metal firmware | verified |
| rschlaikjer/hx4k-pmod | Verilog | 11 | 2020-09-08 | MIT | Y+N | Board + `gateware/` bring-up | verified |
| rschlaikjer/fpga-2-led-panel-gifs | Verilog | 2 | 2020-04-05 | none | Y+N | Animated GIFs on HUB75 RGB LED panel | verified |

### ice40-breakout-pcb — iCE40HX4K — https://github.com/null-a/ice40-breakout-pcb

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| null-a/ice40-breakout-pcb | Verilog | 4 | 2021-06-07 | none | Y+N (hx4k tq144) | Board + blinky | verified (trivial) |

### ICE40HXDevBoard — iCE40HX4K-TQ144 — https://github.com/aslak3/ICE40HXDevBoard

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| aslak3/ICE40HXDevBoard | none | 1 | 2025-07-26 | GPL-2.0 | n/a | Hardware only (no .v / .pcf in tarball) | unverified — no gateware found |

### IceZero — iCE40HX4K-TQ144 (Trenz TE0876) — https://blackmesalabs.wordpress.com/2017/02/07/icezero-fpga-board-for-rasppi/

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| blackmesalabs/sump2 | Verilog | 103 | 2018-09-05 | GPL-3.0 | unknown | SUMP2 logic analyzer (Black Mesa Labs, IceZero author) | partial (4 .v, no pcf) |
| noscene/ice40_audio | Verilog | 19 | 2018-04-30 | none | Y+A (hx8k tq144) | PCM5102 I2S DAC driver example (IceZero + UP5K pcf) | verified |
| zymurgy/ice_zero_examples | Verilog | 2 | 2018-07-07 | none | Y+A (tq144) | blink, uart_tx, spi_slave examples | verified |
| dmin7/picozsoc | Verilog | 0 | 2018-06-14 | none | Y+A (hx8k tq144) | PicoSoC port for IceZero | verified |
| dmin7/icozsoc | Verilog | 0 | 2018-06-19 | none | icosoc | icosoc port for IceZero | partial (no pcf) |

`cliffordwolf/icotools` also has `examples/icezero/` (see icoBoard).

### Kéfir I — iCE40HX4K — http://fpgalibre.sourceforge.net/Kefir_en/index.html

No GitHub gateware found (project hosted on SourceForge / FPGA Libre; search "kefir fpga ice40" = 0 results).

### Kolibri — iCE40 (HX4K per list) — https://github.com/machdyne/kolibri

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| machdyne/kolibri | Verilog | 8 | 2023-05-06 | NOASSERTION | Y+N (`--hx8k bg121`) | Board repo + blinky + RP2040 firmware | verified |

### Kröte — iCE40HX4K — https://github.com/machdyne/krote

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| machdyne/krote | Verilog | 3 | 2022-02-20 | NOASSERTION | Y+N (hx4k bg121) | Board repo + blinky | verified (trivial) |

### Manila-Ice — iCE40HX4K-TQ144 — https://github.com/joshtyler/manila-ice

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| joshtyler/manila-ice | SystemVerilog | 10 | 2021-03-02 | none | Y+N (tq144) | Board + `hdl/` test design | verified (1 pcf, 16 .v/.sv) |

### picohx — iCE40 HX (listed HX4K) — https://github.com/dan-rodrigues/pico-hx

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| dan-rodrigues/pico-hx | Verilog | 31 | 2024-05-08 | none | Y+N (Makefile: `FPGA_DEVICE = hx1k`, tq144) | Pico + iCE40 board, example RTL + `picoprog.py` | verified — Makefile targets HX1K, not HX4K |

### Riegel — iCE40HX4K — https://github.com/machdyne/riegel

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| machdyne/riegel | Verilog | 17 | 2023-06-30 | NOASSERTION | Y+N (hx4k bg121) | Board repo + blinky (v1/v2/v3 pcf) | verified |

### un0rick — iCE40HX4K-TQ144 — http://un0rick.cc

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| kelu124/un0rick | Verilog + VHDL | 175 | 2026-09-12 | NOASSERTION | Y+A (`usb/verilog/impl/icestorm`) and iCEcube2 (VHDL MATTY) | Ultrasound pulser/ADC acquisition board gateware | verified (6 pcf, 40 .v, 30 .vhd) |

### X65-SBC — iCE40HX4K + 2x UP5K — https://hackaday.io/project/194866-x65-sbc

No GitHub gateware found by search ("x65 65c816 fpga" = 0). unknown.

### Other notable HX4K gateware (board not in list)

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| portlandhodl/nyan-keys-ice40hx4k-bitstream | Verilog | 38 | 2024-01-31 | none | Y+N (README) | Low-latency parallel key-scanning FPGA for a 60% mech keyboard | verified (pcf + 4 .v) |
| halfmanhalftaco/ice40svga | Verilog | 3 | 2018-01-30 | MIT | Y+A (hx8k tq144) | 800x600 SVGA colour bars | verified (trivial) |

---

## HX8K boards

### Alchitry Cu — iCE40HX8K-CB132 — https://alchitry.com/products/alchitry-cu-fpga-development-board (404)

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| mufpga/MicroFPGA | Verilog + VHDL | 25 | 2023-02-27 | MIT | unknown (no pcf in tree) | Microscope control (camera/laser trigger, PWM, servos) on Au/Cu | partial |
| msiddalingaiah/Centurion | Verilog | 12 | 2022-08-02 | MIT | Y+N (hx8k) | Centurion minicomputer (CPU6) | verified (`ice40_alchitry_cu.pcf`) |
| tuppi-ovh/example-sparkfun-alchitry-cu | SpinalHDL | 7 | 2021-04-23 | GPL-3.0 | Spinal → Y+A (hx8k) | SpinalHDL template | verified (pcf, Scala) |
| alchitry/Cu-Base-Project | Verilog | 6 | 2019-02-12 | MIT | iCEcube2 (Device=HX8K) | Vendor base project | partial (proprietary flow) |
| streetdogg/hardware-designs | Verilog | 5 | 2023-05-28 | MIT | Y+A (hx8k) | blinky / 7-seg on Cu + iCEstick | verified (trivial) |
| r1cebank/alchitry-cu-utils | Verilog | 4 | 2022-04-24 | none | unknown | Personal utility modules for Cu | verified (pcf + 6 .v) |
| mjoldfield/ice40-blinky | Verilog | 4 | 2021-01-26 | none | Y+A | Blinky for Cu, HX8K breakout, iCEstick, Olimex HX1K | verified (trivial) |
| Arvind-Srinivasan/Verilog-Projects | Verilog | 2 | 2022-02-21 | MIT | Y+N (hx8k) | Counters | verified (trivial) |
| Mark1626/litex-alchitry-cu-examples | LiteX | 1 | 2024-02-04 | BSD-2-Clause | LiteX | LiteX examples | partial |

Also `FPGAwars/apio-examples` has `examples/alchitry-cu/*`.

### CAT Board — iCE40HX8K-CT256 — https://github.com/xesscorp/CAT-Board (redirects to devbisme/CAT-Board)

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| devbisme/CAT-Board | MyHDL/Verilog | 62 | 2024-02-27 | none | iCEcube2 (SDRAM test) + MyHDL notebooks | RPi HAT board + SDRAM test | partial (1 pcf, 1 .v, iCEcube) |

### DSP ICE — iCE40HX8K-CT256 — https://github.com/tvelliott/dsp_ice

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| tvelliott/dsp_ice | Verilog | 62 | 2017-10-04 | MIT | Y+A (hx8k ct256) | STM32F4 + HX8K SDR dev system, `firmware/fpga/src` | verified (1 pcf, 4 .v) |

### Glasgow Interface Explorer — see HX4K section.

### iCE40-HX8K Breakout Board (ICE40HX8K-B-EVN, CT256) — Lattice page 404

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| YosysHQ/picorv32 | Verilog | 4384 | 2026-09-07 | ISC | Y+N / Y+A (`picosoc/hx8kdemo`) | PicoRV32 RISC-V + PicoSoC with `hx8kdemo` target | verified (hx8kdemo.pcf) |
| YosysHQ/icestorm | Verilog (examples) | 1188 | 2026-09-21 | ISC | Y+N | Toolchain repo; `examples/hx8kboard` blinky | verified (tool repo, example trivial) |
| Wren6991/RISCBoy | Verilog | 508 | 2025-12-14 | none | Y+N | Hazard5 RISC-V games console (CPU, PPU, ...), `synth/riscboy_hx8kevn.pcf` | verified (62 .v) |
| grahamedgecombe/icicle | Amaranth | 313 | 2023-05-25 | ISC | Amaranth → Y+N | RV32I SoC; board `icicle-ice40-hx8k-b-evn` (v1 was Verilog) | verified (Amaranth) |
| jamesbowman/swapforth | Verilog | 305 | 2023-12-26 | BSD-3-Clause | Y+A | J1a/J4a Forth CPU; `j1a/icestorm/j1a8k.pcf` for HX8K | verified |
| zeldin/iceGDROM | Verilog | 170 | 2023-02-18 | GPL-3.0 | Y+A (README) | Sega Dreamcast GD-ROM emulator on HX8K breakout | verified (pcf + 20 .v) |
| cliffordwolf/PonyLink | Verilog | 129 | 2016-07-07 | none | Y+A | Single-wire bidirectional chip-to-chip link, `demos/ice8k` | verified |
| nesl/ice40_examples | Verilog | 116 | 2023-04-24 | GPL-3.0 | Y+A / Y+N (ct256) | Beginner examples: blinky, buttons, UART, ... | verified (8 pcf) |
| mcmayer/iCE40 | Verilog | 107 | 2021-06-30 | none | Y+N (hx8k ct256) | Experiments: TRNG, DAC, blinky ... | verified (10 pcf) |
| abnoname/iceZ0mb1e | Verilog | 59 | 2023-02-03 | MIT | Y+N | TV80 (Z80) SoC, pinmaps hx8k / hx1k / icezum / eis | verified (7 pcf) |
| peepo/verilog_tutorials_BB | Verilog | 23 | 2016-03-02 | none | Y+A (hx8k) | Tutorials for HX8K breakout | verified (12 pcf) |
| n24bass/ice40_8bitworkshop | Verilog | 18 | 2019-12-31 | NOASSERTION | Y+A (hx8k ct256) | "Designing Video Game Hardware in Verilog" ports | verified |
| janrinze/miniatom | Verilog | 11 | 2023-04-30 | none | Y+A (hx8k ct256) | Minimal Acorn Atom (HX8K breakout + icoBoard) | verified |
| alangarf/tm1637-verilog | Verilog | 8 | 2017-12-10 | Apache-2.0 | Y+A | TM1637 7-segment driver | verified |
| cfib/bf2hw | Verilog | 7 | 2017-03-18 | GPL-3.0 | Bambu HLS + Y+A | Brainf*** to hardware | verified |
| rwmjones/icestorm-flash-leds | Verilog | 4 | 2018-03-17 | none | Y+A | Hello-world LEDs | verified (trivial) |
| Dreadrik/fpga-stopwatch | Verilog | 4 | 2021-06-30 | MIT | Y+N (hx8k) | Breadboard stopwatch | verified |
| gunnarsson901/ice40-tap | Verilog | 0 | 2026-04-14 | none | Y+N (hx8k ct256) | Passive Ethernet tap LAN8720 RMII → SPI → Wireshark | verified (new, 0 stars) |

### iceFUN — iCE40HX8K-CB132 — https://en.manu-systems.com/DEV-ICEFUN.shtml

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| MichaelBell/nanoV | Verilog | 27 | 2024-11-17 | Apache-2.0 | Y+N (hx8k) | Minimal-area RV32E core (iceFUN + pico-ice) | verified |
| mikeakohn/apollo11_fpga | Verilog | 22 | 2024-12-25 | MIT | Y+N (hx8k) | Apollo Guidance Computer | verified |
| mikeakohn/riscv_fpga | Verilog | 19 | 2026-06-27 | MIT | Y+N (hx8k) | RISC-V CPU + peripherals | verified |
| mikeakohn/micro68k | Verilog | 17 | 2024-03-24 | MIT | Y+N (hx8k) | Reduced 68000 | verified |
| mikeakohn/powerpc_fpga | Verilog | 13 | 2024-09-12 | MIT | Y+N (hx8k) | PowerPC subset | verified |
| devantech/iceFUN | Verilog | 12 | 2021-09-26 | none | Y+N (hx8k) | Vendor examples: blinky, LEDs, LED strip, music | verified (9 pcf) |
| mikeakohn/intel_8008 | Verilog | 12 | 2025-02-09 | none | Y+N (hx8k) | Intel 8008 | verified |
| mikeakohn/micro86 | Verilog | 11 | 2025-09-24 | MIT | Y+N (hx8k) | Reduced 32-bit x86 | verified |
| mikeakohn/msp430_fpga | Verilog | 5 | 2026-06-25 | MIT | Y+N (hx8k) | MSP430 | verified |
| robin7g/rg-iceFUN | Verilog | 1 | 2023-03-26 | MIT | Y+N (hx8k) | VGA / scrolltext examples | verified |

### icoBoard 1.0 — iCE40HX8K-CT256 — http://icoboard.org/about-icoboard.html (unreachable)

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| cliffordwolf/icotools | Verilog | 80 | 2021-07-13 | none | Y+A (hx8k) | icoprog + icosoc SoC generator + examples (icoboard, icezero) | verified |
| ZipCPU/icozip | Verilog | 19 | 2021-10-21 | none | Y+N / Y+A (hx8k ct256) | ZipCPU demo port with flash, UART, PMODs | verified (14 pcf, 98 .v) |
| jhol/otl-icoboard-pmodoledrgb-demo | Verilog | 9 | 2017-12-17 | BSD-3-Clause | Y+A (hx8k) | Graphics on PmodOLEDrgb | verified |
| janrinze/icoboard_sram | Verilog | 4 | 2017-02-19 | GPL-3.0 | Y+A (hx8k) | SRAM access module | verified |

### iCEboy — iCE40HX8K — https://sourceforge.net/projects/iceboy/

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| msinger/iceboy | SystemVerilog | 24 | 2025-03-29 | NOASSERTION | yosys + icepack (hx8k ct256; P&R tool not confirmed) | Game Boy clone (GitHub home of the SourceForge project) | verified (12 pcf, 86 .v/.sv) |

### Kuchen — iCE40HX8K-CT256 — https://github.com/machdyne/kuchen

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| machdyne/kuchen | Verilog | 23 | 2024-06-26 | NOASSERTION | Y+N (hx8k ct256) | Board repo + blinky (v0/v1 pcf) | verified |
| machdyne/keks | Verilog | 19 | 2023-08-05 | NOASSERTION | Y+N (hx8k ct256) | Keks game console (not in list) + pong | verified |

### MiCE47 — i.MXRT1021 + iCE40HX8K — https://hackaday.io/project/166109-mice47

No GitHub gateware found. unknown.

### Olimex iCE40HX8K-EVB — iCE40HX8K-CT256 — https://www.olimex.com/Products/FPGA/iCE40/iCE40HX8K-EVB/open-source-hardware

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| x653/xv6-riscv-fpga | Verilog | 62 | 2023-03-05 | NOASSERTION | Y+N (hx8k) | RISC-V computer running UNIX xv6, all FOSS | verified |
| OLIMEX/iCE40HX8K-EVB | Verilog | 41 | 2026-05-25 | Apache-2.0 | Y+N (hx8k ct256) | Vendor board repo + demos (blinky, io-video) | verified (2 pcf) |
| mikewolak/olimex-ice40hx8k-picorv32 | Verilog | 1 | 2025-11-01 | NOASSERTION | Y+N (hx8k ct256) | PicoRV32 SoC automated build system | verified (large, 732 files) |
| Junkotron/fpga_memtest | Verilog | 0 | 2024-02-19 | none | Y+A | SRAM test for Olimex HX1K/HX8K | verified |
| iceduino/olimex-neorv32 | VHDL | 0 | 2022-03-11 | BSD-3-Clause | ghdl-yosys + N | NEORV32 setup for this board | verified (VHDL) |

Already in collection: `alangarf__apple-one` (board dir olimex_ice40hx8k), `lawrie__apple-one`.

### Snowflake-FPGA — iCE40HX8K — https://github.com/Wren6991/Snowflake-FPGA

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| Wren6991/Snowflake-FPGA | none | 31 | 2019-07-07 | NOASSERTION | n/a | Board hardware + scripts, no .v/.pcf | unverified — no gateware |

Same author's `Wren6991/RISCBoy` (HX8K) is in the breakout table. Already in collection: `wren6991__hazard3`, `wren6991__smoldvi`.

### Valve Index / Vive (commercial) — no public gateware.

---

## Recommended to clone (20)

| # | repo | reason |
|---|---|---|
| 1 | YosysHQ/picorv32 | Reference RISC-V core + PicoSoC with `hx8kdemo`; the canonical reusable soft CPU for iCE40 (ISC) |
| 2 | schlae/graphics-gremlin | Real product: ISA MDA/CGA video card, Y+N `--hx8k`, clean Verilog video/bus timing |
| 3 | msinger/iceboy | Complete Game Boy in SystemVerilog on HX8K, the notable iCEboy project |
| 4 | Wren6991/RISCBoy | Full console SoC (CPU, PPU, busfabric), HX8K breakout target; same author as hazard3 (already here) |
| 5 | zeldin/iceGDROM | Dreamcast GD-ROM emulator, real-world interface work on HX8K breakout (GPL-3.0) |
| 6 | jamesbowman/swapforth | J1a Forth CPU with HX8K (`j1a8k.pcf`) build, tiny reusable stack CPU (BSD-3) |
| 7 | cliffordwolf/icotools | icosoc SoC generator + icoBoard/IceZero examples |
| 8 | ZipCPU/icozip | ZipCPU port with flash/UART/PMOD cores, well-documented Verilog |
| 9 | hoglet67/Ice40Atom | Acorn Atom retro computer on BlackIce (HX4K), complements lawrie ULX3S retro ports |
| 10 | hoglet67/Ice40Beeb | BBC Micro on BlackIce (HX4K) |
| 11 | lawrie/blackicemxbook | Large Y+N example set (33 designs: audio, video, sensors) |
| 12 | lawrie/verilog_examples | ~60 BlackIce II examples, many peripheral drivers |
| 13 | lawrie/hdmi_examples | DVI/HDMI on iCE40 HX (tq144), comparable to the ULX3S GPDI work |
| 14 | abnoname/iceZ0mb1e | TV80 SoC with pinmaps for several HX boards, MIT |
| 15 | x653/xv6-riscv-fpga | RISC-V computer booting xv6 on Olimex HX8K-EVB, all FOSS |
| 16 | nesl/ice40_examples | Most-starred beginner example set for HX8K breakout (GPL-3.0) |
| 17 | mikeakohn/riscv_fpga | Representative of the mikeakohn iceFUN CPU family (MIT; same structure as micro68k/apollo11/powerpc) |
| 18 | DangerousPrototypes/BusPirateUltraHDL | Bus Pirate protocol engines in Verilog (GPL-3.0) |
| 19 | Obijuan/open-fpga-verilog-tutorial | 872-star Verilog course with Alhambra II builds (GPL-2.0) |
| 20 | kelu124/un0rick | Owner's own HX4K ultrasound board gateware (icestorm build) |

Honourable mentions (not in the 20; all 8 cloned + catalogued 2026-09-28): GlasgowEmbedded/glasgow (Amaranth, biggest HX8K project), mystorm-org/BlackIce-II, mikeakohn/apollo11_fpga, MichaelBell/nanoV, tvelliott/dsp_ice, msiddalingaiah/Centurion, pmezydlo/BeagleWire, rschlaikjer/fpga-3-softcores.

---

## Notes

- **Boards with no GitHub gateware found**: Kéfir I (SourceForge only), MiCE47 (hackaday), X65-SBC (hackaday), ICE40HXDevBoard (hardware only), Snowflake-FPGA (hardware only), BlackIceMx carrier (hardware only), Azukar (pcf only), Valve Index/Vive (commercial).
- **List placement inconsistencies**: `pico-hx` Makefile targets `hx1k` (list: HX4K). `machdyne/eis` and `machdyne/kolibri` Makefiles use `--hx8k --package bg121` (list: HX4K; an HX4K die is normally built as HX8K, so this may be consistent, but the part number is unverified). Glasgow is listed in both HX4K and HX8K (revC is HX8K). The Bus Pirate Ultra HDL Makefile uses `hx8k ct256`.
- **Broken / dead links in the awesome list** (checked 2026-09-28): Lattice iCE40-HX8K Breakout page → 404; Alchitry Cu product page → 404; `icoboard.org` → no response; blackmesalabs.wordpress.com IceZero post → 403 (may be bot-blocking); `xesscorp/CAT-Board` redirects to `devbisme/CAT-Board`. Others (Olimex, iceFUN, SourceForge iceboy, Kéfir, hackaday, un0rick.cc, BeagleWire, BlackIce wiki, Tindie) → 200.
- **Proprietary-flow repos**: `alchitry/Cu-Base-Project`, `devbisme/CAT-Board` SDRAM test (iCEcube2); `kelu124/un0rick` VHDL branch (iCEcube2) alongside an icestorm Verilog build.
- **Rate limits**: 13 search calls, 7 s apart; no "rate limit exceeded" encountered; 0 core API calls (metadata came from search results; file lists came from codeload tarballs, which do not count).
- **Already in collection with HX targets**: `alangarf__apple-one`, `lawrie__apple-one` (Olimex HX8K-EVB), `speccery__icy99` (BlackIce), `lawrie__ice40logicsniffer` (BlackIce, same lineage as hoglet67/Ice40LogicSniffer), `machdyne__zeitlos` (Machdyne HX boards), `splinedrive__my_hdmi_device` (icoboard/blackice targets), `wren6991__*`.
- **Not covered**: excluded per brief — iCEstick, Nandland Go, Olimex HX1K, TinyFPGA B2/BX (LP8K), UPduino (UP5K). The search was repo-level only (unauthenticated code search is not available), so repos that name HX8K only inside a Makefile, and not in their name, description or readme, may be missed.
{% endraw %}
