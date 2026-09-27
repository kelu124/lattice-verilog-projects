# ulx3s-klod

A knowledge base of what people have built for the
[ULX3S](https://github.com/emard/ulx3s) FPGA board (Lattice ECP5), maintained with
Claude Code. It helps people start new gateware on top of existing work.

The repo also holds Claude's working memory (`CLAUDE.md`, `.claude/`), so anyone who
clones it and runs `claude` here picks up where the work stopped.

## Documentation
- [Board reference for gateware developers](docs/board-reference.md): peripherals, signal names, constraint files, build/load, pitfalls
- Reviewed projects:
  - [emard/ulx3s: board hardware + manual](docs/projects/emard__ulx3s.md)
  - [emard/ulx3s-bin: prebuilt bitstreams, self-test, bootloaders](docs/projects/emard__ulx3s-bin.md)
  - [openFPGALoader: programmer](docs/projects/trabucayre__openfpgaloader.md)

## Catalogue
[docs/catalogue.md](docs/catalogue.md): 71 ULX3S repos with FPGA size, toolchain (open or Diamond),
HDL, license, activity, preferred fork, functions and reusable cores. Start there to find prior art.

## Wider survey
[docs/github-survey.md](docs/github-survey.md): about 300 more ULX3S repos found on GitHub (155 verified),
not cloned or catalogued yet.

## Project registry
[`.claude/memory/projects.md`](.claude/memory/projects.md) lists every known ULX3S project with its
functions, toolchain, target and last update, plus the queue of projects still to review.

## Working in this repo
- Upstream sources are cloned (not committed) into `original_sources/`. Re-create them with
  `.claude/skills/clone-original-source/clone.sh --restore`.
- Progress: [TODO.md](.claude/TODO.md), [DONE.md](.claude/DONE.md), [COMMIT_LOG.md](.claude/COMMIT_LOG.md).
- Rules and workflows: [CLAUDE.md](CLAUDE.md) and `.claude/skills/`.
