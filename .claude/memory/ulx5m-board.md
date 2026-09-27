---
name: ulx5m-board
description: ULX5M-GS is Radiona/intergalaktik's CM4-form-factor board with a Cologne Chip GateMate CCGM1A1, NOT an ECP5 — different toolchain and constraint format
metadata:
  type: reference
---

**Owner decision 2026-09-27: ULX5M-GS is excluded from the catalogue and sources** (its 3 repos were
added, then removed on request). Kept here only as board knowledge; do not re-add without asking.

ULX5M = third board of the ULX3S → ULX4M line, built under the openCologne (NLnet) project.
The Lattice ECP5 is **replaced by a Cologne Chip GateMate CCGM1A1**; form factor is the Raspberry Pi
Compute Module 4 (like ULX4M). Variants: **ULX5M-GS** (CM4 module, SDRAM) and **ULX5M-M2** (GateMate on an
M.2 card, hardware only, `intergalaktik/ulx5m-m2`, not cloned).

Verified (2026-09-27):
- Hardware repo `intergalaktik__ulx5m-gs@61b6709f`: KiCad, CERN-OHL-S v2+, README says use **v005**;
  **GPIO default 1.8 V, SDRAM part 1.8 V, VCC core 0.9 V (1.1 V needed for SerDes)**.
- Toolchain (`pu-cc__ulx5m_gpiocheck@402f6517` Makefile): `yosys synth_gatemate` → `nextpnr-himbaechel
  --device CCGM1A1` → `gmpack`; load with `openFPGALoader -b gatemate_evb_jtag` or `-c gatemate_pgm`.
  Constraints are **`.ccf`** (not `.lpf`); that repo's `src/top.ccf` is the only public ULX5M-GS pin file found.
- LiteX: `litex-boards` has `intergalaktik_ulx5m_gs.py` (not cloned).

Unverified (README of `goran-mahovlic__ulx5m-litex-ai`): 64 MB SDRAM IS42VM16320E, gigabit PHY KSZ9031
(RGMII), DVI out, 25 MHz clock, SerDes lane to the M.2 card.

**How to apply:** ULX3S cores (ECP5 primitives: EHXPLLL, ODDRX1F, DP16KD, `.lpf`) do not port as-is; PLL,
DDR I/O, BRAM and constraints must be redone for GateMate. See also [[board-hardware]], [[toolchain-and-programming]].
