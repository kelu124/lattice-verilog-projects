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
| [Pipelined double-SHA256 hasher](#core-xtrinch-sha256-miner) | [xtrinch__fpga-bitcoin-miner](https://github.com/xtrinch/fpga-bitcoin-miner) | Verilog | MIT (LICENSE, root) | ECP5 | 0 |
| [Ring-oscillator TRNG](#core-krishkc5-trng-ring-oscillator) | [krishkc5__trng-ring-oscillator](https://github.com/krishkc5/trng-ring-oscillator) | SystemVerilog | none found | ECP5 | 0 |

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

## Other catalogued projects

Catalogued repos tagged `crypto` (7) are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).
{% endraw %}
