# DONE

## 2026-09-27
- [x] Search GitHub for ULX5M repos (found GateMate, not ECP5): survey group F, clone + catalogue 3 (intergalaktik__ulx5m-gs, goran-mahovlic__ulx5m-litex-ai, pu-cc__ulx5m_gpiocheck), memory ulx5m-board.md → commit "docs(catalogue): add ULX5M (GateMate) repos as survey group F"
- [x] Clone and catalogue the 64 ULX3S/ULX4M-dedicated GitHub-survey repos (group B: 51, group D: 11, ULX4M from group E: 2), via a 3-agent workflow; merge into catalogue.tsv (now 290 repos), add tests column, regenerate docs/catalogue.md, refresh memory counts → commit "docs(catalogue): catalogue 64 ULX3S/ULX4M-dedicated repos from survey groups B/D/E"
- [x] Proofread all 26 hand-maintained markdown files (4 parallel agents: root/skills, memory, docs, tracking logs) for clarity/consistency/formatting; reverted one incorrect grammar "fix" and resolved a flagged 69/68/71 repo-count discrepancy → commit "docs(repo): proofread and fix cross-file inconsistencies across the markdown docs"
- [x] Fix stale repo counts (71 → 226) across MEMORY.md, projects.md, reusable-cores.md, README.md → commit "memory(repo): refresh stale repo counts after the survey catalogue merge"
- [x] Catalogue the 155 GitHub-survey repos (FPGA/toolchain/HDL/license/functions/reuse) via a 6-agent workflow on Sonnet 5, merge into catalogue.tsv (now 226 repos) → commit "docs(catalogue): catalogue 155 more ULX3S repos from the GitHub survey"
- [x] Add a `tests` column (heuristic testbench/simulation scan) to catalogue.tsv for all 226 repos, render a "Testbenches and simulation" section in docs/catalogue.md → same commit
- [x] Shallow-clone the 155 verified GitHub-survey repos (group A), pin them; convert the 71 existing clones to shallow; make shallow the only clone mode → commit "source(survey): shallow-clone 155 verified ULX3S repos, all clones shallow"
- [x] GitHub-wide search for ULX3S gateware: ≈297 candidates in docs/github-survey.md + github-survey skill → commit "docs(survey): record GitHub-wide survey of ULX3S repos"
- [x] Clone all repos from ulx3s.github.io "Projects and examples" (68/69; emard/ulx3s-examples is 404) → commit "source(ulx3s.github.io): clone and pin 68 projects from the projects list"
- [x] Catalogue FPGA/toolchain/HDL/license/functions/reuse for all 71 repos, generate docs/catalogue.md, add reusable-cores memory → commit "docs(catalogue): catalogue 71 ULX3S repos with FPGA, toolchain, HDL, license"
- [x] Clone and review emard__ulx3s-bin (quickstart/self-test kit, catalogue of early demos) and trabucayre__openfpgaloader (ULX3S board IDs) → commit "review(ulx3s-bin,openfpgaloader): add binaries kit and programmer"
- [x] Bootstrap repo memory: CLAUDE.md, skills (clone, committing, documentation, todo-done, review), memory index → commit "skill(repo): bootstrap Claude memory, skills and tracking files"
- [x] Clone and review emard__ulx3s (board hardware + MANUAL) → board-hardware, board-revisions and toolchain memories, docs/board-reference.md → same commit
