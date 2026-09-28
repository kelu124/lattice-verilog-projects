---
title: "LED drivers"
parent: "Cores by function"
nav_order: 33
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# LED drivers

HUB75 panels, WS2812 strips, LED matrices.

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [HUB75(e) LED matrix driver (fpga_led_display)](#core-w531t4-hub75-display-core) ★ | [w531t4__fpga_led_display](https://github.com/w531t4/fpga_led_display) | SystemVerilog | MIT (LICENSE, SPDX header in files) | ECP5 | 0 |
| [64x64 LED panel scanner (ledscan)](#core-goran-mahovlic-ledscan-64x64) | [goran-mahovlic__prjtrellis-led64x64](https://github.com/goran-mahovlic/prjtrellis-led64x64) | VHDL | BSD (`-- (c)EMARD` / `-- LICENSE=BSD` header) | ECP5 | 4 |
| [HUB75e LED panel driver (colorlight-led-cube)](#core-lucysrausch-hub75-ledpanel) | [lucysrausch__colorlight-led-cube](https://github.com/lucysrausch/colorlight-led-cube) | Verilog | GPL-3.0 (LICENSE, root) | ECP5 | 3 |
| [no2hub75 HUB75 panel core (no2fpga library)](#core-no2hub75-led-panel) | [smunaut__ice40-playground](https://github.com/smunaut/ice40-playground) | Verilog | CERN-OHL-W-2.0 | iCE40 UP5K | 0 |
| [PWM/PDM gamma-corrected LED brightness drivers](#core-kbob-led-pwm-pdm-gamma) | [kbob__icebreaker-candy](https://github.com/kbob/icebreaker-candy) | Verilog | GPL-3.0 (LICENSE, root; no per-file SPDX headers) | any | 0 |

## Cores

### HUB75(e) LED matrix driver (fpga_led_display) (best) {#core-w531t4-hub75-display-core}

Board-agnostic HUB75(e) RGB LED panel display_core with gamma correction, double-buffered framebuffer fabric, FM6126 panel init and a watchdog; built with `make BOARD=ulx3s`.

| | |
|---|---|
| Repository | [w531t4__fpga_led_display](https://github.com/w531t4/fpga_led_display): w531t4/fpga_led_display: LED matrix panel driver |
| Files | [`src/display_core.sv`](https://github.com/w531t4/fpga_led_display/blob/7ba06f8f6dd70ef95ebfeca1103158c1868886e0/src/display_core.sv), [`src/matrix_scan.sv`](https://github.com/w531t4/fpga_led_display/blob/7ba06f8f6dd70ef95ebfeca1103158c1868886e0/src/matrix_scan.sv), [`src/hub75_rgb_pack.sv`](https://github.com/w531t4/fpga_led_display/blob/7ba06f8f6dd70ef95ebfeca1103158c1868886e0/src/hub75_rgb_pack.sv), [`src/gamma_correct.sv`](https://github.com/w531t4/fpga_led_display/blob/7ba06f8f6dd70ef95ebfeca1103158c1868886e0/src/gamma_correct.sv), [`src/framebuffer_fabric.sv`](https://github.com/w531t4/fpga_led_display/blob/7ba06f8f6dd70ef95ebfeca1103158c1868886e0/src/framebuffer_fabric.sv), [`src/fm6126init.sv`](https://github.com/w531t4/fpga_led_display/blob/7ba06f8f6dd70ef95ebfeca1103158c1868886e0/src/fm6126init.sv), [`src/top_ulx3s.sv`](https://github.com/w531t4/fpga_led_display/blob/7ba06f8f6dd70ef95ebfeca1103158c1868886e0/src/top_ulx3s.sv), [`src/constraints/ulx3s_v316.lpf`](https://github.com/w531t4/fpga_led_display/blob/7ba06f8f6dd70ef95ebfeca1103158c1868886e0/src/constraints/ulx3s_v316.lpf) |
| Top module | `top_ulx3s` |
| Language | SystemVerilog |
| License | MIT (LICENSE, SPDX header in files) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | none found in this pass |

**On ULX3S:** top_ulx3s.sv is the real ULX3S build target (ESP32 wifi_gpio SPI control link); src/constraints/ulx3s_v316.lpf ships in-repo.

### 64x64 LED panel scanner (ledscan) {#core-goran-mahovlic-ledscan-64x64}

EMARD's VHDL scan-out driver for 64x64 indoor RGB LED panel modules (P2.5/P3/P4), proven on ULX3S 12F with prjtrellis.

| | |
|---|---|
| Repository | [goran-mahovlic__prjtrellis-led64x64](https://github.com/goran-mahovlic/prjtrellis-led64x64): HUB75 64x64 LED panel, sprite animation |
| Files | [`emard/ledscan.vhd`](https://github.com/goran-mahovlic/prjtrellis-led64x64/blob/ffa935a32df75f6b93442cb0ce7e5c70da3e794c/emard/ledscan.vhd) |
| Top module | `ledscan` |
| Language | VHDL |
| License | BSD (`-- (c)EMARD` / `-- LICENSE=BSD` header) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | none found |

**On ULX3S:** Small, self-contained driver; pair with sprite_rom.v in the same repo for a framebuffer source.

**Used by 4 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc) (instantiates [`examples/led64x64/emard/top.v`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/led64x64/emard/top.v))
- [lawrie__ulx3s_examples](https://github.com/lawrie/ulx3s_examples) (instantiates [`ledpanel/top.v`](https://github.com/lawrie/ulx3s_examples/blob/b6ff00099265401fef4843e4e89c2ac54254c95f/ledpanel/top.v))
- [michaelbell__nanov](https://github.com/MichaelBell/nanoV) (instantiates [`top.v`](https://github.com/MichaelBell/nanoV/blob/e1a405edd9af2cb56c3f54bae2316a29c9bcd2d9/top.v))
- [ulx3s__fpga-odysseus](https://github.com/ulx3s/fpga-odysseus) (instantiates [`projects/LedPanel/DualPanel/top.v`](https://github.com/ulx3s/fpga-odysseus/blob/3f91fd255e07b6570616224f5c2389f29aac6b03/projects/LedPanel/DualPanel/top.v))

### HUB75e LED panel driver (colorlight-led-cube) {#core-lucysrausch-hub75-ledpanel}

HUB75e RGB LED panel scan-out driver plus a UDP-payload-to-framebuffer writer, originally from Clifford Wolf's c3demo, adapted for a Colorlight-driven LED cube.

| | |
|---|---|
| Repository | [lucysrausch__colorlight-led-cube](https://github.com/lucysrausch/colorlight-led-cube): Colorlight 5A-75B "LED cube" hack: HUB75e RGB panel driver |
| Files | [`fpga/ledpanel.v`](https://github.com/lucysrausch/colorlight-led-cube/blob/ebac05e1faed52fef736eef9c1a2e3b0c391b68c/fpga/ledpanel.v), [`fpga/udp_panel_writer.v`](https://github.com/lucysrausch/colorlight-led-cube/blob/ebac05e1faed52fef736eef9c1a2e3b0c391b68c/fpga/udp_panel_writer.v) |
| Top module | `ledpanel` |
| Language | Verilog |
| License | GPL-3.0 (LICENSE, root) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | none found |

**On ULX3S:** Proven on Colorlight 5A-75B (ECP5 25F); fpga/pll.v (25->125MHz + 52MHz panel clock) uses ECP5 EHXPLLL and needs reparameterizing, ledpanel.v itself is plain Verilog.

**Used by 3 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [lawrie__blackicemxbook](https://github.com/lawrie/blackicemxbook) (instantiates [`examples/ledbaby/baby.v`](https://github.com/lawrie/blackicemxbook/blob/ff5fdb31c85d20eacbe24b1bf8f5ed2e0df0bb8f/examples/ledbaby/baby.v))
- [lawrie__verilog_examples](https://github.com/lawrie/verilog_examples) (instantiates [`fpga/ledbaby/baby.v`](https://github.com/lawrie/verilog_examples/blob/ee8f0d2b44313b683a63ea6a0b151f454f8b9ddc/fpga/ledbaby/baby.v))
- [msiddalingaiah__centurion](https://github.com/msiddalingaiah/Centurion) (instantiates [`Verilog/iCE40.v`](https://github.com/msiddalingaiah/Centurion/blob/407d7482feb2955629ce4c38c11e6362354dd29e/Verilog/iCE40.v))

### no2hub75 HUB75 panel core (no2fpga library) {#core-no2hub75-led-panel}

Full-featured HUB75 driver library (scan, binary-code-modulation gamma, colormap, framebuffer, PHY) from smunaut's no2fpga core collection.

| | |
|---|---|
| Repository | [smunaut__ice40-playground](https://github.com/smunaut/ice40-playground): iCEBreaker: collection of iCE40 UP5K IP cores |
| Files | [`cores/no2hub75/rtl/hub75_top.v`](https://github.com/smunaut/ice40-playground/blob/d2fa0050129c14a7fc42f64f115366f6f2a51669/cores/no2hub75/rtl/hub75_top.v), [`cores/no2hub75/rtl/hub75_scan.v`](https://github.com/smunaut/ice40-playground/blob/d2fa0050129c14a7fc42f64f115366f6f2a51669/cores/no2hub75/rtl/hub75_scan.v), [`cores/no2hub75/rtl/hub75_bcm.v`](https://github.com/smunaut/ice40-playground/blob/d2fa0050129c14a7fc42f64f115366f6f2a51669/cores/no2hub75/rtl/hub75_bcm.v), [`cores/no2hub75/rtl/hub75_colormap.v`](https://github.com/smunaut/ice40-playground/blob/d2fa0050129c14a7fc42f64f115366f6f2a51669/cores/no2hub75/rtl/hub75_colormap.v), [`cores/no2hub75/rtl/hub75_gamma.v`](https://github.com/smunaut/ice40-playground/blob/d2fa0050129c14a7fc42f64f115366f6f2a51669/cores/no2hub75/rtl/hub75_gamma.v), [`cores/no2hub75/rtl/hub75_framebuffer.v`](https://github.com/smunaut/ice40-playground/blob/d2fa0050129c14a7fc42f64f115366f6f2a51669/cores/no2hub75/rtl/hub75_framebuffer.v), [`cores/no2hub75/rtl/hub75_phy.v`](https://github.com/smunaut/ice40-playground/blob/d2fa0050129c14a7fc42f64f115366f6f2a51669/cores/no2hub75/rtl/hub75_phy.v) |
| Top module | `hub75_top` |
| Language | Verilog |
| License | CERN-OHL-W-2.0 (cores/no2hub75/LICENSE) |
| FPGA / primitives | iCE40 UP5K: `SB_IO` |
| Tests | sim/hub75_init_inject_tb.v (waveform-only, not individually re-run here) |

**On ULX3S:** Only hub75_phy.v/hub75_phy_ddr.v instantiate SB_IO and need an ECP5 IO-primitive rewrite; hub75_scan.v/hub75_bcm.v/hub75_colormap.v/hub75_gamma.v/hub75_framebuffer.v are portable.

Full review: [smunaut__ice40-playground](../projects/smunaut__ice40-playground.md).

### PWM/PDM gamma-corrected LED brightness drivers {#core-kbob-led-pwm-pdm-gamma}

Technology-independent PWM and PDM gamma-corrected LED brightness drivers (led_main pipeline) for RGB LED panels, plus a simple un-gamma-corrected variant.

| | |
|---|---|
| Repository | [kbob__icebreaker-candy](https://github.com/kbob/icebreaker-candy): iCEBreaker: eye-candy demos driving a 64x64 HUB75 RGB LED panel |
| Files | [`include/led-pwm-gamma.v`](https://github.com/kbob/icebreaker-candy/blob/e3c09f357b5f4862751aba7ea337a82cfa4f20e0/include/led-pwm-gamma.v), [`include/led-pdm-gamma.v`](https://github.com/kbob/icebreaker-candy/blob/e3c09f357b5f4862751aba7ea337a82cfa4f20e0/include/led-pdm-gamma.v), [`include/led-simple.v`](https://github.com/kbob/icebreaker-candy/blob/e3c09f357b5f4862751aba7ea337a82cfa4f20e0/include/led-simple.v) |
| Top module | n/a |
| Language | Verilog |
| License | GPL-3.0 (LICENSE, root; no per-file SPDX headers) |
| FPGA / primitives | any: none (portable) |
| Tests | none found in this pass |

**On ULX3S:** No vendor primitives in these include/ files; client instantiates led_main and supplies a painter24 module plus a generated gamma table hex.

## Other catalogued projects

Catalogued repos tagged `led-matrix` (14), `led` (1) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
