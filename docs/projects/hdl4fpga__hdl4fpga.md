---
title: "hdl4fpga__hdl4fpga"
parent: "Project reviews"
nav_order: 7
---
<!-- Generated from data/projects/hdl4fpga__hdl4fpga.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# hdl4fpga (`hdl4fpga__hdl4fpga`)

| Field | Value |
|---|---|
| Upstream | https://github.com/hdl4fpga/hdl4fpga |
| Reviewed at | `662986b` (upstream date 2025-08-17), reviewed 2026-09-28 |
| License | MIT (`LICENSE`, Miguel Angel Sagreras) for all VHDL/Verilog source checked (headers on every file spot-checked: `boards/ULX3S/common/ulx3s.vhd`, `boards/ULX3S/apps/{graphics,scopeio,ser_debug}.vhd`, `library/scope/scopeio.vhd`, `library/mii/mii_ipoe.vhd`, `library/sdram/sdram_ctlr.vhd`, `library/usb/usbhost.vhd`, `library/video/dvi.vhd`, `library/latticesemi/ecp5/ecp5_sdrphy.vhd`, `library/apps/ecp5_videodcm.vhd` — all carry the same MIT boilerplate as `LICENSE`, `grep -rl "gnu general public license" -i --include=*.vhd --include=*.v .` returns nothing). The GPL-3.0-or-later text only appears in the Diamond build **Makefiles** (`boards/ULX3S/diamond/Makefile`, `boards/ULX4M_LS/diamond/Makefile`, `boards/ULX4M_LD/diamond/Makefile`, `library/latticesemi/scripts/Makefile`, `library/xilinx/scripts/Makefile`), not in any HDL source — this corrects the catalogue's "mixed MIT/GPL" note, see Open questions. |
| HDL / framework | VHDL (this repo is ~all VHDL; the catalogue's "274" file count and the "Verilog, JS" entries refer to the wider repo — Micron DDR verification models (`library/micron/ddr{,2,3}/*.v`) and non-ULX3S board tooling — not to anything used by the ULX3S apps) |
| Toolchain | `diamond` only for ULX3S. `boards/ULX3S/diamond/apps.ldf` is a Lattice Diamond project (`synthesis="synplify"`, `device="LFE5U-12F-8BG381C"`) built via `boards/ULX3S/diamond/Makefile` (`diamondc` batch calls). No yosys/nextpnr-ecp5 flow exists for ULX3S. `boards/ULX3S/ghdl/app_graphics.sh` and `library/ghdl/*.sh` run `ghdl -a` (analysis/type-check only, `--std=02`) for the `graphics` app — this is a GHDL front-end syntax check, not a synthesis or simulation run, and there is no `nextpnr`/`yosys` call anywhere in the tree (`grep -rn "nextpnr\|yosys" boards/ULX3S library` → no hits). |
| Programmer | Not stated for ULX3S in this repo (Diamond produces a `.bit`/`.svf`; loading is left to the user — `openFPGALoader -b ulx3s` per CLAUDE.md convention, unverified here) |
| Target FPGA(s) | 12F (`apps.ldf` `device="LFE5U-12F-8BG381C"`, all three apps share one project/device) |
| Board revision(s) | v2.x / v3.0.x (`apps.lpf` header: `## ULX3S v2.x.x and v3.0.x`; pin names/sites match the `ulx3s_v20.lpf` convention from CLAUDE.md, e.g. `clk_25mhz` at `G2`, `gpdi_d[0..3]` at `A16/A14/A12/A17`) |
| Activity | Last commit to the whole monorepo `662986b`, 2025-08-17 (`git -C original_sources/hdl4fpga__hdl4fpga log -1 --format=%cs`). First commit 2013-06-05, 11860 commits total (`.claude/memory/history.tsv`, recorded before the clone was made shallow — commit count not independently verifiable from this `--depth 1` clone) |

## Scope of this page

hdl4fpga is a very large portable VHDL library (many boards: ULX3S, ULX4M_LS/LD,
arty, orangecrab, ml50x, …). This page covers only what is ULX3S-relevant:
the three `boards/ULX3S/apps/` designs and the reusable cores they pull in
(`library/scope`, `library/mii`, `library/sdram` + `library/latticesemi/ecp5`,
`library/usb`, `library/video`). The rest of `library/` (Xilinx/Altera
back-ends, other boards' apps, CPU/soft-core work) is out of scope.

## What the gateware does

`boards/ULX3S/common/ulx3s.vhd` declares one entity `ulx3s` whose port list is
the full ULX3S pin set from `apps.lpf` (clk_25mhz, ftdi_*, leds, buttons, sw,
oled_*, adc_*, sdram_*, gpdi_*, gp/gn, usb_fpga_*, wifi_*, sd_*, audio_*).
Each app in `boards/ULX3S/apps/` is a separate **architecture** of that same
entity, selected as the Diamond implementation (`apps.ldf` has one
implementation per architecture, default `ser_debug`; `boards/ULX3S/diamond/Makefile`
has matching `ser_debug`/`graphics`/`scopeio` targets):

- **`ser_debug`** (`boards/ULX3S/apps/ser_debug.vhd`, architecture `ser_debug`) —
  serial/USB debug console. Drives an 800x600@60Hz DVI/GPDI text display
  (`hdl4fpga.ecp5_videodcm`, 40 MHz pixel clock from 25 MHz) and a bidirectional
  link on US2 selectable at build time between USB (`usb_device` constant,
  `true`⇒`hdl4fpga.usbdev`, `false`⇒`hdl4fpga.usbhostdvr`+`hdl4fpga.usbphy`) or
  Ethernet (`io_link = "io_ipoe"`, via `hdl4fpga.ipoepkg`/`library/mii`).
- **`graphics`** (`boards/ULX3S/apps/graphics.vhd`, architecture `graphics`) —
  SDRAM-backed framebuffer/graphics demo: instantiates the generic
  `sdram_ctlr` against the ULX3S's actual SDR SDRAM chip
  (`chip_data => "MT48LC16M16MA2-7E"`, `sdram.dcm` 25→133 MHz via
  `hdl4fpga.ecp5_profiles.sdram_dcm`) and drives 800x600@60Hz over
  GPDI/DVI, again with a USB or Ethernet `io_link`.
- **`scopeio`** (`boards/ULX3S/apps/scopeio.vhd`, architecture `scopeio`) —
  the ScopeIO 8-input digital storage oscilloscope. Bit-bangs the onboard
  MAX1112x SPI ADC directly in this file (`adc_sclk`/`adc_csn`/`adc_mosi`/`adc_miso`,
  lines 751-957), stores samples in the SDR SDRAM (same `MT48LC16M16MA2-7E`
  chip data), and renders the waveform/grid/trigger UI at 1280x720@60Hz
  (64 MHz pixel clock) via `library/scope/scopeio.vhd`. This is the source
  for the `scope/` prebuilt bitstream catalogued in `emard__ulx3s-bin.md`
  (mouse GUI, 4-channel storage scope claim there — this repo's `scopeio.vhd`
  top sets `"inputs:" & "8"`, i.e. 8 channels are wired in the settings string
  though the ulx3s-bin doc says 4; not reconciled, see Open questions).

## Structure

- `boards/ULX3S/common/ulx3s.vhd` — shared `ulx3s` entity (port list = board pins).
- `boards/ULX3S/apps/{ser_debug,graphics,scopeio}.vhd` — one architecture each.
- `boards/ULX3S/diamond/{apps.ldf,apps.lpf,apps_video.lpf,Makefile}` — Diamond
  project, pin constraints (v2.x/v3.0.x), and `diamondc` batch build.
- `boards/ULX3S/ghdl/app_graphics.sh` — GHDL analysis-only script for `graphics`.
- `boards/ULX3S/testbenches/` — 8 files: `{ser_debug,graphics,scopeio}.vhd`
  testbenches with matching `.do` (ModelSim/Aldec) scripts, plus `eth_tb.vhd`
  and `graphics_structure.do`.
- `library/scope/` — ScopeIO core (`scopeio.vhd` + ~20 `scopeio_*` helper units:
  grid, trigger, storage, capture, downsampler, axis, palette, textbox…).
- `library/mii/` — Ethernet/IP stack (see Reuse notes).
- `library/sdram/` — portable multi-generation SDRAM/DDR controller.
- `library/latticesemi/ecp5/` — ECP5-specific SDRAM PHY + I/O gearbox primitives.
- `library/apps/ecp5_videodcm.vhd`, `ecp5_sdramdcm.vhd` — ECP5 `EHXPLLL`-based
  clock generators for video and SDRAM.
- `library/video/` — DVI/TMDS encoder, VGA/CGA text-mode helpers.
- `library/usb/` — USB 1.1 device (`usbdev.vhd`) and host (`usbhost.vhd`) cores.
- `library/basic/`, `library/hdlc/`, `library/sio/`, `library/uart/` — smaller
  reusable utility packages (not reviewed in depth here).
- `library/micron/{ddr,ddr2,ddr3}/*.v` — Micron's own bus-functional
  **simulation models** for DDR/DDR2/DDR3 chips (verification IP, not an
  hdl4fpga controller; not ULX3S-relevant since ULX3S has SDR SDRAM).

## How to build

Not run (per task constraints: no make/build/simulate). As found in
`boards/ULX3S/diamond/Makefile`:

```
cd boards/ULX3S/diamond
make graphics     # or ser_debug / scopeio
```

Each target does `echo prj_project open apps.ldf \; prj_run Export -impl $@ -task Bitgen | diamondc`,
i.e. it requires Lattice Diamond (`diamondc`) on PATH; `apps.ldf` targets
`LFE5U-12F-8BG381C` with Synplify synthesis. Whether this currently builds
clean was not verified (no Diamond available here).

## Reuse notes

### Reusable blocks

| Block | Path | Top module | Language | Vendor primitives | License |
|---|---|---|---|---|---|
| ScopeIO oscilloscope UI/storage | `library/scope/` | `scopeio` (`library/scope/scopeio.vhd`) | VHDL | None directly; depends on the SDRAM PHY and video PLL below, which do | MIT |
| Ethernet/IP stack (ARP/IP/UDP/DHCP/ICMP) | `library/mii/` | `mii_ipoe` (`library/mii/mii_ipoe.vhd`), built from `eth_rx/eth_tx`, `arpd`, `ipv4`, `udp`, `icmpd`, `dhcpcd` | VHDL | None found (portable MII-level logic; RMII pad wiring is board-side) | MIT |
| SDRAM/DDR controller (generation-generic) | `library/sdram/` | `sdram_ctlr` (`library/sdram/sdram_ctlr.vhd`) | VHDL | None in the controller itself | MIT |
| ECP5 SDRAM PHY (gearbox/serdes) | `library/latticesemi/ecp5/` | `ecp5_sdrphy` → `ecp5_sdrbaphy` + `ecp5_sdrdqphy` → `ecp5_ogbx`/`ecp5_igbx` | VHDL | `oddrx1f`, `fd1s3ax` (ECP5 primitives, via `ecp5u.components`) | MIT |
| ECP5 PLL/clock gen (video, SDRAM) | `library/apps/` | `ecp5_videodcm`, `ecp5_sdramdcm` | VHDL | `EHXPLLL` | MIT |
| USB 1.1 device + host | `library/usb/` | `usbdev` (device), `usbhost`/`usbhostdvr` (host), `usbphy` (PHY-level) | VHDL | None found | MIT |
| DVI/TMDS encoder | `library/video/` | `dvi` (`library/video/dvi.vhd`), uses `tmds_encoder.vhd` | VHDL | None in `dvi.vhd`/`tmds_encoder.vhd` itself; final GPDI serialization goes through `ecp5_ogbx` (see above) | MIT |

### Per-block detail

- **ScopeIO** (`library/scope/scopeio.vhd`): generics `profile`, `settings`
  (a compact JSON-like config string parsed via `hdl4fpga.hdo`), `sdram_freq`,
  `fifo_size` (default 8*8192), `video_gear`, `red/green/blue_length` (default
  8/8/8). Ports split into an `si_*/so_*` serial I/O link (USB or Ethernet),
  `input_clk`/`input_data` (ADC sample stream), and a full `ctlr_*`/`ctlrphy_*`
  SDRAM controller/PHY interface it drives directly — i.e. ScopeIO expects to
  own the SDRAM controller, not share it. On ULX3S the ADC SPI bit-banging
  (MAX1112x, `adc_sclk/adc_csn/adc_mosi/adc_miso`) lives in the app file
  `boards/ULX3S/apps/scopeio.vhd`, not in `library/scope/`, so reusing ScopeIO
  elsewhere means writing your own ADC driver to feed `input_data`.
- **mii/ethernet stack** (`library/mii/mii_ipoe.vhd`): generics `half_duplex`,
  `default_ipv4a` (32-bit), `my_mac` (48-bit). Ports: `mii_clk` plus a
  `plrx_*`/`pltx_*` payload link (to the app) and `miirx_*`/`miitx_*` (to the
  RMII/MII PHY pins). Confirms the catalogue's "full ARP/IP/UDP/DHCP stack"
  claim: `arpd.vhd`/`arp_rx.vhd`/`arp_tx.vhd` (ARP), `ipv4.vhd`/`ipv4_rx.vhd`/`ipv4_tx.vhd`
  (IP), `udp.vhd`/`udp_rx.vhd`/`udp_tx.vhd` (UDP), `icmpd.vhd`/`icmprply_tx.vhd`/`icmprqst_rx.vhd`
  (ICMP ping), `dhcpcd.vhd`/`dhcp_dscb.vhd`/`dhcp_offer.vhd` (DHCP client). No
  RMII pad-level PHY driver is in this directory — that's board-side (e.g.
  ulx3s-misc's `examples/eth/rmii` per `reusable-cores.md`).
  This is exactly the stack used by the `eth/` prebuilt bitstream in
  `emard__ulx3s-bin.md` (DHCP + ping responder on LAN8720 RMII, GP/GN 9-13).
- **SDRAM controller** (`library/sdram/sdram_ctlr.vhd`): generics `debug`,
  `ctlr_tcp` (clock period, real), `chip_data`/`phy_data` (strings naming
  entries in `sdrampkg.vhd`'s `sdram_db`/`phy_db` tables). It is
  **generation-generic**: `sdrampkg.vhd` lists chip timing for `sdr` (e.g.
  `MT48LC16M16MA2-7E` — the chip ULX3S actually has), `ddr`, `ddr2` and `ddr3`
  parts (e.g. Micron `MT41K128M16-125`). ULX3S's two ULX3S apps
  (`graphics`, `scopeio`) both instantiate it with `chip_data =>
  "MT48LC16M16MA2-7E"` (SDR, 2 banks/13 row/9 col/16-bit), i.e. **only the
  SDR path is exercised on ULX3S** — the DDR2/DDR3 entries in the same table
  are for other boards/chips and do not apply here (ULX3S has SDR SDRAM only,
  per CLAUDE.md). The vendor-specific part is the PHY layer
  (`library/latticesemi/ecp5/ecp5_sdrphy.vhd` and friends), which uses ECP5
  `oddrx1f`/`fd1s3ax` I/O primitives through small `ecp5_igbx`/`ecp5_ogbx`
  gearbox wrappers — this PHY is required to actually connect `sdram_ctlr` to
  ECP5 pins and is not portable to other vendors as-is.
- **USB device/host** (`library/usb/usbdev.vhd`, `usbhost.vhd`): used on
  ULX3S by `ser_debug.vhd` on US2 (`usb_fpga_{dp,dn,bd_dp,bd_dn}`), switchable
  device/host via the `usb_device` constant. `library/usb/README.rst` notes
  36 MHz oversampling clock (tested 35.9-36.36 MHz). No ECP5-specific
  primitives found in `usbdev.vhd`/`usbhost.vhd`/`usbphy*.vhd` — this core
  looks portable.
- **DVI/TMDS** (`library/video/dvi.vhd`): generic `gear` (default 10, ULX3S
  apps use 2), ports `clk`, `rgb` (3×8), `hsync`/`vsync`/`blank`, `cclk`, and
  four serialized `gear`-wide output channels `chn0/chn1/chn2/chnc`. Portable
  by itself; on ULX3S the final serialization to `gpdi_d[0..3]` again goes
  through the ECP5 `ecp5_ogbx` gearbox (`oddrx1f`), so dropping `dvi.vhd` into
  a non-ECP5 board needs a different output stage.

### Clock/reset assumptions and drop-in notes

- All three ULX3S apps assume a single 25 MHz input (`clk_25mhz`, `apps.lpf`
  site `G2`) and derive everything else (40/64 MHz pixel clocks, 133 MHz
  SDRAM clock, 36 MHz USB oversampling) via `EHXPLLL`-based `ecp5_videodcm`/
  `ecp5_sdramdcm` — this matches the ULX3S board's actual 25 MHz oscillator
  (CLAUDE.md). Reset is informal: `ser_debug.vhd` uses the `right` joystick
  button (`alias sys_rst is right`) as reset; `graphics.vhd`/`scopeio.vhd`
  were not checked for an explicit reset alias (grep found none) and appear
  to rely on PLL lock signals instead.
- Dependencies: every block above pulls in `library/basic/hdo.vhd` and
  `library/basic/base.vhd` (the `hdo` "hierarchical data object" string-based
  config-parsing package used pervasively for generics like `settings` and
  `chip_data` — this is unusual and adds real complexity to reusing any
  single block standalone; expect to need `hdo.vhd`/`base.vhd` plus whichever
  `*pkg.vhd` package (`sdrampkg`, `videopkg`, `scopeiopkg`, `ecp5_profiles`)
  the block references).
- To drop a block into a new ULX3S design targeting `ulx3s_v20.lpf`
  conventions: pin names in `boards/ULX3S/diamond/apps.lpf` already use the
  standard ULX3S names (`clk_25mhz`, `gpdi_d[]`, `sdram_*`, `gp[]/gn[]`,
  `adc_*`), so the LPF constraints themselves are directly reusable; the main
  porting cost is pulling in the `hdo`/package dependency chain and (for
  SDRAM/DVI) the ECP5-specific PHY/gearbox files.

## Open questions

- Programmer for ULX3S bitstreams from this repo is unstated (unverified:
  presumably standard `openFPGALoader -b ulx3s` per CLAUDE.md, not confirmed
  in-repo).
- ScopeIO's `"inputs:" & "8"` setting in `boards/ULX3S/apps/scopeio.vhd`
  (8 analog inputs configured) vs. the "4-channel storage oscilloscope"
  description in `docs/projects/emard__ulx3s-bin.md` (from the `scope/`
  prebuilt bitstream) is not reconciled — could be a different commit/config,
  or the 4 channels described there could be a UI/display subset of the 8
  wired. Needs the `ulx3s-bin` `scope/` build's actual source commit to compare.
- Whether `boards/ULX3S/diamond/apps.ldf` currently builds clean under a
  present-day Diamond install was not tested (no build performed, per task
  constraints).
- `library/apps/ecp3_sdramdcm.vhd`, `xc3s_sdramdcm.vhd`, `xc5v_sdramdcm.vhd`,
  `xc7a_sdramdcm.vhd` show the same SDRAM-DCM pattern exists for other vendors
  (Xilinx Spartan3/Virtex5/Artix7, Lattice ECP3) — not reviewed, out of scope
  for ULX3S but useful to know when porting.
- Catalogue `reusable_blocks` cell says `library/sdram, ecp5 phys, video/tmds,
  usb/ dev+host, mii/ full eth stack, scope/` — all verified present and
  correctly named; catalogue `license` cell ("mixed: MIT (LICENSE) vs
  GPL-3.0-or-later headers") should be corrected per the License field above:
  the mix is MIT-source vs. GPL-headed **Makefiles**, not mixed HDL.
{% endraw %}
