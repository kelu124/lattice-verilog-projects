---
title: "sylefeb__silice"
parent: "Project reviews"
nav_order: 14
---
<!-- Generated from data/projects/sylefeb__silice.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# Silice (`sylefeb__silice`)

| Field | Value |
|---|---|
| Upstream | https://github.com/sylefeb/Silice |
| Reviewed at | `620487d` (upstream date 2026-06-18), reviewed 2026-09-28 |
| License | Mixed, by directory. Compiler + docs: GPL-3.0 (`LICENSE_GPLv3`, see `LICENSE.md`). Example projects (`projects/`): MIT (`LICENSE_MIT`), per-file headers confirm this on the files checked below. Compiler-generated Verilog glue code: MIT (`LICENSE.md`). Submodule `projects/tinygpus`: triple-licensed MIT/GPL-3.0/CERN-OHL-S-2.0 (`projects/tinygpus/LICENSE_mit`, `LICENSE_gplv3`, `LICENSE_ohls`); hardware `.si` files such as DMC-1 are marked CERN-OHL-S (`projects/tinygpus/hardware/GPUs/dmc-1/dmc-1.si`). |
| HDL / framework | **Silice** — a custom hardware-description language + compiler (C++ source under `src/`, ANTLR4 grammar in `antlr/`, entry point `src/silice.cpp`) that compiles `.si` sources down to synthesizable Verilog. Also Verilog (board glue, vendor-primitive wrappers, PLLs) and C/C++ (fire-v firmware, tinygpus tooling). |
| Toolchain | open (yosys + nextpnr-ecp5 + ecppack), driven by Silice's own `bin/silice-make.py` orchestrator, which calls the `silice` compiler then one of the board's builders declared in `frameworks/boards/ulx3s/board.json` (`shell` → `ulx3s.sh`, `yowasp` → `ulx3s.py`, or `edalize`/trellis or `edalize`/Diamond). |
| Programmer | openFPGALoader `-b ulx3s` (`frameworks/boards/ulx3s/ulx3s.sh`, and `board.json` `program` entries) |
| Target FPGA(s) | 12F / 25F / 45F / 85F — four board variants `12k`/`25k`/`45k`/`85k` in `frameworks/boards/ulx3s/board.json`; the `shell`/`ulx3s.sh` build script defaults to `--85k` |
| Board revision(s) | v2.x / v3.0.x — `frameworks/boards/ulx3s/ulx3s.lpf` header cites `https://github.com/emard/ulx3s/blob/master/doc/constraints/ulx3s_v20.lpf` and states "ULX3S v2.x.x and v3.0.x" (not v3.1.x) |
| Activity | Last commit 2026-06-18 (pinned commit `620487d`). 3420 commits, first commit 2019-10-07, per `.claude/memory/history.tsv` (recorded before this repo's clone was made shallow; this clone is `--depth 1` so commit count cannot be re-verified here). Submodule `projects/tinygpus` pinned at `498be1b`, fetched 2026-09-27. |

## What the gateware does

Silice is **not a single piece of gateware** — it is a language + compiler, plus a
large example library that happens to include many ULX3S designs. This page does
**not** review the compiler internals; it covers the ULX3S board framework and the
reusable cores named in the review brief.

- The compiler (`src/`, built via `CMakeLists.txt` into `bin/silice`) takes `.si`
  source and a board framework file (e.g. `frameworks/boards/ulx3s/ulx3s.v`) and
  emits plain Verilog (conventionally `build.v` or `out.v`). Neither output file
  is committed — both are listed in `.gitignore` (`out.v`, `BUILD*`), confirming
  generated Verilog is a build artifact, never checked into the repo.
- `frameworks/boards/ulx3s/` is the ULX3S board framework: pin mapping, the
  Verilog `top` wrapper, four FPGA-size variants, and four build backends. This
  is what lets any `.si` design target the ULX3S.
- `projects/` holds roughly two dozen example/demo designs (RISC-V SoCs,
  a DooM GPU, VGA/HDMI graphics demos, SDRAM/SD-card/OLED tests, audio
  streaming, arithmetic/algorithm demos…), several of which build directly for
  `ulx3s`. `projects/common/` is the shared peripheral-core library.
- A fetched submodule, `projects/tinygpus`, adds the DMC-1 tiny GPU rasterizer;
  it is not itself ULX3S-targeted (see Structure below).

## Structure

- `src/` — the Silice compiler itself (C++; `Algorithm.cpp`/`.h` is the bulk of
  the implementation at ~420 KB / 78 KB). Not reviewed in depth here.
- `bin/silice-make.py` — Python build orchestrator. Reads a board's `board.json`,
  applies the pin sets given via `-p`, invokes `silice --frameworks_dir … -f
  <board>.v -o build.v <design>.si`, then dispatches to the selected builder.
- `frameworks/boards/ulx3s/`:
  - `board.json` — declares variants `85k`/`45k`/`25k`/`12k`, pin sets (`basic`,
    `buttons`, `vga`, `oled`, `sdram`, `sdcard`, `hdmi`, `gpio`, `audio`, `uart`,
    `uart2`, `spiflash`, `qspiflash`, `us2_ps2`, `i2c`, `pmod_qqspi` — the last
    only on `85k`/`45k`), and four builders (`edalize`/trellis, `edalize`/Diamond,
    `shell` via `ulx3s.sh`, `yowasp` via `ulx3s.py`).
  - `ulx3s.v` — MIT-licensed Verilog top template with `%TOP_SIGNATURE%` /
    `%WIRE_DECL%` / `%MAIN_GLUE%` placeholders the compiler fills in, board pins
    declared via Lua-preprocessor `$$pin.*` variables, and the compiled design
    instantiated as `M_main __main(...)` — confirming Silice's convention that
    every design's entry point is a unit/algorithm literally named `main`.
  - `ulx3s.lpf` — pin constraints (see Board revision(s) above).
  - `ulx3s.sh` / `ulx3s.py` — shell/yowasp build scripts:
    `silice → yosys (synth_ecp5 -abc9) → nextpnr-ecp5 (--85k --package CABGA381
    --freq 25 --lpf ulx3s.lpf) → ecppack → openFPGALoader -b ulx3s`.
- `projects/common/` — the reusable peripheral-core library (see Reuse notes).
- `projects/` — ~23 example projects, several with a `ulx3s` Makefile target:
  `fire-v` (RISC-V SoC + graphics), `ice-v` (RISC-V CPUs), `doomchip`, `terrain`,
  `wolfpga`, `hdmi_test`, `sdram_test`, `sdram_memtest`, `oled_test`,
  `oled_text`, `oled_sdcard_test`, `video_sdram_test`, `audio_sdcard_streamer`,
  `i2s_audio`, `spiflash`, `qpsram`, `qspi_terrain`, `vga_demo`, `vga_test`,
  `vga_text_buffer`, `vga_wfc`, `blinky`, `uart_echo`, `buttons_and_leds`,
  `inout`, `neopixel`, `neopixel_uart`, `pipeline_sort`, `bram_interface`,
  `bram_wmask`, `divint_bare`, `divstd_bare`, `divstd_pipe`, `mulint_bare`,
  `mulint_pipe_bare`, `easy-riscv`, `kbfcrabe`, `flashbang`, `lcd_test`,
  `rsqrt`, `verilog-export` (list per `projects/README.md` + directory listing;
  `ice40-warmboot`/`ice40-dynboot` are ice40-only). Deep review here was scoped
  to `fire-v`, `ice-v` and the `common/` cores named in the review brief; the
  rest are listed but not individually reviewed.
- `projects/tinygpus/` — fetched submodule (pinned `498be1b`), triple-licensed
  (see License row). DMC-1 GPU at `hardware/GPUs/dmc-1/dmc-1.si`. Its own build
  system targets `icebreaker`/`mch2022` (`BOARD=` argument; `grep -rli ulx3s
  projects/tinygpus/` matches only `README.md`, no Makefile/board config). The
  README mentions the author "was using" a ULX3S 85F at one point
  (`projects/tinygpus/README.md:149`), but there is no ULX3S board target in the
  submodule itself.
- `tests/`, `tests/error_checks/`, `tests/issues/` — 385 `.si` regression files
  (recount at this commit; catalogue's `make_tests` column has the details),
  run via `test_all.sh`, not reviewed here.

File count check: excluding `tests/` and the `tinygpus` submodule, this repo has
194 `.si` files at commit `620487d` (`find . -name "*.si" ! -path "./tests/*" !
-path "./projects/tinygpus/*"`); `tests/` adds 385 more, and the submodule adds
10 — total 589. `.claude/memory/catalogue.tsv` states "578 .si" for the main
repo, close to (but ~1 off from) the 579 counted outside the submodule here;
not investigated further, treat as approximate.

## How to build

Not run or built as part of this review (read-only clone; no make/build per
task instructions). Commands below are as found in the repo, not verified to
succeed.

1. Install the compiler + toolchain: `./get_started_linux.sh` (`GetStarted_Linux.md`)
   builds Silice via CMake, installs it to `/usr/local/bin`/`/usr/local/shared/silice`,
   and downloads oss-cad-suite (yosys/nextpnr/etc.) — sudo required.
2. From a project directory, `make <board>`, e.g.:
   - `cd projects/fire-v && make ulx3s` → `projects/fire-v/Makefile`:
     `silice-make.py -s wildfire.si -b ulx3s -p basic,sdram,hdmi,sdcard -o BUILD_ulx3s`.
   - `cd projects/ice-v && make ulx3s` → `projects/ice-v/Makefile`'s `.DEFAULT`
     target uses `$@` as the board name: `silice-make.py -s SOCs/ice-v-soc.si -b
     ulx3s -p basic -o BUILD_ulx3s`.
3. `silice-make.py` compiles the design to `build.v` and calls the board's
   `shell` builder, `ulx3s.sh`, which runs the yosys → nextpnr-ecp5 → ecppack →
   openFPGALoader chain described in Structure above.

## Reuse notes

### Reusable blocks

| Block | Path | Top module | Language | Vendor primitives | License |
|---|---|---|---|---|---|
| ULX3S board framework | `frameworks/boards/ulx3s/{ulx3s.v,ulx3s.lpf,board.json,ulx3s.sh,ulx3s.py}` | `top` (wraps `M_main`) | Verilog + Lua preprocessor | `USRMCLK` (only for SPI/QSPI-flash builds) | MIT (`ulx3s.v` header) |
| DVI/HDMI (`hdmi.si`) | `projects/common/hdmi.si` (+ `hdmi_clock.v`, `ddr.v`, `hdmi_ddr_crgb.v`) | `algorithm hdmi(...)` clocked `<@pixel_clk,!rst>` | Silice + imported Verilog | `EHXPLLL` (PLL, `hdmi_clock.v` under `` `ifdef ECP5``), `ODDRX1F` (DDR serializer, `ddr.v`) | MIT (`hdmi.si` line 16, `ddr.v`, `hdmi_clock.v` all state it explicitly) |
| SDRAM controllers (`sdram_*.si`) | `projects/common/sdram_controller_autoprecharge_pipelined_r512_w64.si` (+ `_r128_w8`, `_r16_w16` variants; `sdram_interfaces.si`, `sdram_utils.si`, `sdram_arbitrers.si`; ULX3S IO wrappers `inout16_ff_ulx3s.v`, `out1_ff_ulx3s.v`, `out2_ff_ulx3s.v`, `out13_ff_ulx3s.v`; 37 board-specific PLL files in `projects/common/plls/ulx3s_*.v`) | `unit sdram_controller_autoprecharge_pipelined_r512_w64(...)` | Silice + imported Verilog | `BB` (bidirectional IO buffer) + `IFS1P3BX` (input FF), both via `inout16_ff_ulx3s.v`; `EHXPLLL` in the `plls/ulx3s_*.v` files | MIT (file header) |
| SD-card controller (`sdcard.si`) | `projects/common/sdcard.si` | `algorithm sdcard(...)` | Silice | none (bit-banged SPI mode, SDHC/SDXC only) | MIT (file header) |
| OLED/LCD (`oled*.si`) | `projects/common/oled.si` (driver dispatcher, selects one via `$$ST7789`/`$$SSD1351`/`$$SSD1331`) + `oled_st7789.si` / `oled_ssd1331.si` / `oled_ssd1351.si` | `algorithm oled(...)` (e.g. `oled_st7789.si`) | Silice | none (bit-banged SPI) | MIT (file header) |
| fire-v (RISC-V CPU + graphics SoC) | `projects/fire-v/{wildfire.si, fire-v/fire-v.si, inferno.si, spark.si, blaze.si}` | `unit rv32i_cpu(...)` (`fire-v/fire-v.si`); SoC top is `wildfire.si` | Silice + C firmware (`compile_c.sh`) | none in the CPU core itself; the `wildfire.si` SoC wrapper pulls in the `sdram`/`hdmi`/`sdcard` cores above (per its Makefile pin list `basic,sdram,hdmi,sdcard`) | MIT (`fire-v.si` header) |
| ice-v (RISC-V CPU family) | `projects/ice-v/CPUs/{ice-v.si, ice-v-dual.si, ice-v-dual-compact.si, ice-v-swirl.si, ...}`; default SoC top `projects/ice-v/SOCs/ice-v-soc.si` | `unit rv32i_cpu(bram_port mem)` (`CPUs/ice-v.si`); SoC entry point is `unit main(...)` (`SOCs/ice-v-soc.si:41`) | Silice | none in the CPU core; the SoC only imports a PLL for `ICESTICK`/`FOMU`/`ICEBREAKER`/`ICEBITSY` — no PLL branch for ULX3S, it runs directly off the 25 MHz board clock | MIT (`ice-v.si` header) |

### General reuse caveat: generated Verilog is not checked in

**Silice designs compile down to Verilog, but no generated Verilog is committed
anywhere in this repo** (`.gitignore` excludes `out.v` and `BUILD*`, and no
`build.v` or similar was found in the clone). This means reusing any `.si` core
in a plain-Verilog/VHDL ULX3S project requires **running the Silice compiler as
a build step** — there is no pre-generated `.v` to lift out directly. Concretely:
run `silice --frameworks_dir frameworks -f frameworks/boards/ulx3s/ulx3s.v -o
build.v <design>.si` (or use `bin/silice-make.py`) to produce Verilog, then that
output Verilog can be dropped into a non-Silice project — but the consumer needs
the Silice toolchain installed at build time, not just at "copy this file" time.
The Verilog *glue* code the compiler emits (module wiring, board top-level) is
MIT-licensed per `LICENSE.md` regardless of the license of the `.si` source that
generated it, but the `.si` source's own license (MIT for the cores above, GPL-3.0
for the compiler that processes it) still governs redistribution of the source.

### Per-block dependency/self-containment notes

- **hdmi.si**: self-contained; only depends on the three imported `.v` files
  named above (all in `projects/common/`) and `clean_reset.si`. Needs a 25 MHz
  pixel clock input; produces its own 250/125/25 MHz PLL domains internally via
  `hdmi_clock.v`.
- **sdram controllers**: depend on `sdram_interfaces.si` for the `sdram_provider`/
  `sdram_user` interface `group`s, and on the ULX3S-specific IO/PLL `.v` files
  above when `$$ULX3S` is set (`$$if ULX3S or ICEPI_ZERO then ... $$end` in the
  controller source) — porting to a non-ULX3S board means swapping those IO/PLL
  wrappers.
- **sdcard.si / oled\*.si**: standalone bit-banged SPI cores, no board-specific
  primitives, easiest to lift into another Silice design; still needs the
  compiler to produce Verilog for non-Silice reuse (see caveat above).
- **fire-v / ice-v**: the CPU cores themselves (`rv32i_cpu`) have no board
  dependency; the SoC wrappers (`wildfire.si`, `ice-v-soc.si`) pull in the board
  framework's pin sets and, for fire-v, the sdram/hdmi/sdcard cores above.

## Open questions

- Exact reason for the ~1-file discrepancy between the catalogue's "578 .si"
  count and the 579 recounted here (excluding `tests/` and the submodule) —
  not investigated, likely a minor recount/tooling difference.
- Whether the `12k`/`25k` ULX3S board variants in `board.json` have been tested
  on real 12F/25F hardware, or only `85k`/`45k` (not stated in the repo).
- Full commit-count/activity re-verification is blocked by the shallow
  (`--depth 1`) clone; `.claude/memory/history.tsv`'s 3420-commit / 2019-10-07
  figures are carried over from before the clone was made shallow and were not
  re-checked here.
- Whether any of the ~19 other `projects/` demos not reviewed here (DooM-chip,
  terrain, wolfpga, qpsram, etc.) have licensing or vendor-primitive quirks
  different from the pattern seen in `common/` — not checked.
{% endraw %}
