---
title: "pico-ice"
parent: "iCE40 UP5K boards"
grand_parent: "Boards"
nav_order: 5
---
<!-- Generated from data/boards.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# pico-ice

RP2040 microcontroller plus UP5K; the RP2040 programs the FPGA (DFU on the MCU).

| | |
|---|---|
| Board | pico-ice (tinyVision.ai, RP2040 + iCE40) |
| FPGA | iCE40 UP5K, SG48 |
| Evidence | catalogue rows (tinyvision-ai-inc__pico-ice-sdk) |
| Clock | unknown |
| Catalogued repos | 2 |

*The description is a short summary; FPGA facts come from the catalogue rows cited above.*

## Constraint files (PCF)

| PCF | Repository |
|---|---|
| [`iceFUN.pcf`](https://github.com/MichaelBell/nanoV/blob/e1a405edd9af2cb56c3f54bae2316a29c9bcd2d9/iceFUN.pcf) | michaelbell__nanov |
| [`pico_ice/pico_ice.pcf`](https://github.com/MichaelBell/nanoV/blob/e1a405edd9af2cb56c3f54bae2316a29c9bcd2d9/pico_ice/pico_ice.pcf) | michaelbell__nanov |
| [`rtl/pico_ice.pcf`](https://github.com/tinyvision-ai-inc/pico-ice-sdk/blob/f3ddedcdabdbb929939720df0856f2f6b39962fc/rtl/pico_ice.pcf) | tinyvision-ai-inc__pico-ice-sdk |
| [`rtl/pico2_ice.pcf`](https://github.com/tinyvision-ai-inc/pico-ice-sdk/blob/f3ddedcdabdbb929939720df0856f2f6b39962fc/rtl/pico2_ice.pcf) | tinyvision-ai-inc__pico-ice-sdk |
| [`examples/ice_apio_uart_echo/pico_ice.pcf`](https://github.com/tinyvision-ai-inc/pico-ice-sdk/blob/f3ddedcdabdbb929939720df0856f2f6b39962fc/examples/ice_apio_uart_echo/pico_ice.pcf) | tinyvision-ai-inc__pico-ice-sdk |
| [`examples/rp2_ice_blinky/pico_ice.pcf`](https://github.com/tinyvision-ai-inc/pico-ice-sdk/blob/f3ddedcdabdbb929939720df0856f2f6b39962fc/examples/rp2_ice_blinky/pico_ice.pcf) | tinyvision-ai-inc__pico-ice-sdk |
| [`examples/ice_apio_blinky/up5k.pcf`](https://github.com/tinyvision-ai-inc/pico-ice-sdk/blob/f3ddedcdabdbb929939720df0856f2f6b39962fc/examples/ice_apio_blinky/up5k.pcf) | tinyvision-ai-inc__pico-ice-sdk |
| [`examples/ice_makefile_iverilog_counter/ice40.pcf`](https://github.com/tinyvision-ai-inc/pico-ice-sdk/blob/f3ddedcdabdbb929939720df0856f2f6b39962fc/examples/ice_makefile_iverilog_counter/ice40.pcf) | tinyvision-ai-inc__pico-ice-sdk |
| [`examples/ice_makefile_verilator_counter/ice40.pcf`](https://github.com/tinyvision-ai-inc/pico-ice-sdk/blob/f3ddedcdabdbb929939720df0856f2f6b39962fc/examples/ice_makefile_verilator_counter/ice40.pcf) | tinyvision-ai-inc__pico-ice-sdk |
| [`examples/ice_makefile_blinky/ice40.pcf`](https://github.com/tinyvision-ai-inc/pico-ice-sdk/blob/f3ddedcdabdbb929939720df0856f2f6b39962fc/examples/ice_makefile_blinky/ice40.pcf) | tinyvision-ai-inc__pico-ice-sdk |

## Reusable cores seen on this board

Cores whose source repo, or a repo that copies/instantiates them, targets this board.

| Core | Function | Source repo |
|---|---|---|
| 64x64 LED panel scanner (ledscan) | [led-drivers](https://github.com/kelu124/ulx3s-klod/blob/main/functions/led-drivers.md) | goran-mahovlic__prjtrellis-led64x64 |

## Projects targeting this board

- [michaelbell__nanov](https://github.com/MichaelBell/nanoV): NanoV: minimal-area bit-serial RISC-V
- [tinyvision-ai-inc__pico-ice-sdk](https://github.com/tinyvision-ai-inc/pico-ice-sdk): pico-ice / pico2-ice: RP2040/RP2350 C SDK for the onboard iCE40 UP5K FPGA, incl.
{% endraw %}
