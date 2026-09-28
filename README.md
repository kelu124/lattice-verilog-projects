# ulx3s-klod

A knowledge base of **open gateware for the [ULX3S](https://github.com/emard/ulx3s) FPGA board**
(Radiona, Lattice ECP5 LFE5U-12F/25F/45F/85F) and, for reuse, other small Lattice boards
(ECP5, iCE40 UP5K and iCE40 HX8K/HX4K). It records which projects exist, what their gateware does, which FPGA
and toolchain they target, their license, whether they have testbenches, and which blocks can be
lifted into a new design. It is maintained with [Claude Code](https://claude.com/claude-code).

Use it to **find prior art before writing a core**: a DVI encoder, a USB device, an SDRAM or
HyperRAM controller, a RISC-V SoC, an ESP32 on-screen display, a retro computer… The public site presents
**153 reusable cores in 33 functions**, each with links to the original files and the projects that use it.

The repo also holds Claude's working memory (`CLAUDE.md`, `.claude/`), so anyone who clones it
and runs `claude` here picks up exactly where the work stopped.

## Start here

**Website:** <https://kelu124.github.io/ulx3s-klod/> (GitHub Pages, generated from [`data/`](data/) into [`docs/`](docs/);
Pages must be enabled once in the repo settings: source `main`, folder `/docs`). The links below open the
same pages as markdown on GitHub.

| If you want to… | Open |
|---|---|
| Find the best existing core for a function (HDMI, VGA, SDRAM, SD, USB, UART, SPI, I2C, ADC, DAC, audio, radio, CPUs…), with links to the original files and the projects that use it | [Cores by function](docs/functions/index.md) (data: [`data/cores.json`](data/cores.json), [`data/core_usage.json`](data/core_usage.json)) |
| Learn a board: FPGA, constraint files, cores seen on it, projects | [Boards](docs/boards/index.md): ULX3S, ULX4M, OrangeCrab, Colorlight, IcePi Zero, iCESugar-Pro; iCEBreaker, UPduino, iCESugar, Fomu, pico-ice; HX8K breakout, BlackIce, iceFUN, Olimex HX8K-EVB, IcoBoard |
| Learn the ULX3S hardware: pins, signal names, constraint files, pitfalls | [ULX3S board page](docs/boards/ulx3s.md) |
| Build and load a bitstream, use DFU, port an iCE40 core to ECP5 | [Guides](docs/guides/index.md): [toolchain](docs/guides/toolchain.md), [USB DFU](docs/guides/DFUs.md), [porting iCE40 → ECP5](docs/guides/porting-ice40-to-ecp5.md) |
| Read an in-depth review with per-block reuse notes | [Project reviews](docs/projects/index.md) (18 repos) |
| Browse every catalogued repo, or every LPF pin map | [Full catalogue](docs/methodology/catalogue.md), [LPF catalogue](docs/methodology/lpf-catalogue.md) (data: [`data/catalogue.json`](data/catalogue.json), [`data/lpfs.json`](data/lpfs.json)) |
| See how the collection was found | [Methodology](docs/methodology/index.md) and the surveys below |

## The catalogue

The [full catalogue](docs/methodology/catalogue.md) is generated from
[`data/catalogue.json`](data/catalogue.json) (one object per repo) by
`.claude/skills/review-gateware-project/gen_catalogue.py`. It currently covers **376 repos**:

- **292 ULX3S / ULX4M** repos: the ulx3s.github.io project list plus a GitHub-wide search (and RISCBoy, found via the HX survey, and the US2 DFU bootloader source);
- **26 on other ECP5 boards**: TrellisBoard, OrangeCrab, ECP5-EVN, Colorlight i5/i9/5A-75B, iCESugar-Pro, Hackaday 2019 badge,
  ECPIX-5, Versa ECP5-5G, IcePi Zero, LUNA, ECP5 Mini, Pergola, GreyBadge 2025, Machdyne…;
- **58 non-ECP5** repos: **iCE40 UP5K** (iCEBreaker, UPduino, iCESugar, Fomu, MCH2022 badge, reDIP-SID,
  pico-ice…), **iCE40 HX8K/HX4K** (PicoRV32, iceboy, Glasgow, BlackIce, IcoBoard, Alhambra II, BeagleWire, un0rick…) and ZipCPU sdspi, found via [awesome-latticeFPGAs](https://github.com/kelu124/awesome-latticeFPGAs) and GitHub.
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
| [`github-survey`](docs/methodology/github-survey.md) | GitHub-wide search for ULX3S repos (groups A–F). A, B, D and the ULX4M part of E are cloned; C (multi-board) is not. F = ULX5M (GateMate, excluded) |
| [`ecp5-boards-survey`](docs/methodology/ecp5-boards-survey.md) | Gateware for other ECP5 boards (OrangeCrab, LUNA, iCESugar-Pro, HAD2019, Colorlight, ButterStick, ECPIX-5…), 114 repos, all 24 recommended catalogued |
| [`lattice-boards-survey`](docs/methodology/lattice-boards-survey.md) | Gateware for the UP5K and ECP5 boards of awesome-latticeFPGAs (20 recommended, all catalogued) |
| [`hx-boards-survey`](docs/methodology/hx-boards-survey.md) | Gateware for the iCE40 HX8K/HX4K boards of awesome-latticeFPGAs (20 recommended + 8 honourable mentions, all catalogued; iceZ0mb1e is a submodule) |

## Data and the GitHub Pages site

Everything gathered is stored as JSON in [`data/`](data/); [`docs/`](docs/) is **generated** from it and published
with GitHub Pages (just-the-docs theme; Settings → Pages → source `main`, folder `/docs`; config in
`docs/_config.yml`). Never edit `docs/` by hand.

| Data | What | Site |
|---|---|---|
| `data/functions.json` | 33 functions (ADC, SPI, DAC, VGA, HDMI…) | [Cores by function](docs/functions/index.md) |
| `data/cores.json` | 153 reusable cores: repo, files, top module, license, FPGA/primitives, tests, ULX3S notes | function pages |
| `data/core_usage.json` | which repos copy or instantiate each core (scan) | "Used by" lists |
| `data/boards.json` | 16 boards in 3 families (ECP5, UP5K, HX) | [Boards](docs/boards/index.md) |
| `data/pages/*.json`, `data/projects/*.json` | guides, surveys, methodology, home intro, 18 reviews | Guides, Project reviews, Methodology |
| `data/catalogue.json`, `data/lpfs.json` | every cloned repo, every LPF | Methodology data views |

```bash
make check   # validate data/ (core files exist in the clones, ids, pins vs rows)
make usage   # rescan which repos use each core -> data/core_usage.json
make lpfs    # rescan every *.lpf in original_sources/ -> data/lpfs.json
make docs    # render the whole site into docs/
```

Scripts: `.claude/skills/documentation/{gen_site.py,mdjson.py,md2json.py,check_data.py}`,
`.claude/skills/review-gateware-project/{gen_catalogue.py,scan_core_usage.py,scan_lpfs.py,gen_lpf_catalogue.py}`.

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
| [`.claude/memory/reusable-cores.md`](.claude/memory/reusable-cores.md) | Quick picks per function and cross-project facts (the data is `data/cores.json`) |
| [`.claude/memory/source-lists.md`](.claude/memory/source-lists.md) | Where each batch of repos came from, and when |
| [`data/`](data/) | **All gathered data as JSON** (source of truth): `functions.json`, `cores.json`, `core_usage.json`, `boards.json`, `catalogue.json`, `lpfs.json`, `pages/*.json` (guides, surveys, methodology, home), `projects/*.json` (reviews) |
| [`docs/`](docs/) | **Generated** GitHub Pages site (just-the-docs); never edit by hand |
| [`Makefile`](Makefile) | `make check`, `make usage`, `make lpfs`, `make docs` |
| [`.claude/skills/`](.claude/skills/) | Repeatable workflows: GitHub survey, clone + prune, review/catalogue, document, commit, TODO/DONE |
| [`.claude/TODO.md`](.claude/TODO.md), [`DONE.md`](.claude/DONE.md), [`COMMIT_LOG.md`](.claude/COMMIT_LOG.md) | Open work, finished work, and the why of each commit |

## Working in this repo

1. Clone it, run `claude`, and it follows the resume protocol in `CLAUDE.md` (read memory, TODO, last commits;
   restore `original_sources/` if empty).
2. To add a project, ask for a review (skill `review-gateware-project`): it clones, prunes, catalogues
   (`gen_catalogue.py --merge`), adds any better core to `data/cores.json`, documents, runs
   `make check usage docs`, and commits with a `COMMIT_LOG.md` entry.
3. Never edit files under `original_sources/`, and never edit anything under `docs/` by hand (edit `data/`, then `make docs`).
