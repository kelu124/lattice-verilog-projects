---
name: board-hardware
description: Key ULX3S hardware facts and pitfalls that matter when writing gateware (clock, peripherals, GPIO sharing, power, audio, display). Source is emard/ulx3s README + doc/MANUAL.md.
metadata:
  type: reference
---

Verified from `original_sources/emard__ulx3s` @ 6a92cec (README.md, doc/MANUAL.md,
doc/constraints/*.lpf), 2026-09-27. Full human reference: `docs/boards/ulx3s.md`.

- FPGA: Lattice ECP5 LFE5U-{12,25,45,85}F, package CABGA381, speed grade -6 (README).
  JTAG IDCODEs: 12F 0x21111043, 25F 0x41111043, 45F 0x41112043, 85F 0x41113043.
- Clock: single 25 MHz oscillator on `clk_25mhz` (site G2). Everything else via EHXPLLL.
- SDRAM: 16-bit SDR, MT48LC16M16-class 32 MB on most boards (README allows 8–64 MB;
  production boards also used AS4C32M16SB, M12L2561616A, IS42S16160G — see [[board-revisions]]).
- Config flash: QSPI 4–16 MB (IS25LP / W25Q128JV / S25FL064L depending on batch).
  In 1-bit SPI mode, hold unused IO lines high or some ISSI chips fail (crosstalk).
- USB: US1 = FT231X (JTAG + serial, VID:PID 0403:6015); US2 = FPGA-direct USB
  (`usb_fpga_*`, 1.5/12 Mbps, host or device on v2.0+; PS/2 via adapter).
- Video: GPDI (HDMI/DVI-style connector), 4 TMDS pairs `gpdi_dp/dn[3:0]`, I2C for EDID
  (`gpdi_sda/scl`), CEC. Series coupling caps (220 nF on v2/v3.0, 22 nF on v3.1.4+).
  HPD does not work on v2.x/v3.0.x.
- Audio jack (OMTP TRRS): Tip=L, Ring1=R, Ring2=SPDIF or composite video, 4-bit DAC per
  channel (`audio_l/r/v[3:0]`), 75 Ω. Sony-wired cables are wrong.
- ADC: MAX11125 8-ch 12-bit 1 MSa/s total (SPI `adc_*`). Shares J2 GP/GN 14–17.
- OLED/LCD header: 7 pin CS DC RES SDA SCL VCC GND (ST7789, SSD1331, SSD1351, SSD1306).
- 7 buttons `btn[6:0]` = PWRn (active-low, pull-up), FIRE1, FIRE2, UP, DOWN, LEFT, RIGHT
  (active-high, pull-down) — verified in ulx3s_v20.lpf;
  8 LEDs, 4 DIP switches `sw[3:0]`.
- GPIO: 56 pins on J1/J2 (`gp/gn[27:0]`), 3.3 V, **not 5 V tolerant**.
  0–7 and 22–27 single-ended; 8–21 true differential. GP/GN 12 = differential primary
  clock input; GP/GN 0,1 primary clock capable.
  Sharing: GP/GN 11–13 with ESP32 (v2.0+; 9–13 on v1.7); GP/GN 14–17 with the ADC.
  LAN8720 RMII Ethernet modules plug on GP/GN 9–13 at 3.3 V.
- SD card: all signals to FPGA, shared with ESP32.
- ESP32 (optional, WROOM or WROVER): `wifi_en`, `wifi_gpio*`, `wifi_rxd/txd`. It can
  JTAG-program the FPGA. Pin sets differ between v3.0.x and v3.1.x, see [[board-revisions]].
- Power: `shutdown` pin lets the FPGA power the board off (RTC MCP7940N alarm wakes it);
  needs RTC battery and a configured alarm. Max USB input 6 V. 3.3 V-only power is impossible.
- Onboard FM/ASK antenna trace `ant_433mhz` (88–108 / 433 MHz transmit by toggling a pin).

**How to apply:** use these signal names (from `ulx3s_v20.lpf`) as the canonical top-level port
names in new designs. They are what most community projects use, so code stays portable.
