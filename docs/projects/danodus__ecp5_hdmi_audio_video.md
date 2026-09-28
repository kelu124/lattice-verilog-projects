# ECP5 HDMI Audio + Video Transmitter (`danodus__ecp5_hdmi_audio_video`)

| Field | Value |
|---|---|
| Upstream | https://github.com/danodus/ecp5_hdmi_audio_video |
| Reviewed at | `a4710f9` (upstream date 2026-05-19), reviewed 2026-09-28 |
| License | MIT (`LICENSE`: Copyright (c) 2026 Daniel Cliche, Copyright (c) 2019 Sameer Puri) |
| HDL / framework | Verilog-2001 (21 `.v` files: 11 in `rtl/`, 2 shared test-app generators in `boards/common/`, 4 each in `boards/ulx3s/` and `boards/icepi_zero/`) |
| Toolchain | `open` (yosys + nextpnr-ecp5 + ecppack, via oss-cad-suite; `boards/ulx3s/Makefile`) |
| Programmer | `fujprog` (`make prog`, `make prog-flash`); `openFPGALoader` also mentioned in README for IcePi Zero |
| Target FPGA(s) | **85F**, CABGA381, `--85k` (ULX3S) — repo also targets IcePi Zero (25F, CABGA256, `--25k`), not covered here |
| Board revision(s) | v3.1.7 (`boards/ulx3s/ulx3s_v316.lpf`, also valid for v3.1.6 per this collection's board notes); comment in `ulx3s_top.v:2` says "ULX3S v3.1.7 HDMI demo" |
| Activity | last commit 2026-05-19 (`a4710f9`, "Add custom mode 1024x600 ~61Hz (VIC=0)"); commit count / first commit unknown (shallow clone, repo not in `.claude/memory/history.tsv`) |

## What the gateware does
A reusable **HDMI audio + video transmitter** stack (top module `hdmi`,
`rtl/hdmi.v`) — TMDS video encode, HDMI data-island packets (audio sample,
audio clock regeneration, AVI/SPD/vendor infoframes) and an ECP5-specific
TMDS serializer — ported from the hdl-util/hdmi SystemVerilog project into
plain Verilog-2001, plus a small test application wired up for two boards.
For ULX3S (`boards/ulx3s/ulx3s_top.v`, top module `ulx3s_top`), the demo
drives **EIA-189A colour bars** and a **440 Hz** stereo sine wave at 48 kHz
LPCM out over HDMI, selectable at build time between four video modes (VIC):
0 (1024×600 custom, ~61 Hz, 50 MHz pixel clock), 1 (640×480p60, 25.2 MHz,
default), 4 (1280×720@~60 Hz, ~74 MHz) and 34 (1920×1080@~30 Hz, ~74 MHz).

## Structure
- `rtl/` — the portable transmitter stack: `hdmi.v` (top), `hdmi_tmds_channel.v`
  (per-channel TERC4/TMDS encode), `hdmi_serializer_ecp5.v` (**ECP5-specific**,
  see Reuse notes), `hdmi_packet_assembler.v`/`hdmi_packet_picker.v` (data
  island scheduling), `hdmi_audio_*` (audio sample packet, clock
  regeneration packet, clk_gen), `hdmi_*_info_frame.v` (AVI, SPD, vendor
  infoframes).
- `boards/common/` — `color_bars.v`, `sine_gen.v` (shared test-pattern/tone
  generators), `video_config.vh` (per-VIC timing/`CLK_HZ` macros).
- `boards/ulx3s/` — `ulx3s_top.v` (top), `hdmi_pll.v` / `hdmi_pll_50.v` /
  `hdmi_pll_hd.v` (one `EHXPLLL`-based PLL per VIC group), `ulx3s_v316.lpf`,
  `Makefile`.
- `boards/icepi_zero/` — equivalent files for the other target board (not
  reviewed in depth here; out of scope per the brief).

## How to build
Not run (read-only review). From `README.md` / `boards/ulx3s/Makefile`:
```
source ~/oss-cad-suite/environment
cd boards/ulx3s
make VIC=1 bitstream    # default; also VIC=0, 4, 34
make VIC=1 prog         # fujprog
make VIC=1 prog-flash   # fujprog -j flash
```
Internally: `yosys` (`synth_ecp5 -top ulx3s_top`) → `nextpnr-ecp5 --85k
--package CABGA381 --freq 25` (`--timing-allow-fail --randomize-seed` added
for VIC 0/4/34, per the Makefile) → `ecppack --compress`. VIC must match
`hdmi_pll*.v`'s `CLK_HZ` in `boards/common/video_config.vh` or the 48 kHz
audio sample rate drifts (README).

## Reusable blocks

| Block | Path | Top module | Language | Vendor primitives | License |
|---|---|---|---|---|---|
| HDMI transmitter (video+audio+infoframes) | `rtl/*.v` | `hdmi` | Verilog-2001 | none directly (all vendor I/O is isolated in `hdmi_serializer_ecp5.v`) | MIT |
| ECP5 TMDS serializer | `rtl/hdmi_serializer_ecp5.v` | `hdmi_serializer_ecp5` | Verilog-2001 | `ODDRX1F` (×3 or ×4 depending on `TMDS_CLOCK_DDR`) | MIT |
| ULX3S 25→pixel/serial PLL | `boards/ulx3s/hdmi_pll*.v` | `hdmi_pll` / `hdmi_pll_50` / `hdmi_pll_hd` | Verilog | `EHXPLLL` | MIT |

## Reuse notes
- **`hdmi` top ports/parameters** (`rtl/hdmi.v:4-42`): `clk_pixel_x5` (serial
  clock), `clk_pixel`, `sample_strobe` (one-cycle 48 kHz pulse), `reset`,
  `rgb[23:0]`, `audio_sample_word_0/1` (`AUDIO_BIT_WIDTH`-wide, signed),
  `tmds[2:0]`/`tmds_clock` (single-ended internal signals, unused by the
  ULX3S top) and `tmds_p[3:0]`/`tmds_n[3:0]` (the ones actually driven out).
  Parameters cover `VIDEO_ID_CODE` (CEA VIC), full frame/screen/sync timing,
  `TMDS_CLOCK_DDR`, `TMDS_DIFFERENTIAL`, `AUDIO_RATE`/`AUDIO_BIT_WIDTH`,
  `VENDOR_NAME`/`PRODUCT_DESCRIPTION` (SPD infoframe strings).
- **`hdmi_serializer_ecp5`** (`rtl/hdmi_serializer_ecp5.v:1-103`): takes three
  10-bit TMDS-encoded channels, shifts them out 2 bits/cycle on `clk_serial`
  (5× `clk_pixel`) through `ODDRX1F` (`SCLK=clk_serial`, `RST` tied low). With
  the defaults used by the ULX3S demo (`TMDS_CLOCK_DDR=0`,
  `TMDS_DIFFERENTIAL=0`), only `tmds_p[3:0]` is driven (clock lane is SDR,
  fed straight from `clk_pixel`) and `tmds_n` is forced to `4'b0000` — this is
  intentional, not a bug: ULX3S's GPDI pins are constrained
  `IO_TYPE=LVCMOS33D` (`boards/ulx3s/ulx3s_v316.lpf:348-355`), a true-LVDS
  pad type where driving only the P leg is sufficient; the N leg is generated
  by the pad hardware, not by RTL.
- **PLLs** (`boards/ulx3s/hdmi_pll.v`): each is a single `EHXPLLL` with
  `CLKI_DIV=25` (25 MHz in), producing `CLKOS` = 5× pixel clock (serial) and
  `CLKOS2` = pixel clock, e.g. 126 MHz / 25.2 MHz for VIC 1. One PLL file per
  VIC group (`hdmi_pll.v` for VIC 1, `hdmi_pll_50.v` for VIC 0, `hdmi_pll_hd.v`
  for VIC 4/34) — reuse the `CLKI_DIV`/`CLKOS_DIV`/`CLKFB_DIV` pattern to
  retarget other pixel clocks from a 25 MHz ULX3S oscillator.
- **Drop-in reuse**: this repo already targets ULX3S directly (25 MHz clock,
  `ulx3s_v316.lpf`, 85F/CABGA381), so `rtl/` + `boards/ulx3s/` can be used
  close to as-is; swap `boards/common/color_bars.v`/`sine_gen.v` and the
  `rgb`/`audio_sample_word_*` drive in a new top-level for a real video/audio
  source. Note `ulx3s_v316.lpf` (v3.1.6/v3.1.7 pinout) — repoint to
  `ulx3s_v20.lpf` pin names for v2.x/v3.0.x boards per this collection's
  board notes.
- **Licensing**: MIT-licensed by this repo, but portions are "ported from
  hdl-util/hdmi" (`README.md:67`), whose own attribution note says
  `SPDX-License-Identifier: MIT OR Apache-2.0` (`README.md:78-81`); the ECP5
  serializer is "adapted from BrunoLevy/learn-fpga ULX3S_hdmi examples"
  (`README.md:82`, no explicit upstream license stated for that portion). The
  README also carries an **HDMI Adopter licensing note**: "for development
  and education. Commercial products with HDMI connectors may require HDMI
  Adopter licensing" (`README.md:72-74`) — worth flagging to anyone reusing
  this for a shipping product.

## Open questions
- `boards/icepi_zero/` was not reviewed in detail (out of scope: the brief
  asked to focus on the ULX3S top).
- Whether VIC 4/34 (`--timing-allow-fail`, random-seed nextpnr) close timing
  reliably was not tested — the Makefile itself documents needing to retry
  with `make clean && make VIC=4 bitstream` on failure.
- No `hdmi_packet_assembler.v`/`hdmi_packet_picker.v` internals were read
  beyond line counts; infoframe payload correctness (EDID/CEC interplay) not
  verified against the HDMI spec.
