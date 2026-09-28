---
title: "Bootloaders and DFU"
parent: "Cores by function"
nav_order: 17
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# Bootloaders and DFU

USB DFU and other FPGA bootloaders, multiboot.

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [ULX3S/ULX4M USB DFU bootloader (had2019-playground)](#core-had2019-dfu-bootloader) ★ | [emard__had2019-playground](https://github.com/emard/had2019-playground) | Verilog, C | per file: bootloader RTL BSD-3-Clause, USB core +… | ECP5 | 0 |
| [Hazard3-Doom vendored DFU bootloader (ULX4M-LD validated)](#core-hazard3-doom-dfu-bootloader) | [ulx3s__hazard3-doom](https://github.com/ulx3s/Hazard3-Doom) | Verilog, C | provenance in… | ECP5 | 0 |
| [no2usb DFU runtime + dfu_helper.v (iCE40)](#core-no2usb-dfu-helper) | [smunaut__ice40-playground](https://github.com/smunaut/ice40-playground) | Verilog | mixed CERN-OHL-P-2.0/LGPL-3.0-or-later/MIT per… | iCE40 | 3 |

## Cores

### ULX3S/ULX4M USB DFU bootloader (had2019-playground) (best) {#core-had2019-dfu-bootloader}

The gateware ULX3S/ULX4M ship from flash address 0: PicoRV32 + no2usb-derived USB device core enumerating as DFU 1d50:614b, writing the user bitstream to flash 0x200000 via a QSPI master, with a 6-zone alt-setting layout. Fully documented in docs/DFUs.md.

| | |
|---|---|
| Repository | [emard__had2019-playground](https://github.com/emard/had2019-playground): HAD2019 badge playground |
| Files | [`projects/bootloader/rtl`](https://github.com/emard/had2019-playground/tree/0723f2a536b20f26ec1b2d5cf1dcc2b5355b6808/projects/bootloader/rtl), [`projects/bootloader/fw`](https://github.com/emard/had2019-playground/tree/0723f2a536b20f26ec1b2d5cf1dcc2b5355b6808/projects/bootloader/fw), [`cores/usb/rtl`](https://github.com/emard/had2019-playground/tree/0723f2a536b20f26ec1b2d5cf1dcc2b5355b6808/cores/usb/rtl) |
| Top module | `top` |
| Language | Verilog, C |
| License | per file: bootloader RTL BSD-3-Clause, USB core + DFU firmware LGPL-3.0-or-later, picorv32.v ISC (see docs/DFUs.md) |
| FPGA / primitives | ECP5: `TRELLIS_IO`, `OFS1P3DX`, `IDDRX1F`, `USRMCLK` |
| Tests | none found (cores/usb/sim + project tbs are waveform-only, never run to a pass/fail check) |

**On ULX3S:** USER_BITSTREAM_ADDR, dfu_zones[0] (fw/usb_dfu.c) and ecpmulti --address must all agree; PROGRAMN (LPF site M4) must loop back for hand-off.

### Hazard3-Doom vendored DFU bootloader (ULX4M-LD validated) {#core-hazard3-doom-dfu-bootloader}

Self-contained fork of the had2019 bootloader (own mk/, cores/, no external Makefile deps), remapped buttons, validated on real ULX4M-LD v0.0.3 (LFE5UM-85F) hardware, with a byte-for-byte readback recovery procedure documented in README_ULX4M_BOOTLOADER.md.

| | |
|---|---|
| Repository | [ulx3s__hazard3-doom](https://github.com/ulx3s/Hazard3-Doom): ulx3s/Hazard3-Doom: Doom |
| Files | [`bootloader/rtl`](https://github.com/ulx3s/Hazard3-Doom/tree/42621599f78f7ce3bd51fcc6b95a56ba83e31279/bootloader/rtl), [`bootloader/fw`](https://github.com/ulx3s/Hazard3-Doom/tree/42621599f78f7ce3bd51fcc6b95a56ba83e31279/bootloader/fw), [`bootloader/cores`](https://github.com/ulx3s/Hazard3-Doom/tree/42621599f78f7ce3bd51fcc6b95a56ba83e31279/bootloader/cores) |
| Top module | `top` |
| Language | Verilog, C |
| License | provenance in LICENSES/HAD2019-Bootloader-NOTICE.md; per-file licenses match the emard original (BSD-3/LGPL-3.0+/ISC) |
| FPGA / primitives | ECP5: `TRELLIS_IO`, `OFS1P3DX`, `IDDRX1F`, `USRMCLK` |
| Tests | none found (same iverilog-compile-only sim rule as the original) |

**On ULX3S:** Prefer this copy over the emard original for a self-contained tree; same USER_BITSTREAM_ADDR/dfu_zones agreement rule applies.

### no2usb DFU runtime + dfu_helper.v (iCE40) {#core-no2usb-dfu-helper}

Button debouncer that reboots into the no2bootloader DFU image via SB_WARMBOOT (long press) or resets the app (short press); the DFU class firmware itself (usb_dfu.c/usb_dfu_rt.c) lives in the fetched no2usb submodule.

| | |
|---|---|
| Repository | [smunaut__ice40-playground](https://github.com/smunaut/ice40-playground): iCEBreaker: collection of iCE40 UP5K IP cores |
| Files | [`projects/riscv_usb/rtl/dfu_helper.v`](https://github.com/smunaut/ice40-playground/blob/d2fa0050129c14a7fc42f64f115366f6f2a51669/projects/riscv_usb/rtl/dfu_helper.v) |
| Top module | `dfu_helper` |
| Language | Verilog |
| License | mixed CERN-OHL-P-2.0/LGPL-3.0-or-later/MIT per file (doc/LICENSE-*.txt) |
| FPGA / primitives | iCE40: `SB_WARMBOOT` |
| Tests | none found for dfu_helper.v itself |

**On ULX3S:** iCE40-only (SB_WARMBOOT multiboot); porting to ECP5 needs a different warm-boot mechanism plus the no2bootloader project, which is not in this collection.

Full review: [smunaut__ice40-playground](../projects/smunaut__ice40-playground.md).

**Used by 3 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [icebreaker-fpga__icebreaker-verilog-examples](https://codeberg.org/icebreaker-fpga/icebreaker-verilog-examples) (instantiates [`icebitsy/blink_count_shift/blink_count_shift.v`](https://codeberg.org/icebreaker-fpga/icebreaker-verilog-examples/src/commit/8d0892bf62dd5d8ae59c48c882d9ebebd1cab9c2/icebitsy/blink_count_shift/blink_count_shift.v))
- [icebreaker-fpga__icetwang](https://codeberg.org/icebreaker-fpga/icetwang) (instantiates [`soc/ice-twang/rtl/top.v`](https://codeberg.org/icebreaker-fpga/icetwang/src/commit/a4915ff538be621d8cab4a9d82c555ee8627e0c3/soc/ice-twang/rtl/top.v))
- [osmocom__osmo-e1-hardware](https://github.com/osmocom/osmo-e1-hardware) (instantiates [`gateware/e1-tracer/rtl/misc.v`](https://github.com/osmocom/osmo-e1-hardware/blob/85acea8b6d656add7c098d51f816f4ac34084fa2/gateware/e1-tracer/rtl/misc.v))

## Other catalogued projects

Catalogued repos tagged `bootloader` (31) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
