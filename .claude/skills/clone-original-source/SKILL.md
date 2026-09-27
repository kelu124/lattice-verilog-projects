---
name: clone-original-source
description: Clone (or restore) an upstream ULX3S gateware repository into original_sources/ and pin it in .claude/memory/sources.tsv. Use whenever you need to read upstream code, or on a fresh checkout of this repo where original_sources/ is empty.
---

# Cloning upstream repos into `original_sources/`

## Rules

1. **Location**: always `original_sources/<owner>__<repo>` (double underscore,
   lowercase as on the forge). Example: `original_sources/emard__ulx3s-misc`.
2. **Always use the script** — it records the clone in
   `.claude/memory/sources.tsv` (url, pinned commit, date cloned, slug), which is
   what makes the checkout reproducible for anyone who clones this repo.
3. **Read-only**: never edit, build in-place, or commit anything under
   `original_sources/` (the folder is gitignored). If you need to build, copy
   to a scratch directory or use `git worktree` outside the repo.
4. **Pin**: the commit recorded is the one reviewed. When you `--update` a
   source, the new commit is recorded and the project must be re-checked
   (add a TODO item "re-review <slug> at <new commit>").
5. Use shallow-ish clones for huge repos only if history is not needed; the
   "last updated" field in `projects.md` needs `git log -1`, which works in
   shallow clones too.

## Commands

```bash
# Clone a new source and pin it
.claude/skills/clone-original-source/clone.sh https://github.com/<owner>/<repo>

# Re-create every pinned source at its recorded commit (fresh checkout of this repo)
.claude/skills/clone-original-source/clone.sh --restore

# Pull latest upstream for one slug and re-pin
.claude/skills/clone-original-source/clone.sh --update <owner>__<repo>
```

## After cloning

- Add / update the project's entry in `.claude/memory/projects.md`
  (status `cloned`, commit, last upstream commit date).
- Commit `sources.tsv` + `projects.md` together (see skill `committing`).
