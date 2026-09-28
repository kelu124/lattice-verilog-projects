<!-- Generated from data/projects/emard__ulx3s.json by .claude/skills/documentation/gen_pages.py; do not edit. -->

# ULX3S board hardware (`emard__ulx3s`)

| Field | Value |
|---|---|
| Upstream | https://github.com/emard/ulx3s |
| Reviewed at | `6a92cec` (upstream date 2025-04-27), reviewed 2026-09-27 |
| License | Modified MIT (`LICENSE.md`): EMARD, RADIONA and FER logos must stay on the top silkscreen |
| HDL / framework | None (hardware project). KiCad 4 up to v1.8, then KiCad 5; opened/saved with KiCad 7 in 2023 |
| Toolchain | n/a for gateware; the manual documents the open ECP5 flow (see below) |
| Programmer | Documented: openFPGALoader, fujprog/ujprog, OpenOCD, FleaFPGA-JTAG, ESP32, DFU |
| Target FPGA(s) | LFE5U-12F / 25F / 45F / 85F, CABGA381 |
| Board revision(s) | v1.7 → v3.1.7 (tags v3.0.6 … v3.1.7) |
| Activity | 2732 commits, 2016-01-28 → 2025-04-27. Hardware frozen since v3.1.7 (2021); recent commits are docs only |

## What it provides

- **PCB design**: `ulx3s.pro`, `ulx3s.sch` + sub-sheets (`analog`, `blinkey`, `flash`, `gpdi`,
  `gpio`, `power`, `ram`, `serdes`, `usb`, `wifi`), `ulx3s.kicad_pcb`, gerbers in `plot/`.
- **BOM**: `doc/ulx3s_bom.csv`, `1-click-bom.tsv` (Kitspace), `doc/MINIMAL.md` for hand assembly.
- **Schematics PDF**: `doc/schematics.pdf` → `schematics_v316.pdf` (v308…v317 also present).
- **Constraint files** (the part that matters for gateware):
  - `doc/constraints/ulx3s_v20.lpf`: PCB v2.x.x and v3.0.x
  - `doc/constraints/prototype/ulx3s_v17patch.lpf`, `ulx3s_v314.lpf`, `ulx3s_v316.lpf`
- **ECP5 pinout CSVs** for all densities (`doc/ECP5U*Pinout.csv`), BGA381 package doc.
- **User manual**: `doc/MANUAL.md` (connectors, power/sleep, every programming method,
  ESP32 setup, displays, add-on modules, board revision history and production table).
- **Enclosure**: parametric OpenSCAD box in `box/` (snapbox recommended).
- `doc/TODO.txt`: upstream hardware TODO list (not yet reviewed here).

## Structure

Top-level KiCad project, `doc/` for documentation/constraints/datasheets, `plot/` for gerbers,
`footprints/`, `spice/`, `tools/`, `pic/` for photos, `old/` for earlier versions.

## How to build

Not a gateware project. PCB: `kicad ulx3s.pro`; gerbers: `gerbv -p plot/ulx3s.gvp`,
`zip -r /tmp/ulx3s.zip plot/ulx3s` for fabs (IPC class 3, 5/5 mil, 0.2 mm holes).

## Reuse notes

- Start any new design from the LPF matching the board revision; see
  [`docs/board-reference.md`](../board-reference.md) for the condensed pin/peripheral reference.
- The signal names in `ulx3s_v20.lpf` (`clk_25mhz`, `led`, `btn`, `gp/gn`, `gpdi_dp/dn`,
  `sdram_*`, `usb_fpga_*`, `wifi_*`, `audio_*`, `oled_*`, `sd_*`, `adc_*`, `shutdown`, …)
  are the de-facto top-level port names across the community.
- The manual lists external modules known to work: LAN8720 RMII Ethernet, PCM5102 I2S DAC,
  AN108/AN926 fast ADC/DAC (via gojimmypi adapter), e-ink 1.54" IL3829, ST7789 LCDs.

## Open questions

- The manual's "Board differences" section still calls v3.1.4/v3.1.6 "currently tested".
  Check whether v3.1.7 is now the mainstream shipping revision (Mouser listing).
- The manual mentions a `v18` LPF compatibility class, but no v1.8 LPF exists in the repo.
- `doc/TODO.txt` not yet read.
