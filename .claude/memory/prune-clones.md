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

**How to apply:** not done yet (TODO): write `.claude/skills/clone-original-source/prune.sh` (dry-run by default,
`--apply` to delete, per-slug or `--all`), run it, log working-tree and total savings. Deleting working-tree files does
not shrink `.git` (the shallow pack keeps compressed blobs), so report both numbers. When checking a clone is unmodified,
ignore deletions (`git status --porcelain | grep -v '^ D'`). `--restore` re-creates full clones: re-run the prune after.
Don't prune while subagents are reading the clones. See also [[shallow-clones]].
