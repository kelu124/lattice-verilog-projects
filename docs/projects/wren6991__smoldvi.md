---
title: "wren6991__smoldvi"
parent: "Project reviews"
nav_order: 17
---
<!-- Generated from data/projects/wren6991__smoldvi.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# SmolDVI (`wren6991__smoldvi`)

| Field | Value |
|---|---|
| Upstream | https://github.com/Wren6991/SmolDVI |
| Reviewed at | `e8b8f87` (upstream date 2021-07-15), reviewed 2026-09-28 |
| License | CC0-1.0 (`LICENSE.md`) |
| HDL / framework | Verilog (12 `.v` files) |
| Toolchain | `open` (yosys + nextpnr-ice40 + icepack/icetime, via `synth/{Icebreaker,Icestick,Icesugar,TinyFPGA_BX}.mk` + `synth/Makefile`, driven by the `Wren6991/fpgascripts` submodule) |
| Programmer | board-specific, invoked from the per-board `.mk` (e.g. iCEBreaker `prog` target); not read in detail here |
| Target FPGA(s) | iCE40 UP5K (iCEBreaker, iCESugar), iCE40 HX1K (iCEstick), iCE40 LP8K (TinyFPGA BX) — **not ECP5, no ULX3S target in this repo** |
| Board revision(s) | n/a — repo does not target ULX3S |
| Activity | last commit 2021-07-15 (`e8b8f87`, "Port to TinyFPGA BX"); commit count / first commit unknown (shallow clone, repo not in `.claude/memory/history.tsv`) |

## What the gateware does

A small, portable direct DVI/TMDS video-output core (top module `smoldvi`,
`hdl/smoldvi/smoldvi.v`) that generates a pixel-doubled RGB666 640×480p60
(or configurable CEA-861D) DVI signal from an RGB pixel stream, using a
minimal ("stateless") TMDS encoder trick documented in
`hdl/smoldvi/smoldvi_tmds_encode.v` (~20 LUTs/lane, at the cost of halving
horizontal resolution and dropping the colour LSB — acceptable per the author
for the iCE40 UP5K/HX1K this was built for). Per-board top-level example
designs (`hdl/fpga/smoldvi_fpga_*.v`) drive a scrolling colour-gradient test
pattern out to a DVI PMOD on iCEBreaker, iCEstick, iCESugar and TinyFPGA BX.

## Structure

- `hdl/smoldvi/` — the portable core: `smoldvi.v` (top: timing + TMDS encode +
  serialise), `smoldvi_timing.v` (CEA-861D-style H/V counters, sync/den
  generation), `smoldvi_tmds_encode.v` (the stateless TMDS trick),
  `smoldvi_serialiser.v` (10:2 gearbox + DDR output, **not fully
  self-contained**, see Reuse notes), `smoldvi_fast_gearbox.v`,
  `smoldvi_clock_driver.v`.
- `hdl/fpga/` — per-board top levels + PLLs (`pll_12_126.v`, `pll_16_126.v`)
  and `.f` file lists.
- `synth/` — per-board Makefile fragments, `.pcf` pin constraints,
  `synth/Makefile` (shared rules).
- `hdl/libfpga` (git submodule, **not fetched** in this shallow clone —
  `.gitmodules` points at `https://github.com/Wren6991/libfpga.git`) supplies
  the platform `ddr_out` module and reset helpers used by the example
  top-levels.

## How to build

Not run (read-only review; the `hdl/libfpga` submodule is also absent, so a
build would fail as checked out). From `Readme.md`:

```
git clone --recursive https://github.com/Wren6991/SmolDVI.git smoldvi
cd smoldvi && . sourceme
cd synth && make -f Icebreaker.mk prog     # also: Icestick.mk, Icesugar.mk, TinyFPGA_BX.mk
```

No ECP5/ULX3S Makefile exists in this repo.

## Reusable blocks

| Block | Path | Top module | Language | Vendor primitives | License |
|---|---|---|---|---|---|
| Small DVI/TMDS core | `hdl/smoldvi/*.v` | `smoldvi` | Verilog | **none in `hdl/smoldvi/` itself** — see below for the one platform-specific dependency | CC0-1.0 |

## Reuse notes

- **Top module ports** (`hdl/smoldvi/smoldvi.v:18-35`): `clk_pix`/`rst_n_pix`
  (pixel-rate domain), `clk_bit`/`rst_n_bit` (bit-rate domain, must be
  **exactly 5× `clk_pix`**, common root oscillator, reset deassertion
  synchronised to each domain's clock — README, "Reusing" section), `en`,
  `r`/`g`/`b` (`RGB_BITS`-wide, 1–7 bits, default 6), `rgb_rdy` (pixel
  request/ready strobe), `dvi_p[3:0]`/`dvi_n[3:0]` (`{CK, D2, D1, D0}`, TMDS
  channel order Blue/Green/Red like other DVI cores in this collection). Key
  parameters: the full CEA-861D H/V timing set (front porch, sync width, back
  porch, active) plus `RGB_BITS`.
- **The only platform-specific piece is `ddr_out`** (per the author, in
  `Readme.md` "Reusing"): `smoldvi_serialiser.v:59-75` instantiates a module
  called `ddr_out` (2:1 DDR output buffer, ports `clk`, `rst_n`, `d_rise`,
  `d_fall`, `e`, `q`) that is **not itself in this repo** — it comes from the
  unfetched `hdl/libfpga` submodule and is compiled under `` `FPGA_ICE40 ``
  to become a `SB_IO` DDR primitive. Everything else in `hdl/smoldvi/` is
  plain, portable Verilog by the author's own description.
- **Porting to ULX3S (ECP5)**: supply (1) an `EHXPLLL` generating `clk_bit` =
  5× the desired pixel clock from the 25 MHz oscillator (e.g. 126 MHz for
  25.2 MHz / 640×480p60, matching the `pll_12_126`/`pll_16_126` naming
  convention already used for the iCE40 boards) with `clk_pix` derived from
  it (in-fabric ring-counter divide-by-5, as the iCEBreaker top-level does at
  `hdl/fpga/smoldvi_fpga_icebreaker.v:54-64`, or a second PLL output tap);
  (2) a `` `define FPGA_ECP5 ``-style `ddr_out` implementing the same
  `clk`/`rst_n`/`d_rise`/`d_fall`/`e`/`q` port list around `ODDRX1F` (one
  instance per TMDS lane, 4 total incl. clock) — the same primitive and DDR
  gearing already used by `danodus__ecp5_hdmi_audio_video`'s
  `rtl/hdmi_serializer_ecp5.v` in this collection, so that file is a good
  reference for the ECP5-specific half; (3) map `dvi_p`/`dvi_n` to
  `gpdi_dp[3:0]`/`gpdi_dn[3:0]` (`ulx3s_v316.lpf`, `IO_TYPE=LVCMOS33D`,
  ULX3S's GPDI pins auto-generate the complementary leg from a single-ended
  drive, as used by the emard `vga2dvid`/danodus `hdmi_serializer_ecp5`
  cores) instead of the SB_IO-based differential pads used on the iCE40
  boards.
- CC0-1.0 (public-domain-equivalent) license makes this one of the least
  encumbered DVI cores in the survey; RGB666 pixel-doubled 640×480p60 is
  small enough to be a good "just need a picture out" option compared to
  full hdl-util/hdmi-derived stacks when audio/HDMI infoframes aren't needed.

## Open questions

- `hdl/libfpga`'s exact `ddr_out.v` implementation was not read (submodule
  not fetched in this shallow clone; not in `.claude/memory/submodules.tsv`
  allowlist). The port list quoted above comes from the call site in
  `smoldvi_serialiser.v`, not from the module's own source.
- Whether `smoldvi_clock_driver.v` / `smoldvi_fast_gearbox.v` also assume any
  iCE40-specific behaviour (e.g. LUT-based shift register inference) was not
  checked line-by-line; the author's "everything in hdl/smoldvi is portable"
  claim is unverified beyond the explicit `ddr_out` callout.
{% endraw %}
