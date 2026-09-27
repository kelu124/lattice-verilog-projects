---
name: catalogue-fields
description: The owner requires every gateware repo in the catalogue (projects.md) to record FPGA size(s), toolchain (Lattice Diamond vs open-source), HDL language (Verilog/VHDL/…) and license.
metadata:
  type: feedback
---

For every gateware repo, the catalogue [[projects]] must say:
1. **FPGA**: which ECP5 size(s) it targets/supports (12F/25F/45F/85F…).
2. **Toolchain**: Lattice Diamond (`diamond`), the open-source flow (`open`: yosys + nextpnr-ecp5 +
   ecppack, also via LiteX/apio/ghdl plugin), or `both`.
3. **HDL**: Verilog, VHDL, SystemVerilog, or generator language (SpinalHDL, Migen/LiteX, Silice…).
4. **License**: SPDX id (look for LICENSE/COPYING at any depth, README, file headers); `none found` if
   absent. That means *all rights reserved* by default, which matters for reuse. The owner explicitly
   praised keeping licenses (2026-09-27): keep doing it.

**Why:** asked explicitly by the repo owner on 2026-09-27 (license added the same day). These are the first filters someone
uses to decide whether a design can be reused (their chip size, their toolchain, their language).

**How to apply:** always fill these four columns in the summary table; write `unknown` if not
determinable, never guess. The skill `review-gateware-project` step 5b spells out how to detect them.
