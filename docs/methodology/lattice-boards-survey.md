---
title: "UP5K/ECP5 boards survey"
parent: "Methodology"
nav_order: 5
---
<!-- Generated from data/pages/lattice-boards-survey.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# UP5K and ECP5 boards from awesome-latticeFPGAs: gateware survey

**Status 2026-09-28:** all 20 "Recommended to clone" repos are cloned and in `docs/catalogue.md`.

Date: 2026-09-28. Research only. Nothing was cloned into ulx3s-klod.

Source list: `kelu124/awesome-latticeFPGAs` `Readme.md`. The README has a capital R, so `README.md` returns 404. There is
no data file; the list is hand-written markdown. I kept the sections "UP5K", "ECP5", "Conference badges" and
"Other commercial products → UP5K / ECP5".

Excluded: every slug in `.claude/memory/sources.tsv` (for example wuxx__icesugar, osresearch__up5k,
icebreaker-fpga__*, kbob__icebreaker-candy, smunaut__ice40-playground, damdoy__ice40_ultraplus_examples,
machdyne__zeitlos, machdyne__nes_ecp5), all boards and repos in `docs/ecp5-boards-survey.md` (OrangeCrab, LUNA/Cynthion,
iCESugar-Pro, HAD2019, Colorlight, ButterStick, ECPIX-5, Logicbone, Versa/EVN, TinyFPGA EX, IcePi Zero including
m1nl/icepi-zero-minimig, ECP5-mini, Pergola, basic-ecp5-pcb), and ULX3S/ULX4M.

**Evidence** comes from a tarball file listing (codeload `tar.gz/HEAD`, streamed, not kept) taken on 2026-09-28:

- `V` = verified: a constraint file (`.pcf` for iCE40, `.lpf` for ECP5) and HDL are in the tree. Counts are given as p=pcf, l=lpf, v=.v, sv=.sv.
- `U` = unverified: no constraint file seen, the files were not checked, or the only source is the README.

**Toolchain:**

- "open" = a Makefile, .mk or .ys file in the tree calls nextpnr-ice40/icepack or nextpnr-ecp5/ecppack.
- "open?" = the HDL and pcf/lpf are present but no build file matched. Often the build files sit in a submodule (for example no2build), which the tarball does not include.

Stars, last push and license come from the GitHub search API on 2026-09-28.

---

## UP5K boards

### Fomu (iCE40UP5K-UWG30), https://www.crowdsupply.com/sutajio-kosagi/fomu

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| im-tomu/fomu-workshop | Verilog/VHDL/Python | 170 | 2024-03-17 | Apache-2.0 | open (+LiteX) | Official workshop: blink, RGB, USB, RISC-V examples | V (p4 v6 vhd4) |
| ulixxe/usb_cdc | Verilog | 193 | 2024-03-10 | MIT | open | Board-agnostic FS USB CDC-ACM device core (single/multi-channel); examples for Fomu, TinyFPGA-BX, iCEBreaker and others | V (p21 v51) |
| im-tomu/foboot | Verilog (LiteX gen) + C | 105 | 2022-12-31 | Apache-2.0 | LiteX + open | Fomu DFU bootloader SoC | V-HDL / pcf via LiteX platform (U) |
| im-tomu/fomu-tests | Verilog | 9 | 2023-02-05 | Apache-2.0 | open | Factory/bring-up test bitstreams | V (p4 v5) |
| stef/nb-fomu-hw | Verilog | 8 | 2019-09-30 | NOASSERTION | open | "non-blinky" USB-UART hello world | V (p1 v2) |
| mntmn/fomu-vga | Verilog | 16 | 2020-07-10 | none | open | VGA output from Fomu | U (v8, no pcf) |

### UPduino v1/v2/v3.x (iCE40UP5K-SG48), https://github.com/tinyvision-ai-inc/UPduino-v3.0

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| tinyvision-ai-inc/UPduino-v3.0 | Verilog | 365 | 2026-07-21 | MIT | open | Vendor board repo + RGB blink example | V (p1 v2) |
| tinyvision-ai-inc/UPduino-v2.1 | Verilog | 29 | 2020-03-30 | MIT | open | v2.1 board + blink | U (v1, no pcf) |
| alangarf/apple-one | Verilog/SV | 153 | 2025-09-22 | Apache-2.0 | open | Apple-1 in Verilog; UPduino, iCEBreaker, other iCE40 boards, and one ECP5 lpf (25k) | V (p11 l1 v44) |
| osresearch/risc8 | Verilog | 30 | 2021-09-30 | none | open? | Mostly AVR-compatible 8-bit soft core | V (p1 v10) |
| tomverbeure/upduino | Verilog | 20 | 2024-04-02 | none | open | Minimal UPduino open-flow template | V (p1 v2) |
| gtjennings1/HyperBUS | Verilog | 64 | 2019-01-08 | none | open? | HyperRAM controller for iCE40 UltraPlus | V (p1 v23) |
| gtjennings1/UPDuino-OV7670-Camera | Verilog | 21 | 2018-02-08 | none | U | OV7670 camera capture on UPduino | U (not tree-checked) |
| igor-m/UPduino-Mecrisp-Ice-15kB | Verilog | 19 | 2025-11-05 | BSD-3-Clause | open? | Mecrisp-Ice Forth on a J1a 16-bit CPU | V (p3 v27) |
| ranzbak/fpga-workshop | Verilog | 23 | 2021-10-29 | none | open | 15-step UPduino workshop (VGA, UART and more) | V (p15 v48) |
| XarkLabs/upduino-video | SystemVerilog | 5 | 2024-02-29 | NOASSERTION | open | 8-colour VGA text generator | V (p1 sv7) |
| tinyvision-ai-inc/spi_slave | SystemVerilog | 4 | 2021-03-03 | NOASSERTION | U | SPI slave → 32-bit Wishbone bridge | U (no pcf) |

### Lattice iCE40 UltraPlus Breakout / generic UP5K (no specific board)

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| daveshah1/up5k-demos | Verilog/VHDL | 23 | 2020-10-12 | none | open | UP5K demos from the nextpnr author (DSP, SPRAM, video, and more) | V (p1 v37 vhd13) |
| Wren6991/SmolDVI | Verilog | 34 | 2021-07-15 | CC0-1.0 | open? | Low-area DVI/TMDS for UP5K and HX1K | V (p4 v12) |
| emeb/up5k_basic | Verilog | 54 | 2019-06-03 | MIT | open | 6502 + MS BASIC in ROM | V (p1 v19) |
| emeb/up5k_vga | Verilog | 29 | 2019-06-12 | MIT | open | 65C02 computer with VGA | V (p1 v18) |
| emeb/up5k_6502 | Verilog | 15 | 2019-03-11 | MIT | open | Simple 6502 system | V (p1 v5) |
| emeb/up5k_osc | Verilog | 35 | 2024-11-25 | MIT | open | Oscilloscope/DSP gateware (ADC, display) | V (p2 v19) |
| damdoy/fpga_peripherals | Verilog | 17 | 2020-06-14 | none | open | OV7670 camera, ST7735 LCD and other peripherals on the UP5K breakout | V (p1 v15) |
| ToNi3141/RasteriCEr | Verilog | 45 | 2021-11-14 | GPL-3.0 | open | OpenGL 1.x rasteriser for UP5K | V (p1 v17) |
| mcci-catena/catena-riscv32-fpga | Verilog | 10 | 2019-07-31 | NOASSERTION | open? | RISC-V SoC for the MCCI Catena 4710 (UP5K) | V (p7 v24) |
| johnMamish/jfpjc | Verilog | 8 | 2024-04-30 | MIT | U | JPEG compressor targeting UP5K | U (no pcf) |
| will127534/IMU_Array | Verilog | 342 | 2024-11-04 | MIT | U | 32× ICM-42688 IMU array aggregated by UP5K | V (p1 v3) |

### iCEBreaker / iCEBreaker-bitsy (iCE40UP5K-SG48), only repos new to sources.tsv

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| nickmqb/fpga_craft | Verilog (generated from Wyre) | 214 | 2025-10-28 | Apache-2.0 | open (yosys/nextpnr per README) | Voxel "Minecraft" game on UP5K + VGA + N64 pad | V (p1 v1) |
| SySS-Research/icebreaker-glitcher | Verilog | 21 | 2020-03-02 | NOASSERTION | open | Voltage glitcher | V (p1 v12) |
| esden/icekeeb | Verilog | 20 | 2022-04-09 | none | open? | Keyboard gateware + firmware | V (p3 v14) |
| kbob/icebreaker-synth | Amaranth | 28 | 2020-01-26 | GPL-3.0 | Amaranth | Audio synthesizer | U (Python only) |

Bitsy: icebreaker-fpga/icecrash (the bitsy "motherboard") has no HDL at HEAD. No bitsy-specific gateware was found beyond the known icebreaker-fpga repos.

### iCESugar v1.5 (iCE40UP5K), https://github.com/wuxx/icesugar (vendor repo already in sources.tsv)

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| jorislee/picorv32_ice40up5k_icesugar | Verilog | 3 | 2020-04-12 | none | open | PicoRV32 SoC on iCESugar | V (p1 v8) |
| metro94/LED_PWM_IP_Demo | Verilog | 6 | 2020-04-16 | none | open? | UP5K hard LED-PWM IP demo | V (p1 v2) |
| Archfx/ice40lib | Verilog | 8 | 2024-04-25 | none | open? | Peripheral library configured for iCESugar | V (p4 v11) |
| MuratovAS/icesugar-z80 / icesugar-riscv / icesugar-6502 | Verilog | 6/6/1 | 2023 | MIT | U | Z80/RISC-V/6502 VSCode projects | U (not tree-checked) |
| punzik/sugar-lissajous | SystemVerilog | 4 | 2021-03-03 | MIT | U | Light organ | U |
| nihirash/Ice81 | Verilog | 2 | 2021-03-28 | none | U | ZX81 on iCESugar | U |

### pico-ice / pico2-ice (RP2040/RP2350 + UP5K), https://github.com/tinyvision-ai-inc/pico-ice

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| tinyvision-ai-inc/pico-ice | SystemVerilog | 202 | 2025-07-04 | MIT | open | Board repo + gateware examples | V (p3 sv3) |
| tinyvision-ai-inc/pico-ice-sdk | Verilog/SV | 79 | 2026-03-06 | MIT | open (+some Amaranth) | RP2040 SDK + FPGA examples (8 pcf) | V (p8 v14 sv6) |
| MichaelBell/pico-ice-projects | Verilog | 2 | 2023-12-14 | MIT | open | Projects incl. a RISC-V core on pico-ice | V (p5 v40) |
| PythonLinks/pico2-ice-pong, frohro/pico2-ice_VGA-Pong | Verilog/SV | 0 | 2024/2025 | –/MIT | U | Pong on pico2-ice | U |

pico2-ice board repo: no HDL at HEAD.

### MCH2022 badge (iCE40UP5K), https://github.com/badgeteam/mch2022-firmware-ice40

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| badgeteam/mch2022-firmware-ice40 | Verilog | 14 | 2022-11-14 | NOASSERTION | open? (no2build submodule) | Official FPGA examples: LCD, PSRAM, SPI to ESP32 | V (p2 v82) |
| smunaut/mch2022-ice40 | Verilog | 4 | 2022-08-02 | NOASSERTION | open? (no2build) | tnt's badge experiments (video, PSRAM, audio) | V (p2 v57) |

### ICE-V Wireless (ESP32-C3 + UP5K)

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| ICE-V-Wireless/ICE-V-Wireless | Verilog/VHDL | 82 | 2025-10-06 | MIT | open | Vendor repo: board + gateware examples + ESP32 firmware | V (p4 v16) |

### OK-iCE40Pro (UP5K handheld game board)

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| WiFiBoy/OK-iCE40Pro | Verilog | 16 | 2023-05-06 | MIT | open | Educational game console: LCD, audio, 13 example designs | V (p13 v43) |

### RocketFPGA (UP5K audio board)

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| pablogs9/RocketFPGA | Verilog | 10 | 2020-04-19 | none | open | Audio codec board + audio DSP gateware (oscillators, filters) | V (p3 v39) |

### reDIP SID (UP5K, 5 V DIP-28)

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| daglem/reDIP-SID | SystemVerilog | 119 | 2024-09-23 | NOASSERTION | open | Cycle-accurate MOS 6581/8580 SID emulation | V (p1 v8 sv14) |
| emeb/up5k_resid | Verilog | 4 | 2021-10-15 | none | open | reDIP-SID gateware extended with audio in/out + DSP | V (p1 v17) |

### emeb boards: ICE-dongle and icehat (UP5K)

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| emeb/ice-dongle | Verilog | 7 | 2023-03-09 | MIT | open (+LiteX) | USB-C dongle; many example designs | V (p10 v35) |
| emeb/icehat | Verilog | 29 | 2017-01-27 | MIT | U | RPi hat + minimal gateware | V (p1 v2) |

### Other UP5K boards with gateware in their own repo

| board / repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| iCEboy → rniwase/tsuraraGB (renamed) | SystemVerilog | 16 | 2026-06-16 | BSD-3-Clause | open | Game Boy cartridge-shaped board + examples | V (p1 sv18) |
| iCE40-feather → joshajohnson/iCE40-feather | Verilog | 26 | 2022-08-11 | NOASSERTION | open | Feather board + examples | V (p5 v27) |
| lit3rick → kelu124/lit3rick | Verilog | 43 | 2024-07-16 | none | open | Ultrasound pulse-echo acquisition (ADC, pulser) | V (p1 v125) |
| pi_smi_up5k → braingram/pi_smi_up5k | Verilog | 16 | 2020-11-11 | none | open | RPi SMI-bus data link to UP5K | V (p3 v5) |
| SingularitySurfer → nkrackow/SingularitySurfer-FPGA-Lock-In-Amplifier (renamed) | Verilog | 79 | 2023-05-11 | MIT | open | DSP lock-in amplifier | V (p7 v36) |
| Vision FPGA SoM → tinyvision-ai-inc/Vision-FPGA-SoM | Verilog/SV | 48 | 2021-06-23 | MIT | open | Image-sensor SoM gateware | V (p2 v22 sv27) |
| PicoStation3D → Wren6991/PicoStation3D | Verilog | 50 | 2021-02-14 | CC0-1.0 | U | RP2040 + UP5K console; minimal HDL | V (p1 v1) |
| ice40helper → kehribar/ice40helper | Verilog | 6 | 2020-06-20 | none | open | Helper board + examples | V (p4 v11) |
| FPGA101 badge → mmicko/fpga101-workshop | Verilog | 81 | 2019-03-17 | MIT | open? | 20-exercise workshop for the UP5K badge | V (p20 v82) |
| icE1usb → osmocom/osmo-e1-hardware (GitHub mirror of gitea) | Verilog | 9 | 2024-11-22 | none on GitHub | open? (no2build) | Dual E1 (TDM) USB adapter gateware | V (p4 v25) |
| Precursor/betrusted-ec → betrusted-io/betrusted-ec | LiteX + Verilog | 50 | 2023-12-22 | NOASSERTION | LiteX | UP5K embedded controller SoC | U (no pcf; LiteX) |
| nrfICE → HurleyResearch/nRFICE | Verilog/VHDL | 8 | 2024-07-12 | GPL-3.0 | **Radiant** (`.rdf`) | nRF5340 + UP5K examples | U for open flow |
| WebFPGA → webfpga/webfpga_icestorm_examples, webfpga/verilog | Verilog | 5 / 11 | 2022 / 2019 | MIT | open (cloud) | ShastaPlus examples + std library | U (no pcf) |
| Doppler → noscene/ice40_audio | Verilog | 19 | 2018-04-30 | none | open | PCM5102 DAC driver | V (p2 v1) |

**UP5K boards with no gateware found:** ARISE (mfkiwl fork, hardware only), ice40-dip40, ice-dip, ice40-fpga-pico, ICE40UPDevBoard,
medhyal ice40-dev-board, ICEd ESPresso, Humble ICE (mkvenkit/humble_ice is not tree-checked), whatnick iCE40 Feather, MCUPduino,
MTX-BC48-DB (hardware only), S1 Module, DEF CON 28 DCFurs (no HDL in dc28 repo), NiCE5340 SoM (no HDL), dadamachines/doppler (no HDL).

---

## ECP5 boards (not already surveyed)

### Machdyne / Lone Dynamics: Schoko (45F), Konfekt (12F), Lakritz (25F), Obst (12F), Kopflos (12F)

Each board repo has one lpf plus a blinky and builds with the open flow (V). The main gateware, machdyne/zeitlos and nes_ecp5, is already in sources.tsv.
| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| machdyne/schoko, konfekt, lakritz, obst, kopflos | Verilog | 11/10/1/2/11 | 2023–2026 | NOASSERTION | open | Board files + blinky | V (l1 v1 each) |
| machdyne/fpga-dac | Verilog | 6 | 2024-06-17 | NOASSERTION | open | Sigma-delta DAC + PCM player (12k/45k lpfs) | V (l3 v3) |
| parport0/lakritz-hdl | Verilog | 0 | 2025-01-10 | 0BSD | open | HDL snippets for Lakritz | V (l1 v8) |
| machdyne/serbl | Verilog | 0 | 2025-06-01 | NOASSERTION | open | Serial bootloader for FPGAs (iCE40 pcf seen) | V (p1 v38) |

### GreyBadge 2025 (RP2350 + LFE5U-25F), https://github.com/NUSGreyhats/greybadge25

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| NUSGreyhats/greybadge25 | Verilog | 0 | 2026-02-05 | none | open (Makefile, --25k) | CTF badge gateware: main design + ~10 test designs | V (l11 v59) |

### TrellisBoard (LFE5UM5G-85F)

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| gatecat/TrellisBoard | Verilog + LiteX | 121 | 2019-07-04 | NOASSERTION | open / LiteX | Board + small bring-up gateware | V (l1 v2) |

### LimeSDR Mini 2.0 (ECP5 + LMS7002M)

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| myriadrf/LimeSDR-Mini-v2_GW | Verilog/VHDL | 25 | 2024-11-28 | Apache-2.0 | **Diamond** (mico32, synplify) | Official SDR gateware | V (l6 v73 vhd214), not open flow |
| enjoy-digital/litex_limesdr_mini_v2_test | LiteX | 5 | 2022-04-11 | none | LiteX | Alternative LiteX SoC | U |

natsfr/LimeSDR_DVBSGateware is for the MAX10-based Mini v1, so I dropped it.

### NUT2NT+ (GNSS front end, ECP5)

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| amungo/nut2nt | Verilog/VHDL | 26 | 2020-04-27 | none | **Diamond** (`.ldf`) | NT1065 → FT601 data path | V (l4 v18), not open flow |

### PicoFabric (LFE5U-12F module for RPi Pico)

| repo | HDL | stars | last push | license | toolchain | what it does | evidence |
|---|---|---|---|---|---|---|---|
| picolemon/picofabric-examples | VHDL | 0 | 2023-08-09 | NOASSERTION | U (VS Code flow) | Examples incl. HyperRAM | V (l7 vhd34) |

**ECP5 boards with no usable gateware found:**

- Only hardware or firmware at HEAD: FleaFPGA Ohm (Basman74/FleaFPGA-Ohm; its Minimig/Oberon repos have no HDL files matched; Minimig is covered by m1nl), SD2SNES-ECP5 (samlittlewood repo has no HDL at HEAD), TinySDR (uw-x/tinysdr has no .v/.vhd matched), OVIO core (Python only), Kilsyth (gregdavill/kilsyth has no HDL), Zeal video board (only an SDK is public), Elgato CamLink 4K (enjoy-digital/camlink_4k has no HDL at HEAD).
- No repo found: EPIC Erebus, Darsena/Private Island, FUSBee5, medhyal ecp5-dev-board, Kondor AX, Schlappi Three Body, Magewell.

---

## Recommended to clone (20)

The picks favour reusable Verilog blocks and board example sets on the open flow.

1. **ulixxe/usb_cdc**: pure-Verilog FS USB CDC-ACM core with 21 board pcfs. The most reusable block found, and it ports to ULX3S US2.
2. **daveshah1/up5k-demos**: UP5K demos from the nextpnr author, covering hard IP (SPRAM, DSP).
3. **Wren6991/SmolDVI**: tiny TMDS/DVI encoder (CC0) for small iCE40 parts.
4. **gtjennings1/HyperBUS**: standalone HyperRAM controller.
5. **im-tomu/fomu-workshop**: official Fomu examples (Verilog + VHDL + LiteX).
6. **daglem/reDIP-SID**: high-quality SystemVerilog SID emulation, and the audio blocks can be reused.
7. **badgeteam/mch2022-firmware-ice40**: badge examples (LCD, PSRAM, SPI slave).
8. **smunaut/mch2022-ice40**: tnt's reusable no2 cores on UP5K.
9. **osmocom/osmo-e1-hardware**: icE1usb gateware (E1 framer + USB), production code.
10. **alangarf/apple-one**: Apple-1 system with many board ports, including an ECP5 lpf.
11. **emeb/up5k_osc**: ADC/DSP oscilloscope gateware (active 2024).
12. **emeb/up5k_vga**: 65C02 + VGA computer (the emeb up5k_* family; `up5k_basic` is the smaller sibling).
13. **ToNi3141/RasteriCEr**: OpenGL-style rasteriser, a rare 3D graphics pipeline in Verilog.
14. **nickmqb/fpga_craft**: 3D voxel renderer on UP5K (generated Verilog, 214 stars).
15. **WiFiBoy/OK-iCE40Pro**: 13 example designs for a game-board (LCD, audio).
16. **pablogs9/RocketFPGA**: audio codec + DSP gateware.
17. **tinyvision-ai-inc/pico-ice-sdk**: vendor examples for pico-ice/pico2-ice (MCU+FPGA co-design).
18. **ranzbak/fpga-workshop**: 15-step UPduino tutorial on the open flow.
19. **NUSGreyhats/greybadge25**: new ECP5 LFE5U-25F badge with open-flow gateware (2026).
20. **machdyne/fpga-dac**: sigma-delta DAC/PCM player with ECP5 lpfs (12k/45k), a small reusable block.

Runners-up: osresearch/risc8 (AVR-compatible core), nkrackow/SingularitySurfer lock-in amplifier (DSP), mmicko/fpga101-workshop (cloned + catalogued 2026-09-28, with a review page),
ICE-V-Wireless/ICE-V-Wireless, emeb/ice-dongle, tinyvision-ai-inc/Vision-FPGA-SoM, igor-m/UPduino-Mecrisp-Ice.

## Notes, gaps, rate limits

- Search API: 63 repository queries, per_page=100, sort=stars, 7 s sleep. Six hit HTTP 403 "rate limit exceeded" (the quota was shared); each succeeded after a 60 s retry. Core API: about 15 calls used for metadata, and 45 of 60 were left.
- File lists come from codeload tarballs (`tar.gz/HEAD`). These do not count against the API quota. Git submodules are not included, so repos built on no2build (the MCH2022 and osmo-e1 repos) show "open?".
- Two awesome-list links have moved: rniwase/iCEboy is now rniwase/tsuraraGB, and SingularitySurfer's lock-in repo is now nkrackow/SingularitySurfer-FPGA-Lock-In-Amplifier. It is worth updating the awesome list.
- The awesome list has no entry for OK-iCE40Pro or RocketFPGA. I found both through GitHub search.
- msinger/iceboy (Game Boy clone) targets HX8K, not UP5K, so I dropped it.
- The "fomu", "vision fpga", "schoko", "iceboy" and "picostation" queries are very noisy (unrelated repos). I filtered them by hand.
- No evidence was found of open-flow gateware for LimeSDR Mini 2.0 or NUT2NT+. Both use Lattice Diamond.
{% endraw %}
