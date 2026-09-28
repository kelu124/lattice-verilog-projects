---
title: "RISC-V CPUs and SoCs"
parent: "Cores by function"
nav_order: 28
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# RISC-V CPUs and SoCs

RISC-V cores and small SoCs.

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [PicoRV32 RISC-V core](#core-yosyshq-picorv32) ★ | [yosyshq__picorv32](https://github.com/YosysHQ/picorv32) | Verilog | ISC (COPYING) | any | 26 |
| [f32c RISC-V/MIPS-compatible core](#core-f32c-core) | [f32c__f32c](https://github.com/f32c/f32c) | VHDL | BSD-2-Clause | any | 0 |
| [FPGA 101 PicoSoC with LCD text console and MicroPython](#core-mmicko-fpga101-picosoc) | [mmicko__fpga101-workshop](https://github.com/mmicko/fpga101-workshop) | Verilog, C | MIT (repo LICENSE); z_picorv32.v ISC; MicroPython… | iCE40 | 3 |
| [Hazard3 RV32IMAC core](#core-wren6991-hazard3) | [wren6991__hazard3](https://github.com/Wren6991/Hazard3) | Verilog | Apache-2.0 | any | 1 |
| [KianV RV32IMA+Sv32 core (Linux-capable)](#core-kianv-sv32-core) | [splinedrive__kianriscv](https://github.com/splinedrive/kianRiscV) | Verilog | Apache-2.0 | any | 0 |
| [NEORV32 RV32 core (VHDL)](#core-stnolting-neorv32) | [stnolting__neorv32](https://github.com/stnolting/neorv32) | VHDL (+ generated Verilog wrapper in… | BSD-3-Clause | any | 0 |
| [VexRiscv (SpinalHDL-generated Verilog)](#core-rschlaikjer-vexriscv) | [rschlaikjer__fpga-3-softcores](https://github.com/rschlaikjer/fpga-3-softcores) | Verilog (SpinalHDL-generated) | MIT (upstream VexRiscv/SpinalHDL project; repo… | any | 14 |

## Cores

### PicoRV32 RISC-V core (best) {#core-yosyshq-picorv32}

Single-file RV32I(MC) core, board- and vendor-agnostic, the most-reused RISC-V core in the collection (had2019/hazard3-doom bootloaders, hadbadge2019, wuxx__icesugar, racerxdl__colorlight-picorv32, nklabs, lawrie examples...).

| | |
|---|---|
| Repository | [yosyshq__picorv32](https://github.com/YosysHQ/picorv32): PicoRV32: size-optimized RISC-V |
| Files | [`picorv32.v`](https://github.com/YosysHQ/picorv32/blob/ef203c2b0a3fb793280f5114941416c425c5b461/picorv32.v) |
| Top module | `picorv32` |
| Language | Verilog |
| License | ISC (COPYING) |
| FPGA / primitives | any: none (portable) |
| Tests | self-checking: make test/test_wb/test_ez/test_axi (iverilog) and test_verilator, magic-MMIO pass/fail check |

**On ULX3S:** No board dependency; wrap with picosoc.v-style memory-mapped peripherals and a BRAM/flash for firmware.

Full review: [yosyshq__picorv32](../projects/yosyshq__picorv32.md).

**Used by 26 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [badgeteam__mch2022-firmware-ice40](https://github.com/badgeteam/mch2022-firmware-ice40) (instantiates [`projects/selftest/rtl/picorv32.v`](https://github.com/badgeteam/mch2022-firmware-ice40/blob/ce6473addcf6066cada7d80d8ba352f52173d01d/projects/selftest/rtl/picorv32.v))
- [cliffordwolf__icotools](https://github.com/cliffordwolf/icotools) (instantiates [`icosoc/common/picorv32.v`](https://github.com/cliffordwolf/icotools/blob/9c6185bad15323e5982b68e60923aaea22b074d4/icosoc/common/picorv32.v))
- [dan-rodrigues__icestation-32](https://github.com/dan-rodrigues/icestation-32) (instantiates [`hardware/ics32.v`](https://github.com/dan-rodrigues/icestation-32/blob/55214d79f74a547dedb54f99cb2fad431b7ac277/hardware/ics32.v))
- [emard__had2019-playground](https://github.com/emard/had2019-playground) (instantiates [`projects/bootloader/rtl/picorv32.v`](https://github.com/emard/had2019-playground/blob/0723f2a536b20f26ec1b2d5cf1dcc2b5355b6808/projects/bootloader/rtl/picorv32.v))
- [emeb__up5k_osc](https://github.com/emeb/up5k_osc) (instantiates [`gateware/riscv/src/system.v`](https://github.com/emeb/up5k_osc/blob/a24453f385d57726643c7c1ee87937a842b78f8d/gateware/riscv/src/system.v))
- [evansm7__arcdvi](https://github.com/evansm7/ArcDVI) (instantiates [`external-src/picorv32.v`](https://github.com/evansm7/ArcDVI/blob/6640691c6862ca8949a7f2bb37b2ce00c18f90ab/external-src/picorv32.v))
- [gtjennings1__hyperbus](https://github.com/gtjennings1/HyperBUS) (instantiates [`riscv32/hardware/picosoc.v`](https://github.com/gtjennings1/HyperBUS/blob/37bf73d0f5f7884d007b5a20566508a292a3c11c/riscv32/hardware/picosoc.v))
- [icebreaker-fpga__icetwang](https://codeberg.org/icebreaker-fpga/icetwang) (instantiates [`soc/ice-twang/rtl/picorv32.v`](https://codeberg.org/icebreaker-fpga/icetwang/src/commit/a4915ff538be621d8cab4a9d82c555ee8627e0c3/soc/ice-twang/rtl/picorv32.v))
- [lawrie__ulx3s_examples](https://github.com/lawrie/ulx3s_examples) (instantiates [`hdmi/menu/attosoc.v`](https://github.com/lawrie/ulx3s_examples/blob/b6ff00099265401fef4843e4e89c2ac54254c95f/hdmi/menu/attosoc.v))
- [lawrie__ulx4m_examples](https://github.com/lawrie/ulx4m_examples) (instantiates [`hdmi/menu/attosoc.v`](https://github.com/lawrie/ulx4m_examples/blob/415ee5309545da06b1bda7bfe7ec3a1c65a5376c/hdmi/menu/attosoc.v))
- [machdyne__zeitlos](https://github.com/machdyne/zeitlos) (instantiates [`rtl/cpu/picorv32/picorv32.v`](https://github.com/machdyne/zeitlos/blob/a7e7e85ee0ad1fd0cfff4129e24b2aa528d444e8/rtl/cpu/picorv32/picorv32.v))
- [mkvenkit__learn_fpga](https://github.com/mkvenkit/learn_fpga) (instantiates [`ice40up5k/picosoc_gpio/picosoc.v`](https://github.com/mkvenkit/learn_fpga/blob/b4784c67b83344f7b2c4b01f3f8bf345c9c54faf/ice40up5k/picosoc_gpio/picosoc.v))
- [mmicko__fpga101-workshop](https://github.com/mmicko/fpga101-workshop) (instantiates [`tutorials/12-RiscV/picosoc.v`](https://github.com/mmicko/fpga101-workshop/blob/1f5d605bc158810148626df5261bf1dc87cf50a1/tutorials/12-RiscV/picosoc.v))
- [nklabs__libnklabs-ulx3s](https://github.com/nklabs/libnklabs-ulx3s) (instantiates [`rtl/picorv32.v`](https://github.com/nklabs/libnklabs-ulx3s/blob/6b6a6b2c50cff5415666ab0a4351a33f036c1761/rtl/picorv32.v))
- [nullobject__riscv-ulx3s](https://github.com/nullobject/riscv-ulx3s) (instantiates [`hdl/picorv32.v`](https://github.com/nullobject/riscv-ulx3s/blob/f344cef2a29b795cfd3ef4596277d61df9954ab9/hdl/picorv32.v))
- … and 11 more (see `data/core_usage.json`)

### f32c RISC-V/MIPS-compatible core {#core-f32c-core}

Pipelined core that decodes either RISC-V (RV32IM) or a MIPS-compatible ISA (MI32) at build time (idecode_rv32.vhd/idecode_mi32.vhd), backing an entire SoC family (UART/SDRAM/DVI/USB/audio) proven across ULX3S 12F-85F for over a decade.

| | |
|---|---|
| Repository | [f32c__f32c](https://github.com/f32c/f32c): f32c: retargetable RISC-V/MIPS 32-bit soft CPU + SoC library |
| Files | [`rtl/cpu/f32c_core.vhd`](https://github.com/f32c/f32c/blob/7dbf56d42a94ae599eabfd1e7fa15db14a10afd7/rtl/cpu/f32c_core.vhd), [`rtl/cpu/idecode_rv32.vhd`](https://github.com/f32c/f32c/blob/7dbf56d42a94ae599eabfd1e7fa15db14a10afd7/rtl/cpu/idecode_rv32.vhd), [`rtl/cpu/idecode_mi32.vhd`](https://github.com/f32c/f32c/blob/7dbf56d42a94ae599eabfd1e7fa15db14a10afd7/rtl/cpu/idecode_mi32.vhd) |
| Top module | `f32c_core` |
| Language | VHDL |
| License | BSD-2-Clause (most files, per docs/projects/f32c__f32c.md) |
| FPGA / primitives | any: none (portable) |
| Tests | none found |

**On ULX3S:** Select ISA via the defs_f32c.vhd generic; comes with its own SoC glue, not a bare drop-in CPU.

Full review: [f32c__f32c](../projects/f32c__f32c.md).

### FPGA 101 PicoSoC with LCD text console and MicroPython {#core-mmicko-fpga101-picosoc}

PicoRV32 PicoSoC for the UP5K badge: 128 KB SPRAM main memory, XIP flash, UART, memory-mapped text-mode video on the parallel LCD; firmware examples and a MicroPython port (board LCD/LED/switch modules).

| | |
|---|---|
| Repository | [mmicko__fpga101-workshop](https://github.com/mmicko/fpga101-workshop): FPGA 101 workshop |
| Files | [`tutorials/12-RiscV/top.v`](https://github.com/mmicko/fpga101-workshop/blob/1f5d605bc158810148626df5261bf1dc87cf50a1/tutorials/12-RiscV/top.v), [`tutorials/12-RiscV/picosoc.v`](https://github.com/mmicko/fpga101-workshop/blob/1f5d605bc158810148626df5261bf1dc87cf50a1/tutorials/12-RiscV/picosoc.v), [`tutorials/12-RiscV/up_spram.v`](https://github.com/mmicko/fpga101-workshop/blob/1f5d605bc158810148626df5261bf1dc87cf50a1/tutorials/12-RiscV/up_spram.v), [`tutorials/12-RiscV/video.v`](https://github.com/mmicko/fpga101-workshop/blob/1f5d605bc158810148626df5261bf1dc87cf50a1/tutorials/12-RiscV/video.v), [`tutorials/12-RiscV/simpleuart.v`](https://github.com/mmicko/fpga101-workshop/blob/1f5d605bc158810148626df5261bf1dc87cf50a1/tutorials/12-RiscV/simpleuart.v), [`tutorials/12-RiscV/02-Micropython/ports/picorv32`](https://github.com/mmicko/fpga101-workshop/tree/1f5d605bc158810148626df5261bf1dc87cf50a1/tutorials/12-RiscV/02-Micropython/ports/picorv32) |
| Top module | `top` |
| Language | Verilog, C |
| License | MIT (repo LICENSE); z_picorv32.v ISC; MicroPython MIT |
| FPGA / primitives | iCE40: `SB_SPRAM256KA`, `SB_PLL40_CORE`, `SB_IO`, `SB_HFOSC` |
| Tests | none found |

**On ULX3S:** Replace SB_SPRAM256KA with DP16KD/SDRAM, SB_PLL40_CORE with EHXPLLL, LCD video with a DVI path; the ULX3S follow-up is ulx3s__fpga-odysseus tutorials/08-RISCV.

Full review: [mmicko__fpga101-workshop](../projects/mmicko__fpga101-workshop.md).

**Used by 3 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [daveshah1__up5k-demos](https://github.com/daveshah1/up5k-demos) (instantiates [`nes/cart_mem.v`](https://github.com/daveshah1/up5k-demos/blob/d85f0516f013a6a026946afc386196b1b2ac1e4e/nes/cart_mem.v))
- [wifiboy__ok-ice40pro](https://github.com/WiFiBoy/OK-iCE40Pro) (instantiates [`ok-nes-vga-src/cart_mem.v`](https://github.com/WiFiBoy/OK-iCE40Pro/blob/01c99298f8b059da09a72dd4b3286d9b0a96fe95/ok-nes-vga-src/cart_mem.v))
- [wuxx__icesugar](https://github.com/wuxx/icesugar) (instantiates [`src/advanced/up5k-demos/nes/cart_mem.v`](https://github.com/wuxx/icesugar/blob/1ebe71bf448e33a1bccfa2db6730d59eafb6c390/src/advanced/up5k-demos/nes/cart_mem.v))

### Hazard3 RV32IMAC core {#core-wren6991-hazard3}

Pipelined RV32IMAC core with CSR/PMP/debug support, board-agnostic; the ulx3s__hazard3 build validates it on real ULX3S 85F and ULX4M-LD hardware with documented Fmax/build steps.

| | |
|---|---|
| Repository | [wren6991__hazard3](https://github.com/Wren6991/Hazard3): Hazard3: 3-stage RV32IMACZb* core with debug, example_soc synthesizable for ULX3S |
| Files | [`hdl/hazard3_core.v`](https://github.com/Wren6991/Hazard3/blob/8af992930f71a69b0e06c38734c1094f41a05ca0/hdl/hazard3_core.v), [`hdl/hazard3_csr.v`](https://github.com/Wren6991/Hazard3/blob/8af992930f71a69b0e06c38734c1094f41a05ca0/hdl/hazard3_csr.v), [`hdl/hazard3_pmp.v`](https://github.com/Wren6991/Hazard3/blob/8af992930f71a69b0e06c38734c1094f41a05ca0/hdl/hazard3_pmp.v) |
| Top module | `hazard3_core` |
| Language | Verilog |
| License | Apache-2.0 (root LICENSE) |
| FPGA / primitives | any: none (portable) |
| Tests | self-checking: test/sim/test.py via cxxrtl, PASS/FAIL + CPU exit code |

**On ULX3S:** 12F is too small (BRAM); use 85F. See ulx3s__hazard3/doc/ulx3s-ulx4m-build-and-validation.md.

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [ulx3s__hazard3](https://github.com/ulx3s/Hazard3) (instantiates [`hdl/hazard3_core.v`](https://github.com/ulx3s/Hazard3/blob/3c0aca063517bb7fdbe869019c984954c7dd5c97/hdl/hazard3_core.v))

### KianV RV32IMA+Sv32 core (Linux-capable) {#core-kianv-sv32-core}

Standalone SoC-independent RV32IMA core with an Sv32 MMU, the CPU used by splinedrive's Linux-on-ULX3S SoC; reusable on its own wherever an MMU-capable RV32 core is needed, not just with kianriscv's own bus.

| | |
|---|---|
| Repository | [splinedrive__kianriscv](https://github.com/splinedrive/kianRiscV): KianV RV32IMA SV32 Linux SoCs |
| Files | [`linux_socs/LinuxSoC_v2/engineering/kianv-rv32-linuxcore/kianv_sv32.v`](https://github.com/splinedrive/kianRiscV/blob/da994e6c25b0667d6579922f4bab8d800d19e944/linux_socs/LinuxSoC_v2/engineering/kianv-rv32-linuxcore/kianv_sv32.v) |
| Top module | `kianv_sv32` |
| Language | Verilog |
| License | Apache-2.0 (SPDX header in file) |
| FPGA / primitives | any: none (portable) |
| Tests | 1 tb file present (not confirmed self-checking) |

**On ULX3S:** Pair with the repo's sdram/icache/dcache/clint/plic modules for a full SoC (85F default).

### NEORV32 RV32 core (VHDL) {#core-stnolting-neorv32}

Full-featured RV32 microcontroller core (CSR, on-chip debugger, rich peripheral set), vendor-agnostic; stnolting__neorv32-setups provides a generic open-toolchain osflow that builds it for ULX3S (BOARD=ULX3S).

| | |
|---|---|
| Repository | [stnolting__neorv32](https://github.com/stnolting/neorv32): NEORV32 RISC-V microcontroller SoC |
| Files | [`rtl/core`](https://github.com/stnolting/neorv32/tree/90a4c8675de567c67b385cfa7f3441cec13a63cc/rtl/core) |
| Top module | `neorv32_top` |
| Language | VHDL (+ generated Verilog wrapper in rtl/verilog) |
| License | BSD-3-Clause |
| FPGA / primitives | any: none (portable) |
| Tests | self-checking: make -C rtl/verilog sim (ghdl->Verilog, checks for 'Simulation successful!' vs timeout) |

**On ULX3S:** No ULX3S target ships inside this repo itself; use the neorv32-setups osflow or fedy0__neo's neorv32_ULX3S_BoardTop_MinimalBoot.vhd top.

### VexRiscv (SpinalHDL-generated Verilog) {#core-rschlaikjer-vexriscv}

Vendored single-file Verilog output of a VexRiscv RV32 configuration, wired to a Wishbone SoC in this repo; the same generate-a-.v-snapshot pattern also appears in hanseo03__ulx3s-vexriscv-soc and thorkn's ULX3S VexRiscv examples.

| | |
|---|---|
| Repository | [rschlaikjer__fpga-3-softcores](https://github.com/rschlaikjer/fpga-3-softcores): fpga-3-softcores: VexRiscv Wishbone SoC demo |
| Files | [`vendor/vexriscv/VexRiscv.v`](https://github.com/rschlaikjer/fpga-3-softcores/blob/6ccc8ac55f16ffcf17cef1d831714142ab64f27b/vendor/vexriscv/VexRiscv.v) |
| Top module | `VexRiscv` |
| Language | Verilog (SpinalHDL-generated) |
| License | MIT (upstream VexRiscv/SpinalHDL project; repo LICENSE.md is MIT, no per-file header on the generated .v) |
| FPGA / primitives | any: none (portable) |
| Tests | waveform tb in ./test, ./sim (8 files, not confirmed self-checking) |

**On ULX3S:** Regenerate with GenVexRiscv.scala for a different pipeline/extension config; the checked-in .v is a fixed snapshot.

**Used by 14 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [badgeteam__mch2022-firmware-ice40](https://github.com/badgeteam/mch2022-firmware-ice40) (instantiates [`projects/riscv_doom/rtl/top.v`](https://github.com/badgeteam/mch2022-firmware-ice40/blob/ce6473addcf6066cada7d80d8ba352f52173d01d/projects/riscv_doom/rtl/top.v))
- [dan-rodrigues__icestation-32](https://github.com/dan-rodrigues/icestation-32) (instantiates [`hardware/vexriscv/vexriscv_shared_bus.v`](https://github.com/dan-rodrigues/icestation-32/blob/55214d79f74a547dedb54f99cb2fad431b7ac277/hardware/vexriscv/vexriscv_shared_bus.v))
- [hanseo03__ulx3s-vexriscv-soc](https://github.com/hanseo03/ulx3s-vexriscv-soc) (instantiates [`GenMyVexRiscv.scala`](https://github.com/hanseo03/ulx3s-vexriscv-soc/blob/29b4f43f3b5b74bf2ccac97ed8d64687455fd2e1/GenMyVexRiscv.scala))
- [mcejp__poly94](https://github.com/mcejp/Poly94) (instantiates [`GenPoly94Cpu.scala`](https://github.com/mcejp/Poly94/blob/e2fa3d9406ee09760004d1ff97d4125825c2d345/GenPoly94Cpu.scala))
- [sefbkn__versa-ecp5-demo](https://github.com/sefbkn/versa-ecp5-demo) (instantiates [`rtl/soc/control_soc.v`](https://github.com/sefbkn/versa-ecp5-demo/blob/1d6d4cb535e11f935c1afa707b35ded5df4d658d/rtl/soc/control_soc.v))
- [smunaut__ice40-playground](https://github.com/smunaut/ice40-playground) (instantiates [`projects/riscv_doom/rtl/top.v`](https://github.com/smunaut/ice40-playground/blob/d2fa0050129c14a7fc42f64f115366f6f2a51669/projects/riscv_doom/rtl/top.v))
- [smunaut__ice40linux](https://github.com/smunaut/iCE40linux) (instantiates [`gateware/riscv_linux/rtl/top.v`](https://github.com/smunaut/iCE40linux/blob/16bc38fd181ddba8074f68da162cc35a802ec84b/gateware/riscv_linux/rtl/top.v))
- [smunaut__mch2022-ice40](https://github.com/smunaut/mch2022-ice40) (instantiates [`projects/riscv_doom/rtl/top.v`](https://github.com/smunaut/mch2022-ice40/blob/52e220eec7f833bfa6237bf227cd4795ddbdfe0a/projects/riscv_doom/rtl/top.v))
- [spinalhdl__saxonsoc](https://github.com/SpinalHDL/SaxonSoc) (instantiates [`hardware/deprecated/ice40up5kbevn/Ice40up5kbevnNoXip.scala`](https://github.com/SpinalHDL/SaxonSoc/blob/227b8686b734c7995b10ce81e193a01b010d2407/hardware/deprecated/ice40up5kbevn/Ice40up5kbevnNoXip.scala))
- [thorkn__vexriscv-ulx3s-helloworld](https://github.com/ThorKn/vexriscv-ulx3s-helloworld) (instantiates [`vexriscv/src/main/scala/vexriscv/TestsWorkspace.scala`](https://github.com/ThorKn/vexriscv-ulx3s-helloworld/blob/9987abab9256daba513aff66a66298a32006abcd/vexriscv/src/main/scala/vexriscv/TestsWorkspace.scala))
- [thorkn__vexriscv-ulx3s-simple-plugin](https://github.com/ThorKn/vexriscv-ulx3s-simple-plugin) (instantiates [`vexriscv/src/main/scala/vexriscv/VexRiscv.scala`](https://github.com/ThorKn/vexriscv-ulx3s-simple-plugin/blob/06606ec4dbfd5bf9748ac6fcbe3be3340cbe3469/vexriscv/src/main/scala/vexriscv/VexRiscv.scala))
- [ulx3s__hazard3](https://github.com/ulx3s/Hazard3) (instantiates [`example_soc/third_party/LiteDRAM/generated-vexrisc/litedram_ulx4m_cpu.v`](https://github.com/ulx3s/Hazard3/blob/3c0aca063517bb7fdbe869019c984954c7dd5c97/example_soc/third_party/LiteDRAM/generated-vexrisc/litedram_ulx4m_cpu.v))
- [wuxx__icesugar-pro](https://github.com/wuxx/icesugar-pro) (instantiates [`src/litex_linux/top.v`](https://github.com/wuxx/icesugar-pro/blob/087e48d9e0b0a0168ce165a961cba306335c4cf2/src/litex_linux/top.v))
- [zeldin__icegdrom](https://github.com/zeldin/iceGDROM) (instantiates [`fpga/source/vexriscv/vexriscv_wrapper.v`](https://github.com/zeldin/iceGDROM/blob/80a9fa6c8f287ae26b7a5ffd3c6002794bb29ae0/fpga/source/vexriscv/vexriscv_wrapper.v))

## Other catalogued projects

Catalogued repos tagged `soc-cpu` (130) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
