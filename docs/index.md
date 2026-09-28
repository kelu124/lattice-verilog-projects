<!-- Generated from data/pages/index.json by .claude/skills/documentation/gen_pages.py; do not edit. -->

# ulx3s-klod: open gateware for the ULX3S and small Lattice boards

A knowledge base of **open gateware for the [ULX3S](https://github.com/emard/ulx3s) FPGA board** (Radiona, Lattice ECP5 LFE5U-12F/25F/45F/85F) and, for reuse, other small Lattice boards (ECP5, iCE40 UP5K, iCE40 HX8K/HX4K). It records which projects exist, what their gateware does, which FPGA and toolchain they target, their license, whether they have testbenches, and which blocks can be lifted into a new design.

Use it to **find prior art before writing a core**: a DVI encoder, a USB device, an SDRAM or HyperRAM controller, a RISC-V SoC, an ESP32 on-screen display, a retro computer… Start with the [reusable cores map](https://github.com/kelu124/ulx3s-klod/blob/main/.claude/memory/reusable-cores.md), then the catalogue and the project pages below.

Every page here is generated from JSON in [`data/`](https://github.com/kelu124/ulx3s-klod/tree/main/data) (do not edit `docs/` by hand); the repo also holds Claude's working memory, see the [README](https://github.com/kelu124/ulx3s-klod/blob/main/README.md).

## Catalogues

- [Project catalogue](catalogue.md): every cloned repo with FPGA, toolchain, HDL, license, functions, reusable blocks and tests (from `data/catalogue.json`)
- [LPF catalogue](lpf-catalogue.md): every ECP5 pin-constraint file with board, revision, FPGA size and peripherals (from `data/lpfs.json`)

## Guides

- [USB DFU bootloaders and DFU programming flows](DFUs.md): USB DFU bootloaders and flows: the ULX3S/ULX4M US2 bootloader (source, alt settings, flash layout, recovery) and OrangeCrab, Fomu, no2bootloader, pico-ice, BlackIce.

## Board reference

- [ULX3S board reference for gateware developers](board-reference.md): ULX3S hardware at a glance: FPGA sizes, peripherals, canonical signal names, constraint files per revision, build and load commands, pitfalls.

## Surveys (candidate lists)

- [ECP5 (non-ULX3S) gateware survey on GitHub](ecp5-boards-survey.md): Gateware for other ECP5 boards (OrangeCrab, LUNA, iCESugar-Pro, HAD2019, Colorlight, ButterStick, ECPIX-5…): 114 repos, 24 recommended.
- [GitHub survey of ULX3S repositories (2026-09-27)](github-survey.md): GitHub-wide search for ULX3S gateware (2026-09-27): ~297 candidates in groups A–F with evidence and clone status.
- [iCE40 HX4K / HX8K gateware survey (from awesome-latticeFPGAs)](hx-boards-survey.md): Gateware for the iCE40 HX8K/HX4K boards of awesome-latticeFPGAs: 20 recommended plus 8 honourable mentions.
- [UP5K and ECP5 boards from awesome-latticeFPGAs: gateware survey](lattice-boards-survey.md): Gateware for the iCE40 UP5K and ECP5 boards of awesome-latticeFPGAs: 20 recommended, all catalogued.

## Project pages (18)

Full reviews with per-block reuse notes (module, ports, vendor primitives, license, what to change for a ULX3S design).

| Project | Target FPGA | License | HDL |
|---|---|---|---|
| [chrismoos__m6502](projects/chrismoos__m6502.md) | 85F by default | MIT (`LICENSE`, "Copyright 2026 Chris Moos") | SystemVerilog |
| [danodus__ecp5_hdmi_audio_video](projects/danodus__ecp5_hdmi_audio_video.md) | **85F**, CABGA381, `--85k` | MIT (`LICENSE`: Copyright (c) 2026 Daniel Cliche, Copyright (c) 2019 Sameer Puri) | Verilog-2001 |
| [emard__ulx3s-bin](projects/emard__ulx3s-bin.md) | 12F / 25F / 45F / 85F | none stated in the repo | n/a: prebuilt `.bit`/`.bit.gz`/`.svf`/`.vme`/`.img` files, no HDL sources |
| [emard__ulx3s-misc](projects/emard__ulx3s-misc.md) | 12F mostly, also 25F/85F, plus `um-85k` | No repo-level `LICENSE` file. | Verilog and VHDL roughly 60/40 |
| [emard__ulx3s](projects/emard__ulx3s.md) | LFE5U-12F / 25F / 45F / 85F, CABGA381 | Modified MIT | None (hardware project). KiCad 4 up to v1.8, then KiCad 5; opened/saved with KiCad 7 in… |
| [f32c__f32c](projects/f32c__f32c.md) | 12F / 25F / 45F / 85F | BSD-2-Clause, repo-wide | VHDL (bulk of `rtl/cpu`, `rtl/soc`, `rtl/lattice`), a handful of Verilog leaf modules… |
| [hdl4fpga__hdl4fpga](projects/hdl4fpga__hdl4fpga.md) | 12F (`apps.ldf` `device="LFE5U-12F-8BG381C"`, all three apps share one project/device) | MIT (`LICENSE`, Miguel Angel Sagreras) for all VHDL/Verilog source checked (headers on… | VHDL (this repo is ~all VHDL; the catalogue's "274" file count and the "Verilog, JS"… |
| [lawrie__ulx3s_examples](projects/lawrie__ulx3s_examples.md) | Mixed per example: root `ulx3s.mk` defaults `DEVICE ?= 85k`, but most example `Makefile`s… | none stated: no `LICENSE`/`COPYING` file anywhere in the repo | Verilog (194 `.v` files per `.claude/memory/catalogue.tsv`); one VHDL demo… |
| [lawrie__ulx3s_sms](projects/lawrie__ulx3s_sms.md) | **85F default** | No repo-level `LICENSE` file | Verilog only |
| [smunaut__ice40-playground](projects/smunaut__ice40-playground.md) | **iCE40 UP5K only** | No single top-level license | Verilog (170 files across `cores/` + `projects/`) |
| [spritetm__hadbadge2019_fpgasoc](projects/spritetm__hadbadge2019_fpgasoc.md) | 45F — `LFE5U-45F-6BG381`, `nextpnr-ecp5 --45k --package CABGA381` (`soc/Makefile`) | No single top-level license: per-file SPDX-less headers referencing one of `LICENSE.bsd`,… | Verilog (95 files, own) + submodule `soc/picorv32` (41 files) |
| [sylefeb__silice](projects/sylefeb__silice.md) | 12F / 25F / 45F / 85F | Mixed, by directory. | **Silice** |
| [trabucayre__openfpgaloader](projects/trabucayre__openfpgaloader.md) |  | Apache-2.0 |  |
| [ulixxe__usb_cdc](projects/ulixxe__usb_cdc.md) | iCE40 UP5K SG48 | MIT (`LICENSE`, Copyright (c) 2021 ulixxe) | Verilog-2001 |
| [ultraembedded__orangecrab](projects/ultraembedded__orangecrab.md) | unknown — no `--25k`/`--85k` device flag anywhere in source; OrangeCrab r0.2 boards ship… | Apache-2.0 | Verilog (11 files) + 1 SystemVerilog file (`ecp5pll.sv`) |
| [wren6991__smoldvi](projects/wren6991__smoldvi.md) | iCE40 UP5K | CC0-1.0 (`LICENSE.md`) | Verilog (12 `.v` files) |
| [yosyshq__picorv32](projects/yosyshq__picorv32.md) | iCE40 HX8K | ISC (`COPYING`; per-file headers, e.g. `picorv32.v:1-17`) | Verilog (41 `.v` files: `picorv32.v` core + `picosoc/`, `scripts/*`, `tests/*.S` assembly) |
| [zipcpu__sdspi](projects/zipcpu__sdspi.md) | none — vendor-neutral; no `.pcf`/`.xdc`/`.lpf`/`.sdc` anywhere in the repo (verified:… | GPL-3.0 (per-file headers, e.g. `rtl/spi/sdspi.v:22` "License: GPL, v3";… | Verilog (85 `.v` files total: 37 in `rtl/`, 48 test/model files in `bench/`) |
