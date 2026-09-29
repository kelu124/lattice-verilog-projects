---
name: owner-working-style
description: How the repo owner likes work to run — parallel agents are welcome, commit + push at checkpoints when asked, English for published content, keep everything recoverable in the repo
metadata:
  type: feedback
---

Observed and stated by the owner on 2026-09-28:
- **Parallel agents are welcome** ("you can spin different agents for the cataloguing if it helps"; asked which TODO
  repos could go to "a few agents"). Batches of 4–17 repos per Sonnet agent worked well; see the review skill,
  "Batch cataloguing with agents".
- **Commit and push at checkpoints when asked**; the default rule (skill `committing`) is still: never push unless asked.
  The owner often asks "update skills and memory first, then push" — do the bookkeeping before the push.
- **Published content is in English** (site, README, contribute.md); the owner sometimes writes in French.
- **Start-of-session handoff**: before a new chat the owner asks to review README and the site index, update memory and
  push, so a fresh session resumes cleanly: keep the "Start here next session" block in `.claude/TODO.md` current.

**Why:** the owner restarts sessions often and relies on the repo (not the chat) to carry state.
**How to apply:** propose parallel batches for large work, finish with memory + TODO + COMMIT_LOG, then push only when
asked. See [[data-docs-layout]], [[project-goal]].
