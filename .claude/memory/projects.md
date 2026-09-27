---
name: projects
description: Registry of every ULX3S-related project known or reviewed — functions provided, HDL/toolchain, target FPGA/revision, last upstream update, review status. The central index of "what people have done with the ULX3S".
metadata:
  type: project
---

# ULX3S project registry

Keep in sync with `.claude/memory/sources.tsv` (pinned clones) and `docs/projects/<slug>.md`
(details). Update the row + detail block in the same commit as the review.

Status values: `candidate` (known to exist, not cloned) → `cloned` → `reviewed`
(→ `stale` when upstream moved past the pinned commit and has not been re-reviewed).

## Function tags (shared vocabulary so projects are comparable)
`board-hw` (PCB/schematics), `constraints` (LPF), `video-dvi` (GPDI/HDMI/DVI out),
`video-composite`, `audio-dac`, `audio-spdif`, `audio-i2s`, `sdram`, `flash-spi`,
`sdcard`, `usb-device`, `usb-host`, `ps2`, `uart`, `jtag`, `esp32` (ESP32 interaction/passthru),
`adc`, `oled-lcd`, `ethernet`, `rtc-power`, `soc-cpu` (softcore SoC), `linux`,
`retro-computer`, `retro-console`, `dsp-sdr`, `bootloader`, `programmer-tool`,
`toolchain`, `examples` (collection of small demos), `education`.

## Summary table

| Slug | Kind | Functions | HDL / flow | Target | Last upstream commit | Status (date) |
|---|---|---|---|---|---|---|
| emard__ulx3s | Board hardware (KiCad) + manual | board-hw, constraints, toolchain docs | KiCad 4→5→7; no gateware | all 12/25/45/85F; PCB v1.7–v3.1.7 | 2025-04-27 (6a92cec) | reviewed (2026-09-27) |
| emard__ulx3s-bin | Prebuilt bitstreams + quickstart/self-test kit | examples, bootloader, esp32, soc-cpu, linux, retro-computer, sdram, ethernet, usb-host, adc, programmer-tool | binaries only (Diamond .vme era + open flow .bit.gz) | 12/25/45/85F, v17patch/v18/v20/v314/v317, ULX4M | 2022-04-19 (2a40f50) | reviewed (2026-09-27) |
| trabucayre__openfpgaloader | Universal FPGA programmer (C++) | programmer-tool, bootloader (DFU client) | CMake, libftdi/libusb | boards `ulx3s`, `ulx3s_dfu`, `ulx3s_esp`, `ulx4m_dfu` | 2026-09-23 (676e53e), v1.1.1 | reviewed (2026-09-27) |

## Detail blocks

### emard__ulx3s
- Upstream: https://github.com/emard/ulx3s — pinned 6a92cec (2025-04-27). 2732 commits since 2016-01-28;
  authors Emard (emard), Davor; Marko Zec minor. Tags up to v3.1.7.
- What it is: **the ULX3S board itself**: KiCad schematics/PCB, gerbers, BOM, 3D box, the
  user MANUAL, and the **reference constraint files** (`doc/constraints/ulx3s_v20.lpf`,
  `prototype/ulx3s_v17patch.lpf`, `ulx3s_v314.lpf`, `ulx3s_v316.lpf`).
- Gateware: none. It is the ground truth for pin names and board behaviour.
- License: modified MIT (EMARD/RADIONA/FER logos must stay on silkscreen).
- Activity: hardware stable since v3.1.7 (2021); 2023–2025 commits are docs/KiCad-7 DRC/TODO only.
- Reuse: take the LPF for your revision; signal names are the de-facto standard top ports.
- Facts extracted → [[board-hardware]], [[board-revisions]], [[toolchain-and-programming]].
- Page: `docs/projects/emard__ulx3s.md`.

### emard__ulx3s-bin
- Upstream: https://github.com/emard/ulx3s-bin, pinned 2a40f50. 327 commits, 2018-03-11 → 2022-04-19. Dormant.
- Quickstart kit: FT231X setup, **f32c self-test** (RTC/EDID/ADC/DAC/BTN/SW/LED), passthru, **DFU multiboot
  bootloader** (US2), memtest (SDRAM up to ~200 MHz), demos: hdl4fpga oscilloscope/Ethernet/slides, C64, Oberon,
  LiteX Linux, USB HID host, RTC. Full per-folder table with source projects in `docs/projects/emard__ulx3s-bin.md`.
- Reuse: known-good bitstreams to check hardware before debugging your own design. Points to hdl4fpga, f32c,
  had2019-playground and linux-on-litex-vexriscv as the upstream projects.

### trabucayre__openfpgaloader
- Upstream: https://github.com/trabucayre/openFPGALoader, pinned 676e53e. 2095 commits, 2019-09-26 → 2026-09-23. Very active.
- ULX3S support in `src/board.hpp`: `ulx3s` (FT231X bit-bang JTAG, SRAM+flash), `ulx3s_dfu` (US2 DFU 1d50:614b),
  `ulx3s_esp` (ESP32-S3 USB-JTAG, added 2025, working status unverified), `ulx4m_dfu`, `ulx2s`.
- Reuse: the default programmer to recommend. Page: `docs/projects/trabucayre__openfpgaloader.md`.

## Candidates (referenced but not yet cloned)
Found as links inside emard/ulx3s README/MANUAL (2026-09-27). Descriptions are **unverified**
and come from the link context only.

| Slug | Why it matters (unverified) |
|---|---|
| emard__ulx3s-passthru | FPGA passthru for programming the ESP32 over US1 |
| emard__esp32ecp5 | MicroPython on ESP32: program FPGA/flash/SD over WiFi |
| emard__libxsvf-esp | ESP32 Arduino JTAG SVF player (websvf) |
| emard__minimig_ecs | Amiga (Minimig ECS) port: retro-computer |
| emard__had2019-playground | Hackaday 2019 badge fork with the US2 DFU bootloader |
| f32c__f32c | f32c MIPS/RISC-V softcore SoC (the board's original purpose) |
| f32c__tools | ujprog programmer |
| kost__fujprog | fujprog programmer |
| gojimmypi__ulx3s-adda | Adapter board for AN108 fast ADC/DAC |
| tinyfpga__tinyfpga-bootloader | USB bootloader (US2) |
| alpin3__ulx3s | KOST's packaged ULX3S toolchain |
| emard__fleafpga-jtag | JTAG programmer for .vme files |
| emard__ulx2s | Predecessor board |
| hdl4fpga__hdl4fpga | Oscilloscope (ScopeIO), RMII Ethernet, DVI, USB CDC-ECM: source of several ulx3s-bin demos |
| litex-hub__linux-on-litex-vexriscv | Linux on ULX3S via LiteX/VexRiscv |
| smunaut__had2019-playground | Upstream of the DFU bootloader |
| intergalaktik__ulx4m-ls | ULX4M successor board |

Further candidates known from general knowledge (**unverified, check they exist**):
emard/ulx3s-misc, ulx3s/ulx3s-examples (lawrie), litex-hub/litex-boards (radiona_ulx3s),
SpinalHDL/SaxonSoc (ulx3s Linux), lawrie/ulx3s_examples, emard/ulx3s-usb.
