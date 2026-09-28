# Hackaday Supercon 2019 badge SoC (`spritetm__hadbadge2019_fpgasoc`)

| Field | Value |
|---|---|
| Upstream | https://github.com/Spritetm/hadbadge2019_fpgasoc |
| Reviewed at | `6e706d5` (upstream date 2023-11-30), reviewed 2026-09-28 |
| License | No single top-level license: per-file SPDX-less headers referencing one of `LICENSE.bsd`, `LICENSE.gplv3`, `LICENSE.lgpl3`, `LICENSE.mit`, `LICENSE.beerware`, `LICENSE.fatfs` (root). Submodule `soc/picorv32` is ISC-style (Clifford Wolf header); `soc/picorv32/tests/LICENSE` is BSD-3-Clause (RISC-V tests, unrelated to the core itself) |
| HDL / framework | Verilog (95 files, own) + submodule `soc/picorv32` (41 files) |
| Toolchain | `open`: yosys (`synth_ecp5 -abc9`) + nextpnr-ecp5 + ecppack, via `soc/Makefile`. Docs recommend a prebuilt `xobs/ecp5-toolchain` (per repo docs, not independently verified) |
| Programmer | `openocd` (SVF over JTAG, `soc/openocd.cfg`) or `dfu-util` (DFU class 1d50:614a/614b, once the DFU IPL is running) |
| Target FPGA(s) | 45F — `LFE5U-45F-6BG381`, `nextpnr-ecp5 --45k --package CABGA381` (`soc/Makefile`) |
| Board revision(s) | Hackaday Supercon 2019 badge only: `had19_proto1.lpf`/`proto2`/`proto3`/`prod.lpf`, selected by `BADGE_VER` (1–4); **not** a ULX3S board |
| Activity | single commit at the pinned clone depth (shallow, `--depth 1`); upstream date 2023-11-30; commit count/first commit unknown (`.claude/memory/history.tsv` has no entry) |

## What the gateware does
A complete **badge SoC**: PicoRV32 RISC-V CPU, 16 MB of interleaved QPI-PSRAM as main
memory, tile/sprite video out over HDMI/GPDI, a PDM audio synth, a soft-PHY USB2 device,
plus a DFU/IPL boot chain and a large collection of badge apps (games, demos, a BASIC
interpreter). Top module `top_fpga` (`soc/top_fpga.v`); the CPU/bus/peripheral glue is in
`soc/soc.v`.
- **PicoRV32 CPU + Wishbone-ish bus** — `soc/soc.v` (`module soc`), `soc/arbiter.v`. Custom
  fast multiplier via ECP5 DSP: `soc/pcpi_fastmul_dsp.v` + `soc/mul_18x18_ecp5.v`.
- **QPI PSRAM (2× interleaved 8 MB chips, 16 MB total)** — `soc/qpi_cache/` (see Reuse
  notes). `soc/soc.v:57-64` exposes two independent PSRAM chip interfaces
  (`psrama_*`/`psramb_*`); `soc/soc.v:165` comments "top of 16 MByte PSRAM" per CPU
  region, and `qpimem_dma_rdr.v:33` notes "interleaved psram @ 48MHz".
- **Video** — tile/sprite 2D renderer (`soc/video/vid_linerenderer.v`, `vid_spriteeng.v`,
  `video_alphamixer.v`) feeding an HDMI/GPDI TMDS encoder (`soc/hdmi/`).
- **Audio** — an 8-voice wavetable synth (`soc/audio/synth_core.v`) mixed down
  (`audio_mix.v`) and output as 1st-order dithered PDM (`soc/audio/pdm.v`).
- **USB2 device** — a from-scratch, bit-banged full-speed device PHY + link layer
  (`soc/usb/`), used for the DFU bootloader and badge-to-host communication
  (`soc/usb_soc.v`).
- **PIC16F84-compatible softcore** (`soc/pic/`) — used as an LCD/IPL helper co-processor;
  not investigated further (out of scope for this pass).
- **DFU/IPL bootloader + apps** — `soc/ipl/` (with `tinyusb`, `elfload`, `lodepng`, `yxml`
  submodules) and ~14 `app-*/` directories (games/demos), out of scope here.

## Structure
- `soc/Makefile` — the SoC build (badge-specific; see How to build).
- `soc/soc.v` — CPU + bus + all peripheral instantiation and address decode.
- `soc/top_fpga.v` — top-level pad/pin glue, instantiates `sysmgr`, `soc`, PHYs.
- `soc/sysmgr.v` — PLL/reset manager (see Reuse notes: clock tree).
- `soc/qpi_cache/`, `soc/hdmi/`, `soc/video/`, `soc/audio/`, `soc/usb/` — the reusable
  cores documented below.
- `soc/picorv32/` — `cliffordwolf/picorv32` submodule, pinned at
  `e0baf2e0bd49fdddef2e3440c1f6364478655154` (per `.claude/memory/submodules.tsv`), the
  standard single-file RV32I core, ISC-style license.
- `soc/had19_prod.lpf` (and `proto1`–`proto3` variants) — badge-specific pin constraints.
- `app-*/`, `blink/`, `soc/ipl/` — badge applications and bootloader, not covered by this
  pass (brief scope: qpi_cache, video, audio, USB only). DFU/bootloader details for the
  ULX3S ecosystem are covered separately in `../DFUs.md`.

## How to build
Not run. Exact commands from `soc/Makefile`:
```
make            # -> soc.svf (yosys synth_ecp5 -abc9 -> nextpnr-ecp5 --45k --package CABGA381
                #    --speed 8 --freq 48 --seed 37 -> ecpbram (BRAM init) -> ecppack --svf)
make prog       # openocd -f ../openocd.cfg -c "init; svf soc.svf; exit"
make dfu_flash  # dfu-util -d 1d50:614a,1d50:614b -a 0 -R -D soc.bit
make verilator  # full-SoC/video simulation (SDL output), needs sdl2-config
```
`BADGE_VER` (default 4 = prod) selects the LPF/hardware-define set. Flash timing:
`FLASH_MODE=qspi`, `FLASH_FREQ=38.8` MHz. `TRELLIS=/usr/share/trellis` is hard-coded and
would need overriding for other installs (same pattern as the emard "universal make" repos
per `reusable-cores.md`).

Self-checking testbenches (iverilog, `$display` mismatch + `$finish`), not run here:
`soc/qpi_cache/qpimem_iface_testbench.v`, `qpimem_cache_testbench.v`,
`qpimem_interleave_testbench.v`, `soc/pcpi_fastmul_dsp_testbench.v`. `make verilator`
(full SoC + video, SDL) is visual/waveform-only, no pass/fail.

## Reuse notes

### Reusable blocks

| Block | Path | Top module | Language | Vendor primitives | License |
|---|---|---|---|---|---|
| QPI PSRAM PHY (2×2-wide interleave) | `soc/qpi_cache/qspi_phy_2x_ecp5.v` | `qspi_phy_2x_ecp5` | Verilog | `ODDRX1F` (×2), `IDDRX1F`, `TRELLIS_IO` (bidir), `OFS1P3DX` | BSD-3 |
| QPI PSRAM link-layer (dual interleaved chips) | `soc/qpi_cache/qpimem_iface_2x2w.v` | `qpimem_iface_2x2w` | Verilog | none (drives the PHY above) | BSD-3 |
| QPI PSRAM link-layer (single/other variants) | `soc/qpi_cache/qpimem_iface.v`, `qpimem_iface_intl.v` | `qpimem_iface`, `qpimem_iface_intl` | Verilog | none | BSD-3 |
| 2-way direct-mapped cache in front of PSRAM | `soc/qpi_cache/qpimem_cache.v` | `qpimem_cache` | Verilog | none (pure logic; parametric `CACHELINE_WORDS`/`CACHELINE_CT`/`ADDR_WIDTH`) | BSD-3 |
| PSRAM bus arbiter / DMA reader | `soc/qpi_cache/qpimem_arbiter.v`, `qpimem_dma_rdr.v` | `qpimem_arbiter`, `qpimem_dma_rdr` | Verilog | none | BSD-3 |
| HDMI/DVI TMDS encode + serialize | `soc/hdmi/vga2dvid.v`, `tmds_encoder.v` | `vga2dvid`, `tmds_encoder` | Verilog (vhd2vl-translated from Mike Field's "hamsterworks" VHDL) | `fake_differential.v` uses `ODDRX1F` for DDR TMDS serialization; `vga2dvid`/`tmds_encoder` themselves are primitive-free | MIT (Mike Field, 2012, header in `vga2dvid.v`/`tmds_encoder.v`); `fake_differential.v` and `hdmi-encoder.v` have **no license header** (not covered by any `LICENSE.*` reference found) |
| Audio wavetable synth core | `soc/audio/synth_core.v` | `synth_core` | Verilog | none | BSD-3 |
| PDM DAC (1st-order, dithered) | `soc/audio/pdm.v` | `pdm` (+ helper `pdm_lfsr`) | Verilog | none; parametric `WIDTH` (8-bit shown), `PHY="GENERIC"` | BSD-3 |
| USB2 full-speed device PHY + link | `soc/usb/usb_phy.v`, `usb.v`, `usb_trans.v`, etc. | `usb_phy`, `usb` | Verilog | `usb_phy.v` has an `ECP5` branch using `TRELLIS_IO` (bidir, bit-banged D+/D-, manual input latching since "ecp5 io isn't latching"); rest of `soc/usb/` is primitive-free | LGPL-3.0-or-later (`usb.v`, `usb_phy.v` headers) |
| SoC top glue (PSRAM/USB/etc. wiring) | `soc/usb_soc.v` | `usb_soc` | Verilog | none | BSD-3 |
| Clock/reset manager | `soc/sysmgr.v` | `sysmgr` | Verilog | `EHXPLLL` | BSD-3 |

### Notes
- **QPI PSRAM controller (`soc/qpi_cache/`)**: cleanly layered — `qspi_phy_2x_ecp5.v` is the
  only ECP5-primitive-dependent file (DDR IO via `ODDRX1F`/`IDDRX1F` plus `TRELLIS_IO`
  tristate buffers); everything above it (`qpimem_iface_2x2w`, `qpimem_cache`,
  `qpimem_arbiter`, `qpimem_dma_rdr`) is portable Verilog. It targets **two** Lyontek
  LY68L6400 QPI PSRAM chips (8 MB each, interleaved for a 16-bit-wide effective bus /
  16 MB total) — confirmed by the bundled behavioral model
  `soc/qpi_cache/ly68l6400_model.v` and the `//ly68l6400:` comments in
  `qpimem_iface.v:69` and `qpimem_iface_intl.v:36`. Clock: the PHY runs on `clk_2x`/`clk_1x`
  (from `sysmgr`'s 96/48 MHz PLL outputs — see below) and the interleave comment pins the
  interleaved-PSRAM design point at 48 MHz (`qpimem_dma_rdr.v:33`). To reuse on a ULX3S: a
  ULX3S has no on-board QPI PSRAM (it's SDR SDRAM), so this only applies if pairing with an
  add-on PSRAM board carrying the same or a compatible QPI-mode chip; pin remap via a new
  LPF is required either way, and using a single chip instead of two would mean dropping
  the interleave and using `qpimem_iface.v` directly instead of `qpimem_iface_2x2w.v`.
- **`soc/sysmgr.v` clock tree**: one `EHXPLLL` takes an **8 MHz** input
  (`FREQUENCY_PIN_CLKI="8"`, `soc/had19_prod.lpf:2` confirms "8MHz clock" on the badge) and
  produces 96 MHz (`CLKOP`), 48 MHz (`CLKOS`), and 24 MHz (`CLKOS2`). ULX3S's board
  oscillator is 25 MHz, not 8 MHz, so the PLL divider/multiplier constants in `sysmgr.v`
  would need recomputing (e.g. with EMARD's `ecp5pll.sv` generator used elsewhere in the
  collection) rather than reused as-is.
- **HDMI/TMDS (`soc/hdmi/`)**: `vga2dvid.v`/`tmds_encoder.v` are the same well-known
  Mike Field "hamsterworks" HDMI core (MIT) that appears all over the ULX3S ecosystem
  (`reusable-cores.md`); only `fake_differential.v`'s DDR serialization
  (`ODDRX1F`) is ECP5-specific and is directly usable on ULX3S GPDI pins (same fake-diff
  pseudo-differential trick as `emard__ulx3s-misc`). `hdmi-encoder.v` and
  `clk_8_250_125_25.v` are badge-specific glue/PLL and would be replaced by a
  ULX3S-appropriate pixel-clock PLL.
- **Audio (`soc/audio/`)**: `synth_core.v` and `pdm.v` have no vendor primitives at all —
  fully portable. `pdm.v` is parametric (`WIDTH`, `PHY="GENERIC"`) and outputs a single PDM
  bitstream per channel (`audio_out_dc` is a separate 12-bit DC/bias output from
  `synth_core`); only the output pin assignment in a new LPF is needed to reuse it on
  ULX3S (e.g. feeding an RC filter to a GPIO, as ULX3S has no dedicated audio DAC).
- **USB device (`soc/usb/`)**: this is a **soft, bit-banged full-speed device PHY** — no
  external ULPI/USB3300 PHY chip is needed, just two GPIO pins (D+/D-) with the usual
  1.5 kΩ pull-up. The `usb_phy.v` `TARGET="ECP5"` branch is exactly the pattern needed for
  ULX3S's US2 direct-USB port (which is also bare D+/D- GPIO, no PHY chip). This makes it
  one of the more directly reusable USB device cores in the collection, alongside
  `smunaut__ice40-playground`'s `no2usb` (same author, similar architecture, LGPL vs
  CERN-OHL-P licensing difference to note). License is LGPL-3.0-or-later (copyleft on
  modifications to `usb.v`/`usb_phy.v` themselves, not on code merely linked against it).
- **License caution**: this repo mixes BSD-3, LGPL-3+, GPLv3, MIT, Beerware and
  license-less files in one tree with no single top-level grant; reusers must keep the
  per-file header attached (e.g. `qpi_cache/*.v` and `sysmgr.v`/`usb_soc.v` are BSD-3, but
  `usb/usb.v` is LGPL-3+, and `hdmi/fake_differential.v` + `hdmi-encoder.v` have no
  license statement at all — treat those two as all-rights-reserved until clarified with
  upstream).

## Open questions
- `fake_differential.v` and `hdmi-encoder.v` license is unclear (no header found); would
  need to ask upstream (Sylvain Munaut / Jeroen Domburg) before redistributing.
- `soc/pic/` (PIC16F84 softcore) role and portability not investigated (out of brief scope).
- Whether `LY68L6400` (or a pin-compatible QPI PSRAM) is available as a ULX3S add-on board
  is unverified — no such board is catalogued yet in this repo's survey.
- Commit count / first-commit date for full-history stats not recorded in
  `.claude/memory/history.tsv`.
- DFU bootloader details are covered separately; see `../DFUs.md`.
