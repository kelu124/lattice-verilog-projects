#!/usr/bin/env python3
"""Find Makefile targets that run a simulation/testbench in one or more repos.

Usage: scan_make_tests.py original_sources/<slug> [...]
Prints one line per repo: slug<TAB>candidates, where candidates is a '; '-separated list of
  <makefile path>:<target> [<tools>]
for every target whose recipe calls a simulator or test runner (iverilog/vvp, verilator, ghdl -r/--elab-run,
cocotb, sby/SymbiYosys, nvc, pytest/unittest, vunit, make -C <sim/test dir>), or 'none found'.
This is a candidate list only: whether the testbench exists and passes must be checked by hand.
"""
import os, re, sys

SIM = [
    ('iverilog', re.compile(r'\b(iverilog|vvp)\b')),
    ('verilator', re.compile(r'\bverilator\b')),
    ('ghdl', re.compile(r'\bghdl\b.*(\s-r\b|--elab-run|\s-e\b|\srun\b)')),
    ('nvc', re.compile(r'\bnvc\b')),
    ('cocotb', re.compile(r'cocotb|Makefile\.sim|\$\(shell cocotb-config')),
    ('sby', re.compile(r'\bsby\b|symbiyosys', re.I)),
    ('pytest', re.compile(r'\bpytest\b|-m unittest\b')),
    ('vunit', re.compile(r'\bvunit\b|run\.py\b')),
    ('sub-make', re.compile(r'\$\(MAKE\)\s+-C\s+\S*(sim|test|tb|bench|verif)\S*|make\s+-C\s+\S*(sim|test|tb|bench|verif)', re.I)),
]
MAKEFILE = re.compile(r'^(GNUmakefile|makefile|Makefile(\..*)?|.*\.mk)$')
TARGET = re.compile(r'^([A-Za-z0-9_./%$(){}-]+(?:\s+[A-Za-z0-9_./%$(){}-]+)*)\s*::?(?!=)')
SKIP_DIRS = {'.git', 'node_modules', '__pycache__'}


def scan(repo):
    found = []
    for root, dirs, files in os.walk(repo):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if not MAKEFILE.match(f):
                continue
            path = os.path.join(root, f)
            try:
                lines = open(path, errors='replace').read().splitlines()
            except OSError:
                continue
            # cocotb makefiles run sims via an include, not a recipe
            text = '\n'.join(lines)
            if re.search(r'include\s+\$\(shell cocotb-config --makefiles\)', text):
                found.append((os.path.relpath(path, repo), '(cocotb include)', {'cocotb'}))
            target, tools = None, set()
            for line in lines + ['']:
                m = TARGET.match(line)
                if m and not line.startswith('\t'):
                    if target and tools:
                        found.append((os.path.relpath(path, repo), target, tools))
                    target, tools = m.group(1).split()[0], set()
                elif line.startswith('\t') and target:
                    for name, rx in SIM:
                        if rx.search(line):
                            tools.add(name)
                elif line.strip() == '' and target and tools:
                    found.append((os.path.relpath(path, repo), target, tools))
                    target, tools = None, set()
    seen, out = set(), []
    for p, t, tools in found:
        if (p, t) in seen:
            continue
        seen.add((p, t))
        out.append(f"{p}:{t} [{','.join(sorted(tools))}]")
    return out


for repo in sys.argv[1:]:
    res = scan(repo)
    slug = os.path.basename(os.path.normpath(repo))
    print(f"{slug}\t{'; '.join(res[:12]) + (f'; …(+{len(res)-12})' if len(res) > 12 else '') if res else 'none found'}")
