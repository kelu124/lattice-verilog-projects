---
title: "Methodology"
nav_order: 6
has_children: true
permalink: "/methodology/"
---
<!-- Generated from data/pages/methodology.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# Methodology

How the collection was built, and where the raw material lives in the [GitHub repository](https://github.com/kelu124/lattice-verilog-projects).

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
| Catalogue of every cloned repo | [data/catalogue.json](https://github.com/kelu124/lattice-verilog-projects/blob/main/data/catalogue.json) |
| Reusable cores and their usage | [data/cores.json](https://github.com/kelu124/lattice-verilog-projects/blob/main/data/cores.json), [data/core_usage.json](https://github.com/kelu124/lattice-verilog-projects/blob/main/data/core_usage.json), [data/functions.json](https://github.com/kelu124/lattice-verilog-projects/blob/main/data/functions.json) |
| Boards | [data/boards.json](https://github.com/kelu124/lattice-verilog-projects/blob/main/data/boards.json) |
| Every LPF in the clones | [data/lpfs.json](https://github.com/kelu124/lattice-verilog-projects/blob/main/data/lpfs.json) |
| Page sources (guides, surveys, reviews) | [data/pages/](https://github.com/kelu124/lattice-verilog-projects/tree/main/data/pages), [data/projects/](https://github.com/kelu124/lattice-verilog-projects/tree/main/data/projects) |
| Pinned upstream commits | [.claude/memory/sources.tsv](https://github.com/kelu124/lattice-verilog-projects/blob/main/.claude/memory/sources.tsv), [submodules.tsv](https://github.com/kelu124/lattice-verilog-projects/blob/main/.claude/memory/submodules.tsv), [history.tsv](https://github.com/kelu124/lattice-verilog-projects/blob/main/.claude/memory/history.tsv) |
| Distilled knowledge (board, revisions, toolchain, decisions) | [.claude/memory/](https://github.com/kelu124/lattice-verilog-projects/blob/main/.claude/memory/MEMORY.md) |
| Workflows and generator scripts | [.claude/skills/](https://github.com/kelu124/lattice-verilog-projects/tree/main/.claude/skills) |
| Change log (what and why) | [.claude/COMMIT_LOG.md](https://github.com/kelu124/lattice-verilog-projects/blob/main/.claude/COMMIT_LOG.md) |

## Surveys

- [TinyFPGA EX, ECPIX-5 and Cynthion gateware survey](boards3-survey.md): TinyFPGA EX (announced, never shipped), LambdaConcept ECPIX-5 and Great Scott Gadgets Cynthion: board facts and gateware (2026-09-28).
- [ECP5 (non-ULX3S) gateware survey on GitHub](ecp5-boards-survey.md): Gateware for other ECP5 boards (OrangeCrab, LUNA, iCESugar-Pro, HAD2019, Colorlight, ButterStick, ECPIX-5…): 114 repos, 24 recommended.
- [FFT gateware on Lattice FPGAs](fft-survey.md): FFT gateware on Lattice FPGAs (2026-09-28): FFT cores already in the collection and 14 new iCE40/ECP5 designs (sliding DFT, radix-2 pipelines, Goertzel, spectrum displays).
- [Gitee examples from ulx3s.github.io](gitee-survey.md): Gitee examples and remaining sections of ulx3s.github.io (2026-09-28): the single Gitee link is a stale copy of learn-fpga; 5 new ULX3S repos found elsewhere on the page.
- [GitHub survey of ULX3S repositories (2026-09-27)](github-survey.md): GitHub-wide search for ULX3S gateware (2026-09-27): ~297 candidates in groups A–F with evidence and clone status.
- [iCE40 HX4K / HX8K gateware survey (from awesome-latticeFPGAs)](hx-boards-survey.md): Gateware for the iCE40 HX8K/HX4K boards of awesome-latticeFPGAs: 20 recommended plus 8 honourable mentions.
- [UP5K and ECP5 boards from awesome-latticeFPGAs: gateware survey](lattice-boards-survey.md): Gateware for the iCE40 UP5K and ECP5 boards of awesome-latticeFPGAs: 20 recommended, all catalogued.
- [RF and signal-processing gateware on Lattice FPGAs](rf-dsp-survey.md): RF and signal-processing gateware on Lattice FPGAs (2026-09-28): SDR receivers/transmitters, lock-in amplifiers, VNA, WSPR, LoRa; 15 repos cloned.
- [ECP5-5G / ECP5UM SERDES survey: PCIe, SATA, NVMe/M.2 and other links](serdes-survey.md): ECP5-5G (LFE5UM/LFE5UM5G) SERDES survey: PCIe, SATA, NVMe/M.2, SGMII, USB3 on open gateware; no open design drives an M.2 SSD, LiteSATA drives a SATA SSD on ECPIX-5.

## Data views

- [Full catalogue](catalogue.md): every cloned repo (from `data/catalogue.json`)
- [LPF catalogue](lpf-catalogue.md): every ECP5 constraint file (from `data/lpfs.json`)
{% endraw %}
