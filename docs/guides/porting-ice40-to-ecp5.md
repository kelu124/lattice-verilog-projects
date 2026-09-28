---
title: "Porting iCE40 to ECP5"
parent: "Guides"
nav_order: 2
---
<!-- Generated from data/pages/porting-ice40-to-ecp5.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# Porting iCE40 cores to ECP5

Many of the best small cores in the collection were written for iCE40 boards (iCEBreaker, UPduino, BlackIce, HX8K breakout). Their logic is usually portable Verilog; only the instantiated `SB_*` primitives and the clocking need changing. This page collects what the reviews found; the primitive table comes from the [ice40-playground review](../projects/smunaut__ice40-playground.md).

## Checklist

1. `grep -n "SB_" -r rtl/` to list the iCE40 primitives the core instantiates. Cores listed as `fpga: any` in [Cores by function](../functions/index.md) have none.
2. Replace the PLL: `SB_PLL40_*` (parameters from `icepll`) becomes `EHXPLLL` on ECP5. Use emard's parametric `ecp5pll` wrapper or Project Trellis `ecppll` to compute dividers (see [PLLs and clocking](../functions/pll-clock.md)).
3. Re-check clock frequencies: iCE40 boards run from 12 MHz (iCEBreaker, HX8K breakout) or other crystals, the ULX3S from 25 MHz (`clk_25mhz`). Baud-rate dividers, video timings and USB 48 MHz clocks must be recomputed.
4. Replace IO and memory primitives (table below), then the pin constraints: `.pcf` (`set_io name pin`) becomes `.lpf` (`LOCATE COMP "name" SITE "pin"; IOBUF PORT "name" IO_TYPE=LVCMOS33;`). Start from the reference [ULX3S LPF](../boards/ulx3s.md).
5. Replace the internal oscillator `SB_HFOSC`/`SB_LFOSC` with the board clock (or ECP5 `OSCG`), and `SB_WARMBOOT` with the ECP5 reboot mechanism of your board (the ULX3S DFU bootloader pulls PROGRAMN, see the [DFU guide](DFUs.md)).

## Primitive map

| iCE40 primitive | Used for | ECP5 equivalent |
|---|---|---|
| `SB_IO` | IO pads, tristate, registered and DDR IO (PHYs of USB, HyperRAM, QPI, HUB75, SPI, I2C cores) | `TRELLIS_IO` or `BB` (tristate pad) + `ODDRX1F`/`IDDRX1F` for DDR, `OFS1P3DX`/`IFS1P3DX` for registered IO; already done natively in the HAD2019 badge SoC and ultraembedded's OrangeCrab DDR3 PHY |
| `SB_PLL40_CORE`, `SB_PLL40_PAD`, `SB_PLL40_2F_*` | Clock synthesis | `EHXPLLL` |
| `SB_GB` | Global clock buffer | usually automatic in nextpnr-ecp5; `ECLKSYNCB`/`CLKDIVF` for edge clocks |
| `SB_RAM40_4K` | 4 Kbit block RAM (often instantiated for USB endpoint buffers) | `DP16KD` (16 Kbit): remap depth/width and init parameters, or let yosys infer from a plain array |
| `SB_SPRAM256KA` | 256 Kbit single-port RAM (UP5K only) | no equivalent: build from several `DP16KD`, or use the SDRAM |
| `SB_MAC16` | DSP multiply-accumulate (UP5K) | `MULT18X18D` / `ALU54B`, or inferred `*` |
| `SB_LUT4`, `SB_CARRY`, `SB_DFF*` | Hand-placed logic, carry chains, flip-flops | `LUT4`, `CCU2C`, inferred flip-flops (or let synthesis infer them) |
| `SB_RGBA_DRV`, `SB_LEDDA_IP` | Constant-current RGB LED driver (UP5K) | no hard macro: PWM on a GPIO plus resistors |
| `SB_HFOSC`, `SB_LFOSC` | Internal oscillators | board clock, or `OSCG` |

## Examples of ports already in the collection

- [smunaut__ice40-playground](../projects/smunaut__ice40-playground.md): the no2 cores separate a portable controller from a small `SB_IO` PHY; the HAD2019 badge SoC has ECP5 versions of the same PHY pattern ([review](../projects/spritetm__hadbadge2019_fpgasoc.md)).
- [yosyshq__picorv32](../projects/yosyshq__picorv32.md): the core is primitive-free; only the board tops use `SB_IO` and `SB_SPRAM256KA`.
- [wren6991__smoldvi](../projects/wren6991__smoldvi.md): only `ddr_out` needs an `ODDRX1F` version.
{% endraw %}
