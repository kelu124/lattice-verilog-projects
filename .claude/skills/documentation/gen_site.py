#!/usr/bin/env python3
"""Generate the GitHub Pages site (just-the-docs theme) in docs/ from the JSON in data/.

usage: gen_site.py            (normally via `make docs`, which also renders the catalogue and LPF catalogue)

Site tree (front matter drives the just-the-docs navigation):
  docs/index.md                      Home                 <- data/pages/index.json + generated quick links
  docs/functions/index.md, <id>.md   Cores by function    <- data/functions.json, data/cores.json, data/core_usage.json
  docs/boards/index.md, <family>.md, <board>.md  Boards   <- data/boards.json (+ data/pages/<page>.json body), data/lpfs.json
  docs/guides/index.md, <slug>.md    Guides               <- data/pages/<slug>.json with kind guide
  docs/projects/index.md, <slug>.md  Project reviews      <- data/projects/<slug>.json
  docs/methodology/index.md, <slug>.md  Methodology       <- data/pages/<slug>.json with kind survey (+ catalogue,
                                                             lpf-catalogue written by gen_catalogue.py / gen_lpf_catalogue.py)
Links inside page JSON text are relative to the legacy flat layout (docs/<slug>.md for data/pages, docs/projects/
for data/projects); they are remapped to the tree above, and links leaving docs/ become GitHub URLs.
Every body is wrapped in {% raw %} so Verilog `{{...}}` never reaches Liquid.
"""
import csv, glob, json, os, posixpath, re, sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mdjson

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
DATA = os.path.join(ROOT, "data")
DOCS = os.path.join(ROOT, "docs")
REPO_URL = "https://github.com/kelu124/ulx3s-klod"
GEN = ".claude/skills/documentation/gen_site.py"
LINK = re.compile(r"(\]\()([^)\s]+)(\))")

SECTIONS = {  # title, nav_order, dir
    "functions": ("Cores by function", 2), "boards": ("Boards", 3), "guides": ("Guides", 4),
    "projects": ("Project reviews", 5), "methodology": ("Methodology", 6)}
LEGACY = {}  # legacy docs path -> new docs path (filled in main)


def load(name):
    return json.load(open(os.path.join(DATA, name)))


def pins():
    with open(os.path.join(ROOT, ".claude", "memory", "sources.tsv")) as f:
        return {r["slug"]: r for r in csv.DictReader(f, delimiter="\t")}


PINS = pins()


def repo_url(slug):
    return PINS.get(slug, {}).get("url", "").removesuffix(".git").rstrip("/")


def file_url(slug, path):
    p = PINS.get(slug)
    if not p:
        return ""
    u, c = repo_url(slug), p["commit"]
    if "codeberg.org" in u:
        return f"{u}/src/commit/{c}/{path}"
    if "gitlab.com" in u:
        return f"{u}/-/blob/{c}/{path}"
    kind = "tree" if os.path.isdir(os.path.join(ROOT, "original_sources", slug, path)) else "blob"
    return f"{u}/{kind}/{c}/{path}"


def fm(**kw):
    lines = ["---"]
    for k, v in kw.items():
        if v is None:
            continue
        if isinstance(v, bool):
            v = "true" if v else "false"
        elif isinstance(v, str):
            v = json.dumps(v, ensure_ascii=False)
        lines.append(f"{k}: {v}")
    return "\n".join(lines + ["---", ""])


def rewrite_links(md, legacy_dir, out_rel):
    out_dir = posixpath.dirname(out_rel)

    def fix(m):
        target = m.group(2)
        if re.match(r"^[a-z]+:|^#|^/", target):
            return m.group(0)
        path, _, frag = target.partition("#")
        if not path:
            return m.group(0)
        resolved = posixpath.normpath(posixpath.join(legacy_dir, path))
        resolved = LEGACY.get(resolved, resolved)
        frag = "#" + frag if frag else ""
        if resolved.startswith("docs/"):
            return f"{m.group(1)}{posixpath.relpath(resolved, out_dir)}{frag}{m.group(3)}"
        kind = "tree" if os.path.isdir(os.path.join(ROOT, resolved)) else "blob"
        return f"{m.group(1)}{REPO_URL}/{kind}/main/{resolved}{frag}{m.group(3)}"
    parts = re.split(r"(```.*?```|`[^`\n]*`)", md, flags=re.S)
    return "".join(p if i % 2 else LINK.sub(fix, p) for i, p in enumerate(parts))


def write(out_rel, front, body_md, src, legacy_dir=None):
    body = rewrite_links(body_md, legacy_dir or posixpath.dirname(out_rel), out_rel)
    path = os.path.join(ROOT, out_rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(front + f"<!-- Generated from {src} by {GEN}; do not edit. -->\n\n{{% raw %}}\n" + body.rstrip("\n")
                + "\n{% endraw %}\n")


def section_index(key, body, src, has_children=True):
    title, order = SECTIONS[key]
    write(f"docs/{key}/index.md", fm(title=title, nav_order=order, has_children=has_children, permalink=f"/{key}/"),
          body, src)


def short(text, n=90):
    t = re.sub(r"\s+", " ", text or "").strip()
    cut = re.split(r"(?<=[.;)])\s|\s[—(]", t)[0]
    t = cut if len(cut) >= 8 else t
    if len(t) > n:
        t = t[:n].rsplit(" ", 1)[0] + "…"
    return t + ("`" if t.count("`") % 2 else "")


def cell(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


def one_line(page):
    if page.get("description"):
        return page["description"]
    for b in page.get("blocks", []):
        if b["type"] == "paragraph":
            return short(b["text"], 200)
    return ""


# ------------------------------------------------------------------ functions / cores

def core_md(c, usage, catalogue):
    u = repo_url(c["repo"])
    files = ", ".join(f"[`{p}`]({file_url(c['repo'], p)})" for p in c.get("files", []))
    prim = ", ".join(f"`{p}`" for p in c.get("primitives", [])) or "none (portable)"
    rows = [("Repository", f"[{c['repo']}]({u})" + (f": {short(catalogue[c['repo']]['name'], 110)}" if c['repo'] in catalogue else "")),
            ("Files", files), ("Top module", f"`{c['top']}`" if c.get("top") else "n/a"),
            ("Language", c.get("language", "")), ("License", c.get("license", "")),
            ("FPGA / primitives", f"{c.get('fpga', '')}: {prim}"), ("Tests", c.get("tests", ""))]
    review = os.path.exists(os.path.join(DATA, "projects", c["repo"] + ".json"))
    out = [f"### {c['name']}" + (" (best)" if c.get("rank") == "best" else "") + f" {{#core-{c['id']}}}", "",
           c.get("summary", ""), "",
           "| | |", "|---|---|"] + [f"| {k} | {cell(v)} |" for k, v in rows] + [""]
    if c.get("ulx3s_notes"):
        out += [f"**On ULX3S:** {c['ulx3s_notes']}", ""]
    if review:
        out += [f"Full review: [{c['repo']}](../projects/{c['repo']}.md).", ""]
    users = usage.get(c["id"], [])
    if users:
        items = []
        for us in users[:15]:
            ev = (us["instance"] or us["copy"])[:1]
            how = "instantiates" if us["instance"] else "copies"
            evs = f" ({how} [`{ev[0]}`]({file_url(us['repo'], ev[0])}))" if ev else ""
            items.append(f"- [{us['repo']}]({repo_url(us['repo'])}){evs}")
        more = f"- … and {len(users) - 15} more (see `data/core_usage.json`)" if len(users) > 15 else None
        out += [f"**Used by {len(users)} other catalogued repo{'s' if len(users) > 1 else ''}** "
                "(file copies or module instances found by `scan_core_usage.py`; heuristic):", ""] + items + ([more] if more else []) + [""]
    return "\n".join(out)


def gen_functions(funcs, cores, usage, catalogue):
    by_f = defaultdict(list)
    for c in cores:
        for fid in c["functions"]:
            by_f[fid].append(c)
    for fid in by_f:
        by_f[fid].sort(key=lambda c: (c["functions"][0] != fid, c.get("rank") != "best", c["name"].lower()))
    groups = defaultdict(list)
    for f in funcs:
        groups[f["group"]].append(f)
    tag_count = defaultdict(int)
    for r in catalogue.values():
        for t in r.get("functions", []):
            tag_count[t.replace("NEW:", "")] += 1
    idx = ["Every reusable core found in the collection, grouped by function. Each function page lists the best core "
           "first, then alternatives, with links to the original files upstream (at the commit that was reviewed) and "
           "the other projects that copy or instantiate the core.", ""]
    for g, fl in groups.items():
        idx += [f"## {g}", "", "| Function | Best core | Alternatives | Projects using these cores |", "|---|---|---|---|"]
        for f in fl:
            cs = by_f.get(f["id"], [])
            best = next((c for c in cs if c.get("rank") == "best" and c["functions"][0] == f["id"]), cs[0] if cs else None)
            users = {u["repo"] for c in cs for u in usage.get(c["id"], [])}
            idx.append(f"| [{f['title']}]({f['id']}.md) | " + (f"{cell(best['name'])} ({best['repo']})" if best else "none found")
                       + f" | {max(len(cs) - 1, 0)} | {len(users)} |")
        idx.append("")
    section_index("functions", "# Cores by function\n\n" + "\n".join(idx), "data/functions.json, data/cores.json")
    for f in funcs:
        cs = by_f.get(f["id"], [])
        body = [f"# {f['title']}", "", f["description"], ""]
        if cs:
            body += ["| Core | Repository | Language | License | FPGA | Used by |", "|---|---|---|---|---|---|"]
            for c in cs:
                anchor = "core-" + c["id"]
                body.append(f"| [{cell(c['name'])}](#{anchor})" + (" ★" if c.get("rank") == "best" and c["functions"][0] == f["id"] else "")
                            + f" | [{c['repo']}]({repo_url(c['repo'])}) | {cell(short(c.get('language', ''), 40))} | "
                            f"{cell(short(c.get('license', ''), 50))} | {cell(c.get('fpga', ''))} | {len(usage.get(c['id'], []))} |")
            body += ["", "## Cores", ""] + [core_md(c, usage, catalogue) for c in cs]
        else:
            body += ["No reusable core for this function was found in the collection yet.", ""]
        tags = [t for t in f.get("catalogue_tags", []) if tag_count.get(t)]
        if tags:
            body += ["## Other catalogued projects", "",
                     "Catalogued repos tagged " + ", ".join(f"`{t}` ({tag_count[t]})" for t in tags)
                     + " are listed in the [full catalogue](../methodology/catalogue.md#index-by-function).", ""]
        write(f"docs/functions/{f['id']}.md", fm(title=f["title"], parent="Cores by function", nav_order=f["order"]),
              "\n".join(body), "data/functions.json, data/cores.json, data/core_usage.json")


# ------------------------------------------------------------------ boards

def board_repos(b, catalogue):
    rx = re.compile(b["match"], re.I)
    out = []
    for slug, r in catalogue.items():
        text = " ".join(r.get(k, "") for k in ("board_rev", "name", "fpga", "ulx3s_path"))
        text = re.sub(r"\bnot\s+(?:a\s+)?(?:an?\s+)?" + b["match"], " ", text, flags=re.I)
        text = re.sub(r"\bno\s+(?:real\s+)?" + b["match"], " ", text, flags=re.I)
        if rx.search(text):
            out.append(slug)
    return sorted(out)


def pcf_files(b, repos):
    rx = re.compile(b["match"], re.I)
    out = []
    for slug in repos:
        base = os.path.join(ROOT, "original_sources", slug)
        for d, dirs, files in os.walk(base):
            dirs[:] = [x for x in dirs if x != ".git"]
            for f in files:
                if f.lower().endswith(".pcf"):
                    rel = os.path.relpath(os.path.join(d, f), base)
                    if rx.search(rel) or len(repos) <= 3:
                        out.append((slug, rel))
    return out[:12]


def gen_boards(boards, cores, usage, catalogue, lpfs, pages):
    fams = boards["families"]
    idx = ["The most relevant boards of the collection, in three FPGA families. Each page gives the FPGA, the "
           "constraint files found in the cloned repos, the reusable cores known to run on it and the projects "
           "that target it.", ""]
    for i, fam in enumerate(fams, 1):
        bl = [b for b in boards["boards"] if b["family"] == fam["id"]]
        idx += [f"## [{fam['title']}]({fam['id']}.md)", "", fam["description"], "",
                "| Board | FPGA | Catalogued repos |", "|---|---|---|"]
        for b in bl:
            idx.append(f"| [{b['name']}]({b['id']}.md) | {cell(b['fpga'])} | {len(board_repos(b, catalogue))} |")
        idx.append("")
        fbody = [f"# {fam['title']}", "", fam["description"], "", "| Board | FPGA | Description |", "|---|---|---|"]
        fbody += [f"| [{b['name']}]({b['id']}.md) | {cell(b['fpga'])} | {cell(b['description'])} |" for b in bl]
        write(f"docs/boards/{fam['id']}.md", fm(title=fam["title"], parent="Boards", nav_order=i, has_children=True),
              "\n".join(fbody), "data/boards.json")
    section_index("boards", "# Boards\n\n" + "\n".join(idx), "data/boards.json")
    for fam_i, fam in enumerate(fams):
        for j, b in enumerate([b for b in boards["boards"] if b["family"] == fam["id"]], 1):
            repos = board_repos(b, catalogue)
            rs = set(repos)
            head = [f"# {b['name']}", "", b["description"], "",
                    "| | |", "|---|---|", f"| Board | {cell(b['full_name'])} |", f"| FPGA | {cell(b['fpga'])} |",
                    f"| Evidence | {cell(b['fpga_evidence'])} |", f"| Clock | {cell(b['clock'])} |",
                    f"| Catalogued repos | {len(repos)} |", ""]
            if b["id"] != "ulx3s":
                head += ["*The description is a short summary; FPGA facts come from the catalogue rows cited above.*", ""]
            body = []
            if b.get("page"):
                pj = pages.get(b["page"])
                if pj:
                    body += ["## Board reference", ""] + mdjson.render_blocks(pj.get("blocks", [])) \
                        + mdjson.render_sections(pj.get("sections", []), 3)
                    body = ["\n\n".join(body), ""]
            # constraint files
            if fam["id"] == "ecp5":
                names = {"ulx3s": "ULX3S", "ulx4m": "ULX4M", "orangecrab": "OrangeCrab", "colorlight": "Colorlight",
                         "icepi-zero": "IcePi Zero", "icesugar-pro": "iCESugar-Pro"}
                ents = [e for e in lpfs["lpfs"] if e["board"] == names.get(b["id"]) and e["kind"] == "pin-map"][:12]
                if ents:
                    body += ["## Constraint files (LPF)", "",
                             "Most-copied distinct LPFs for this board in the cloned repos (from the "
                             "[LPF catalogue](../methodology/lpf-catalogue.md)).", "",
                             "| LPF | Revision | Copies | Peripherals constrained |", "|---|---|---|---|"]
                    for e in ents:
                        c = e["copies"][0]
                        body.append(f"| [`{e['name']}`]({c['url']}) ({c['repo']}) | {cell(', '.join(e['board_rev']))} | "
                                    f"{e['copy_count']} | {cell(', '.join(e['chips']))} |")
                    body.append("")
            else:
                pcfs = pcf_files(b, repos)
                if pcfs:
                    body += ["## Constraint files (PCF)", "", "| PCF | Repository |", "|---|---|"]
                    body += [f"| [`{p}`]({file_url(s, p)}) | {s} |" for s, p in pcfs] + [""]
            # cores
            used = [c for c in cores if c["repo"] in rs or any(u["repo"] in rs for u in usage.get(c["id"], []))]
            if used:
                body += ["## Reusable cores seen on this board", "",
                         "Cores whose source repo, or a repo that copies/instantiates them, targets this board.", "",
                         "| Core | Function | Source repo |", "|---|---|---|"]
                for c in sorted(used, key=lambda c: (c["functions"][0], c["name"]))[:40]:
                    body.append(f"| {cell(c['name'])} | [{c['functions'][0]}](../functions/{c['functions'][0]}.md) | {c['repo']} |")
                body.append("")
            # projects
            reviewed = [s for s in repos if os.path.exists(os.path.join(DATA, "projects", s + ".json"))]
            body += ["## Projects targeting this board", ""]
            if len(repos) > 25:
                body += [f"{len(repos)} catalogued repos target this board; see the "
                         "[full catalogue](../methodology/catalogue.md). Those with a full review:", ""]
                body += [f"- [{s}](../projects/{s}.md): {short(catalogue[s]['name'], 120)}" for s in reviewed] + [""]
            else:
                body += [f"- [{s}]({repo_url(s)}): {short(catalogue[s]['name'], 120)}"
                         + (f" ([review](../projects/{s}.md))" if s in reviewed else "") for s in repos] + [""]
            write(f"docs/boards/{b['id']}.md",
                  fm(title=b["name"], parent=fam["title"], grand_parent="Boards", nav_order=j),
                  "\n".join(head + body), "data/boards.json" + (f", data/pages/{b['page']}.json" if b.get("page") else ""),
                  legacy_dir="docs")


# ------------------------------------------------------------------ main

def main():
    funcs = load("functions.json")["functions"]
    cores = load("cores.json")["cores"] if os.path.exists(os.path.join(DATA, "cores.json")) else []
    usage = load("core_usage.json")["usage"] if os.path.exists(os.path.join(DATA, "core_usage.json")) else {}
    catalogue = {r["slug"]: r for r in load("catalogue.json")["repos"]}
    boards = load("boards.json")
    lpfs = load("lpfs.json")
    pages = {json.load(open(p))["slug"]: json.load(open(p)) for p in glob.glob(os.path.join(DATA, "pages", "*.json"))}
    projects = [json.load(open(p)) for p in sorted(glob.glob(os.path.join(DATA, "projects", "*.json")))]

    # new locations of legacy pages
    board_pages = {b["page"]: b["id"] for b in boards["boards"] if b.get("page")}
    for slug, p in pages.items():
        k = p.get("kind")
        if slug in board_pages:
            LEGACY[f"docs/{slug}.md"] = f"docs/boards/{board_pages[slug]}.md"
        elif k == "guide":
            LEGACY[f"docs/{slug}.md"] = f"docs/guides/{slug}.md"
        elif k == "survey":
            LEGACY[f"docs/{slug}.md"] = f"docs/methodology/{slug}.md"
    LEGACY["docs/catalogue.md"] = "docs/methodology/catalogue.md"
    LEGACY["docs/lpf-catalogue.md"] = "docs/methodology/lpf-catalogue.md"

    # remove stale generated pages from the old flat layout
    for old in LEGACY:
        p = os.path.join(ROOT, old)
        if os.path.exists(p) and old not in LEGACY.values():
            os.remove(p)

    gen_functions(funcs, cores, usage, catalogue)
    gen_boards(boards, cores, usage, catalogue, lpfs, pages)

    # guides
    guides = sorted([p for p in pages.values() if p.get("kind") == "guide"], key=lambda p: p.get("nav_order", 99))
    section_index("guides", "# Guides\n\n" + "\n".join(f"- [{p['title']}]({p['slug']}.md): {one_line(p)}" for p in guides),
                  "data/pages/*.json")
    for i, p in enumerate(guides, 1):
        write(f"docs/guides/{p['slug']}.md", fm(title=p.get("nav_title", p["title"]), parent="Guides", nav_order=i),
              mdjson.page_to_md(p), f"data/pages/{p['slug']}.json", legacy_dir="docs")

    # project reviews
    rows = ["| Project | Target FPGA | License | HDL |", "|---|---|---|---|"]
    for p in projects:
        f = p.get("fields", {})
        rows.append(f"| [{p['slug']}]({p['slug']}.md) | {cell(short(f.get('Target FPGA(s)', '')))} | "
                    f"{cell(short(f.get('License', '')))} | {cell(short(f.get('HDL / framework', '')))} |")
    section_index("projects", "# Project reviews\n\nIn-depth reviews of the repos that hold the most reusable gateware: "
                  "per-block reuse notes (module, ports, vendor primitives, license, what to change for a ULX3S design).\n\n"
                  + "\n".join(rows), "data/projects/*.json")
    for i, p in enumerate(projects, 1):
        write(f"docs/projects/{p['slug']}.md", fm(title=p["slug"], parent="Project reviews", nav_order=i),
              mdjson.page_to_md(p), f"data/projects/{p['slug']}.json", legacy_dir="docs/projects")

    # methodology
    surveys = sorted([p for p in pages.values() if p.get("kind") == "survey"], key=lambda p: p["slug"])
    meth = pages.get("methodology")
    body = mdjson.page_to_md(meth) if meth else "# Methodology\n"
    body += "\n## Surveys\n\n" + "\n".join(f"- [{p['title']}]({p['slug']}.md): {one_line(p)}" for p in surveys)
    body += ("\n\n## Data views\n\n- [Full catalogue](catalogue.md): every cloned repo (from `data/catalogue.json`)\n"
             "- [LPF catalogue](lpf-catalogue.md): every ECP5 constraint file (from `data/lpfs.json`)\n")
    write("docs/methodology/index.md", fm(title="Methodology", nav_order=6, has_children=True, permalink="/methodology/"),
          body, "data/pages/methodology.json", legacy_dir="docs")
    for i, p in enumerate(surveys, 1):
        write(f"docs/methodology/{p['slug']}.md", fm(title=p.get("nav_title", p["title"]), parent="Methodology", nav_order=i),
              mdjson.page_to_md(p), f"data/pages/{p['slug']}.json", legacy_dir="docs")

    # home
    index = pages.get("index", {"title": "ulx3s-klod", "blocks": []})
    n_users = len({u["repo"] for us in usage.values() for u in us})
    groups = defaultdict(list)
    for f in funcs:
        groups[f["group"]].append(f"[{f['title']}](functions/{f['id']}.md)")
    extra = {"title": "Browse", "blocks": [
        {"type": "paragraph", "text": f"**{len(cores)} reusable cores** in {len(funcs)} functions, used by {n_users} of the "
                                      f"{len(catalogue)} catalogued repos; {len(boards['boards'])} board pages; "
                                      f"{len(projects)} in-depth reviews."},
        {"type": "table", "columns": ["Area", "Functions"],
         "rows": [{"Area": g, "Functions": ", ".join(v)} for g, v in groups.items()]},
        {"type": "list", "ordered": False, "items": [
            "[Boards](boards/index.md): " + ", ".join(f"[{b['name']}](boards/{b['id']}.md)" for b in boards["boards"]),
            "[Guides](guides/index.md): " + ", ".join(f"[{p.get('nav_title', p['title'])}](guides/{p['slug']}.md)" for p in guides),
            "[Project reviews](projects/index.md) · [Methodology and data](methodology/index.md)"]}]}
    home = dict(index, sections=index.get("sections", []) + [extra])
    write("docs/index.md", fm(title="Home", nav_order=1, permalink="/"), mdjson.page_to_md(home),
          "data/pages/index.json", legacy_dir="docs")
    print(f"site: {len(funcs)} function pages, {len(boards['boards'])} board pages, {len(guides)} guides, "
          f"{len(projects)} reviews, {len(surveys)} surveys")


if __name__ == "__main__":
    main()
