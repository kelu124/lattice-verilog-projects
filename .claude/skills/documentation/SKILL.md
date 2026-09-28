---
name: documentation
description: Rules for writing documentation in ulx3s-klod — data/ JSON is the source, docs/ is the generated GitHub Pages site; per-project page template; sourcing/accuracy rules. Use when writing or editing anything under data/, docs/ or the project registry.
---

# Documentation rules

## Data first, docs generated (owner rule 2026-09-28)
Everything gathered lives as **JSON in `data/`**; **`docs/` is the GitHub Pages site and is generated**. Never edit
`docs/` by hand: edit the JSON, then `make docs`.

| Data (source of truth) | Rendered to | By |
|---|---|---|
| `data/catalogue.json` (one object per repo, 15 fields, `functions` = list) | `docs/catalogue.md` | `review-gateware-project/gen_catalogue.py` (`--merge rows.tsv\|rows.json` upserts rows) |
| `data/lpfs.json` (every LPF in the clones) | `docs/lpf-catalogue.md` | `review-gateware-project/scan_lpfs.py` (scan clones → JSON), `gen_lpf_catalogue.py` |
| `data/pages/<slug>.json` (guides, references, surveys) | `docs/<slug>.md` | `documentation/gen_pages.py` |
| `data/pages/index.json` (intro) | `docs/index.md` (+ generated lists) | `documentation/gen_pages.py` |
| `data/projects/<owner>__<repo>.json` (one review per project) | `docs/projects/<slug>.md` | `documentation/gen_pages.py` |

Page JSON model (`documentation/mdjson.py`, schema `ulx3s-klod/page/v1`): `kind` (project | guide | reference |
survey | index), `slug`, `title`, `description` (one line, shown on the index), `fields` (project header table),
`blocks` and nested `sections` (`title`, `blocks`, `sections`). Blocks: `paragraph` (inline markdown text),
`table` (`columns` + `rows` as objects keyed by column), `list` (`items`: strings or `{text, items}`), `code`
(`lang`, `text`), `hr`. Links in text are relative to the rendered page (`docs/` or `docs/projects/`); links that
leave `docs/` are rewritten to GitHub URLs at render time.

**Writing a new page**: draft it in markdown (following the template below; agents may write the draft to the
scratchpad), import it with `documentation/md2json.py draft.md data/projects/<slug>.json --kind project
[--description "..."]`, then `make docs`. Editing an existing page: edit its JSON (or render, edit the markdown
copy, re-import). Survey tables are data: update the row objects (e.g. a `status` cell) instead of prose.

## Where things go
- `data/projects/<owner>__<repo>.json` → `docs/projects/<owner>__<repo>.md` — one page per reviewed project (template below).
- `data/pages/<topic>.json` → `docs/<topic>.md` — cross-project topics (surveys, board reference, DFU guide).
  The index (`docs/index.md`) lists them automatically; also link important ones from `README.md`.
- `.claude/memory/projects.md` — the **summary row** for each project (the
  registry). The docs page holds details; the registry holds the one-liner.
  Keep both in sync in the same commit.
- `README.md` — human entry point on GitHub: purpose of the repo + index of docs pages. `docs/index.md` is the
  landing page of the GitHub Pages site (source: main branch, `/docs`; `docs/_config.yml`).

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
| Toolchain | `open` (yosys+nextpnr-ecp5+ecppack) / `diamond` (Lattice) / `both` — details, versions if pinned |
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
Things not verified yet (also add them to `.claude/TODO.md`).
```
