#!/usr/bin/env python3
"""Validate the JSON in data/ before rendering the site (`make check`).

Checks: every core's repo is catalogued and its `files` exist in the clone (skipped with a note when the clone is
missing), function ids are known, at most one `best` core per main function, unique core ids, usage patterns are
lists, catalogue rows match the pins in .claude/memory/sources.tsv, board families exist, page JSON has the fields
the generators need. Exit code 1 on errors.
"""
import csv, glob, json, os, sys
from collections import Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
D = os.path.join(ROOT, "data")
errors, notes = [], []


def err(m):
    errors.append(m)


funcs = {f["id"] for f in json.load(open(os.path.join(D, "functions.json")))["functions"]}
cat = {r["slug"] for r in json.load(open(os.path.join(D, "catalogue.json")))["repos"]}
with open(os.path.join(ROOT, ".claude", "memory", "sources.tsv")) as f:
    pins = {r["slug"] for r in csv.DictReader(f, delimiter="\t")}
for s in sorted(pins - cat):
    err(f"catalogue: {s} pinned but has no row")
for s in sorted(cat - pins):
    err(f"catalogue: {s} has a row but no pin")

cp = os.path.join(D, "cores.json")
if os.path.exists(cp):
    cores = json.load(open(cp))["cores"]
    ids = Counter(c["id"] for c in cores)
    for i, n in ids.items():
        if n > 1:
            err(f"cores: duplicate id {i}")
    best = Counter(c["functions"][0] for c in cores if c.get("rank") == "best")
    for f, n in best.items():
        if n > 1:
            err(f"cores: {n} 'best' cores for function {f}")
    for c in cores:
        for f in c.get("functions", []):
            if f not in funcs:
                err(f"cores: {c['id']} unknown function {f}")
        if c["repo"] not in cat:
            err(f"cores: {c['id']} repo {c['repo']} not catalogued")
        base = os.path.join(ROOT, "original_sources", c["repo"])
        if not os.path.isdir(base):
            notes.append(f"cores: {c['id']}: clone {c['repo']} missing, files not checked")
            continue
        for p in c.get("files", []):
            if not os.path.exists(os.path.join(base, p)):
                err(f"cores: {c['id']} file missing: {c['repo']}/{p}")
        up = c.get("usage_patterns", {})
        if not isinstance(up.get("files", []), list) or not isinstance(up.get("modules", []), list):
            err(f"cores: {c['id']} usage_patterns must hold lists")

b = json.load(open(os.path.join(D, "boards.json")))
fams = {f["id"] for f in b["families"]}
for x in b["boards"]:
    if x["family"] not in fams:
        err(f"boards: {x['id']} unknown family {x['family']}")
    if x.get("page") and not os.path.exists(os.path.join(D, "pages", x["page"] + ".json")):
        err(f"boards: {x['id']} page {x['page']} missing")

for p in glob.glob(os.path.join(D, "pages", "*.json")) + glob.glob(os.path.join(D, "projects", "*.json")):
    j = json.load(open(p))
    for k in ("kind", "slug", "title"):
        if k not in j:
            err(f"{os.path.relpath(p, ROOT)}: missing {k}")

for n in notes:
    print("note:", n)
for e in errors:
    print("ERROR:", e)
print(f"check: {len(errors)} errors, {len(notes)} notes")
sys.exit(1 if errors else 0)
