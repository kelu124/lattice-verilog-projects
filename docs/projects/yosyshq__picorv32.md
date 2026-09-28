# PicoRV32 (`yosyshq__picorv32`)

| Field | Value |
|---|---|
| Upstream | https://github.com/YosysHQ/picorv32 |
| Reviewed at | `ef203c2` (upstream date 2026-09-07), reviewed 2026-09-28 |
| License | ISC (`COPYING`; per-file headers, e.g. `picorv32.v:1-17`) |
| HDL / framework | Verilog (41 `.v` files: `picorv32.v` core + `picosoc/`, `scripts/*`, `tests/*.S` assembly) |
| Toolchain | `open` for the two shipped board demos: yosys + nextpnr-ice40 + icepack (`picosoc/Makefile`). Also has proprietary-flow benchmarking scripts for Xilinx Vivado (`scripts/vivado`) and Intel/Altera Quartus (`scripts/quartus`), neither board-specific. **No ECP5/ULX3S flow is shipped anywhere in the repo** (verified: no `.lpf` file, no `synth_ecp5`/`nextpnr-ecp5` reference found) |
| Programmer | `iceprog` (for the shipped iCE40 demos only) |
| Target FPGA(s) | iCE40 HX8K (CT256, `picosoc/hx8kdemo.v`/`.pcf`) and iCE40 UP5K (SG48, `picosoc/icebreaker.v`/`.pcf`) — **neither is ECP5**. Core itself (`picorv32.v`) is FPGA-family-agnostic |
| Board revision(s) | n/a — targets are the iCE40-HX8K Breakout Board and the iCEBreaker board, not ULX3S |
| Activity | last commit 2026-09-07 (`git log -1`), likely a CI/doc touch given the README's "no longer under active development" banner (`README.md:6`), not feature work. Commit count/first commit: unknown (shallow clone; not in `history.tsv`) |

## What the gateware does
- **`picorv32.v`** — a size-optimized RV32I/E/M/C RISC-V CPU core, configurable via
  Verilog parameters into RV32E, RV32I, RV32IC, RV32IM, or RV32IMC variants
  (`README.md:14-15`). No FPU. Optional IRQ, PCPI (co-processor), and RISC-V Formal
  (`RISCV_FORMAL`) interfaces.
- **PicoSoC** (`picosoc/picosoc.v`) — a minimal example SoC wrapping the core with a
  memory-mapped SPI flash execute-in-place controller (`spimemio.v`) and a UART
  (`simpleuart.v`), plus an `iomem_*` bus for board-specific peripherals.
- Two ready-made board demos: `picosoc/hx8kdemo.v` (iCE40 HX8K breakout board, external
  SPI flash for code+data) and `picosoc/icebreaker.v` (iCEBreaker UP5K, adds on-chip SPRAM
  via `ice40up5k_spram.v`).
- **No ULX3S or ECP5 support exists in this repo** — this catalogue entry is for the core
  and PicoSoC as *reusable IP*, not as a runnable ULX3S project.

## Structure
- `picorv32.v` — the CPU core (single file, ~92 KB / ~2400 lines).
- `picosoc/` — example SoC: `picosoc.v`, `spimemio.v`, `simpleuart.v`, two board tops
  (`hx8kdemo.v`, `icebreaker.v`) with matching `.pcf`/`.core`/testbenches, plus
  `ice40up5k_spram.v` and firmware (`firmware.c`, `start.s`, `sections.lds`).
- `tests/` — RISC-V assembly instruction tests (`*.S`) used by the root Makefile testbenches.
- `firmware/` — the default test firmware built for `testbench.v`.
- `dhrystone/` — Dhrystone benchmark sources.
- `scripts/vivado/`, `scripts/quartus/` — proprietary-flow area/speed benchmarking scripts,
  generic (no board).
- `scripts/icestorm/` — a third, generic iCE40 example under the open flow.
- `picorv32.core` — FuseSoC package descriptor for the core.

## How to build
Not run (per repo instructions: read-only review). Commands as found:
- Root `Makefile` self-checking testbenches (Icarus Verilog unless noted):
  `test`, `test_vcd`, `test_wb`, `test_wb_vcd`, `test_ez`, `test_ez_vcd`, `test_sp`,
  `test_axi`, `test_synth` — each builds `testbench(_wb/_ez/_synth).v` + `picorv32.v` +
  `tests/*.S`, self-checks via a magic MMIO word the testbench watches
  (`Makefile:24-54`). `test_verilator` builds the same testbench through Verilator/C++
  (`Makefile:81`).
- `picosoc/Makefile` (iCE40 only):
  ```
  make hx8kdemo.bin      # yosys synth_ice40 -> nextpnr-ice40 --hx8k --package ct256 -> icepack
  make hx8kprog          # iceprog hx8kdemo.bin; iceprog -o 1M hx8kdemo_fw.bin
  make icebreaker.bin    # yosys synth_ice40 -dsp -> nextpnr-ice40 --up5k --package sg48 -> icepack
  ```
  Simulation-only targets `hx8ksim`/`hx8ksynsim`/`icebsim`/`icebsynsim` run the demo SoC +
  firmware through Icarus Verilog and self-check via the simulated UART.
- `scripts/vivado`/`scripts/quartus`: proprietary Vivado/Quartus TCL/QSF scripts for
  synthesis benchmarking on generic 7-series/Altera parts — not build targets for a board.

## Reuse notes

| Block | Path | Top module | Language | Vendor primitives | License |
|---|---|---|---|---|---|
| RISC-V CPU core | `picorv32.v` | `picorv32` | Verilog-2005 | none | ISC |
| Example SoC wrapper | `picosoc/picosoc.v` | `picosoc` | Verilog | none | ISC |
| SPI-flash XIP controller | `picosoc/spimemio.v` | `spimemio` | Verilog | none | ISC |
| Minimal UART | `picosoc/simpleuart.v` | `simpleuart` | Verilog | none | ISC |
| iCE40 UP5K SPRAM wrapper (**not portable as-is**) | `picosoc/ice40up5k_spram.v` | `ice40up5k_spram` | Verilog | `SB_SPRAM256KA` ×4 (iCE40-only) | ISC |
| Board tops (reference only, iCE40) | `picosoc/hx8kdemo.v`, `picosoc/icebreaker.v` | `hx8kdemo`, `icebreaker` | Verilog | `SB_IO` (tristate flash I/O) | ISC |

- **`picorv32` core**: fully portable, board-agnostic synthesizable Verilog-2005, **zero
  vendor primitives** (verified: no `SB_`/`EHXPLLL`/etc. in `picorv32.v`) — drops directly
  into an ECP5/ULX3S design under `synth_ecp5`. Interface is a simple Wishbone-like
  `mem_valid/mem_ready/mem_addr/mem_wdata/mem_wstrb/mem_rdata` memory bus plus an optional
  look-ahead variant (`mem_la_*`), a 32-bit `irq` vector with `eoi`, and an optional PCPI
  co-processor port (`picorv32.v:87-119`). Key parameters: `ENABLE_MUL`/`ENABLE_DIV`/
  `ENABLE_FAST_MUL`, `ENABLE_IRQ`, `COMPRESSED_ISA` (RVC), `ENABLE_REGS_16_31`=0 for RV32E,
  `PROGADDR_RESET`/`PROGADDR_IRQ`/`STACKADDR` (`picorv32.v:63-86`). Clock: single `clk`
  input, synchronous active-low-free `resetn`; runs the two shipped iCE40 demos at
  12–13 MHz (per catalogue note) — would need re-timing/PLL work to run near ULX3S's
  25 MHz or higher on ECP5, but nothing in the core itself limits frequency beyond timing
  closure.
- **`picosoc`/`spimemio`/`simpleuart`**: also primitive-free and portable as-is. `spimemio`
  expects a QSPI-capable flash controller pattern (four bidirectional `flash_io[0:3]`
  split into `_oe`/`_do`/`_di` triples, `picosoc.v:49-64`) — on the ULX3S this maps onto
  the shared SPI-flash pins used for configuration; needs a board top providing tristate
  buffers (ECP5 generic `inout`/`BB`, not the iCE40 `SB_IO` used in the reference tops).
- **What needs replacing to target ULX3S/ECP5**: only `ice40up5k_spram.v` (4×
  `SB_SPRAM256KA`, iCE40-only 128 KB SPRAM — for ECP5 substitute inferred BRAM/DP16KD or a
  parameterized on-chip RAM) and the `SB_IO`-based tristate buffers in `hx8kdemo.v`/
  `icebreaker.v` (for ECP5 substitute plain `inout` + generic tristate, or `BB` primitive
  as used e.g. in `chrismoos__m6502`'s `targets/ulx3s/top.sv`). Everything else — the CPU,
  the SoC glue, the flash and UART controllers — is drop-in.
- No ULX3S `.lpf` exists to copy; a new top-level and pin file (`ulx3s_v20.lpf` names, per
  `CLAUDE.md`) must be written from scratch, e.g. reusing PicoSoC's `iomem_*` interface to
  wire in ULX3S-specific peripherals.
- Pairs naturally with `zipcpu__sdspi` (see that page) for SD-card storage: PicoSoC's
  `iomem_valid/ready/addr/wstrb/wdata/rdata` bus can front the Wishbone `sdspi`/`sdio` core
  with a small adapter, since both are simple synchronous register-mapped interfaces.

## Open questions
- No ULX3S/ECP5 fork or example using this exact PicoRV32 checkout was found in this repo
  or cross-referenced elsewhere in this session — unknown whether one exists upstream
  (the catalogue's `reusable-cores.md` lists "picorv32 (fpga-odysseus)" as a separate,
  unreviewed ECP5 port to check).
- Achievable clock frequency on ECP5 25F/45F/85F after `synth_ecp5 -abc9`: not measured
  (would need an actual build).
- Commit count / first-commit date: unknown (not in `history.tsv`, clone is shallow).
