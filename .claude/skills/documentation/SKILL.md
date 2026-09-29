---
name: documentation
description: Rules for writing documentation in lattice-verilog-projects — data/ JSON is the source, docs/ is the generated GitHub Pages site; per-project page template; sourcing/accuracy rules. Use when writing or editing anything under data/, docs/ or the project registry.
---

# Documentation rules

## Data first, docs generated (owner rules 2026-09-28)
Everything gathered lives as **JSON in `data/`**; **`docs/` is the GitHub Pages site (just-the-docs theme), fully
generated**. Never edit `docs/` by hand: edit the JSON, then `make docs`. The site is organised around **reusable
cores by function** (not a list of all repos), with links to the original files upstream at the pinned commit and the
projects that use each core; boards only for the most relevant ones in 3 families (ECP5, UP5K, HX); a methodology
section that links to the raw material on GitHub. Site language: English.

| Data (source of truth) | Rendered to | By |
|---|---|---|
| `data/functions.json` (function taxonomy: id, title, group, catalogue_tags) | `docs/functions/index.md`, `docs/functions/<id>.md` | `documentation/gen_site.py` |
| `data/cores.json` (reusable cores: repo, files, top, license, primitives, usage_patterns…) | function pages | `gen_site.py` |
| `data/core_usage.json` (which repos copy/instantiate each core) | "Used by" lists | `review-gateware-project/scan_core_usage.py` (scan clones) |
| `data/boards.json` (families + curated boards, match regex) | `docs/boards/…` | `gen_site.py` (+ `data/lpfs.json`, PCF scan) |
| `data/pages/<slug>.json` kind `guide` / `survey` / `reference` / `methodology` / `index` | `docs/guides/`, `docs/methodology/`, ULX3S board page, `docs/index.md` | `gen_site.py` |
| `data/projects/<owner>__<repo>.json` (in-depth reviews) | `docs/projects/<slug>.md` | `gen_site.py` |
| `data/pages/contributing.json` (kind `contribute`) | `docs/contributing.md` **and root `contribute.md`** (+ `CONTRIBUTING.md` pointer) | `gen_site.py` (edit the JSON, not the .md) |
| `data/catalogue.json` (every repo) | `docs/methodology/catalogue.md` | `review-gateware-project/gen_catalogue.py` (`--merge rows.tsv\|json`) |
| `data/lpfs.json` (every LPF) | `docs/methodology/lpf-catalogue.md` | `scan_lpfs.py` (scan) + `gen_lpf_catalogue.py` |

`make docs` renders everything; `make lpfs` rescans LPFs; `make usage` rescans core usage. Generated pages carry
just-the-docs front matter (title/parent/grand_parent/nav_order) and a `{% raw %}` wrapper (Verilog `{{…}}` would
break Liquid). `docs/_config.yml` holds the theme config (Pages source: main, `/docs`).

Page JSON model (`documentation/mdjson.py`, schema `lattice-verilog-projects/page/v1`): `kind`, `slug`, `title`, optional
`nav_title`/`nav_order`, `description` (one line for indexes), `fields` (project header table), `blocks` and nested
`sections`. Blocks: `paragraph`, `table` (`columns` + `rows` as objects), `list`, `code`, `hr`. **Links in page
text are written relative to the legacy flat layout** (`docs/<slug>.md` for data/pages, `docs/projects/` for
data/projects, e.g. `DFUs.md`, `projects/x.md`, `../data/x.json`); `gen_site.py` remaps them to the site tree and
turns links that leave `docs/` into GitHub URLs.

Core records (`data/cores.json`): `id`, `name`, `functions` (ids, first = main), `rank` (best/alternative), `repo`,
`files` (paths that must exist in the clone), `top`, `language`, `license`, `fpga`, `primitives`, `summary`,
`ulx3s_notes`, `tests`, `usage_patterns` {`files`, `modules`} (distinctive names only). Validate with
`make check` (every file path exists in its clone, function ids known, one best per function).

**Writing a new page**: draft in markdown (template below; agents may write drafts to the scratchpad), import with
`documentation/md2json.py draft.md data/projects/<slug>.json --kind project [--description "..."]`, then `make docs`.
Survey tables are data: update the row objects instead of prose. Adding a core: add its record to
`data/cores.json`, `make usage docs`.

## Where things go
- `data/projects/<owner>__<repo>.json` → `docs/projects/<owner>__<repo>.md` — one page per reviewed project (template below).
- `data/pages/<topic>.json` → `docs/guides/` (kind guide), `docs/methodology/` (kind survey); the section indexes and
  the home page list them automatically; also link important ones from `README.md`.
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
