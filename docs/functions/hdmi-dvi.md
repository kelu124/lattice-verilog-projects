---
title: "HDMI / DVI output"
parent: "Cores by function"
nav_order: 1
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# HDMI / DVI output

TMDS encoders, serializers and DVI/HDMI transmitters (with or without audio), for the GPDI port.

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [vga2dvid + tmds_encoder DVI/TMDS core (Mike Field / EMARD)](#core-emard-vga2dvid-tmds) ★ | [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc) | VHDL, Verilog | MIT (vga2dvid.vhd, tmds_encoder.vhd headers,… | ECP5 | 103 |
| [hdl4fpga TMDS encoder (video component library)](#core-hdl4fpga-tmds-encoder) | [hdl4fpga__hdl4fpga](https://github.com/hdl4fpga/hdl4fpga) | VHDL | MIT (LICENSE; file header confirms same… | any | 0 |
| [HDMI TX with audio (danodus ecp5_hdmi_audio_video)](#core-danodus-hdmi-audio) | [danodus__ecp5_hdmi_audio_video](https://github.com/danodus/ecp5_hdmi_audio_video) | Verilog | MIT (LICENSE, Copyright 2026 Daniel Cliche / 2019… | ECP5 | 0 |
| [my_hdmi_device TMDS encoder + video timing (chip_balls)](#core-splinedrive-hdmi-device) | [splinedrive__my_hdmi_device](https://github.com/splinedrive/my_hdmi_device) | Verilog | ISC (LICENSE.md, Copyright 2021 Hirosh Dabui) | ECP5 | 4 |
| [smoldvi small portable DVI core](#core-smoldvi-dvi) | [wren6991__smoldvi](https://github.com/Wren6991/SmolDVI) | Verilog | CC0-1.0 (LICENSE.md) | any | 4 |
| [sound2fft TMDS encoder + ECP5 DVI serializer](#core-mebner86-tmds-serializer) | [mebner86__icesugar-pro_sound2fft](https://github.com/mebner86/icesugar-pro_sound2fft) | Verilog | MIT (LICENSE, root) | ECP5 | 0 |

## Cores

### vga2dvid + tmds_encoder DVI/TMDS core (Mike Field / EMARD) (best) {#core-emard-vga2dvid-tmds}

Converts VGA-style RGB+HV+blank into 8b/10b TMDS-encoded DDR/SDR bitstreams for the GPDI port; fake_differential wraps ECP5 ODDRX1F for the 4 pseudo-differential pairs. Copied into dozens of repos in this collection.

| | |
|---|---|
| Repository | [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc): ULX3S misc/advanced examples: EMARD's building-block library |
| Files | [`examples/dvi/hdl/vga2dvid.vhd`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/dvi/hdl/vga2dvid.vhd), [`examples/dvi/hdl/tmds_encoder.vhd`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/dvi/hdl/tmds_encoder.vhd), [`examples/dvi/hdl/fake_differential.v`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/dvi/hdl/fake_differential.v) |
| Top module | `vga2dvid` |
| Language | VHDL, Verilog |
| License | MIT (vga2dvid.vhd, tmds_encoder.vhd headers, Copyright 2012 Mike Field); fake_differential.v BSD-style (EMARD, no repo LICENSE file) |
| FPGA / primitives | ECP5: `ODDRX1F` |
| Tests | none found (top/top_vgatest.v is a synthesis smoke test, not self-checking) |

**On ULX3S:** Drop-in for GPDI: instantiate vga2dvid with fake_differential(C_ddr=1) at 25 MHz pixel clock x5 shift clock.

Full review: [emard__ulx3s-misc](../projects/emard__ulx3s-misc.md).

**Used by 103 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [adrmcintyre__vixen](https://github.com/adrmcintyre/vixen) (instantiates [`video/hdmi_video.v`](https://github.com/adrmcintyre/vixen/blob/e2db4fda79d2e73a7a595ce1773de64203346c0b/video/hdmi_video.v))
- [advikbahadur__ulx3s-superresolution-cnn](https://github.com/ADVIKBAHADUR/ULX3s-Superresolution-CNN) (instantiates [`src/hdmi_device.v`](https://github.com/ADVIKBAHADUR/ULX3s-Superresolution-CNN/blob/7979af367cc20e4393071c718ab0e04dae12ad86/src/hdmi_device.v))
- [alangarf__apple-one](https://github.com/alangarf/apple-one) (instantiates [`rtl/boards/icepi_zero/vga2tmds.sv`](https://github.com/alangarf/apple-one/blob/0f15ef6d62c2f8820aa5a68b7f973eef4a78dd8d/rtl/boards/icepi_zero/vga2tmds.sv))
- [angelojacobo__ulx3s_fpga_camera_streaming](https://github.com/AngeloJacobo/ULX3S_FPGA_Camera_Streaming) (instantiates [`src/hdmi_device.v`](https://github.com/AngeloJacobo/ULX3S_FPGA_Camera_Streaming/blob/ba9b3d836a548b30f4f52cfe46123ae57beefe33/src/hdmi_device.v))
- [angelojacobo__ulx3s_fpga_sobel_edge_detection_ov7670](https://github.com/AngeloJacobo/ULX3S_FPGA_Sobel_Edge_Detection_OV7670) (instantiates [`src/hdmi_device.v`](https://github.com/AngeloJacobo/ULX3S_FPGA_Sobel_Edge_Detection_OV7670/blob/693dacba2f8450417d9944f1803255a44c842042/src/hdmi_device.v))
- [brunolevy__learn-fpga](https://github.com/BrunoLevy/learn-fpga) (instantiates [`Basic/ULX3S/ULX3S_SDRAM_hdmi/SDRAM_HDMI_test.v`](https://github.com/BrunoLevy/learn-fpga/blob/5c08c870315c09ccd9ec64ccde20ab3375b3f273/Basic/ULX3S/ULX3S_SDRAM_hdmi/SDRAM_HDMI_test.v))
- [cheyao__icepi-zero](https://github.com/cheyao/icepi-zero) (instantiates [`gateware/dvi/hdl/vga2tmds.sv`](https://github.com/cheyao/icepi-zero/blob/e01faa2bd35dcb7269827f8420b845d46c78c869/gateware/dvi/hdl/vga2tmds.sv))
- [cheyao__nes_ecp5](https://github.com/cheyao/nes_ecp5) (instantiates [`top.v`](https://github.com/cheyao/nes_ecp5/blob/e8dd1eb7f9f440a552cd24c0b936e58705a272e7/top.v))
- [cheyao__oberon](https://github.com/cheyao/oberon) (instantiates [`hdl/dvi/vga2dvid.v`](https://github.com/cheyao/oberon/blob/07511b33357a95d68db67fc9351c86a13d106ecf/hdl/dvi/vga2dvid.v))
- [cheyao__sega-sms](https://github.com/cheyao/sega-sms) (instantiates [`src/hdmi.v`](https://github.com/cheyao/sega-sms/blob/c37e846d94f88eb9a95f44b15f2b23019aa25a26/src/hdmi.v))
- [chriscamacho__yazsof](https://github.com/chriscamacho/YAZSOF) (instantiates [`video/dvi.v`](https://github.com/chriscamacho/YAZSOF/blob/3a8ff5dcf25dcf149683adf109ac3096caa0a786/video/dvi.v))
- [dan-rodrigues__icestation-32](https://github.com/dan-rodrigues/icestation-32) (instantiates [`hardware/ulx3s/hdmi_encoder.v`](https://github.com/dan-rodrigues/icestation-32/blob/55214d79f74a547dedb54f99cb2fad431b7ac277/hardware/ulx3s/hdmi_encoder.v))
- [danodus__msx_fpga](https://github.com/danodus/msx_fpga) (instantiates [`src/msx.v`](https://github.com/danodus/msx_fpga/blob/f3266f78762094ab3eb5621279011efb504c69df/src/msx.v))
- [danodus__ulx3s_68k](https://github.com/danodus/ulx3s_68k) (instantiates [`src/hdmi.v`](https://github.com/danodus/ulx3s_68k/blob/ee10339210d0c302143745d3cc584a21a4878ace/src/hdmi.v))
- [danodus__ulx3s_sms](https://github.com/danodus/ulx3s_sms) (instantiates [`src/hdmi.v`](https://github.com/danodus/ulx3s_sms/blob/13c2361a5039d205de47857bab9201055ac9e566/src/hdmi.v))
- … and 88 more (see `data/core_usage.json`)

### hdl4fpga TMDS encoder (video component library) {#core-hdl4fpga-tmds-encoder}

Reusable TMDS 8b/10b encoder entity from the hdl4fpga component library; encoder logic only, no serializer, meant to be paired with a board PHY (hdl4fpga ships ECP5 PHY files elsewhere in library/).

| | |
|---|---|
| Repository | [hdl4fpga__hdl4fpga](https://github.com/hdl4fpga/hdl4fpga): hdl4fpga: portable VHDL library, ScopeIO oscilloscope, SDRAM graphics, eth/USB links |
| Files | [`library/video/tmds_encoder.vhd`](https://github.com/hdl4fpga/hdl4fpga/blob/662986ba0f17b7ce3a066ddcb799d42fa1b24dea/library/video/tmds_encoder.vhd) |
| Top module | `tmds_encoder` |
| Language | VHDL |
| License | MIT (LICENSE; file header confirms same permissive terms, Copyright 2015 Miguel Angel Sagreras) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Pair with an ECP5 ODDRX1F/ODDRX2F serializer to drive GPDI; VHDL-only, hdl4fpga's own build scripts assume Diamond but the entity itself is toolchain-neutral.

Full review: [hdl4fpga__hdl4fpga](../projects/hdl4fpga__hdl4fpga.md).

### HDMI TX with audio (danodus ecp5_hdmi_audio_video) {#core-danodus-hdmi-audio}

Full HDMI TX stack with audio and info-frame packet insertion (clock regeneration, AVI/audio packets); ULX3S top-level wiring already provided in boards/ulx3s/.

| | |
|---|---|
| Repository | [danodus__ecp5_hdmi_audio_video](https://github.com/danodus/ecp5_hdmi_audio_video): ULX3S/IcePi Zero: HDMI audio+video transmitter core |
| Files | [`rtl/hdmi.v`](https://github.com/danodus/ecp5_hdmi_audio_video/blob/a4710f9e7986fe9aafde765b8b3f264ca61631be/rtl/hdmi.v), [`rtl/hdmi_tmds_channel.v`](https://github.com/danodus/ecp5_hdmi_audio_video/blob/a4710f9e7986fe9aafde765b8b3f264ca61631be/rtl/hdmi_tmds_channel.v), [`rtl/hdmi_serializer_ecp5.v`](https://github.com/danodus/ecp5_hdmi_audio_video/blob/a4710f9e7986fe9aafde765b8b3f264ca61631be/rtl/hdmi_serializer_ecp5.v), [`boards/ulx3s/ulx3s_top.v`](https://github.com/danodus/ecp5_hdmi_audio_video/blob/a4710f9e7986fe9aafde765b8b3f264ca61631be/boards/ulx3s/ulx3s_top.v) |
| Top module | `hdmi` |
| Language | Verilog |
| License | MIT (LICENSE, Copyright 2026 Daniel Cliche / 2019 Sameer Puri) |
| FPGA / primitives | ECP5: `ODDRX1F` |
| Tests | none found |

**On ULX3S:** boards/ulx3s/ulx3s_top.v + hdmi_pll*.v are ready-made for GPDI; pick the hdmi_pll variant matching your target resolution.

Full review: [danodus__ecp5_hdmi_audio_video](../projects/danodus__ecp5_hdmi_audio_video.md).

### my_hdmi_device TMDS encoder + video timing (chip_balls) {#core-splinedrive-hdmi-device}

hdmi_device.v does 8b/10b TMDS encoding from an incoming VGA-style RGB+sync stream; chip_balls.v wires it to ECP5 ODDRX1F for GPDI output. Builds against ulx3s_v20.lpf at --85k.

| | |
|---|---|
| Repository | [splinedrive__my_hdmi_device](https://github.com/splinedrive/my_hdmi_device): my_hdmi_device: from-spec TMDS/HDMI encoder, multi-board |
| Files | [`tmds_encoder.v`](https://github.com/splinedrive/my_hdmi_device/blob/16a93372a9e07d27b23cf093a649dc870c208851/tmds_encoder.v), [`hdmi_device.v`](https://github.com/splinedrive/my_hdmi_device/blob/16a93372a9e07d27b23cf093a649dc870c208851/hdmi_device.v), [`video_timings.v`](https://github.com/splinedrive/my_hdmi_device/blob/16a93372a9e07d27b23cf093a649dc870c208851/video_timings.v), [`chip_balls.v`](https://github.com/splinedrive/my_hdmi_device/blob/16a93372a9e07d27b23cf093a649dc870c208851/chip_balls.v) |
| Top module | `chip_balls` |
| Language | Verilog |
| License | ISC (LICENSE.md, Copyright 2021 Hirosh Dabui) |
| FPGA / primitives | ECP5: `ODDRX1F` |
| Tests | none found |

**On ULX3S:** Already has a ulx3s_v20.lpf and Makefile target (PROJ=chip_balls, --85k, CABGA381); pair with ecp5pll.sv (also in this repo) for the pixel/shift clocks.

**Used by 4 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [advikbahadur__ulx3s-superresolution-cnn](https://github.com/ADVIKBAHADUR/ULX3s-Superresolution-CNN) (instantiates [`src/vga_interface.v`](https://github.com/ADVIKBAHADUR/ULX3s-Superresolution-CNN/blob/7979af367cc20e4393071c718ab0e04dae12ad86/src/vga_interface.v))
- [angelojacobo__ulx3s_fpga_camera_streaming](https://github.com/AngeloJacobo/ULX3S_FPGA_Camera_Streaming) (instantiates [`src/vga_interface.v`](https://github.com/AngeloJacobo/ULX3S_FPGA_Camera_Streaming/blob/ba9b3d836a548b30f4f52cfe46123ae57beefe33/src/vga_interface.v))
- [angelojacobo__ulx3s_fpga_sobel_edge_detection_ov7670](https://github.com/AngeloJacobo/ULX3S_FPGA_Sobel_Edge_Detection_OV7670) (instantiates [`src/vga_interface.v`](https://github.com/AngeloJacobo/ULX3S_FPGA_Sobel_Edge_Detection_OV7670/blob/693dacba2f8450417d9944f1803255a44c842042/src/vga_interface.v))
- [msrraju07__iop](https://github.com/MSRRaju07/IOP) (instantiates [`src/vga_interface.v`](https://github.com/MSRRaju07/IOP/blob/693dacba2f8450417d9944f1803255a44c842042/src/vga_interface.v))

### smoldvi small portable DVI core {#core-smoldvi-dvi}

Minimal DVI TX (~20 LUTs/lane TMDS encoder); timing/encode/gearbox logic is vendor-neutral per the author, only the final serialiser targets a specific FPGA's DDR output primitive.

| | |
|---|---|
| Repository | [wren6991__smoldvi](https://github.com/Wren6991/SmolDVI): iCEBreaker/iCEstick/iCESugar/TinyFPGA-BX: SmolDVI, a small direct DVI/TMDS output core |
| Files | [`hdl/smoldvi/smoldvi.v`](https://github.com/Wren6991/SmolDVI/blob/e8b8f875795f619a184a47f95c8c83a201479dc5/hdl/smoldvi/smoldvi.v), [`hdl/smoldvi/smoldvi_tmds_encode.v`](https://github.com/Wren6991/SmolDVI/blob/e8b8f875795f619a184a47f95c8c83a201479dc5/hdl/smoldvi/smoldvi_tmds_encode.v), [`hdl/smoldvi/smoldvi_timing.v`](https://github.com/Wren6991/SmolDVI/blob/e8b8f875795f619a184a47f95c8c83a201479dc5/hdl/smoldvi/smoldvi_timing.v), [`hdl/smoldvi/smoldvi_serialiser.v`](https://github.com/Wren6991/SmolDVI/blob/e8b8f875795f619a184a47f95c8c83a201479dc5/hdl/smoldvi/smoldvi_serialiser.v) |
| Top module | `smoldvi` |
| Language | Verilog |
| License | CC0-1.0 (LICENSE.md) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Port smoldvi_serialiser.v/smoldvi_clock_driver.v from iCE40 SB_IO to ECP5 ODDRX2F/ECLKSYNCB; the rest is drop-in.

Full review: [wren6991__smoldvi](../projects/wren6991__smoldvi.md).

**Used by 4 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [rj45__vdp](https://github.com/rj45/vdp) (instantiates [`rtl/smoldvi.v`](https://github.com/rj45/vdp/blob/291d6f11fd68d8dce9a1b6d4ebd56c4eb3b6531f/rtl/smoldvi.v))
- [ulx3s__hazard3](https://github.com/ulx3s/Hazard3) (instantiates [`example_soc/libfpga/video/dvi_tx_parallel.v`](https://github.com/ulx3s/Hazard3/blob/3c0aca063517bb7fdbe869019c984954c7dd5c97/example_soc/libfpga/video/dvi_tx_parallel.v))
- [wren6991__hazard3-swd-soc](https://github.com/Wren6991/Hazard3-SWD-SoC) (instantiates [`lib/libfpga/video/dvi_tx_parallel.v`](https://github.com/Wren6991/Hazard3-SWD-SoC/blob/6f3bfe190a9dd20185913ec8e97bd2eaea75a788/lib/libfpga/video/dvi_tx_parallel.v))
- [wren6991__riscboy](https://github.com/Wren6991/RISCBoy) (instantiates [`hdl/libfpga/video/dvi_tx_parallel.v`](https://github.com/Wren6991/RISCBoy/blob/25f8bb6eaebee6ace509cecc9b3891f43fae5bf6/hdl/libfpga/video/dvi_tx_parallel.v))

### sound2fft TMDS encoder + ECP5 DVI serializer {#core-mebner86-tmds-serializer}

8b/10b TMDS encoder plus an ECP5 ODDRX1F-based DVI serializer, part of a larger FFT+PDM-mic+HDMI pipeline built for an ECP5 25F board (iCEsugar-Pro).

| | |
|---|---|
| Repository | [mebner86__icesugar-pro_sound2fft](https://github.com/mebner86/icesugar-pro_sound2fft): iCESugar-Pro sound2fft: real-time audio spectrum analyzer |
| Files | [`rtl/tmds_encoder.v`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/rtl/tmds_encoder.v), [`rtl/tmds_serializer.v`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/rtl/tmds_serializer.v) |
| Top module | `tmds_serializer` |
| Language | Verilog |
| License | MIT (LICENSE, root) |
| FPGA / primitives | ECP5: `ODDRX1F` |
| Tests | waveform-only tb: projects/02_hdmi_test/hdmi_test_tb.v (no PASS/FAIL assertions found for tmds specifically) |

**On ULX3S:** Board is ECP5 25F like the ULX3S 25F variant; only GPDI pin remapping should be needed.

## Other catalogued projects

Catalogued repos tagged `video-dvi` (107) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
