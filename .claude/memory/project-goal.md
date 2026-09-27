---
name: project-goal
description: Why this repo exists — a cloneable, persistent Claude memory of everything people have built on the ULX3S, used to help design new gateware on top of it.
metadata:
  type: project
---

Goal (stated by the repo owner, 2026-09-27): build up a **thorough memory of what
people have done with the ULX3S** (gateware, SoCs, cores, tools, add-on
hardware) so that Claude can **help people develop new things on top of it**:
suggest existing cores to reuse, know board pitfalls, pick a toolchain, and
point at working reference designs.

The memory must travel with the repo: anyone who clones it and runs Claude Code
here resumes at the same state. So all memory lives in `.claude/memory/` (tracked),
never only in `~/.claude/projects/...`.

**Why:** a single place that answers "has someone already done X on ULX3S, and how?"

**How to apply:**
- When reviewing a project, record *reusable building blocks* (cores, drivers,
  pin usage, tricks), not only a summary — see [[projects]] "Reuse notes".
- When a user asks to build something new, first search [[projects]] and
  `docs/` for prior art and board constraints ([[board-hardware]], [[board-revisions]]).
- Hardware ground truth comes from the board repo and its manual: [[board-hardware]].
