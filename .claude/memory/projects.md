---
name: projects
description: Registry of every ULX3S-related project known or reviewed — functions provided, HDL/toolchain, target FPGA/revision, last upstream update, review status. The central index of "what people have done with the ULX3S".
metadata:
  type: project
---

# ULX3S project registry

Keep in sync with `.claude/memory/sources.tsv` (pinned clones) and `docs/projects/<slug>.md`
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

## Summary table → `catalogue.tsv`
The per-repo facts (kind, name, fork/preferred copy, ULX3S build path, **FPGA**, **toolchain**,
**HDL**, **license**, LPF, function tags, reusable blocks, notes) live in
[`catalogue.tsv`](catalogue.tsv), one row per slug in `sources.tsv`. Render the human view with
`.claude/skills/review-gateware-project/gen_catalogue.py` → `docs/catalogue.md`.

Status as of 2026-09-27: **336 repos cloned and catalogued: 290 ULX3S/ULX4M + 14 on other ECP5 boards** (top 14 of `docs/ecp5-boards-survey.md`, 2 of which were already in, + ecp5-mini-projects + pergola_projects) **+ 12 iCE40 UP5K** (iCEBreaker org on codeberg + damdoy, then 8 from a GitHub search and 20 from `docs/lattice-boards-survey.md` on 2026-09-28 (2 of those are ECP5: greybadge25, machdyne fpga-dac); FPGA column says `NOT ECP5`) (ULX5M-GS repos were added then removed on owner request, 2026-09-27; see [[ulx5m-board]]) (71 pre-survey — the board repo,
ulx3s-bin, openFPGALoader, plus 68 of the 69 ulx3s.github.io "Projects and examples" links (one is a
404) — + 155 from GitHub-search category A + 64 more from categories B (51, all ULX3S-dedicated), D
(11, forks with own commits) and the 2 ULX4M-specific repos in E; first pass by read-only agents over
Makefiles, LPFs, READMEs, license files and a testbench heuristic; not built — and for this last batch
of 64, several turned out to have no real ULX3S/ULX4M build despite matching the survey, see
`docs/catalogue.md`'s notes). Only the three below also have a full docs page (`reviewed`); the
rest are `catalogued`. The GitHub survey found ≈297 candidates in total; the remaining ~78 (category C,
multi-board, and E minus the 2 ULX4M repos) are listed in `docs/github-survey.md` but not yet cloned —
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

## Candidates (known, not cloned yet)
| Slug | Why it matters (unverified) |
|---|---|
| emard__libxsvf-esp | ESP32 Arduino JTAG SVF player (websvf) |
| kost__fujprog | fujprog programmer (ujprog successor) |
| tinyfpga__tinyfpga-bootloader | USB bootloader (US2) |
| emard__fleafpga-jtag | JTAG programmer for .vme files |
| emard__ulx2s | Predecessor board |
| emard__had2019-playground, smunaut__had2019-playground | DFU bootloader source |
| intergalaktik__ulx4m-ls | ULX4M successor board |
| litex-hub__litex-boards | `radiona_ulx3s` platform/target used by linux-on-litex |
| alangarf__apple-one, basman74__oberon_sdram | upstreams of already-cloned forks |
| gitee ULX3S examples | section after "Projects and examples" on ulx3s.github.io |
| GitHub survey groups C (69, multi-board) and E-minus-ULX4M (9) | in `docs/github-survey.md`; skipped 2026-09-27 as not device-dedicated |

`spinalhdl__saxonsoc`, `stnolting__neorv32-setups` and `lawrie__jupiter_ace` were also candidates here but
turned up already cloned by the GitHub-wide search — removed from this list.
GitHub-wide search results (2026-09-27) are recorded in [[source-lists]].
