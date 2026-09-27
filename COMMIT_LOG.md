# Commit log

Newest first. One entry per meaningful commit: what was done and why (see skill `committing`).

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
