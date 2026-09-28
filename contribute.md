<!-- Generated from data/pages/contributing.json by .claude/skills/documentation/gen_site.py; do not edit. -->

# Contribute

Contributions are welcome: a project we missed, a better core for a function, a wrong license or FPGA size, a board
page, a new survey. This repo is built to be worked on with [Claude Code](https://claude.com/claude-code): the rules,
the workflows and the whole working memory live **inside the repo** (`CLAUDE.md` and the `.claude/` folder), so
anyone who clones it can continue exactly where the last session stopped, with the same conventions.

## What you can contribute

| Contribution | Where it ends up |
|---|---|
| A repo with ULX3S / ECP5 / iCE40 gateware we don't have | cloned, pinned, catalogued in [`data/catalogue.json`](data/catalogue.json) |
| A better (or first) core for a function | a record in [`data/cores.json`](data/cores.json), shown on the [function pages](docs/functions/index.md) |
| A correction (license, FPGA size, toolchain, a wrong claim) | the JSON record that holds the fact, with the file and commit that prove it |
| An in-depth review of a rich repo | [`data/projects/<owner>__<repo>.json`](data/projects), rendered in [Project reviews](docs/projects/index.md) |
| A new board, guide or survey | [`data/boards.json`](data/boards.json) or [`data/pages/`](data/pages) |
| A fix to the generators or scanners | the scripts in [`.claude/skills/`](.claude/skills) |

## How the repo is organised for Claude

| Path | Role |
|---|---|
| [`CLAUDE.md`](CLAUDE.md) | Entry point read by Claude Code at the start of every session: the resume protocol, the layout, the rules |
| [`.claude/memory/`](.claude/memory/MEMORY.md) | The working memory: one fact per file with frontmatter (`name`, `description`, `metadata.type`), indexed in `MEMORY.md`. Board facts, toolchain notes, owner decisions, the project registry, pinned sources (`sources.tsv`, `submodules.tsv`) |
| [`.claude/skills/`](.claude/skills) | Repeatable workflows (`SKILL.md`) and their scripts, invoked by Claude when a task matches |
| [`.claude/TODO.md`](.claude/TODO.md), [`DONE.md`](.claude/DONE.md), [`COMMIT_LOG.md`](.claude/COMMIT_LOG.md) | Open work (with a "start here next session" handoff), finished work, and the what/why of every commit |
| [`data/`](data) | All gathered data as JSON: the source of truth |
| [`docs/`](docs) | This site, **generated** from `data/` (never edited by hand) |
| `original_sources/` | Local shallow clones of the upstream repos (gitignored, read-only, pruned of non-gateware files) |

The skills:

| Skill | Use it to |
|---|---|
| [`review-gateware-project`](.claude/skills/review-gateware-project/SKILL.md) | Add or review a project end to end: clone, catalogue, add cores, write the page, commit |
| [`clone-original-source`](.claude/skills/clone-original-source/SKILL.md) | Clone, pin, restore and prune upstream repos (`clone.sh`, `prune.py`) |
| [`github-survey`](.claude/skills/github-survey/SKILL.md) | Search GitHub for new candidates and record the survey |
| [`documentation`](.claude/skills/documentation/SKILL.md) | The data model (pages, cores, boards), the page template, accuracy rules, the site generator |
| [`committing`](.claude/skills/committing/SKILL.md) | Commit format and the mandatory `COMMIT_LOG.md` entry |
| [`todo-done`](.claude/skills/todo-done/SKILL.md) | Keep `TODO.md` / `DONE.md` up to date |

## Contribute with Claude Code (recommended)

1. Fork and clone the repo, then start Claude Code at its root:

```bash
   git clone https://github.com/<you>/lattice-verilog-projects && cd lattice-verilog-projects
   claude
```

1. Claude reads `CLAUDE.md` and follows the resume protocol: memory index, `TODO.md`, last commits. The upstream
   clones are not in git; restore only what you need (all of them take about 5 GB after pruning, several hours
   of cloning):

```bash
   .claude/skills/clone-original-source/clone.sh https://github.com/<owner>/<repo>   # one repo
   .claude/skills/clone-original-source/clone.sh --restore                          # everything
   .claude/skills/clone-original-source/prune.py --apply --all
```

1. Ask in plain words, for example:
   - "Review https://github.com/owner/repo and add it to the catalogue."
   - "Is there a better UART core than the one on the UART page? Update data/cores.json."
   - "The license of core X is wrong, check the file header and fix it."
   - "Survey GitHub for ULX3S Ethernet projects we don't have yet."
2. Claude applies the skills: shallow clone pinned in `sources.tsv`, facts read from the sources (never built or
   guessed), JSON updated, `make check usage docs`, memory / TODO / DONE updated, and a commit with a
   `COMMIT_LOG.md` entry. Review the diff, then push to your fork and open a pull request.

Keep the memory in the repo: anything Claude learns about this project must go to `.claude/memory/` (one fact per
file, linked from `MEMORY.md`), not to your personal `~/.claude/` memory, so the next contributor gets it too.

## Contribute without Claude

Everything is plain files; follow the same rules by hand:

1. Edit the JSON in `data/` (for a page, you can write markdown and import it with
   `.claude/skills/documentation/md2json.py draft.md data/projects/<slug>.json --kind project`).
2. Run `make check` (validates the data; core file paths need the clones) and `make docs` (regenerates `docs/`).
3. Update `.claude/TODO.md` / `DONE.md` if relevant and prepend an entry to `.claude/COMMIT_LOG.md`
   (`## YYYY-MM-DD — type(scope): summary`, then What / Why).
4. Commit data and regenerated docs together and open a pull request.

Small corrections are also welcome as a GitHub issue: say what is wrong and link the upstream file (and commit) that
shows it.

## Rules

- **Cite sources**: every fact points to a file at a pinned commit; write `unknown` or "unverified" instead of guessing.
- **Licenses matter**: record the SPDX id found in the file or repo; `none found` means all rights reserved.
- **Never edit `docs/` by hand**: change `data/` and run `make docs`.
- **Never modify or commit `original_sources/`**; clones are shallow (`--depth 1`); fetch submodules only when they
  are gateware (`clone.sh --submodule`).
- **Mark non-ECP5 targets** `NOT ECP5` in the catalogue; iCE40 cores must say which `SB_*` primitives need porting.
- **Dates are absolute** (YYYY-MM-DD); English for everything published.
- **One commit per coherent change**, with its `COMMIT_LOG.md` entry and the memory/TODO/DONE updates in the same commit.
