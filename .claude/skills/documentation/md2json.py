#!/usr/bin/env python3
"""Import a markdown page into the page-JSON model (see mdjson.py) under data/.

usage: md2json.py <page.md> <out.json> [--kind project|survey|guide|reference|index] [--slug SLUG]
                  [--description TEXT]

Use it to import a page an agent drafted in markdown (e.g. a new docs/projects/<slug>.md draft written to the
scratchpad): the JSON in data/ is the source of truth, `gen_site.py` renders docs/ from it. Links inside the
text must be relative to the legacy flat layout (docs/<slug>.md for data/pages, docs/projects/ for data/projects);
gen_site.py remaps them. Front matter, the leading "generated" HTML comment and the {% raw %} wrapper of a
generated page are dropped, so a rendered page can be edited and re-imported (fix its links first). Existing "description" in <out.json> is kept unless --description is given.
"""
import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mdjson


def main():
    a = sys.argv[1:]
    if len(a) < 2:
        sys.exit(__doc__)
    src, out = a[0], a[1]
    opts = dict(zip(a[2::2], a[3::2]))
    slug = opts.get("--slug", os.path.splitext(os.path.basename(src))[0])
    kind = opts.get("--kind", "project" if "/projects/" in out else "guide")
    text = open(src).read()
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"\A\s*<!--.*?-->\s*", "", text, flags=re.S)
    text = text.replace("{% raw %}", "").replace("{% endraw %}", "")
    page = mdjson.md_to_page(text, kind, slug)
    old = json.load(open(out)) if os.path.exists(out) else {}
    desc = opts.get("--description", old.get("description", ""))
    ordered = {"schema": page["schema"], "kind": kind, "slug": slug, "title": page["title"], "description": desc}
    ordered.update({k: v for k, v in page.items() if k not in ordered})
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    with open(out, "w") as f:
        json.dump(ordered, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
