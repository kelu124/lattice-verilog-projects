# DONE

## 2026-09-28
- [x] Search GitHub for UP5K gateware, clone + catalogue 8 repos (+11 gateware submodules) via 2 subagents; 308 → 316 → commit "docs(catalogue): catalogue 8 iCE40 UP5K gateware repos from GitHub"

## 2026-09-27
- [x] Add `clone.sh --submodule` + `submodules.tsv` allowlist (gateware-only submodules, owner rule); fetch 30 gateware submodules in 22 repos; refresh their catalogue rows (3 agents) → commit "source(submodules): fetch gateware submodules and refresh their catalogue rows"
- [x] Add joshajohnson/ecp5-mini-projects, kbeckmann/pergola_projects (ECP5), iCEBreaker org repos + damdoy/ice40_ultraplus_examples (iCE40 UP5K, marked NOT ECP5; icecrash dropped: no HDL); gen_catalogue lists non-ECP5 repos → same commit
- [x] Clone + catalogue the top 14 non-ULX3S ECP5 repos (12 new, 2 rows refreshed) via 3 parallel agents; reusable-cores gets DDR3, PSRAM, HDMI-audio, USB-CDC, JTAGG, SGMII rows → commit "docs(catalogue): catalogue 14 gateware repos for other ECP5 boards"
- [x] Remove the ULX5M-GS repos from the catalogue, sources.tsv and original_sources/ (owner request); drop the ULX5M TODO → commit "chore(catalogue): remove ULX5M-GS repos on owner request"
- [x] Survey GitHub for gateware of other ECP5 boards (OrangeCrab, LUNA/Cynthion, iCESugar-Pro, Hackaday 2019 badge, Colorlight, ButterStick, ECPIX-5, …): 114 repos, 24 recommended → docs/ecp5-boards-survey.md, commit "docs(survey): record GitHub survey of non-ULX3S ECP5 board gateware"
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
