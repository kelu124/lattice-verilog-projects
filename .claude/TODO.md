# TODO

## Start here next session (handoff 2026-09-28, in this order)
1. Resume protocol (CLAUDE.md). Check `git status` is clean and `df -h /` (~11 GB free on 2026-09-28).
2. ~~Prune clones~~ done 2026-09-28 (prune.py, 5 GB freed).
3. **Write the 3 missing catalogue rows** (gatecat__trellisboard, zipcpu__sdspi, toasterllc__mdccode): sources.tsv has 339
   pins vs 336 rows. One subagent, mixed-family rules (`NOT ECP5` for non-ECP5), fill `make_tests` via scan_make_tests.py.
4. **HX8K/HX4K batch** (owner approved): clone the 20 recommended repos of `docs/hx-boards-survey.md` minus
   abnoname/iceZ0mb1e; fetch gateware-only submodules (`clone.sh --submodule`); catalogue with ~4 subagents (5 repos each),
   FPGA column `iCE40 HX8K (NOT ECP5)` / `iCE40 HX4K (NOT ECP5)`, plus `make_tests`; merge, regenerate, update counts in
   README/MEMORY/projects/reusable-cores, commit, push.
5. Then continue with "Next" below.

## In progress

## Next
- [ ] Write catalogue rows for gatecat__trellisboard, zipcpu__sdspi, toasterllc__mdccode (cloned + pinned 2026-09-28; the agent was stopped by a classifier outage). For MDCCode look only at Code/ICE40, Sim, Other/ExampleSDRAMControllers; run scan_make_tests.py for make_tests. Mixed-family brief rules: non-ECP5 rows say `NOT ECP5` (added 2026-09-28)
- [ ] Clone + catalogue the 20 recommended repos of docs/hx-boards-survey.md (owner approved; skip abnoname/iceZ0mb1e; FPGA column `iCE40 HX8K (NOT ECP5)`; fetch gateware submodules only; fill make_tests too) (added 2026-09-28)
- [ ] Write full docs pages for the most reusable repos: emard__ulx3s-misc, lawrie__ulx3s_examples, f32c__f32c, sylefeb__silice, hdl4fpga__hdl4fpga (only catalogued so far) (added 2026-09-27)
- [ ] Clone the remaining candidates in projects.md (litex-boards, SaxonSoc, neorv32-setups, fujprog, had2019-playground, ulx4m-ls) (added 2026-09-27)
- [ ] Harvest the "Gitee examples" section of ulx3s.github.io (added 2026-09-27)
- [ ] Build a wider list of ULX3S projects: GitHub search "ulx3s", topic `ulx3s`, Hackaday/Crowd Supply pages, radiona.org (added 2026-09-27)

## Backlog
- [ ] scan_make_tests.py blind spots: tests run via Python orchestrators (Hazard3 test/sim/test.py), default `all`/`run` targets, shell scripts (apple-one tools/iverilog/*.sh); extend it (added 2026-09-28)
- [ ] scan_tests.sh misses CMake/Verilator harnesses (CMakeLists.txt, verilator/ dirs), e.g. bit-hack__icesid; extend it and re-run (added 2026-09-28)
- [ ] Clone items 15–24 (except 21, done) of the "recommended" list in docs/ecp5-boards-survey.md if wanted (added 2026-09-27)
- [ ] Nested gateware submodules not fetched (clone.sh --submodule only takes top-level paths): z386 CPU (gojimmypi__z80386-ulx3s-doom third_party/z386_MiSTer/src/z386), ACoreBase CPU (chiplet__acorechip-ulx3s ACoreChip/…) (added 2026-09-27)
- [ ] Consider cloning markus-zzz/hyperram-test (ULX3S HyperRAM add-on test, github-survey group C) (added 2026-09-27)
- [ ] gen_catalogue.py / docs/catalogue.md intro are ULX3S-worded; consider a `board` column now that non-ULX3S ECP5 repos are in (board currently in `board_rev`) (added 2026-09-27)
- [ ] Clone/catalogue the remaining ~78 GitHub-survey repos (group C multi-board, group E minus ULX4M) if wanted (added 2026-09-27)
- [ ] Record history stats (first commit, commit count) for the 155+64=219 GitHub-survey repos in history.tsv via GitHub API (added 2026-09-27)
- [ ] Spot-check a sample of the heuristic test-scan results (tests column) by hand; the scan is name/path only, not proof tests run or pass (added 2026-09-27)
- [ ] Find the sources of the ulx3s-bin demos with unknown origin: memtest, emi, oled, rtc, usb, c64, oberon, flashblink (added 2026-09-27)
- [ ] Check whether openFPGALoader `ulx3s_esp` (ESP32-S3 USB-JTAG) works, and on which hardware (added 2026-09-27)
- [ ] Verify catalogue rows by actually building a sample per toolchain (e.g. ulx3s-misc dvi, nes_ecp5, lawrie sms), if oss-cad-suite is installed (added 2026-09-27)
- [ ] Check which Diamond-only projects (f32c, minimig, papilio-arcade, hdl4fpga…) can be built with ghdl-yosys-plugin (added 2026-09-27)
- [ ] ironsteel__nes_ecp5 README (2026-01) says OSD game load is broken: check whether emard fork works (added 2026-09-27)
- [ ] Read emard/ulx3s `doc/TODO.txt` and record known hardware issues (added 2026-09-27)
- [ ] Diff ulx3s_v20.lpf against v316.lpf and document per-signal changes for porting designs (added 2026-09-27)
- [ ] Write docs/function-catalogue.md: per function tag, which projects provide a reusable core (added 2026-09-27)
- [ ] Decide whether to check that example builds pass with a local oss-cad-suite (is it installed?) (added 2026-09-27)

## Blocked
- [ ] Authenticated GitHub code search (`filename:ulx3s_v20.lpf`) to find repos that never say "ulx3s" in name/README (blocked: needs `gh auth login`) (added 2026-09-27)
