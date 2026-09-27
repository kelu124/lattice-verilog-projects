# ULX3S board reference for gateware developers

A condensed reference for people writing new gateware for the ULX3S. Everything
here comes from [emard/ulx3s](https://github.com/emard/ulx3s) at `6a92cec` (2025-04-27):
the README, [`doc/MANUAL.md`](https://github.com/emard/ulx3s/blob/master/doc/MANUAL.md)
and the LPF constraint files. When in doubt, the manual and the LPF for your board revision are authoritative.

## The board at a glance

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

## GPIO details
- `gp/gn 0–7` (J1) and `22–27` (J2) are single-ended; `8–21` are true differential pairs.
- Clock-capable: `gp/gn 12` (differential primary clock), `gp/gn 0,1` (primary), `gp13`, `gn17` (general routing).
- Shared: `gp/gn 11–13` with ESP32 (v2.0+), `gp/gn 14–17` with the onboard ADC.
- 4 PMODs fit on J1/J2 with power and ground in the right places. J2 also carries 5 V in/out.

## Choosing the constraint file

| PCB revision | LPF |
|---|---|
| v1.7 | `doc/constraints/prototype/ulx3s_v17patch.lpf` |
| v2.x.x, v3.0.x (most boards in circulation) | `doc/constraints/ulx3s_v20.lpf` |
| v3.1.4 | `doc/constraints/prototype/ulx3s_v314.lpf` |
| v3.1.6, v3.1.7 (Mouser from 2022) | `doc/constraints/prototype/ulx3s_v316.lpf` |

The revision is printed on the PCB silkscreen. v3.1.x changed the ESP32 wiring
(`wifi_gpio16/17` removed, use `wifi_gpio26/27`), fixed GPDI hot-plug detect, and added SERDES RX pairs on an 8-pin OLED header.

## Build and load (open-source flow)

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

## Pitfalls
- Max USB input voltage is 6 V. GPIOs are 3.3 V only.
- In 1-bit SPI flash mode, drive `flash_wpn`/`flash_holdn` high (some ISSI parts fail otherwise).
- To drive flash pins from the user design, set `MASTER_SPI_PORT=DISABLE` in the LPF `SYSCONFIG` line.
- Leave `wifi_en` as input with pull-up unless you use the ESP32 on purpose. A bitstream holding the
  ESP32 enabled, combined with ESP32 firmware that grabs JTAG, can lock out JTAG (jumper J3 disables the ESP32).
- Composite/SPDIF on Ring2 needs an OMTP (Apple/Nokia) 3-RCA cable. Sony-wired cables put GND there.
- High-resolution GPDI video interferes with ESP32 WiFi on v3.0.x boards.
- The RTC on v2/v3.0 runs about 30 ppm fast.
