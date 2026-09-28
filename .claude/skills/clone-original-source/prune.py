#!/usr/bin/env python3
"""Delete non-gateware files from the local clones in original_sources/ (owner rule 2026-09-28,
memory prune-clones.md). Dry-run by default; --apply deletes. Never commits: deletions stay as
unstaged working-tree changes in each clone.

usage: prune.py [--apply] (--all | <slug> ...)

Rules:
  1. per-slug paths in prune.tsv (slug, path, action=delete|keep, reason); `keep` wins over `delete`
     and over the generic rules. Used for folders like prebuilt toolchains (toasterllc__mdccode Tools/).
  2. generic rules by extension (bitstreams, build outputs, tool binaries, PCB/3D files, documents,
     videos), by extension + size (images > 256 KiB, archives / disk images > 1 MiB, outside sim/test
     dirs for archives), and by extension + content (yosys JSON netlists, trellis .config, icestorm .asc,
     KiCad/Eagle .sch).
Never deleted: .git, README*/LICENSE*/COPYING*, and anything not matched above (HDL, constraints,
Makefiles, testbenches, .hex/.mem/.bin/.mif/.coe ROM files...).
Reports the working-tree bytes removed per clone and in total; .git packs do not shrink.
"""
import os, sys, csv

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SRC = os.path.join(ROOT, "original_sources")
RULES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prune.tsv")

ALWAYS = {  # extension -> category
    **dict.fromkeys("bit svf dfu jed rbf sof pof vme mcs fs".split(), "bitstream"),
    **dict.fromkeys("ncd ngd rpt sdf vdb log vcd fst ghw lxt oa twr mrp par".split(), "build-output"),
    **dict.fromkeys("exe dll so dylib msi dmg deb rpm appimage elf".split(), "binary"),
    **dict.fromkeys("kicad_pcb kicad_sch kicad_mod kicad_sym kicad_pro kicad_prl kicad_dru brd "
                    "gbr gtl gbl gto gbo gts gbs gtp gbp gko gm1 gml drl gbrjob".split(), "pcb"),
    **dict.fromkeys("step stp wrl stl dae 3ds 3mf f3d".split(), "3d-model"),
    **dict.fromkeys("pdf doc docx ppt pptx xls xlsx odt odp ods epub chm djvu webarchive".split(), "document"),
    **dict.fromkeys("mp4 mov avi webm mkv mp3".split(), "video"),
}
SIZED = {  # extension -> (min bytes, category)
    **dict.fromkeys("png jpg jpeg gif bmp tif tiff webp svg".split(), (256 << 10, "image")),
    **dict.fromkeys("zip gz tgz xz bz2 7z rar tar".split(), (1 << 20, "archive")),
    "img": (1 << 20, "disk-image"),
}
SIM_DIRS = {"sim", "sims", "simulation", "tb", "test", "tests", "testbench", "verilator", "formal", "cocotb"}


def head(path, n=4096):
    try:
        with open(path, "rb") as f:
            return f.read(n)
    except OSError:
        return b""


def generic(path, rel, name):
    low = name.lower()
    if low.startswith(("readme", "license", "licence", "copying")):
        return None
    ext = low.rsplit(".", 1)[-1] if "." in low else ""
    if ext in ALWAYS:
        return ALWAYS[ext]
    if ext in SIZED:
        size, cat = SIZED[ext]
        if cat == "archive" and SIM_DIRS & {p.lower() for p in rel.split("/")[:-1]}:
            return None
        return cat if os.path.getsize(path) > size else None
    if ext == "json" and b'"creator": "Yosys' in head(path, 512):
        return "build-output"
    if ext == "config" and head(path, 16).startswith(b".device"):
        return "build-output"
    if ext == "asc" and head(path, 16).startswith((b".comment", b".device")):
        return "build-output"
    if ext == "sch" and (b"EESchema" in head(path, 256) or b"eagle" in head(path, 512).lower()):
        return "pcb"
    return None


def load_rules():
    rules = {}
    with open(RULES) as f:
        for r in csv.DictReader(f, delimiter="\t"):
            rules.setdefault(r["slug"], []).append((r["path"].strip("/"), r["action"]))
    return rules


def under(rel, path):
    return rel == path or rel.startswith(path + "/")


def prune(slug, rules, apply):
    base = os.path.join(SRC, slug)
    mine = rules.get(slug, [])
    keeps = [p for p, a in mine if a == "keep"]
    dels = [p for p, a in mine if a == "delete"]
    total, cats = 0, {}
    for dirpath, dirnames, filenames in os.walk(base):
        if ".git" in dirnames:
            dirnames.remove(".git")
        for name in filenames:
            path = os.path.join(dirpath, name)
            if os.path.islink(path) or not os.path.isfile(path):
                continue
            rel = os.path.relpath(path, base)
            if name == ".git" or any(under(rel, k) for k in keeps):
                continue
            cat = "slug-rule" if any(under(rel, d) for d in dels) else generic(path, rel, name)
            if not cat:
                continue
            size = os.path.getsize(path)
            total += size
            cats[cat] = cats.get(cat, 0) + size
            if apply:
                os.remove(path)
    if apply:  # drop directories left empty
        for dirpath, dirnames, filenames in os.walk(base, topdown=False):
            if ".git" not in dirpath.split(os.sep) and dirpath != base and not os.listdir(dirpath):
                os.rmdir(dirpath)
    return total, cats


def main():
    args = sys.argv[1:]
    apply = "--apply" in args
    args = [a for a in args if a != "--apply"]
    if not args:
        sys.exit(__doc__)
    slugs = sorted(d for d in os.listdir(SRC) if os.path.isdir(os.path.join(SRC, d, ".git"))) if args == ["--all"] else args
    rules = load_rules()
    grand, gcats = 0, {}
    for slug in slugs:
        if not os.path.isdir(os.path.join(SRC, slug)):
            print(f"skip {slug}: not cloned", file=sys.stderr)
            continue
        total, cats = prune(slug, rules, apply)
        grand += total
        for c, s in cats.items():
            gcats[c] = gcats.get(c, 0) + s
        if total:
            print(f"{total / 1048576:9.1f} MB  {slug}")
    print(f"{grand / 1048576:9.1f} MB  TOTAL {'deleted' if apply else 'would delete (dry run, --apply to delete)'}")
    for c, s in sorted(gcats.items(), key=lambda x: -x[1]):
        print(f"{s / 1048576:9.1f} MB    {c}")


if __name__ == "__main__":
    main()
