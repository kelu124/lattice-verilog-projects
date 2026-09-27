---
name: board-revisions
description: ULX3S PCB revisions (v1.7 → v3.1.7), what differs for gateware, and which .lpf constraint file each needs.
metadata:
  type: reference
---

Source: emard/ulx3s doc/MANUAL.md "Board differences" + "Board Versions" table,
@ 6a92cec, read 2026-09-27.

| PCB | LPF to use | Notes for gateware |
|---|---|---|
| v1.7 | `doc/constraints/prototype/ulx3s_v17patch.lpf` | 8+1 made. 1-bit SPI flash, ESP32 needs wire patch, BTN routing differs, US2 incomplete |
| v1.8 | `v18` (file not found in repo — unverified) | 10 prototypes |
| v2.0.x, v2.1.x, v3.0.x | `doc/constraints/ulx3s_v20.lpf` | **Most common** (v3.0.3 ×~475, v3.0.7 ×96, v3.0.8 ×1000+). QSPI flash, full US2, 220 nF GPDI caps, HPD broken |
| v3.1.4 | `doc/constraints/prototype/ulx3s_v314.lpf` | ESP32 JTAG moved, WROVER support, 22 nF GPDI caps, HPD works, 8-pin OLED header with SERDES RX pairs |
| v3.1.6, v3.1.7 | `doc/constraints/prototype/ulx3s_v316.lpf` | v3.1.6: ESP32 GPIO0 needs FPGA pull-up to boot (15k patch). v3.1.7 adds R56 and boots standalone. Sold at Mouser from 2022 |

Pitfalls:
- The MANUAL links `/doc/constraints/ulx3s_v17patch.lpf` but the file actually lives in
  `doc/constraints/prototype/`. Same for v314/v316.
- v3.1.x ESP32 pinout changed: `wifi_gpio16/17` are gone (WROVER uses them for PSRAM),
  so use `wifi_gpio26/27` instead. Designs talking to the ESP32 are revision-specific.
- v3.1.x: if esptool can't program through passthru, short TMS to GND on the JTAG header.
- Around v3.0.5 an extra FTDI line gives a slow secondary JTAG channel (softcore debug).

**How to apply:** when reviewing or writing a design, always record which LPF/revision it
targets. When a design touches ESP32, GPDI HPD or flash pins, check the revision first.
See [[board-hardware]].
