---
name: source-lists
description: Where lists of ULX3S projects come from (ulx3s.github.io "Projects and examples", emard/ulx3s links, GitHub search) and when each was last harvested — used to re-sync the collection.
metadata:
  type: reference
---

| Source | Harvested | Result |
|---|---|---|
| https://ulx3s.github.io/ section "Projects and examples" (between "ULX3S manual" and "Gitee examples") | 2026-09-27 | 69 git URLs; 68 cloned. `emard/ulx3s-examples` is 404 (use `ulx3s/ulx3s-examples`). Not clonable: BLE gist (vmedea), YouTube logic-analyzer video, bonfirecpu.eu blog, nxlab.fer.hr FPGArduino page |
| emard/ulx3s README + MANUAL links | 2026-09-27 | candidates in [[projects]] |
| emard/ulx3s-bin folder sources | 2026-09-27 | see docs/projects/emard__ulx3s-bin.md |
| GitHub search (repo/topic/readme/fork queries; code search not possible without auth) | 2026-09-27 | ≈297 candidates → `docs/github-survey.md`: A 155 verified, B 51, C 69 multi-board, D 11 forks, E 11 links. A+B+D+2(E, ULX4M) = 219 now cloned (see [[projects]]) — the other ~78 (C, and E minus the 2 ULX4M repos) skipped as not device-dedicated. How to repeat: skill `github-survey` |
| GitHub search `ulx5m` (repo, readme, forks, `ulx5m-gs`) | 2026-09-27 | 5 own repos + 7 forks + mentions → `docs/github-survey.md` group F; 3 were cloned then removed on owner request the same day; ULX5M is GateMate, not ECP5 |
| GitHub search, other ECP5 boards (OrangeCrab, LUNA/Cynthion, iCESugar-Pro, HAD2019 badge, Colorlight, ButterStick, ECPIX-5, Logicbone, Versa/EVN, …), 53 queries | 2026-09-27 | 114 repos, ~85 verified by file list (.lpf + HDL), 24 recommended → `docs/ecp5-boards-survey.md`; top 14 cloned + catalogued 2026-09-27, items 15–20 and 22–24 on 2026-09-28 (all 24 now in) (12 new; danodus__ecp5_hdmi_audio_video and wuxx__colorlight-fpga-projects were already in, rows refreshed); owner then added #21 joshajohnson/ecp5-mini-projects and kbeckmann/pergola_projects |
| codeberg.org/icebreaker-fpga org (14 repos) + github damdoy/ice40_ultraplus_examples (owner request) | 2026-09-27 | iCE40 UP5K, NOT ECP5. Cloned: icebreaker-verilog-examples, icebreaker-workshop, icetwang, damdoy. icecrash cloned then dropped (KiCad only, no HDL). Skipped: icestudio/migen/amaranth/litex examples, case, docs, board hw, pmod, v2-usb-firmware, pages |
| GitHub search `up5k`/`icebreaker`/`ice40up5k`/`upduino` (language verilog, by stars; hit the search rate limit) | 2026-09-28 | cloned 8: smunaut/ice40-playground, smunaut/iCE40linux, osresearch/up5k, bit-hack/icesid, bnossum/midgetv, kbob/icebreaker-candy, jamchamb/cojiro, wuxx/icesugar (+11 gateware submodules: no2 cores, osdvu, wuxx forks of up5k_6502/up5k-demos/iceZ0mb1e). Other hits (UPduino-v2.1, Mecrisp-Ice, OK-iCE40Pro, RocketFPGA, fpga-workshop, Hands-on-FPGA-class, i2c_oled_bresenham, icebreaker-glitcher…) not cloned |
| kelu124/awesome-latticeFPGAs `Readme.md` (UP5K + ECP5 boards; boards already in ecp5-boards-survey skipped) | 2026-09-28 | ~30 UP5K + 6 ECP5 boards with gateware (Fomu, UPduino, pico-ice, MCH2022, Machdyne, GreyBadge…), ~28 boards with none found → `docs/lattice-boards-survey.md`, 20 recommended, all 20 cloned + catalogued 2026-09-28 (+2 gateware submodules: no2e1, hoglet67 verilog-6502) |
| kelu124/awesome-latticeFPGAs HX8K/HX4K boards (1 subagent, 13 searches, tarball listings) | 2026-09-28 | ~40 boards, ~110 repos → `docs/hx-boards-survey.md`, 20 recommended; 19 cloned + catalogued 2026-09-28 (+2 RISCBoy gateware submodules hazard5, libfpga); abnoname/iceZ0mb1e skipped (already the wuxx__icesugar submodule); the 8 honourable mentions (glasgow, BlackIce-II, apollo11_fpga, nanoV, dsp_ice, Centurion, BeagleWire, fpga-3-softcores +2 submodules) cloned + catalogued 2026-09-28 |
| Owner-named repos: gatecat/TrellisBoard, ZipCPU/sdspi, toasterllc/MDCCode | 2026-09-28 | cloned + pinned; catalogue rows written 2026-09-28 |

The ulx3s.github.io page also has a "Gitee examples" section (Chinese mirror/examples), not yet harvested.

**How to apply:** to refresh the collection, re-fetch these sources, diff the list against
`sources.tsv`, clone new ones with `clone.sh`, and add a row for each here with the new date.
Many ulx3s.github.io entries list two URLs (an original and an `ulx3s/` or `emard/` fork); both
were cloned, and the registry notes which copy has the ULX3S port.

Frameworks with ULX3S board support (from the survey): litex-boards `radiona_ulx3s`, amaranth-boards `ulx3s.py`,
apio `ulx3s-{12,25,45,85}f`, icestudio, Silice `frameworks/boards/ulx3s`, fusesoc/blinky, SaxonSoc `bsp/radiona/ulx3s`,
neorv32-setups (osflow ULX3S), YoWASP toolchain-demo, cascade (Verilog JIT), CFU-Playground (via LiteX).
Notable high-value candidates: BrunoLevy/learn-fpga, darklife/darkriscv, Wren6991/Hazard3 (+ ulx3s/Hazard3-Doom),
lawrie/fpga_pio, dan-rodrigues/icestation-32, gatecat|emard/SNES_MiSTer_ulx3s, sylefeb/a5k, sylefeb/tinygpus,
the ~25 lawrie/ulx3s_* retro machines (Mac 128, MSX, BBC Micro, QL, Amstrad CPC, ColecoVision, Atari 2600, VIC-20…).
