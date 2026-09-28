---
name: prune-clones
description: Owner rule: local clones in original_sources/ may be pruned of non-gateware files (prebuilt tools, bitstreams, hardware design files, datasheets, large images) to save disk; never commit to the clones
metadata:
  type: feedback
---

Files and folders in `original_sources/<slug>/` that are **not gateware-related** may be deleted locally to save space
(owner, 2026-09-28): prebuilt tools/toolchains, prebuilt bitstreams (.bit/.svf/.dfu/.jed), hardware design files
(KiCad/Eagle/Altium/Gerber, 3D models .step/.stp/.wrl/.stl), datasheets and other PDFs, large images, videos, archives
of binaries. Then **report how much space it saved**. **Never commit to the clones** (deletions stay as unstaged
working-tree changes).

Always keep: HDL (.v/.sv/.vh/.vhd, Amaranth/LiteX/Migen .py, .scala, .bsv, .si…), constraint files (.lpf/.pcf/.ccf/.xdc),
Makefiles/build scripts, testbenches and sim harnesses, ROM/memory-init files (.hex/.mem/.bin/.mif/.coe) and firmware
sources built into the bitstream, READMEs and LICENSE/COPYING files (licenses are catalogued).

**Why:** disk was 95 % full (11 GB free) after ~340 clones; e.g. toasterllc__mdccode is 963 MB shallow (Tools/ 441 MB
prebuilt toolchains, Other/ 189 MB) while its gateware is under Code/ICE40 (a few MB).

**How to apply:** run `.claude/skills/clone-original-source/prune.py [--apply] (--all | <slug>...)` (dry run by
default). Generic rules by extension/size/content live in the script; per-slug folders (delete/keep) in `prune.tsv`
next to it (`keep` wins). First run 2026-09-28: 5.0 GB of working-tree files deleted (MDCCode 622 MB, then all clones
4.4 GB: build outputs 1.36 GB, bitstreams 0.75, images 0.75, archives 0.56, documents 0.39, PCB 0.22…);
original_sources/ 9.3 → 4.5 GB, free disk 11.0 → 16.0 GB. Deleting working-tree files does not shrink `.git`. When
checking a clone is unmodified, ignore deletions (`git status --porcelain | grep -v '^ D'`). **Re-run `prune.py
--apply` after every new clone batch and after `clone.sh --restore`.** Don't prune while subagents are reading the
clones. See also [[shallow-clones]].
