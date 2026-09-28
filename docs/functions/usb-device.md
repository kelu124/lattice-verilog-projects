---
title: "USB device"
parent: "Cores by function"
nav_order: 15
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# USB device

USB full-speed device stacks and CDC-ACM serial on the US2 port.

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [no2usb-derived ECP5 USB FS device core (had2019 bootloader)](#core-emard-had2019-usb-device) ★ | [emard__had2019-playground](https://github.com/emard/had2019-playground) | Verilog | LGPL-3.0-or-later | ECP5 | 4 |
| [circuit-killer USB FS serial device (VHDL, ULX3S-built)](#core-circuit-killer-usbserial) | [circuit-killer__fpga-usbserial](https://github.com/Circuit-killer/fpga-usbserial) | VHDL | GPL-2.0 (usb_serial/COPYING) | ECP5 | 2 |
| [f32c USB CDC-ACM device + soft PHY](#core-f32c-usb-serial) | [f32c__f32c](https://github.com/f32c/f32c) | VHDL | BSD-2-Clause | any | 2 |
| [hdl4fpga USB 1.1 device core](#core-hdl4fpga-usbdev) | [hdl4fpga__hdl4fpga](https://github.com/hdl4fpga/hdl4fpga) | VHDL | MIT (LICENSE, Miguel Angel Sagreras) | any | 11 |
| [ulixxe USB CDC-ACM device core](#core-ulixxe-usb-cdc) | [ulixxe__usb_cdc](https://github.com/ulixxe/usb_cdc) | Verilog | MIT (LICENSE) | any | 2 |
| [ulx3s-misc USB CDC-ACM device (VHDL)](#core-ulx3s-misc-usbcdc) | [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc) | VHDL | GPL-2.0-or-later | any | 0 |

## Cores

### no2usb-derived ECP5 USB FS device core (had2019 bootloader) (best) {#core-emard-had2019-usb-device}

Early ECP5-ported snapshot of Sylvain Munaut's no2usb: full-speed USB device MAC/PHY (EP buffers, CRC, transaction engine) driving the US2 pins directly; the core shipped as the fielded ULX3S DFU bootloader's USB device.

| | |
|---|---|
| Repository | [emard__had2019-playground](https://github.com/emard/had2019-playground): HAD2019 badge playground |
| Files | [`cores/usb/rtl`](https://github.com/emard/had2019-playground/tree/0723f2a536b20f26ec1b2d5cf1dcc2b5355b6808/cores/usb/rtl) |
| Top module | `usb` |
| Language | Verilog |
| License | LGPL-3.0-or-later (LICENSE.lgpl3; header in cores/usb/rtl/usb.v) |
| FPGA / primitives | ECP5: `TRELLIS_IO`, `OFS1P3DX`, `IDDRX1F` |
| Tests | waveform-only (cores/usb/sim/*_tb.v via iverilog, never run to a pass/fail check) |

**On ULX3S:** Runs at 48 MHz from a 25->48MHz EHXPLLL (sysmgr.v); wire to usb_fpga_bd_dp/dn + usb_fpga_pu_dp on US2.

**Used by 4 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [icebreaker-fpga__icetwang](https://codeberg.org/icebreaker-fpga/icetwang) (instantiates [`soc/cores/no2usb/rtl/usb.v`](https://codeberg.org/icebreaker-fpga/icetwang/src/commit/a4915ff538be621d8cab4a9d82c555ee8627e0c3/soc/cores/no2usb/rtl/usb.v))
- [smunaut__ice40-playground](https://github.com/smunaut/ice40-playground) (instantiates [`cores/no2usb/rtl/usb.v`](https://github.com/smunaut/ice40-playground/blob/d2fa0050129c14a7fc42f64f115366f6f2a51669/cores/no2usb/rtl/usb.v))
- [spritetm__hadbadge2019_fpgasoc](https://github.com/Spritetm/hadbadge2019_fpgasoc) (instantiates [`soc/usb/usb.v`](https://github.com/Spritetm/hadbadge2019_fpgasoc/blob/6e706d52ecdc007e9179bda01d8eac60d55b7c45/soc/usb/usb.v))
- [ulx3s__hazard3-doom](https://github.com/ulx3s/Hazard3-Doom) (instantiates [`bootloader/cores/usb/rtl/usb.v`](https://github.com/ulx3s/Hazard3-Doom/blob/42621599f78f7ce3bd51fcc6b95a56ba83e31279/bootloader/cores/usb/rtl/usb.v))

### circuit-killer USB FS serial device (VHDL, ULX3S-built) {#core-circuit-killer-usbserial}

USB CDC-ACM device core with its own soft PHY (usb11_phy_vhdl, no vendor primitives) plus an optional ULPI wrapper; the repo ships ULX3S v2.0/v3.1.7 LPFs and 12F/25F/45F/85F build dirs.

| | |
|---|---|
| Repository | [circuit-killer__fpga-usbserial](https://github.com/Circuit-killer/fpga-usbserial): USB1.1 full-speed device-side USB-to-serial core |
| Files | [`usb_serial`](https://github.com/Circuit-killer/fpga-usbserial/tree/bc9e18e84df7025315bd08c71bc4d17b0b5b6a0b/usb_serial), [`usb11_phy_vhdl`](https://github.com/Circuit-killer/fpga-usbserial/tree/bc9e18e84df7025315bd08c71bc4d17b0b5b6a0b/usb11_phy_vhdl) |
| Top module | `usb_serial` |
| Language | VHDL |
| License | GPL-2.0 (usb_serial/COPYING) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | none found |

**On ULX3S:** Use usb11_phy_vhdl (direct US2 pins), not ulpi_wrapper (needs an external ULPI PHY chip).

**Used by 2 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc) (copies [`examples/usb/usbcdc/usb_control.vhd`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/usb/usbcdc/usb_control.vhd))
- [f32c__f32c](https://github.com/f32c/f32c) (copies [`rtl/soc/usb_serial/usb_control.vhd`](https://github.com/f32c/f32c/blob/7dbf56d42a94ae599eabfd1e7fa15db14a10afd7/rtl/soc/usb_serial/usb_control.vhd))

### f32c USB CDC-ACM device + soft PHY {#core-f32c-usb-serial}

USB 2.0 CDC-ACM device entity (usb_serial.vhd) over a UTMI-style soft PHY (usb11_phy, ported from Verilog), wired into f32c SoCs proven across ULX3S 12F-85F.

| | |
|---|---|
| Repository | [f32c__f32c](https://github.com/f32c/f32c): f32c: retargetable RISC-V/MIPS 32-bit soft CPU + SoC library |
| Files | [`rtl/soc/usb_serial`](https://github.com/f32c/f32c/tree/7dbf56d42a94ae599eabfd1e7fa15db14a10afd7/rtl/soc/usb_serial), [`rtl/soc/usb11_phy`](https://github.com/f32c/f32c/tree/7dbf56d42a94ae599eabfd1e7fa15db14a10afd7/rtl/soc/usb11_phy) |
| Top module | `usb_serial` |
| Language | VHDL |
| License | BSD-2-Clause (repo fallback, no per-file header on usb_serial.vhd); usb11_phy is OpenCores-permissive (Copyright 2000-2002 Rudolf Usselmann) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Same core family as emard__ulx3s-misc/examples/usb/usbcdc; check docs/projects/f32c__f32c.md before reuse (license per-file uncertainty).

Full review: [f32c__f32c](../projects/f32c__f32c.md).

**Used by 2 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [circuit-killer__fpga-usbserial](https://github.com/Circuit-killer/fpga-usbserial) (copies [`usb_serial/usb_transact.vhd`](https://github.com/Circuit-killer/fpga-usbserial/blob/bc9e18e84df7025315bd08c71bc4d17b0b5b6a0b/usb_serial/usb_transact.vhd))
- [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc) (copies [`examples/usb/usbcdc/usb_transact.vhd`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/usb/usbcdc/usb_transact.vhd))

### hdl4fpga USB 1.1 device core {#core-hdl4fpga-usbdev}

Portable USB 1.1 device core with no vendor primitives, switchable device/host role via a build constant; used on real ULX3S hardware by boards/ULX3S/apps/ser_debug.vhd on the US2 pins.

| | |
|---|---|
| Repository | [hdl4fpga__hdl4fpga](https://github.com/hdl4fpga/hdl4fpga): hdl4fpga: portable VHDL library, ScopeIO oscilloscope, SDRAM graphics, eth/USB links |
| Files | [`library/usb/usbdev.vhd`](https://github.com/hdl4fpga/hdl4fpga/blob/662986ba0f17b7ce3a066ddcb799d42fa1b24dea/library/usb/usbdev.vhd), [`library/usb/usbphy.vhd`](https://github.com/hdl4fpga/hdl4fpga/blob/662986ba0f17b7ce3a066ddcb799d42fa1b24dea/library/usb/usbphy.vhd) |
| Top module | `usbdev` |
| Language | VHDL |
| License | MIT (LICENSE, Miguel Angel Sagreras) |
| FPGA / primitives | any: none (portable) |
| Tests | waveform tb in boards/ULX3S/testbenches (12 tb files across boards, not all self-checking) |

**On ULX3S:** Set the usb_device constant true in a ser_debug.vhd-style top; needs the matching usbphy.vhd PHY.

Full review: [hdl4fpga__hdl4fpga](../projects/hdl4fpga__hdl4fpga.md).

**Used by 11 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [antoinevg__cynthion-tutorials](https://github.com/antoinevg/cynthion-tutorials) (instantiates [`examples/soc/top.py`](https://github.com/antoinevg/cynthion-tutorials/blob/8b711adb4c1c1495f7bd815239b52e1d789d4d91/examples/soc/top.py))
- [apfaudio__guh](https://github.com/apfaudio/guh) (instantiates [`guh/util/test_devices.py`](https://github.com/apfaudio/guh/blob/9aa0fd3511490674bdd038760abc8729f9e0b023/guh/util/test_devices.py))
- [greatscottgadgets__cynthion](https://github.com/greatscottgadgets/cynthion) (instantiates [`cynthion/python/examples/tutorials/gateware-usb-device-01.py`](https://github.com/greatscottgadgets/cynthion/blob/dd2340e20de66341b73c6276cf1654800b655db2/cynthion/python/examples/tutorials/gateware-usb-device-01.py))
- [greatscottgadgets__cynthion-uac](https://github.com/greatscottgadgets/cynthion-uac) (instantiates [`uac/uac2.py`](https://github.com/greatscottgadgets/cynthion-uac/blob/0dfc4186182b6c9c2bbaa9199f88a6d196306a7d/uac/uac2.py))
- [greatscottgadgets__luna](https://github.com/greatscottgadgets/luna) (instantiates [`applets/clear_endpoint_halt_test.py`](https://github.com/greatscottgadgets/luna/blob/82a8f733296603b70ba56755206e13092609c6f0/applets/clear_endpoint_halt_test.py))
- [lawrie__ulx3s_examples](https://github.com/lawrie/ulx3s_examples) (instantiates [`usbhost/usbh_host_hid.v`](https://github.com/lawrie/ulx3s_examples/blob/b6ff00099265401fef4843e4e89c2ac54254c95f/usbhost/usbh_host_hid.v))
- [orangecrab-fpga__orangecrab-examples](https://github.com/orangecrab-fpga/orangecrab-examples) (instantiates [`litex/deps/valentyusb/sim/test-cdc-eptri.py`](https://github.com/orangecrab-fpga/orangecrab-examples/blob/eefbafa8729e7807fb64357c306a635a40fa8b34/litex/deps/valentyusb/sim/test-cdc-eptri.py))
- [orbcode__orbtrace](https://github.com/orbcode/orbtrace) (instantiates [`orbtrace/amaranth_glue/luna.py`](https://github.com/orbcode/orbtrace/blob/e416cd5b074fc725a04cf6b877d458e2074467ae/orbtrace/amaranth_glue/luna.py))
- [spinalhdl__saxonsoc](https://github.com/SpinalHDL/SaxonSoc) (instantiates [`hardware/scala/saxon/board/digilent/ArtyA7SmpLinux.scala`](https://github.com/SpinalHDL/SaxonSoc/blob/227b8686b734c7995b10ce81e193a01b010d2407/hardware/scala/saxon/board/digilent/ArtyA7SmpLinux.scala))
- [voltcyclone__hurra-fpga](https://github.com/VoltCyclone/hurra-fpga) (instantiates [`src/hurra_cynthion/device.py`](https://github.com/VoltCyclone/hurra-fpga/blob/0a050ad254eb27b43a00e61efe953cd842fcd27f/src/hurra_cynthion/device.py))
- [voltcyclone__hurricanefpga](https://github.com/VoltCyclone/HurricaneFPGA) (instantiates [`legacy/src/backend/usb_serial.py`](https://github.com/VoltCyclone/HurricaneFPGA/blob/6f0b109cf0ab1ad77ee7670693e3d1a6aa11cab5/legacy/src/backend/usb_serial.py))

### ulixxe USB CDC-ACM device core {#core-ulixxe-usb-cdc}

Self-contained full-speed USB CDC-ACM device (SIE, control/bulk endpoints, PHY rx/tx) with no BRAM/vendor primitives, shipped with pin files for 21 boards (Fomu, TinyFPGA-BX, iCEBreaker...).

| | |
|---|---|
| Repository | [ulixxe__usb_cdc](https://github.com/ulixxe/usb_cdc): Fomu / TinyFPGA-BX: USB_CDC, a from-scratch Full-Speed |
| Files | [`usb_cdc`](https://github.com/ulixxe/usb_cdc/tree/6798bf42d43be81368d4e5e2c26b262b41e9fb6a/usb_cdc) |
| Top module | `usb_cdc` |
| Language | Verilog |
| License | MIT (LICENSE) |
| FPGA / primitives | any: none (portable) |
| Tests | self-checking: examples/{TinyFPGA-BX,Fomu}/.../tb_demo.v uses assert_error macros (iverilog) |

**On ULX3S:** No ULX3S pin file yet; add one for usb_fpga_bd_dp/dn + pull-up, following an existing board example.

Full review: [ulixxe__usb_cdc](../projects/ulixxe__usb_cdc.md).

**Used by 2 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [machdyne__zeitlos](https://github.com/machdyne/zeitlos) (instantiates [`rtl/csrs.vh`](https://github.com/machdyne/zeitlos/blob/a7e7e85ee0ad1fd0cfff4129e24b2aa528d444e8/rtl/csrs.vh))
- [mb-sat__ulx3s-longwave-sdr](https://github.com/mb-sat/ulx3s-longwave-sdr) (instantiates [`logic/ulx3s-stream-verilog/ulx3s.v`](https://github.com/mb-sat/ulx3s-longwave-sdr/blob/1c2609dd20997b93c40331148adf972b99e33265/logic/ulx3s-stream-verilog/ulx3s.v))

### ulx3s-misc USB CDC-ACM device (VHDL) {#core-ulx3s-misc-usbcdc}

Same usb_serial.vhd device entity family as f32c, packaged as a standalone ULX3S example with a Windows .inf driver file; this copy documents itself as GPL, unlike the BSD-2 fallback claimed for the f32c copy.

| | |
|---|---|
| Repository | [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc): ULX3S misc/advanced examples: EMARD's building-block library |
| Files | [`examples/usb/usbcdc`](https://github.com/emard/ulx3s-misc/tree/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/usb/usbcdc) |
| Top module | `usb_serial` |
| Language | VHDL |
| License | GPL-2.0-or-later (examples/usb/usbcdc/README.txt) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** examples/usb/usbcdc/usbtest.vhd is the ready-to-build ULX3S top.

Full review: [emard__ulx3s-misc](../projects/emard__ulx3s-misc.md).

## Other catalogued projects

Catalogued repos tagged `usb-device` (31) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
