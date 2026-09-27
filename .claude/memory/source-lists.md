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
| GitHub search, other ECP5 boards (OrangeCrab, LUNA/Cynthion, iCESugar-Pro, HAD2019 badge, Colorlight, ButterStick, ECPIX-5, Logicbone, Versa/EVN, …), 53 queries | 2026-09-27 | 114 repos, ~85 verified by file list (.lpf + HDL), 24 recommended → `docs/ecp5-boards-survey.md`; top 14 cloned + catalogued 2026-09-27 (12 new; danodus__ecp5_hdmi_audio_video and wuxx__colorlight-fpga-projects were already in, rows refreshed); owner then added #21 joshajohnson/ecp5-mini-projects and kbeckmann/pergola_projects |
| codeberg.org/icebreaker-fpga org (14 repos) + github damdoy/ice40_ultraplus_examples (owner request) | 2026-09-27 | iCE40 UP5K, NOT ECP5. Cloned: icebreaker-verilog-examples, icebreaker-workshop, icetwang, damdoy. icecrash cloned then dropped (KiCad only, no HDL). Skipped: icestudio/migen/amaranth/litex examples, case, docs, board hw, pmod, v2-usb-firmware, pages |

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
