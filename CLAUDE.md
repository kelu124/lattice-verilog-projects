# CLAUDE.md — ulx3s-klod

This repo is a **knowledge base about gateware developed for the ULX3S board**
(Radiona ULX3S, Lattice ECP5 FPGA: LFE5U-12F/25F/45F/85F). It records which
projects exist, what their gateware does, which toolchain they use, how alive
they are, and what Claude has learnt while reviewing them.

The repo is designed so that **Claude's working memory lives inside the repo**.
Anyone who clones it and starts Claude Code here picks up the work at the
exact state it was left in. Do **not** rely on the per-user memory in
`~/.claude/projects/...` for anything about this repo — write it here instead.

## Start of every session (resume protocol)

1. Read `.claude/memory/MEMORY.md` (index) and follow the links relevant to the task.
2. Read `TODO.md` (what is left) and skim the top of `DONE.md` / `COMMIT_LOG.md` (what happened last).
3. If `original_sources/` is empty or missing repos (fresh clone of this repo),
   restore them: `.claude/skills/clone-original-source/clone.sh --restore`.
4. Then work on the task. Before ending, update memory, TODO/DONE and commit
   (see rules below).

## Layout

| Path | Role | Tracked in git |
|------|------|----------------|
| `CLAUDE.md` | This file — entry point and rules summary | yes |
| `.claude/skills/*/SKILL.md` | Repeatable workflows (clone, commit, document, track, review) | yes |
| `.claude/memory/MEMORY.md` | Index of memory files (one line each) | yes |
| `.claude/memory/projects.md` | **Project registry**: every ULX3S gateware project, its functions, toolchain, last update, review status | yes |
| `.claude/memory/sources.tsv` | Pinned list of cloned upstream repos (url, commit, date) — lets anyone re-create `original_sources/` | yes |
| `.claude/memory/*.md` | Other facts: board knowledge, toolchain notes, decisions, user preferences | yes |
| `original_sources/` | Upstream repos cloned for review (read-only, never edited) | **no** (gitignored, re-creatable) |
| `docs/` | Human-readable documentation produced from reviews (`docs/projects/<slug>.md`, etc.) | yes |
| `TODO.md` | Open work items | yes |
| `DONE.md` | Completed work items, newest first, dated | yes |
| `COMMIT_LOG.md` | Why/what of each meaningful commit, newest first | yes |

## Rules (details in the skills)

- **Cloning upstream code** → skill `clone-original-source`. Always into
  `original_sources/<owner>__<repo>`, always via `clone.sh` so it is pinned in
  `sources.tsv`. Never modify cloned code; never commit it.
- **Committing** → skill `committing`. Small, focused commits; conventional
  prefixes; every commit gets an entry in `COMMIT_LOG.md` (what + why) in the
  same commit; memory/TODO/DONE updated in the same commit as the work.
- **Documentation** → skill `documentation`. One page per reviewed project in
  `docs/projects/`, facts cite the source file/commit, unknowns written as
  `unknown`, never guessed.
- **TODO / DONE** → skill `todo-done`. Every task discovered goes in `TODO.md`;
  when finished it moves to `DONE.md` with the date and commit.
- **Reviewing a project** → skill `review-gateware-project`. The end-to-end
  workflow that ties all of the above together and updates `projects.md`.

## Memory rules

- One fact per file in `.claude/memory/`, with frontmatter
  (`name`, `description`, `metadata.type` = user | feedback | project | reference).
- Add a one-line pointer to `.claude/memory/MEMORY.md` for each file.
- Update an existing file rather than duplicating; delete facts proven wrong.
- Dates are absolute (YYYY-MM-DD), never "yesterday" / "last week".
- Distinguish **verified** facts (checked in source, cite path@commit) from
  **unverified** ones (from memory / README claims) — mark the latter.

## Domain quick facts

Ground truth for the hardware is the board repo `emard/ulx3s` and its
[MANUAL](https://github.com/emard/ulx3s/blob/master/doc/MANUAL.md)
(`original_sources/emard__ulx3s/doc/MANUAL.md`). Distilled into
`.claude/memory/board-hardware.md`, `board-revisions.md`, `toolchain-and-programming.md`
and the human-facing `docs/board-reference.md`. Read those before advising on any design.

- ULX3S = Lattice ECP5 LFE5U-12F/25F/45F/85F (CABGA381), 25 MHz clock, 32 MB SDRAM (typical),
  QSPI flash, GPDI video, US1 FT231X + US2 direct USB, SD, ESP32, ADC, OLED header, 56 GPIO.
- Open flow: yosys → nextpnr-ecp5 → ecppack; load with openFPGALoader (`-b ulx3s`) or fujprog.
- Most boards are v2.x/v3.0.x → `ulx3s_v20.lpf`; v3.1.6/v3.1.7 → `ulx3s_v316.lpf`.
