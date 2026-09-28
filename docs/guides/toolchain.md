---
title: "Build and load"
parent: "Guides"
nav_order: 1
---
<!-- Generated from data/pages/toolchain.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# Build and load bitstreams (open toolchain)

Source: the ULX3S [MANUAL](https://github.com/emard/ulx3s/blob/master/doc/MANUAL.md) (emard/ulx3s @ 6a92cec, read 2026-09-27) and the programmers catalogued here ([openFPGALoader review](../projects/trabucayre__openfpgaloader.md)).

## Build (ECP5)

yosys `synth_ecp5` → nextpnr-ecp5 → ecppack (Project Trellis):

```bash
yosys -p "synth_ecp5 -top top -json top.json" top.v
nextpnr-ecp5 --85k --package CABGA381 --lpf ulx3s_v20.lpf --json top.json --textcfg top.config
ecppack top.config top.bit
```

- Pick `--12k`, `--25k`, `--45k` or `--85k` for your chip; the ULX3S package is always `CABGA381`.
- Use `ulx3s_v20.lpf` for boards v2.x/v3.0.x and `ulx3s_v316.lpf` for v3.1.6/v3.1.7 (see the [ULX3S board page](../boards/ulx3s.md) and the [LPF catalogue](../methodology/lpf-catalogue.md)).
- A common trick: build with `--25k` and pass `--idcode 0x21111043` to ecppack to load the bitstream on a 12F (same die).
- Toolchain bundle recommended by the manual: YosysHQ **oss-cad-suite-build** (also ships fujprog and openFPGALoader). Lattice Diamond is only needed for Diamond-only historical projects and `.vme` files.

## Build (iCE40)

yosys `synth_ice40` → nextpnr-ice40 (`--up5k --package sg48`, `--hx8k --package ct256`, HX4K boards: `--hx8k --package tq144:4k`) → icepack. Older designs use arachne-pnr instead of nextpnr-ice40.

## Load (ULX3S)

| Tool | SRAM | Flash | Notes |
|---|---|---|---|
| openFPGALoader | `openFPGALoader -b ulx3s top.bit` | `openFPGALoader -b ulx3s -f top.bit` | Recommended; accepts `.bit.gz`. `-b ulx3s_dfu` uses the US2 DFU bootloader |
| fujprog | `fujprog top.bit` | `fujprog -j flash top.bit` | Successor of ujprog; FT231X on US1 |
| OpenOCD | `ft232r` driver (slow) |  | Or an external FT2232 on the J4 JTAG header |
| ESP32 | emard/esp32ecp5 (MicroPython, FTP/web) | yes | Can also write the SD card |
| dfu-util |  | `dfu-util -a0 -D top.bit` | Needs the [DFU bootloader](DFUs.md); user image at flash 0x200000 |

- The LPF line `SYSCONFIG ... MASTER_SPI_PORT=ENABLE` lets JTAG write the flash at any time; set `MASTER_SPI_PORT=DISABLE` if the user bitstream must drive the flash pins.
- Linux udev: FT231X is `0403:6015` (group `dialout`).
- The ESP32 needs the **passthru** bitstream in FPGA flash (emard/ulx3s-passthru) to be flashed from US1. A bitstream that holds `wifi_en` asserted plus ESP32 firmware that grabs JTAG can lock JTAG out; jumper J3 disables the ESP32.
{% endraw %}
