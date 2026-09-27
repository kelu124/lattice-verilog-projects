# Commit log

Newest first. One entry per meaningful commit: what was done and why (see skill `committing`).

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
