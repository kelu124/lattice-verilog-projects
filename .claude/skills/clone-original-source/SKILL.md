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
5. **Shallow only**: `clone.sh` always clones with `--depth 1` (owner's rule, 2026-09-27; the disk
   is nearly full). Never run a plain `git clone` or `git fetch --unshallow` here. `git log -1` still gives the
   last-update date. If first-commit date or commit count is needed, get it from the GitHub API or
   from a temporary clone outside the repo, and record it in `.claude/memory/history.tsv`.
6. **Submodules**: not fetched by default. Fetch one only when it is explicitly gateware (a USB/CPU/DDR3/UART
   core the repo is built around), with `clone.sh --submodule <slug> <path> "<reason>"`. It is shallow, at
   the superproject's pinned commit, and recorded in `.claude/memory/submodules.tsv` (restored by `--restore`).
   Don't fetch frameworks/generators (LiteX, migen, SpinalHDL, jtframe), software, tests, KiCad libs, or
   upstreams already cloned under their own slug. Then update the repo's catalogue row (hdl, license, reuse, notes).
7. Check free space (`df -h /`) before large batches.
8. **Prune** after cloning (owner rule, memory `prune-clones.md`): `prune.py --apply --all` deletes
   non-gateware files (bitstreams, build outputs, tools, PCB/3D, PDFs, big images/archives) from the working
   trees, never commits. Per-slug folders go in `prune.tsv` (`delete`/`keep`). Dry run without `--apply`.
9. **Other forges**: GitLab and Codeberg URLs work with `clone.sh` (slug = owner__repo). Gitee clones work but can
   fail once with a GnuTLS error: re-run. `clone.sh` clones the **default branch** only: repos whose ULX3S work is on
   another branch (gregdavill/foboot `OrangeCrab`, ulx3s/ttsky-verilog-template `ulx3s`) need branch support (TODO).

## Commands

```bash
# Clone a new source and pin it
.claude/skills/clone-original-source/clone.sh https://github.com/<owner>/<repo>

# Re-create every pinned source at its recorded commit (fresh checkout of this repo)
.claude/skills/clone-original-source/clone.sh --restore

# Fetch one gateware submodule (shallow, pinned in submodules.tsv)
.claude/skills/clone-original-source/clone.sh --submodule <owner>__<repo> <path> "<why it is gateware>"

# Clone many (clone + pin + prune each; prints SUBMODULES for repos that declare some)
.claude/skills/clone-original-source/clone_batch.sh list.txt   # lines: owner/repo or full URL

# Pull latest upstream for one slug and re-pin
.claude/skills/clone-original-source/clone.sh --update <owner>__<repo>
```

## After cloning

- Add / update the project's entry in `.claude/memory/projects.md`
  (status `cloned`, commit, last upstream commit date).
- Commit `sources.tsv` + `projects.md` together (see skill `committing`).
