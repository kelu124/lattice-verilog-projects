<!-- Generated from data/projects/emard__ulx3s-misc.json by .claude/skills/documentation/gen_pages.py; do not edit. -->

# ULX3S miscellaneous/advanced examples (`emard__ulx3s-misc`)

| Field | Value |
|---|---|
| Upstream | https://github.com/emard/ulx3s-misc |
| Reviewed at | `d0c6f15dd2` (upstream date 2026-02-07), reviewed 2026-09-28 |
| License | No repo-level `LICENSE` file. Per-file headers are mostly `LICENSE=BSD` (EMARD/Marko Zec/MMICKO), but several imported third-party cores are GPL-2/3 or LGPL-2.1 — see the peripheral-by-peripheral table below. Treat each file's own header as authoritative |
| HDL / framework | Verilog and VHDL roughly 60/40 (`.claude/memory/catalogue.tsv`: 156 `.v` / 102 `.vhd`), one nMigen (Python) DVI port (`examples/nmigen/dvi/`), MicroPython for ESP32-side companions |
| Toolchain | `both`: open flow (yosys/nextpnr-ecp5/ecppack, VHDL converted with `vhd2vl` or synthesized via `yosys -m ghdl`) and Lattice Diamond, driven by a shared "universal make" system (`scripts/trellis_main.mk`, `scripts/diamond_main.mk`, `scripts/trellis_main_ghdl.mk`/`_sv.mk`); catalogue.tsv counts 63 trellis vs 60 diamond makefiles (42 default to trellis, 5 default to diamond) |
| Programmer | `ujprog`/`fujprog`/`openFPGALoader` (JTAG or SRAM/flash), plus OpenOCD scripts in `scripts/*.ocd` for the FT231X/FT2232/FT232R JTAG adapters |
| Target FPGA(s) | 12F mostly, also 25F/85F, plus `um-85k` (ULX4M) — `FPGA_SIZE` variable in each example's `Makefile` |
| Board revision(s) | `ulx3s_v20` and variants (`_extgpdi`, `_sd4bit`, `_segpdi`), `ulx3s_v314`, `ulx3s_v316`, `ulx3s_v17patch` (referenced from other examples), `ulx4m_v002`, plus one `FFM-LFE5U` module LPF (`constraints/FFM-LFE5U-V0r0_mit_FFC-CA7-V2r0.lpf`) |
| Activity | Single commit reviewed: `d0c6f15dd2` dated 2026-02-07 (`git -C original_sources/emard__ulx3s-misc log -1 --format=%cs`). `.claude/memory/history.tsv`: first commit 2019-03-14, **1284 commits** total (clone is shallow, no further history available) |

## What the gateware does

The **reference building-block library** for ULX3S: EMARD's own advanced examples, organised as one
self-contained `examples/<name>/` per peripheral, each with its own `Makefile`/`makefile.trellis`/
`makefile.diamond` and (usually) its own `proj/constraints/*.lpf`. Grouped by peripheral:

- **Clock generation**: `ecp5pll/` — parametric ECP5 PLL wrapper, SV and VHDL editions.
- **Video out, DVI/HDMI (GPDI)**: `dvi/` (fpga4fun-style color-bar test pattern, VHDL, flexible
  resolution/refresh via compile-time PLL math), `dvi_osd/` (DVI + on-screen character display driven
  from ESP32 over SPI — the same OSD stack reused in `lawrie__ulx3s_sms`), `dvi_in/` (DVI/HDMI **input**
  deserializer + EDID ROM), `serdes_dvi/` (raw SERDES-based DVI), `ov7670_dvi/` (OV7670 camera → DVI).
- **Video out, other**: `lvds/`, `lvds_passthru/` (VGA↔LVDS for the optional LVDS display connector),
  `lcd35/` (3.5" LCD RTL + enclosure STL), `serdes/` (raw SERDES demo).
- **Displays (SPI TFT/OLED)**: `spi_display/` — ST7789, SSD1306, SSD1331, SSD1351 XY-scan display cores
  in both Verilog and VHDL, feeding VGA-style or OSD content; `oled/`, `hex/` (hex-digit decoders over
  the same display cores), `lcd_st7789/` (MicroPython-side 240×240 init), `eink/` (e-paper 1.54"/2.9"
  drivers, ESP32 MicroPython side only).
- **SDRAM**: `sdram/` — seven independent controller ports (`sdram_mistery`=MiST board GPL-3.0,
  `sdram_pnru`/`sdram_pnru2`=public domain, `sdram_16bit`=Next186/opencores LGPL-2.1, `sdram_ctrl`,
  `sdram_mist`, `sdram_pnru_68k` [+ 180° phase variant], `sdram_pnru_99k`, `sdram_fpga`), plus
  `memtest_mister/` (a full memory-test/scope harness with its own `sdram_control.v`).
- **USB host**: `usb/usbhost/` — Ultra-Embedded USB1.1 full-speed host SIE (`usbh_sie.v`, GPL) plus a
  vhd2vl-translated convertible HID decoder (`usbh_host_hid.v`, also GPL per its own header); VHDL
  originals (`usbh_sie_vhdl.vhd`, `usbh_host_hid_convertible.vhd`) and HID report decoders for
  mouse/joystick/Xbox360 pads (`usb/usbhid/`).
- **USB device**: `usb/usbcdc/` — Joris van Rantwijk's USB1.1/2.0 CDC-ACM serial core (VHDL, **GPL-2+**,
  confirmed via `README.txt` and per-file `-- License=GPL` headers), plus a USB-CDC-to-ICMP-echo demo
  (`usbcdc/eth/usbeth_icmp_echo.vhd`); `usb/ulpi_wrapper.v`, `usb/usb11_phy_vhdl/` (raw PHY layer);
  `usb/ch376/` (CH376 USB-to-SD/file-system chip driver, ESP32 + HDL sides).
  and `db9joy/` (DB9 Atari-style joystick reader, not USB but grouped with input peripherals).
- **PS/2**: `ps2/kbd/` (keyboard decoder), `ps2/mouse/` (mouse decoder, VHDL + Verilog editions).
- **ESP32 companion interfaces**: `spi_ram/` — ESP32↔FPGA SPI-RAM-emulation slave, `esp32_passthru/`
  (JTAG passthrough so the ESP32 can flash the FPGA), `esp32_rmii/` (ESP32 drives an LAN8720 RMII PHY
  through the FPGA), `dvi_osd/esp32/` and `oled/micropython/` (MicroPython OSD/display clients).
- **ADC**: `adc/max1112x/` — MAX1112x 8/12-channel ADC init+read cores (shift and array variants, VHDL).
- **RF**: `fm/` — stereo FM transmitter with RDS (`fm.vhd`, `rds.vhd`, `fir.vhd`/`lowpass.vhd` filters,
  Marko Zec, BSD).
- **Ethernet**: `eth/rmii/` — LAN8720 RMII packet sniffer/sender: hex-dumps received frames to DVI/LCD,
  sends a canned ARP reply on button press (`top_eth_hex_demo.v`).
- **RTC/power**: `rtc/i2c_master/` (I2C RTC reader), `rtc/micropython-mcp7940n/` (MCP7940N over
  MicroPython/ESP32).
- **Flash/bitstream management**: `flash_passthru/` (JTAG-to-flash passthrough), `multiboot/` (3-slot
  flash multiboot image via `ecpmulti`, BTN0-triggered bitstream-jump using `USER_PROGRAMN`), `qspi/`
  (QSPI flash controller cores: `eqspiflash.v`, `wbspiflash.v` Wishbone wrapper).
- **JTAG**: `jtag_slave/` (user-JTAG TAP + JTAGG slave with hex/OLED readout), `jtagthru/` (JTAG
  passthrough demo).
- **Sensors**: `adxl355/` (SPI accelerometer + GPS-sync logging, ESP32 + PC-side Python tools).
- **Misc/education**: `bram/`, `btn_debounce/`, `collatz/` (Collatz-conjecture demo with SPI display
  output), `gray_counter/`, `onchip_osc_blink[_ffm]/` (internal oscillator `OSCG` primitive demo),
  `jtag_slave` already listed above.
- **nMigen**: `nmigen/dvi/` — the only non-Verilog/VHDL example, a Python (Amaranth-predecessor) port of
  the DVI test pattern.

## Structure

`examples/<peripheral>/` — each is independent, usually split into `hdl/` (reusable core, often shared by
several `proj/` variants) and `proj/<variant>/` or `top/` (board-specific top level + own `constraints/`).
Some examples (`dvi/`, `ecp5pll/`, `fm/`, `onchip_osc_blink*/`) keep their Makefile at the example root
instead of under `proj/`. `scripts/` holds the shared build system: `trellis_main.mk` (open flow),
`trellis_main_ghdl.mk` (adds `yosys -m ghdl` synthesis for VHDL-only examples), `trellis_main_sv.mk`
(SystemVerilog), `diamond_main.mk` (Lattice Diamond), plus OpenOCD interface configs (`ft231x.ocd`,
`ft2232.ocd`, …) and Diamond XCF flash-programming scripts. `clocks/` and `multiplatform/` exist at repo
root (not inspected in depth for this pass). `constraints/` holds the shared board LPFs referenced by
`../../constraints/<file>.lpf` from most examples.

## How to build

Not run (read-only review). Generic trellis path, e.g. `examples/ecp5pll/`:

```
cd examples/ecp5pll
make            # or: make -f makefile.trellis
```

`Makefile`/`makefile.trellis` set `PROJECT`, `BOARD = ulx3s`, `FPGA_SIZE` (12/25/45/85), `CONSTRAINTS`,
`TOP_MODULE(_FILE)`, `VHDL_FILES`/`VERILOG_FILES`, then `include $(SCRIPTS)/trellis_path.mk` and one of
`trellis_main.mk` / `trellis_main_ghdl.mk` / `trellis_main_sv.mk`. VHDL-only examples list their sources
in `VHDL_FILES`; the build converts them with `vhd2vl` (or synthesizes directly through
`yosys -m ghdl -p "ghdl --ieee=synopsys --std=08 -fexplicit -frelaxed-rules ... -e <top>"` for the ghdl
variant) before `synth_ecp5` → `nextpnr-ecp5 --<size>f --package CABGA381` → `ecppack`. Diamond path:
`make -f makefile.diamond`. Default tool paths assume `/mt/scratch/tmp/openfpga/` (per `README.md`);
override via `scripts/trellis_path.mk`/`diamond_path.mk`. `multiboot/`: builds 3 sub-bitstreams then
`ecpmulti --input ... --flashsize 128 --output multiboot.img`, flashed with `fujprog -j flash` or
`openFPGALoader -b ulx3s --file-type bin -f`.

**Testbenches**: essentially none. `.claude/memory/catalogue.tsv` records exactly one non-synthesis test
artifact in the whole repo — `examples/audio/testbench/sinewave.c` — and it is a **standalone C
reference model** for the sine-wave generator (computes min/max envelope values), not a Verilog
testbench; confirmed by reading the file (plain `#include <stdio.h>` C program, no HDL). `ghdl` appears
only inside `trellis_main_ghdl.mk` as a synthesis front-end (`ghdl ... -e $(TOP_VHDL_MODULE)` feeding
`synth_ecp5`), never as a simulator.

## Reuse notes

| Block | Path | Top module | Language | Vendor primitives | License |
|---|---|---|---|---|---|
| Parametric ECP5 PLL | `examples/ecp5pll/hdl/sv/ecp5pll.sv` (also `hdl/vhd/ecp5pll.vhd`) | `ecp5pll` | SV/VHDL | `EHXPLLL` | BSD (`// (c)EMARD` / `// License=BSD`) |
| DVI/TMDS output (VHDL) | `examples/dvi/hdl/{vga2dvid,tmds_encoder}.vhd` + `fake_differential.v` | `vga2dvid` / `TMDS_encoder` | VHDL + 1 Verilog file | `ODDRX1F` (`fake_differential.v`) | `vga2dvid.vhd`/`tmds_encoder.vhd`: **MIT** (Mike Field, hamsterworks.co.nz, full MIT text in header); `fake_differential.v`: no explicit header found |
| SPI ST7789/SSD1306/SSD1331/SSD1351 display core | `examples/spi_display/hdl/spi_display_verilog/lcd_video.v` (+ VHDL edition `spi_display_vhdl/spi_display.vhd`) | `lcd_video` | Verilog/VHDL | none | BSD (`// AUTHORS=EMARD,MMICKO and Lawrie Griffiths` / `// LICENSE=BSD`) |
| ESP32↔FPGA SPI RAM slave | `examples/spi_ram/hdl/spi_ram_slave.vhd`, top `hdl/top/ulx3s_spi_ram_oled.vhd` | `spi_ram_slave` | VHDL | none | BSD (`-- AUTHOR=EMARD` / `-- LICENSE=BSD`) |
| MAX1112x ADC reader | `examples/adc/max1112x/hdl/max1112x_reader_{shift,array}.vhd` | `max1112x_reader_shift` / `_array` | VHDL | none | BSD (`-- AUTHOR=EMARD` / `-- LICENSE=BSD`) |
| FM transmitter + RDS | `examples/fm/hdl/{fm,fmgen,rds,fir,lowpass}.vhd` | `fm` | VHDL | none apparent | BSD (`-- (c) Marko Zec` / `-- LICENSE=BSD` on `fmgen.vhd`; other files not individually re-checked) |
| Ethernet RMII (LAN8720) hex-dump/ARP demo | `examples/eth/rmii/proj/top/top_eth_hex_demo.v` | `top_eth_hex_demo` | Verilog | none | not verified in this pass (no header text found in the excerpt read) — `unknown` |
| USB1.1 full-speed host SIE | `examples/usb/usbhost/usbh_sie.v` | (Ultra-Embedded SIE core) | Verilog | none | **GPL** (Ultra-Embedded.com, 2015-2019; header offers a paid permissive-license option) |
| USB HID host report decoder (vhd2vl-translated) | `examples/usb/usbhost/usbh_host_hid.v` | — | Verilog (from VHDL) | none | **GPL** (`// License=GPL` in the vhd2vl header, referencing a GPLv2 LICENSE file) |
| USB1.1/2.0 CDC-ACM device | `examples/usb/usbcdc/usb_serial.vhd` + subentities | `usb_serial` | VHDL | none (needs external UTMI PHY) | **GPL-2.0-or-later** (Joris van Rantwijk, confirmed in `README.txt` and per-file headers) |
| SDRAM controller (MiST-board port) | `examples/sdram/sdram_mistery/hdl/sdram.v` | `sdram` | Verilog | none | **GPL-3.0-or-later** (Till Harbaum) |
| SDRAM controller (simplistic, public domain) | `examples/sdram/sdram_pnru/sdram_pnru.v` | `sdram_pnru` | Verilog | none | **public domain** (explicit header statement) |
| SDRAM controller (Next186 SoC) | `examples/sdram/sdram_16bit/hdl/sdram_16bit.v` | (module `sdram`, file `sdram_16bit.v`) | Verilog | none | **LGPL-2.1** (Nicolae Dumitrache, opencores.org, confirmed header) |

To drop any of these into a new ULX3S design: keep `clk_25mhz` as the board input and instantiate
`ecp5pll` to derive whatever clock the block needs (all clock-domain math is compile-time constant
functions, no external IP); use the matching `proj/constraints/ulx3s_v20.lpf` (or `_v314`/`_v316` for
newer boards) for port names; the DVI/TMDS and PLL blocks are ECP5-specific (`EHXPLLL`, `ODDRX1F`) and
need re-targeting for another vendor, everything else here is vendor-neutral RTL. **License caution**:
`usbhost`, `usbcdc` and the MiST-derived `sdram_mistery`/`sdram_16bit` controllers carry GPL/LGPL terms
(copyleft) even though this repo has no top-level `LICENSE` file and `catalogue.tsv` currently records
the whole repo as "mixed... mostly BSD... plus MIT and GPL/LGPL third-party" — this page confirms which
specific files are GPL/LGPL so a reuser can avoid them in a closed design, or accept the copyleft.

## Open questions

- No repo-level `LICENSE` file exists (confirmed via `find`), so licensing is per-file only; several
  files checked here have no license header at all (`fake_differential.v`, `top_eth_hex_demo.v`) —
  treat as `unknown`/all-rights-reserved until clarified with upstream.
- `sdram/sdram_ctrl`, `sdram_mist`, `sdram_pnru_68k[_180deg]`, `sdram_pnru_99k`, `sdram_fpga` were listed
  from `catalogue.tsv`/directory structure but their individual licenses were not read in this pass —
  only `sdram_mistery`, `sdram_pnru`, and `sdram_16bit` were verified.
- `usb/usbhid/` (report decoders for Logitech mouse, Saitek/Darfon/Xbox360 joysticks), `usb/ch376/`,
  `usb/ulpi_wrapper.v`, `usb/usb11_phy_vhdl/`, `qspi/`, `jtag_slave/`, `dvi_in/`, `dvi_osd/`,
  `ov7670_dvi/`, `adxl355/` were catalogued by directory listing only, not individually read for
  license/port details — candidates for a follow-up deeper pass if reused.
- `clocks/` and `multiplatform/` top-level directories were not explored in this pass.
- `nmigen/dvi/` (Python/Amaranth-predecessor port) not evaluated for correctness or completeness.
