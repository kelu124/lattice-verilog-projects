# LPF catalogue

Generated 2026-09-28 by `.claude/skills/review-gateware-project/scan_lpfs.py` from every `*.lpf` in `original_sources/` (scan), rendered by `.claude/skills/review-gateware-project/gen_lpf_catalogue.py`; do not edit by hand. Data: [`data/lpfs.json`](https://github.com/kelu124/ulx3s-klod/blob/main/data/lpfs.json).

**916 LPF files, 479 distinct contents.** Per-file last-change dates are unknown (shallow clones): `repo_last_commit` is the repo's pinned commit date. `board`/`board_rev` come from matching (signal, site) pairs against emard/ulx3s reference LPFs when >= 90 %, else from the path or the repo's catalogue row (see `board_evidence`). per-copy `device`/`luts` come from the LPF text, a build file next to it, or the repo's catalogue row (see `device_evidence`); LUT4 counts: 12k=12000, 25k=24000, 45k=44000, 85k=84000. `chips` are inferred from active signal names (the matched names are listed); `chips_commented_only` from commented-out LOCATE lines.

| Kind | LPF files |
|---|---|
| pin-map | 836 |
| no-pins (timing/IP/tool-generated or all commented out) | 47 |
| empty | 33 |

The tables below count only `pin-map` LPFs (at least one active LOCATE line).

## Files per board (copies)

| Board | LPF files |
|---|---|
| ULX3S | 648 |
| IcePi Zero | 36 |
| Colorlight | 31 |
| iCESugar-Pro | 26 |
| ULX4M | 23 |
| FleaFPGA Ohm/Uno | 11 |
| GreyBadge 2025 | 11 |
| ULX2S | 10 |
| Hackaday 2019 badge | 10 |
| FFM-LFE5U module | 7 |
| OrangeCrab | 7 |
| ECP5 Evaluation board | 6 |
| Pergola | 5 |
| Versa ECP5 | 3 |
| ECPIX-5 | 1 |
| TrellisBoard | 1 |

## ULX3S revisions (copies, by reference match)

| Revision(s) | LPF files |
|---|---|
| v2.x/v3.0.x (ulx3s_v20) | 354 |
| unknown | 135 |
| v2.x/v3.0.x (ulx3s_v20, file name) | 64 |
| v3.1.6/v3.1.7 (ulx3s_v316) | 38 |
| v1.7 patched (ulx3s_v17patch) | 23 |
| v3.1.4 (ulx3s_v314) | 11 |
| v2.x/v3.0.x (ulx3s_v20) / v1.7 patched (ulx3s_v17patch) / v3.1.4 (ulx3s_v314) | 7 |
| v2.x/v3.0.x (ulx3s_v20) / v1.7 patched (ulx3s_v17patch) / v3.1.4 (ulx3s_v314) / v3.1.6/v3.1.7 (ulx3s_v316) | 5 |
| v2.x/v3.0.x (ulx3s_v20) / v3.1.4 (ulx3s_v314) / v3.1.6/v3.1.7 (ulx3s_v316) | 5 |
| v2.x/v3.0.x (ulx3s_v20) / v3.1.4 (ulx3s_v314) | 3 |
| v2.x/v3.0.x (ulx3s_v20) / v3.1.6/v3.1.7 (ulx3s_v316) | 1 |
| v31 (file name) | 1 |
| v318 (file name) | 1 |

## Peripherals constrained (active signals, copies)

| Chip / peripheral | LPF files |
|---|---|
| led | 740 |
| button | 633 |
| ftdi-uart | 616 |
| sdcard | 593 |
| gpio-header | 579 |
| usb | 579 |
| hdmi-dvi | 577 |
| sdram | 572 |
| spi-flash | 572 |
| esp32-wifi | 527 |
| switch | 511 |
| rtc-power | 508 |
| oled-lcd | 500 |
| audio | 498 |
| adc | 497 |
| radio-antenna | 491 |
| ps2 | 92 |
| vga | 33 |
| i2c | 31 |
| ethernet | 25 |
| camera | 22 |
| jtag | 16 |
| sram | 13 |
| psram | 11 |
| ddr3 | 8 |
| hyperram | 2 |
| serdes-pcie-sata | 2 |
| dac | 1 |

## Most-copied LPFs

| Name | Copies | Board | Rev | Device | Active signals | Chips | First copy |
|---|---|---|---|---|---|---|---|
| `ulx3s_v20.lpf` | 48 | ULX3S | v2.x/v3.0.x (ulx3s_v20) | 12k/25k/45k/85k | 184 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, ps2, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb | [lawrie__ulx3s_examples](https://github.com/lawrie/ulx3s_examples/blob/b6ff00099265401fef4843e4e89c2ac54254c95f/audio/piano/ulx3s_v20.lpf) |
| `ulx3s.lpf` | 42 | ULX3S | v2.x/v3.0.x (ulx3s_v20) | 12k/25k/85k | 184 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb | [adrmcintyre__vixen](https://github.com/adrmcintyre/vixen/blob/e2db4fda79d2e73a7a595ce1773de64203346c0b/ulx3s/ulx3s.lpf) |
| `ulx3s_v20.lpf` | 35 | ULX3S | v2.x/v3.0.x (ulx3s_v20) | 12k/45k/85k | 183 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb | [ahamidi87__simpleblinky](https://github.com/ahamidi87/simpleblinky/blob/b3d9c4bcdebf65733916ec63e47e0db2bc48fc95/ulx3s_v20.lpf) |
| `ulx3s_v20.lpf` | 18 | ULX3S | v2.x/v3.0.x (ulx3s_v20) | 12k/25k/45k/85k | 246 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb | [chiplet__ulx3s-blinky](https://github.com/chiplet/ulx3s-blinky/blob/656e60b55080998d95237ee440e5033ae32c6749/constr/ulx3s_v20.lpf) |
| `icepi-zero.lpf` | 17 | IcePi Zero | unknown | 25k | 127 | button, gpio-header, hdmi-dvi, led, sdcard, sdram, spi-flash, usb | [cheyao__icepi-zero](https://github.com/cheyao/icepi-zero/blob/e01faa2bd35dcb7269827f8420b845d46c78c869/gateware/blinky/icepi-zero.lpf) |
| `ulx3s_v20.lpf` | 13 | ULX3S | v2.x/v3.0.x (ulx3s_v20) | 12k/25k/45k/85k | 184 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb | [emard__papilio-arcade](https://github.com/emard/Papilio-Arcade/blob/4f91f938c200f1b0d80f03f835bdadcc5f21aa58/pacman_rel004_sp3e_papilio/proj/lattice/ulx3s/pacman_ulx3s_v20_12f/ulx3s_v20.lpf) |
| `ulx3s_v20.lpf` | 12 | ULX3S | v2.x/v3.0.x (ulx3s_v20) | 45k/85k | 184 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb | [diegob94__ulx3s_blink](https://github.com/diegob94/ulx3s_blink/blob/1d465a44289aac1c3a024004abae6eb9a2609e08/ulx3s_v20.lpf) |
| `ulx3s_v316.lpf` | 12 | ULX3S | v3.1.6/v3.1.7 (ulx3s_v316) | 12k/25k/45k/85k | 252 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb | [danodus__ecp5_hdmi_audio_video](https://github.com/danodus/ecp5_hdmi_audio_video/blob/a4710f9e7986fe9aafde765b8b3f264ca61631be/boards/ulx3s/ulx3s_v316.lpf) |
| `ulx3s.lpf` | 10 | ULX3S | v2.x/v3.0.x (ulx3s_v20) | 85k | 184 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, ps2, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb | [danodus__msx_fpga](https://github.com/danodus/msx_fpga/blob/f3266f78762094ab3eb5621279011efb504c69df/ulx3s/ulx3s.lpf) |
| `ulx3s_v20_segpdi.lpf` | 9 | ULX3S | v2.x/v3.0.x (ulx3s_v20) | 12k/25k/45k/85k | 184 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb | [circuit-killer__fpga-usbserial](https://github.com/Circuit-killer/fpga-usbserial/blob/bc9e18e84df7025315bd08c71bc4d17b0b5b6a0b/proj/lattice/ulx3s/constraints/ulx3s_v20_segpdi.lpf) |
| `ulx3s_v20.lpf` | 8 | ULX3S | v2.x/v3.0.x (ulx3s_v20) | 12k/85k | 184 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb | [danodus__ulx3s_sms](https://github.com/danodus/ulx3s_sms/blob/13c2361a5039d205de47857bab9201055ac9e566/ulx3s/ulx3s_v20.lpf) |
| `ulx3s_v20.lpf` | 8 | ULX3S | v2.x/v3.0.x (ulx3s_v20) | 12k/25k/45k/85k | 183 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb | [f32c__f32c](https://github.com/f32c/f32c/blob/7dbf56d42a94ae599eabfd1e7fa15db14a10afd7/rtl/proj/lattice/constraints/ulx3s_v20.lpf) |
| `ulx3s_v20.lpf` | 8 | ULX3S | v2.x/v3.0.x (ulx3s_v20) | 85k | 179 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb | [stereoninja__stereoninjafpga](https://github.com/StereoNinja/StereoNinjaFPGA/blob/2def6f03fb93285817ced475b7c67dee756ac51a/old/Componets/HDMI_Transciever/TMDS_Encoder/ulx3s_v20.lpf) |
| `ulx3s_v17patch.lpf` | 6 | ULX3S | v1.7 patched (ulx3s_v17patch) | 12k/25k/45k/85k | 179 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb | [emard__ulx3s](https://github.com/emard/ulx3s/blob/6a92cec6b177191c5b0f80e260013a1f8ec147dd/doc/constraints/prototype/ulx3s_v17patch.lpf) |
| `ulx3s_v314.lpf` | 6 | ULX3S | v3.1.4 (ulx3s_v314) | 12k/25k/45k/85k | 189 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb | [emard__ulx3s](https://github.com/emard/ulx3s/blob/6a92cec6b177191c5b0f80e260013a1f8ec147dd/doc/constraints/prototype/ulx3s_v314.lpf) |
| `ulx4m_v002.lpf` | 6 | ULX4M | v0.0.2 (file name) | 45k | 155 | button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, rtc-power, sdcard, sdram, spi-flash, switch, usb | [lawrie__apple-one](https://github.com/lawrie/apple-one/blob/40412e90909378db3bd84b7537196ed8799fa477/boards/ulx4m/yosys/ulx4m_v002.lpf) |
| `FFM-LFE5U-V0r0_mit_FFC-CA7-V2r0.lpf` | 5 | ULX3S | unknown | 12k/25k/45k/85k | 198 | ethernet, ftdi-uart, i2c, led, sdcard, sdram, usb | [emard__ulx3s-emi](https://github.com/emard/ulx3s-emi/blob/8c93799e664c3d6ea5f7cbd427667c382f40927c/constraints/FFM-LFE5U-V0r0_mit_FFC-CA7-V2r0.lpf) |
| `ulx3s_v20.lpf` | 5 | ULX3S | v2.x/v3.0.x (ulx3s_v20) | 12k/85k | 183 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb | [acairncross__clash-ulx3s-examples](https://github.com/acairncross/clash-ulx3s-examples/blob/8263d13efbb7c40956e78306a173b19e3b8c167f/ulx3s_v20.lpf) |
| `FFM-LFE5U-V0r0_mit_FFC-CA7-V2r0.lpf` | 4 | FFM-LFE5U module | unknown | 12k/25k/45k/85k | 198 | ethernet, ftdi-uart, i2c, led, sdcard, sdram, usb | [cheyao__oberon](https://github.com/cheyao/oberon/blob/07511b33357a95d68db67fc9351c86a13d106ecf/constraints/FFM-LFE5U-V0r0_mit_FFC-CA7-V2r0.lpf) |
| `FleaFPGA_Ohm_A5.lpf` | 4 | FleaFPGA Ohm/Uno | unknown | 25k | 90 | gpio-header, led, sdcard, sdram, usb | [emard__minimig_ecs](https://github.com/emard/Minimig_ECS/blob/a0a94bfa0b8534f50be7b79086ad00a41184c266/proj/lattice/fleafpga-ohm-ps2kbd/constraints/FleaFPGA_Ohm_A5.lpf) |
| `icepi-zero.lpf` | 4 | IcePi Zero | unknown | 25k | 126 | button, gpio-header, hdmi-dvi, led, sdcard, sdram, spi-flash, usb | [cheyao__icepi-zero](https://github.com/cheyao/icepi-zero/blob/e01faa2bd35dcb7269827f8420b845d46c78c869/gateware/third-party/jtag/icepi-zero.lpf) |
| `pinout.lpf` | 4 | GreyBadge 2025 | unknown | 25k | 22 | button, led | [nusgreyhats__greybadge25](https://github.com/NUSGreyhats/greybadge25/blob/3ce9bfbf0061ee36e17dca1274c2f65ae9a5bb07/firmware/ecp5/tests/fpgaing/shooting_button/pinout.lpf) |
| `ulx2s.lpf` | 4 | ULX2S | unknown | 12k/45k | 159 | button, ftdi-uart, gpio-header, led, sdcard, spi-flash, sram | [emard__uk101onfpga](https://github.com/emard/UK101onFPGA/blob/7264146bca76c6f751039ab569824a59875fe976/proj/lattice/orao_ulx2s_sram_composite/ulx2s.lpf) |
| `ulx3s.lpf` | 4 | ULX3S | v2.x/v3.0.x (ulx3s_v20), v1.7 patched (ulx3s_v17patch), v3.1.4 (ulx3s_v314) | 85k | 57 | button, esp32-wifi, ftdi-uart, hdmi-dvi, led, sdram | [jlopezr__mini-gpu](https://github.com/jlopezr/mini-gpu/blob/5c50faef39e53dadacede43ea8b1cd6290d1be95/16.fpga-cpu-hdmi/ulx3s.lpf) |
| `ulx3s_v17patch.lpf` | 4 | ULX3S | v1.7 patched (ulx3s_v17patch) | 12k/25k/45k/85k | 179 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb | [circuit-killer__fpga-usbhid-host](https://github.com/Circuit-killer/fpga-usbhid-host/blob/166e991b17db73b5a1158969ca7c8b9a4cecfb36/proj/lattice/constraints/ulx3s_v17patch.lpf) |
| `ulx3s_v20.lpf` | 4 | ULX3S | v2.x/v3.0.x (ulx3s_v20) | 12k/85k | 184 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb | [felipesanches__anotherworld_fpga](https://github.com/felipesanches/AnotherWorld_FPGA/blob/61dc2512597ec0e183afd360d95e2a3b1e759e66/ulx3s_v20.lpf) |
| `ulx3s_v20_dif.lpf` | 4 | ULX3S | v2.x/v3.0.x (ulx3s_v20) | 12k/25k/45k/85k | 184 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb | [circuit-killer__fpga-usbserial](https://github.com/Circuit-killer/fpga-usbserial/blob/bc9e18e84df7025315bd08c71bc4d17b0b5b6a0b/proj/lattice/constraints/ulx3s_v20_dif.lpf) |
| `ulx3s_v31.lpf` | 4 | ULX3S | v3.1.4 (ulx3s_v314) | 12k/25k/45k/85k | 189 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb | [cheyao__oberon](https://github.com/cheyao/oberon/blob/07511b33357a95d68db67fc9351c86a13d106ecf/constraints/ulx3s_v31.lpf) |
| `ulx3s_v314.lpf` | 4 | ULX3S | v3.1.6/v3.1.7 (ulx3s_v316) | 12k/25k/85k | 252 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb | [emard__tinyfpga-bootloader-ulx3s](https://github.com/emard/tinyfpga-bootloader-ulx3s/blob/8e8ab8036c440a24be3279107dc689a197d2ef17/boards/ulx3s/constraints/ulx3s_v314.lpf) |
| `ULX3S.lpf` | 3 | ULX3S | v2.x/v3.0.x (ulx3s_v20) | 85k | 246 | adc, audio, button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, oled-lcd, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb | [fedy0__neo](https://github.com/fedy0/neo/blob/1fcd64bba20ddbd263b9274bccb89604c7252152/ULX3S.lpf) |

## LPFs for boards other than ULX3S

| Name | Board | Device | Chips | Repo |
|---|---|---|---|---|
| [`icepi-zero.lpf`](https://github.com/cheyao/icepi-zero/blob/e01faa2bd35dcb7269827f8420b845d46c78c869/gateware/blinky/icepi-zero.lpf) | IcePi Zero | 25k | button, gpio-header, hdmi-dvi, led, sdcard, sdram, spi-flash, usb | cheyao__icepi-zero |
| [`ulx4m_v002.lpf`](https://github.com/lawrie/apple-one/blob/40412e90909378db3bd84b7537196ed8799fa477/boards/ulx4m/yosys/ulx4m_v002.lpf) | ULX4M | 45k | button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, rtc-power, sdcard, sdram, spi-flash, switch, usb | lawrie__apple-one |
| [`FFM-LFE5U-V0r0_mit_FFC-CA7-V2r0.lpf`](https://github.com/cheyao/oberon/blob/07511b33357a95d68db67fc9351c86a13d106ecf/constraints/FFM-LFE5U-V0r0_mit_FFC-CA7-V2r0.lpf) | FFM-LFE5U module | 12k/25k/45k/85k | ethernet, ftdi-uart, i2c, led, sdcard, sdram, usb | cheyao__oberon |
| [`FleaFPGA_Ohm_A5.lpf`](https://github.com/emard/Minimig_ECS/blob/a0a94bfa0b8534f50be7b79086ad00a41184c266/proj/lattice/fleafpga-ohm-ps2kbd/constraints/FleaFPGA_Ohm_A5.lpf) | FleaFPGA Ohm/Uno | 25k | gpio-header, led, sdcard, sdram, usb | emard__minimig_ecs |
| [`icepi-zero.lpf`](https://github.com/cheyao/icepi-zero/blob/e01faa2bd35dcb7269827f8420b845d46c78c869/gateware/third-party/jtag/icepi-zero.lpf) | IcePi Zero | 25k | button, gpio-header, hdmi-dvi, led, sdcard, sdram, spi-flash, usb | cheyao__icepi-zero |
| [`pinout.lpf`](https://github.com/NUSGreyhats/greybadge25/blob/3ce9bfbf0061ee36e17dca1274c2f65ae9a5bb07/firmware/ecp5/tests/fpgaing/shooting_button/pinout.lpf) | GreyBadge 2025 | 25k | button, led | nusgreyhats__greybadge25 |
| [`ulx2s.lpf`](https://github.com/emard/UK101onFPGA/blob/7264146bca76c6f751039ab569824a59875fe976/proj/lattice/orao_ulx2s_sram_composite/ulx2s.lpf) | ULX2S | 12k/45k | button, ftdi-uart, gpio-header, led, sdcard, spi-flash, sram | emard__uk101onfpga |
| [`had19_proto2.lpf`](https://github.com/hexagon5un/hackaday_supercon_2019_logic_noise_FPGA_workshop/blob/1297ac5f3111212b27e0f3ac2ace908b2e2d4a6c/includes/had19_proto2.lpf) | Hackaday 2019 badge | 45k | adc, button, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, psram, spi-flash, usb | hexagon5un__hackaday_supercon_2019_logic_noise_fpga_workshop |
| [`pergola_hdmi.lpf`](https://github.com/kbeckmann/pergola_projects/blob/1bb4e1318de40cd6a5ad131de50cdb01ce81a8ac/verilog/hdmi_passthrough_ddr1x/pergola_hdmi.lpf) | Pergola | 12k | button, hdmi-dvi, led | kbeckmann__pergola_projects |
| [`FFM-LFE5U-V0r0_mit_FFC-CA7-V2r0.lpf`](https://github.com/emard/Minimig_ECS/blob/a0a94bfa0b8534f50be7b79086ad00a41184c266/proj/lattice/constraints/FFM-LFE5U-V0r0_mit_FFC-CA7-V2r0.lpf) | FFM-LFE5U module | 25k/45k | ethernet, ftdi-uart, i2c, led, sdcard, sdram, usb | emard__minimig_ecs |
| [`FleaFPGA_Ohm_A5.lpf`](https://github.com/Circuit-killer/fpga-usbhid-host/blob/166e991b17db73b5a1158969ca7c8b9a4cecfb36/proj/fleafpga_ohm/FleaFPGA_Ohm_A5.lpf) | FleaFPGA Ohm/Uno | 12k/25k/45k/85k | gpio-header, led, sdcard, sdram, usb | circuit-killer__fpga-usbhid-host |
| [`FleaFPGA_Uno_revE_top.lpf`](https://github.com/emard/vhdl_phoenix/blob/43f3b39cc87f71835844d200c83f3c7735eaec68/proj/lattice/fleafpga/constraints/FleaFPGA_Uno_revE_top.lpf) | FleaFPGA Ohm/Uno | 12k/25k/45k/85k | adc, audio, esp32-wifi, gpio-header, ps2, sram | emard__vhdl_phoenix |
| [`Flea_Ohm_revision_A3.lpf`](https://github.com/cheyao/oberon/blob/07511b33357a95d68db67fc9351c86a13d106ecf/constraints/Flea_Ohm_revision_A3.lpf) | FleaFPGA Ohm/Uno | 12k/25k/45k/85k | adc, gpio-header, ps2, sdcard, sdram | cheyao__oberon |
| [`blink.lpf`](https://github.com/kholia/Colorlight-5A-75B/blob/9d4433be7c9a719af739fa958889c98b05a91515/blink/blink.lpf) | Colorlight | 25k | led | kholia__colorlight-5a-75b |
| [`colorlighti5.lpf`](https://github.com/splinedrive/kianRiscV/blob/da994e6c25b0667d6579922f4bab8d800d19e944/linux_socs/kianv_mc_rv32ima_sv32/engineering/boards/colorlighti5/colorlighti5.lpf) | Colorlight | 25k/45k | adc, button, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, psram, radio-antenna, rtc-power, sdcard, sdram, spi-flash, switch, usb | splinedrive__kianriscv |
| [`darksocv.lpf`](https://github.com/darklife/darkriscv/blob/974034aa8079039a36b89c14dcdfed575de183b7/boards/colorlighti5/darksocv.lpf) | Colorlight | 25k/45k | ftdi-uart, led | darklife__darkriscv |
| [`dds.lpf`](https://github.com/kholia/Colorlight-5A-75B/blob/9d4433be7c9a719af739fa958889c98b05a91515/dds_ssb_docker/dds.lpf) | Colorlight | 25k | led, radio-antenna | kholia__colorlight-5a-75b |
| [`had19_proto1.lpf`](https://github.com/hexagon5un/hackaday_supercon_2019_logic_noise_FPGA_workshop/blob/1297ac5f3111212b27e0f3ac2ace908b2e2d4a6c/includes/had19_proto1.lpf) | Hackaday 2019 badge | 45k | button, led | hexagon5un__hackaday_supercon_2019_logic_noise_fpga_workshop |
| [`had19_proto3.lpf`](https://github.com/hexagon5un/hackaday_supercon_2019_logic_noise_FPGA_workshop/blob/1297ac5f3111212b27e0f3ac2ace908b2e2d4a6c/includes/had19_proto3.lpf) | Hackaday 2019 badge | 45k | adc, button, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, psram, spi-flash, usb | hexagon5un__hackaday_supercon_2019_logic_noise_fpga_workshop |
| [`icepi-zero-v1_2.lpf`](https://github.com/splinedrive/kianRiscV/blob/da994e6c25b0667d6579922f4bab8d800d19e944/linux_socs/LinuxSoC_v2/engineering/boards/icepi-zero/icepi-zero-v1_2.lpf) | IcePi Zero | 25k | button, ftdi-uart, gpio-header, hdmi-dvi, led, sdcard, sdram, spi-flash, usb | splinedrive__kianriscv |
| [`icepi-zero-v1_3.lpf`](https://github.com/splinedrive/kianRiscV/blob/da994e6c25b0667d6579922f4bab8d800d19e944/linux_socs/LinuxSoC_v2/engineering/boards/icepi-zero/icepi-zero-v1_3.lpf) | IcePi Zero | 25k | button, ftdi-uart, gpio-header, hdmi-dvi, led, sdcard, sdram, spi-flash, usb | splinedrive__kianriscv |
| [`icepi-zero.lpf`](https://github.com/cheyao/sega-sms/blob/c37e846d94f88eb9a95f44b15f2b23019aa25a26/icepi-zero/icepi-zero.lpf) | IcePi Zero | 25k/85k | button, gpio-header, hdmi-dvi, led, sdcard, sdram, spi-flash, usb | cheyao__sega-sms |
| [`icesugar-pro.lpf`](https://github.com/splinedrive/kianRiscV/blob/da994e6c25b0667d6579922f4bab8d800d19e944/linux_socs/LinuxSoC_v2/engineering/boards/icesugar_pro/icesugar-pro.lpf) | iCESugar-Pro | 25k | esp32-wifi, ftdi-uart, led, sdram, spi-flash | splinedrive__kianriscv |
| [`icesugar_pro.lpf`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/projects/02_hdmi_test/icesugar_pro.lpf) | iCESugar-Pro | 25k | hdmi-dvi, led | mebner86__icesugar-pro_sound2fft |
| [`icesugar_pro.lpf`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/projects/03_i2s_direct_loopback/icesugar_pro.lpf) | iCESugar-Pro | 25k | led | mebner86__icesugar-pro_sound2fft |
| [`icesugar_pro.lpf`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/projects/06_live_fft/icesugar_pro.lpf) | iCESugar-Pro | 25k | hdmi-dvi, led | mebner86__icesugar-pro_sound2fft |
| [`icesugar_pro.lpf`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/projects/08_pdm_bitstream_loopback/icesugar_pro.lpf) | iCESugar-Pro | 25k | led | mebner86__icesugar-pro_sound2fft |
| [`orangecrab.lpf`](https://github.com/hsa-ees/piconut/blob/826460dc12cd22c2b6e177182b9d63abdc1eabe0/boards/orangecrab/orangecrab.lpf) | OrangeCrab | 85k | ftdi-uart | hsa-ees__piconut |
| [`ulx2s.lpf`](https://github.com/emard/flearadio/blob/5439d88e3f1a85113a6c8f6ee724a86edbd9f938/rtl/proj/lattice/ulx2s/ulx2s.lpf) | ULX2S | 25k | button, ftdi-uart, gpio-header, led, sdcard, spi-flash, sram | emard__flearadio |
| [`ulx2s.lpf`](https://github.com/emard/rdsfpga/blob/12a8b817f2bc8cabfb3d7d3cc4fb0ab1a95cfedf/diamond/ulx2s.lpf) | ULX2S | unknown | button, ftdi-uart, gpio-header, led, sdcard, spi-flash, sram | emard__rdsfpga |
| [`ulx2s.lpf`](https://github.com/emard/synthowheel/blob/c2c6b2435418099f96397f2bd84bf87dcc4083e9/ulx2s/ulx2s.lpf) | ULX2S | 12k/25k/45k/85k | button, ftdi-uart, gpio-header, led, oled-lcd, sdcard, spi-flash, sram, switch | emard__synthowheel |
| [`ulx4m_v002.lpf`](https://github.com/danodus/ulx3s_sms/blob/13c2361a5039d205de47857bab9201055ac9e566/ulx4m/ulx4m_v002.lpf) | ULX4M | 45k | button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, rtc-power, sdcard, sdram, spi-flash, switch, usb | danodus__ulx3s_sms |
| [`FFM-LFE5U-V0r0_mit_FFC-CA7-V2r0.lpf`](https://github.com/emard/Next186/blob/cfd9550f7aa4f126839692755d4eb3793ea5e40e/constraints/FFM-LFE5U-V0r0_mit_FFC-CA7-V2r0.lpf) | FFM-LFE5U module | 85k | ethernet, ftdi-uart, i2c, led, sdcard, sdram, usb | emard__next186 |
| [`FleaFPGA_2v5_DSO_toplevel.lpf`](https://github.com/emard/flearadio/blob/5439d88e3f1a85113a6c8f6ee724a86edbd9f938/rtl/proj/lattice/fleafpga/FleaFPGA_2v5_DSO_toplevel.lpf) | FleaFPGA Ohm/Uno | unknown | audio, gpio-header, ps2, sdcard, sdram, vga | emard__flearadio |
| [`OrangeCrab.lpf`](https://github.com/stnolting/neorv32-setups/blob/57f86d5ad3fa54f6919165b7bcc61fad9a5cae0a/osflow/constraints/OrangeCrab.lpf) | OrangeCrab | 85k | spi-flash | stnolting__neorv32-setups |
| [`blink.lpf`](https://github.com/kholia/Colorlight-5A-75B/blob/9d4433be7c9a719af739fa958889c98b05a91515/blink_docker/blink.lpf) | Colorlight | 25k | led | kholia__colorlight-5a-75b |
| [`blink.lpf`](https://github.com/wuxx/Colorlight-FPGA-Projects/blob/5042201f6ae848d4269680cc289c7bde3ab8cf71/src/i5/blink/blink.lpf) | Colorlight | 25k | led | wuxx__colorlight-fpga-projects |
| [`blink.lpf`](https://github.com/wuxx/Colorlight-FPGA-Projects/blob/5042201f6ae848d4269680cc289c7bde3ab8cf71/src/i9/blink/blink.lpf) | Colorlight | 45k | led | wuxx__colorlight-fpga-projects |
| [`blink.lpf`](https://github.com/wuxx/icesugar-pro/blob/087e48d9e0b0a0168ce165a961cba306335c4cf2/src/blink/blink.lpf) | iCESugar-Pro | 25k | led | wuxx__icesugar-pro |
| [`blinky.lpf`](https://github.com/fusesoc/blinky/blob/496eae5e447151c1ca720f995d292e2e99349b22/colorlight_5a75b/blinky.lpf) | Colorlight | 45k/85k |  | fusesoc__blinky |
| [`blinky.lpf`](https://github.com/fusesoc/blinky/blob/496eae5e447151c1ca720f995d292e2e99349b22/ecp5_evn/blinky.lpf) | ECP5 Evaluation board | 45k/85k |  | fusesoc__blinky |
| [`colorlight-i5.lpf`](https://github.com/racerxdl/colorlight-picorv32/blob/73daf2842c5c1fc147bc59c4589d2150a260fe6b/constraints/colorlight-i5.lpf) | Colorlight | 25k | ftdi-uart, gpio-header, led, sdram | racerxdl__colorlight-picorv32 |
| [`colorlight_5A-75B.lpf`](https://github.com/antonblanchard/chiselwatt/blob/61a07a99046f8ffe56f33918c8f9685ab7a75fb5/constraints/colorlight_5A-75B.lpf) | Colorlight | 25k/85k |  | antonblanchard__chiselwatt |
| [`colorlight_i9_v7.2.lpf`](https://github.com/DatanoiseTV/colorlight-i9-aes67/blob/71420b772d48409ae8e3a70c3103828495687737/constraints/colorlight_i9_v7.2.lpf) | Colorlight | 45k | audio, ethernet, led, sdram, spi-flash | datanoisetv__colorlight-i9-aes67 |
| [`colorlight_i9_v7.2.lpf`](https://github.com/sylefeb/Silice/blob/620487d6b83035dd98299734c8c8fccf8f636005/frameworks/boards/colorlight/colorlight_i9_v7.2.lpf) | Colorlight | 45k | ftdi-uart, hdmi-dvi, led, rtc-power, sdram, spi-flash | sylefeb__silice |
| [`colorlighti5.lpf`](https://github.com/splinedrive/my_hdmi_device/blob/16a93372a9e07d27b23cf093a649dc870c208851/colorlighti5.lpf) | Colorlight | 85k | adc, button, esp32-wifi, ftdi-uart, hdmi-dvi, led, oled-lcd, radio-antenna, rtc-power, sdcard, spi-flash, switch, usb | splinedrive__my_hdmi_device |
| [`constraints_colorlight_i5.lpf`](https://github.com/Hassan2203/System-On-Chip-SOC-Design-and-verification/blob/f4fa639aa86ab3867d2dd1644a289a6e57797270/constraints_colorlight_i5.lpf) | Colorlight | 45k | led | hassan2203__system-on-chip-soc-design-and-verification |
| [`dds.lpf`](https://github.com/kholia/Colorlight-5A-75B/blob/9d4433be7c9a719af739fa958889c98b05a91515/dds_ssb_uart/dds.lpf) | Colorlight | 25k | ftdi-uart, led, radio-antenna | kholia__colorlight-5a-75b |
| [`dds.lpf`](https://github.com/kholia/Colorlight-5A-75B/blob/9d4433be7c9a719af739fa958889c98b05a91515/dds_ssb_uart_alt/dds.lpf) | Colorlight | 25k | ftdi-uart, led, radio-antenna | kholia__colorlight-5a-75b |
| [`ecp3versa.lpf`](https://github.com/hdl4fpga/hdl4fpga/blob/662986ba0f17b7ce3a066ddcb799d42fa1b24dea/boards/ecp3versa/diamond/ecp3versa.lpf) | Versa ECP5 | 12k | ddr3, led, switch | hdl4fpga__hdl4fpga |
| [`ecp5-evn.lpf`](https://github.com/antonblanchard/chiselwatt/blob/61a07a99046f8ffe56f33918c8f9685ab7a75fb5/constraints/ecp5-evn.lpf) | ECP5 Evaluation board | 25k/85k |  | antonblanchard__chiselwatt |
| [`ecp5-evn.lpf`](https://github.com/wuxx/icesugar/blob/1ebe71bf448e33a1bccfa2db6730d59eafb6c390/src/advanced/icicle/boards/ecp5-evn.lpf) | ECP5 Evaluation board | 85k | ftdi-uart, led, spi-flash | wuxx__icesugar |
| [`ecp5_evn.lpf`](https://github.com/BrunoLevy/learn-fpga/blob/5c08c870315c09ccd9ec64ccde20ab3375b3f273/FemtoRV/BOARDS/ecp5_evn.lpf) | ECP5 Evaluation board | 85k | oled-lcd | brunolevy__learn-fpga |
| [`ecp5_evn.lpf`](https://github.com/BrunoLevy/learn-fpga/blob/5c08c870315c09ccd9ec64ccde20ab3375b3f273/FemtoRV/TUTORIALS/FROM_BLINKER_TO_RISCV/BOARDS/ecp5_evn.lpf) | ECP5 Evaluation board | 85k | led | brunolevy__learn-fpga |
| [`ecp5_jtag.lpf`](https://github.com/tomverbeure/ecp5_jtag/blob/6a2302e079d003ddce8335a5300172fdbb2bd1b5/colorlight_i5/ecp5_jtag.lpf) | Colorlight | 25k | led | tomverbeure__ecp5_jtag |
| [`ecp5evn.lpf`](https://github.com/xtrinch/fpga-bitcoin-miner/blob/7c9ca1c3776b533166c54d35ab7172ccb675a09c/src/ecp5evn.lpf) | ECP5 Evaluation board | 85k | led | xtrinch__fpga-bitcoin-miner |
| [`ecpix5.lpf`](https://github.com/sylefeb/Silice/blob/620487d6b83035dd98299734c8c8fccf8f636005/frameworks/boards/ecpix5/ecpix5.lpf) | ECPIX-5 | 85k | ftdi-uart, led | sylefeb__silice |
| [`fpga_ulx4m_ld.lpf`](https://github.com/ulx3s/Hazard3/blob/3c0aca063517bb7fdbe869019c984954c7dd5c97/example_soc/synth/fpga_ulx4m_ld.lpf) | ULX4M | 85k | ddr3, ftdi-uart, hdmi-dvi, led, sdcard | ulx3s__hazard3 |
| [`fpga_ulx4m_ld_blinky.lpf`](https://github.com/ulx3s/Hazard3/blob/3c0aca063517bb7fdbe869019c984954c7dd5c97/example_soc/synth/fpga_ulx4m_ld_blinky.lpf) | ULX4M | 85k | led | ulx3s__hazard3 |
| [`fpga_ulx4m_ld_v002.lpf`](https://github.com/ulx3s/Hazard3/blob/3c0aca063517bb7fdbe869019c984954c7dd5c97/example_soc/synth/fpga_ulx4m_ld_v002.lpf) | ULX4M | 85k | ddr3, ftdi-uart, hdmi-dvi, led | ulx3s__hazard3 |
| [`fpga_ulx4m_ls.lpf`](https://github.com/ulx3s/Hazard3/blob/3c0aca063517bb7fdbe869019c984954c7dd5c97/example_soc/synth/fpga_ulx4m_ls.lpf) | ULX4M | 85k | ftdi-uart, hdmi-dvi, led, sdram | ulx3s__hazard3 |
| [`had19_prod.lpf`](https://github.com/Spritetm/hadbadge2019_fpgasoc/blob/6e706d52ecdc007e9179bda01d8eac60d55b7c45/soc/had19_prod.lpf) | Hackaday 2019 badge | 45k | adc, button, ftdi-uart, gpio-header, hdmi-dvi, led, oled-lcd, psram, spi-flash, usb | spritetm__hadbadge2019_fpgasoc |
| [`had19_proto1.lpf`](https://github.com/Spritetm/hadbadge2019_fpgasoc/blob/6e706d52ecdc007e9179bda01d8eac60d55b7c45/soc/had19_proto1.lpf) | Hackaday 2019 badge | 45k | button, ftdi-uart, hdmi-dvi, led, oled-lcd, psram, spi-flash, usb | spritetm__hadbadge2019_fpgasoc |
| [`icepi-zero-v1_0.lpf`](https://github.com/cheyao/icepi-zero/blob/e01faa2bd35dcb7269827f8420b845d46c78c869/gateware/v1.0/icepi-zero-v1_0.lpf) | IcePi Zero | 25k | button, gpio-header, hdmi-dvi, led, sdcard, sdram, spi-flash, usb | cheyao__icepi-zero |
| [`icepi-zero-v1_1.lpf`](https://github.com/cheyao/icepi-zero/blob/e01faa2bd35dcb7269827f8420b845d46c78c869/gateware/v1.1/icepi-zero-v1_1.lpf) | IcePi Zero | 25k | button, gpio-header, hdmi-dvi, led, sdcard, sdram, spi-flash, usb | cheyao__icepi-zero |
| [`icepi-zero-v1_2.lpf`](https://github.com/cheyao/icepi-zero/blob/e01faa2bd35dcb7269827f8420b845d46c78c869/gateware/v1.2/icepi-zero-v1_2.lpf) | IcePi Zero | 25k | button, gpio-header, hdmi-dvi, led, sdcard, sdram, spi-flash, usb | cheyao__icepi-zero |
| [`icepi-zero.lpf`](https://github.com/alangarf/apple-one/blob/0f15ef6d62c2f8820aa5a68b7f973eef4a78dd8d/boards/icepi_zero/yosys/icepi-zero.lpf) | IcePi Zero | 25k | button, gpio-header, hdmi-dvi, led, sdcard, sdram, spi-flash, usb | alangarf__apple-one |
| [`icepi-zero.lpf`](https://github.com/cheyao/icepi-zero/blob/e01faa2bd35dcb7269827f8420b845d46c78c869/gateware/third-party/dvi/hdl/icepi-zero.lpf) | IcePi Zero | 25k | button, ftdi-uart, gpio-header, hdmi-dvi, led, sdcard, sdram, spi-flash, usb | cheyao__icepi-zero |
| [`icepi-zero.lpf`](https://github.com/cheyao/icepi-zero/blob/e01faa2bd35dcb7269827f8420b845d46c78c869/gateware/third-party/dvi/icepi-zero.lpf) | IcePi Zero | 25k | button, gpio-header, hdmi-dvi, led, sdcard, sdram, spi-flash, usb | cheyao__icepi-zero |
| [`icepi-zero.lpf`](https://github.com/cheyao/nes_ecp5/blob/e8dd1eb7f9f440a552cd24c0b936e58705a272e7/icepi-zero.lpf) | IcePi Zero | 25k | button, gpio-header, hdmi-dvi, led, sdcard, sdram, spi-flash, usb | cheyao__nes_ecp5 |
| [`icepi-zero.lpf`](https://github.com/sylefeb/Silice/blob/620487d6b83035dd98299734c8c8fccf8f636005/frameworks/boards/icepi_zero/icepi-zero.lpf) | IcePi Zero | 25k | button, gpio-header, hdmi-dvi, led, sdcard, sdram, spi-flash, usb | sylefeb__silice |
| [`icepi_zero.lpf`](https://github.com/danodus/ecp5_hdmi_audio_video/blob/a4710f9e7986fe9aafde765b8b3f264ca61631be/boards/icepi_zero/icepi_zero.lpf) | IcePi Zero | 25k | hdmi-dvi | danodus__ecp5_hdmi_audio_video |
| [`icesugar-pro.lpf`](https://github.com/splinedrive/kianRiscV/blob/da994e6c25b0667d6579922f4bab8d800d19e944/linux_socs/kianv_harris_mcycle_edition/icesugar-pro.lpf) | iCESugar-Pro | 25k | esp32-wifi, ftdi-uart, led, sdram, spi-flash | splinedrive__kianriscv |
| [`icesugar_pro.lpf`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/projects/01_blinky/icesugar_pro.lpf) | iCESugar-Pro | 25k | led | mebner86__icesugar-pro_sound2fft |
| [`icesugar_pro.lpf`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/projects/09_pdm_sigma_delta_modulator/icesugar_pro.lpf) | iCESugar-Pro | 25k | led | mebner86__icesugar-pro_sound2fft |
| [`icesugar_pro.lpf`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/projects/11_pdm_to_i2s_loopback/icesugar_pro.lpf) | iCESugar-Pro | 25k | led | mebner86__icesugar-pro_sound2fft |
| [`icesugar_pro.lpf`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/projects/12_uart_loopback/icesugar_pro.lpf) | iCESugar-Pro | 25k | ftdi-uart, led | mebner86__icesugar-pro_sound2fft |
| [`icesugar_pro.lpf`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/projects/13_fft_uart/icesugar_pro.lpf) | iCESugar-Pro | 25k | ftdi-uart, led | mebner86__icesugar-pro_sound2fft |
| [`icesugar_pro.lpf`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/projects/14_i2s_record_to_uart/icesugar_pro.lpf) | iCESugar-Pro | 25k | ftdi-uart, led | mebner86__icesugar-pro_sound2fft |
| [`icesugar_pro.lpf`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/projects/15_pdm_hil/icesugar_pro.lpf) | iCESugar-Pro | 25k | ftdi-uart, led | mebner86__icesugar-pro_sound2fft |
| [`icesugar_pro.lpf`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/projects/16_pdm_replay/icesugar_pro.lpf) | iCESugar-Pro | 25k | led | mebner86__icesugar-pro_sound2fft |
| [`icesugar_pro.lpf`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/projects/17_hil_2mics/icesugar_pro.lpf) | iCESugar-Pro | 25k | ftdi-uart, led | mebner86__icesugar-pro_sound2fft |
| [`icesugar_pro.lpf`](https://github.com/wuxx/icesugar-pro/blob/087e48d9e0b0a0168ce165a961cba306335c4cf2/src/hdmi_test_pattern/icesugar_pro.lpf) | iCESugar-Pro | 25k | esp32-wifi, hdmi-dvi | wuxx__icesugar-pro |
| [`icesugarpro.lpf`](https://github.com/robinsonb5/EightThirtyTwoDemos/blob/223a4f141cd9c1edee9b2b42a1d4275566019ea4/Board/icesugarpro/icesugarpro.lpf) | iCESugar-Pro | 25k | gpio-header, hdmi-dvi, led, sdram | robinsonb5__eightthirtytwodemos |
| [`io.lpf`](https://github.com/wuxx/Colorlight-FPGA-Projects/blob/5042201f6ae848d4269680cc289c7bde3ab8cf71/src/i5/common/io.lpf) | Colorlight | 25k/45k | gpio-header, led | wuxx__colorlight-fpga-projects |
| [`liteeth_core.lpf`](https://github.com/lucysrausch/colorlight-led-cube/blob/ebac05e1faed52fef736eef9c1a2e3b0c391b68c/fpga/liteeth_core.lpf) | Colorlight | 25k | ethernet | lucysrausch__colorlight-led-cube |
| [`ocadc.lpf`](https://github.com/emeb/orangecrab_adc/blob/daa94e19abb11e3cee3bc1e97d87908b6da1e08a/gateware/verilog/trellis/ocadc.lpf) | OrangeCrab | 25k | adc, button, led, usb | emeb__orangecrab_adc |
| [`orangecrab.lpf`](https://github.com/hdl4fpga/hdl4fpga/blob/662986ba0f17b7ce3a066ddcb799d42fa1b24dea/boards/orangecrab/diamond/orangecrab.lpf) | OrangeCrab | 25k | ddr3, gpio-header, led, usb | hdl4fpga__hdl4fpga |
| [`orangecrab_r02.lpf`](https://github.com/fusesoc/blinky/blob/496eae5e447151c1ca720f995d292e2e99349b22/orangecrab/orangecrab_r02.lpf) | OrangeCrab | 45k/85k | button | fusesoc__blinky |
| [`pergola.lpf`](https://github.com/kbeckmann/pergola_projects/blob/1bb4e1318de40cd6a5ad131de50cdb01ce81a8ac/verilog/pergola.lpf) | Pergola | 12k | button, led | kbeckmann__pergola_projects |
| [`pergola_hdmi.lpf`](https://github.com/kbeckmann/pergola_projects/blob/1bb4e1318de40cd6a5ad131de50cdb01ce81a8ac/verilog/hdmi_passthrough/pergola_hdmi.lpf) | Pergola | 12k | button, hdmi-dvi, led | kbeckmann__pergola_projects |
| [`pinout.lpf`](https://github.com/NUSGreyhats/greybadge25/blob/3ce9bfbf0061ee36e17dca1274c2f65ae9a5bb07/firmware/ecp5/main/pinout.lpf) | GreyBadge 2025 | 25k | button, gpio-header, led | nusgreyhats__greybadge25 |
| [`pinout.lpf`](https://github.com/NUSGreyhats/greybadge25/blob/3ce9bfbf0061ee36e17dca1274c2f65ae9a5bb07/firmware/ecp5/tests/fpgaing/fpga_clock_test/pinout.lpf) | GreyBadge 2025 | 25k | led | nusgreyhats__greybadge25 |
| [`pinout.lpf`](https://github.com/NUSGreyhats/greybadge25/blob/3ce9bfbf0061ee36e17dca1274c2f65ae9a5bb07/firmware/ecp5/tests/fpgaing/fpga_test/pinout.lpf) | GreyBadge 2025 | 25k | led | nusgreyhats__greybadge25 |
| [`pinout.lpf`](https://github.com/NUSGreyhats/greybadge25/blob/3ce9bfbf0061ee36e17dca1274c2f65ae9a5bb07/firmware/ecp5/tests/fpgaing/shooting/pinout.lpf) | GreyBadge 2025 | 25k | button, led | nusgreyhats__greybadge25 |
| [`pinout.lpf`](https://github.com/NUSGreyhats/greybadge25/blob/3ce9bfbf0061ee36e17dca1274c2f65ae9a5bb07/firmware/ecp5/tests/fpgaing/spi_latch_test/pinout.lpf) | GreyBadge 2025 | 25k | button, gpio-header, led | nusgreyhats__greybadge25 |
| [`pinout.lpf`](https://github.com/NUSGreyhats/greybadge25/blob/3ce9bfbf0061ee36e17dca1274c2f65ae9a5bb07/firmware/ecp5/tests/pmod_oled_test/pinout.lpf) | GreyBadge 2025 | 25k | button, gpio-header, led | nusgreyhats__greybadge25 |
| [`pinout.lpf`](https://github.com/NUSGreyhats/greybadge25/blob/3ce9bfbf0061ee36e17dca1274c2f65ae9a5bb07/firmware/ecp5/uart_coprocessor/pinout.lpf) | GreyBadge 2025 | 25k | button, led | nusgreyhats__greybadge25 |
| [`pinout.lpf`](https://github.com/sylefeb/Silice/blob/620487d6b83035dd98299734c8c8fccf8f636005/frameworks/boards/orangecrab/pinout.lpf) | OrangeCrab | 25k | led | sylefeb__silice |
| [`pong.lpf`](https://github.com/wuxx/Colorlight-FPGA-Projects/blob/5042201f6ae848d4269680cc289c7bde3ab8cf71/src/i5/vga_pong/pong.lpf) | Colorlight | 25k | led, vga | wuxx__colorlight-fpga-projects |
| [`top-had2019-badge.lpf`](https://github.com/emard/had2019-playground/blob/0723f2a536b20f26ec1b2d5cf1dcc2b5355b6808/projects/bootloader/data/top-had2019-badge.lpf) | Hackaday 2019 badge | 12k/85k | button, ftdi-uart, led, spi-flash, usb | emard__had2019-playground |
| [`top-ulx4m-v002.lpf`](https://github.com/emard/had2019-playground/blob/0723f2a536b20f26ec1b2d5cf1dcc2b5355b6808/projects/bootloader/data/top-ulx4m-v002.lpf) | ULX4M | 12k/85k | button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, rtc-power, sdcard, sdram, spi-flash, switch, usb | emard__had2019-playground |
| [`top-ulx4m-v002.lpf`](https://github.com/ulx3s/Hazard3-Doom/blob/42621599f78f7ce3bd51fcc6b95a56ba83e31279/bootloader/data/top-ulx4m-v002.lpf) | ULX4M | 12k | button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, rtc-power, sdcard, sdram, spi-flash, switch, usb | ulx3s__hazard3-doom |
| [`top.lpf`](https://github.com/lucysrausch/colorlight-led-cube/blob/ebac05e1faed52fef736eef9c1a2e3b0c391b68c/fpga/syn/top.lpf) | Colorlight | 25k | button, ethernet, led | lucysrausch__colorlight-led-cube |
| [`top.lpf`](https://github.com/wuxx/Colorlight-FPGA-Projects/blob/5042201f6ae848d4269680cc289c7bde3ab8cf71/src/5a-75b-v7.0/uart_tx/top.lpf) | Colorlight | 25k |  | wuxx__colorlight-fpga-projects |
| [`top.lpf`](https://github.com/wuxx/Colorlight-FPGA-Projects/blob/5042201f6ae848d4269680cc289c7bde3ab8cf71/src/i5/oled_ssd1331/top.lpf) | Colorlight | 25k | oled-lcd | wuxx__colorlight-fpga-projects |
| [`top.lpf`](https://github.com/wuxx/Colorlight-FPGA-Projects/blob/5042201f6ae848d4269680cc289c7bde3ab8cf71/src/i5/picosoc/top.lpf) | Colorlight | 25k | ftdi-uart, led | wuxx__colorlight-fpga-projects |
| [`top.lpf`](https://github.com/wuxx/Colorlight-FPGA-Projects/blob/5042201f6ae848d4269680cc289c7bde3ab8cf71/src/i5/rgblcd/top.lpf) | Colorlight | 25k | led, oled-lcd | wuxx__colorlight-fpga-projects |
| [`top.lpf`](https://github.com/wuxx/Colorlight-FPGA-Projects/blob/5042201f6ae848d4269680cc289c7bde3ab8cf71/src/i5/uart_tx/top.lpf) | Colorlight | 25k |  | wuxx__colorlight-fpga-projects |
| [`top.lpf`](https://github.com/wuxx/Colorlight-FPGA-Projects/blob/5042201f6ae848d4269680cc289c7bde3ab8cf71/src/i5/vga_rotate/top.lpf) | Colorlight | 25k | led, vga | wuxx__colorlight-fpga-projects |
| [`top.lpf`](https://github.com/wuxx/icesugar-pro/blob/087e48d9e0b0a0168ce165a961cba306335c4cf2/src/uart_tx/top.lpf) | iCESugar-Pro | 25k |  | wuxx__icesugar-pro |
| [`top_bg256.lpf`](https://github.com/wuxx/icesugar-pro/blob/087e48d9e0b0a0168ce165a961cba306335c4cf2/src/litex_linux/top_bg256.lpf) | iCESugar-Pro | 25k | esp32-wifi, ftdi-uart, sdram | wuxx__icesugar-pro |
| [`top_passthru-ulx4m-v002.lpf`](https://github.com/emard/had2019-playground/blob/0723f2a536b20f26ec1b2d5cf1dcc2b5355b6808/projects/bootloader/data/top_passthru-ulx4m-v002.lpf) | ULX4M | 12k/85k | button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, rtc-power, sdcard, sdram, spi-flash, switch, usb | emard__had2019-playground |
| [`top_passthru-ulx4m-v002.lpf`](https://github.com/ulx3s/Hazard3-Doom/blob/42621599f78f7ce3bd51fcc6b95a56ba83e31279/bootloader/data/top_passthru-ulx4m-v002.lpf) | ULX4M | 12k | button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, rtc-power, sdcard, sdram, spi-flash, switch, usb | ulx3s__hazard3-doom |
| [`trellisboard.lpf`](https://github.com/gatecat/TrellisBoard/blob/54e073cb5775e6312db093f4fdbd762250d38ff2/gateware/simple/trellisboard.lpf) | TrellisBoard | 85k | button, led, switch | gatecat__trellisboard |
| [`ulx4m_ld.lpf`](https://github.com/hdl4fpga/hdl4fpga/blob/662986ba0f17b7ce3a066ddcb799d42fa1b24dea/boards/ULX4M_LD/diamond/ulx4m_ld.lpf) | ULX4M | 85k | button, ddr3, ethernet, ftdi-uart, hdmi-dvi, i2c, led, rtc-power, sdcard, usb | hdl4fpga__hdl4fpga |
| [`ulx4m_ls.lpf`](https://github.com/hdl4fpga/hdl4fpga/blob/662986ba0f17b7ce3a066ddcb799d42fa1b24dea/boards/ULX4M_LS/diamond/ulx4m_ls.lpf) | ULX4M | 12k | button, camera, ethernet, ftdi-uart, gpio-header, hdmi-dvi, i2c, led, rtc-power, sdcard, sdram, spi-flash, switch, usb | hdl4fpga__hdl4fpga |
| [`ulx4m_ls.lpf`](https://github.com/sylefeb/Silice/blob/620487d6b83035dd98299734c8c8fccf8f636005/frameworks/boards/ulx4m_ls/ulx4m_ls.lpf) | ULX4M | 12k/25k/45k | button, ftdi-uart, gpio-header, hdmi-dvi, i2c, led, rtc-power, sdcard, sdram, spi-flash, switch, usb | sylefeb__silice |
| [`ulx4m_v002.lpf`](https://github.com/cheyao/nes_ecp5/blob/e8dd1eb7f9f440a552cd24c0b936e58705a272e7/ulx4m_v002.lpf) | ULX4M | 25k | button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, rtc-power, sdcard, sdram, spi-flash, switch, usb | cheyao__nes_ecp5 |
| [`ulx4m_v002.lpf`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/constraints/ulx4m_v002.lpf) | ULX4M | 12k/25k/85k | button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, rtc-power, sdcard, sdram, spi-flash, switch, usb | emard__ulx3s-misc |
| [`ulx4m_v002.lpf`](https://github.com/lawrie/ulx3s_acorn_atom/blob/8364160ee406e127ea9f82f8cd49803e51565112/ulx4m/ulx4m_v002.lpf) | ULX4M | 45k | button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, rtc-power, sdcard, sdram, spi-flash, switch, usb | lawrie__ulx3s_acorn_atom |
| [`ulx4m_v002.lpf`](https://github.com/lawrie/ulx4m_examples/blob/415ee5309545da06b1bda7bfe7ec3a1c65a5376c/ulx4m_v002.lpf) | ULX4M | 85k | button, esp32-wifi, ftdi-uart, gpio-header, hdmi-dvi, led, rtc-power, sdcard, sdram, spi-flash, switch, usb | lawrie__ulx4m_examples |
| [`usb_hid_host_demo.lpf`](https://github.com/machdyne/zeitlos/blob/a7e7e85ee0ad1fd0cfff4129e24b2aa528d444e8/rtl/ext/usb_hid_host/boards/icesugar-pro/usb_hid_host_demo.lpf) | iCESugar-Pro | 25k | ftdi-uart, led, usb | machdyne__zeitlos |
| [`versa_rgmii.lpf`](https://github.com/sefbkn/versa-ecp5-demo/blob/1d6d4cb535e11f935c1afa707b35ded5df4d658d/constraints/versa_rgmii.lpf) | Versa ECP5 | 45k | ftdi-uart, led, serdes-pcie-sata | sefbkn__versa-ecp5-demo |
| [`versa_sgmii.lpf`](https://github.com/sefbkn/versa-ecp5-demo/blob/1d6d4cb535e11f935c1afa707b35ded5df4d658d/constraints/versa_sgmii.lpf) | Versa ECP5 | 45k | ftdi-uart, led, serdes-pcie-sata | sefbkn__versa-ecp5-demo |
