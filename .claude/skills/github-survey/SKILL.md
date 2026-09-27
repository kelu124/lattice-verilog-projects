---
name: github-survey
description: Repeat or extend the GitHub-wide search for ULX3S gateware repos (repo/topic/readme/fork queries, evidence check, diff against sources.tsv). Use when asked to find more ULX3S projects or refresh docs/github-survey.md.
---

# GitHub survey for ULX3S repositories

Last run: 2026-09-27 → `docs/github-survey.md` (≈297 candidates in groups A–E).

## Queries (GitHub search API, `sort=updated`)
- `ulx3s` · `topic:ulx3s` · `ulx3s in:readme` (all pages) · `ulx3s fork:only` · `ulx3s in:description fork:true`
- `ulx4m` · `ecp5 hdmi` · `ecp5 dvi` · `radiona` (noisy)
- Community link lists: RadionaOrg/ulx3s-links, lawrie/ulx3s_cores, lawrie/ulx3s_retro, ulx3s/ulx3s.github.io
- **Not done yet (needs auth)**: code search `filename:ulx3s_v20.lpf`, `"clk_25mhz" "gpdi_dp"`. Run
  `gh auth login` first (gh was not installed on 2026-09-27; unauthenticated API: search 10/min,
  1000 results/query, core 60/h).

## Evidence levels
- **A (verified)**: a ULX3S `.lpf`, top or `ulx3s/` board dir exists (`tree:` recursive tree, `root:` top listing).
- **B**: ULX3S-dedicated by name/description/topic, HDL present, no LPF at root.
- **C**: multi-board, README states a ULX3S target.
- **D**: forks with substantial own commits.
- **E**: linked from ulx3s-links, relevance to check.

## Procedure
1. Run the queries and collect `full_name, language, stars, pushed_at, license, fork`.
2. Drop anything whose slug (`owner__repo`, lowercase) is already in `.claude/memory/sources.tsv`.
3. Check the evidence (repo tree or the github.com root listing; raw README grep for "ulx3s").
4. Regenerate `docs/github-survey.md`, and log the run in `.claude/memory/source-lists.md`.
5. Clone the chosen ones with the `clone-original-source` skill, then catalogue them (review skill, step 7b).
   **Check free disk space first** (`df -h`): on 2026-09-27 the disk was 98 % full.
