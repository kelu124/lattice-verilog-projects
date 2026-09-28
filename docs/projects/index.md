---
title: "Project reviews"
nav_order: 5
has_children: true
permalink: "/projects/"
---
<!-- Generated from data/projects/*.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# Project reviews

In-depth reviews of the repos that hold the most reusable gateware: per-block reuse notes (module, ports, vendor primitives, license, what to change for a ULX3S design).

| Project | Target FPGA | License | HDL |
|---|---|---|---|
| [chrismoos__m6502](chrismoos__m6502.md) | 85F by default | MIT (`LICENSE`, "Copyright 2026 Chris Moos") | SystemVerilog |
| [danodus__ecp5_hdmi_audio_video](danodus__ecp5_hdmi_audio_video.md) | **85F**, CABGA381, `--85k` | MIT (`LICENSE`: Copyright (c) 2026 Daniel Cliche, Copyright (c) 2019 Sameer Puri) | Verilog-2001 |
| [emard__ulx3s-bin](emard__ulx3s-bin.md) | 12F / 25F / 45F / 85F | none stated in the repo | n/a: prebuilt `.bit`/`.bit.gz`/`.svf`/`.vme`/`.img` files, no HDL sources |
| [emard__ulx3s-misc](emard__ulx3s-misc.md) | 12F mostly, also 25F/85F, plus `um-85k` | No repo-level `LICENSE` file. | Verilog and VHDL roughly 60/40 |
| [emard__ulx3s](emard__ulx3s.md) | LFE5U-12F / 25F / 45F / 85F, CABGA381 | Modified MIT | None (hardware project). KiCad 4 up to v1.8, then KiCad 5; opened/saved with KiCad 7 in… |
| [f32c__f32c](f32c__f32c.md) | 12F / 25F / 45F / 85F | BSD-2-Clause, repo-wide | VHDL (bulk of `rtl/cpu`, `rtl/soc`, `rtl/lattice`), a handful of Verilog leaf modules… |
| [hdl4fpga__hdl4fpga](hdl4fpga__hdl4fpga.md) | 12F (`apps.ldf` `device="LFE5U-12F-8BG381C"`, all three apps share one project/device) | MIT (`LICENSE`, Miguel Angel Sagreras) for all VHDL/Verilog source checked (headers on… | VHDL (this repo is ~all VHDL; the catalogue's "274" file count and the "Verilog, JS"… |
| [lawrie__ulx3s_examples](lawrie__ulx3s_examples.md) | Mixed per example: root `ulx3s.mk` defaults `DEVICE ?= 85k`, but most example `Makefile`s… | none stated: no `LICENSE`/`COPYING` file anywhere in the repo | Verilog (194 `.v` files per `.claude/memory/catalogue.tsv`); one VHDL demo… |
| [lawrie__ulx3s_sms](lawrie__ulx3s_sms.md) | **85F default** | No repo-level `LICENSE` file | Verilog only |
| [smunaut__ice40-playground](smunaut__ice40-playground.md) | **iCE40 UP5K only** | No single top-level license | Verilog (170 files across `cores/` + `projects/`) |
| [spritetm__hadbadge2019_fpgasoc](spritetm__hadbadge2019_fpgasoc.md) | 45F — `LFE5U-45F-6BG381`, `nextpnr-ecp5 --45k --package CABGA381` (`soc/Makefile`) | No single top-level license: per-file SPDX-less headers referencing one of `LICENSE.bsd`,… | Verilog (95 files, own) + submodule `soc/picorv32` (41 files) |
| [sylefeb__silice](sylefeb__silice.md) | 12F / 25F / 45F / 85F | Mixed, by directory. | **Silice** |
| [trabucayre__openfpgaloader](trabucayre__openfpgaloader.md) |  | Apache-2.0 |  |
| [ulixxe__usb_cdc](ulixxe__usb_cdc.md) | iCE40 UP5K SG48 | MIT (`LICENSE`, Copyright (c) 2021 ulixxe) | Verilog-2001 |
| [ultraembedded__orangecrab](ultraembedded__orangecrab.md) | unknown — no `--25k`/`--85k` device flag anywhere in source; OrangeCrab r0.2 boards ship… | Apache-2.0 | Verilog (11 files) + 1 SystemVerilog file (`ecp5pll.sv`) |
| [wren6991__smoldvi](wren6991__smoldvi.md) | iCE40 UP5K | CC0-1.0 (`LICENSE.md`) | Verilog (12 `.v` files) |
| [yosyshq__picorv32](yosyshq__picorv32.md) | iCE40 HX8K | ISC (`COPYING`; per-file headers, e.g. `picorv32.v:1-17`) | Verilog (41 `.v` files: `picorv32.v` core + `picosoc/`, `scripts/*`, `tests/*.S` assembly) |
| [zipcpu__sdspi](zipcpu__sdspi.md) | none — vendor-neutral; no `.pcf`/`.xdc`/`.lpf`/`.sdc` anywhere in the repo (verified:… | GPL-3.0 (per-file headers, e.g. `rtl/spi/sdspi.v:22` "License: GPL, v3";… | Verilog (85 `.v` files total: 37 in `rtl/`, 48 test/model files in `bench/`) |
{% endraw %}
