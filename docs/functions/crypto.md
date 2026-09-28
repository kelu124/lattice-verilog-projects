---
title: "Crypto and hashing"
parent: "Cores by function"
nav_order: 34
---
<!-- Generated from data/functions.json, data/cores.json, data/core_usage.json by .claude/skills/documentation/gen_site.py; do not edit. -->

{% raw %}
# Crypto and hashing

Hash and cipher cores.

| Core | Repository | Language | License | FPGA | Used by |
|---|---|---|---|---|---|
| [yaaes AES core (VHDL, cocotb/vunit tested)](#core-marph91-yaaes) ★ | [marph91__yaaes](https://github.com/marph91/yaaes) | VHDL | LGPL-3.0 | ECP5 | 0 |
| [AES / SHA-256 / DES crypto cores (greybadge25 uart coprocessor)](#core-greybadge25-aes-sha256-des) | [nusgreyhats__greybadge25](https://github.com/NUSGreyhats/greybadge25) | Verilog | OpenCores permissive redistribution clause | ECP5 | 0 |
| [Pipelined double-SHA256 hasher](#core-xtrinch-sha256-miner) | [xtrinch__fpga-bitcoin-miner](https://github.com/xtrinch/fpga-bitcoin-miner) | Verilog | MIT (LICENSE, root) | ECP5 | 1 |
| [Pruned 64-stage double-SHA256 miner pipeline](#core-williamsharkey-sha256-pruned) | [williamsharkey__pruned-sha256-miner](https://github.com/williamsharkey/Pruned-SHA256-Miner) | SystemVerilog | none found | any | 0 |
| [Ring-oscillator TRNG](#core-krishkc5-trng-ring-oscillator) | [krishkc5__trng-ring-oscillator](https://github.com/krishkc5/trng-ring-oscillator) | SystemVerilog | none found | ECP5 | 0 |
| [secworks AES-128/256 core (via ct-key)](#core-secworks-aes-ctkey) | [assured__ct-key](https://github.com/Assured/CT-key) | Verilog (core), Python/Migen (CSR… | BSD-2-Clause | any | 0 |
| [SRNG ring-oscillator TRNG + Blake2s DRBG](#core-secworks-cryptkey-srng) | [secworks__cryptkey](https://github.com/secworks/CrypTkey) | Verilog | BSD-2-Clause | ECP5 | 0 |

## Cores

### yaaes AES core (VHDL, cocotb/vunit tested) (best) {#core-marph91-yaaes}

AES-128/192/256 cipher core (key expansion + cipher datapath) built for ECP5 85F, with a VUnit/cocotb-based testbench suite for verification.

| | |
|---|---|
| Repository | [marph91__yaaes](https://github.com/marph91/yaaes): YAAES: VHDL AES-128/256 block cipher core |
| Files | [`src/aes.vhd`](https://github.com/marph91/yaaes/blob/43fdc855d783c4f4ca61f8a8ad64c60a798c119c/src/aes.vhd), [`src/cipher.vhd`](https://github.com/marph91/yaaes/blob/43fdc855d783c4f4ca61f8a8ad64c60a798c119c/src/cipher.vhd), [`src/key_expansion.vhd`](https://github.com/marph91/yaaes/blob/43fdc855d783c4f4ca61f8a8ad64c60a798c119c/src/key_expansion.vhd), [`src/aes_pkg.vhd`](https://github.com/marph91/yaaes/blob/43fdc855d783c4f4ca61f8a8ad64c60a798c119c/src/aes_pkg.vhd), [`src/input_conversion.vhd`](https://github.com/marph91/yaaes/blob/43fdc855d783c4f4ca61f8a8ad64c60a798c119c/src/input_conversion.vhd), [`src/output_conversion.vhd`](https://github.com/marph91/yaaes/blob/43fdc855d783c4f4ca61f8a8ad64c60a798c119c/src/output_conversion.vhd) |
| Top module | `aes` |
| Language | VHDL |
| License | LGPL-3.0 (LICENSE, root) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | VUnit testbench suite (sim/vunit/); self-checking per repo structure, not individually re-run here |

**On ULX3S:** Vendor-neutral VHDL; synth.sh targets nextpnr-ecp5 --85k --package CABGA381 which matches the ULX3S 85F.

### AES / SHA-256 / DES crypto cores (greybadge25 uart coprocessor) {#core-greybadge25-aes-sha256-des}

Bundle of three classic crypto cores (AES cipher/inverse-cipher, SHA-256 block processor, DES) wired to a UART coprocessor on the ECP5 25F greybadge25 badge.

| | |
|---|---|
| Repository | [nusgreyhats__greybadge25](https://github.com/NUSGreyhats/greybadge25): Greybadge25 |
| Files | [`firmware/ecp5/uart_coprocessor/src/aes/aes_cipher_top.v`](https://github.com/NUSGreyhats/greybadge25/blob/3ce9bfbf0061ee36e17dca1274c2f65ae9a5bb07/firmware/ecp5/uart_coprocessor/src/aes/aes_cipher_top.v), [`firmware/ecp5/uart_coprocessor/src/aes/aes_inv_cipher_top.v`](https://github.com/NUSGreyhats/greybadge25/blob/3ce9bfbf0061ee36e17dca1274c2f65ae9a5bb07/firmware/ecp5/uart_coprocessor/src/aes/aes_inv_cipher_top.v), [`firmware/ecp5/uart_coprocessor/src/aes/aes_key_expand_128.v`](https://github.com/NUSGreyhats/greybadge25/blob/3ce9bfbf0061ee36e17dca1274c2f65ae9a5bb07/firmware/ecp5/uart_coprocessor/src/aes/aes_key_expand_128.v), [`firmware/ecp5/main/src/computation/sha256.v`](https://github.com/NUSGreyhats/greybadge25/blob/3ce9bfbf0061ee36e17dca1274c2f65ae9a5bb07/firmware/ecp5/main/src/computation/sha256.v), [`firmware/ecp5/main/src/computation/tl_des.v`](https://github.com/NUSGreyhats/greybadge25/blob/3ce9bfbf0061ee36e17dca1274c2f65ae9a5bb07/firmware/ecp5/main/src/computation/tl_des.v) |
| Top module | `aes_cipher_top` |
| Language | Verilog |
| License | OpenCores permissive redistribution clause (in-file header, Rudolf Usselmann 2000-2002) for the AES core; sha256.v ported from github.com/russm/sha2-verilog (no separate header found); no repo-wide LICENSE file |
| FPGA / primitives | ECP5: none (portable) |
| Tests | none found in this pass |

**On ULX3S:** Built for ECP5 25F (--25k); review timing/reset behaviour before reuse per the catalogue note, and re-check licensing carefully since the repo itself carries no LICENSE file.

### Pipelined double-SHA256 hasher {#core-xtrinch-sha256-miner}

Pipelined, parametrically-unrolled double-SHA256 hasher (one 256-bit hash every LOOP cycles) originally for a bitcoin miner; pure portable Verilog.

| | |
|---|---|
| Repository | [xtrinch__fpga-bitcoin-miner](https://github.com/xtrinch/fpga-bitcoin-miner): Bitcoin miner: pipelined double-SHA256 FPGA miner |
| Files | [`src/sha256_transform.v`](https://github.com/xtrinch/fpga-bitcoin-miner/blob/7c9ca1c3776b533166c54d35ab7172ccb675a09c/src/sha256_transform.v), [`src/sha256_functions.v`](https://github.com/xtrinch/fpga-bitcoin-miner/blob/7c9ca1c3776b533166c54d35ab7172ccb675a09c/src/sha256_functions.v) |
| Top module | `sha256_transform` |
| Language | Verilog |
| License | MIT (LICENSE, root) |
| FPGA / primitives | ECP5: none (portable) |
| Tests | self-checking `make test-miner`/`make test-uart`/`make test-top` targets plus helpers/test_hasher.py |

**On ULX3S:** Built for the ECP5-EVN board (LFE5UM5G-85F, --um5g-85k); the hasher itself has no board dependency and drops onto ULX3S 85F.

**Used by 1 other catalogued repo** (file copies or module instances found by `scan_core_usage.py`; heuristic):

- [vmware-archive__cascade](https://github.com/vmware-archive/cascade) (instantiates [`share/cascade/test/benchmark/bitcoin/fpgaminer_top.v`](https://github.com/vmware-archive/cascade/blob/8b7dfdabfaa5db3aaedfaf71e0257d378b3c0737/share/cascade/test/benchmark/bitcoin/fpgaminer_top.v))

### Pruned 64-stage double-SHA256 miner pipeline {#core-williamsharkey-sha256-pruned}

Fully unrolled 64-round double-SHA256 pipeline pruned for Bitcoin mining (drops H0-H6 in the final round, single 1-bit 'hit' output instead of a 32-bit nonce). Plain SV, no vendor primitives; ECP5-85F PnR numbers claimed in README are unverified in this clone (see catalogue notes).

| | |
|---|---|
| Repository | [williamsharkey__pruned-sha256-miner](https://github.com/williamsharkey/Pruned-SHA256-Miner): Pruned 64-stage double-SHA256 Bitcoin miner pipeline for ULX3S ECP5-85F, single-bit hit-pulse output to… |
| Files | [`rtl/factory75_pruned.sv`](https://github.com/williamsharkey/Pruned-SHA256-Miner/blob/ea4a0f77febbc0d29c1a90de5f3d29e836770940/rtl/factory75_pruned.sv), [`rtl/formal75.sv`](https://github.com/williamsharkey/Pruned-SHA256-Miner/blob/ea4a0f77febbc0d29c1a90de5f3d29e836770940/rtl/formal75.sv) |
| Top module | `ulx3s_factory75` |
| Language | SystemVerilog |
| License | none found |
| FPGA / primitives | any: none (portable) |
| Tests | rtl/tb_factory75.sv, tb_stages75.sv, tb_benchmark.sv, tb_mining_sim.sv: present but no PASS/FAIL/assert found; rtl/formal75.sv SAT-miter flow (run.py) not runnable in this clone (missing copies/upstream-u2.sv) |

**On ULX3S:** Repo ships constraints/ulx3s-miner-v20.lpf, but run.py (the only build driver) references a missing sibling toolchain dir and missing scripts/copies/logs dirs, so the claimed 46.7MHz/61,830-LUT result cannot be reproduced as cloned.

### Ring-oscillator TRNG {#core-krishkc5-trng-ring-oscillator}

True-random-number-generator entropy core: 8 ring oscillators of varied inverter counts XORed and sampled through a sync chain.

| | |
|---|---|
| Repository | [krishkc5__trng-ring-oscillator](https://github.com/krishkc5/trng-ring-oscillator): True Random Number Generator using ring oscillators, SystemVerilog + Verilator/cocotb sim, Python entropy… |
| Files | [`rtl/ring_oscillator.sv`](https://github.com/krishkc5/trng-ring-oscillator/blob/446dcd058b693f415aabb7688a2475626ca07461/rtl/ring_oscillator.sv), [`rtl/trng_core.sv`](https://github.com/krishkc5/trng-ring-oscillator/blob/446dcd058b693f415aabb7688a2475626ca07461/rtl/trng_core.sv) |
| Top module | `trng_core` |
| Language | SystemVerilog |
| License | none found |
| FPGA / primitives | ECP5: none (portable) |
| Tests | none found in this pass |

**On ULX3S:** Built with `nextpnr-ecp5 --85k` by default (Makefile notes 12F/25F/45F are selectable); board-independent entropy source, not tied to a fixed FPGA size.

### secworks AES-128/256 core (via ct-key) {#core-secworks-aes-ctkey}

Classic secworks AES-128/256 core (encipher+decipher+key_mem+sbox), CSR-mapped over an 8-bit addr/data bus in ctkey's Migen wrapper (aes.py) via Instance("aes",...). Genuinely instantiated in ctkey's real ULX3S LiteX target.

| | |
|---|---|
| Repository | [assured__ct-key](https://github.com/Assured/CT-key): CT-key: LiteX/VexRiscv SoC with a Wishbone/CSR-mapped secworks AES core, real target for ULX3S |
| Files | [`ctkey_package/src/ctkey/cores/aes.py`](https://github.com/Assured/CT-key/blob/8a70cfeaf2a082874c693302d767636f63634b98/ctkey_package/src/ctkey/cores/aes.py), [`ctkey_package/src/ctkey/cores/aes/src/rtl/aes.v`](https://github.com/Assured/CT-key/blob/8a70cfeaf2a082874c693302d767636f63634b98/ctkey_package/src/ctkey/cores/aes/src/rtl/aes.v), [`ctkey_package/src/ctkey/cores/aes/src/rtl/aes_core.v`](https://github.com/Assured/CT-key/blob/8a70cfeaf2a082874c693302d767636f63634b98/ctkey_package/src/ctkey/cores/aes/src/rtl/aes_core.v), [`ctkey_package/src/ctkey/cores/aes/src/rtl/aes_key_mem.v`](https://github.com/Assured/CT-key/blob/8a70cfeaf2a082874c693302d767636f63634b98/ctkey_package/src/ctkey/cores/aes/src/rtl/aes_key_mem.v), [`ctkey_package/src/ctkey/cores/aes/src/rtl/aes_encipher_block.v`](https://github.com/Assured/CT-key/blob/8a70cfeaf2a082874c693302d767636f63634b98/ctkey_package/src/ctkey/cores/aes/src/rtl/aes_encipher_block.v), [`ctkey_package/src/ctkey/cores/aes/src/rtl/aes_decipher_block.v`](https://github.com/Assured/CT-key/blob/8a70cfeaf2a082874c693302d767636f63634b98/ctkey_package/src/ctkey/cores/aes/src/rtl/aes_decipher_block.v), [`ctkey_package/src/ctkey/cores/aes/src/rtl/aes_sbox.v`](https://github.com/Assured/CT-key/blob/8a70cfeaf2a082874c693302d767636f63634b98/ctkey_package/src/ctkey/cores/aes/src/rtl/aes_sbox.v), [`ctkey_package/src/ctkey/cores/aes/src/rtl/aes_inv_sbox.v`](https://github.com/Assured/CT-key/blob/8a70cfeaf2a082874c693302d767636f63634b98/ctkey_package/src/ctkey/cores/aes/src/rtl/aes_inv_sbox.v) |
| Top module | `aes` |
| Language | Verilog (core), Python/Migen (CSR wrapper) |
| License | BSD-2-Clause (ctkey_package/src/ctkey/cores/aes/LICENSE, Joachim Stromberg 2014) |
| FPGA / primitives | any: none (portable) |
| Tests | toolruns/Makefile core.sim/keymem.sim/encipher.sim/decipher.sim/top.sim (iverilog): src/tb/tb_aes_*.v - self-checking (error_ctr counter, $display ERROR on mismatch) |

**On ULX3S:** Already wired into a working LiteX SoC for radiona_ulx3s (ctkey_ulx3s.py, device=LFE5U-45F default); reuse the CSR wrapper pattern in aes.py or drop aes_core.v directly into any Wishbone/CSR SoC.

### SRNG ring-oscillator TRNG + Blake2s DRBG {#core-secworks-cryptkey-srng}

32x explicit LUT4 ring oscillators (trng.v) feed a von Neumann-conditioned entropy source that periodically reseeds a Blake2s-based hash DRBG (srng_core.v), with a stuck-source error check.

| | |
|---|---|
| Repository | [secworks__cryptkey](https://github.com/secworks/CrypTkey): CrypTkey: WIP port of the Tillitis TKey RISC-V security SoC |
| Files | [`cores/srng/rtl/srng.v`](https://github.com/secworks/CrypTkey/blob/70d36bb6017a3bc82d49e91711a4fb37dae917ca/cores/srng/rtl/srng.v), [`cores/srng/rtl/srng_core.v`](https://github.com/secworks/CrypTkey/blob/70d36bb6017a3bc82d49e91711a4fb37dae917ca/cores/srng/rtl/srng_core.v), [`cores/srng/rtl/trng.v`](https://github.com/secworks/CrypTkey/blob/70d36bb6017a3bc82d49e91711a4fb37dae917ca/cores/srng/rtl/trng.v), [`cores/srng/rtl/blake2s_core.v`](https://github.com/secworks/CrypTkey/blob/70d36bb6017a3bc82d49e91711a4fb37dae917ca/cores/srng/rtl/blake2s_core.v), [`cores/srng/rtl/blake2s_G.v`](https://github.com/secworks/CrypTkey/blob/70d36bb6017a3bc82d49e91711a4fb37dae917ca/cores/srng/rtl/blake2s_G.v), [`cores/srng/rtl/blake2s_m_select.v`](https://github.com/secworks/CrypTkey/blob/70d36bb6017a3bc82d49e91711a4fb37dae917ca/cores/srng/rtl/blake2s_m_select.v) |
| Top module | `srng` |
| Language | Verilog |
| License | BSD-2-Clause (repo LICENSE; file header cites Joachim Strombergson / Amagicom AB) |
| FPGA / primitives | ECP5: `LUT4` |
| Tests | cores/srng/tb: iverilog/verilator testbenches present (per scan_tests.sh); not independently re-run |

**On ULX3S:** Vendored from secworks' own CrypTech/TKey work; ring oscillators are LUT4-instantiated so they need re-checking (not just re-synthesizing) on non-ECP5 targets. Has its own ulx3s_v20.lpf and standalone fpga build under cores/srng/fpga/.

## Other catalogued projects

Catalogued repos tagged `crypto` (10) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
