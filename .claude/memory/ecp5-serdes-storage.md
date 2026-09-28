---
name: ecp5-serdes-storage
description: State of open gateware for SSD/PCIe/SATA over the ECP5-5G SERDES (surveyed 2026-09-28) — no open M.2/NVMe SSD design; LiteSATA works on ECPIX-5; PCIe is endpoint-only Gen1 x1 PoCs
metadata:
  type: project
---

Survey 2026-09-28 (47 GitHub searches, `data/pages/serdes-survey.json` → `docs/methodology/serdes-survey.md`):
- **No open design drives an M.2 SSD (NVMe or M.2-SATA) over the ECP5 SERDES.** NVMe needs a PCIe *root complex* +
  NVMe host; every open ECP5 PCIe stack is endpoint-only, Gen1 x1, experimental; LitePCIe has no ECP5 PHY
  (issue #20, bounty). No LFE5UM board wires an M-key M.2 slot to the FPGA SERDES: TrellisBoard and Logicbone have
  E-key M.2 (Wi-Fi key) on 2 SERDES lanes; Antmicro DC-SCM's M-key lanes go to the host edge, not the FPGA.
- **SATA works**: LiteSATA (`enjoy-digital__litesata`, `litesata/phy/ecp5sataphy.py` on liteiclink `SerDesECP5`)
  drives a SATA drive at Gen2 on **ECPIX-5** (LFE5UM5G), open toolchain; validated by upstream commit 0b7ce00
  (2026-07-30: IDENTIFY + 16 MiB BIST); `litex-boards lambdaconcept_ecpix5 --with-sata`. Not built here.
- Best PCIe blocks: zyp katsuo-pcie + litepcie-katsuo-poc (enumerates in lspci on Versa ECP5, Gen1 x1, no
  retransmit/flow control), ECP5-PCIe (Amaranth, L0 on ECP5-5G EVN), Yumewatari (original PHY). SGMII:
  sefbkn versa-ecp5-demo, kazkojima litex-lattice-ecp5-evn. All catalogued; function `serdes-links` in data/cores.json.
- **The ULX3S (LFE5U) has no SERDES**; emard ulx3s-misc `examples/serdes*` only work on the v3.1.4 prototype with a UM part.
- Nearest paths to an SSD: an M.2-SATA SSD via adapter on the ECPIX-5 SATA port (plausible, unreported); NVMe needs
  new root-complex + NVMe host work (E-key lanes, or ULX4M-LD CM4 PCIe lane — unverified idea).

Related: TinyFPGA EX was announced (LFE5U-25F/85F, LFE5UM5G-85F) but never shipped; no gateware exists
(`docs/methodology/boards3-survey.md`). See [[reusable-cores]], [[source-lists]].

**How to apply:** answer "SSD / PCIe / SATA on ECP5?" from this; re-run the survey before claiming nothing new exists.
