---
name: catalogue-fields
description: The owner requires every gateware repo in the catalogue (projects.md) to record FPGA size(s), toolchain (Lattice Diamond vs open-source), HDL language (Verilog/VHDL/…) and license.
metadata:
  type: feedback
---

For every gateware repo, the catalogue [[projects]] must say:
1. **FPGA**: which ECP5 size(s) it targets/supports (12F/25F/45F/85F…).
   If the target is **not an ECP5**, the column must start with the family and "(NOT ECP5)", e.g.
   `iCE40 UP5K (NOT ECP5) - SG48` (iCEBreaker, owner request 2026-09-27) or `Xilinx XC7A50T (NOT ECP5)`.
   iCE40 designs use SB_* primitives (SB_PLL40, SB_SPRAM256KA, SB_RGBA_DRV, SB_IO) and must be ported for ECP5.
2. **Toolchain**: Lattice Diamond (`diamond`), the open-source flow (`open`: yosys + nextpnr-ecp5 +
   ecppack, also via LiteX/apio/ghdl plugin), or `both`.
3. **HDL**: Verilog, VHDL, SystemVerilog, or generator language (SpinalHDL, Migen/LiteX, Silice…).
4. **License**: SPDX id (look for LICENSE/COPYING at any depth, README, file headers); `none found` if
   absent. That means *all rights reserved* by default, which matters for reuse. The owner explicitly
   praised keeping licenses (2026-09-27): keep doing it.
5. **Tests**: any testbench/simulation setup found (test/sim dirs, testbench-named files, simulator
   mentions). `none found` if nothing turns up. Owner asked for this on 2026-09-27 too — a heuristic
   name/path scan is enough (`scan_tests.sh`), it doesn't need to confirm the tests pass.

**Why:** asked explicitly by the repo owner on 2026-09-27 (license added the same day). These are the first filters someone
uses to decide whether a design can be reused (their chip size, their toolchain, their language).

**How to apply:** always fill these five columns in the summary table; write `unknown` if not
determinable, never guess. The skill `review-gateware-project` step 5b spells out how to detect them.
