---
name: shallow-clones
description: Owner rule: every clone under original_sources/ is shallow (--depth 1); history stats live in history.tsv.
metadata:
  type: feedback
---

All upstream clones in this repo must be **shallow** (`--depth 1`). This is the default in `clone.sh`; there is no
full-clone mode. On 2026-09-27 the 71 existing full clones were converted in place: the pinned commit was kept,
other refs were dropped, and `git gc` was run.

**Submodules** (owner rule, 2026-09-27): not fetched by default. A submodule is fetched only when it is explicitly
gateware (e.g. a USB, CPU, DDR3 or UART core the repo is built around), with
`clone.sh --submodule <slug> <path> "<reason>"`: shallow, at the commit the superproject pins, recorded in
`.claude/memory/submodules.tsv` so `--restore` re-fetches it. Never fetch frameworks/generators (LiteX, migen,
SpinalHDL, jtframe), software, test suites, hardware libraries, or upstreams already cloned as their own slug.

**Why:** the owner asked for it explicitly on 2026-09-27. The disk was 97–99 % full (about 4 GB free after 226 clones).

**How to apply:** never unshallow or full-clone. Activity stats that need history (first commit, commit count)
are in `.claude/memory/history.tsv` for the first 71 repos (the GitHub-survey 155 still need this — see TODO). For newer repos, use the GitHub API (`created_at`,
plus commits/contributors pagination) and add them there. `gen_catalogue.py` reads history.tsv. After cloning, prune non-gateware files ([[prune-clones]]). See [[source-lists]].
