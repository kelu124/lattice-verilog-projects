---
name: catalogue-fields
description: The owner requires every gateware repo in the catalogue (projects.md) to record FPGA size(s), toolchain (Lattice Diamond vs open-source), and HDL language (Verilog/VHDL/…).
metadata:
  type: feedback
---

For every gateware repo, the catalogue [[projects]] must say:
1. **FPGA**: which ECP5 size(s) it targets/supports (12F/25F/45F/85F…).
2. **Toolchain**: Lattice Diamond (`diamond`), the open-source flow (`open`: yosys + nextpnr-ecp5 +
   ecppack, also via LiteX/apio/ghdl plugin), or `both`.
3. **HDL**: Verilog, VHDL, SystemVerilog, or generator language (SpinalHDL, Migen/LiteX, Silice…).

**Why:** asked explicitly by the repo owner on 2026-09-27. These are the first filters someone
uses to decide whether a design can be reused (their chip size, their toolchain, their language).

**How to apply:** always fill these three columns in the summary table; write `unknown` if not
determinable, never guess. The skill `review-gateware-project` step 5b spells out how to detect them.
