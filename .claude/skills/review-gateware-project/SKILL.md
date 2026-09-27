---
name: review-gateware-project
description: End-to-end workflow to review one ULX3S gateware project — clone it, identify its functions, toolchain, target FPGA and activity, write its docs page and update the project registry. Use when asked to review, survey, or add a ULX3S project.
---

# Reviewing a ULX3S gateware project

1. **TODO**: move "review <slug>" to *In progress* in `TODO.md` (add it if absent).
2. **Clone**: `.claude/skills/clone-original-source/clone.sh <url>` (skill
   `clone-original-source`). Note the pinned commit.
3. **Activity**: from the clone
   ```bash
   cd original_sources/<slug>
   git log -1 --format='%cs %h'           # last update
   git log --reverse --format=%cs | head -1  # first commit
   git rev-list --count HEAD               # commit count
   git shortlog -sn | head                 # main authors
   ```
   **Pitfall**: on this machine the RTK hook rewrites `git log` and filters its output
   (it once reported a wrong first-commit date). For history statistics use
   `rtk proxy git log ...` / `rtk proxy git rev-list ...` to get raw output.
4. **Toolchain**: look at `Makefile`s, `*.mk`, `*.lpf`, `*.py` (LiteX/Amaranth),
   `build.sbt` (SpinalHDL), `*.ldf`/`*.lpf` + `.xcf` (Diamond), CI files.
   Record synthesis / P&R / packing / programmer, and pinned versions if any.
5. **Target**: FPGA size (`--12k/--25k/--45k/--85k`, `LFE5U-xxF`), package
   (`CABGA381`), board revision from the `.lpf` name.
5b. **Mandatory catalogue fields** (the owner asked for these on every gateware repo):
   - **FPGA**: ECP5 size(s) supported (12F/25F/45F/85F, or `UM`/`UM5G` variants), from Makefiles/LPF/nextpnr flags.
   - **Toolchain**: `open` (yosys+nextpnr-ecp5+ecppack, incl. via LiteX/apio/ghdl-yosys-plugin),
     `diamond` (Lattice Diamond: `.ldf`, `.xcf`, `diamond`/`pnmainc` scripts), or `both`.
   - **HDL**: Verilog, SystemVerilog, VHDL, or generator (SpinalHDL, Migen/LiteX, Amaranth,
     Silice, Clash, Chisel…); list all present, main one first.
   - **License**: SPDX id from LICENSE/COPYING (any depth), README or file headers; `none found`
     otherwise (= all rights reserved; flag it for reuse). Mixed licenses (e.g. ROMs) noted.
6. **Functions**: list what the gateware does (one bullet per function, with top
   module path). Use the vocabulary in `.claude/memory/projects.md` → "Function tags"
   so projects are comparable; add a new tag there if needed.
7. **Build check (optional, only if toolchain present)**: build in a copy
   outside `original_sources/`, record result (pass/fail + error) — never flash
   hardware without the user's explicit go-ahead.
8. **Write** `docs/projects/<slug>.md` (skill `documentation` template) and
   update the project's row + detail block in `.claude/memory/projects.md`
   (status → `reviewed`, review date, commit).
9. **Follow-ups**: every open question → `TODO.md`. Cross-project insights
   (reusable cores, common pitfalls) → a memory file + `MEMORY.md` pointer.
10. **Close**: TODO → DONE, `COMMIT_LOG.md` entry, commit
    `review(<slug>): ...` (skill `committing`).
