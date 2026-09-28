#!/usr/bin/env python3
"""Render the GitHub Pages site pages in docs/ from the page JSON in data/.

usage: gen_pages.py

  data/pages/<slug>.json     -> docs/<slug>.md          (guides, references, surveys)
  data/pages/index.json      -> docs/index.md           (intro blocks + generated lists of every page)
  data/projects/<slug>.json  -> docs/projects/<slug>.md (one review page per repo)

Page JSON model: see mdjson.py. Relative links that leave docs/ (e.g. ../.claude/memory/x.md, ../data/x.json)
are rewritten to GitHub URLs, since GitHub Pages only serves docs/. docs/catalogue.md and docs/lpf-catalogue.md
are rendered by gen_catalogue.py and gen_lpf_catalogue.py; build everything with `make docs`.
"""
import glob, json, os, posixpath, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mdjson

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
DATA = os.path.join(ROOT, "data")
DOCS = os.path.join(ROOT, "docs")
REPO_URL = "https://github.com/kelu124/ulx3s-klod"
LINK = re.compile(r"(\]\()([^)\s]+)(\))")
KIND_TITLES = [("guide", "Guides"), ("reference", "Board reference"), ("survey", "Surveys (candidate lists)")]


def rewrite_links(md, out_rel_dir):
    def fix(m):
        target = m.group(2)
        if re.match(r"^[a-z]+:|^#|^/", target):
            return m.group(0)
        path, _, frag = target.partition("#")
        resolved = posixpath.normpath(posixpath.join(out_rel_dir, path))
        if resolved.startswith("docs/") or resolved == "docs":
            return m.group(0)
        kind = "tree" if os.path.isdir(os.path.join(ROOT, resolved)) else "blob"
        return f"{m.group(1)}{REPO_URL}/{kind}/main/{resolved}{'#' + frag if frag else ''}{m.group(3)}"
    # leave code spans and fenced blocks alone
    parts = re.split(r"(```.*?```|`[^`\n]*`)", md, flags=re.S)
    return "".join(p if i % 2 else LINK.sub(fix, p) for i, p in enumerate(parts))


def render(page, src_rel, out_rel):
    md = mdjson.page_to_md(page)
    md = rewrite_links(md, posixpath.dirname(out_rel))
    head = f"<!-- Generated from {src_rel} by .claude/skills/documentation/gen_pages.py; do not edit. -->\n\n"
    with open(os.path.join(ROOT, out_rel), "w") as f:
        f.write(head + md)


def short(text, n=90):
    """First clause of a field value, for index tables (keeps code spans balanced)."""
    t = re.sub(r"\s+", " ", text).strip()
    cut = re.split(r"(?<=[.;)])\s|\s[—(]", t)[0]
    t = cut if len(cut) >= 8 else t
    if len(t) > n:
        t = t[:n].rsplit(" ", 1)[0] + "…"
    return t + ("`" if t.count("`") % 2 else "")


def one_line(page):
    if page.get("description"):
        return page["description"]
    for b in page.get("blocks", []):
        if b["type"] == "paragraph":
            t = re.sub(r"\s+", " ", b["text"])
            return t if len(t) < 220 else t[:217] + "…"
    return ""


def main():
    pages, projects = [], []
    for p in sorted(glob.glob(os.path.join(DATA, "pages", "*.json"))):
        page = json.load(open(p))
        if page.get("kind") == "index":
            continue
        render(page, f"data/pages/{os.path.basename(p)}", f"docs/{page['slug']}.md")
        pages.append(page)
    os.makedirs(os.path.join(DOCS, "projects"), exist_ok=True)
    for p in sorted(glob.glob(os.path.join(DATA, "projects", "*.json"))):
        page = json.load(open(p))
        render(page, f"data/projects/{os.path.basename(p)}", f"docs/projects/{page['slug']}.md")
        projects.append(page)
    idx_p = os.path.join(DATA, "pages", "index.json")
    index = json.load(open(idx_p)) if os.path.exists(idx_p) else {"title": "ulx3s-klod", "blocks": [], "sections": []}
    secs = [{"title": "Catalogues", "blocks": [{"type": "list", "ordered": False, "items": [
        "[Project catalogue](catalogue.md): every cloned repo with FPGA, toolchain, HDL, license, functions, "
        "reusable blocks and tests (from `data/catalogue.json`)",
        "[LPF catalogue](lpf-catalogue.md): every ECP5 pin-constraint file with board, revision, FPGA size and "
        "peripherals (from `data/lpfs.json`)"]}]}]
    for kind, title in KIND_TITLES:
        items = [f"[{p['title']}]({p['slug']}.md): {one_line(p)}".rstrip(": ") for p in pages if p.get("kind") == kind]
        if items:
            secs.append({"title": title, "blocks": [{"type": "list", "ordered": False, "items": items}]})
    rows = []
    for p in projects:
        f = p.get("fields", {})
        rows.append({"Project": f"[{p['slug']}](projects/{p['slug']}.md)",
                     "Target FPGA": short(f.get("Target FPGA(s)", "")), "License": short(f.get("License", "")),
                     "HDL": short(f.get("HDL / framework", ""))})
    secs.append({"title": f"Project pages ({len(projects)})", "blocks": [
        {"type": "paragraph", "text": "Full reviews with per-block reuse notes (module, ports, vendor primitives, "
                                      "license, what to change for a ULX3S design)."},
        {"type": "table", "columns": ["Project", "Target FPGA", "License", "HDL"], "rows": rows}]})
    index = dict(index, sections=index.get("sections", []) + secs)
    render(index, "data/pages/index.json", "docs/index.md")
    print(f"wrote docs/index.md, {len(pages)} pages, {len(projects)} project pages")


if __name__ == "__main__":
    main()
