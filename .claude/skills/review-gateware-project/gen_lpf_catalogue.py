#!/usr/bin/env python3
"""Render docs/lpf-catalogue.md from data/lpfs.json (written by scan_lpfs.py).

usage: gen_lpf_catalogue.py
"""
import json, os
from collections import Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
IN_JSON = os.path.join(ROOT, "data", "lpfs.json")
OUT_MD = os.path.join(ROOT, "docs", "lpf-catalogue.md")


def write_md(doc):
    E = doc["lpfs"]
    by_board = Counter()
    by_rev = Counter()
    chip_c = Counter()
    kinds = Counter()
    for e in E:
        kinds[e["kind"]] += e["copy_count"]
    E = [e for e in E if e["kind"] == "pin-map"]
    for e in E:
        by_board[e["board"]] += e["copy_count"]
        if e["board"] == "ULX3S":
            by_rev[" / ".join(e["board_rev"])] += e["copy_count"]
        for c in e["chips"]:
            chip_c[c] += e["copy_count"]
    L = [f"# LPF catalogue", "",
         f"Generated {doc['generated']} by `{doc['generator']}` from every `*.lpf` in `original_sources/` "
         f"(scan), rendered by `.claude/skills/review-gateware-project/gen_lpf_catalogue.py`; do not edit by hand. "
         f"Data: [`data/lpfs.json`](https://github.com/kelu124/ulx3s-klod/blob/main/data/lpfs.json).", "",
         f"**{doc['files_scanned']} LPF files, {doc['distinct_lpfs']} distinct contents.** " + " ".join(doc["notes"][1:]), "",
         "| Kind | LPF files |", "|---|---|"] + [f"| {k} | {n} |" for k, n in kinds.most_common()] + ["",
         "The tables below count only `pin-map` LPFs (at least one active LOCATE line).", "",
         "## Files per board (copies)", "", "| Board | LPF files |", "|---|---|"]
    L += [f"| {b} | {n} |" for b, n in by_board.most_common(25)]
    L += ["", "## ULX3S revisions (copies, by reference match)", "", "| Revision(s) | LPF files |", "|---|---|"]
    L += [f"| {r} | {n} |" for r, n in by_rev.most_common()]
    L += ["", "## Peripherals constrained (active signals, copies)", "", "| Chip / peripheral | LPF files |", "|---|---|"]
    L += [f"| {c} | {n} |" for c, n in chip_c.most_common()]
    L += ["", "## Most-copied LPFs", "", "| Name | Copies | Board | Rev | Device | Active signals | Chips | First copy |", "|---|---|---|---|---|---|---|---|"]
    for e in E[:30]:
        c = e["copies"][0]
        L.append(f"| `{e['name']}` | {e['copy_count']} | {e['board']} | {', '.join(e['board_rev'])} | {'/'.join(e['devices_seen'])} | "
                 f"{e['signals_active']} | {', '.join(e['chips'])} | [{c['repo']}]({c['url']}) |")
    L += ["", "## LPFs for boards other than ULX3S", "", "| Name | Board | Device | Chips | Repo |", "|---|---|---|---|---|"]
    for e in E:
        if e["board"] != "ULX3S":
            c = e["copies"][0]
            L.append(f"| [`{e['name']}`]({c['url']}) | {e['board'][:60]} | {'/'.join(e['devices_seen'])} | {', '.join(e['chips'])} | {c['repo']} |")
    open(OUT_MD, "w").write("\n".join(L) + "\n")




if __name__ == "__main__":
    write_md(json.load(open(IN_JSON)))
    print(f"wrote {os.path.relpath(OUT_MD, ROOT)}")
