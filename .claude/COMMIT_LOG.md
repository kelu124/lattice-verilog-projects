# Commit log

Newest first. One entry per meaningful commit: what was done and why (see skill `committing`).

## 2026-09-27 — docs(catalogue): add ULX5M (GateMate) repos as survey group F
- **What**: searched GitHub for `ulx5m` (repo name, README, forks, `ulx5m-gs`); recorded 5 own repos, the
  forks and related projects as group F in `docs/github-survey.md`. Shallow-cloned and pinned 3:
  `intergalaktik__ulx5m-gs` (board hardware), `goran-mahovlic__ulx5m-litex-ai` (LiteX Linux SBC + SerDes),
  `pu-cc__ulx5m_gpiocheck` (GPIO test with the only public `.ccf` pin file). Added their catalogue rows
  (290 → 293), regenerated `docs/catalogue.md`, new memory `ulx5m-board.md`, counts in MEMORY/projects/source-lists.
- **Why**: owner asked whether ULX5M repos could be added to the catalogue.
- **Notes**: ULX5M uses a **Cologne Chip GateMate CCGM1A1, not an ECP5**, so its rows say "NOT ECP5" in the
  fpga column and ECP5 cores do not port as-is. Hardware-only / bitstream-only / 118 MB student repos left
  uncloned (disk 94 % full), listed with reasons in group F.

## 2026-09-27 — docs(catalogue): catalogue 64 ULX3S/ULX4M-dedicated repos from survey groups B/D/E
- **What**: shallow-cloned and pinned 64 more repos from `docs/github-survey.md` — all 51 of group B
  (ULX3S-dedicated by name/description), all 11 of group D (forks with substantial own commits), and
  the 2 ULX4M-specific repos in group E (`lawrie/ulx4m_examples`, `lawrie/ulx4m_amaranth_examples`).
  Deliberately skipped group C (69 multi-board projects where ULX3S is one of many targets) and the 9
  non-ULX4M links in group E. Catalogued all 64 with a 3-agent workflow (FPGA, toolchain, HDL, license,
  functions, reuse, notes), added the heuristic `tests` column, merged into `.claude/memory/catalogue.tsv`
  (226 → 290 rows, verified 1:1 against `sources.tsv`), regenerated `docs/catalogue.md`, and refreshed
  repo counts in `MEMORY.md`, `projects.md`, `reusable-cores.md`, `source-lists.md` and `README.md`.
- **Why**: owner asked to prioritise the repos that are actually about ULX3S/ULX4M devices from the
  wider GitHub survey, over generic multi-board frameworks that merely support the board among many.
- **Notes**: because this batch's survey evidence was weaker (name/description match or fork activity,
  not a confirmed `.lpf`), the cataloguing agents were told to verify honestly — 7 of the 64 turned out
  to have **no real ULX3S/ULX4M build** despite matching the survey (`mkvenkit__ulx3s_examples`,
  `lawrie__ulx3s_pdp_11`, `pepijndevos__rust-litex-example`, `dpks2003__dice_crap_game`,
  `pfontvilanova__pfforthmachine`, `tom7980__ulxws`, `cheyao__sega-sms` — the last now targets Machdyne's
  icepi-zero instead), plus 2 more (`ghaworth__ulx3s-bldc-foc`, `ghaworth__ulx3s-tinyai`) are empty
  skeleton repos. Also found byte-identical forks already covered by other slugs (`danodus__ulx3s_68k`/
  `_sms` mirror `lawrie__ulx3s_68k`/`_sms`; `machdyne__nes_ecp5` mirrors `ironsteel__nes_ecp5`) — kept
  in the catalogue with `fork_of` noting the duplicate, not removed. `spinalhdl__saxonsoc`,
  `stnolting__neorv32-setups` and `lawrie__jupiter_ace` were removed from the candidates list in
  `projects.md` — they turned out to already be cloned via the earlier GitHub-search batch.

## 2026-09-27 — docs(repo): proofread and fix cross-file inconsistencies across the markdown docs
- **What**: 4 parallel agents proofread all 26 hand-maintained markdown files (CLAUDE.md, README.md, 6
  skill files, 10 memory files, 5 docs pages, TODO/DONE/COMMIT_LOG) for clarity, consistency and
  formatting, with instructions not to change facts or remove content. `docs/catalogue.md` was left
  untouched (generated file). Fixed: a stale "not cloned yet" claim about the 155 GitHub-survey repos
  that are in fact cloned (MEMORY.md, source-lists.md); a broken `[[projects]]` cross-reference
  (project-goal.md pointed at a "Reuse notes" section that doesn't exist); an undeclared `catalogued`
  status value used but never defined (projects.md); a missing `github-survey` skill entry in CLAUDE.md's
  layout table and rules section; assorted typos and spacing. Also resolved, by hand, a flagged
  69-vs-68-vs-71 repo-count discrepancy in projects.md: 68 of 69 ulx3s.github.io links were clonable
  (one 404) plus the 3 initial review targets (board repo, ulx3s-bin, openFPGALoader) = 71 pre-survey,
  matching `history.tsv`; reworded projects.md to state that explicitly instead of the wrong "69".
- **Why**: requested by the owner after the catalogue-merge push, to catch drift accumulated over a long
  incremental session before it misleads a future session.
- **Notes**: one agent's proposed "grammar fix" in COMMIT_LOG.md ("flearadio/rdsfpga are ULX2S-only" →
  "is") was actually wrong — that's a compound subject (two separate repos) — and was reverted by hand
  before committing. A reminder that agent-proposed prose fixes still need a human/parent check, especially
  around domain facts.

## 2026-09-27 — memory(repo): refresh stale repo counts after the survey catalogue merge
- **What**: updated `.claude/memory/MEMORY.md`, `projects.md`, `reusable-cores.md` and `README.md`,
  which still said "71 repos cloned/catalogued" after the merge that brought the total to 226
  (69 ulx3s.github.io + 155 GitHub-survey group A). README's "Wider survey" section also wrongly
  implied the 155 verified repos were still uncatalogued.
- **Why**: requested before pushing to main — stale counts in memory are worse than no counts, since
  they read as confirmed facts to a future session.
- **Notes**: none.

## 2026-09-27 — docs(catalogue): catalogue 155 more ULX3S repos from the GitHub survey
- **What**: ran a 6-agent Workflow (Sonnet 5) to catalogue all 155 group-A repos from `docs/github-survey.md`
  (kind, name, fork/preferred copy, ULX3S build path, FPGA, toolchain, HDL, license, LPF, functions, reuse,
  notes); merged into `.claude/memory/catalogue.tsv` (71 → 226 rows, verified 1:1 against `sources.tsv`).
  Added a heuristic `tests` column (`.claude/skills/review-gateware-project/scan_tests.sh`: detects tb/test/sim
  dirs, testbench-named files, and iverilog/Verilator/GHDL-sim/cocotb/VUnit mentions) for all 226 repos, and a
  new "Testbenches and simulation" section in `docs/catalogue.md` (107/226 repos have something detected).
  `catalogue-fields.md` and the review skill now require the tests field too.
- **Why**: owner asked to catalogue the survey repos once on a cheaper model, and separately asked to record
  available testbenches/tests per repo in the docs.
- **Notes**: the tests scan is a name/path heuristic (dirs/filenames/tool mentions), not proof anything actually
  runs or passes — flagged as such in the generated docs. A few repos surfaced real problems worth following up:
  emard__vhdl_c64_c1541_sd's own README says the ULX3S port "doesn't work... I give up"; ironsteel__nes_ecp5 was
  already known broken; several repos bundle copyrighted ROMs with no license file.

## 2026-09-27 — chore(repo): move TODO/DONE/COMMIT_LOG under .claude/
- **What**: moved `TODO.md`, `DONE.md`, `COMMIT_LOG.md` to `.claude/TODO.md`, `.claude/DONE.md`,
  `.claude/COMMIT_LOG.md`; updated every reference in `CLAUDE.md`, `README.md` and the five skill files.
- **Why**: owner asked to move them under `.claude/`, alongside the skills and memory that already
  live there, so the repo root stays uncluttered.
- **Notes**: none.

## 2026-09-27 — source(survey): shallow-clone 155 verified ULX3S repos, all clones shallow
- **What**: shallow-cloned and pinned the 155 group-A repos from `docs/github-survey.md` (now 226 in `sources.tsv`);
  converted the 71 earlier full clones to shallow in place (pinned commit kept); `clone.sh` is now always `--depth 1`;
  new `history.tsv` holds the first-commit date and commit count captured before shallowing; `gen_catalogue.py` reads it;
  memory `shallow-clones.md`; CLAUDE.md and the clone skill updated.
- **Why**: the owner asked to add the survey results to the collection, then to keep only shallow clones and make
  shallow the default. The disk was 98 % full.
- **Notes**: original_sources is 5.8 GB, with about 4 GB free. The largest is jderobot__fpga-robotics (1.5 GB even shallow). The 155 new repos are
  not catalogued yet (TODO).

## 2026-09-27 — docs(survey): record GitHub-wide survey of ULX3S repos
- **What**: `docs/github-survey.md` (≈297 candidate repos in 5 evidence groups with stars, last push, license,
  evidence path); skill `github-survey` (queries, evidence levels, procedure); `source-lists.md` updated with the
  run, frameworks with ULX3S support, and notable candidates; TODO for cloning (blocked on disk space).
- **Why**: the owner asked which other GitHub repos used the ULX3S for Verilog gateware. The list is saved in-repo
  so the survey is not lost with the session scratchpad.
- **Notes**: unauthenticated API only (no gh CLI), so no code search. Disk at 98 % (6.1 GB free), so nothing cloned yet.

## 2026-09-27 — docs(catalogue): catalogue 71 ULX3S repos with FPGA, toolchain, HDL, license
- **What**: `.claude/memory/catalogue.tsv` (one row per cloned repo: kind, fork/preferred copy, ULX3S build path,
  FPGA, toolchain, HDL, license, LPF, function tags, reusable blocks, notes); generator
  `.claude/skills/review-gateware-project/gen_catalogue.py` → `docs/catalogue.md` (grouped tables + per-repo
  details + index by function); memory `reusable-cores.md`; registry now points to the catalogue; new function tags.
- **Why**: owner asked for FPGA, Diamond vs open toolchain, Verilog vs VHDL, and licenses for every gateware repo, as the
  basis for helping people build new things. The TSV is the single source of truth, so it stays diffable and editable.
- **Notes**: filled by 5 parallel read-only agents (static inspection, nothing built). 31/71 repos have no license found.
  Several ulx3s.github.io entries are stale mirrors (ulx3s__apple2fpga, ulx3s__zx81, ulx3s__anotherworld_fpga with no ULX3S
  build, ulx3s__ulx3s-adda identical). flearadio/rdsfpga are ULX2S-only; neorv32 has no ULX3S target in-repo.

## 2026-09-27 — source(ulx3s.github.io): clone and pin 68 projects from the projects list
- **What**: cloned 68 repos into `original_sources/` and pinned them in `sources.tsv`; memory `source-lists.md`;
  license added as a mandatory catalogue field (`catalogue-fields.md`, review skill step 5b).
- **Why**: the owner asked to clone every repo listed under "Projects and examples" on https://ulx3s.github.io/.
- **Notes**: emard/ulx3s-examples returns 404. Non-git links skipped (gist, YouTube, blog, nxlab page). 3.1 GB of clones.

## 2026-09-27 — review(ulx3s-bin,openfpgaloader): add binaries kit and programmer
- **What**: cloned and pinned `emard__ulx3s-bin` @ 2a40f50 and `trabucayre__openfpgaloader` @ 676e53e;
  pages `docs/projects/emard__ulx3s-bin.md` (a per-folder table of every prebuilt design and its source
  project) and `docs/projects/trabucayre__openfpgaloader.md` (ULX3S board IDs `ulx3s`, `ulx3s_dfu`,
  `ulx3s_esp`, `ulx4m_dfu`); registry rows; new memory `catalogue-fields`; review skill now requires
  FPGA/toolchain/HDL fields and warns about RTK filtering `git log`.
- **Why**: requested by the owner. ulx3s-bin is the board's quickstart kit and the oldest catalogue of designs
  run on it; openFPGALoader is the recommended programmer. The owner also asked that FPGA, toolchain and HDL be recorded.
- **Notes**: the RTK hook's `git log` filtering gave wrong first-commit dates (fixed with `rtk proxy`).

## 2026-09-27 — skill(repo): bootstrap Claude memory, skills and tracking files
- **What**: `CLAUDE.md` (resume protocol, layout, rules); `.claude/skills/` with
  `clone-original-source` (+ `clone.sh`, pins commits in `sources.tsv`), `committing`,
  `documentation`, `todo-done`, `review-gateware-project`; `.claude/memory/` (goal, registry,
  board hardware, revisions, toolchain); first review, of emard/ulx3s @ 6a92cec
  (`docs/projects/emard__ulx3s.md`, `docs/board-reference.md`); README, TODO, DONE; `.gitignore`
  for `original_sources/` and build outputs.
- **Why**: the owner wants a repo that remembers everything done with the ULX3S and helps build
  new designs on it, with Claude's memory stored in the repo so a clone resumes the same state.
  The board repo and its MANUAL are the ground truth for everything else, so they came first.
- **Notes**: the MANUAL links LPFs at the wrong path (they are under `doc/constraints/prototype/`);
  a "v18" LPF is referenced but missing. 15 linked projects queued as candidates in `projects.md`.
