# Core-record brief for agents (ulx3s-klod)

Give this file to an agent with the function ids (or repos) to cover and an output path in the scratchpad.
The orchestrator appends the records to `data/cores.json` after validating them, then runs `make check usage docs`.

Repo: /home/kelu/projets/ulx3s-klod — a knowledge base of FPGA gateware for the ULX3S (Lattice ECP5, 25 MHz clock,
SDR SDRAM, GPDI HDMI port, ESP32, US2 USB, SD card, MAX11125 ADC, OLED header) and other small Lattice boards (ECP5,
iCE40 UP5K, iCE40 HX8K/HX4K). Its public site will present **reusable cores organised by function**, each linking to
the original files upstream, plus the projects that use them.

Inputs (read these first):
- `data/functions.json` — the function ids (use ONLY these ids).
- `.claude/memory/reusable-cores.md` — the current table of best cores (starting point; verify it).
- `data/catalogue.json` — all catalogued repos; the `functions` (tags), `reuse`, `license`, `fpga` fields point to candidate cores
  (e.g. `python3 -c` scripts filtering repos whose tags match your functions, then read their `reuse` field).
- `docs/projects/*.md` — 18 in-depth reviews with "Reusable blocks" tables (verified module/primitive/license facts).
- The clones in `original_sources/<slug>/` (READ-ONLY: never edit, build, or run anything there; read-only commands only).
  Non-gateware files were deleted locally ("pruned"): ignore deletions.

Task: for each function id you are given, pick **1 best core and up to 5 alternatives** from the cloned repos. Prefer:
proven on ULX3S/ECP5, open toolchain, self-contained, permissive license, tests. Include iCE40 cores when they are the
best of their kind (say which primitives need porting). For a function where the collection has nothing good, write
fewer entries; never invent. Also keep "whole-system" entries only when the function is itself a system (cpu, linux).

Output: a JSON array (UTF-8) written to the output file you are given. One object per core:
```json
{
 "id": "emard-ecp5pll",                      // short unique kebab-case id
 "name": "ecp5pll parametric PLL",            // human name
 "functions": ["pll-clock"],                  // ids from data/functions.json (first = main)
 "rank": "best",                              // "best" (one per function) or "alternative"
 "repo": "emard__ulx3s-misc",                 // slug in data/catalogue.json
 "files": ["examples/ecp5pll/hdl/sv/ecp5pll.sv", "examples/ecp5pll/hdl/vhd/ecp5pll.vhd"],  // paths relative to the repo root, files or dirs; MUST exist in the clone
 "top": "ecp5pll",                            // top module/entity name ("" if n/a)
 "language": "SystemVerilog, VHDL",
 "license": "BSD-2-Clause (file header)",     // as verified in the file(s); "none found" if none
 "fpga": "ECP5",                              // "any" (no vendor primitives) | "ECP5" | "iCE40" | "Xilinx" | ...
 "primitives": ["EHXPLLL"],                   // vendor primitives instantiated; [] if none
 "summary": "Computes EHXPLLL dividers from requested frequencies at elaboration time; up to 4 outputs with phase.",
 "ulx3s_notes": "Drop-in on ULX3S: in_hz=25000000.",   // what to change for a ULX3S design (short)
 "tests": "none found",                       // self-checking tb / formal / waveform-only / none found (short, with path)
 "usage_patterns": {"files": ["ecp5pll.sv", "ecp5pll.vhd"], "modules": ["ecp5pll"]}
}
```
`usage_patterns` is used by a scanner to find OTHER repos in the collection that copy or instantiate this core:
`files` = distinctive file basenames (avoid generic names like top.v, uart.v, pll.v, sdram.v unless nothing better),
`modules` = distinctive module/entity names (avoid generic ones like `uart_tx`, `fifo`, `top`). Leave a list empty
rather than put a generic name in it.

Rules: facts only, cite by path; verify every `files` path exists (`ls`), verify license from the file header or the
repo LICENSE, verify primitives by grep. Keep strings short (summary < 300 chars, notes < 200). Before finishing,
validate: `python3 -c "import json,os; d=json.load(open(OUT)); [print(c['id'], p) for c in d for p in c['files'] if not os.path.exists(os.path.join('original_sources', c['repo'], p))]"`
must print nothing. Do not modify any file other than your output file. Reply with a short summary: count per
function, notable finds, functions where nothing good exists.
