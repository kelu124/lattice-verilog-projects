---
title: "lit3rick_review"
parent: "Project reviews"
nav_order: 8
---
<!-- Generated from data/projects/lit3rick_review.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# lit3rick open ultrasound pulse-echo board (`kelu124__lit3rick`)

| Field | Value |
|---|---|
| Upstream | https://github.com/kelu124/lit3rick |
| Reviewed at | `ca4ad98` (upstream date 2024-07-13), reviewed 2026-09-28 |
| License | GPL-3.0-or-later for software/gateware (`Readme.md` `# License`); hardware under TAPR Open Hardware License 1.0 (`TAPR.txt`); documentation CC-BY-SA-3.0 (`Readme.md`). Individual RTL files carry different upstream licenses (see Reuse notes). |
| HDL / framework | Verilog (119 `.v`) + SystemVerilog (5 `.sv`, testbenches only), under `verilog/src/`, `verilog/sigprocessing/` (a duplicate/standalone copy of the DFT and A-law cores with their own docs) and `verilog/radiant/fft_adc/` (Lattice Radiant IP-catalog project sources). |
| Toolchain | `both`: open (`yosys`, `verilog/src/synth.ys` — `synth_ice40 -top top -blif out.blif`; the script only reads `top.v`, `debounce.v`, `i2c_slave_axil_master.v`, `i2c_slave.v`, `main_fsm.v`, `mcp4812.v`, `ram_256k.v`, `spi_slave.v`, i.e. **not** the ADC/FFT/I2S/memory-mux datapath, and no `nextpnr-ice40`/`icepack` step is checked in) and proprietary Lattice Radiant (`verilog/radiant/fft_adc/fft_adc.rdf`, a full project with `impl_1/` place-and-route reports and a built `fft_adc_impl_1.bin` already committed, plus IP-catalog-generated cores under `ip_cores/`) |
| Programmer | Custom tool, not `openFPGALoader`/`fujprog`: `program/utilities/lit3prog.cc` bit-bangs SPI over the board's Raspberry Pi header to program either the flash or the FPGA SRAM directly (`program/Readme.md`); a prebuilt bitstream ships at `verilog/lit3_v2.0.bin` |
| Target FPGA(s) | **iCE40 UP5K only** (`SG48I` package) — **not ECP5, not ULX3S**. Confirmed in `verilog/radiant/fft_adc/fft_adc.rdf:1` (`device="iCE40UP5K-SG48I" performance_grade="High-Performance_1.2V"`) and `verilog/src/synth.ys:11` (`synth_ice40 -top top`); `top.v` also instantiates the iCE40-only `HSOSC` internal oscillator and `RGB` LED-driver primitives. Catalogued here as a source of reusable ultrasound/DSP logic to port, and as the repo owner's other board alongside `un0rick` |
| Board revision(s) | lit3rick UP5K board (not applicable to ULX3S) — repo owner's own single-channel open ultrasound pulse-echo board, forkable design on Upverter (`Readme.md`) |
| Activity | last commit `2024-07-13` (`git -C original_sources/kelu124__lit3rick log -1 --format=%cs`), pinned at `ca4ad98`; commit-history stats not recorded in `.claude/memory/history.tsv` |

## What the gateware does

- **Ultrasound pulser control** — `verilog/src/rtl/main_fsm.v` (top `main_fsm`) sequences a
  fixed acquisition cycle: drive a DAC gain ramp, assert `PHV`/`PnHV`/`PDamp` (pulse
  polarity/damping control for the HV7361GA-G pulser) for durations set by
  `PHV_time`/`PnHV_time`/`PDamp_time` registers, then trigger sampling and, once the DFT
  finishes, either idle or loop (`autorestart_mode`).
- **ADC acquisition** — `verilog/src/rtl/adc_receiver.v` captures a fixed 8192-sample burst
  from a 12-bit parallel ADC (AD9629BCPZ-65, a 65-MSPS-rated part; `Readme.md` states it
  reaches 64 Msps in this design) into
  `verilog/src/rtl/ram_256k.v` (256k-point on-chip RAM) via `verilog/src/rtl/memory_mux.v`,
  removing the ADC's 2048 mid-scale DC offset in the same cycle.
- **TGC / gain DAC** — `verilog/src/rtl/mcp4812.v` drives an MCP4812 SPI DAC that ramps the
  AD8331 variable-gain amplifier over the acquisition window (time-gain compensation),
  fed from a small dual-port RAM (`ebr_dp`, a Radiant IP-catalog core) loaded over I2C/AXI.
- **On-chip DSP / envelope extraction** — `verilog/src/rtl/signal_filter.v` feeds the 8192
  acquired samples through a `sc_fifo` (Radiant IP-catalog sync FIFO) into
  `verilog/src/rtl/fft/dft.v` (top `dft`): a 16-point sliding, non-overlapped window DFT
  (`dft_core.v`, based on the sliding-DFT technique referenced in-file) computing 3
  frequency bins per window, taking the magnitude (`dft_complex_abs.v` + `dft_sqrt.v`), and
  producing a 256-sample envelope signal. That envelope is then compressed 15→8 bit with
  `verilog/src/rtl/alaw_coder.v` (G.711 A-law, per ITU-T G.191) before being written to a
  second on-chip RAM (`fft_memory`, another `ebr_dp` instance). The identical core (with its
  own README calling it "Fourier (envelope extraction) IP-core") also ships standalone under
  `verilog/sigprocessing/code_fourrier/`, alongside the A-law coder under
  `verilog/sigprocessing/code_alaw/`.
- **Host interfaces** — `verilog/src/rtl/i2c_slave_axil_master.v` (Alex Forencich's
  `verilog-i2c` `i2c_slave` wrapped as an AXI-Lite master) exposes the register file and
  both RAMs to an I2C host at device address `0x25`; `verilog/src/rtl/spi_slave.v`
  (OpenCores `spi_verilog_master_slave`) exposes the same RAMs over SPI to the Raspberry Pi
  header; `verilog/src/rtl/i2s_master.v` + `i2s_control.v` stream either RAM out over I2S in
  an autorestart/streaming mode, buffered by an `sc_fifo`.
- **Housekeeping** — `verilog/src/rtl/debounce.v` debounces the two user buttons; `top.v`
  drives an RGB status LED through the iCE40 `RGB` hard IP and a Radiant-IP-catalog PLL
  (`pll_adc`) that derives `ADC_REF_CLK` from the internal `HSOSC` oscillator.

## Structure

- `verilog/src/rtl/` — hand-written top-level design: `top.v` (top), `main_fsm.v`,
  `adc_receiver.v`, `signal_filter.v`, `memory_mux.v`, `ram_256k.v`, `mcp4812.v`,
  `spi_slave.v`, `i2c_slave_axil_master.v`/`i2c_slave.v`/`i2c_wrapper.v`, `i2s_master.v`/
  `i2s_control.v`, `alaw_coder.v`, `debounce.v`, `sqrt.v`; `fft/` (DFT core, see above);
  `ip_cores/` (`ebr_dp.v`, `sc_fifo.v` — Radiant IP-catalog dual-port RAM and sync FIFO).
- `verilog/src/tb/` — a single self-checking SystemVerilog testbench `tb_top.sv` plus
  bus-functional models `ad9629.sv` (ADC), `i2c_if.sv`, `mcp4812_imit.sv`, `mi_if.sv`.
- `verilog/src/synth.ys` — partial open-flow (yosys) synthesis script (see Toolchain).
- `verilog/modelsim/` — `compile.tcl` (full file list, ModelSim/Questa `vlog`/`vcom`) and
  `tb_top.do` (`vsim -do tb_top.do`) to run `tb_top.sv`.
- `verilog/radiant/fft_adc/` — the full Lattice Radiant project (`fft_adc.rdf`) targeting
  `iCE40UP5K-SG48I`, with completed place-and-route under `impl_1/` and IP-catalog sources
  under `ip_cores/` (`pll_adc`, `sc_fifo`, `spi_slave`) and `ebr_dp/`.
- `verilog/sigprocessing/code_fourrier/` and `code_alaw/` — the DFT and A-law cores
  packaged standalone with their own `README.md`, icarus/ModelSim simulation setups and a
  Python reference model (`math/dft.py`, `math/alaw.py`).
- `verilog/lit3_v2.0.bin` — prebuilt bitstream (101.7 KB).
- `hardware/` — board fabrication files (BOM, pick-and-place, drills, Upverter export);
  out of gateware scope.
- `program/` — `lit3prog` RPi-SPI programmer (source in `program/utilities/`) and
  `prog_ram.sh`/`prog_flash.sh` wrapper scripts.
- `py_fpga/`, `micropython/` — host-side Python/MicroPython drivers to configure and read
  the board (not reviewed here).

## How to build

No end-to-end open-flow build (`nextpnr`/`icepack`) is checked into the repo for the full
design; what is present:

- Partial open synthesis only: `cd verilog/src && yosys synth.ys` produces `out.blif` for a
  subset of modules (see Toolchain) — not attempted here (read-only review), and would need
  a hand-written `.pcf` (none found for this design; the only `.pcf` in the repo,
  `micropython/source/pinout.pcf`, is for an unrelated bootloader/SPI-flash pin set) plus
  `nextpnr-ice40 --up5k --package sg48` + `icepack` to finish the flow.
- Full design, proprietary flow: open `verilog/radiant/fft_adc/fft_adc.rdf` in Lattice
  Radiant (device `iCE40UP5K-SG48I`) and run synthesize/map/place-and-route on `impl_1`;
  pin constraints are in `verilog/radiant/fft_adc/source/impl_1/impl_1.pdc`. The project
  already contains completed P&R output (`impl_1/fft_adc_impl_1.bin` and reports), so this
  flow is known to close.
- Simulation: ModelSim/Questa via `verilog/modelsim/tb_top.do` (`vsim -do tb_top.do`,
  sources `compile.tcl`) runs the self-checking `tb_top.sv` (see Reuse notes/tests below).
  The standalone `code_fourrier`/`code_alaw` cores additionally support Icarus Verilog
  (`sim/icarus/run_sim`).
- Programming: build/flash a `.bin` with `program/prog_ram.sh` (SRAM, volatile) or
  `prog_flash.sh`, using the `lit3prog` binary built from `program/utilities/Makefile`; no
  FTDI is used, only the Raspberry Pi SPI header (`program/Readme.md`).

None of the above was executed in this review (read-only, no build/simulate per task rules).

## Reuse notes

The design mixes fully portable, vendor-primitive-free DSP/protocol RTL with a few
iCE40-specific primitives and several Lattice-Radiant-IP-catalog-generated black boxes.

### Reusable blocks

| Block | Path | Top module | Language | Vendor primitives | License |
|---|---|---|---|---|---|
| Sliding-DFT envelope extractor | `verilog/src/rtl/fft/` (`dft.v`, `dft_core.v`, `dft_preproc.v`, `dft_postproc.v`, `dft_complex_abs.v`, `dft_sqrt.v`, `dft_fifo.v`, `dft_dline.v`) | `dft` | Verilog | none | GPL-3.0-or-later (repo-level `Readme.md`; no per-file SPDX) |
| A-law compressor | `verilog/src/rtl/alaw_coder.v` | `alaw_coder` | Verilog | none | GPL-3.0-or-later (repo-level; no per-file SPDX); algorithm per ITU-T G.191 |
| ADC burst capture | `verilog/src/rtl/adc_receiver.v` | `adc_receiver` | Verilog | none | GPL-3.0-or-later (repo-level; no per-file SPDX) |
| DAC/TGC driver | `verilog/src/rtl/mcp4812.v` | `mcp4812` | Verilog | none | GPL-3.0-or-later (repo-level; no per-file SPDX) |
| I2C-slave-to-AXI-Lite-master bridge | `verilog/src/rtl/i2c_slave_axil_master.v` (+ `i2c_slave.v`) | `i2c_slave_axil_master` | Verilog | none | MIT (in-file header, (c) 2017/2019 Alex Forencich — `verilog-i2c`) |
| SPI slave | `verilog/src/rtl/spi_slave.v` | `spi_slave` | Verilog | none | unknown / no SPDX (OpenCores `spi_verilog_master_slave`, Santhosh G) |
| iCE40 EBR dual-port RAM wrapper | `verilog/src/rtl/ip_cores/ebr_dp.v` (also `verilog/radiant/fft_adc/ebr_dp/`) | `ebr_dp` | Verilog | Radiant IP-catalog generated (UP5K EBR) | Lattice IP-catalog template (no explicit SPDX seen) |
| iCE40 sync FIFO wrapper | `verilog/src/rtl/ip_cores/sc_fifo.v` | `sc_fifo` | Verilog | Radiant IP-catalog generated (UP5K EBR) | Lattice IP-catalog template (no explicit SPDX seen) |

- The DFT and A-law cores have no vendor primitives and are the most portable/interesting
  reuse candidates — they implement a lightweight, resource-cheap alternative to a full FFT
  for narrowband envelope/amplitude extraction, useful for any project needing cheap
  spectral-magnitude estimation rather than a full spectrum.
- `top.v` itself instantiates two iCE40-only hard macros that block a direct ECP5 port:
  `HSOSC` (internal ~48 MHz oscillator) and `RGB` (current-mode RGB LED driver) — both have
  ECP5 equivalents (`OSCG`, discrete LED drive) but need rewriting, not just renaming.
  `pll_adc` (the ADC reference-clock PLL) is a Radiant IP-catalog wrapper and would need
  regenerating for ECP5's `EHXPLLL` (e.g. with `emard`'s `ecp5pll`, already catalogued as
  this project's best `pll-clock` core).
- `ebr_dp`/`sc_fifo` are IP-catalog black boxes (see `verilog/radiant/fft_adc/ip_cores/*/component.xml`)
  rather than hand-written RTL; porting means reimplementing the same dual-port-RAM/FIFO
  behaviour on ECP5 `DP16KD`, not copying the file.
- The `i2c_slave_axil_master.v`/`i2c_slave.v` pair is the same upstream `verilog-i2c`
  library (Alex Forencich, MIT) already catalogued as this collection's best `i2c` core
  (via `asinghani__pifive-cpu`), just wrapped as an AXI-Lite master here instead of a
  Wishbone slave — a useful second integration pattern to reference.
- **Tests**: `verilog/src/tb/tb_top.sv` is a genuinely self-checking testbench (`err` flag,
  `$error` on mismatch, `"Tests finished successfully!"`/`"Tests failed!"` banner) covering
  `test_adc`, `test_i2s`, `test_dac` and `test_fft` tasks (the last drives the DFT/A-law
  path through the I2C register interface and reads bins back), run via ModelSim/Questa
  (`verilog/modelsim/tb_top.do`). The standalone `code_fourrier`/`code_alaw` copies add
  Icarus Verilog simulation and per-submodule testbenches
  (`sim/tb/tb_dft*.v`, `tb_alaw_coder.v`). No CI / `make check` was found — simulation is
  manual (ModelSim or Icarus), and no formal verification is present.

## Open questions

- Which of the two design captures (`verilog/src/` hand-written RTL vs.
  `verilog/radiant/fft_adc/` Radiant project) is the one actually flashed to produce
  `verilog/lit3_v2.0.bin` — the file lists and module sets differ (e.g. `synth.ys` omits
  the ADC/FFT/I2S path entirely) and this was not resolved from the source tree alone.
  → add to `.claude/TODO.md`.
- Whether the open-source flow (`synth_ice40` + `nextpnr-ice40` + `icepack`) can actually
  close for the *full* design (ADC + DFT + I2S + both RAMs), given that `ebr_dp`/`sc_fifo`
  are Radiant-IP-catalog black boxes with no open-source equivalent checked in — unverified,
  would need to actually run the flow (out of scope for a read-only review).
- Exact license for `verilog/src/rtl/ip_cores/ebr_dp.v` and `sc_fifo.v` (Lattice IP-catalog
  templates) — no SPDX header found; treat as Lattice-template code, not open source, until
  confirmed.
- Whether `verilog/src/rtl/i2c_wrapper.v` (a near-duplicate of
  `i2c_slave_axil_master.v`) is dead code or an alternate integration point — not
  instantiated from `top.v` in this pass.
- Clock frequencies for `ADC_DCLK` / `i2s_clk` are supplied externally by the AD9629 and by
  the I2S host respectively; not derivable from the RTL alone (would need the board's
  MANUAL/README or a schematic check under `hardware/`).
{% endraw %}
