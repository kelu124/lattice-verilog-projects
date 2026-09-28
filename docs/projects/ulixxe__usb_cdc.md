---
title: "ulixxe__usb_cdc"
parent: "Project reviews"
nav_order: 16
---
<!-- Generated from data/projects/ulixxe__usb_cdc.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# USB_CDC (`ulixxe__usb_cdc`)

| Field | Value |
|---|---|
| Upstream | https://github.com/ulixxe/usb_cdc |
| Reviewed at | `6798bf4` (upstream date 2024-03-10), reviewed 2026-09-28 |
| License | MIT (`LICENSE`, Copyright (c) 2021 ulixxe) |
| HDL / framework | Verilog-2001 (`usb_cdc/*.v` core); VHDL top-level wrappers in the TinyFPGA-BX example (`examples/TinyFPGA-BX/hdl/demo/demo_fpga.vhd`) |
| Toolchain | `open` (yosys + nextpnr-ice40 + icepack, via `examples/{Fomu,TinyFPGA-BX}/OSS_CAD_Suite/Makefile`); examples also carry a Lattice iCEcube2 project. No ECP5/open-flow ECP5 build exists in this repo |
| Programmer | `tinyprog` (TinyFPGA-BX, `examples/TinyFPGA-BX/OSS_CAD_Suite/Makefile:33`); `dfu-util` (Fomu, `examples/Fomu/OSS_CAD_Suite/Makefile:65`) |
| Target FPGA(s) | iCE40 UP5K SG48 (Fomu), iCE40 LP8K CM81 (TinyFPGA-BX) — **not ECP5, no ULX3S target in this repo** |
| Board revision(s) | n/a — repo does not target ULX3S |
| Activity | last commit 2024-03-10 (`6798bf4`); commit count / first commit unknown (shallow clone, repo not in `.claude/memory/history.tsv`) |

## What the gateware does

A from-scratch, vendor-primitive-free Full-Speed (12 Mbit/s) USB device core
implementing the USB Communications Device Class, Abstract Control Model
subclass (`usb_cdc/usb_cdc.v`, top module `usb_cdc`) — i.e. a USB-to-serial
("virtual COM port") device, recognized out of the box by Windows/macOS/Linux
CDC-ACM drivers. Configurable for 1–7 CDC channels via the `CHANNELS`
parameter. No ULX3S example is provided; the repo ships example
applications/top-levels only for Fomu (iCE40 UP5K) and TinyFPGA-BX (iCE40
LP8K): `bootloader` (TinyFPGA bootloader replacement, `tinyprog`-compatible),
`demo` (throughput/reliability test with RAM/ROM/flash access), `loopback`,
`loopback_2ch`/`loopback_7ch`, and `soc` (FIFO bus interface for a CPU).

## Structure

- `usb_cdc/` — the reusable core, 8 files, ~3260 lines total: `usb_cdc.v` (top,
  wires SIE + endpoints + FIFOs), `sie.v` (Serial Interface Engine: packet
  recognition, CRC, PID, bus reset), `phy_rx.v`/`phy_tx.v` (NRZI, bit
  stuffing, SOP/EOP), `ctrl_endp.v` (control endpoint / enumeration, largest
  file at 981 lines), `bulk_endp.v`, `in_fifo.v`, `out_fifo.v`.
- `examples/Fomu/`, `examples/TinyFPGA-BX/` — each has `hdl/` (per-example
  Verilog `app.v` + VHDL top `demo_fpga.vhd`), `OSS_CAD_Suite/` (open-flow
  Makefile + `.pcf`), `iCEcube2/` (Lattice project files), `python/` (host-side
  test scripts).
- `examples/common/` — shared HDL helpers, GTKWave save files, Synplify Pro
  project fragments.

## How to build

Not run (read-only review). From `examples/README.md` and
`examples/TinyFPGA-BX/OSS_CAD_Suite/Makefile`:

```
cd examples/TinyFPGA-BX/OSS_CAD_Suite
make all PROJ=demo        # yosys synth_ice40 -> nextpnr-ice40 --lp8k --package cm81 -> icepack
make prog PROJ=demo        # tinyprog -p <bin>
make sim PROJ=demo         # iverilog/vvp -> .fst (self-checking testbench, `assert_error` macros)
```

Fomu flow is identical but targets `up5k`/`sg48` and programs with
`dfu-util -D <dfu>` (`examples/Fomu/OSS_CAD_Suite/Makefile:65`). Neither
Makefile references ECP5 parts or an ULX3S `.lpf`.

## Reusable blocks

| Block | Path | Top module | Language | Vendor primitives | License |
|---|---|---|---|---|---|
| USB FS CDC-ACM device core | `usb_cdc/*.v` | `usb_cdc` | Verilog-2001 | none (README claims no EBR use; not independently re-verified beyond reading the source, which has no `SB_*`/`EHX*` instantiations) | MIT |

## Reuse notes

- **Ports** (`usb_cdc/usb_cdc.v:8-47`): `clk_i` (must run at `12 MHz *
  BIT_SAMPLES`, default `BIT_SAMPLES=4` → **48 MHz**), `rstn_i` (async,
  active-low), optional `app_clk_i` when `USE_APP_CLK=1` (lets the
  IN/OUT FIFO application side run on its own async clock, e.g. a slower SoC
  clock — the TinyFPGA-BX demo uses `APP_CLK_FREQ=2` MHz). Application side is
  a simple valid/ready byte-stream FIFO interface (`out_data_o`/`out_valid_o`/
  `out_ready_i`, `in_data_i`/`in_valid_i`/`in_ready_o`), one byte lane per
  channel. Key parameters: `VENDORID`, `PRODUCTID`, `CHANNELS` (1–7),
  `IN_BULK_MAXPACKETSIZE`/`OUT_BULK_MAXPACKETSIZE` (8/16/32/64),
  `BIT_SAMPLES` (oversampling of the 12 Mbit/s bit clock).
- **PHY pins** are exposed raw, not wrapped in vendor I/O primitives:
  `dp_pu_o` (drive the 1.5 kΩ pull-up enable), `tx_en_o` (output-enable for
  the D+/D- tristate pair), `dp_tx_o`/`dn_tx_o` (drive when enabled),
  `dp_rx_i`/`dn_rx_i` (read back). The board wrapper is expected to instantiate
  its own tristate I/O buffer per pin and a separate pull-up-enable pin/pad —
  see the SB_IO-based reference wiring in
  `examples/TinyFPGA-BX/hdl/demo/demo_fpga.vhd:170-232`.
- **Porting to ULX3S (ECP5)**: no vendor primitives in the core itself, so the
  gate-level logic should synthesize unchanged with `synth_ecp5`. What must be
  supplied is a board top-level that: (1) generates 48 MHz (`BIT_SAMPLES=4`)
  from the 25 MHz oscillator via an `EHXPLLL` instance; (2) drives ULX3S's
  direct-FPGA USB pins, which on `ulx3s_v20.lpf` are `usb_fpga_bd_dp`/
  `usb_fpga_bd_dn` (bidirectional D+/D-, `SITE "D15"`/`"E15"`, `IO_TYPE=LVCMOS33`)
  tristated by `tx_en_o`, plus the **separate** `usb_fpga_pu_dp`/`usb_fpga_pu_dn`
  pull-up/pull-down control pins (`SITE "B12"`/`"C12"`) — `dp_pu_o` should
  drive `usb_fpga_pu_dp` high (device mode = D+ pull-up only), leaving
  `usb_fpga_pu_dn` low, mirroring the TinyFPGA-BX `usb_pu`/`dp_pu` pattern but
  with independent D+/D- control (ULX3S's US2 also supports host mode, which
  TinyFPGA-BX's fixed pull-up doesn't need to model). Note ULX3S also has a
  separate, non-bidirectional `usb_fpga_dp`/`usb_fpga_dn` pin pair (`SITE
  "E16"`/`"F16"`, "single ended or differential input only" per
  `original_sources/emard__ulx3s/doc/constraints/ulx3s_v20.lpf:212-223`) — the
  `_bd_` pair is the one that matches this core's bidirectional tristate I/O
  model.
- No RAM/EBR usage claimed by the README; useful where LUTs are cheap but
  block RAM is needed elsewhere.
- **Correction to the survey brief**: the task notes said to "check its ULX3S
  example", but this repo has **no ULX3S example or `.lpf`** — only Fomu and
  TinyFPGA-BX. `catalogue.tsv`'s row is correct on this point
  ("examples/Fomu/…; examples/TinyFPGA-BX/…", target FPGAs listed as
  iCE40 UP5K/LP8K, "not ULX3S"). The D+/D-/pull-up wiring above was worked out
  by reading the TinyFPGA-BX VHDL top-level and the ULX3S `.lpf`, not from a
  ULX3S example in this repo.

## Open questions

- Whether the README's "no EBR" claim holds after `synth_ecp5` (not
  synthesized here).
- Full-speed USB timing margins for a bit-banged D+/D- pair on ULX3S's US2
  traces are unverified — the TinyFPGA-BX/Fomu boards this was designed for
  have short, controlled-impedance USB traces to the connector; ULX3S's
  routing to its USB-C/micro connector is unknown without checking the board
  schematic.
- No `iCEcube2` project or `.pcf` was read in detail (Lattice-only flow, out
  of scope for the open-flow toolchain this repo's catalogue entry targets).
{% endraw %}
