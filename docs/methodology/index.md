---
title: "Methodology"
nav_order: 6
has_children: true
permalink: "/methodology/"
---
<!-- Generated from data/pages/methodology.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# Methodology

How the collection was built, and where the raw material lives in the [GitHub repository](https://github.com/kelu124/ulx3s-klod).

## How the data was gathered

1. **Find** candidate repos: the ulx3s.github.io project list, GitHub-wide searches, and the board lists of awesome-latticeFPGAs (see the surveys below). Each search is recorded with its date and queries.
2. **Clone** each chosen repo shallowly (`--depth 1`) and **pin** its commit in `sources.tsv`. Gateware submodules are fetched only when the repo is built around them. Non-gateware files (prebuilt bitstreams, PCB files, datasheets) are deleted locally to save disk; nothing is ever committed to the clones.
3. **Catalogue** each repo by reading its Makefiles, constraint files, READMEs, license files and sources: FPGA and size, toolchain, HDL, license, functions, reusable blocks, tests. Facts cite a path at the pinned commit; anything not verified is written `unknown`. Nothing is built or simulated.
4. **Scan** the clones with scripts: every LPF (board, revision, peripherals), testbench heuristics, Makefile test targets, and which repos copy or instantiate each reusable core.
5. **Review** the repos with the most reusable gateware in depth (per-block module, ports, primitives, license, what to change for ULX3S).
6. **Publish**: all data is JSON in `data/`; this site is generated from it (`make docs`). Pages are never edited by hand.

## Raw material on GitHub

| What | Where |
|---|---|
| Catalogue of every cloned repo | [data/catalogue.json](https://github.com/kelu124/ulx3s-klod/blob/main/data/catalogue.json) |
| Reusable cores and their usage | [data/cores.json](https://github.com/kelu124/ulx3s-klod/blob/main/data/cores.json), [data/core_usage.json](https://github.com/kelu124/ulx3s-klod/blob/main/data/core_usage.json), [data/functions.json](https://github.com/kelu124/ulx3s-klod/blob/main/data/functions.json) |
| Boards | [data/boards.json](https://github.com/kelu124/ulx3s-klod/blob/main/data/boards.json) |
| Every LPF in the clones | [data/lpfs.json](https://github.com/kelu124/ulx3s-klod/blob/main/data/lpfs.json) |
| Page sources (guides, surveys, reviews) | [data/pages/](https://github.com/kelu124/ulx3s-klod/tree/main/data/pages), [data/projects/](https://github.com/kelu124/ulx3s-klod/tree/main/data/projects) |
| Pinned upstream commits | [.claude/memory/sources.tsv](https://github.com/kelu124/ulx3s-klod/blob/main/.claude/memory/sources.tsv), [submodules.tsv](https://github.com/kelu124/ulx3s-klod/blob/main/.claude/memory/submodules.tsv), [history.tsv](https://github.com/kelu124/ulx3s-klod/blob/main/.claude/memory/history.tsv) |
| Distilled knowledge (board, revisions, toolchain, decisions) | [.claude/memory/](https://github.com/kelu124/ulx3s-klod/blob/main/.claude/memory/MEMORY.md) |
| Workflows and generator scripts | [.claude/skills/](https://github.com/kelu124/ulx3s-klod/tree/main/.claude/skills) |
| Change log (what and why) | [.claude/COMMIT_LOG.md](https://github.com/kelu124/ulx3s-klod/blob/main/.claude/COMMIT_LOG.md) |

## Surveys

- [ECP5 (non-ULX3S) gateware survey on GitHub](ecp5-boards-survey.md): Gateware for other ECP5 boards (OrangeCrab, LUNA, iCESugar-Pro, HAD2019, Colorlight, ButterStick, ECPIX-5…): 114 repos, 24 recommended.
- [GitHub survey of ULX3S repositories (2026-09-27)](github-survey.md): GitHub-wide search for ULX3S gateware (2026-09-27): ~297 candidates in groups A–F with evidence and clone status.
- [iCE40 HX4K / HX8K gateware survey (from awesome-latticeFPGAs)](hx-boards-survey.md): Gateware for the iCE40 HX8K/HX4K boards of awesome-latticeFPGAs: 20 recommended plus 8 honourable mentions.
- [UP5K and ECP5 boards from awesome-latticeFPGAs: gateware survey](lattice-boards-survey.md): Gateware for the iCE40 UP5K and ECP5 boards of awesome-latticeFPGAs: 20 recommended, all catalogued.

## Data views

- [Full catalogue](catalogue.md): every cloned repo (from `data/catalogue.json`)
- [LPF catalogue](lpf-catalogue.md): every ECP5 constraint file (from `data/lpfs.json`)
{% endraw %}
