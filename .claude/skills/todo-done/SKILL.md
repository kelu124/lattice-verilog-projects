---
name: todo-done
description: Rules for maintaining .claude/TODO.md (open work) and .claude/DONE.md (completed work log) in ulx3s-klod. Use whenever a task is discovered, started, finished, or abandoned.
---

# TODO / DONE tracking

`.claude/TODO.md` is the queue; `.claude/DONE.md` is the log. Together with `.claude/COMMIT_LOG.md`
they let the next session (or the next person) know exactly where things stand.

## .claude/TODO.md
Sections, in this order: `## In progress`, `## Next`, `## Backlog`, `## Blocked`.

Item format:
```markdown
- [ ] <imperative task> — <context/why, 1 line> (added YYYY-MM-DD)
```
- Anything discovered while working that you are not doing *now* → add it
  immediately, don't keep it in your head.
- At most a few items under **In progress**; move an item there when you start it.
- Blocked items say what they are blocked on: `(blocked: needs 85F board)`.
- Prefer concrete items ("review emard__ulx3s-misc DVI examples") over vague
  ones ("look at video stuff").

## .claude/DONE.md
Newest first, grouped by date:
```markdown
## YYYY-MM-DD
- [x] <task as it was in TODO> — result in one line → commit "<type(scope): summary>"
```
- When an item is finished: remove it from `.claude/TODO.md`, add it to `.claude/DONE.md`, in the
  same commit as the work.
- Abandoned items also go to `.claude/DONE.md`, prefixed `[~] abandoned:` with the reason.

## Session hygiene
- Start of session: read `.claude/TODO.md`; pick from In progress, then Next.
- End of session: TODO/DONE reflect reality before the final commit.
