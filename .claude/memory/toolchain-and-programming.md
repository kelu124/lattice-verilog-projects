---
name: toolchain-and-programming
description: How ULX3S bitstreams are built and loaded — open toolchain, programmers (openFPGALoader, fujprog, OpenOCD, ESP32, DFU), flash layout and multiboot address, ESP32 passthru.
metadata:
  type: reference
---

Source: emard/ulx3s doc/MANUAL.md @ 6a92cec, read 2026-09-27.

Build (open flow): yosys `synth_ecp5` → nextpnr-ecp5 (`--12k/--25k/--45k/--85k --package CABGA381`,
`--lpf ulx3s_v20.lpf`) → ecppack (Project Trellis). Binary bundle recommended by the
manual: YosysHQ **oss-cad-suite-build** (also ships fujprog + openFPGALoader).
Older: KOST's alpin3/ulx3s .deb (2020), open-tool-forge fpga-toolchain (dead since 2021).
Closed: Lattice Diamond (needed only for .vme files).

The LPF's `SYSCONFIG ... MASTER_SPI_PORT=ENABLE` lets JTAG write flash at any time;
set `MASTER_SPI_PORT=DISABLE` if the **user bitstream** must drive the flash pins.

Programming:
- `openFPGALoader -b ulx3s x.bit` (SRAM), `-f` / `--write-flash` (flash); accepts .bit.gz.
- `fujprog x.bit`, `fujprog -j flash x.bit` (successor of ujprog). Both use FT231X on US1.
- OpenOCD with `ft232r` driver (slow) or external FT2232 on J4 JTAG header (fast, 25 MHz).
- ESP32: `emard/esp32ecp5` (MicroPython, FTP/web, can also write flash + SD) or
  `emard/LibXSVF-ESP` websvf (SVF, needs `-maxdata 8`).
- US2 DFU bootloader (fork of had2019 badge): `openFPGALoader -b ulx3s_dfu` or `dfu-util -a0 -D`.
  **Multiboot: user bitstream at flash byte 0x200000**, bootloader at 0. Solder D28 so BTN0 → PROGRAMN.
- udev: 0403:6015, group dialout.

ESP32 setup needs the **passthru** bitstream in FPGA flash (`emard/ulx3s-passthru`, binaries in
`emard/ulx3s-bin`) to route FT231X serial to the ESP32. A bitstream that holds `wifi_en` asserted
plus ESP32 firmware that grabs JTAG can brick JTAG; jumper J3 disables the ESP32.

**How to apply:** default to oss-cad-suite + openFPGALoader when advising new users. Record
each reviewed project's actual flow in [[projects]].
