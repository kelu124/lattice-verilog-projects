#!/usr/bin/env python3
"""Find which catalogued repos use each reusable core of data/cores.json -> data/core_usage.json.

usage: scan_core_usage.py

For every core, `usage_patterns.files` (distinctive file basenames) and `usage_patterns.modules` (distinctive
module/entity names) are searched in all HDL files of original_sources/ (shallow, pruned clones):
  - "copy": a file with the same basename exists in another repo (vendored copy),
  - "instance": a Verilog/SystemVerilog instantiation (`name #(` / `name inst (`) or a VHDL
    `entity work.name` / `component name` of the module appears in another repo.
The core's own repo is excluded. Heuristic: names can collide; results list the matching paths as evidence.
"""
import json, os, re, sys
from collections import defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SRC = os.path.join(ROOT, "original_sources")
HDL = (".v", ".sv", ".vh", ".svh", ".vhd", ".vhdl", ".si", ".py", ".scala")
MAX_EVIDENCE = 3


def hdl_files():
    for d, dirs, files in os.walk(SRC):
        dirs[:] = [x for x in dirs if x != ".git"]
        for f in files:
            p = os.path.join(d, f)
            if f.lower().endswith(HDL) and not os.path.islink(p) and os.path.isfile(p):
                yield p


def main():
    cores = json.load(open(os.path.join(ROOT, "data", "cores.json")))["cores"]
    by_file = defaultdict(list)          # basename -> cores
    mods = {}                            # module name -> cores
    for c in cores:
        pat = c.get("usage_patterns", {})
        for f in pat.get("files", []):
            by_file[f.lower()].append(c["id"])
        for m in pat.get("modules", []):
            mods.setdefault(m, []).append(c["id"])
    home = {c["id"]: c["repo"] for c in cores}
    mod_re = None
    if mods:
        names = "|".join(sorted((re.escape(m) for m in mods), key=len, reverse=True))
        mod_re = re.compile(r"(?:^|[^\w.])(" + names + r")\s*(?:#\s*\(|\w+\s*\(|\s*\()"          # verilog instance
                            r"|entity\s+work\.(" + names + r")\b|component\s+(" + names + r")\b", re.I | re.M)
    hits = defaultdict(lambda: defaultdict(lambda: {"copy": [], "instance": []}))
    n = 0
    for p in hdl_files():
        n += 1
        rel = os.path.relpath(p, SRC)
        slug, path = rel.split("/", 1)
        for cid in by_file.get(os.path.basename(p).lower(), []):
            if slug != home[cid]:
                hits[cid][slug]["copy"].append(path)
        if mod_re is None or os.path.getsize(p) > 2_000_000:
            continue
        try:
            text = open(p, errors="ignore").read()
        except OSError:
            continue
        for m in mod_re.finditer(text):
            name = next(g for g in m.groups() if g)
            # skip the module's own definition line (`module name (` / `entity name is`)
            line = text[text.rfind("\n", 0, m.start()) + 1: text.find("\n", m.end())]
            if re.match(r"\s*(module|entity|architecture)\b", line, re.I):
                continue
            for mk, cids in mods.items():
                if mk.lower() == name.lower():
                    for cid in cids:
                        if slug != home[cid]:
                            hits[cid][slug]["instance"].append(path)
    out = {"schema": "lattice-verilog-projects/core-usage/v1",
           "generator": ".claude/skills/review-gateware-project/scan_core_usage.py",
           "note": "Heuristic: file-name copies and module instantiations found in other clones; verify before relying on it.",
           "hdl_files_scanned": n, "usage": {}}
    for c in cores:
        users = []
        for slug, ev in sorted(hits[c["id"]].items()):
            users.append({"repo": slug, "copy": sorted(set(ev["copy"]))[:MAX_EVIDENCE],
                          "instance": sorted(set(ev["instance"]))[:MAX_EVIDENCE]})
        out["usage"][c["id"]] = users
    with open(os.path.join(ROOT, "data", "core_usage.json"), "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
        f.write("\n")
    tot = sum(len(v) for v in out["usage"].values())
    print(f"wrote data/core_usage.json ({n} HDL files, {tot} core-repo uses for {len(cores)} cores)")


if __name__ == "__main__":
    main()
