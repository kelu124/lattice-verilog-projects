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
