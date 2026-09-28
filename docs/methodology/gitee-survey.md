---
title: "Gitee / ulx3s.github.io harvest"
parent: "Methodology"
nav_order: 4
---
<!-- Generated from data/pages/gitee-survey.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# Gitee examples from ulx3s.github.io

Date: 2026-09-28

## Method

1. Fetched https://ulx3s.github.io/ with curl (28 067 bytes) and extracted every `<a href>` from the heading
   "Gitee examples (China's answer to GitHub)" to the end of the page (sections Toolchains and Utilities,
   Tiny Tapeout, Tiny Tapeout Projects using the ULX3S, Other ULX3S Links, Articles, Forums, Blogs, Podcasts,
   Videos, Other FPGA Hardware Links, Other Interesting Stuff, Chat and support).
2. Each forge repo link was reduced to `owner/repo` and compared with the slug column of
   `.claude/memory/sources.tsv` (437 lines, `owner__repo` lowercase).
3. For every repo not already pinned: repo metadata from the forge API (Gitee `api/v5/repos/<o>/<r>`,
   GitHub `api.github.com/repos/<o>/<r>`, GitLab `api/v4/projects/<o>%2F<r>`), recursive file tree
   (`git/trees/<branch>?recursive=1`, GitLab `repository/tree?recursive=true`), and grep of paths for
   `ulx3s` and `.lpf` (evidence levels of skill `github-survey`: A = ULX3S `.lpf` present).
   For forks, `compare/upstream...fork` gives own commits.
4. `lawrie/ulx3s_retro` turned out to be a one-file README index; its 62 github.com links were also diffed
   against `sources.tsv`.
5. Clone test: `git clone --depth 1 https://gitee.com/ynxing/learn-fpga.git` into the scratchpad.
   First attempt failed after 23 s (`curl 56 GnuTLS recv error (-110)` / `early EOF`); second attempt,
   same command, succeeded (158 MB, HEAD `494945ef` 2021-01-05). Clone deleted afterwards.
   Conclusion: cloning from Gitee works, but the connection is flaky; retry on failure.

## The "Gitee examples" section

It contains exactly **one** link: https://gitee.com/ynxing/learn-fpga/blob/master/FemtoRV/TUTORIALS/ULX3S.md

## Table (Gitee + other forge repos after "Projects and examples" not already in sources.tsv)

| Repo URL | What it is | HDL | ULX3S evidence | License | Last update | Duplicate of | Recommendation |
|---|---|---|---|---|---|---|---|
| https://gitee.com/ynxing/learn-fpga | Gitee import (not flagged fork/mirror) of BrunoLevy/learn-fpga, frozen at upstream commit `494945ef` 2021-01-05 (author Bruno Levy, message "Merge branch 'master' of https://github.com/BrunoLevy/learn-fpga"); FemtoRV + Basic tutorials | Verilog (58 .v), C/asm firmware | A: `FemtoRV/BOARDS/ulx3s.lpf`, `Basic/ULX3S_hdmi/ulx3s.lpf`, `FemtoRV/TUTORIALS/ULX3S.md` | BSD-3-Clause | 2021-01-05 (pushed; single upload, 0 stars) | brunolevy__learn-fpga (pinned 2025-11-18, same `ULX3S.md` present) | **skip** — stale 2021 snapshot of a repo already cloned |
| https://github.com/kbeckmann/tt08-flame | TT08 demoscene submission (flame effect), with a ULX3S HDMI port | Verilog/SV (9 .v) | A: `ulx3s/ulx3s_v20.lpf`, `ulx3s/top.v`, `ulx3s/hdmi.v`, `ulx3s/ecp5pll.sv`, Makefile | Apache-2.0 | 2024-09-14 | — | **clone** |
| https://github.com/htfab/asicle2 | Asicle 2: Wordle clone for Tiny Tapeout, FPGA ports | SystemVerilog (23 .sv) | A: `fpga/ulx3s/ulx3s_custom.lpf`, `fpga_top.sv`, apio.ini, build.sh (also basys3, pico-ice) | Apache-2.0 | 2025-10-30 | — | **clone** |
| https://gitlab.com/TheZoq2/tinytapeout02 | TT02 submission in Spade (FPGA-like cell/routing fabric, config chain) with a ULX3S build | Spade + Verilog/SV (`src/*.spade`, `src/top.sv`) | A: `ulx3s_v20.lpf` at root, swim.toml | none declared (GitLab API: null) | 2024-02-13 (`b66c40d4`) | — | **clone** (only Spade-language ULX3S design found so far; no license — note it) |
| https://github.com/ulx3s/tt-support-tools (branch `experimental`, = default) | Fork of TinyTapeout/tt-support-tools with ULX3S/ULX4M FPGA harness for TT projects | Verilog top + Python tools | A: `fpga/ulx3s/tt_fpga_top_ulx3s.v`, `ulx3s_v20.lpf`, `ulx3s_v316.lpf`, `ulx3s_v314.lpf`, `ulx3s_v17patch.lpf` | Apache-2.0 | 2026-09-04 | fork of TinyTapeout/tt-support-tools (not in sources.tsv) | **clone** — the TT-on-ULX3S harness that the other TT repos use |
| https://github.com/rxrbln/picorv32 | Fork of YosysHQ/picorv32: 131 own commits (PicoSoC + VGA text mode, palette, cursor) | Verilog | A: `picosoc/ulx3s.lpf`, `picosoc/ulx3s.v` (absent from pinned yosyshq__picorv32) | ISC inherited (GitHub API: none detected) | 2021-05-12 | fork of yosyshq__picorv32, but ULX3S port is own work (level D) | **clone** |
| https://github.com/ulx3s/ttsky-verilog-template (branch `ulx3s`) | Fork of TinyTapeout ttsky template; branch adds a `fpga-ulx3s` CI job | Verilog (2 .v, template) | B: only `.github/workflows/fpga.yaml` uses `tt-gds-action/fpga/ulx3s` with `tt/fpga/ulx3s/ulx3s_v20.lpf` (fetched from tt-support-tools) | Apache-2.0 | 2026-04-29 | fork of TinyTapeout/ttsky-verilog-template | skip (template, no own gateware; needs non-default branch, `clone.sh` has no branch option) |
| https://github.com/ulx3s/tt-gds-action (branch `experimental`) | Fork of TinyTapeout/tt-gds-action: GitHub Action YAML (`fpga/ulx3s/action.yml`) | none (YAML only) | CI action for ULX3S | Apache-2.0 | 2026-09-08 | fork of TinyTapeout/tt-gds-action | skip (no HDL) |
| https://github.com/lawrie/ulx3s_retro | Single README: essay + index of retro-computing cores on ULX3S | none | README only | none | 2022-03-03 | — | skip; index diffed: all ULX3S repos it links already cloned |
| https://github.com/ulx3s/ulx3s-toolchain | Toolchain installer scripts | none | scripts | MIT | 2020-10-19 | — | skip (tooling) |
| https://github.com/kost/homebrew-ulx3s | Homebrew tap for the toolchain | none | — | MIT | 2020-10-14 | — | skip (tooling) |
| https://github.com/xobs/circuitpython (branch `fomu`) | CircuitPython for Fomu | none | not ULX3S | MIT | 2020-03-24 | — | skip |
| https://github.com/lawrie/ulx3s_bit_streams (via ulx3s_retro) | Prebuilt .bit files for lawrie cores | none (74 .bit) | bitstreams only | none | 2023-04-09 | — | skip (binaries) |
| https://github.com/lawrie/atari_2600 (via ulx3s_retro) | TinyFPGA BX Atari 2600 (.pcf) | Verilog | none (iCE40) | LGPL-3.0 | 2018-12-13 | ULX3S port already pinned as lawrie__ulx3s_atari_2600 | skip |

Already in `sources.tsv` (no action): brunolevy__learn-fpga, sylefeb__silice, gojimmypi__ttsky-uart-fsm-trng-lab,
mole99__tt05-one-sprite-pony, ulx3s__hazard3-doom, cbalint13__e-verest, evgenymuryshkin__quokkaevaluation,
glasgowembedded__glasgow, icebreaker-fpga__icebreaker-workshop, emard__ulx3s, emard__ulx3s-bin, yosyshq__picorv32.
Non-gateware tool/framework links skipped: YosysHQ/nextpnr, prjtrellis, openFPGALoader, f32c/tools, FPGAwars/apio,
FPGAwars/icestudio, enjoy-digital/litex, litex-hub/linux-on-litex-vexriscv, gregdavill/OrangeCrab (hardware),
icebreaker-fpga/icebreaker (hardware), RadionaOrg/ulx3s-links, ulx3s/ulx3s.github.io, TinyTapeout PR/issue links.
Non-forge links (blogs, articles, videos, spade-lang.org showcase, tinytapeout.com/chips/tt08/tt_um_silice) not harvested.
ulx3s_retro links not in sources.tsv are all tools/frameworks (amaranth, ghdl, SpinalHDL, verilator, iverilog, yosys…),
MiSTer/MiST cores for other boards, or dan-rodrigues/super-miyamoto-sprint (C game software for icestation-32, no HDL).

## Findings

- The "Gitee examples" section holds a single link, and it is not a separate project: `ynxing/learn-fpga` is a
  2021-01-05 snapshot of BrunoLevy/learn-fpga (same author in commits, same `FemtoRV/TUTORIALS/ULX3S.md`),
  which is already pinned at a 2025-11-18 commit. Nothing to clone from Gitee.
- Cloning from Gitee works with plain `git clone --depth 1 https://gitee.com/<o>/<r>.git` (no auth), but the
  first attempt hit a TLS disconnect; `clone.sh` would need a retry for Gitee URLs. The Gitee v5 API works
  unauthenticated for repo metadata, trees and commits.
- The sections after "Projects and examples" (mainly "Tiny Tapeout Projects using the ULX3S" and "Tiny Tapeout")
  yield 5 ULX3S gateware repos not yet collected: kbeckmann/tt08-flame, htfab/asicle2, gitlab TheZoq2/tinytapeout02,
  ulx3s/tt-support-tools, and (from "Other Interesting Stuff") the rxrbln/picorv32 fork with a PicoSoC+VGA ULX3S port.
- `gitlab.com/TheZoq2/tinytapeout02` has no license file; clone for review only.
- `ulx3s/ttsky-verilog-template` needs branch `ulx3s`, which `clone.sh` cannot select; it has no own gateware anyway.
{% endraw %}
