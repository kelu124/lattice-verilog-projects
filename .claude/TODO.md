# TODO

## In progress

## Next
- [ ] Clone + catalogue the 24 "recommended to clone first" non-ULX3S ECP5 repos in docs/ecp5-boards-survey.md (waiting for owner go-ahead; ~14 GB disk free) (added 2026-09-27)
- [ ] Write full docs pages for the most reusable repos: emard__ulx3s-misc, lawrie__ulx3s_examples, f32c__f32c, sylefeb__silice, hdl4fpga__hdl4fpga (only catalogued so far) (added 2026-09-27)
- [ ] Clone the remaining candidates in projects.md (litex-boards, SaxonSoc, neorv32-setups, fujprog, had2019-playground, ulx4m-ls) (added 2026-09-27)
- [ ] Harvest the "Gitee examples" section of ulx3s.github.io (added 2026-09-27)
- [ ] Build a wider list of ULX3S projects: GitHub search "ulx3s", topic `ulx3s`, Hackaday/Crowd Supply pages, radiona.org (added 2026-09-27)

## Backlog
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
