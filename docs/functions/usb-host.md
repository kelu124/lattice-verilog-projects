---
title: "USB host"
parent: "Cores by function"
nav_order: 16
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# USB host

USB low/full-speed host (HID keyboards, mice, gamepads).

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [Ultra-Embedded USB FS host (ulx3s-misc copy)](#core-ulx3s-misc-usbhost) ★ | [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc) | Verilog, VHDL | GPL-2.0-or-later | any | 12 |
| [circuit-killer minimal USB HID host](#core-circuit-killer-usbhid-host) | [circuit-killer__fpga-usbhid-host](https://github.com/Circuit-killer/fpga-usbhid-host) | VHDL | none found | ECP5 | 1 |
| [emard standalone USB1.1 host PHY/SIE (usb_host repo)](#core-emard-usb-host-soc) | [emard__usb_host](https://github.com/emard/usb_host) | Verilog | none found | any | 0 |
| [emard USB host + gamepad report decoders](#core-nes-ecp5-usb-gamepad) | [emard__nes_ecp5](https://github.com/emard/nes_ecp5) | Verilog | GPL-2.0-or-later | any | 4 |
| [hdl4fpga USB 1.1 host core](#core-hdl4fpga-usbhost) | [hdl4fpga__hdl4fpga](https://github.com/hdl4fpga/hdl4fpga) | VHDL | MIT (LICENSE, Miguel Angel Sagreras) | any | 2 |

## Cores

### Ultra-Embedded USB FS host (ulx3s-misc copy) (best) {#core-ulx3s-misc-usbhost}

Ultra-Embedded's full-speed USB host SIE plus a HID-report host driver; the most reused USB-host core in the collection, copied into emard's NES/Apple-1/Minimig/Next186/Papilio-Arcade/Phoenix/Apple2fpga cores for keyboard/gamepad input.

| | |
|---|---|
| Repository | [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc): ULX3S misc/advanced examples: EMARD's building-block library |
| Files | [`examples/usb/usbhost/usbh_sie.v`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/usb/usbhost/usbh_sie.v), [`examples/usb/usbhost/usbh_host_hid.v`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/usb/usbhost/usbh_host_hid.v) |
| Top module | `usbh_sie` |
| Language | Verilog, VHDL (usbh_sie_vhdl.vhd, usbh_host_hid.vhd variants also present) |
| License | GPL-2.0-or-later (file header, Ultra-Embedded.com, Copyright 2015-2019) |
| FPGA / primitives | any: none (portable) |
| Tests | none found in this copy |

**On ULX3S:** Drop-in on ULX3S US2 pins; pair with a report_decoder for the target gamepad/keyboard (see emard__nes_ecp5/usb/report_decoder).

Full review: [emard__ulx3s-misc](../projects/emard__ulx3s-misc.md).

**Used by 12 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [cheyao__nes_ecp5](https://github.com/cheyao/nes_ecp5) (instantiates [`top.v`](https://github.com/cheyao/nes_ecp5/blob/e8dd1eb7f9f440a552cd24c0b936e58705a272e7/top.v))
- [dan-rodrigues__icestation-32](https://github.com/dan-rodrigues/icestation-32) (instantiates [`hardware/usb/gamepads/usb_gamepad_reader.v`](https://github.com/dan-rodrigues/icestation-32/blob/55214d79f74a547dedb54f99cb2fad431b7ac277/hardware/usb/gamepads/usb_gamepad_reader.v))
- [emard__apple2fpga](https://github.com/emard/apple2fpga) (instantiates [`rtl_emard/lattice/top/ulx3s_v20_apple2.vhd`](https://github.com/emard/apple2fpga/blob/0ad84ae2f9d9d5cc0e8db6128d630a9e16cdd6de/rtl_emard/lattice/top/ulx3s_v20_apple2.vhd))
- [emard__minimig_ecs](https://github.com/emard/Minimig_ECS) (instantiates [`rtl_emard/usb/usbhost/usbh_host.v`](https://github.com/emard/Minimig_ECS/blob/a0a94bfa0b8534f50be7b79086ad00a41184c266/rtl_emard/usb/usbhost/usbh_host.v))
- [emard__nes_ecp5](https://github.com/emard/nes_ecp5) (instantiates [`top.v`](https://github.com/emard/nes_ecp5/blob/fd421a13886cccc6da13be28a4a803a90b201e60/top.v))
- [emard__vhdl_phoenix](https://github.com/emard/vhdl_phoenix) (instantiates [`rtl_emard/usb/usbhost/usbh_host.v`](https://github.com/emard/vhdl_phoenix/blob/43f3b39cc87f71835844d200c83f3c7735eaec68/rtl_emard/usb/usbhost/usbh_host.v))
- [ironsteel__nes_ecp5](https://github.com/ironsteel/nes_ecp5) (instantiates [`top.v`](https://github.com/ironsteel/nes_ecp5/blob/ff331d4b9c422e0b792560dd7b2b67a28622f67f/top.v))
- [lawrie__ulx3s_examples](https://github.com/lawrie/ulx3s_examples) (instantiates [`usbemard/ulx3s_usbhost_test.v`](https://github.com/lawrie/ulx3s_examples/blob/b6ff00099265401fef4843e4e89c2ac54254c95f/usbemard/ulx3s_usbhost_test.v))
- [lawrie__ulx3s_zx_spectrum](https://github.com/lawrie/ulx3s_zx_spectrum) (instantiates [`src/spectrum.v`](https://github.com/lawrie/ulx3s_zx_spectrum/blob/19f242c057e25b38254004b1ea57306a28d85414/src/spectrum.v))
- [linuxjedi__minimig_ecs](https://github.com/LinuxJedi/Minimig_ECS) (instantiates [`rtl_emard/usb/usbhost/usbh_host.v`](https://github.com/LinuxJedi/Minimig_ECS/blob/a0a94bfa0b8534f50be7b79086ad00a41184c266/rtl_emard/usb/usbhost/usbh_host.v))
- [machdyne__nes_ecp5](https://github.com/machdyne/nes_ecp5) (instantiates [`top.v`](https://github.com/machdyne/nes_ecp5/blob/ff331d4b9c422e0b792560dd7b2b67a28622f67f/top.v))
- [ulx3s__apple2fpga](https://github.com/ulx3s/apple2fpga) (instantiates [`rtl_emard/usb/usbhost/usbh_sie_vhdl.vhd`](https://github.com/ulx3s/apple2fpga/blob/b19e79be5cbbbadd3f7a31708425da9bfcfed78f/rtl_emard/usb/usbhost/usbh_sie_vhdl.vhd))

### circuit-killer minimal USB HID host {#core-circuit-killer-usbhid-host}

Minimal single-file USB HID host state machine with CRC5/CRC16 helper functions, built for ULX3S 45F/85F (saitek/dragonrise-oled projects) with dedicated OLED demo tops.

| | |
|---|---|
| Repository | [circuit-killer__fpga-usbhid-host](https://github.com/Circuit-killer/fpga-usbhid-host): Minimal FPGA USB-HID host |
| Files | [`usbhid_host.vhd`](https://github.com/Circuit-killer/fpga-usbhid-host/blob/166e991b17db73b5a1158969ca7c8b9a4cecfb36/usbhid_host.vhd), [`usb_req_gen_func_pack.vhd`](https://github.com/Circuit-killer/fpga-usbhid-host/blob/166e991b17db73b5a1158969ca7c8b9a4cecfb36/usb_req_gen_func_pack.vhd) |
| Top module | `usbhid_host` |
| Language | VHDL |
| License | none found (no LICENSE/COPYING file) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | none found |

**On ULX3S:** No license file: get owner clearance before reuse.

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [emard__papilio-arcade](https://github.com/emard/Papilio-Arcade) (copies [`scramble_rel001_papilio/source/usbhid/usb_req_gen_func_pack.vhd`](https://github.com/emard/Papilio-Arcade/blob/4f91f938c200f1b0d80f03f835bdadcc5f21aa58/scramble_rel001_papilio/source/usbhid/usb_req_gen_func_pack.vhd))

### emard standalone USB1.1 host PHY/SIE (usb_host repo) {#core-emard-usb-host-soc}

Standalone USB1.1 host PHY + SIE + register block, packaged as its own small ULX3S 12F demo with a BRAM firmware loader (ucmem/), separate from the ulx3s-misc/nes_ecp5 usbh_sie lineage.

| | |
|---|---|
| Repository | [emard__usb_host](https://github.com/emard/usb_host): USB host core |
| Files | [`usb11/phy.v`](https://github.com/emard/usb_host/blob/47408bb4f69532118cea32f3c668a8637f77bb76/usb11/phy.v), [`usb11/sie.v`](https://github.com/emard/usb_host/blob/47408bb4f69532118cea32f3c668a8637f77bb76/usb11/sie.v), [`usb11/regs.v`](https://github.com/emard/usb_host/blob/47408bb4f69532118cea32f3c668a8637f77bb76/usb11/regs.v) |
| Top module | `SIE` |
| Language | Verilog |
| License | none found |
| FPGA / primitives | any: none (portable) |
| Tests | 1 tb file in ./tb (not confirmed self-checking) |

**On ULX3S:** Demo bitstream targets ULX3S 12F (soc/build.sh --12k).

### emard USB host + gamepad report decoders {#core-nes-ecp5-usb-gamepad}

Same usbh_sie host core as the ulx3s-misc copy, plus five ready HID report decoders for specific gamepads (NES-style, Saitek, Darfon, Xbox 360), the piece usually missing when reusing the bare host core.

| | |
|---|---|
| Repository | [emard__nes_ecp5](https://github.com/emard/nes_ecp5): NES (MiST core) on ULX3S: DVI, SDRAM, ESP32 OSD, USB gamepads |
| Files | [`usb/usbhost`](https://github.com/emard/nes_ecp5/tree/fd421a13886cccc6da13be28a4a803a90b201e60/usb/usbhost), [`usb/report_decoder`](https://github.com/emard/nes_ecp5/tree/fd421a13886cccc6da13be28a4a803a90b201e60/usb/report_decoder) |
| Top module | `usbh_sie` |
| Language | Verilog |
| License | GPL-2.0-or-later (same Ultra-Embedded usbh_sie.v core) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Use report_decoder/usbh_report_decoder_xbox360.v (or another pad's file) to parse usbh_host_hid's output into button state.

**Used by 4 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [cheyao__nes_ecp5](https://github.com/cheyao/nes_ecp5) (copies [`usb/report_decoder/usbh_report_decoder_saitek.v`](https://github.com/cheyao/nes_ecp5/blob/e8dd1eb7f9f440a552cd24c0b936e58705a272e7/usb/report_decoder/usbh_report_decoder_saitek.v))
- [ironsteel__nes_ecp5](https://github.com/ironsteel/nes_ecp5) (copies [`usb/report_decoder/usbh_report_decoder_saitek.v`](https://github.com/ironsteel/nes_ecp5/blob/ff331d4b9c422e0b792560dd7b2b67a28622f67f/usb/report_decoder/usbh_report_decoder_saitek.v))
- [lawrie__ulx3s_zx_spectrum](https://github.com/lawrie/ulx3s_zx_spectrum) (copies [`src/usb/report_decoder/usbh_report_decoder_saitek.v`](https://github.com/lawrie/ulx3s_zx_spectrum/blob/19f242c057e25b38254004b1ea57306a28d85414/src/usb/report_decoder/usbh_report_decoder_saitek.v))
- [machdyne__nes_ecp5](https://github.com/machdyne/nes_ecp5) (copies [`usb/report_decoder/usbh_report_decoder_saitek.v`](https://github.com/machdyne/nes_ecp5/blob/ff331d4b9c422e0b792560dd7b2b67a28622f67f/usb/report_decoder/usbh_report_decoder_saitek.v))

### hdl4fpga USB 1.1 host core {#core-hdl4fpga-usbhost}

Portable USB 1.1 host core, no vendor primitives, sharing a PHY with the device core (usbdev.vhd) via a build-time role switch; used on real ULX3S hardware in boards/ULX3S/apps/ser_debug.vhd.

| | |
|---|---|
| Repository | [hdl4fpga__hdl4fpga](https://github.com/hdl4fpga/hdl4fpga): hdl4fpga: portable VHDL library, ScopeIO oscilloscope, SDRAM graphics, eth/USB links |
| Files | [`library/usb/usbhost.vhd`](https://github.com/hdl4fpga/hdl4fpga/blob/662986ba0f17b7ce3a066ddcb799d42fa1b24dea/library/usb/usbhost.vhd), [`library/usb/usbphy.vhd`](https://github.com/hdl4fpga/hdl4fpga/blob/662986ba0f17b7ce3a066ddcb799d42fa1b24dea/library/usb/usbphy.vhd) |
| Top module | `usbhost` |
| Language | VHDL |
| License | MIT (LICENSE, Miguel Angel Sagreras) |
| FPGA / primitives | any: none (portable) |
| Tests | waveform tb in boards/ULX3S/testbenches |

**On ULX3S:** Set usb_device=false to select host mode in a ser_debug-style top.

Full review: [hdl4fpga__hdl4fpga](../projects/hdl4fpga__hdl4fpga.md).

**Used by 2 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [lawrie__spinalulx3s](https://github.com/lawrie/SpinalULX3S) (instantiates [`src/main/scala/mylib/UsbHidTest.scala`](https://github.com/lawrie/SpinalULX3S/blob/7cb99e7f62c7abdc9210790d2d934e7e197ae627/src/main/scala/mylib/UsbHidTest.scala))
- [spinalhdl__saxonsoc](https://github.com/SpinalHDL/SaxonSoc) (instantiates [`hardware/deprecated/ulx3s/peripheral/UsbHostHid.scala`](https://github.com/SpinalHDL/SaxonSoc/blob/227b8686b734c7995b10ce81e193a01b010d2407/hardware/deprecated/ulx3s/peripheral/UsbHostHid.scala))

## Other catalogued projects

Catalogued repos tagged `usb-host` (27) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
