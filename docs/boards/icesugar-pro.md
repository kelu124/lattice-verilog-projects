---
title: "iCESugar-Pro"
parent: "ECP5 boards"
grand_parent: "Boards"
nav_order: 6
---
<!-- Generated from data/boards.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# iCESugar-Pro

SODIMM-format ECP5 module with SDRAM and HDMI on the carrier.

| | |
|---|---|
| Board | MuseLab iCESugar-Pro (SODIMM module) |
| FPGA | LFE5U-25F, CABGA256 |
| Evidence | catalogue rows (wuxx__icesugar-pro, mebner86__icesugar-pro_sound2fft) |
| Clock | unknown |
| Catalogued repos | 2 |

*The description is a short summary; FPGA facts come from the catalogue rows cited above.*

## Constraint files (LPF)

Most-copied distinct LPFs for this board in the cloned repos (from the [LPF catalogue](https://github.com/kelu124/ulx3s-klod/blob/main/methodology/lpf-catalogue.md)).

| LPF | Revision | Copies | Peripherals constrained |
|---|---|---|---|
| [`icesugar-pro.lpf`](https://github.com/splinedrive/kianRiscV/blob/da994e6c25b0667d6579922f4bab8d800d19e944/linux_socs/LinuxSoC_v2/engineering/boards/icesugar_pro/icesugar-pro.lpf) (splinedrive__kianriscv) | unknown | 2 | esp32-wifi, ftdi-uart, led, sdram, spi-flash |
| [`icesugar_pro.lpf`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/projects/02_hdmi_test/icesugar_pro.lpf) (mebner86__icesugar-pro_sound2fft) | unknown | 2 | hdmi-dvi, led |
| [`icesugar_pro.lpf`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/projects/03_i2s_direct_loopback/icesugar_pro.lpf) (mebner86__icesugar-pro_sound2fft) | unknown | 2 | led |
| [`icesugar_pro.lpf`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/projects/06_live_fft/icesugar_pro.lpf) (mebner86__icesugar-pro_sound2fft) | unknown | 2 | hdmi-dvi, led |
| [`icesugar_pro.lpf`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/projects/08_pdm_bitstream_loopback/icesugar_pro.lpf) (mebner86__icesugar-pro_sound2fft) | unknown | 2 | led |
| [`blink.lpf`](https://github.com/wuxx/icesugar-pro/blob/087e48d9e0b0a0168ce165a961cba306335c4cf2/src/blink/blink.lpf) (wuxx__icesugar-pro) | unknown | 1 | led |
| [`icesugar-pro.lpf`](https://github.com/splinedrive/kianRiscV/blob/da994e6c25b0667d6579922f4bab8d800d19e944/linux_socs/kianv_harris_mcycle_edition/icesugar-pro.lpf) (splinedrive__kianriscv) | unknown | 1 | esp32-wifi, ftdi-uart, led, sdram, spi-flash |
| [`icesugar_pro.lpf`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/projects/01_blinky/icesugar_pro.lpf) (mebner86__icesugar-pro_sound2fft) | unknown | 1 | led |
| [`icesugar_pro.lpf`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/projects/09_pdm_sigma_delta_modulator/icesugar_pro.lpf) (mebner86__icesugar-pro_sound2fft) | unknown | 1 | led |
| [`icesugar_pro.lpf`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/projects/11_pdm_to_i2s_loopback/icesugar_pro.lpf) (mebner86__icesugar-pro_sound2fft) | unknown | 1 | led |
| [`icesugar_pro.lpf`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/projects/12_uart_loopback/icesugar_pro.lpf) (mebner86__icesugar-pro_sound2fft) | unknown | 1 | ftdi-uart, led |
| [`icesugar_pro.lpf`](https://github.com/mebner86/icesugar-pro_sound2fft/blob/9b513e33c641066fe4b607ee597adec16839200f/projects/13_fft_uart/icesugar_pro.lpf) (mebner86__icesugar-pro_sound2fft) | unknown | 1 | ftdi-uart, led |

## Reusable cores seen on this board

Cores whose source repo, or a repo that copies/instantiates them, targets this board.

| Core | Function | Source repo |
|---|---|---|
| I2S RX/TX + PDM/CIC mic front-end (sound2fft) | [audio-digital](https://github.com/kelu124/ulx3s-klod/blob/main/functions/audio-digital.md) | mebner86__icesugar-pro_sound2fft |
| VexRiscv (SpinalHDL-generated Verilog) | [cpu-riscv](https://github.com/kelu124/ulx3s-klod/blob/main/functions/cpu-riscv.md) | rschlaikjer__fpga-3-softcores |
| 256-point radix-2 FFT core | [dsp](https://github.com/kelu124/ulx3s-klod/blob/main/functions/dsp.md) | mebner86__icesugar-pro_sound2fft |
| sound2fft TMDS encoder + ECP5 DVI serializer | [hdmi-dvi](https://github.com/kelu124/ulx3s-klod/blob/main/functions/hdmi-dvi.md) | mebner86__icesugar-pro_sound2fft |
| vga2dvid + tmds_encoder DVI/TMDS core (Mike Field / EMARD) | [hdmi-dvi](https://github.com/kelu124/ulx3s-klod/blob/main/functions/hdmi-dvi.md) | emard__ulx3s-misc |

## Projects targeting this board

- [mebner86__icesugar-pro_sound2fft](https://github.com/mebner86/icesugar-pro_sound2fft): iCESugar-Pro sound2fft: real-time audio spectrum analyzer
- [wuxx__icesugar-pro](https://github.com/wuxx/icesugar-pro): iCESugar-pro: vendor example collection
{% endraw %}
