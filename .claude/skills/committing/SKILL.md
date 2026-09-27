---
name: committing
description: Rules for making git commits in ulx3s-klod — message format, what goes together in one commit, and the mandatory .claude/COMMIT_LOG.md entry recording what was done and why. Use before every commit.
---

# Committing rules

## When
- Commit at the end of every coherent unit of work (one project reviewed, one
  skill changed, one batch of TODO items closed). Do not leave the session with
  uncommitted memory changes — uncommitted memory is lost memory.
- Commit only on the user's request or at the end of a task the user asked
  for; never push unless asked.

## What goes in one commit
- The work **plus** its bookkeeping, together:
  - `.claude/memory/*` updates (registry, sources.tsv, facts learnt)
  - `.claude/TODO.md` / `.claude/DONE.md` changes
  - the `.claude/COMMIT_LOG.md` entry for this commit
- Never commit `original_sources/` content, build outputs (`*.bit`, `*.json`,
  `*.config`, `*.svf`), or secrets.

## Message format
```
<type>(<scope>): <imperative summary, ≤ 72 chars>

<why: 1–3 lines — the motivation, not a restatement of the diff>

Co-Authored-By: ...   (attribution line required by the harness, if any)
```
Types: `review` (project reviewed), `source` (clone/pin/update upstream),
`docs`, `memory` (facts / registry only), `skill` (skill or CLAUDE.md rules),
`chore`. Scope = project slug or area, e.g. `review(emard__ulx3s-misc): ...`.

## .claude/COMMIT_LOG.md entry (mandatory)
Prepend (newest first) to `.claude/COMMIT_LOG.md` **before** committing, in the same commit:

```markdown
## YYYY-MM-DD — <type>(<scope>): <summary>
- **What**: files / artefacts created or changed (short list)
- **Why**: the reason / the question this answers / the TODO item it closes
- **Notes**: surprises, open questions, follow-ups added to TODO (optional)
```
The hash is not known before committing; do not amend just to add it —
`git log --grep "<summary>"` finds it. `.claude/DONE.md` items reference the summary line.

## Checklist before `git commit`
1. `git status` — nothing under `original_sources/`, no build artefacts.
2. Memory updated? (`projects.md`, `MEMORY.md` index if a file was added)
3. TODO/DONE updated?
4. `.claude/COMMIT_LOG.md` entry prepended?
