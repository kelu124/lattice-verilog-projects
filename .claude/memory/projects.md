---
name: projects
description: Registry of every ULX3S-related project known or reviewed — functions provided, HDL/toolchain, target FPGA/revision, last upstream update, review status. The central index of "what people have done with the ULX3S".
metadata:
  type: project
---

# ULX3S project registry

Keep in sync with `.claude/memory/sources.tsv` (pinned clones) and `data/projects/<slug>.json` (→ `docs/projects/<slug>.md`)
(details). Update the row + detail block in the same commit as the review.

Status values: `candidate` (known to exist, not cloned) → `cloned` → `catalogued`
(TSV row filled in) → `reviewed` (full docs page) (→ `stale` when upstream moved
past the pinned commit and has not been re-reviewed).

## Function tags (shared vocabulary so projects are comparable)
`board-hw` (PCB/schematics), `constraints` (LPF), `video-dvi` (GPDI/HDMI/DVI out),
`video-composite`, `audio-dac`, `audio-spdif`, `audio-i2s`, `sdram`, `flash-spi`,
`sdcard`, `usb-device`, `usb-host`, `ps2`, `uart`, `jtag`, `esp32` (ESP32 interaction/passthru),
`adc`, `oled-lcd`, `ethernet`, `rtc-power`, `soc-cpu` (softcore SoC), `linux`,
`retro-computer`, `retro-console`, `dsp-sdr`, `bootloader`, `programmer-tool`,
`toolchain`, `examples` (collection of small demos), `education`,
`retro-arcade`, `radio-rx`, `radio-tx`, `synth-audio`, `logic-analyzer`, `flash-emulator`, `adapter-board`,
`pmod-hardware`, `camera`, `eink`, `lvds-display`, `led-matrix`, `video-input`, `multiboot`, `multi-board`,
`fm-transmitter`, `debug-instrument`, `hdl-language`, `os-software` (added 2026-09-27 by the survey).

## Summary table → `data/catalogue.json`
The per-repo facts (kind, name, fork/preferred copy, ULX3S build path, **FPGA**, **toolchain**,
**HDL**, **license**, LPF, function tags, reusable blocks, notes, tests, make_tests) live in
[`data/catalogue.json`](../../data/catalogue.json) (moved from `.claude/memory/catalogue.tsv` on 2026-09-28), one
object per slug in `sources.tsv`. Render the human view with
`.claude/skills/review-gateware-project/gen_catalogue.py` → `docs/methodology/catalogue.md` (`--merge rows.tsv` adds rows).
Review pages are `data/projects/<slug>.json` rendered to `docs/projects/<slug>.md` (see [[data-docs-layout]]).

Status as of 2026-09-28: **523 repos catalogued (= 523 pinned in sources.tsv; +125 on 2026-09-28 late: GitHub-survey groups C (69) and E (9), registry candidates (9), DFU bootloaders (4), lit3rick, ulx3s.github.io harvest (4), RF/DSP (15) and FFT (15) surveys; +mmicko__fpga101-workshop; +9 ECP5-5G SERDES repos and +12 ECPIX-5/Cynthion repos from the two 2026-09-28 surveys; +emard__had2019-playground, +8 HX honourable mentions, +9 ECP5-survey items 15–24 on 2026-09-28): 290 ULX3S/ULX4M + 14 on other ECP5 boards** (+ gatecat__trellisboard ECP5, zipcpu__sdspi vendor-neutral, toasterllc__mdccode iCE40 HX8K, and 19 iCE40 HX8K/HX4K repos from `docs/methodology/hx-boards-survey.md` on 2026-09-28, of which wren6991__riscboy also has a ULX3S 85F target) (top 14 of `docs/methodology/ecp5-boards-survey.md`, 2 of which were already in, + ecp5-mini-projects + pergola_projects) **+ 12 iCE40 UP5K** (iCEBreaker org on codeberg + damdoy, then 8 from a GitHub search and 20 from `docs/methodology/lattice-boards-survey.md` on 2026-09-28 (2 of those are ECP5: greybadge25, machdyne fpga-dac); FPGA column says `NOT ECP5`) (ULX5M-GS repos were added then removed on owner request, 2026-09-27; see [[ulx5m-board]]) (71 pre-survey — the board repo,
ulx3s-bin, openFPGALoader, plus 68 of the 69 ulx3s.github.io "Projects and examples" links (one is a
404) — + 155 from GitHub-search category A + 64 more from categories B (51, all ULX3S-dedicated), D
(11, forks with own commits) and the 2 ULX4M-specific repos in E; first pass by read-only agents over
Makefiles, LPFs, READMEs, license files and a testbench heuristic; not built — and for this last batch
of 64, several turned out to have no real ULX3S/ULX4M build despite matching the survey, see
`docs/methodology/catalogue.md`'s notes). Only the 20 in the detail blocks below also have a full docs page (`reviewed`); the
rest are `catalogued`. The GitHub survey found ≈297 candidates in total; the remaining ~78 (category C,
multi-board, and E minus the 2 ULX4M repos) are listed in `docs/methodology/github-survey.md` but not yet cloned —
skipped deliberately since they are not primarily about ULX3S/ULX4M devices.
Cross-project map of reusable cores: [[reusable-cores]].

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

## Reviewed 2026-09-28 (most reusable gateware; full pages)
- `emard__ulx3s-misc`: reference ULX3S peripheral examples: ecp5pll, DVI, USB host/CDC, SDRAM, SPI displays, ESP32 SPI RAM, ADC, FM. Page: `docs/projects/emard__ulx3s-misc.md`.
- `lawrie__ulx3s_examples`: ~100 Verilog examples: PS/2, ST7789, PicoRV32 SD menu, HDMI, SDRAM. Page: `docs/projects/lawrie__ulx3s_examples.md`.
- `lawrie__ulx3s_sms`: Sega Master System + the ESP32 SPI OSD stack (src/osd/) reused by many retro ports. Page: `docs/projects/lawrie__ulx3s_sms.md`.
- `f32c__f32c`: MIPS/RISC-V SoC, ULX3S self-test; BSD peripherals (SPDIF, FM/RDS, DVI); Diamond, trellis not working. Page: `docs/projects/f32c__f32c.md`.
- `hdl4fpga__hdl4fpga`: ScopeIO, SDR..DDR3 controller, full Ethernet stack (MIT), Diamond only. Page: `docs/projects/hdl4fpga__hdl4fpga.md`.
- `sylefeb__silice`: Silice language + ULX3S framework, HDMI/SDRAM/RISC-V cores in .si (compile step needed). Page: `docs/projects/sylefeb__silice.md`.
- `ulixxe__usb_cdc`: portable USB CDC-ACM device (MIT, no vendor primitives, 48 MHz); no ULX3S example in repo. Page: `docs/projects/ulixxe__usb_cdc.md`.
- `wren6991__smoldvi`: tiny DVI encoder (CC0); ECP5 needs an ODDRX1F ddr_out. Page: `docs/projects/wren6991__smoldvi.md`.
- `danodus__ecp5_hdmi_audio_video`: HDMI with audio, ULX3S top, ECP5-native serializer (MIT). Page: `docs/projects/danodus__ecp5_hdmi_audio_video.md`.
- `zipcpu__sdspi`: SD SPI/SDIO/eMMC Wishbone cores (GPL-3.0), SPI mode drop-in for ULX3S sd_* pins. Page: `docs/projects/zipcpu__sdspi.md`.
- `yosyshq__picorv32`: RISC-V core + PicoSoC (ISC), portable; iCE40 tops only. Page: `docs/projects/yosyshq__picorv32.md`.
- `chrismoos__m6502`: SystemVerilog 6502 with tests (MIT), ULX3S 85F bring-up top. Page: `docs/projects/chrismoos__m6502.md`.
- `smunaut__ice40-playground`: no2fpga cores (USB, HyperRAM, QPI, cache, HUB75) with SB_*→ECP5 porting map. Page: `docs/projects/smunaut__ice40-playground.md`.
- `ultraembedded__orangecrab`: DDR3 AXI controller for ECP5 (Apache-2.0), OrangeCrab memtest. Page: `docs/projects/ultraembedded__orangecrab.md`.
- `spritetm__hadbadge2019_fpgasoc`: HAD2019 badge SoC: QPI PSRAM cache, ECP5 USB FS PHY, video/audio (per-file licenses). Page: `docs/projects/spritetm__hadbadge2019_fpgasoc.md`.
- `kelu124__lit3rick`: owner's open ultrasound board, iCE40 UP5K (ADC capture, 16-point sliding DFT, SPI/I2C), Radiant + partial open flow. Page: `docs/projects/kelu124__lit3rick.md`.
- `mmicko__fpga101-workshop`: FPGA 101 workshop (Hackaday Belgrade 2018), 20 UP5K exercises; original of the grom CPU and of ulx3s__fpga-odysseus (same author). Page: `docs/projects/mmicko__fpga101-workshop.md`.
- `emard__had2019-playground` (cloned + catalogued 2026-09-28): source of the ULX3S/ULX4M US2 DFU bootloader. Page: `docs/guides/DFUs.md`.

## Candidates (known, not cloned yet)
| Slug | Why it matters (unverified) |
|---|---|
| gregdavill/foboot (branch OrangeCrab) | OrangeCrab DFU bootloader source (clone.sh cannot select a branch yet) |
| myriadrf/LimeSDR_GW, LimeSDR-Mini-v2_GW, mehrdadh/fsk-modulator, chiralhat/fpga-pulses | next RF/DSP candidates (rf-dsp-survey) |
| ulx3s/ttsky-verilog-template (branch ulx3s) | Tiny Tapeout template with ULX3S port (branch needed) |

All earlier candidates (fujprog, TinyFPGA bootloader, LibXSVF-ESP, FleaFPGA-JTAG, ULX2S, ULX4M-LS, litex-boards,
oberon_sdram, smunaut had2019-playground, GitHub survey groups C and E) were cloned + catalogued on 2026-09-28.

`spinalhdl__saxonsoc`, `stnolting__neorv32-setups` and `lawrie__jupiter_ace` were also candidates here but
turned up already cloned by the GitHub-wide search — removed from this list.
GitHub-wide search results (2026-09-27) are recorded in [[source-lists]].
