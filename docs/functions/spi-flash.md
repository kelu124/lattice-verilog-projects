---
title: "SPI flash"
parent: "Cores by function"
nav_order: 11
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# SPI flash

SPI/QSPI flash readers, XIP controllers and flash writers.

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [spimemio SPI/QSPI flash XIP controller](#core-picorv32-spimemio) ★ | [yosyshq__picorv32](https://github.com/YosysHQ/picorv32) | Verilog | ISC (COPYING; per-file header) | any | 11 |
| [MappedSPIFlash read-only XIP driver](#core-mb-sat-mappedspiflash) | [mb-sat__ulx3s-longwave-sdr](https://github.com/mb-sat/ulx3s-longwave-sdr) | Verilog | GPL-3.0 (repo LICENSE) | any | 1 |
| [NEORV32 ULX3S XIP flash-execute top](#core-neorv32-ulx3s-xip) | [fedy0__neo](https://github.com/fedy0/neo) | VHDL | BSD-3-Clause | ECP5 | 0 |
| [qspi_phy_ecp5 QSPI flash PHY (ECP5-native)](#core-had2019-qspi-phy-ecp5) | [emard__had2019-playground](https://github.com/emard/had2019-playground) | Verilog | BSD-3-clause | ECP5 | 2 |
| [Wishbone Quad-SPI flash controller (Gisselquist-derived)](#core-emard-misc-wbqspiflash) | [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc) | Verilog | GPL-3.0 (Gisselquist Technology LLC 2015-2016,… | any | 0 |

## Cores

### spimemio SPI/QSPI flash XIP controller (best) {#core-picorv32-spimemio}

Memory-mapped SPI-flash execute-in-place controller from PicoSoC: no vendor primitives, expects four bidirectional flash_io[0:3] pins split into oe/do/di triples. Widely reused, well-tested reference XIP controller.

| | |
|---|---|
| Repository | [yosyshq__picorv32](https://github.com/YosysHQ/picorv32): PicoRV32: size-optimized RISC-V |
| Files | [`picosoc/spimemio.v`](https://github.com/YosysHQ/picorv32/blob/ef203c2b0a3fb793280f5114941416c425c5b461/picosoc/spimemio.v) |
| Top module | `spimemio` |
| Language | Verilog |
| License | ISC (COPYING; per-file header) |
| FPGA / primitives | any: none (portable) |
| Tests | root Makefile self-checking testbenches (test/test_wb/test_synth/...) exercise picosoc including spimemio via firmware; no standalone spimemio testbench found |

**On ULX3S:** Needs a board-side tristate wrapper (ECP5 generic inout/BB instead of the reference tops' iCE40 SB_IO) for the shared ULX3S config-flash pins.

Full review: [yosyshq__picorv32](../projects/yosyshq__picorv32.md).

**Used by 11 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [chipflow__example-socs](https://github.com/ChipFlow/example-socs) (instantiates [`my_design/design.py`](https://github.com/ChipFlow/example-socs/blob/e019daedd1a775735ff120363267046830c08edc/my_design/design.py))
- [gtjennings1__hyperbus](https://github.com/gtjennings1/HyperBUS) (instantiates [`riscv32/hardware/picosoc.v`](https://github.com/gtjennings1/HyperBUS/blob/37bf73d0f5f7884d007b5a20566508a292a3c11c/riscv32/hardware/picosoc.v))
- [im-tomu__foboot](https://github.com/im-tomu/foboot) (copies [`hw/rtl/spimemio.v`](https://github.com/im-tomu/foboot/blob/dfa09fc84b0acb4d9a2d409f3a381274a1551e9f/hw/rtl/spimemio.v))
- [im-tomu__fomu-workshop](https://github.com/im-tomu/fomu-workshop) (copies [`litex/rtl/spimemio.v`](https://github.com/im-tomu/fomu-workshop/blob/af55dff1ffdd7cd833ed4619295053c87f7a07a0/litex/rtl/spimemio.v))
- [kelu124__lit3rick](https://github.com/kelu124/lit3rick) (instantiates [`micropython/source/picosoc.v`](https://github.com/kelu124/lit3rick/blob/ca4ad983046943fae0694a609154839e8c051283/micropython/source/picosoc.v))
- [mkvenkit__learn_fpga](https://github.com/mkvenkit/learn_fpga) (instantiates [`ice40up5k/picosoc_gpio/picosoc.v`](https://github.com/mkvenkit/learn_fpga/blob/b4784c67b83344f7b2c4b01f3f8bf345c9c54faf/ice40up5k/picosoc_gpio/picosoc.v))
- [mmicko__fpga101-workshop](https://github.com/mmicko/fpga101-workshop) (instantiates [`tutorials/12-RiscV/picosoc.v`](https://github.com/mmicko/fpga101-workshop/blob/1f5d605bc158810148626df5261bf1dc87cf50a1/tutorials/12-RiscV/picosoc.v))
- [nklabs__libnklabs-ulx3s](https://github.com/nklabs/libnklabs-ulx3s) (instantiates [`rtl/bus_spiflash.v`](https://github.com/nklabs/libnklabs-ulx3s/blob/6b6a6b2c50cff5415666ab0a4351a33f036c1761/rtl/bus_spiflash.v))
- [rxrbln__picorv32](https://github.com/rxrbln/picorv32) (instantiates [`picosoc/picosoc.v`](https://github.com/rxrbln/picorv32/blob/c6886214f33a5d9a9ae9941c66275df115d80b17/picosoc/picosoc.v))
- [spritetm__hadbadge2019_fpgasoc](https://github.com/Spritetm/hadbadge2019_fpgasoc) (instantiates [`soc/picorv32/picosoc/picosoc.v`](https://github.com/Spritetm/hadbadge2019_fpgasoc/blob/6e706d52ecdc007e9179bda01d8eac60d55b7c45/soc/picorv32/picosoc/picosoc.v))
- [wuxx__icesugar](https://github.com/wuxx/icesugar) (instantiates [`src/advanced/picorv32/picosoc/picosoc.v`](https://github.com/wuxx/icesugar/blob/1ebe71bf448e33a1bccfa2db6730d59eafb6c390/src/advanced/picorv32/picosoc/picosoc.v))

### MappedSPIFlash read-only XIP driver {#core-mb-sat-mappedspiflash}

Minimal read-only SPI-flash-in-memory-space driver from Bruno Levy's FemtoRV32 project, vendored to run the FemtoRV32 core on the ULX3S 85F longwave-SDR design.

| | |
|---|---|
| Repository | [mb-sat__ulx3s-longwave-sdr](https://github.com/mb-sat/ulx3s-longwave-sdr): mb-sat/ulx3s-longwave-sdr: longwave/VLF direct-conversion SDR receiver for ULX3S 85F |
| Files | [`logic/common-verilog/MappedSPIFlash.v`](https://github.com/mb-sat/ulx3s-longwave-sdr/blob/1c2609dd20997b93c40331148adf972b99e33265/logic/common-verilog/MappedSPIFlash.v) |
| Top module | `MappedSPIFlash` |
| Language | Verilog |
| License | GPL-3.0 (repo LICENSE) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Read-only (no write/erase); smallest option here when a design only needs to execute firmware from flash.

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [brunolevy__learn-fpga](https://github.com/BrunoLevy/learn-fpga) (instantiates [`FemtoRV/RTL/femtosoc.v`](https://github.com/BrunoLevy/learn-fpga/blob/5c08c870315c09ccd9ec64ccde20ab3375b3f273/FemtoRV/RTL/femtosoc.v))

### NEORV32 ULX3S XIP flash-execute top {#core-neorv32-ulx3s-xip}

ULX3S 85F board top pairing the NEORV32 RISC-V core's built-in XIP module with the ECP5 config-flash pins (USRMCLK), so firmware executes directly from SPI flash instead of block RAM.

| | |
|---|---|
| Repository | [fedy0__neo](https://github.com/fedy0/neo): NEORV32 RISC-V SoC running on the ULX3S |
| Files | [`top/neorv32_ULX3S_xip.vhd`](https://github.com/fedy0/neo/blob/1fcd64bba20ddbd263b9274bccb89604c7252152/top/neorv32_ULX3S_xip.vhd) |
| Top module | `neorv32_ULX3S_xip` |
| Language | VHDL |
| License | BSD-3-Clause (NEORV32, Stephan Nolting 2023) |
| FPGA / primitives | ECP5: `USRMCLK` |
| Tests | none found |

**On ULX3S:** Built via a dedicated Makefile.xip target; simplest path to XIP-from-flash on ULX3S if already using NEORV32.

### qspi_phy_ecp5 QSPI flash PHY (ECP5-native) {#core-had2019-qspi-phy-ecp5}

ECP5-native QSPI flash PHY (drives USRMCLK and the shared config-flash IO through TRELLIS_IO/IFS1P3DX/OFS1P3DX) used by the PicoRV32-based USB DFU bootloader that ships bitstreams into ULX3S flash from the US2 port.

| | |
|---|---|
| Repository | [emard__had2019-playground](https://github.com/emard/had2019-playground): HAD2019 badge playground |
| Files | [`projects/bootloader/rtl/qspi_phy_ecp5.v`](https://github.com/emard/had2019-playground/blob/0723f2a536b20f26ec1b2d5cf1dcc2b5355b6808/projects/bootloader/rtl/qspi_phy_ecp5.v) |
| Top module | `qspi_phy_ecp5` |
| Language | Verilog |
| License | BSD-3-clause (Sylvain Munaut 2019, file header + LICENSE.bsd) |
| FPGA / primitives | ECP5: `USRMCLK`, `TRELLIS_IO`, `IFS1P3DX`, `OFS1P3DX` |
| Tests | none found |

**On ULX3S:** Proven in production on ULX3S (emard's DFU bootloader, 1d50:614b); pairs with picorv32/picosoc for a full XIP+DFU stack.

**Used by 2 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [smunaut__had2019-playground](https://github.com/smunaut/had2019-playground) (instantiates [`projects/bootloader/rtl/top.v`](https://github.com/smunaut/had2019-playground/blob/9bd9aa38ae1e77eaa9e8a7870beefb1a344baec7/projects/bootloader/rtl/top.v))
- [ulx3s__hazard3-doom](https://github.com/ulx3s/Hazard3-Doom) (instantiates [`bootloader/rtl/top-ulx3s.v`](https://github.com/ulx3s/Hazard3-Doom/blob/42621599f78f7ce3bd51fcc6b95a56ba83e31279/bootloader/rtl/top-ulx3s.v))

### Wishbone Quad-SPI flash controller (Gisselquist-derived) {#core-emard-misc-wbqspiflash}

ZipCPU/Gisselquist eqspiflash core (originally for the Arty board) wrapped as a Wishbone slave (wbqspiflash), ported into EMARD's ULX3S example library with read/write/erase register control and XIP support.

| | |
|---|---|
| Repository | [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc): ULX3S misc/advanced examples: EMARD's building-block library |
| Files | [`examples/qspi/hdl/wbspiflash.v`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/qspi/hdl/wbspiflash.v), [`examples/qspi/hdl/eqspiflash.v`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/qspi/hdl/eqspiflash.v), [`examples/qspi/hdl/llqspi.v`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/qspi/hdl/llqspi.v) |
| Top module | `wbqspiflash` |
| Language | Verilog |
| License | GPL-3.0 (Gisselquist Technology LLC 2015-2016, file header) |
| FPGA / primitives | any: none (portable) |
| Tests | bench/busmaster.v simulation harness (not confirmed self-checking) |

**On ULX3S:** GPL-3.0 copyleft; has a bench/busmaster.v simulation harness for standalone verification before wiring into a SoC.

Full review: [emard__ulx3s-misc](../projects/emard__ulx3s-misc.md).

## Other catalogued projects

Catalogued repos tagged `flash-spi` (58) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
