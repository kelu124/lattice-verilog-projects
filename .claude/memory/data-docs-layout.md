---
name: data-docs-layout
description: Owner rule (2026-09-28) — all gathered data lives as JSON in data/; docs/ is a generated GitHub Pages site built by scripts (make docs), never edited by hand
metadata:
  type: feedback
---

All data gathered in this repo is stored as **JSON in `data/`** and **`docs/` is generated** from it for a GitHub
Pages site (owner request, 2026-09-28: "the docs folder will be about pushing to a gh page").

- `data/catalogue.json` (was `.claude/memory/catalogue.tsv`) → `docs/catalogue.md` via `gen_catalogue.py`
  (`--merge rows.tsv|rows.json` upserts agent rows).
- `data/lpfs.json` (from `scan_lpfs.py` over the clones) → `docs/lpf-catalogue.md` via `gen_lpf_catalogue.py`.
- `data/pages/*.json` (surveys, board reference, DFU guide, index intro) and `data/projects/*.json` (review pages)
  → `docs/*.md`, `docs/projects/*.md`, `docs/index.md` via `documentation/gen_pages.py` (page model in `mdjson.py`;
  tables are row objects; outward links rewritten to GitHub URLs).
- `make docs` renders everything; `make lpfs` rescans LPFs. `docs/_config.yml` = Jekyll config (Pages source:
  main, `/docs`). `.claude/memory/{sources,submodules,history}.tsv` stay in memory: they drive `clone.sh`.

**Why:** the owner wants `docs/` to be a publishable GitHub Pages site and the data to be machine-readable.

**How to apply:** never edit `docs/` by hand. New pages: write a markdown draft, import with
`documentation/md2json.py draft.md data/projects/<slug>.json --kind project`, then `make docs`. Change survey
status by editing the table row objects in `data/pages/*.json`. Commit data + regenerated docs together.
The round-trip md → JSON → md was verified lossless on all 24 pages at migration. See [[projects]], [[catalogue-fields]].
