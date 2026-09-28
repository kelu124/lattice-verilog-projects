---
name: reusable-cores
description: Cross-project map of the reusable ULX3S building blocks (PLL, DVI/HDMI, ESP32 OSD, USB host, SDRAM, displays, CPUs) and which repo has the best copy — first stop when helping someone build a new design.
metadata:
  type: reference
---

From the 2026-09-27/28 survey of 376 repos (292 ULX3S/ULX4M + 26 on other ECP5 boards + 58 non-ECP5, iCE40 UP5K and HX8K/HX4K); iCE40 cores use SB_* primitives and need porting (details in `docs/catalogue.md`, source `data/catalogue.json`).
Paths are relative to `original_sources/<slug>/`. Licenses matter; see [[catalogue-fields]].

| Need | Best source (language, license) | Also |
|---|---|---|
| Parametric ECP5 PLL | emard__ulx3s-misc `examples/ecp5pll/hdl/{sv,vhd}/ecp5pll` (SV/VHDL, BSD header) | copied into many lawrie/splinedrive repos |
| DVI/HDMI out (TMDS) | emard__ulx3s-misc `examples/dvi/hdl/{vga2dvid,tmds_encoder}.vhd` (MIT, Mike Field) + `fake_differential.v` (BSD); page `docs/projects/emard__ulx3s-misc.md` | Verilog: lawrie__apple-one `rtl/boards/ulx3s/` (Apache-2.0), splinedrive__my_hdmi_device (ISC), doctorwkt tic-tac-toe `HDMI/` (GPL-3.0), Silice `projects/common/hdmi.si` (MIT) |
| HDMI with audio | emard__papilio-arcade `scramble_rel001_papilio/source/vga/` av_hdmi (VHDL) | — |
| ESP32 SPI OSD + ROM/disk loading | lawrie__ulx3s_sms `src/osd/` (osd.v, spi_osd.v, spirw_slave_v.v) + `esp32/osd` MicroPython; same stack in nes_ecp5, trs_80, apple2fpga. No vendor primitives; osd.v/spi_osd.v have no license header (spirw_slave_v.v BSD); page `docs/projects/lawrie__ulx3s_sms.md` | the de-facto way to load games/disks from SD via the ESP32 |
| ESP32 ↔ FPGA SPI RAM | emard__uk101onfpga `rtl_emard/spi_ram/spi_ram_slave.vhd`; ulx3s-misc `examples/spi_ram` | — |
| USB 1.1 HID host (US2: keyboard/gamepad) | emard__ulx3s-misc `examples/usb/usbhost` (usbh_sie.v, usbh_host_hid) (mixed, GPL/MIT parts) | Verilog + gamepad decoders: emard__nes_ecp5 `usb/`; VHDL: hdl4fpga `library/usb` |
| USB device (CDC serial) | ulx3s-misc `examples/usb/usbcdc` (VHDL); osresearch__spispy `verilog/usb/` (TinyFPGA stack, Verilog) | f32c `rtl/soc/usb_serial` |
| SDRAM controller | ulx3s-misc `examples/sdram/` (pnru public domain, mistery GPL-3.0, 16bit LGPL-2.1, memtest_mister); lawrie__ulx3s_examples `sdram16/sdram.v` (GPL-3.0-or-later, MiST) | Linux-grade: splinedrive__kianriscv `engineering/sdram/` (ISC/Apache); cache: emard__oberon `hdl/cache_controller.v`; VHDL: f32c `rtl/soc/sdram*.vhd` (MIT); multi-generation SDR/DDR/DDR2/DDR3: hdl4fpga `library/sdram/sdram_ctlr.vhd` (MIT) |
| ST7789 / SSD1331 / SSD1351 displays | ulx3s-misc `examples/spi_display/hdl` (Verilog+VHDL) | lawrie__ulx3s_examples `st7789/`; Silice `oled_*.si`; SpinalHDL: lawrie__slabboy `ST7789.scala` |
| PS/2 keyboard/mouse | lawrie__ulx3s_examples `ps2/`, `ps2port/` | ulx3s-misc `examples/ps2` |
| Audio | SPDIF: f32c `rtl/soc/spdif_tx.vhd` (BSD-2); I2S: ulx3s-misc `examples/audio`; PSG: lawrie__ulx3s_sms `src/sn76489.v` | synth: emard__synthowheel (BSD) |
| FM / RDS transmitter | ulx3s-misc `examples/fm/hdl`; f32c `rtl/soc/fm/` | emard__rdsfpga is ULX2S-only |
| Ethernet (LAN8720 RMII on GP/GN 9–13) | ulx3s-misc `examples/eth/rmii`; hdl4fpga `library/mii` (full ARP/IP/UDP/DHCP stack, VHDL, Diamond) | — |
| Onboard ADC MAX11125 | ulx3s-misc `examples/adc` | hdl4fpga ScopeIO oscilloscope |
| CPUs | Z80 tv80 (many); 6502: chrismoos__m6502 (SV, MIT, verified by tests); RISC-V: picorv32 (fpga-odysseus), kianV (Linux), Silice fire-v/ice-v, NEORV32 (VHDL, BSD-3, no ULX3S target in repo), VexRiscv via LiteX; RISC-V/MIPS: f32c (BSD-2); 68000 fx68k (lawrie examples); TMS99000 (pnru__ti99, public domain); CDP1802 SpinalHDL | — |
| DDR3 on ECP5 (not ULX3S: it has SDR SDRAM) | ultraembedded__orangecrab `ddr_test/src_v/ddr3_*.v` (Verilog, Apache-2.0) | — |
| QSPI/QPI PSRAM | spritetm__hadbadge2019_fpgasoc `soc/qpi_cache/` (ECP5 primitives; per-file licenses) | — |
| HDMI with audio | danodus__ecp5_hdmi_audio_video `rtl/` (Verilog, MIT, ULX3S top in `boards/ulx3s/`) | tallenintegsys__hdmi-orangecrab (SV, synlig, no license) |
| USB CDC-ACM device (soft PHY, US2) | fdarling__orangecrab-usb-cdc-demo / orangecrab-examples `usb_acm_device` (wrap tinyfpga_bx_usbserial, submodule not in shallow clone) | gregdavill__luna-usb-serial-acm (Amaranth-generated Verilog, needs ULPI PHY) |
| ECP5 JTAGG user-JTAG | tomverbeure__ecp5_jtag (write-up + demo, no license) | — |
| SGMII/RGMII gigabit Ethernet | sefbkn__versa-ecp5-demo (Verilog, CERN-OHL-S-2.0, Versa ECP5-5G DCU) | — |
| HyperRAM (ULX3S has none: add-on board) | smunaut__ice40-playground `cores/no2hyperbus` (Verilog, iCE40 IO primitives to port); asinghani__pifive-cpu `soc/third_party/hyperram/hyper_xface.v` (Black Mesa Labs, Verilog, fabric clk/4, CERN-OHL claimed in-file only, instance commented out in pifive) | joshajohnson__ecp5-mini-projects `litex/soc-hr` (LiteX litehyperbus, 8 MB); not cloned: markus-zzz/hyperram-test (ULX3S add-on board test, same hyper_xface.v) |
| USB device cores (Verilog) | tinyfpga_bx_usbserial (fdarling__orangecrab-usb-cdc-demo submodule, Apache-2.0; copy in joshajohnson__ecp5-mini-projects `verilog/common/usb`); no2usb (icebreaker-fpga__icetwang submodule, LGPL-3.0+, iCE40 SB_* IO); FPGA-USB-Device (mangelajo__orangecrab-usb submodule, GPL-3.0 at pinned commit) | valentyusb (Migen, BSD-3, orangecrab-examples submodule) |
| DVI/TMDS in nMigen, DVI input | kbeckmann__pergola_projects `pergola/gateware/{tmds,vga2dvid,dvid2vga}.py` (BSD-2) | — |
| USB CDC-ACM, portable (no vendor primitives) | ulixxe__usb_cdc (Verilog, MIT; pin files for 21 boards) | — |
| DVI, small and portable | wren6991__smoldvi `hdl/smoldvi/` (Verilog, CC0; only ddr_out is platform-specific) | — |
| SID (C64 sound), SystemVerilog | daglem__redip-sid (CERN-OHL-S-2.0, primitive-free DSP) | bit-hack__icesid |
| E1 telecom line interface | osmocom__osmo-e1-hardware `gateware/cores/no2e1` (Verilog, iCE40 SB_IO, author says easy to adapt) | — |
| iCE40 cores library (no2fpga: USB, HyperRAM, QPI PSRAM, cache, HUB75) | smunaut__ice40-playground `cores/no2*` (Verilog; iCE40 SB_* IO in no2ice40, logic mostly portable; check each core's license) | — |
| SID (C64 sound) | bit-hack__icesid `icesid/*.v` (Verilog, CERN-OHL-S-2.0, no SB_* primitives: portable) | — |
| SD card controller (SPI + SDIO/eMMC, Wishbone) | zipcpu__sdspi `rtl/{spi,sdio}/` (Verilog, GPL-3.0, vendor-neutral, ~60 SymbiYosys proofs) | — |
| RISC-V reference core + SoC | yosyshq__picorv32 `picorv32.v`, `picosoc/` (Verilog, ISC, no vendor primitives; self-checking `make test`) | Hazard5 in wren6991__riscboy `hdl/hazard5` (RISCBoy also has a ULX3S 85F target, `synth/ULX3S.mk`) |
| 6845 CRTC / MDA-CGA video | schlae__graphics-gremlin `verilog/crtc6845.v` (Verilog, CC-BY-SA-4.0, primitive-free) | MC6845 + SAA5050 teletext in hoglet67__ice40beeb |
| Scandoubler (15 kHz RGB → VGA) | hoglet67__ice40beeb `src/mist_scandoubler.v` (from MiST, GPL-3.0-or-later, portable) | — |
| Game Boy (SM83 CPU + PPU), formally verified | msinger__iceboy (SystemVerilog, CERN-OHL-W-2.0, SymbiYosys per-instruction proofs) | — |
| USB DFU bootloader (US2) | emard__had2019-playground `projects/bootloader/` (PicoRV32 + ECP5 USB core, BSD-3/LGPL-3.0+; `1d50:614b`, user image at 0x200000) | see `docs/DFUs.md` |
| ECP5 PLL parameter solver (Python/Amaranth) | glasgowembedded__glasgow `software/glasgow/gateware/pll/ecp5.py` (0BSD OR Apache-2.0; Glasgow revD is ECP5 25F) | emard ecp5pll (HDL, see above) |
| USB 2.0 / 3.0 device stack (Amaranth) | greatscottgadgets__luna `luna/gateware/usb/` (BSD-3; ULPI/UTMI, USB3 PIPE, ECP5 SERDES PHY) | — |
| FFT + I2S/PDM mic + HDMI, cocotb-tested | mebner86__icesugar-pro_sound2fft `rtl/` (fft256.v, fft_real512.v, pdm_cic, i2s_rx/tx, tmds; MIT, bit-exact numpy tests) | — |
| IEEE 1588 PTP + AES67 audio over Ethernet | datanoisetv__colorlight-i9-aes67 (ptp_top/ptp_clock/ptp_servo, RGMII MAC/RTP; MIT) | — |
| SHA-256 (pipelined, double hash) | xtrinch__fpga-bitcoin-miner `src/sha256_transform.v` (MIT, self-checking `make test-*`) | — |
| HUB75(e) LED panel driver | lucysrausch__colorlight-led-cube `ledpanel.v` (GPL-3.0) | no2hub75 (smunaut__ice40-playground, CERN-OHL-W) |
| SDR receive chain (DDC, CIC, FIR, AM demod, PDM DAC) | emeb__orangecrab_adc (Verilog, no license found) | — |
| Wishbone interconnect + arbiter | rschlaikjer__fpga-3-softcores `vendor/wb_intercon`, `vendor/verilog-arbiter` (portable) | — |
| Bit-serial RISC-V (RV32E), cocotb-tested | michaelbell__nanov (Apache-2.0) | — |
| Linux on ULX3S | linux-on-litex-vexriscv (`./make.py --board=ulx3s`); kianV (85F); SaxonSoc (docker recipes stale since 2020) | — |

Cross-project facts:
- **The emard "universal make" build system** (`scripts/trellis_main.mk` + `diamond_main.mk`, `FPGA_SIZE=12|25|45|85`)
  appears in ulx3s-misc, galaksija, oberon, apple2fpga, papilio-arcade, etc. It often hard-codes tool paths
  (`/mt/scratch/tmp/openfpga`), so override `TRELLIS`/path variables when building.
- **Diamond-only historical ports**: f32c, minimig, papilio-arcade, vhdl_phoenix, next186, uk101, hdl4fpga, bonfire, synthowheel.
  Porting them to the open flow usually means ghdl-yosys-plugin (VHDL). f32c's own trellis attempts are marked not working.
- **`--25k` + `--idcode 0x21111043`** is a common trick: build for 25k and load it on a 12F (same die).
- Many ulx3s.github.io entries have two copies; the preferred ones are recorded in `data/catalogue.json` `fork_of`.

Full review pages with per-block reuse notes (module, ports, primitives, license, ULX3S changes) exist for 15 of these repos
in `docs/projects/`; pin maps of every LPF in the collection are in `data/lpfs.json` (rendered `docs/lpf-catalogue.md`).

**How to apply:** when a user wants to build X, look up X here first, check its license, then open the repo's
row in `docs/catalogue.md`. Add rows here whenever a review finds a better or new reusable block.
