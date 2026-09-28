# ulx3s-klod

A knowledge base of **open gateware for the [ULX3S](https://github.com/emard/ulx3s) FPGA board**
(Radiona, Lattice ECP5 LFE5U-12F/25F/45F/85F) and, for reuse, other small Lattice boards
(ECP5, iCE40 UP5K and iCE40 HX8K/HX4K). It records which projects exist, what their gateware does, which FPGA
and toolchain they target, their license, whether they have testbenches, and which blocks can be
lifted into a new design. It is maintained with [Claude Code](https://claude.com/claude-code).

Use it to **find prior art before writing a core**: a DVI encoder, a USB device, an SDRAM or
HyperRAM controller, a RISC-V SoC, an ESP32 on-screen display, a retro computer…

The repo also holds Claude's working memory (`CLAUDE.md`, `.claude/`), so anyone who clones it
and runs `claude` here picks up exactly where the work stopped.

## Start here

| If you want to… | Open |
|---|---|
| Find the best existing core for a function (PLL, DVI, USB, SDRAM, HyperRAM, CPU, Linux…) | [`.claude/memory/reusable-cores.md`](.claude/memory/reusable-cores.md) |
| Browse every catalogued repo (FPGA, toolchain, HDL, license, functions, tests, reuse) | [`docs/catalogue.md`](docs/catalogue.md) |
| Learn the ULX3S hardware: pins, signal names, constraint files, build and load, pitfalls | [`docs/board-reference.md`](docs/board-reference.md) |
| Read a full review of a project | [`docs/projects/`](docs/projects/) — [emard/ulx3s](docs/projects/emard__ulx3s.md), [ulx3s-bin](docs/projects/emard__ulx3s-bin.md), [openFPGALoader](docs/projects/trabucayre__openfpgaloader.md) |
| See how the collection was found, and what is not cloned yet | the surveys below |

## The catalogue

[`docs/catalogue.md`](docs/catalogue.md) is generated from
[`.claude/memory/catalogue.tsv`](.claude/memory/catalogue.tsv) (one row per repo) by
`.claude/skills/review-gateware-project/gen_catalogue.py`. It currently covers **358 repos**:

- **291 ULX3S / ULX4M** repos: the ulx3s.github.io project list plus a GitHub-wide search (and RISCBoy, found via the HX survey);
- **17 on other ECP5 boards**: TrellisBoard, OrangeCrab, iCESugar-Pro, Hackaday 2019 badge, Colorlight,
  ECPIX-5, Versa ECP5-5G, IcePi Zero, LUNA, ECP5 Mini, Pergola, GreyBadge 2025, Machdyne…;
- **50 non-ECP5** repos: **iCE40 UP5K** (iCEBreaker, UPduino, iCESugar, Fomu, MCH2022 badge, reDIP-SID,
  pico-ice…), **iCE40 HX8K/HX4K** (PicoRV32, iceboy, BlackIce, IcoBoard, Alhambra II, un0rick…) and ZipCPU sdspi, found via [awesome-latticeFPGAs](https://github.com/kelu124/awesome-latticeFPGAs) and GitHub.
  Any row whose FPGA is not an ECP5 says **`NOT ECP5`** in the FPGA column: iCE40 cores use `SB_*`
  primitives and need porting.

For each repo it records the FPGA size, toolchain (open yosys/nextpnr, Lattice Diamond, or both),
HDL, **license** (`none found` = all rights reserved: ask before reusing), functions, reusable
blocks, activity, preferred fork, a heuristic **testbench** scan, and which **Makefile targets
actually run a testbench** (`make_tests`). Nothing was built or simulated: facts come from reading
the sources at a pinned commit.

## Surveys (candidates, cloned or not)

| File | What |
|---|---|
| [`docs/github-survey.md`](docs/github-survey.md) | GitHub-wide search for ULX3S repos (groups A–F). A, B, D and the ULX4M part of E are cloned; C (multi-board) is not. F = ULX5M (GateMate, excluded) |
| [`docs/ecp5-boards-survey.md`](docs/ecp5-boards-survey.md) | Gateware for other ECP5 boards (OrangeCrab, LUNA, iCESugar-Pro, HAD2019, Colorlight, ButterStick, ECPIX-5…), 114 repos |
| [`docs/lattice-boards-survey.md`](docs/lattice-boards-survey.md) | Gateware for the UP5K and ECP5 boards of awesome-latticeFPGAs (20 recommended, all catalogued) |
| [`docs/hx-boards-survey.md`](docs/hx-boards-survey.md) | Gateware for the iCE40 HX8K/HX4K boards of awesome-latticeFPGAs (20 recommended; 19 catalogued, iceZ0mb1e already present as a submodule) |

## Upstream sources

Upstream repos are cloned into `original_sources/<owner>__<repo>` (gitignored, read-only, always
shallow). They are pinned in [`.claude/memory/sources.tsv`](.claude/memory/sources.tsv); gateware
submodules that were fetched are pinned in
[`.claude/memory/submodules.tsv`](.claude/memory/submodules.tsv). Re-create everything with:

```bash
.claude/skills/clone-original-source/clone.sh --restore
.claude/skills/clone-original-source/prune.py --apply --all   # then drop non-gateware files (see below)
```

To save disk, the local clones are **pruned** of files that are not gateware: prebuilt tools, bitstreams,
build outputs, PCB/3D files, datasheets, large images and archives (`prune.py`, dry run without
`--apply`; per-repo folder rules in `prune.tsv`). HDL, constraints, Makefiles, testbenches, ROM files,
READMEs and licenses are always kept. The deletions are never committed. The first run (2026-09-28)
freed 5 GB.

## Main files

| Path | Role |
|---|---|
| [`CLAUDE.md`](CLAUDE.md) | Rules and resume protocol for Claude sessions |
| [`.claude/memory/MEMORY.md`](.claude/memory/MEMORY.md) | Index of the memory files (board facts, toolchain, decisions, lists) |
| [`.claude/memory/board-hardware.md`](.claude/memory/board-hardware.md), [`board-revisions.md`](.claude/memory/board-revisions.md), [`toolchain-and-programming.md`](.claude/memory/toolchain-and-programming.md) | Distilled ULX3S hardware, revision and toolchain knowledge |
| [`.claude/memory/projects.md`](.claude/memory/projects.md) | Project registry: status and the queue of candidates still to review |
| [`.claude/memory/source-lists.md`](.claude/memory/source-lists.md) | Where each batch of repos came from, and when |
| [`.claude/skills/`](.claude/skills/) | Repeatable workflows: GitHub survey, clone + prune, review/catalogue, document, commit, TODO/DONE |
| [`.claude/TODO.md`](.claude/TODO.md), [`DONE.md`](.claude/DONE.md), [`COMMIT_LOG.md`](.claude/COMMIT_LOG.md) | Open work, finished work, and the why of each commit |

## Working in this repo

1. Clone it, run `claude`, and it follows the resume protocol in `CLAUDE.md` (read memory, TODO, last commits;
   restore `original_sources/` if empty).
2. To add a project, ask for a review (skill `review-gateware-project`): it clones, catalogues, documents and
   commits with a `COMMIT_LOG.md` entry.
3. Never edit files under `original_sources/`, and never edit `docs/catalogue.md` by hand (regenerate it).
