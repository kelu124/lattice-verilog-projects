---
title: "Ethernet"
parent: "Cores by function"
nav_order: 18
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# Ethernet

RMII/RGMII/SGMII MACs and IP/UDP stacks, PTP.

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [mii_ipoe ARP/IP/UDP/DHCP stack](#core-hdl4fpga-mii-ipoe) ★ | [hdl4fpga__hdl4fpga](https://github.com/hdl4fpga/hdl4fpga) | VHDL | MIT (LICENSE; header spot-checked on mii_ipoe.vhd) | any | 0 |
| [Gigabit RGMII MAC](#core-datanoisetv-eth-mac-rgmii) | [datanoisetv__colorlight-i9-aes67](https://github.com/DatanoiseTV/colorlight-i9-aes67) | Verilog | MIT (SPDX headers) | ECP5 | 2 |
| [MDIO Clause-22 management controller](#core-sefbkn-mdio) | [sefbkn__versa-ecp5-demo](https://github.com/sefbkn/versa-ecp5-demo) | Verilog | CERN-OHL-S-2.0 | any | 1 |
| [RMII hex-dump packet sniffer](#core-emard-eth-rmii-hexdemo) | [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc) | Verilog | none found | ECP5 | 0 |
| [kazkojima LiteEth SGMII PHY over ECP5 DCU (GBE mode)](#core-kazkojima-ecp5-sgmii) | [kazkojima__litex-lattice-ecp5-evn](https://github.com/kazkojima/litex-lattice-ecp5-evn) | Python (Migen) | BSD-2-Clause | ECP5 | 0 |

## Cores

### mii_ipoe ARP/IP/UDP/DHCP stack (best) {#core-hdl4fpga-mii-ipoe}

Full MII-level protocol stack (eth_rx/tx, ARP, IPv4, UDP, ICMP, DHCP client) built from library/mii/*.vhd, generic RMII/MII pad-independent.

| | |
|---|---|
| Repository | [hdl4fpga__hdl4fpga](https://github.com/hdl4fpga/hdl4fpga): hdl4fpga: portable VHDL library, ScopeIO oscilloscope, SDRAM graphics, eth/USB links |
| Files | [`library/mii/mii_ipoe.vhd`](https://github.com/hdl4fpga/hdl4fpga/blob/662986ba0f17b7ce3a066ddcb799d42fa1b24dea/library/mii/mii_ipoe.vhd) |
| Top module | `mii_ipoe` |
| Language | VHDL |
| License | MIT (LICENSE; header spot-checked on mii_ipoe.vhd) |
| FPGA / primitives | any: none (portable) |
| Tests | boards/ULX3S/testbenches/eth_tb.vhd (ModelSim/Aldec .do script, waveform-based) |

**On ULX3S:** This is the exact stack behind emard__ulx3s-bin's prebuilt DHCP+ping-responder bitstream on the ULX3S LAN8720 RMII PHY (GP/GN 9-13); pair with ulx3s-misc's examples/eth/rmii for the board-side pad wiring. Repo toolchain is Diamond-only, but this file has no vendor primitives.

Full review: [hdl4fpga__hdl4fpga](../projects/hdl4fpga__hdl4fpga.md).

### Gigabit RGMII MAC {#core-datanoisetv-eth-mac-rgmii}

Complete Gigabit Ethernet MAC with RGMII PHY interface, AXI-Stream data ports and PTP timestamp triggers.

| | |
|---|---|
| Repository | [datanoisetv__colorlight-i9-aes67](https://github.com/DatanoiseTV/colorlight-i9-aes67): AES67/RAVENNA audio-over-IP bridge for Colorlight i9 v7.2: hardware PTP |
| Files | [`rtl/eth/eth_mac.v`](https://github.com/DatanoiseTV/colorlight-i9-aes67/blob/71420b772d48409ae8e3a70c3103828495687737/rtl/eth/eth_mac.v), [`rtl/eth/rgmii_rx.v`](https://github.com/DatanoiseTV/colorlight-i9-aes67/blob/71420b772d48409ae8e3a70c3103828495687737/rtl/eth/rgmii_rx.v), [`rtl/eth/rgmii_tx.v`](https://github.com/DatanoiseTV/colorlight-i9-aes67/blob/71420b772d48409ae8e3a70c3103828495687737/rtl/eth/rgmii_tx.v) |
| Top module | `eth_mac` |
| Language | Verilog |
| License | MIT (SPDX headers) |
| FPGA / primitives | ECP5: `ODDRX1F` |
| Tests | sim/tb_ptp_clock.v (not eth_mac-specific; waveform-only, no assert/PASS-FAIL) |

**On ULX3S:** Built for a Colorlight i9 (LFE5U-45F); rgmii_tx.v genuinely instantiates ECP5 ODDRX1F, but rgmii_rx.v uses behavioral posedge/negedge sampling rather than a real IDDRX1F (comment says so explicitly) — verify RX timing before reuse.

**Used by 2 other catalogued repos** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [hdl4fpga__hdl4fpga](https://github.com/hdl4fpga/hdl4fpga) (instantiates [`boards/ULX4M_LD/apps/graphics.vhd`](https://github.com/hdl4fpga/hdl4fpga/blob/662986ba0f17b7ce3a066ddcb799d42fa1b24dea/boards/ULX4M_LD/apps/graphics.vhd))
- [sefbkn__versa-ecp5-demo](https://github.com/sefbkn/versa-ecp5-demo) (instantiates [`rtl/ethernet/rgmii/rgmii_port.v`](https://github.com/sefbkn/versa-ecp5-demo/blob/1d6d4cb535e11f935c1afa707b35ded5df4d658d/rtl/ethernet/rgmii/rgmii_port.v))

### MDIO Clause-22 management controller {#core-sefbkn-mdio}

IEEE 802.3 Clause-22 MDIO read/write controller plus a paged wrapper for 88E1512-style PHY register maps.

| | |
|---|---|
| Repository | [sefbkn__versa-ecp5-demo](https://github.com/sefbkn/versa-ecp5-demo): Versa ECP5-5G: dual-port Ethernet PHY passthrough bridge |
| Files | [`rtl/ethernet/mdio/mdio_master.v`](https://github.com/sefbkn/versa-ecp5-demo/blob/1d6d4cb535e11f935c1afa707b35ded5df4d658d/rtl/ethernet/mdio/mdio_master.v), [`rtl/ethernet/mdio/mdio_paged.v`](https://github.com/sefbkn/versa-ecp5-demo/blob/1d6d4cb535e11f935c1afa707b35ded5df4d658d/rtl/ethernet/mdio/mdio_paged.v) |
| Top module | `mdio_master` |
| Language | Verilog |
| License | CERN-OHL-S-2.0 (SPDX headers) |
| FPGA / primitives | any: none (portable) |
| Tests | sim/ has 1 iverilog tb file, not confirmed MDIO-specific |

**On ULX3S:** Built for a Lattice Versa ECP5-5G board (SGMII/RGMII bring-up demo); the MDIO logic itself is board-agnostic and reusable for any PHY needing register access over MDIO.

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [datanoisetv__colorlight-i9-aes67](https://github.com/DatanoiseTV/colorlight-i9-aes67) (instantiates [`rtl/aes67_top.v`](https://github.com/DatanoiseTV/colorlight-i9-aes67/blob/71420b772d48409ae8e3a70c3103828495687737/rtl/aes67_top.v))

### RMII hex-dump packet sniffer {#core-emard-eth-rmii-hexdemo}

Self-contained single-file RMII receiver that hex-dumps captured LAN8720 packets to OLED/DVI; includes an ARP-reply memory skeleton, not a full MAC.

| | |
|---|---|
| Repository | [emard__ulx3s-misc](https://github.com/emard/ulx3s-misc): ULX3S misc/advanced examples: EMARD's building-block library |
| Files | [`examples/eth/rmii/proj/top/top_eth_hex_demo.v`](https://github.com/emard/ulx3s-misc/blob/d0c6f15dd22608d15b60fdf3c3b3c16201eea0f6/examples/eth/rmii/proj/top/top_eth_hex_demo.v) |
| Top module | `top_eth_hex_demo` |
| Language | Verilog |
| License | none found |
| FPGA / primitives | ECP5: none (portable) |
| Tests | none found |

**On ULX3S:** Documents the exact ULX3S LAN8720 RMII pinout (gn9/gp10/gn10/gp13 TX, gp11/gn11/gp12/gn12 RX, gn13 MDIO) referenced by other RMII cores in this collection.

Full review: [emard__ulx3s-misc](../projects/emard__ulx3s-misc.md).

### kazkojima LiteEth SGMII PHY over ECP5 DCU (GBE mode) {#core-kazkojima-ecp5-sgmii}

SGMII (1000BASE-X) PHY built from Instance('DCUA', CHX_PROTOCOL='GBE'), a reduction of liteeth pcs_1000basex.py plus liteiclink serdes_ecp5.py for the DCU's Gigabit-Ethernet mode. Used on an ECP5-5G Evaluation Board with a TI DP83867S add-on to run a LiteX/linux-on-litex-vexriscv SoC over Ethernet.

| | |
|---|---|
| Repository | [kazkojima__litex-lattice-ecp5-evn](https://github.com/kazkojima/litex-lattice-ecp5-evn): LiteEth SGMII PHY |
| Files | [`liteeth/ecp5sgmii.py`](https://github.com/kazkojima/litex-lattice-ecp5-evn/blob/6c526658a7c1cc963e8bcaa6c45e3468f6123e1e/liteeth/ecp5sgmii.py) |
| Top module | `SGMIIECP5` |
| Language | Python (Migen) |
| License | BSD-2-Clause (file header: Copyright (c) 2019-2021 Florent Kermarrec, LiteEth) |
| FPGA / primitives | ECP5: `DCUA` |
| Tests | none found |

**On ULX3S:** ULX3S (LFE5U) has no SERDES; needs an ECP5 UM/UM5G part. Author calls the whole setup 'experimental'; validated only with a home-brewed DP83867S daughterboard, not a stock module.

## Other catalogued projects

Catalogued repos tagged `ethernet` (14) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
