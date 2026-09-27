#!/usr/bin/env bash
# Heuristic testbench/simulation scanner for one repo dir. Prints one summary line.
d="$1"
cd "$d" || { echo "unreadable"; exit 0; }

tools=()
grep -rlqiE 'cocotb' --include='Makefile*' --include='*.py' --include='requirements*.txt' . 2>/dev/null && tools+=("cocotb")
grep -rlqiE '\bverilator\b' --include='Makefile*' --include='*.mk' --include='*.sh' . 2>/dev/null && tools+=("verilator")
grep -rlqiE '\biverilog\b|\bvvp\b' --include='Makefile*' --include='*.mk' --include='*.sh' . 2>/dev/null && tools+=("iverilog")
grep -rlqiE 'ghdl .*-r |ghdl --elaborate|ghdl -r ' --include='Makefile*' --include='*.mk' --include='*.sh' . 2>/dev/null && tools+=("ghdl-sim")
grep -rlqiE '\bvunit\b' --include='Makefile*' --include='*.py' . 2>/dev/null && tools+=("vunit")

tb_dirs=$(find . -maxdepth 3 -type d \( -iname 'tb' -o -iname 'test' -o -iname 'tests' -o -iname 'testbench*' -o -iname 'sim' -o -iname 'simulation' -o -iname 'verif*' \) 2>/dev/null | grep -v '^\./\.git' | head -5)
tb_files=$(find . -maxdepth 4 -type f \( -iname '*_tb.v' -o -iname '*_tb.sv' -o -iname '*_tb.vhd' -o -iname 'tb_*.v' -o -iname 'tb_*.sv' -o -iname 'tb_*.vhd' -o -iname '*_test.py' -o -iname 'test_*.py' \) 2>/dev/null | grep -v '^\./\.git' | wc -l)

parts=()
[ -n "$tb_dirs" ] && parts+=("dirs: $(echo "$tb_dirs" | tr '\n' ' ' | sed 's/ $//')")
[ "$tb_files" -gt 0 ] 2>/dev/null && parts+=("$tb_files tb/test files")
[ ${#tools[@]} -gt 0 ] && parts+=("tools: $(IFS=,; echo "${tools[*]}")")

if [ ${#parts[@]} -eq 0 ]; then
  echo "none found"
else
  IFS='; '; echo "${parts[*]}"
fi
