---
title: "JTAG and debug"
parent: "Cores by function"
nav_order: 20
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# JTAG and debug

User JTAG access, debug bridges, logic analysers.

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [OpenCores JTAG TAP + JTAGG bridge](#core-emard-jtag-slave) ★ | [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc) | Verilog | LGPL-2.1-or-later | ECP5 | 0 |
| [ECP5 JTAGG demo (Ecp5JtagDemo)](#core-tomverbeure-ecp5-jtag) | [tomverbeure__ecp5_jtag](https://github.com/tomverbeure/ecp5_jtag) | Verilog | none found | ECP5 | 0 |
| [eSPI bus capture + packet decoder](#core-johnazoidberg-espi-analyzer) | [johnazoidberg__ulx3s-espi-analyzer](https://github.com/JohnAZoidberg/ulx3s-espi-analyzer) | Verilog | none found | ECP5 | 0 |
| [OpenDAP SW-DP + Mem-AP (SWD debug probe)](#core-opendap-sw-dp) | [wren6991__hazard3-swd-soc](https://github.com/Wren6991/Hazard3-SWD-SoC) | Verilog | CC0-1.0 (file header + submodule LICENSE) | any | 0 |
| [SUMP logic analyzer core (ECP5-ported)](#core-lawrie-ice40logicsniffer) | [lawrie__ice40logicsniffer](https://github.com/lawrie/Ice40LogicSniffer) | Verilog | GPL-2.0-or-later | ECP5 | 0 |

## Cores

### OpenCores JTAG TAP + JTAGG bridge (best) {#core-emard-jtag-slave}

Generic OpenCores JTAG TAP (jtag_slave.v, vendor-neutral) plus a demo top that bridges it through the ECP5 JTAGG primitive so user logic gets its own JTAG chain via the board's existing FTDI/ESP32 JTAG.

| | |
|---|---|
| Repository | [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc): ULX3S misc/advanced examples: EMARD's building-block library |
| Files | [`examples/jtag_slave/hdl/jtag_slave.v`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/jtag_slave/hdl/jtag_slave.v), [`examples/jtag_slave/hdl/jtag_slave_clk.v`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/jtag_slave/hdl/jtag_slave_clk.v), [`examples/jtag_slave/hdl/tap_defines.v`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/jtag_slave/hdl/tap_defines.v), [`examples/jtag_slave/hdl/top/top_jtagg_slave.v`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/jtag_slave/hdl/top/top_jtagg_slave.v) |
| Top module | `jtag_slave` |
| Language | Verilog |
| License | LGPL-2.1-or-later (jtag_slave.v OpenCores tap_top.v header, Igor Mohor/Nathan Yawn); top_jtagg_slave.v: none found |
| FPGA / primitives | ECP5: `JTAGG`, `ODDRX1F` |
| Tests | none found |

**On ULX3S:** top_jtagg_slave.v is a real ULX3S example (clk_25mhz, btn/led/oled/gpdi ports); ODDRX1F instances are only in the demo's DVI/OLED wiring, not the TAP itself.

Full review: [emard__ulx3s-misc](../projects/emard__ulx3s-misc.md).

### ECP5 JTAGG demo (Ecp5JtagDemo) {#core-tomverbeure-ecp5-jtag}

Minimal, well-documented instantiation of the ECP5 JTAGG primitive with a reverse-engineering write-up of its TCK/TDI/TDO timing.

| | |
|---|---|
| Repository | [tomverbeure__ecp5_jtag](https://github.com/tomverbeure/ecp5_jtag): Colorlight i5: reverse-engineering notes plus a SpinalHDL/Verilog example demonstrating the Lattice ECP5… |
| Files | [`verilog/top.v`](https://github.com/tomverbeure/ecp5_jtag/blob/6a2302e079d003ddce8335a5300172fdbb2bd1b5/verilog/top.v), [`tb/src/JTAGG.v`](https://github.com/tomverbeure/ecp5_jtag/blob/6a2302e079d003ddce8335a5300172fdbb2bd1b5/tb/src/JTAGG.v) |
| Top module | `Ecp5JtagDemo` |
| Language | Verilog |
| License | none found |
| FPGA / primitives | ECP5: `JTAGG` |
| Tests | tb/ iverilog testbench, waveform-only ($dumpvars, no PASS/FAIL) |

**On ULX3S:** Built for a Colorlight i5 (ECP5-25F); pin remap only needed to reuse on ULX3S.

### eSPI bus capture + packet decoder {#core-johnazoidberg-espi-analyzer}

eSPI (Enhanced SPI) bus signal capture with CDC double-registering and single/dual/quad IO decode, plus a packet decoder pipeline.

| | |
|---|---|
| Repository | [johnazoidberg__ulx3s-espi-analyzer](https://github.com/JohnAZoidberg/ulx3s-espi-analyzer): JohnAZoidberg/ulx3s-espi-analyzer: passive eSPI bus sniffer/analyzer for ULX3S |
| Files | [`hdl/espi_capture.v`](https://github.com/JohnAZoidberg/ulx3s-espi-analyzer/blob/4331dbd4b0e6ebab2096a4f797b0dafb9f7fe1a5/hdl/espi_capture.v), [`hdl/espi_packet_decoder.v`](https://github.com/JohnAZoidberg/ulx3s-espi-analyzer/blob/4331dbd4b0e6ebab2096a4f797b0dafb9f7fe1a5/hdl/espi_packet_decoder.v) |
| Top module | `espi_capture` |
| Language | Verilog |
| License | none found (repo-wide; only ecp5pll.sv credited BSD to EMARD) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | none found |

**On ULX3S:** Nix-flake reproducible ULX3S build (default 12F, also 25/45/85); a purpose-built protocol logic analyzer, not a generic one.

### OpenDAP SW-DP + Mem-AP (SWD debug probe) {#core-opendap-sw-dp}

ADIv5.2 SW-DP (Serial Wire Debug) and APB Mem-AP implementation: an alternative to JTAG for debugging soft cores.

| | |
|---|---|
| Repository | [wren6991__hazard3-swd-soc](https://github.com/Wren6991/Hazard3-SWD-SoC): Example SoC: Hazard3 RISC-V core + OpenDAP SWD debug port + SRAM/UART/timer |
| Files | [`lib/opendap/hdl/opendap_sw_dp.v`](https://github.com/Wren6991/Hazard3-SWD-SoC/blob/6f3bfe190a9dd20185913ec8e97bd2eaea75a788/lib/opendap/hdl/opendap_sw_dp.v), [`lib/opendap/hdl/opendap_mem_ap_apb.v`](https://github.com/Wren6991/Hazard3-SWD-SoC/blob/6f3bfe190a9dd20185913ec8e97bd2eaea75a788/lib/opendap/hdl/opendap_mem_ap_apb.v) |
| Top module | `opendap_sw_dp` |
| Language | Verilog |
| License | CC0-1.0 (file header + submodule LICENSE) |
| FPGA / primitives | any: none (portable) |
| Tests | lib/opendap/test/{dp,dap}/testcase (cxxrtl, self-checking tb_assert) |

**On ULX3S:** Repo's own README calls the SoC experimental ("no idea how to program it"); the DP/Mem-AP cores themselves are standalone and CC0.

### SUMP logic analyzer core (ECP5-ported) {#core-lawrie-ice40logicsniffer}

Classic openbench SUMP-protocol logic analyzer (sampler, RLE encoder, trigger, BRAM ring buffer) already re-targeted to ECP5 via ecp5_pll.v (an SB_PLL40_CORE version, pll.v, also exists for iCE40).

| | |
|---|---|
| Repository | [lawrie__ice40logicsniffer](https://github.com/lawrie/Ice40LogicSniffer): Open Bench Logic Sniffer |
| Files | [`src/Logic_Sniffer.v`](https://github.com/lawrie/Ice40LogicSniffer/blob/f37cc11f4023a6821fa296d0d4f4ceb480361add/src/Logic_Sniffer.v), [`src/core.v`](https://github.com/lawrie/Ice40LogicSniffer/blob/f37cc11f4023a6821fa296d0d4f4ceb480361add/src/core.v), [`src/sampler.v`](https://github.com/lawrie/Ice40LogicSniffer/blob/f37cc11f4023a6821fa296d0d4f4ceb480361add/src/sampler.v), [`src/rle_enc.v`](https://github.com/lawrie/Ice40LogicSniffer/blob/f37cc11f4023a6821fa296d0d4f4ceb480361add/src/rle_enc.v), [`src/trigger.v`](https://github.com/lawrie/Ice40LogicSniffer/blob/f37cc11f4023a6821fa296d0d4f4ceb480361add/src/trigger.v), [`src/ecp5_pll.v`](https://github.com/lawrie/Ice40LogicSniffer/blob/f37cc11f4023a6821fa296d0d4f4ceb480361add/src/ecp5_pll.v) |
| Top module | `Logic_Sniffer` |
| Language | Verilog |
| License | GPL-2.0-or-later (file headers, Copyright 2006 Michael Poppitz) |
| FPGA / primitives | ECP5: `EHXPLLL` |
| Tests | src/Logic_Sniffer_tb.v present, not confirmed self-checking |

**On ULX3S:** Built --25k with an idcode for 12F in this repo; BRAM-based capture buffer, not SDRAM-backed.

## Other catalogued projects

Catalogued repos tagged `jtag` (41), `debug-bridge` (4), `logic-analyzer` (12), `debug-instrument` (1) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
