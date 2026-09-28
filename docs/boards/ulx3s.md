---
title: "ULX3S"
parent: "ECP5 boards"
grand_parent: "Boards"
nav_order: 1
---
<!-- Generated from data/boards.json, data/pages/board-reference.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# ULX3S

The main board of this collection: 32 MB SDR SDRAM, GPDI (HDMI) port, ESP32, US1 FT231X + US2 direct USB, SD card, MAX11125 ADC, OLED header, 56 GPIO.

| | |
|---|---|
| Board | Radiona ULX3S |
| FPGA | LFE5U-12F/25F/45F/85F, CABGA381 |
| Evidence | emard/ulx3s MANUAL + reference LPFs (doc/constraints) |
| Clock | 25 MHz (clk_25mhz, reference LPF) |
| Catalogued repos | 373 |

## Board reference



A condensed reference for people writing new gateware for the ULX3S. Everything
here comes from [emard/ulx3s](https://github.com/emard/ulx3s) at `6a92cec` (2025-04-27):
the README, [`doc/MANUAL.md`](https://github.com/emard/ulx3s/blob/master/doc/MANUAL.md)
and the LPF constraint files. When in doubt, the manual and the LPF for your board revision are authoritative.

### The board at a glance

| Block | Part | Top-level signals (`ulx3s_v20.lpf`) |
|---|---|---|
| FPGA | Lattice ECP5 LFE5U-12F/25F/45F/85F, CABGA381, -6 | — |
| Clock | 25 MHz oscillator (site G2) | `clk_25mhz` |
| SDRAM | 16-bit SDR, 32 MB typical (MT48LC16M16 / IS42S16160G / AS4C32M16SB) | `sdram_clk, cke, csn, rasn, casn, wen, ba[1:0], a[12:0], dqm[1:0], d[15:0]` |
| Config flash | QSPI 4–16 MB (IS25LP128F, W25Q128JV, …) | `flash_csn, flash_clk, flash_mosi, flash_miso, flash_wpn, flash_holdn` (`flash_clk` is the dedicated config clock pin U3; ECP5 designs usually drive it through the `USRMCLK` primitive, which is general ECP5 knowledge and not stated in this repo) |
| USB US1 | FT231X, JTAG + UART (0403:6015) | `ftdi_rxd, ftdi_txd, ftdi_nrts, ftdi_ndtr, ftdi_txden` |
| USB US2 | Direct to FPGA, 1.5/12 Mbps, host/device | `usb_fpga_dp/dn, usb_fpga_bd_dp/dn, usb_fpga_pu_dp/dn` |
| Video | GPDI connector (TMDS/LVDS, HDMI-compatible plug) | `gpdi_dp[3:0], gpdi_dn[3:0], gpdi_sda, gpdi_scl, gpdi_cec, gpdi_hpd` |
| Audio | 3.5 mm TRRS (OMTP): L, R, SPDIF/composite; 4-bit resistor DAC each | `audio_l[3:0], audio_r[3:0], audio_v[3:0]` |
| ADC | MAX11125, 8 ch, 12 bit, 1 MSa/s shared | `adc_csn, adc_sclk, adc_mosi, adc_miso` |
| Display | 7-pin header: ST7789 / SSD1331 / SSD1351 / SSD1306 | `oled_csn, oled_clk, oled_mosi, oled_dc, oled_resn` |
| SD card | micro-SD, 4-bit, shared with ESP32 | `sd_clk, sd_cmd, sd_d[3:0], sd_cdn, sd_wp` |
| WiFi/BT | ESP32 WROOM/WROVER (optional) | `wifi_en, wifi_rxd, wifi_txd, wifi_gpio*` |
| User I/O | 8 LEDs, 7 buttons, 4 DIP switches | `led[7:0], btn[6:0], sw[3:0]` |
| GPIO | J1/J2, 56 pins, 3.3 V, not 5 V tolerant | `gp[27:0], gn[27:0]` |
| Power | RTC MCP7940N wake-up, FPGA-driven power-off | `shutdown` |
| RF | PCB antenna trace, 88–108 / 433 MHz | `ant_433mhz` |

Buttons: `btn[0]` = PWR (active-low), `btn[1..6]` = FIRE1, FIRE2, UP, DOWN, LEFT, RIGHT (active-high).

### GPIO details

- `gp/gn 0–7` (J1) and `22–27` (J2) are single-ended; `8–21` are true differential pairs.
- Clock-capable: `gp/gn 12` (differential primary clock), `gp/gn 0,1` (primary), `gp13`, `gn17` (general routing).
- Shared: `gp/gn 11–13` with ESP32 (v2.0+), `gp/gn 14–17` with the onboard ADC.
- 4 PMODs fit on J1/J2 with power and ground in the right places. J2 also carries 5 V in/out.

### Choosing the constraint file

| PCB revision | LPF |
|---|---|
| v1.7 | `doc/constraints/prototype/ulx3s_v17patch.lpf` |
| v2.x.x, v3.0.x (most boards in circulation) | `doc/constraints/ulx3s_v20.lpf` |
| v3.1.4 | `doc/constraints/prototype/ulx3s_v314.lpf` |
| v3.1.6, v3.1.7 (Mouser from 2022) | `doc/constraints/prototype/ulx3s_v316.lpf` |

The revision is printed on the PCB silkscreen. v3.1.x changed the ESP32 wiring
(`wifi_gpio16/17` removed, use `wifi_gpio26/27`), fixed GPDI hot-plug detect, and added SERDES RX pairs on an 8-pin OLED header.

### Build and load (open-source flow)

```bash
yosys -p "synth_ecp5 -top top -json top.json" top.v
nextpnr-ecp5 --85k --package CABGA381 --lpf ulx3s_v20.lpf --json top.json --textcfg top.config
ecppack --compress top.config top.bit
openFPGALoader -b ulx3s top.bit          # to SRAM
openFPGALoader -b ulx3s -f top.bit       # to config flash
```

Use `--12k`, `--25k` or `--45k` to match your chip. Easiest install: YosysHQ
[oss-cad-suite-build](https://github.com/YosysHQ/oss-cad-suite-build/releases/).
Alternatives: `fujprog`, OpenOCD with an FT2232 on the JTAG header (fastest), ESP32 over WiFi
([esp32ecp5](https://github.com/emard/esp32ecp5)), or the US2 DFU bootloader
(`openFPGALoader -b ulx3s_dfu`; user image at flash offset `0x200000`).

### Pitfalls

- Max USB input voltage is 6 V. GPIOs are 3.3 V only.
- In 1-bit SPI flash mode, drive `flash_wpn`/`flash_holdn` high (some ISSI parts fail otherwise).
- To drive flash pins from the user design, set `MASTER_SPI_PORT=DISABLE` in the LPF `SYSCONFIG` line.
- Leave `wifi_en` as input with pull-up unless you use the ESP32 on purpose. A bitstream holding the
  ESP32 enabled, combined with ESP32 firmware that grabs JTAG, can lock out JTAG (jumper J3 disables the ESP32).
- Composite/SPDIF on Ring2 needs an OMTP (Apple/Nokia) 3-RCA cable. Sony-wired cables put GND there.
- High-resolution GPDI video interferes with ESP32 WiFi on v3.0.x boards.
- The RTC on v2/v3.0 runs about 30 ppm fast.

## Constraint files (LPF)

Most-copied distinct LPFs for this board in the cloned repos (from the [LPF catalogue](https://github.com/kelu124/lattice-verilog-projects/blob/main/methodology/lpf-catalogue.md)).

| LPF | Revision | Copies | Peripherals constrained |
|---|---|---|---|
| [`ulx3s_v20.lpf`](https://github.com/lawrie/ulx3s_examples/blob/b6ff00099265401fef4843e4e89c2ac54254c95f/audio/piano/ulx3s_v20.lpf) (lawrie__ulx3s_examples) | v2.x/v3.0.x (ulx3s_v20) | 48 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, ps2, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb |
| [`ulx3s.lpf`](https://github.com/adrmcintyre/vixen/blob/e2db4fda79d2e73a7a595ce1773de64203346c0b/ulx3s/ulx3s.lpf) (adrmcintyre__vixen) | v2.x/v3.0.x (ulx3s_v20) | 42 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb |
| [`ulx3s_v20.lpf`](https://github.com/ahamidi87/simpleblinky/blob/b3d9c4bcdebf65733916ec63e47e0db2bc48fc95/ulx3s_v20.lpf) (ahamidi87__simpleblinky) | v2.x/v3.0.x (ulx3s_v20) | 40 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb |
| [`ulx3s_v20.lpf`](https://github.com/chiplet/ulx3s-blinky/blob/656e60b55080998d95237ee440e5033ae32c6749/constr/ulx3s_v20.lpf) (chiplet__ulx3s-blinky) | v2.x/v3.0.x (ulx3s_v20) | 20 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb |
| [`ulx3s_v316.lpf`](https://github.com/danodus/ecp5_hdmi_audio_video/blob/a4710f9e7986fe9aafde765b8b3f264ca61631be/boards/ulx3s/ulx3s_v316.lpf) (danodus__ecp5_hdmi_audio_video) | v3.1.6/v3.1.7 (ulx3s_v316) | 14 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb |
| [`ulx3s_v20.lpf`](https://github.com/emard/Papilio-Arcade/blob/4f91f938c200f1b0d80f03f835bdadcc5f21aa58/pacman_rel004_sp3e_papilio/proj/lattice/ulx3s/pacman_ulx3s_v20_12f/ulx3s_v20.lpf) (emard__papilio-arcade) | v2.x/v3.0.x (ulx3s_v20) | 13 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb |
| [`ulx3s_v20.lpf`](https://github.com/diegob94/ulx3s_blink/blob/1d465a44289aac1c3a024004abae6eb9a2609e08/ulx3s_v20.lpf) (diegob94__ulx3s_blink) | v2.x/v3.0.x (ulx3s_v20) | 12 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb |
| [`ulx3s_v20_segpdi.lpf`](https://github.com/Circuit-killer/fpga-usbserial/blob/bc9e18e84df7025315bd08c71bc4d17b0b5b6a0b/proj/lattice/ulx3s/constraints/ulx3s_v20_segpdi.lpf) (circuit-killer__fpga-usbserial) | v2.x/v3.0.x (ulx3s_v20) | 11 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb |
| [`ulx3s.lpf`](https://github.com/danodus/msx_fpga/blob/f3266f78762094ab3eb5621279011efb504c69df/ulx3s/ulx3s.lpf) (danodus__msx_fpga) | v2.x/v3.0.x (ulx3s_v20) | 10 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, ps2, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb |
| [`ulx3s_v20.lpf`](https://github.com/danodus/ulx3s_sms/blob/13c2361a5039d205de47857bab9201055ac9e566/ulx3s/ulx3s_v20.lpf) (danodus__ulx3s_sms) | v2.x/v3.0.x (ulx3s_v20) | 9 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb |
| [`ulx3s_v20.lpf`](https://github.com/f32c/f32c/blob/7dbf56d42a94ae599eabfd1e7fa15db14a10afd7/rtl/proj/lattice/constraints/ulx3s_v20.lpf) (f32c__f32c) | v2.x/v3.0.x (ulx3s_v20) | 9 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb |
| [`ulx3s_v20.lpf`](https://github.com/StereoNinja/StereoNinjaFPGA/blob/2def6f03fb93285817ced475b7c67dee756ac51a/old/Componets/HDMI_Transciever/TMDS_Encoder/ulx3s_v20.lpf) (stereoninja__stereoninjafpga) | v2.x/v3.0.x (ulx3s_v20) | 8 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb |

## Reusable cores seen on this board

Cores whose source repo, or a repo that copies/instantiates them, targets this board.

| Core | Function | Source repo |
|---|---|---|
| Digital down-converter + AM/FM demod chain (post-ADC) | [adc](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/adc.md) | emeb__orangecrab_adc |
| MAX1112x ADC reader (ulx3s-emi copy) | [adc](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/adc.md) | emard__ulx3s-emi |
| MAX1112x ADC reader (ulx3s-misc) | [adc](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/adc.md) | emard__ulx3s-misc |
| I2S audio interface (ulx3s-misc) | [audio-digital](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/audio-digital.md) | emard__ulx3s-misc |
| S/PDIF transmitter (f32c) | [audio-digital](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/audio-digital.md) | f32c__f32c |
| S/PDIF transmitter (synthowheel) | [audio-digital](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/audio-digital.md) | emard__synthowheel |
| Hazard3-Doom vendored DFU bootloader (ULX4M-LD validated) | [bootloader-dfu](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/bootloader-dfu.md) | ulx3s__hazard3-doom |
| Machdyne tinydfu-bootloader (ECP5, TinyFPGA-derived USB core) | [bootloader-dfu](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/bootloader-dfu.md) | machdyne__tinydfu-bootloader |
| TinyFPGA USB Bootloader (USB-serial-to-SPI-flash bridge) | [bootloader-dfu](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/bootloader-dfu.md) | tinyfpga__tinyfpga-bootloader |
| ULX3S/ULX4M USB DFU bootloader (had2019-playground) | [bootloader-dfu](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/bootloader-dfu.md) | emard__had2019-playground |
| no2bootloader (Nitro) iCE40 UP5K DFU bootloader | [bootloader-dfu](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/bootloader-dfu.md) | no2fpga__no2bootloader |
| no2usb DFU runtime + dfu_helper.v (iCE40) | [bootloader-dfu](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/bootloader-dfu.md) | smunaut__ice40-playground |
| AHB-Lite crossbar/arbiter/APB bridge | [bus-fabric](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/bus-fabric.md) | ulx3s__hazard3 |
| wb_intercon Wishbone mux/arbiter (olofk) | [bus-fabric](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/bus-fabric.md) | kulp__tenyr |
| OV7670 RGB/YUV capture + color-filter + VGA preview (ULX3S apio) | [camera](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/camera.md) | jderobot__fpga-robotics |
| OV7670 camera capture + SCCB config core | [camera](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/camera.md) | msrraju07__iop |
| OV7670 capture + SCCB master (ulx3s-experiments) | [camera](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/camera.md) | tucanae47__ulx3s-experiments |
| camera85 nMigen OV7670 capture + image pipeline | [camera](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/camera.md) | lawrie__ulx3s-nmigen-examples |
| MiST composite/RGB scandoubler (composite-video input side) | [composite-video](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/composite-video.md) | hoglet67__ice40beeb |
| f32c PAL composite video (CVBS) generator | [composite-video](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/composite-video.md) | f32c__f32c |
| CDP1802-compatible core (SpinalHDL) | [cpu-retro](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-retro.md) | lawrie__fpgacosmacelf |
| TMS9900-family CPU core (public domain) | [cpu-retro](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-retro.md) | pnru__ti99 |
| TV80 Z80-compatible core (emard__ulx3s_galaksija copy) | [cpu-retro](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-retro.md) | emard__ulx3s_galaksija |
| cpu_6502 (Klaus Dormann-verified 6502 core) | [cpu-retro](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-retro.md) | chrismoos__m6502 |
| danielh186 6502-compatible CPU core (FPGA-proven) | [cpu-retro](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-retro.md) | danielh186__6502-tapeout |
| fx68k 68000-compatible core (nullobject vendored copy) | [cpu-retro](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-retro.md) | nullobject__m68k-ulx3s |
| grom toy 8-bit CPU + computer (FPGA 101 original) | [cpu-retro](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-retro.md) | mmicko__fpga101-workshop |
| i8080-compatible core (Bashkiria-2M-derived) | [cpu-retro](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-retro.md) | lawrie__ulx3s_examples |
| FPGA 101 PicoSoC with LCD text console and MicroPython | [cpu-riscv](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-riscv.md) | mmicko__fpga101-workshop |
| Hazard3 RV32IMAC core | [cpu-riscv](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-riscv.md) | wren6991__hazard3 |
| KianV RV32IMA+Sv32 core (Linux-capable) | [cpu-riscv](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-riscv.md) | splinedrive__kianriscv |
| LUNA-SoC VexRiscv SoC framework (Moondancer's CPU) | [cpu-riscv](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-riscv.md) | greatscottgadgets__luna-soc |
| PicoRV32 RISC-V core | [cpu-riscv](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-riscv.md) | yosyshq__picorv32 |
| VexRiscv (SpinalHDL-generated Verilog) | [cpu-riscv](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-riscv.md) | rschlaikjer__fpga-3-softcores |
| f32c RISC-V/MIPS-compatible core | [cpu-riscv](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-riscv.md) | f32c__f32c |
| Pipelined double-SHA256 hasher | [crypto](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/crypto.md) | xtrinch__fpga-bitcoin-miner |
| Pruned 64-stage double-SHA256 miner pipeline | [crypto](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/crypto.md) | williamsharkey__pruned-sha256-miner |
| Ring-oscillator TRNG | [crypto](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/crypto.md) | krishkc5__trng-ring-oscillator |
| SRNG ring-oscillator TRNG + Blake2s DRBG | [crypto](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/crypto.md) | secworks__cryptkey |
| secworks AES-128/256 core (via ct-key) | [crypto](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/crypto.md) | assured__ct-key |

## Projects targeting this board

373 catalogued repos target this board; see the [full catalogue](https://github.com/kelu124/lattice-verilog-projects/blob/main/methodology/catalogue.md). Those with a full review:

- [chrismoos__m6502](https://github.com/kelu124/lattice-verilog-projects/blob/main/projects/chrismoos__m6502.md): m6502: compact microcoded cycle-accurate 6502 in SystemVerilog + MCU wrapper
- [danodus__ecp5_hdmi_audio_video](https://github.com/kelu124/lattice-verilog-projects/blob/main/projects/danodus__ecp5_hdmi_audio_video.md): ULX3S/IcePi Zero: HDMI audio+video transmitter core
- [emard__ulx3s](https://github.com/kelu124/lattice-verilog-projects/blob/main/projects/emard__ulx3s.md): ULX3S board hardware
- [emard__ulx3s-misc](https://github.com/kelu124/lattice-verilog-projects/blob/main/projects/emard__ulx3s-misc.md): ULX3S misc/advanced examples: EMARD's building-block library
- [f32c__f32c](https://github.com/kelu124/lattice-verilog-projects/blob/main/projects/f32c__f32c.md): f32c: retargetable RISC-V/MIPS 32-bit soft CPU + SoC library
- [hdl4fpga__hdl4fpga](https://github.com/kelu124/lattice-verilog-projects/blob/main/projects/hdl4fpga__hdl4fpga.md): hdl4fpga: portable VHDL library, ScopeIO oscilloscope, SDRAM graphics, eth/USB links
- [lawrie__ulx3s_examples](https://github.com/kelu124/lattice-verilog-projects/blob/main/projects/lawrie__ulx3s_examples.md): Lawrie Griffiths Verilog examples: HDMI, displays, PS/2, SDRAM, USB host, CPUs
- [lawrie__ulx3s_sms](https://github.com/kelu124/lattice-verilog-projects/blob/main/projects/lawrie__ulx3s_sms.md): Sega Master System / SG-1000: TV80, VDP, SN76489, SDRAM carts, ESP32 OSD
- [mmicko__fpga101-workshop](https://github.com/kelu124/lattice-verilog-projects/blob/main/projects/mmicko__fpga101-workshop.md): FPGA 101 workshop
- [sylefeb__silice](https://github.com/kelu124/lattice-verilog-projects/blob/main/projects/sylefeb__silice.md): Silice HDL language/compiler + many ULX3S projects
- [trabucayre__openfpgaloader](https://github.com/kelu124/lattice-verilog-projects/blob/main/projects/trabucayre__openfpgaloader.md): openFPGALoader universal programmer
{% endraw %}
