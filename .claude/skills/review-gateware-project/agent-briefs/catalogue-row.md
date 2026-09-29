# Catalogue-row brief for agents (lattice-verilog-projects)

Give this file to a cataloguing agent together with its slugs and an output path in the scratchpad.
The rows are merged with `gen_catalogue.py --merge ROWS.tsv` (see SKILL.md, "Batch cataloguing with agents").

Repo root: the repository root (the directory containing CLAUDE.md; run agents from there). Clones are in `original_sources/<slug>/` (shallow, READ-ONLY: never edit,
build, run make, or git-commit inside them; do not run simulators). Nothing is executed except read-only shell
commands (ls, find, grep, cat, git log -1) and the two scanners below.

For each slug you are given, write ONE catalogue row: 15 TAB-separated columns, no tabs or newlines inside a field,
in this order (field order of `data/catalogue.json` `fields`):

slug  kind  name  fork_of  ulx3s_path  fpga  toolchain  hdl  license  board_rev  functions  reuse  notes  tests  make_tests

- **slug**: as given.
- **kind**: one of gateware | examples | education | mixed | toolchain | pcb | software | bootloader.
- **name**: one line: project name + what it does.
- **fork_of**: upstream it was forked from, or `none` (say what it derives from if vendored).
- **ulx3s_path**: these repos are mostly NOT ULX3S. Give the main top/build paths (Makefile, top .v, .pcf) for the
  board it targets, e.g. `hdl/top.v, hx8k.pcf, Makefile`; if it has ULX3S/ECP5 support, say where.
- **fpga**: MUST start with the family and `(NOT ECP5)` when not ECP5, e.g. `iCE40 HX8K (NOT ECP5) - CT256 (--hx8k --package ct256, Makefile)`
  or `iCE40 HX4K (NOT ECP5) - TQ144 (built as --hx8k)`. Cite where you saw it. List every family targeted
  (e.g. also ECP5 25F or UP5K). If only a proprietary flow: say so.
- **toolchain**: `open (yosys+nextpnr-ice40+icepack)`, `open (yosys+arachne-pnr+icepack)`, `apio`, `iCEcube2`,
  `diamond`, `both`… with details.
- **hdl**: languages with approx file counts (`find -name '*.v' | wc -l` etc.).
- **license**: SPDX id from LICENSE/COPYING at any depth, README, or file headers; `none found` if absent.
- **board_rev**: target board(s) (e.g. `iCE40-HX8K Breakout (not ULX3S)`, `BlackIce II (not ULX3S)`).
- **functions**: comma-separated tags. Reuse existing tags when they fit: board-hw soc-cpu uart constraints examples
  video-dvi video-vga video-composite retro-computer retro-console retro-arcade sdram sram flash-spi sdcard ps2
  audio-dac audio-i2s synth-audio oled-lcd jtag usb-host usb-device bootloader toolchain dsp-sdr linux gpu
  programmer-tool camera adc ml-accelerator logic-analyzer led-matrix ethernet education hdl-language spi i2c gpio
  bus-fabric wishbone-bus dma debug-bridge ide floppy timer. New tag → prefix `NEW:` (e.g. `NEW:forth`).
- **reuse**: the reusable blocks: path + what + portability note (iCE40 designs use SB_PLL40/SB_IO/SB_RAM40_4K/
  SB_SPRAM256KA and must be ported for ECP5: say which primitives are used).
- **notes**: activity (last commit date from `git -C original_sources/<slug> log -1 --format=%cs`), clock
  frequency of the board, caveats, submodules (fetched or not).
- **tests**: run `.claude/skills/review-gateware-project/scan_tests.sh original_sources/<slug>` and paste its one-line
  output (verbatim).
- **make_tests**: run `python3 .claude/skills/review-gateware-project/scan_make_tests.py original_sources/<slug>`.
  If it prints `none found`, leave the field EMPTY. Otherwise read those Makefile targets and write which ones really
  RUN a testbench / simulation / formal check: `make [-C dir] target (simulator): testbench files - self-checking
  (how) | waveform-only`; separate several with `; `. If none really runs, write `none: <reason>` (lint only,
  tb missing from clone, compiles but never runs vvp, ...).

Rules: facts only, cite paths; write `unknown` when not determinable, never guess. Keep each field reasonably short
(name < 150 chars, reuse/notes < 500 chars). Look at existing rows (objects) in `data/catalogue.json`
(e.g. `wuxx__icesugar`, `machdyne__zeitlos`) for the style.

Helper scripts: only under a unique name in the scratchpad (other agents share it).

OUTPUT: write your rows (no header) to the file path you are given, one line per slug, then verify with
`awk -F'\t' '{print NF}' <file>` that every line has exactly 15 fields. Reply with a 2–3 line summary per repo plus
any facts worth recording (best reusable block, surprises). Do not modify any other file.
