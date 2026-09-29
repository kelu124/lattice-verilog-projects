# Commit log

Newest first. One entry per meaningful commit: what was done and why (see skill `committing`).

## 2026-09-29 — chore(repo): replace the old ulx3s-klod name throughout the repo
- **What**: "ulx3s-klod" → "lattice-verilog-projects" in CLAUDE.md, all skill descriptions and texts, the page model
  (`mdjson.SCHEMA` and every `schema` id in data/*.json: `lattice-verilog-projects/{page,cores,lpfs,…}/v1`),
  generators, survey text, agent briefs (which now say "the repository root" instead of the local absolute path);
  site regenerated. Kept on purpose: the README "formerly" note, the rename note in memory data-docs-layout.md
  (updated) and COMMIT_LOG history.
- **Why**: owner noted the repo changed name and asked to replace it everywhere in the repo.

## 2026-09-28 — skill(repo): record the multi-agent batch workflow and working style
- **What**: `.claude/skills/clone-original-source/clone_batch.sh` (clone + pin + prune a list, flags submodules);
  agent briefs `.claude/skills/review-gateware-project/agent-briefs/{catalogue-row,core-record}.md` (were only in the
  session scratchpad); review skill section "Batch cataloguing with agents" (split, validate, merge, surveys); clone
  skill notes on GitLab/Codeberg/Gitee and default-branch-only; github-survey skill "Topic surveys"; CLAUDE.md pointer;
  memory `owner-working-style.md`; TODO handoff step.
- **Why**: owner asked to update skills and memory before committing and pushing, so the next session can reuse the
  workflow that catalogued ~150 repos with ~20 agents on 2026-09-28.

## 2026-09-28 — docs(catalogue): catalogue groups C/E, candidates, DFU bootloaders, RF and FFT designs
- **What**: cloned (shallow, pruned per repo) + catalogued 125 repos with ~20 Sonnet agents: GitHub survey group C (68 +
  hyperram-test) and remaining E (9), registry candidates (fujprog, TinyFPGA-Bootloader, LibXSVF-ESP, FleaFPGA-JTAG,
  ULX2S, ULX4M-LS, litex-boards, oberon_sdram, hyperram-test), DFU bootloaders (smunaut had2019 original,
  no2bootloader, foboot, tinydfu), ulx3s.github.io harvest (tt08-flame, TheZoq2 tinytapeout02 (GitLab), ulx3s
  tt-support-tools, rxrbln picorv32; Gitee link = stale learn-fpga copy), owner's lit3rick (review page), RF/DSP survey
  (15: HackRF Pro gateware, ZipCPU sdr, emeb lineage, 1bitSDR, lock-ins, WSPR, VNA, LoRa modulator, skywave…) and FFT
  survey (14 + dblclockfft). Gateware submodules fetched: no2usb/no2ice40/no2misc, valentyusb ×2, rf-dds-lo, secworks aes,
  smolfpga, verilog-axis, rggen RTL. DFU guide gains a "Verified 2026-09-28 from the bootloader sources" section
  (OrangeCrab bootloader = gregdavill/foboot branch OrangeCrab). 45 new cores (radio/dsp FFTs, CORDIC, lock-in, WSPR,
  WS2812, crypto SRNG/AES, bootloaders, Linux SoC vernier-rv32…): 218. Survey pages rf-dsp, fft, gitee. usage rescanned
  (691 uses), LPFs rescanned (1063 files). Memory: new lattice-rf-dsp.md; counts; source-lists rows; registry
  candidates replaced; TODO (clone.sh branch support, lit3rick flow question, scanner .vhdl blind spot).
- **Why**: owner asked to run TODO batches 1–5 (not the nested submodules) with parallel agents, catalogue lit3rick, add
  every Lattice FFT design, and survey Lattice RF/signal-processing gateware.
- **Notes**: agents shared a scratchpad; one reported a clobbered helper script, all outputs were re-validated (15
  fields, JSON, file paths) before merging. Class counts in README are approximate.

## 2026-09-28 — chore(repo): switch links to the renamed lattice-verilog-projects repo
- **What**: remote set to `git@github.com:kelu124/lattice-verilog-projects.git`; `REPO_URL` and GitHub links in
  gen_site.py, gen_catalogue.py, gen_lpf_catalogue.py; Pages URL `https://kelu124.github.io/lattice-verilog-projects/`
  in README, memory (project-goal, data-docs-layout), TODO; site title (`docs/_config.yml`, home page) and the clone
  command in the contributor guide; README title notes the former name. Site regenerated (no old URL left outside
  COMMIT_LOG history).
- **Why**: the GitHub repo was renamed from ulx3s-klod; owner asked to switch GitHub and GitHub Pages links.

## 2026-09-28 — docs(contrib): add contribute.md and reference it in the README
- **What**: `gen_site.py` renders the contributor guide (data/pages/contributing.json) to root `contribute.md`;
  `CONTRIBUTING.md` becomes a generated pointer (GitHub shows that name on issues/PRs). README gets a
  "Contributing" section and start-here row linking contribute.md; CLAUDE.md, documentation skill and
  data-docs-layout memory updated.
- **Why**: owner asked for a contribute.md referenced in the README, then commit and push.

## 2026-09-28 — docs(survey): ECP5-5G SERDES storage, ECPIX-5 and Cynthion gateware
- **What**: two research surveys imported as pages: `data/pages/serdes-survey.json` (47 queries: no open design
  drives an M.2 SSD over the ECP5 SERDES; LiteSATA drives a SATA drive on ECPIX-5; PCIe is endpoint-only Gen1 x1
  PoCs; boards table of LFE5UM boards and their connectors) and `data/pages/boards3-survey.json` (TinyFPGA EX never
  shipped, no gateware; ECPIX-5 and Cynthion facts + gateware). Cloned + catalogued 21 repos (9 SERDES, 5 ECPIX-5,
  7 Cynthion; no2misc submodule for eurorack-pmod; ECP5-PCIe's Gateware/utils submodule has no gitlink): 377 → 398.
  New function `serdes-links` (PCIe, SATA and SERDES links) with 9 cores (best: LiteSATA on ECPIX-5) + 9 more cores
  elsewhere (DDR3 core_ddr3_controller, AK4619 audio, orbtrace SWD/JTAG, 3 USB host engines, Cynthion analyzer,
  luna-soc, UAC2): 173 cores. Board pages ECPIX-5 and Cynthion (boards.json `lpf_board` field replaces the
  hard-coded LPF map in gen_site.py; scan_lpfs knows Cynthion). Memory: new ecp5-serdes-storage.md; counts in
  README, MEMORY, projects, reusable-cores; source-lists rows; TODO state + SSD follow-up. Pruned 210 MB.
- **Why**: owner asked whether any design drives an M.2 SSD over SERDES (focus LFE5UM boards), then for designs
  for TinyFPGA EX, LambdaConcept ECPIX-5 and Cynthion.
- **Notes**: HurricaneFPGA's README claims "working" but its PLL is a pass-through and its USB pins are
  placeholders (noted in the row). Agents could not use authenticated code search.

## 2026-09-28 — review(mmicko__fpga101-workshop): catalogue the FPGA 101 exercises and PicoSoC
- **What**: cloned + pinned mmicko/fpga101-workshop (iCE40 UP5K FPGA101 badge, Hackaday Belgrade 2018, MIT).
  Catalogue row (377 repos); review page `data/projects/mmicko__fpga101-workshop.json` with a table of the 20
  exercises (path, topic, SB_* primitives, testbench) plus tests/ and the Galaksija project; 2 new cores in
  `data/cores.json`: `mmicko-grom-cpu` (cpu-retro, used by lawrie ULX3S/ULX4M examples and fpga-odysseus) and
  `mmicko-fpga101-picosoc` (cpu-riscv, SPRAM + LCD text console + MicroPython port); i8080 core notes its origin.
  Found `ulx3s__fpga-odysseus` is the same author's ULX3S follow-up (10 identical files): its `fork_of` updated.
  Resolved the lawrie__ulx3s_examples open question "origin of the grom CPU". Usage rescanned, site rebuilt,
  counts updated (README, MEMORY, projects, reusable-cores), survey runner-up note, source-lists row.
- **Why**: owner asked whether the repo was captured, then to catalogue its 20 exercises and PicoSoC examples.

## 2026-09-28 — docs(contrib): add a contribute page and CONTRIBUTING.md
- **What**: `data/pages/contributing.json` (kind `contribute`): what to contribute, how the repo is organised for
  Claude (CLAUDE.md, `.claude/memory`, `.claude/skills`, TODO/DONE/COMMIT_LOG, data/, docs/), the skills table,
  a Claude Code workflow (clone, `claude`, example requests, what Claude does, PR), a manual workflow (edit data/,
  `make check docs`, COMMIT_LOG), and the rules. `gen_site.py` renders it to `docs/contributing.md` (nav 7, linked
  from the home page) and to root `CONTRIBUTING.md` via a new `write_root` (repo-relative links). README, CLAUDE.md,
  documentation skill and data-docs-layout memory point to it.
- **Why**: owner asked for a contribute page explaining how to contribute, especially with the `.claude` folder and
  CLAUDE.md files.

## 2026-09-28 — docs(repo): polish README and site home, handoff for a fresh session
- **What**: home page intro (data/pages/index.json) rewritten around cores by function (no more link to the memory
  file, no "project pages below"); home links point to section index.md pages. README: 153 cores/33 functions line,
  Pages-enable note, duplicate Colorlight removed, `data/` row lists all JSON files, reusable-cores row, review
  workflow mentions merge/cores/make. Memory: project-goal (search data/cores.json first; site), data-docs-layout
  (URL). TODO: "Start here next session" handoff; stale candidate list fixed.
- **Why**: owner asked to review the README and the site index, update memory and push, to restart from a clean session.

## 2026-09-28 — docs(site): generate a just-the-docs site of reusable cores by function
- **What**: new data: `data/functions.json` (33 functions in 6 groups), `data/cores.json` (153 cores: 1 best +
  alternatives per function, repo/files/top/language/license/FPGA/primitives/tests/ULX3S notes/usage patterns;
  researched by 5 Sonnet agents, every file path verified in the clones), `data/core_usage.json`
  (`scan_core_usage.py`: file copies + module instances in 17,424 HDL files → 481 core-repo uses; generic patterns
  removed), `data/boards.json` (16 boards: ECP5 ULX3S/ULX4M/OrangeCrab/Colorlight/IcePi Zero/iCESugar-Pro, UP5K
  iCEBreaker/UPduino/iCESugar/Fomu/pico-ice, HX breakout/BlackIce/iceFUN/Olimex/IcoBoard), pages toolchain,
  porting-ice40-to-ecp5, methodology. `gen_pages.py` → `gen_site.py`: just-the-docs tree (Home, Cores by function,
  Boards > family > board, Guides, Project reviews, Methodology with surveys + full catalogue + LPF catalogue),
  front matter, `{% raw %}` wrapper, `{#core-id}` anchors, links to upstream files at the pinned commit, legacy link
  remapping. `check_data.py` (`make check`), `make usage`. `docs/_config.yml` → remote_theme just-the-docs.
  Catalogue fixes from the research (emard__oberon sdram.v LGPL-2.1+, detegr composite tag). reusable-cores memory
  now points to data/cores.json; skills (documentation, review, github-survey), CLAUDE.md, README, memory updated.
- **Why**: owner: site in English with just-the-docs, organised by function (ADC, SPI, DAC, VGA, HDMI…) with links to
  the original files, showing reusable cores and the projects that use them (not a list of all repos); boards only
  the most relevant in 3 families; methodology linking to the GitHub materials; then push.
- **Notes**: Jekyll could not be run locally (gem native build failed), so the first real render is on GitHub
  Pages. Usage is a name heuristic. Non-ULX3S board descriptions are summaries (marked on the pages).

## 2026-09-28 — docs(data): move gathered data to data/ JSON, generate docs/ for GitHub Pages
- **What**: new `data/`: `catalogue.json` (was `.claude/memory/catalogue.tsv`; `functions` now a list),
  `lpfs.json` (was `docs/lpf-catalogue.json`), `pages/*.json` (board reference, DFU guide, 4 surveys, index intro),
  `projects/*.json` (18 review pages). Page model `documentation/mdjson.py` (sections/blocks; tables as row objects;
  project header table → `fields`), importer `md2json.py`, renderer `gen_pages.py` (docs/*.md, docs/projects/*.md,
  generated docs/index.md, outward links → GitHub URLs, "generated" header), `gen_catalogue.py` reads JSON and gains
  `--merge rows.tsv|json` + pin/row consistency warnings, `gen_lpf_catalogue.py` split into `scan_lpfs.py` (clones →
  JSON) + renderer. Root `Makefile` (`make docs`, `make lpfs`), `docs/_config.yml` (Jekyll, minimal theme).
  Round trip md → JSON → md verified identical on all 24 pages (only intended link rewrites differ). Skills
  (documentation, review-gateware-project, github-survey), CLAUDE.md, README, memory (new data-docs-layout.md,
  MEMORY, projects, reusable-cores, catalogue-fields) updated.
- **Also**: cloned + catalogued (via `--merge`, as a test of the new flow) the 8 honourable mentions of the HX survey
  (glasgow, BlackIce-II, apollo11_fpga, nanoV, dsp_ice, Centurion, BeagleWire, fpga-3-softcores + wb_intercon and
  verilog-arbiter submodules) and ECP5-survey recommended items 15–20, 22–24 (logic-noise workshop, orangecrab_adc,
  sound2fft, colorlight-i9-aes67, colorlight-led-cube, kholia 5A-75B, fpga-bitcoin-miner, LUNA, colorlight-picorv32).
  376 rows = 376 pins. Survey statuses edited in the page JSON. reusable-cores +9 rows (Glasgow ECP5 PLL solver, LUNA
  USB, FFT/I2S, PTP/AES67, SHA-256, HUB75, SDR chain, Wishbone intercon, nanoV). Pruned new clones (183 MB).
- **Why**: owner wants `docs/` to become a GitHub Pages site generated by scripts from JSON data (like the LPF
  catalogue), and asked to process the HX honourable mentions and the rest of the ECP5 recommended list as a test.
- **Notes**: Glasgow's revD board is ECP5 25F (not only iCE40). Several test harnesses are unittest/pdm, CMake or
  `$(VLOG)`-indirected and invisible to scan_make_tests.py (backlog item extended).

## 2026-09-28 — docs(reuse): add DFU guide, LPF catalogue and 15 reusable-core pages
- **What**: `docs/DFUs.md` (1 agent): USB DFU bootloaders and flows; ULX3S/ULX4M US2 bootloader from the newly cloned
  `emard__had2019-playground` (PicoRV32 + ECP5 USB core, 1d50:614b, alts 0–5, user image 0x200000, PROGRAMN reboot,
  recovery via ulx3s__hazard3-doom), plus OrangeCrab, Fomu, no2bootloader, pico-ice, BlackIce, Machdyne. 15 pages in
  `docs/projects/` (5 Sonnet agents, template + "Reusable blocks" tables): ulx3s-misc, ulx3s_examples, ulx3s_sms, f32c,
  hdl4fpga, silice, usb_cdc, smoldvi, ecp5_hdmi_audio_video, sdspi, picorv32, m6502, ice40-playground, ultraembedded
  orangecrab, hadbadge2019_fpgasoc. New `gen_lpf_catalogue.py` → `docs/lpf-catalogue.json` + `.md`: 883 LPFs, 455
  distinct, per-copy URL at the pinned commit, device + LUTs with evidence, board/rev by (signal, site) match against
  emard/ulx3s reference LPFs, chips from signal names, part numbers from comments. Catalogue row for had2019-playground
  (359 rows); license/reuse corrections from the reviews (ulx3s-misc, ulx3s_examples, ulx3s_sms, f32c, hdl4fpga,
  picorv32, sdspi, ice40-playground); reusable-cores (DVI MIT, SDRAM licenses, OSD, DFU row); projects.md registry,
  README start-here, MEMORY index, review skill.
- **Why**: owner asked for a DFU document, full docs pages for the most reusable gateware, and an LPF catalogue as JSON
  (URL, FPGA type, LUTs, board, rev, last update, chips).
- **Notes**: per-file dates are unknown in shallow clones, so the JSON gives the repo's pinned commit date. Pin-match
  board inference only covers ULX3S revisions; other boards come from path/catalogue keywords. One page agent's forks
  overwrote each other before reconciling; pages were checked for structure afterwards.

## 2026-09-28 — docs(repo): document clone pruning and the HX8K/HX4K batch in README, memory, skills
- **What**: README (scope now includes iCE40 HX8K/HX4K, HX survey status, a pruning paragraph + command after
  `--restore`, skills row); CLAUDE.md (prune after each clone batch and in the resume protocol); skills github-survey
  step 5 and review-gateware-project step 2 (prune after cataloguing); memory source-lists (HX batch + the 3 owner-named
  repos done), shallow-clones (link to prune-clones).
- **Why**: owner asked to bring README, memory and skills up to date after the prune + HX batch commits.

## 2026-09-28 — docs(catalogue): catalogue 19 iCE40 HX8K/HX4K repos and 3 pending rows
- **What**: wrote the 3 rows pending since the last session (gatecat__trellisboard ECP5 85F, mostly PCB + LiteX platform;
  zipcpu__sdspi vendor-neutral SD SPI/SDIO cores with ~60 formal proofs; toasterllc__mdccode iCE40 HX8K camera glue +
  MCU firmware). Shallow-cloned + pinned 19 of the 20 recommended repos of `docs/hx-boards-survey.md` (iceZ0mb1e skipped,
  already a submodule), fetched RISCBoy's `hdl/hazard5` and `hdl/libfpga` submodules; 5 Sonnet subagents wrote the rows
  incl. `make_tests`. catalogue.tsv 336 → 358 rows (= sources.tsv), docs/catalogue.md regenerated; counts in README,
  MEMORY, projects.md, reusable-cores.md (+5 rows: sdspi, picorv32/Hazard5, crtc6845, MiST scandoubler, iceboy);
  survey status line. Ran `prune.py --apply --all` on the new clones: 527 MB deleted, 15 GB free.
- **Why**: owner's handoff checklist steps 3–4 (approved HX8K/HX4K batch).
- **Notes**: wren6991__riscboy has a real ULX3S target (`synth/ULX3S.mk`, 85F) but its build scripts submodule
  (fpgascripts, not gateware) is not fetched. Test harnesses outside Makefiles (un0rick run_sim, MDCCode Sim.sh, icozip
  .sby) are in notes only; scanner backlog item extended. MDCCode `Sim/` is LTspice, not HDL.

## 2026-09-28 — skill(clone): add prune.py and prune non-gateware files from clones
- **What**: `.claude/skills/clone-original-source/prune.py` (dry run by default, `--apply`, `--all` or slugs) deletes
  bitstreams, build outputs (rpt/log/sdf/ncd/vcd, yosys JSON, trellis .config, icestorm .asc), tool binaries, PCB/3D
  files, documents, videos, images > 256 KiB, archives/disk images > 1 MiB (archives kept in sim/test dirs); never
  README/LICENSE or HDL/constraints/ROM files. Per-slug rules in `prune.tsv` (MDCCode: delete Tools/, Other/, keep
  Other/ExampleSDRAMControllers). Ran it: MDCCode 622 MB, then all clones 4.4 GB more; original_sources/ 9.3 → 4.5 GB,
  free disk 11.0 → 16.0 GB. Memory prune-clones.md, clone skill rule 8, MEMORY index updated.
- **Why**: owner rule (2026-09-28) to free disk before the HX8K/HX4K clone batch; clones themselves are never committed.
- **Notes**: `.git` packs are untouched (deletions are unstaged changes); re-run after each clone batch and `--restore`.
  Biggest wins: jderobot__fpga-robotics 1.1 GB of committed iCEcube/Diamond build outputs, f32c__fpgarduino 430 MB of
  toolchain archives.

## 2026-09-28 — chore(todo): add ordered start-of-session checklist for the next chat
- **What/why**: owner is restarting in a new chat; TODO now opens with the ordered handoff steps (prune clones, 3 missing
  rows, HX8K/HX4K batch).

## 2026-09-28 — docs(catalogue): add make_tests column, HX survey, prune rule; handoff
- **What**: `scan_make_tests.py` (candidate Makefile targets calling iverilog/vvp, verilator, ghdl, nvc, cocotb, sby,
  pytest, vunit, or a sub-make into sim/test dirs) flagged 112 of 336 repos; 5 Sonnet subagents read those Makefiles and
  wrote a `make_tests` value per repo (command, simulator, testbench files, self-checking vs waveform-only, or
  `none: <reason>`). Merged as the 15th column of catalogue.tsv (67 with a real make-run test); gen_catalogue.py shows
  and counts it. HX8K/HX4K board survey saved as `docs/hx-boards-survey.md` (20 recommended, not cloned yet). Cloned +
  pinned gatecat/TrellisBoard, ZipCPU/sdspi, toasterllc/MDCCode (963 MB shallow, mostly prebuilt tools), rows still to
  write. New owner rule in memory `prune-clones.md` (delete non-gateware files from local clones, never commit to them).
- **Why**: owner asked for testbenches run by Makefiles, HX8K/HX4K gateware, those three repos and a space-saving prune;
  then to save everything to memory, commit and push before restarting in a new session.
- **Notes**: a server-side classifier outage stopped the TrellisBoard/sdspi/MDCCode agent; the make_tests agents that ran
  during it were verified afterwards (all clones clean, 112 well-formed rows). sources.tsv has 339 pins vs 336 catalogue
  rows until those 3 rows are written. Scanner blind spots: Python orchestrators, default `all`/`run` targets, shell
  scripts. Several sim targets compile but never run (`vvp` missing) or reference testbenches absent from the clone.

## 2026-09-28 — docs(catalogue): catalogue 20 UP5K/ECP5 board repos from awesome-latticeFPGAs
- **What**: shallow-cloned the 20 "recommended" repos of `docs/lattice-boards-survey.md`, fetched 2 new gateware submodules
  (osmo-e1 `no2e1`, up5k_vga hoglet67 `verilog-6502`; other submodules were duplicates of cores already fetched, or
  frameworks/software), catalogued them with 4 Sonnet subagents (mixed-family brief). 316 → 336 rows: 18 non-ECP5
  (UP5K, some also LP8K/HX8K/Artix-7/Gowin), 2 ECP5 (greybadge25, machdyne fpga-dac). New reusable-cores rows (usb_cdc,
  SmolDVI, reDIP-SID, no2e1). README rewritten: what the repo is, "start here" table, catalogue scope, surveys,
  sources/restore, main files, workflow. `gen_catalogue.py` gains an optional `make_tests` column (filled next commit).
- **Why**: owner asked to clone, analyse and catalogue the 20, commit and push; and to refresh the README.
- **Notes**: alangarf/apple-one (upstream of lawrie's fork) spans 10 boards and 5 FPGA families, only IcePi Zero is ECP5.
  badgeteam/ and smunaut/ mch2022 repos overlap heavily without a visible fork link. nickmqb/fpga_craft is mostly
  Wyre HDL, not Verilog.

## 2026-09-28 — docs(survey): record gateware survey of awesome-latticeFPGAs boards
- **What**: `docs/lattice-boards-survey.md`: for each UP5K and ECP5 board in kelu124/awesome-latticeFPGAs not already
  covered, the gateware repos found (verified = .pcf/.lpf + HDL seen in the tarball listing), boards with none found,
  and a 20-repo clone-first list. Logged in `source-lists.md`, pointer in `MEMORY.md`, clone task in TODO.
- **Why**: owner asked to use their awesome-latticeFPGAs list to find gateware for UP5K and ECP5 boards.
- **Notes**: research only (1 subagent, 63 searches, 6 rate-limited retries). Two awesome-list links point to renamed repos
  (iCEboy → rniwase/tsuraraGB; SingularitySurfer → nkrackow/…); worth fixing in that list.

## 2026-09-28 — docs(catalogue): catalogue 8 iCE40 UP5K gateware repos from GitHub
- **What**: GitHub search (`up5k`, `icebreaker`, `ice40up5k`, `upduino`, topic `icebreaker`; Verilog, by stars) →
  cloned smunaut/ice40-playground, smunaut/iCE40linux, osresearch/up5k, bit-hack/icesid, bnossum/midgetv,
  kbob/icebreaker-candy, jamchamb/cojiro, wuxx/icesugar, plus 11 gateware submodules (no2usb, no2hyperbus, no2qpimem,
  no2memcache, no2hub75, no2ice40, no2misc under ice40-playground; osdvu; wuxx forks of up5k_6502, up5k-demos,
  iceZ0mb1e). Rows by 2 Sonnet subagents, FPGA column `iCE40 UP5K (NOT ECP5)`; 308 → 316. reusable-cores gets
  the no2fpga library, no2hyperbus (HyperRAM) and icesid rows.
- **Why**: owner asked for a few UP5K gateware examples from GitHub.
- **Notes**: iCE40linux uses the same no2 cores, fetched once under ice40-playground (its own pins not checked out).
  osresearch/up5k also has a tinyfpga-bx (iCE40 LP8K) target, midgetv an iceblink40 (HX1K) target and an iCEcube2 path.
  Search hit the unauthenticated rate limit, so the list is by stars, not exhaustive.

## 2026-09-27 — source(submodules): fetch gateware submodules and refresh their catalogue rows
- **What**: new `clone.sh --submodule <slug> <path> <reason>` (shallow, at the superproject's pinned commit, ssh URLs
  rewritten to https) and `.claude/memory/submodules.tsv` allowlist, re-fetched by `--restore`. Fetched 30 gateware
  submodules in 22 repos (USB, CPU, DDR3, HyperRAM, I2C/UART, sound, GPU cores); skipped frameworks, software, tests,
  KiCad libs and upstreams already cloned. 3 Sonnet agents rewrote the 21 affected rows (icetwang, damdoy covered by the iCE40 agent) (hdl, license, functions, reuse,
  notes, tests). Also added joshajohnson__ecp5-mini-projects and kbeckmann__pergola_projects (ECP5), and 4 iCE40 UP5K
  repos (iCEBreaker verilog-examples/workshop/icetwang from codeberg, damdoy__ice40_ultraplus_examples) with `NOT ECP5`
  in the FPGA column; `gen_catalogue.py` lists non-ECP5 repos in the summary. 302 → 308 rows. Memory: shallow-clones,
  catalogue-fields (family rule), reusable-cores (HyperRAM, USB device cores, nMigen DVI), source-lists; CLAUDE.md layout.
- **Why**: owner asked to allow submodules when explicitly gateware, then to add those files to the catalogue, and to
  add ecp5-mini-projects, pergola_projects, the iCEBreaker repos and damdoy's UP5K examples, marking the UP5K difference.
- **Notes**: licenses often differ between repo and submodule (e.g. mangelajo no license + GPL-3.0 USB core; ecpix-5
  GPL-2.0/LGPL-2.1/BSD). The remyciterin__dooom submodule was fetched then dropped (unused by its Makefile). icecrash
  (KiCad only) cloned then dropped. Nested submodules (z386 CPU, ACoreBase) still unfetched → TODO.

## 2026-09-27 — docs(catalogue): catalogue 14 gateware repos for other ECP5 boards
- **What**: shallow-cloned and pinned items 1–14 of the "recommended" list in `docs/ecp5-boards-survey.md`
  (OrangeCrab, iCESugar-Pro, HAD2019 badge, Colorlight, ECPIX-5, Versa ECP5-5G, IcePi Zero, LUNA). 12 are new; 2
  (`danodus__ecp5_hdmi_audio_video`, `wuxx__colorlight-fpga-projects`) were already catalogued at the same commit
  and their rows were replaced by the fuller new ones. Rows written by 3 parallel Sonnet agents from source, board
  recorded in `board_rev` as "(not ULX3S)"; 290 → 302 rows, 1:1 with `sources.tsv`. Added 6 rows to `reusable-cores.md`.
- **Why**: owner asked for ECP5 gateware from other boards, Verilog/open toolchain first, and then to clone
  and catalogue "the 14".
- **Notes**: corrected one agent claim (ULX3S has SDR SDRAM, not DDR3). Several USB cores are in git submodules not
  fetched by the shallow clone (TODO). `ultraembedded__orangecrab` and `ultraembedded__ecpix-5` ship no build
  script, so their toolchain/FPGA columns say `unknown`.

## 2026-09-27 — chore(catalogue): remove ULX5M-GS repos on owner request
- **What**: removed `intergalaktik__ulx5m-gs`, `goran-mahovlic__ulx5m-litex-ai`, `pu-cc__ulx5m_gpiocheck` from
  `catalogue.tsv`, `sources.tsv` and `original_sources/`; regenerated `docs/catalogue.md` (293 → 290); counts back
  to 290 in MEMORY/projects/README; survey group F marked "removed" and kept as a search record; ULX5M TODO dropped.
- **Why**: owner asked to remove the ULX5M-GS from the list (it is a GateMate board, outside the ECP5 scope).
- **Notes**: `ulx5m-board.md` memory kept as board knowledge, with the exclusion decision written at the top.

## 2026-09-27 — docs(survey): record GitHub survey of non-ULX3S ECP5 board gateware
- **What**: `docs/ecp5-boards-survey.md` — 114 repos for OrangeCrab, LUNA/Cynthion, iCESugar-Pro, Hackaday 2019
  badge, Colorlight, ButterStick, ECPIX-5, Logicbone, Versa/EVN and others (53 unauthenticated searches, ~85
  verified by reading the file list for `.lpf` + HDL), plus litex-boards/amaranth-boards platform names and a
  24-repo "clone first" list. Logged in `source-lists.md`, pointer in `MEMORY.md`.
- **Why**: owner asked for gateware for other ECP5 boards, Verilog and open toolchain first, as reuse sources.
- **Notes**: research only (one background agent); nothing cloned yet — waiting for the owner to pick, disk 94 % full.

## 2026-09-27 — memory(repo): refresh README repo count after the ULX5M additions
- **What/why**: README still said 290 repos; now 293 (290 ULX3S/ULX4M + 3 ULX5M).

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
