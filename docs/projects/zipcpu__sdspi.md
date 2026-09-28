<!-- Generated from data/projects/zipcpu__sdspi.json by .claude/skills/documentation/gen_pages.py; do not edit. -->

# SD-Card controller (`zipcpu__sdspi`)

| Field | Value |
|---|---|
| Upstream | https://github.com/ZipCPU/sdspi |
| Reviewed at | `dfb16c8` (upstream date 2026-08-01), reviewed 2026-09-28 |
| License | GPL-3.0 (per-file headers, e.g. `rtl/spi/sdspi.v:22` "License: GPL, v3"; `doc/src/gpl-3.0.tex` bundled; no top-level LICENSE/COPYING file) |
| HDL / framework | Verilog (85 `.v` files total: 37 in `rtl/`, 48 test/model files in `bench/`) |
| Toolchain | `open`: no synthesis-to-bitstream flow is shipped. Simulation: Verilator + Icarus Verilog (`bench/cpp`, `bench/verilog`); formal: SymbiYosys (`bench/formal/`). Integration is via `autodata/*.txt` (autofpga) or `sdspi.core` (FuseSoC, `sdspi.core:1`) |
| Programmer | n/a — core only, no board top or bitstream is produced by this repo |
| Target FPGA(s) | none — vendor-neutral; no `.pcf`/`.xdc`/`.lpf`/`.sdc` anywhere in the repo (verified: `find . -iname '*.lpf' -o -iname '*.pcf' -o -iname '*.xdc'` → no matches) |
| Board revision(s) | n/a. README names the XuLA2-LX25 (Xilinx Spartan-6) as the SPI controller's original target board (`README.md:18`) |
| Activity | last commit 2026-08-01 (`git log -1`). Commit count/first commit: unknown (shallow clone; not in `.claude/memory/history.tsv`) |

## What the gateware does

This is a library of three independent, drop-in Wishbone SD-card controllers — not a
ULX3S project. It has no board target, no top-level file, no constraints.

- **SPI-mode SD controller** — `rtl/spi/sdspi.v` (top) + `rtl/spi/llsdspi.v` (bit-level SPI engine)
  + `rtl/spi/spicmd.v`, `spirxdata.v`, `spitxdata.v`. Talks to an SD card over the legacy
  4-wire SPI mode. Older, simpler, "silicon proven" per `README.md:47`.
- **SDIO/eMMC controller** — `rtl/sdio/sdio.v` (Wishbone top) / `sdio_top.v`, with
  `sdcmd.v`, `sdckgen.v`, `sdfrontend.v`, `sdrxframe.v`, `sdtxframe.v`, `sddma.v`, and
  AXI variants `sdaxil.v`, `sdax_mm2s.v`, `sdax_s2mm.v`. Full SDIO protocol up to eMMC
  HS400 (`README.md:76-90`), Wishbone or AXI-Lite.
- **SDIO slave** — `rtl/sdslave/` — lets the FPGA impersonate an SD card (not reviewed in
  depth; out of scope for a ULX3S SD-reader design).

## Structure

- `rtl/spi/` — SPI-mode controller (5 files).
- `rtl/sdio/` — SDIO/eMMC controller (12 files) plus shared DDR/SERDES I/O primitives
  `rtl/xsdddr.v` and `rtl/xsdserdes8x.v` (used by `sdfrontend.v`).
- `rtl/sdslave/` — SDIO slave mode.
- `autodata/{sdspi,sdio}.txt` — ZipCPU `autofpga` glue (Wishbone address decode, top-level
  port names such as `o_sd_sck`, `io_sd_cmd`, `io_sd_dat`).
- `sdspi.core` — FuseSoC package descriptor for the SPI core + its Verilator testbench
  (`sdspi.core:8-13`).
- `bench/formal/` — ~60 SymbiYosys `.sby` proof/cover targets, one per submodule.
- `bench/cpp/`, `bench/verilog/` — C++ (Verilator) and Verilog SD/eMMC card models for
  simulation-based testing.
- `sw/` — `sdspidrv.c`/`sdiodrvr.c`, C drivers meant as a FATFS back end.

## How to build

Not run (core only, no synthesizable board top). From the root `Makefile`:

```
make rtl      # recurse into rtl/ Makefiles (lint/build checks)
make formal   # bench/formal: run all SymbiYosys proofs
make test     # formal + rtl, then bench/verilog and bench/cpp simulation tests
```

`bench/formal/Makefile` has ~60 individual `<module>_prf`/`_prfa`/`_prfc`/`_cvr`/`_cvra`
targets (one group per submodule: `llsdspi`, `sdspi`, `spicmd`, `sdckgen`, `sdcmd`,
`sdwb`, …) run via `sby`. To get a bitstream on a ULX3S, an integrator supplies their own
top-level module instantiating `sdspi` (or `sdio`) and a `.lpf`.

## Reuse notes

| Block | Path | Top module | Language | Vendor primitives | License |
|---|---|---|---|---|---|
| SPI-mode SD/MMC controller | `rtl/spi/{llsdspi.v,sdspi.v}` | `sdspi` | Verilog | none | GPL-3.0 |
| SDIO/eMMC controller (Wishbone) | `rtl/sdio/sdio.v` + `rtl/sdio/*.v` | `sdio` | Verilog | none by default (see below) | GPL-3.0 |
| DDR/SERDES I/O shim (SDIO front end) | `rtl/xsdddr.v`, `rtl/xsdserdes8x.v` | `xsdddr`, `xsdserdes8x` | Verilog | **Xilinx `ODDR`/`IDDR`** (hard-coded) | GPL-3.0 |

- **`sdspi` (SPI mode)**: Wishbone-B4 slave, `AW`/`DW`-parameterized (32-bit data). Key
  ports: `i_clk`, `i_sd_reset`, `i_wb_{cyc,stb,we,addr,data,sel}`, `o_wb_{stall,ack,data}`,
  `o_cs_n, o_sck, o_mosi`, `i_miso`, `i_card_detect`, `o_int` (`rtl/spi/sdspi.v:101-120`).
  Key params: `OPT_CARD_DETECT`, `LGFIFOLN` (FIFO size, default 7 → 512 B), `CKDIV_BITS`,
  `INITIAL_CLKDIV` (SPI clock = `clk/(2*(speed+1))`, comment in `rtl/spi/llsdspi.v:24-32`),
  `OPT_SPI_ARBITRATION` (share the SPI bus with e.g. an SPI-flash controller via
  `i_bus_grant`). Reset is a plain sync/async Wishbone reset, no special sequencing.
  **No vendor primitives** — synthesizes cleanly on ECP5 as-is. Straightforward reuse: wire
  `o_sck→sd_clk`, `o_mosi→sd_cmd` (SD SPI MOSI = CMD line), `i_miso←sd_d[0]` (SD SPI MISO =
  DAT0), `o_cs_n→sd_d[3]` (SD SPI CS = DAT3); the ULX3S `.lpf` names these `sd_clk`,
  `sd_cmd`, `sd_d[0]`, `sd_d[3]` (see below). This is the simplest, lowest-risk block to
  drop into a new ULX3S design that just needs FAT/raw block access to an SD card.
- **`sdio` (SDIO/eMMC mode)**: much larger, faster, and more complex; the default
  configuration (`OPT_SERDES=1'b0, OPT_DDR=1'b0` in `rtl/sdio/sdfrontend.v:62-63`) uses
  **plain single-data-rate I/O with no vendor primitives** (`GEN_NO_SERDES` generate branch,
  `rtl/sdio/sdfrontend.v:250-251`) — this configuration is portable and ECP5-safe.
  **Caution**: enabling `OPT_DDR=1` or `OPT_SERDES=1` (needed for the higher SDIO/eMMC
  speed grades) pulls in `rtl/xsdddr.v` and `rtl/xsdserdes8x.v`, both of which instantiate
  **Xilinx `ODDR`/`IDDR` primitives directly** (`rtl/xsdddr.v:97,146`, guarded only by
  `` `ifdef VERILATOR``/``IVERILOG`` for simulation, not by a vendor `` `ifdef``). Dropping
  DDR/SERDES SDIO into an ECP5 design requires **rewriting these two shim files** against
  ECP5 `ODDRX1F`/`IDDRX1F` (or `ODDRX2F`/`IDDRX2F` for the SERDES ratios) — the author
  explicitly designed `xsdddr`/`xsdserdes8x` as the "minimum number of components that
  need replacing when switching hardware platforms" (`rtl/xsdddr.v:9-11`). For a first
  ULX3S port, stick to `OPT_SERDES=0, OPT_DDR=0` (plain SDR SDIO, no primitives needed).
- **Wiring to the ULX3S SD slot**: the ULX3S `.lpf` (verified in
  `original_sources/emard__nes_ecp5/ulx3s_v20.lpf:113-128`, an ULX3S `ulx3s_v20.lpf` copy)
  names the signals `sd_clk` (site H2), `sd_cmd` (J1, MOSI/CMD), `sd_d[0]` (J3,
  MISO/DAT0), `sd_d[1]` (H1, DAT1/IRQ), `sd_d[2]` (K1, DAT2), `sd_d[3]` (K2, DAT3/CS),
  `sd_wp` (P5, not connected on that board), `sd_cdn` (N5, not connected). All six SD
  lines are **shared with the onboard ESP32's WiFi GPIOs** (14/15/2/4/12/13 per the LPF
  comments) — the ESP32 firmware must release/tristate them before the FPGA drives the
  card, and `sd_d[2]` is pulled `NONE` (not `UP`) because it doubles as an ESP32 boot-strap
  pin. `IOBUF … IO_TYPE=LVCMOS33 DRIVE=4` — no special I/O standard needed.
- Both controllers are Wishbone-B4 slaves designed to sit behind a DMA-capable master
  (ZipCPU + WB DMA per `README.md:33-36`); a soft CPU without WB DMA (e.g. PicoRV32, see
  `yosyshq__picorv32.md`) can still drive them with plain PIO register access, just without
  the multi-block burst optimizations.
- Formal proofs (`bench/formal/*.sby`) are a strong correctness signal but don't prove the
  DDR/SERDES front end (`README.md:96-99` states this explicitly — `sdfrontend.v` is
  verified only by simulation, not formally).
- `sw/sdspidrv.c` / `sw/sdiodrvr.c` are ready-made C driver back ends for the ELM-ChaN
  FATFS library (`README.md:32-33`), useful if pairing this core with a RISC-V SoC that
  wants a FAT filesystem instead of raw block access.

## Open questions

- Whether anyone has actually built `sdspi`/`sdio` into an ECP5/ULX3S bitstream: unknown —
  no ECP5 users found in this repo; README's known integrations are XuLA2 (Spartan-6),
  ZipCPU/eth10g and ZipCPU/videozip (unknown FPGA family, not checked here).
  Also worth reviewing `original_sources/` (if cloned) for those two projects.
- `rtl/sdslave/` (SDIO slave) not reviewed in detail — not directly relevant to a ULX3S
  "add SD storage" use case.
- Exact SPI clock ceiling reachable at 25 MHz ULX3S system clock: not computed (depends on
  `CKDIV_BITS`/`INITIAL_CLKDIV` choice and card tolerance) — unknown, would need bench
  testing on real hardware.
- Commit count / first-commit date: unknown (not in `history.tsv`, clone is shallow).
