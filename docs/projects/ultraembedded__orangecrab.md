---
title: "ultraembedded__orangecrab"
parent: "Project reviews"
nav_order: 15
---
<!-- Generated from data/projects/ultraembedded__orangecrab.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# OrangeCrab DDR3 memory test (`ultraembedded__orangecrab`)

| Field | Value |
|---|---|
| Upstream | https://github.com/ultraembedded/orangecrab |
| Reviewed at | `685d601` (upstream date 2020-08-21), reviewed 2026-09-28 |
| License | Apache-2.0 (`LICENSE`, root; matches per-file headers in `ddr_test/src_v/ddr3_*.v` and `ram_tester.v`); `ecp5pll.sv` is separately BSD (`(c)EMARD / License=BSD` header, `ddr_test/src_v/ecp5pll.sv:1-2`) |
| HDL / framework | Verilog (11 files) + 1 SystemVerilog file (`ecp5pll.sv`) |
| Toolchain | unknown — no Makefile/build script in this shallow clone. Plain synthesizable Verilog/SV and the `ecp5pll.sv`/Trellis-primitive style strongly suggest yosys + nextpnr-ecp5 + ecppack, but this is unconfirmed (no tool invocation found) |
| Programmer | unknown — inferred `dfu-util`/`openFPGALoader --dfu` from the prebuilt `ddr_test/bitstreams/ddr_test_r0_2.dfu` recorded in the original commit (`git show 685d601 --stat`); that file was deleted by this repo's local prune (non-gateware build output) so it is not present in the clone |
| Target FPGA(s) | unknown — no `--25k`/`--85k` device flag anywhere in source; OrangeCrab r0.2 boards ship with either LFE5U-25F or LFE5U-45F/85F depending on order option, not stated here |
| Board revision(s) | OrangeCrab r0.2 (`ddr_test/src_v/orangecrab_r0_2.lpf`, `LOCATE COMP` pin names throughout) |
| Activity | single commit at the pinned clone depth (shallow, `--depth 1`); upstream date 2020-08-21; commit count/first commit unknown (history.tsv has no entry) |

## What the gateware does

A **DDR3 128 MB read/write memory test** for the OrangeCrab r0.2 board, top module `top`
(`ddr_test/src_v/top.v`):

- Drives the on-board DDR3 through a full AXI4 test (`ram_tester.v`, top `ram_tester`):
  writes all 128 MB, reads it back and verifies twice, using incrementing patterns and an
  all-ones pattern (per `README.md`).
- Not tested (per README): the DM (data-mask) pins, and high-speed PCB routing — the test
  runs the DDR clock at only 24 MHz.
- Status is shown on the on-board RGB LED: blue = test in progress, red = failed, green = pass
  (`top.v`, `rgb_led_r/g/b` outputs wired from `status_busy_o`/`status_err_o`).

## Structure

- `ddr_test/src_v/top.v` — top level: instantiates `ecp5pll`, `reset_gen`, `fpga_top` (which
  wraps `ram_tester` + `ddr3_axi`), and drives the LEDs from test status.
- `ddr_test/src_v/fpga_top.v` — glue between `ram_tester` (AXI4 master, test sequencer) and
  `ddr3_axi` (AXI4 slave, DDR3 controller), connected over a plain AXI4 bus with `cfg_*`
  register access for `ram_tester`'s test parameters.
- `ddr_test/src_v/ddr3_axi.v` → `ddr3_axi_core.v` (state machine, `DDR_MHZ` parameter) →
  `ddr3_axi_retime.v` (clock-domain retiming) → `ddr3_dfi_seq.v` (JEDEC DFI command
  sequencer) → `ddr3_dfi_phy.v` (the ECP5 I/O PHY). `ddr3_axi_pmem.v` is a second,
  simpler AXI4↔DFI path (present but not wired into `top.v`; not verified whether any
  target uses it).
- `ddr_test/src_v/ecp5pll.sv` — parametric ECP5 `EHXPLLL` wrapper, by the same author
  (EMARD) as the ULX3S board files.
- `ddr_test/src_v/orangecrab_r0_2.lpf` — pin/frequency constraints for OrangeCrab r0.2 only.
- No `Makefile`, no `.pcf`/nextpnr invocation, no testbench in this clone.

## How to build

Not run. No build script exists in the repository at the pinned commit — only the
prebuilt `ddr_test/bitstreams/ddr_test_r0_2.dfu` (added in the same commit, and pruned
from this local clone as a non-gateware build artifact). Anyone reusing this needs to
write their own yosys/nextpnr-ecp5/ecppack flow from scratch.

## Reuse notes

### Reusable blocks

| Block | Path | Top module | Language | Vendor primitives | License |
|---|---|---|---|---|---|
| DDR3 AXI4 controller | `ddr_test/src_v/ddr3_axi.v` (+ `ddr3_axi_core.v`, `ddr3_axi_retime.v`, `ddr3_dfi_seq.v`, `ddr3_dfi_phy.v`) | `ddr3_axi` | Verilog | `ddr3_dfi_phy.v` only: `ODDRX1F`, `IDDRX1F`, `BB` (bidir buffer) — no `DQSBUFM`/`DELAYF`, i.e. it does **not** use ECP5's dedicated DQS/hardware read-training block, just plain DDR IO registers | Apache-2.0 |
| Alternate AXI4↔DFI path (unused in `top.v`) | `ddr_test/src_v/ddr3_axi_pmem.v` | `ddr3_axi_pmem` | Verilog | none checked (not wired into any target here) | Apache-2.0 |
| Parametric ECP5 PLL | `ddr_test/src_v/ecp5pll.sv` | `ecp5pll` | SystemVerilog | `EHXPLLL` (in `EHXPLLL`-wrapping logic, not shown inline in this file but referenced by the same author's other ULX3S PLL cores) | BSD (EMARD) |
| AXI4 memory-test engine | `ddr_test/src_v/ram_tester.v` | `ram_tester` | Verilog | none (pure logic: LFSR pattern generator `ram_lfsr`, `generic_fifo`) | Apache-2.0 |

- **`ddr3_axi` DDR3 controller** is the main reason this repo is catalogued: it is a
  complete, self-contained "Lightweight DDR3 Memory Controller V0.1" (Ultra-Embedded.com,
  2020) that only needs `ODDRX1F`/`IDDRX1F`/`BB` — all present on every ECP5, not limited to
  the 45F/85F. It is **not applicable to a stock ULX3S board**, which has SDR SDRAM, not
  DDR3; it targets DDR3 add-on/alternate boards only (per `reusable-cores.md`).
  Clock assumptions: `top.v` feeds it a 48 MHz `clk48` input, `ecp5pll` derives a 24 MHz
  system clock (`out0_hz=24000000`) and a 24 MHz DDR clock at 90° phase
  (`out1_hz=24000000, out1_deg=90`) — i.e. this instance runs the DDR3 interface at a very
  conservative `DDR_MHZ=24` (`fpga_top.v:139`). To reuse at a higher, production DDR3
  speed the PHY delay calibration (`DQ_IN_DELAY_INIT` parameter, `ddr3_dfi_phy.v`) and
  timing parameters (`TPHY_RDLAT`/`TPHY_WRLAT`) would need re-tuning; this repo does not
  demonstrate a fast configuration.
- Reused device pins are OrangeCrab r0.2-specific (`ddram_a[0:15]`, `ddram_ba[0:2]`,
  `ddram_dq[0:15]`, `ddram_dqs_p[0:1]`, etc., `orangecrab_r0_2.lpf`); a new board needs a
  full LPF rewrite mapping these AXI/DFI ports to its own DDR3 pinout.
- **`ecp5pll.sv`** is a drop-in for any ULX3S design already using EMARD's parametric PLL
  elsewhere in the collection (`emard__ulx3s-misc examples/ecp5pll`); this copy is
  functionally the same generator.
- `ram_tester.v` is a generic AXI4 read/write/verify engine, independent of DDR3 — could be
  reused to soak-test any AXI4 memory (e.g. an SDRAM controller wrapped in AXI4) on ULX3S.
- Dependencies: none outside this directory (no submodules, no external IP).

## Open questions

- Exact target FPGA size for OrangeCrab r0.2 (25F vs 45F/85F) is not stated in source.
- No confirmed toolchain invocation (yosys/nextpnr flags, `--package`/`--device`) exists in
  this repo; unverified whether the deleted `.dfu` bitstream was built with default or
  tuned nextpnr settings.
- `ddr3_axi_pmem.v` purpose/usage vs. `ddr3_axi.v` not investigated further (not on the
  path exercised by `top.v`).
- Commit count / first-commit date for full-history stats not recorded in
  `.claude/memory/history.tsv`.
{% endraw %}
