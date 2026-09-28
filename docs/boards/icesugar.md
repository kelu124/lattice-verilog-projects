---
title: "iCESugar"
parent: "iCE40 UP5K boards"
grand_parent: "Boards"
nav_order: 3
---
<!-- Generated from data/boards.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# iCESugar

Small UP5K board with a drag-and-drop programmer.

| | |
|---|---|
| Board | MuseLab iCESugar v1.5 |
| FPGA | iCE40 UP5K, SG48 |
| Evidence | catalogue rows (wuxx__icesugar) |
| Clock | 12 MHz (catalogue notes) |
| Catalogued repos | 5 |

*The description is a short summary; FPGA facts come from the catalogue rows cited above.*

## Constraint files (PCF)

| PCF | Repository |
|---|---|
| [`gateware/boards/icesugar/pinmap.pcf`](https://github.com/apfaudio/eurorack-pmod/blob/ddb9aa92fab7f74783f7ed3bf248eec56a6ceb00/gateware/boards/icesugar/pinmap.pcf) | apfaudio__eurorack-pmod |
| [`icesugar/icesugar.pcf`](https://github.com/bit-hack/icesid/blob/b126c46d25a6455914f218f83695d065efd9f961/icesugar/icesugar.pcf) | bit-hack__icesid |
| [`icesugar/icesugar.pcf`](https://github.com/td0034/fpga/blob/476fe356f880d6b8254094a3966e34b9edac7c62/icesugar/icesugar.pcf) | td0034__fpga |
| [`icesugar/granular-synth-engine/02_i2s_passthrough/i2s_passthrough.pcf`](https://github.com/td0034/fpga/blob/476fe356f880d6b8254094a3966e34b9edac7c62/icesugar/granular-synth-engine/02_i2s_passthrough/i2s_passthrough.pcf) | td0034__fpga |
| [`icesugar/granular-synth-engine/04_dds_synth/dds_synth.pcf`](https://github.com/td0034/fpga/blob/476fe356f880d6b8254094a3966e34b9edac7c62/icesugar/granular-synth-engine/04_dds_synth/dds_synth.pcf) | td0034__fpga |
| [`icesugar/granular-synth-engine/01_i2s_out/i2s_out.pcf`](https://github.com/td0034/fpga/blob/476fe356f880d6b8254094a3966e34b9edac7c62/icesugar/granular-synth-engine/01_i2s_out/i2s_out.pcf) | td0034__fpga |
| [`icesugar/granular-synth-engine/03_spi_slave/spi_slave.pcf`](https://github.com/td0034/fpga/blob/476fe356f880d6b8254094a3966e34b9edac7c62/icesugar/granular-synth-engine/03_spi_slave/spi_slave.pcf) | td0034__fpga |
| [`icesugar/granular-synth-engine/05_grain_engine/grain_engine.pcf`](https://github.com/td0034/fpga/blob/476fe356f880d6b8254094a3966e34b9edac7c62/icesugar/granular-synth-engine/05_grain_engine/grain_engine.pcf) | td0034__fpga |
| [`icesugar/examples/tone/tone.pcf`](https://github.com/td0034/fpga/blob/476fe356f880d6b8254094a3966e34b9edac7c62/icesugar/examples/tone/tone.pcf) | td0034__fpga |
| [`icesugar/examples/uart_hello/uart_hello.pcf`](https://github.com/td0034/fpga/blob/476fe356f880d6b8254094a3966e34b9edac7c62/icesugar/examples/uart_hello/uart_hello.pcf) | td0034__fpga |
| [`icesugar/examples/sine_tone/sine_tone.pcf`](https://github.com/td0034/fpga/blob/476fe356f880d6b8254094a3966e34b9edac7c62/icesugar/examples/sine_tone/sine_tone.pcf) | td0034__fpga |
| [`icesugar/examples/sine_rgb/sine_rgb.pcf`](https://github.com/td0034/fpga/blob/476fe356f880d6b8254094a3966e34b9edac7c62/icesugar/examples/sine_rgb/sine_rgb.pcf) | td0034__fpga |

## Reusable cores seen on this board

Cores whose source repo, or a repo that copies/instantiates them, targets this board.

| Core | Function | Source repo |
|---|---|---|
| AK4619 audio codec driver + PMOD I2C master | [audio-digital](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/audio-digital.md) | apfaudio__eurorack-pmod |
| TV80 Z80-compatible core (emard__ulx3s_galaksija copy) | [cpu-retro](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-retro.md) | emard__ulx3s_galaksija |
| FPGA 101 PicoSoC with LCD text console and MicroPython | [cpu-riscv](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-riscv.md) | mmicko__fpga101-workshop |
| PicoRV32 RISC-V core | [cpu-riscv](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/cpu-riscv.md) | yosyshq__picorv32 |
| Sigma-delta DAC (up5k-demos) | [dac](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/dac.md) | daveshah1__up5k-demos |
| smoldvi small portable DVI core | [hdmi-dvi](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/hdmi-dvi.md) | wren6991__smoldvi |
| SID reimplementation (icesid) | [sound-chips](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/sound-chips.md) | bit-hack__icesid |
| spimemio SPI/QSPI flash XIP controller | [spi-flash](https://github.com/kelu124/lattice-verilog-projects/blob/main/functions/spi-flash.md) | yosyshq__picorv32 |

## Projects targeting this board

- [apfaudio__eurorack-pmod](https://github.com/apfaudio/eurorack-pmod): Eurorack PMOD: AK4619 audio-codec PMOD gateware
- [bit-hack__icesid](https://github.com/bit-hack/icesid): reDIP-SID/iCESugar: open-source FPGA reimplementation of the MOS 6581/8580 SID chip audio synthesis, drop-in…
- [td0034__fpga](https://github.com/td0034/fpga): Multi-board
- [wren6991__smoldvi](https://github.com/Wren6991/SmolDVI): iCEBreaker/iCEstick/iCESugar/TinyFPGA-BX: SmolDVI, a small direct DVI/TMDS output core ([review](https://github.com/kelu124/lattice-verilog-projects/blob/main/projects/wren6991__smoldvi.md))
- [wuxx__icesugar](https://github.com/wuxx/icesugar): iCESugar: MuseLab's vendor example/demo collection for the iCESugar v1.5 board
{% endraw %}
