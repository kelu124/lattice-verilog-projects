---
title: "Camera input"
parent: "Cores by function"
nav_order: 6
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# Camera input

Camera sensor capture (OV7670 etc.) and video input.

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [OV7670 camera capture + SCCB config core](#core-msrraju07-ov7670-pipeline) ★ | [msrraju07__iop](https://github.com/MSRRaju07/IOP) | Verilog | MIT (LICENSE, Copyright 2021 Angelo Jacobo) | any | 3 |
| [camera85 nMigen OV7670 capture + image pipeline](#core-lawrie-camera85-nmigen) | [lawrie__ulx3s-nmigen-examples](https://github.com/lawrie/ulx3s-nmigen-examples) | nMigen (Python) | none found | any | 0 |
| [ImgController + ImgI2CMaster image-sensor interface (iCE40)](#core-toasterllc-img-controller) | [toasterllc__mdccode](https://github.com/toasterllc/MDCCode) | Verilog | public domain | iCE40 | 0 |
| [OV7670 capture + SCCB master (ulx3s-experiments)](#core-tucanae47-ov7670-capture) | [tucanae47__ulx3s-experiments](https://github.com/tucanae47/ulx3s-experiments) | Verilog | none found | any | 1 |
| [OV7670 RGB/YUV capture + color-filter + VGA preview (ULX3S apio)](#core-jderobot-ov7670-colorfilter) | [jderobot__fpga-robotics](https://github.com/JdeRobot/FPGA-robotics) | Verilog | GPL-3.0-or-later | any | 0 |

## Cores

### OV7670 camera capture + SCCB config core (best) {#core-msrraju07-ov7670-pipeline}

Captures OV7670 parallel PCLK/HREF/VSYNC/D[7:0] video into a FIFO with brightness/contrast controls, alongside a combined I2C/SCCB master (i2c_top.v, no external pull-ups needed) for camera register configuration; part of a full OV7670->Sobel->SDRAM->HDMI pipeline proven on ULX3S 85F.

| | |
|---|---|
| Repository | [msrraju07__iop](https://github.com/MSRRaju07/IOP): OV7670 camera Sobel edge-detection pipeline on ULX3S with HDMI output, built via Icestudio blocks + generated… |
| Files | [`src/camera_interface.v`](https://github.com/MSRRaju07/IOP/blob/693dacba2f8450417d9944f1803255a44c842042/src/camera_interface.v), [`src/i2c_top.v`](https://github.com/MSRRaju07/IOP/blob/693dacba2f8450417d9944f1803255a44c842042/src/i2c_top.v) |
| Top module | `camera_interface` |
| Language | Verilog |
| License | MIT (LICENSE, Copyright 2021 Angelo Jacobo) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Needs an OV7670 PMOD/breakout wired to GPIO; requires driving cmos_xclk and tuning the i2c_top SCCB timing per camera revision.

**Used by 3 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [advikbahadur__ulx3s-superresolution-cnn](https://github.com/ADVIKBAHADUR/ULX3s-Superresolution-CNN) (instantiates [`src/camera_interface.v`](https://github.com/ADVIKBAHADUR/ULX3s-Superresolution-CNN/blob/7979af367cc20e4393071c718ab0e04dae12ad86/src/camera_interface.v))
- [angelojacobo__ulx3s_fpga_camera_streaming](https://github.com/AngeloJacobo/ULX3S_FPGA_Camera_Streaming) (instantiates [`src/camera_interface.v`](https://github.com/AngeloJacobo/ULX3S_FPGA_Camera_Streaming/blob/ba9b3d836a548b30f4f52cfe46123ae57beefe33/src/camera_interface.v))
- [angelojacobo__ulx3s_fpga_sobel_edge_detection_ov7670](https://github.com/AngeloJacobo/ULX3S_FPGA_Sobel_Edge_Detection_OV7670) (instantiates [`src/camera_interface.v`](https://github.com/AngeloJacobo/ULX3S_FPGA_Sobel_Edge_Detection_OV7670/blob/693dacba2f8450417d9944f1803255a44c842042/src/camera_interface.v))

### camera85 nMigen OV7670 capture + image pipeline {#core-lawrie-camera85-nmigen}

nMigen OV7670 capture (camera.py), SCCB register bus (sccb.py) and camera register table (ov7670_config.py), part of a larger image-processing chain (ROI/statistics/gamma/color control) selectable to any ULX3S FPGA size at build time.

| | |
|---|---|
| Repository | [lawrie__ulx3s-nmigen-examples](https://github.com/lawrie/ulx3s-nmigen-examples): Large collection of nMigen/Amaranth examples for ULX3S: blinky, camera, DVI, SDRAM, PS/2, retro CPUs, OLED |
| Files | [`camera85/camera.py`](https://github.com/lawrie/ulx3s-nmigen-examples/blob/ad5f433e3c154b8fb11d1c116f087a6ba4ebdf5e/camera85/camera.py), [`camera85/sccb.py`](https://github.com/lawrie/ulx3s-nmigen-examples/blob/ad5f433e3c154b8fb11d1c116f087a6ba4ebdf5e/camera85/sccb.py), [`camera85/ov7670_config.py`](https://github.com/lawrie/ulx3s-nmigen-examples/blob/ad5f433e3c154b8fb11d1c116f087a6ba4ebdf5e/camera85/ov7670_config.py) |
| Top module | n/a |
| Language | nMigen (Python) |
| License | none found |
| FPGA / primitives | any: none (portable) |
| Tests | sim_imc.py/sim_conv.py/sim_extend.py present, waveform-only (no assert/PASS-FAIL found) |

**On ULX3S:** Requires the nMigen/amaranth-boards toolchain; camconfig.py + camread.py glue the pieces together.

### ImgController + ImgI2CMaster image-sensor interface (iCE40) {#core-toasterllc-img-controller}

Image-sensor (parallel-bus) capture controller with an accompanying I2C master for sensor register configuration; uses iCE40 SB_IO primitives for the pixel-bus and I2C pins.

| | |
|---|---|
| Repository | [toasterllc__mdccode](https://github.com/toasterllc/MDCCode): mdccode (Photon camera): iCE40 HX8K gateware bridging image sensor/SDRAM/SD card to MSP430/STM32 MCUs; repo… |
| Files | [`Code/ICE40/Shared/ImgController.v`](https://github.com/toasterllc/MDCCode/blob/4de8ad2c5ddb1217a1d29adeabc2d0e747b91a3e/Code/ICE40/Shared/ImgController.v), [`Code/ICE40/Shared/ImgI2CMaster.v`](https://github.com/toasterllc/MDCCode/blob/4de8ad2c5ddb1217a1d29adeabc2d0e747b91a3e/Code/ICE40/Shared/ImgI2CMaster.v) |
| Top module | `ImgController` |
| Language | Verilog |
| License | public domain (LICENSE.md, one line, no SPDX id) |
| FPGA / primitives | iCE40: `SB_IO` |
| Tests | none found |

**On ULX3S:** Needs SB_IO instances ported to ECP5 TRELLIS_IO; logic/FSM is otherwise portable.

### OV7670 capture + SCCB master (ulx3s-experiments) {#core-tucanae47-ov7670-capture}

OV7670 capture core (ov7670_capture.v) with a dedicated SCCB master (sccb_master.v) plus an async-FIFO clock-domain-crossing stack, proven on ULX3S 85F via apio.

| | |
|---|---|
| Repository | [tucanae47__ulx3s-experiments](https://github.com/tucanae47/ulx3s-experiments): tucanae47/ulx3s-experiments: small ULX3S experiments |
| Files | [`cam/ov7670_capture.v`](https://github.com/tucanae47/ulx3s-experiments/blob/f696bf152b910293ef3a4e1e642a2ea95e88f078/cam/ov7670_capture.v), [`cam/sccb_master.v`](https://github.com/tucanae47/ulx3s-experiments/blob/f696bf152b910293ef3a4e1e642a2ea95e88f078/cam/sccb_master.v) |
| Top module | `ov7670_capture` |
| Language | Verilog |
| License | none found |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Comes with a matching vga_display.v/oled_video.v output stage in the same directory for a live preview.

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [jderobot__fpga-robotics](https://github.com/JdeRobot/FPGA-robotics) (instantiates [`phys_fpga/alhambra_ii/apio/ov7670_rgb444_80x60/ov7670_top_ctrl.v`](https://github.com/JdeRobot/FPGA-robotics/blob/b197ad9418f10182829ff914d83fb3b3e7be8e52/phys_fpga/alhambra_ii/apio/ov7670_rgb444_80x60/ov7670_top_ctrl.v))

### OV7670 RGB/YUV capture + color-filter + VGA preview (ULX3S apio) {#core-jderobot-ov7670-colorfilter}

OV7670 RGB/YUV capture with on-the-fly colour filtering and a live VGA preview; one of many near-identical board variants (ULX3S/Alhambra II/Nexys4) in this repo sharing the same capture core, this is the apio/ULX3S build.

| | |
|---|---|
| Repository | [jderobot__fpga-robotics](https://github.com/JdeRobot/FPGA-robotics): FPGA-robotics: JdeRobot teaching library for camera/robotics on FPGA; |
| Files | [`phys_fpga/ulx3s/apio/ov7670_rgb_yuv_320x240_colorfilter/ov7670_capture.v`](https://github.com/JdeRobot/FPGA-robotics/blob/b197ad9418f10182829ff914d83fb3b3e7be8e52/phys_fpga/ulx3s/apio/ov7670_rgb_yuv_320x240_colorfilter/ov7670_capture.v), [`phys_fpga/ulx3s/apio/ov7670_rgb_yuv_320x240_colorfilter/ov7670_ctrl_reg.v`](https://github.com/JdeRobot/FPGA-robotics/blob/b197ad9418f10182829ff914d83fb3b3e7be8e52/phys_fpga/ulx3s/apio/ov7670_rgb_yuv_320x240_colorfilter/ov7670_ctrl_reg.v), [`phys_fpga/ulx3s/apio/ov7670_rgb_yuv_320x240_colorfilter/ov7670_top_ctrl.v`](https://github.com/JdeRobot/FPGA-robotics/blob/b197ad9418f10182829ff914d83fb3b3e7be8e52/phys_fpga/ulx3s/apio/ov7670_rgb_yuv_320x240_colorfilter/ov7670_top_ctrl.v), [`phys_fpga/ulx3s/apio/ov7670_rgb_yuv_320x240_colorfilter/sccb_master.v`](https://github.com/JdeRobot/FPGA-robotics/blob/b197ad9418f10182829ff914d83fb3b3e7be8e52/phys_fpga/ulx3s/apio/ov7670_rgb_yuv_320x240_colorfilter/sccb_master.v) |
| Top module | `ov7670_top_ctrl` |
| Language | Verilog |
| License | GPL-3.0-or-later (LICENSE.md, software); repo also carries CERN-OHL-S-2.0 for hardware/PCB design |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** apio.ini + ulx3s_v20.lpf (or ulx3s_v20_pmodcam.lpf.txt) targets ULX3S directly; the repo has sibling variants (sobel, color-centroid tracking) using the same capture files.

## Other catalogued projects

Catalogued repos tagged `camera` (14), `video-input` (10) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
