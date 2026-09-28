---
title: "trabucayre__openfpgaloader"
parent: "Project reviews"
nav_order: 14
---
<!-- Generated from data/projects/trabucayre__openfpgaloader.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# openFPGALoader (`trabucayre__openfpgaloader`)

| Field | Value |
|---|---|
| Upstream | https://github.com/trabucayre/openFPGALoader |
| Reviewed at | `676e53e` (upstream date 2026-09-23), reviewed 2026-09-27 |
| License | Apache-2.0 |
| Language | C++ (CMake), plus `spiOverJtag/` gateware for other vendors |
| Toolchain | CMake + libftdi/libusb; also bundled in YosysHQ oss-cad-suite |
| Target | Universal FPGA programmer (Xilinx, Intel, Lattice, Gowin, Efinix, Anlogic, Cologne Chip) |
| Activity | 2095 commits, 2019-09-26 → 2026-09-23, very active. Latest release v1.1.1 (2026-03-11). Main author Gwenhael Goavec-Merou |

## What it does for the ULX3S

Only the ULX3S-specific parts were reviewed (`src/board.hpp`, `src/cable.hpp`, `doc/boards.yml`, udev rules).

| Board ID (`-b`) | Transport | Notes |
|---|---|---|
| `ulx3s` | `ft231X` cable: FT231X on US1 (0403:6015) in **bit-bang** JTAG mode | TCK/TMS/TDI/TDO on DCD/DSR/RI/CTS. SRAM + SPI flash |
| `ulx3s_dfu` | USB DFU 1d50:614b on US2 | Needs the DFU bootloader from emard/had2019-playground (binaries in [ulx3s-bin](emard__ulx3s-bin.md)); flash only |
| `ulx3s_esp` | `esp32s3` cable (ESP USB-JTAG, 303a:1001) | Added 2025-04-18. The commit message says "it doesn't work" at that point; current status unverified |
| `ulx4m_dfu` | DFU 1d50:614b | Successor board ULX4M (LD/LS), https://github.com/intergalaktik/ulx4m-ls |
| `ulx2s` | FT232RL bit-bang | Predecessor board |

Common commands:

```bash
openFPGALoader -b ulx3s design.bit             # SRAM (default, -m optional)
openFPGALoader -b ulx3s -f design.bit          # SPI flash
openFPGALoader -b ulx3s design.bit.gz          # gzip accepted
openFPGALoader -b ulx3s_dfu design.bit         # via US2 DFU bootloader
openFPGALoader -b ulx3s --unprotect-flash --file-type bin -f multiboot.img.gz   # install bootloader image
openFPGALoader --detect -b ulx3s               # read IDCODE
```

udev: `70-openfpgaloader.rules` (uaccess) or `99-…` (group plugdev) include FT231X 0403:6015
and ULX3S/ULX4M DFU 1d50:614b.

## Reuse notes

- The recommended programmer for ULX3S today, and the default in our advice ([toolchain memory](https://github.com/kelu124/lattice-verilog-projects/blob/main/.claude/memory/toolchain-and-programming.md)).
- Bit-banged FT231X JTAG is slow. For large 85F bitstreams, an external FT2232 on the JTAG
  header (`-c ft2232`) or DFU is faster.

## Open questions

- Does `ulx3s_esp` (ESP32-S3 USB-JTAG) work now? What ESP32-S3 hardware does it target (not the onboard ESP32)?
{% endraw %}
