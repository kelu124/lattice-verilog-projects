---
name: data-docs-layout
description: Owner rule (2026-09-28) — all gathered data lives as JSON in data/; docs/ is a generated GitHub Pages site built by scripts (make docs), never edited by hand
metadata:
  type: feedback
---

All data gathered in this repo is stored as **JSON in `data/`** and **`docs/` is generated** from it for a GitHub
Pages site (owner request, 2026-09-28: "the docs folder will be about pushing to a gh page").

- `data/catalogue.json` (was `.claude/memory/catalogue.tsv`) → `docs/methodology/catalogue.md` via `gen_catalogue.py`
  (`--merge rows.tsv|rows.json` upserts agent rows).
- `data/lpfs.json` (from `scan_lpfs.py` over the clones) → `docs/methodology/lpf-catalogue.md` via `gen_lpf_catalogue.py`.
- `data/pages/*.json` (guides, surveys, ULX3S board reference, methodology, index intro) and `data/projects/*.json`
  (review pages) → `docs/guides/`, `docs/methodology/`, `docs/boards/ulx3s.md`, `docs/projects/`, `docs/index.md`
  via `documentation/gen_site.py` (page model in `mdjson.py`; tables are row objects; links remapped).
- `make check` validates, `make usage` rescans core usage, `make lpfs` rescans LPFs, `make docs` renders everything. `docs/_config.yml` = Jekyll config (Pages source:
  main, `/docs`). `.claude/memory/{sources,submodules,history}.tsv` stay in memory: they drive `clone.sh`.

**Site (owner decisions 2026-09-28, English, just-the-docs theme; URL https://kelu124.github.io/lattice-verilog-projects/ once Pages is enabled on main /docs):** not a list of all repos but the
**reusable cores and the projects that use them**, organised **by function** (`data/functions.json`, 33 functions:
ADC, SPI, DAC, VGA, HDMI…), each core linking to its original files upstream at the pinned commit
(`data/cores.json`, usage from `scan_core_usage.py` → `data/core_usage.json`). Boards: only the most relevant, in
3 families ECP5 / UP5K / HX (`data/boards.json`, 16 boards). Guides (toolchain, porting iCE40→ECP5, DFU), the
in-depth project reviews, a Contribute page (also rendered as root `contribute.md`, with `CONTRIBUTING.md` as a pointer), and a methodology section linking to the raw material on GitHub (data files, memory,
skills). Generator: `documentation/gen_site.py` (front matter for nav, `{% raw %}` wrapper, explicit
`{#core-<id>}` anchors); validation: `documentation/check_data.py` (`make check`).

**Why:** the owner wants `docs/` to be a publishable GitHub Pages site and the data to be machine-readable.

**How to apply:** never edit `docs/` by hand. New pages: write a markdown draft, import with
`documentation/md2json.py draft.md data/projects/<slug>.json --kind project`, then `make docs`. Change survey
status by editing the table row objects in `data/pages/*.json`. Commit data + regenerated docs together.
The round-trip md → JSON → md was verified lossless on all 24 pages at migration. See [[projects]], [[catalogue-fields]].

**Repo renamed (2026-09-28):** GitHub repo `kelu124/ulx3s-klod` → **`kelu124/lattice-verilog-projects`**
(remote `git@github.com:kelu124/lattice-verilog-projects.git`); site URL
**https://kelu124.github.io/lattice-verilog-projects/**. Generators (`REPO_URL` in gen_site.py, gen_catalogue.py,
gen_lpf_catalogue.py) use the new name. "ulx3s-klod" remains the internal project name in skills/CLAUDE.md and the
local folder name; old links in COMMIT_LOG history are left as they were.
