---
name: documentation
description: Rules for writing documentation in ulx3s-klod — where docs go, the per-project page template, and sourcing/accuracy rules. Use when writing or editing anything under docs/ or the project registry.
---

# Documentation rules

## Where things go
- `docs/projects/<owner>__<repo>.md` — one page per reviewed project (template below).
- `docs/*.md` — cross-project topics (toolchain comparison, board revisions,
  peripheral cores catalogue, etc.). Link them from `README.md`.
- `.claude/memory/projects.md` — the **summary row** for each project (the
  registry). The docs page holds details; the registry holds the one-liner.
  Keep both in sync in the same commit.
- `README.md` — human entry point: purpose of the repo + index of docs pages.

## Accuracy
- Every factual claim about a project cites its source:
  `path/to/file.v` + pinned commit (from `sources.tsv`) or an upstream URL.
- If you did not verify it, write **`unknown`** or mark `(unverified: README claim)`.
  Never guess a toolchain, a board revision, or an FPGA size.
- Dates are absolute (YYYY-MM-DD).
- Write for a human who has a ULX3S but not the project: what it does, how to
  build it, what hardware/peripherals it needs.

## Style
- Markdown, sentence-case headings, tables for structured data.
- Short paragraphs; code blocks for commands, with the exact command.
- No marketing, no filler. Prefer "does X via module `foo.v`" over prose.

## Project page template
```markdown
# <Project name> (`<owner>__<repo>`)

| Field | Value |
|---|---|
| Upstream | <url> |
| Reviewed at | <commit short hash> (upstream date YYYY-MM-DD), reviewed YYYY-MM-DD |
| License | … |
| HDL / framework | Verilog / VHDL / SpinalHDL / LiteX / Amaranth / … |
| Toolchain | yosys+nextpnr-ecp5+ecppack / Diamond / … (versions if pinned) |
| Programmer | openFPGALoader / fujprog / … |
| Target FPGA(s) | 12F / 25F / 45F / 85F |
| Board revision(s) | v1.7 / v2.x / v3.x / unknown |
| Activity | last commit date, commit count, open issues if relevant |

## What the gateware does
Functions satisfied, one bullet each (e.g. HDMI/DVI video out, SDRAM controller,
RISC-V SoC, USB HID host, audio DAC, ESP32 passthrough …), with the top module.

## Structure
Key directories / top-level modules / constraint files.

## How to build
Exact commands, as found in the repo (Makefile targets), and whether they worked.

## Reuse notes
Cores worth reusing elsewhere, dependencies, gotchas.

## Open questions
Things not verified yet (also add them to TODO.md).
```
