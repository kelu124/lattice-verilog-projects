---
title: "chrismoos__m6502"
parent: "Project reviews"
nav_order: 1
---
<!-- Generated from data/projects/chrismoos__m6502.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# m6502 (`chrismoos__m6502`)

| Field | Value |
|---|---|
| Upstream | https://github.com/chrismoos/m6502 |
| Reviewed at | `4471944` (upstream date 2026-03-01), reviewed 2026-09-28 |
| License | MIT (`LICENSE`, "Copyright 2026 Chris Moos") |
| HDL / framework | SystemVerilog (16 `.sv` + 1 `.vh` in `rtl/`); Python/cocotb for the test suite |
| Toolchain | `open`: yosys (`synth_ecp5 -abc9`) → nextpnr-ecp5 (`--85k --package CABGA381 --freq 50`) → ecppack, per `targets/ulx3s/Makefile:23-32` |
| Programmer | `fujprog` (`targets/ulx3s/Makefile:35`, `prog` target) |
| Target FPGA(s) | 85F by default (`DEVICE ?= 85k`, `targets/ulx3s/Makefile:4`); overridable via `DEVICE=` since only `--$(DEVICE)` is passed to nextpnr-ecp5, but only 85F has been exercised in the Makefile default |
| Board revision(s) | v2.x/v3.0.x — `targets/ulx3s/ulx3s_v20.lpf` header states "ULX3S v2.x.x and v3.0.x" (`ulx3s_v20.lpf:3`) |
| Activity | last commit 2026-03-01 (`git log -1 --format=%cs`, pinned commit `4471944`); `.claude/memory/history.tsv` records 5 total commits, first commit 2026-02-17. Young, small repo |

## What the gateware does

- **6502 CPU core** — `rtl/cpu_6502.sv` (top), `rtl/cpu_6502_alu.sv` (ALU),
  `rtl/cpu_6502_ir_decoder.sv` + `rtl/cpu_6502_microcode.sv` + `rtl/cpu_6502_instructions.vh`
  (vertical-microcode instruction decode). A cycle-accurate NMOS 6502 with all addressing
  modes, verified against the Klaus Dormann 6502 functional test (`README.md:9-12`,
  `TESTING.md:15-23`).
- **MCU wrapper** — `rtl/mcu.sv` (top module `mcu`). Integrates the CPU with an internal
  BRAM (`rtl/bram.sv`), an external multiplexed bus (`rtl/bus_multiplexer.sv`), and
  memory-mapped peripherals: `rtl/peripherals/gpio.sv` (base `0xA000`), `sk6812rgbw*.sv`
  (base `0xA010`, addressable-LED driver), `timer.sv` (base `0xA020`), `uart.sv`+
  `uart_rx.sv`/`uart_tx.sv` (README §Peripherals; `clock_control.sv` at base `0xA030`
  handles the CPU clock divider).
- **ULX3S target** — `targets/ulx3s/top.sv` (top module `top`). Instantiates an ECP5
  `EHXPLLL` to derive 100/50/10 MHz from the 25 MHz board clock, runs the `mcu` at 50 MHz,
  drives 8 LEDs, a UART on `gp26`/`gn27`, and an 8-bit multiplexed external bus on
  `gp4..gp7`/`gn4..gn7` via ECP5 `BB` (bidirectional buffer) primitives
  (`targets/ulx3s/top.sv:63-70`) for the RP2040-based `rpi-flash-emulator/` external
  RAM/ROM emulator. **This is a demo/bring-up target, not a full retro-computer** — no
  video, no SD card, no ROM images beyond the test/demo firmware.

## Structure

- `rtl/` — CPU core, ALU, decoder, microcode, BRAM, bus multiplexer.
- `rtl/peripherals/` — GPIO, SK6812 RGBW LED, timer, UART (+ FIFO).
- `targets/ulx3s/` — `top.sv`, `Makefile`, `ulx3s_v20.lpf` (606 lines, standard v2.x/v3.0.x
  pin map).
- `targets/fomu/` — a second FPGA target (Lattice iCE40 UP5K Fomu), not reviewed here.
- `test/` — cocotb Python tests (`test_cpu_6502.py`, `test_mcu.py`, `test_bram.py`,
  `test_uart.py`, `test_timer.py`, `test_clock_control.py`, `test_gpio_mux.py`,
  `test_cpu_6502_reset.py`) each paired with a `.sv` DUT wrapper, plus
  `test_mcu_klaus.sv`/`tb_mcu_klaus.cpp` (Verilator) running the Klaus Dormann functional
  ROM `6502_functional_test.hex`.
- `examples/` — usage examples (not reviewed).
- `rpi-flash-emulator/` — RP2040 PIO firmware providing external RAM/ROM over the
  multiplexed bus (companion hardware, out of FPGA scope).
- `docs/architecture.md`, `docs/peripherals.md`, `docs/bus-multiplexer.md` — design docs
  referenced from the README (not re-verified here).

## How to build

Not run. Commands as found in `targets/ulx3s/Makefile`:

```
make                 # yosys synth_ecp5 -abc9 -> nextpnr-ecp5 --85k --package CABGA381 \
                      #   --freq 50 --lpf ulx3s_v20.lpf -> ecppack --compress -> bin/toplevel.bit
make prog             # fujprog bin/toplevel.bit
make clean
```

Simulation/test, from repo root (`Makefile`):

```
make test             # uv run pytest test/test_runner.py -s -x   (cocotb unit tests,
                      #   default simulator per catalogue: verilator), then make test-klaus
make test-klaus       # cd test && make -f Makefile.mcu_klaus run  (Verilator C++ testbench,
                      #   success = CPU PC reaches 0x3469, TESTING.md:20-21)
```

## Reuse notes

| Block | Path | Top module | Language | Vendor primitives | License |
|---|---|---|---|---|---|
| 6502 CPU core | `rtl/cpu_6502.sv` (+ `cpu_6502_alu.sv`, `cpu_6502_ir_decoder.sv`, `cpu_6502_microcode.sv`) | `cpu_6502` | SystemVerilog | none | MIT |
| MCU wrapper (CPU + BRAM + peripherals) | `rtl/mcu.sv` | `mcu` | SystemVerilog | none | MIT |
| UART, GPIO, timer, SK6812 peripherals | `rtl/peripherals/*.sv` | `uart`, `gpio`, `timer`, `sk6812rgbw_peripheral` | SystemVerilog | none | MIT |
| ULX3S top (PLL + bus mux reference) | `targets/ulx3s/top.sv` | `top` | SystemVerilog | ECP5 `EHXPLLL`, `BB` | MIT |

- **`cpu_6502`**: fully standalone, **no vendor primitives**, ~950 LUTs per the README
  (`README.md:13`, unverified claim, not re-measured here). Ports: `i_clk`, `i_reset_n`,
  `i_rdy`, `i_nmi_n`, `i_irq_n`, `i_so_n`, standard 6502 bus `i_bus_data[7:0]` /
  `o_bus_data[7:0]` / `o_bus_addr[15:0]` / `o_rw`, plus `o_phi1`/`o_phi2` (derived
  combinationally from `i_clk`: `o_phi2 = i_clk; o_phi1 = ~i_clk`, `rtl/cpu_6502.sv:29-30`)
  and a 3-bit debug-select/8-bit debug-data port. Parameters `START_PC_ENABLED`,
  `START_PC` override the reset vector fetch. Single clock domain, synchronous active-low
  reset (`i_reset_n`) — trivially portable to any ECP5 design; no clock-domain-crossing
  concerns since `phi1`/`phi2` are just the core clock and its inverse, not separate
  clocks.
- **`mcu`**: adds `rtl/bram.sv` (parameterized `INIT_FILE`/`SIZE`, default 64 KB — will map
  to ECP5 `DP16KD` block RAM via inference, no explicit primitive instantiated) and the
  four peripherals at fixed base addresses `0xA000`/`0xA010`/`0xA020`/`0xA030`. Also
  primitive-free; drops into any ECP5 design needing a quick 6502 SoC with UART bring-up.
  Runs at `clk_50` (50 MHz) in the ULX3S target, with the CPU further divided by
  `clock_control.sv` (`CPU_CLOCK_DIV_DEFAULT` parameter, register `0xA030`) — the target's
  `.lpf` constrains a `bus_phi2` net to 15 MHz (`ulx3s_v20.lpf:8`), i.e. the reference
  design does not run the CPU at the full period-accurate ~1–2 MHz of a real 6502 nor at
  the raw 50 MHz PLL output; exact CPU frequency depends on the runtime `CPU_DIV` register
  value (not statically fixed in RTL).
- **ULX3S top-level (`targets/ulx3s/top.sv`) as a wiring reference**: shows a clean example
  of an ECP5 `EHXPLLL` instantiation for 25→100/50/10 MHz (`CLKI_DIV=1, CLKFB_DIV=4,
  CLKOP_DIV=6, CLKOS_DIV=12, CLKOS2_DIV=60`, generated by `ecppll -i 25 --clkout0 100
  --clkout1 50 --clkout2 10`, comment at `targets/ulx3s/top.sv:178`) and of `BB` primitive
  usage for a tristate multiplexed bus (`gp4..gp7`/`gn4..gn7`) — both are reusable patterns
  even outside this project, though the PLL numbers/DIVs would need regenerating with
  `ecppll` for a different target frequency.
- To drop just the CPU+peripherals (no bus-mux/RP2040 dependency) into a new ULX3S design:
  take `rtl/*.sv` and `rtl/peripherals/*.sv` wholesale (all primitive-free), write a new
  top-level with an ULX3S PLL (copy the `EHXPLLL` block from `targets/ulx3s/top.sv` and
  regenerate divisors with `ecppll` for the desired frequency), and reuse
  `targets/ulx3s/ulx3s_v20.lpf` as a starting pin file (only `clk_25mhz`, `btn`, `led`, and
  the GPIO pins actually used need to stay).

## Open questions

- Exact effective CPU (phi2) frequency in the shipped ULX3S demo at runtime: depends on
  the `CPU_DIV` register default/reset value in `clock_control.sv` vs. the `bus_phi2` LPF
  constraint (15 MHz) — not fully traced through in this review; `unknown`.
- `DEVICE` override to 12F/25F/45F: not tested; the `Makefile` accepts any `nextpnr-ecp5`
  `--<size>k` value but only 85F is exercised by default and by the `.lpf`'s "ULX3S
  v2.x.x/v3.0.x" pin map (should apply to all sizes on that revision, per board-hardware
  notes, but not verified against this repo specifically).
- `targets/fomu/`, `examples/`, `docs/*.md`, `rpi-flash-emulator/` not reviewed in depth —
  out of scope for the ULX3S-focused reuse notes above.
- Whether `make test`'s default cocotb simulator is Verilator (per `catalogue.tsv`) is
  configured via `test/test_runner.py`/`cocotb_tools.runner` — not independently re-verified
  here.
{% endraw %}
