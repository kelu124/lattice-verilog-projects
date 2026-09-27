---
name: shallow-clones
description: Owner rule: every clone under original_sources/ is shallow (--depth 1); history stats live in history.tsv.
metadata:
  type: feedback
---

All upstream clones in this repo must be **shallow** (`--depth 1`). This is the default in `clone.sh`; there is no
full-clone mode. On 2026-09-27 the 71 existing full clones were converted in place: the pinned commit was kept,
other refs dropped, and gc run.

**Why:** the owner asked for it explicitly on 2026-09-27. The disk was 97–99 % full (about 4 GB free after 226 clones).

**How to apply:** never unshallow or full-clone. Activity stats that need history (first commit, commit count)
are in `.claude/memory/history.tsv` for the first 71 repos. For newer repos use the GitHub API (created_at, and
contributors or commits pagination) and add them there. `gen_catalogue.py` reads history.tsv. See [[source-lists]].
