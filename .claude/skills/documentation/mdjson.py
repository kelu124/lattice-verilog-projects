#!/usr/bin/env python3
"""Markdown <-> JSON page model for lattice-verilog-projects (shared by md2json.py and gen_site.py).

Page JSON (schema "lattice-verilog-projects/page/v1"):
  {"schema", "kind", "slug", "title", "description", "fields": {..} | absent, "blocks": [..], "sections": [..]}
  section = {"title", "blocks": [..], "sections": [..]}   (nested by heading level: ## -> ### -> ####)
  block   = {"type": "paragraph", "text"}
          | {"type": "table", "columns": [..], "rows": [{column: cell}], "align": [..] (only if not default)}
          | {"type": "list", "ordered": bool, "items": [str | {"text", "items": [..]}]}
          | {"type": "code", "lang", "text"}
          | {"type": "hr"}
Inline markdown (links, `code`, **bold**) stays inside the strings. A leading 2-column "Field | Value" table right
after the title becomes the "fields" object (project pages).
"""
import re

SCHEMA = "lattice-verilog-projects/page/v1"
LIST_RE = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")
FENCE_RE = re.compile(r"^(\s*)(```+|~~~+)\s*(\S*)\s*$")
HEAD_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
SEP_RE = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")


def split_row(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    cells, cur, i, code = [], "", 0, 0  # code = length of the open backtick run (0 = not in a code span)
    while i < len(s):
        ch = s[i]
        if ch == "\\" and i + 1 < len(s) and s[i + 1] == "|":
            cur += "\\|"; i += 2; continue
        if ch == "`":
            j = i
            while j < len(s) and s[j] == "`":
                j += 1
            run = j - i
            if not code:
                code = run
            elif run == code:
                code = 0
            cur += s[i:j]; i = j; continue
        if ch == "|" and not code:
            cells.append(cur.strip()); cur = ""
        else:
            cur += ch
        i += 1
    cells.append(cur.strip())
    return cells


def uniq(cols):
    seen, out = {}, []
    for c in cols:
        k = c or "col"
        if k in seen:
            seen[k] += 1; k = f"{k}_{seen[k]}"
        else:
            seen[k] = 1
        out.append(k)
    return out


def parse_blocks(lines):
    blocks, i, n = [], 0, len(lines)
    while i < n:
        line = lines[i]
        if not line.strip():
            i += 1; continue
        m = FENCE_RE.match(line)
        if m:
            fence, lang, body = m.group(2), m.group(3), []
            i += 1
            while i < n and not lines[i].strip().startswith(fence):
                body.append(lines[i]); i += 1
            blocks.append({"type": "code", "lang": lang, "text": "\n".join(body)})
            i += 1; continue
        if re.match(r"^\s*(-{3,}|\*{3,}|_{3,})\s*$", line):
            blocks.append({"type": "hr"}); i += 1; continue
        if line.lstrip().startswith("|") and i + 1 < n and SEP_RE.match(lines[i + 1]):
            raw_cols = split_row(line)
            cols = uniq(raw_cols)
            seps = split_row(lines[i + 1])
            align = ["center" if s.startswith(":") and s.endswith(":") else "right" if s.endswith(":") else "left" if s.startswith(":") else "" for s in seps]
            rows = []
            i += 2
            while i < n and lines[i].lstrip().startswith("|"):
                cells = split_row(lines[i])
                cells += [""] * (len(cols) - len(cells))
                row = dict(zip(cols, cells[:len(cols)]))
                if len(cells) > len(cols):
                    row["_extra"] = cells[len(cols):]
                rows.append(row); i += 1
            b = {"type": "table", "columns": cols, "rows": rows}
            if raw_cols != cols:
                b["headers"] = raw_cols
            if any(align):
                b["align"] = align
            blocks.append(b); continue
        m = LIST_RE.match(line)
        if m:
            items, i = parse_list(lines, i)
            blocks.append({"type": "list", "ordered": m.group(2)[0].isdigit(), "items": items})
            continue
        para = []
        while i < n and lines[i].strip() and not FENCE_RE.match(lines[i]) and not (interrupts(lines[i]) if para else LIST_RE.match(lines[i])) \
                and not HEAD_RE.match(lines[i]) and not (lines[i].lstrip().startswith("|") and para == []) \
                and not re.match(r"^\s*(-{3,}|\*{3,}|_{3,})\s*$", lines[i]):
            para.append(lines[i]); i += 1
        if not para:  # a stray table-looking line without separator
            para.append(lines[i]); i += 1
        blocks.append({"type": "paragraph", "text": "\n".join(para)})
    return blocks


def marker_kind(mark):
    return mark if not mark[0].isdigit() else "ol" + mark[-1]


def interrupts(line):
    """CommonMark: inside a paragraph only '-'/'*' bullets or an ordered item numbered 1 start a list."""
    m = LIST_RE.match(line)
    return bool(m) and (m.group(2) in ("-", "*") or m.group(2)[:-1] == "1")


def parse_list(lines, i):
    """Parse a (possibly nested) list starting at lines[i]. Returns (items, next_index)."""
    first = LIST_RE.match(lines[i])
    base, kind = len(first.group(1)), marker_kind(first.group(2))
    items, n = [], len(lines)
    while i < n:
        line = lines[i]
        if not line.strip():
            # blank line: list continues only if the next line is a list item at >= base indent
            j = i + 1
            if j < n and LIST_RE.match(lines[j]) and len(LIST_RE.match(lines[j]).group(1)) >= base:
                i = j; continue
            break
        m = LIST_RE.match(line)
        if m and len(m.group(1)) == base and marker_kind(m.group(2)) == kind:
            items.append({"text": m.group(3), "items": []}); i += 1; continue
        if m and len(m.group(1)) > base and items and interrupts(line):
            sub, i = parse_list(lines, i)
            items[-1]["items"].extend(sub); continue
        if m and len(m.group(1)) < base:  # less indented: belongs to a parent list
            break
        if m and len(m.group(1)) == base:  # different marker kind at this level: a new list
            break
        if HEAD_RE.match(line) or FENCE_RE.match(line) or (line.lstrip().startswith("|")) or not items:
            break
        items[-1]["text"] += "\n" + line.strip()  # continuation line
        i += 1
    return [it["text"] if not it["items"] else it for it in items], i


def md_to_page(text, kind, slug):
    lines = text.split("\n")
    title, start = slug, 0
    for k, l in enumerate(lines):
        if l.strip():
            m = HEAD_RE.match(l)
            if m and len(m.group(1)) == 1:
                title, start = m.group(2), k + 1
            break
    root = {"title": title, "blocks": [], "sections": []}
    stack = [(1, root)]
    buf = []

    def flush():
        stack[-1][1]["blocks"].extend(parse_blocks(buf)); buf.clear()

    in_code = False
    for l in lines[start:]:
        if FENCE_RE.match(l):
            in_code = not in_code
        m = None if in_code else HEAD_RE.match(l)
        if m and len(m.group(1)) >= 2:
            flush()
            lvl = len(m.group(1))
            while stack[-1][0] >= lvl:
                stack.pop()
            sec = {"title": m.group(2), "blocks": [], "sections": []}
            if lvl - stack[-1][0] > 1:
                sec["level"] = lvl
            stack[-1][1]["sections"].append(sec)
            stack.append((lvl, sec))
        else:
            buf.append(l)
    flush()
    page = {"schema": SCHEMA, "kind": kind, "slug": slug, "title": title}
    blocks = root["blocks"]
    if blocks and blocks[0]["type"] == "table" and blocks[0]["columns"][:2] == ["Field", "Value"] and len(blocks[0]["columns"]) == 2:
        page["fields"] = {r["Field"]: r["Value"] for r in blocks[0]["rows"]}
        blocks = blocks[1:]
    page["blocks"] = blocks
    page["sections"] = root["sections"]
    prune(page)
    return page


def prune(node):
    for s in node.get("sections", []):
        prune(s)
        if not s["sections"]:
            del s["sections"]
        if not s["blocks"]:
            del s["blocks"]


# ---------------------------------------------------------------- rendering

def esc(cell):
    return str(cell).replace("\n", "<br>")


def render_table(b):
    cols = b["columns"]
    heads = b.get("headers", cols)
    align = b.get("align", [""] * len(cols))
    sep = {"": "---", "left": ":---", "right": "---:", "center": ":---:"}
    out = ["| " + " | ".join(heads) + " |", "|" + "|".join(sep[a] for a in align) + "|"]
    for r in b["rows"]:
        cells = [esc(r.get(c, "")) for c in cols] + [esc(x) for x in r.get("_extra", [])]
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)


def render_list(items, ordered, indent=0):
    out = []
    for k, it in enumerate(items, 1):
        text, sub = (it, []) if isinstance(it, str) else (it["text"], it.get("items", []))
        mark = f"{k}." if ordered else "-"
        pad = " " * indent
        cont = "\n" + pad + " " * (len(mark) + 1)
        out.append(pad + mark + " " + text.replace("\n", cont))
        if sub:
            out.append(render_list(sub, False, indent + len(mark) + 1))
    return "\n".join(out)


def render_blocks(blocks):
    out = []
    for b in blocks:
        t = b["type"]
        if t == "paragraph":
            out.append(b["text"])
        elif t == "table":
            out.append(render_table(b))
        elif t == "list":
            out.append(render_list(b["items"], b.get("ordered", False)))
        elif t == "code":
            out.append(f"```{b.get('lang', '')}\n{b['text']}\n```")
        elif t == "hr":
            out.append("---")
        else:
            raise ValueError(f"unknown block type {t}")
    return out


def render_sections(sections, level):
    out = []
    for s in sections:
        lvl = s.get("level", level)
        out.append("#" * lvl + " " + s["title"])
        out += render_blocks(s.get("blocks", []))
        out += render_sections(s.get("sections", []), lvl + 1)
    return out


def page_to_md(page):
    out = ["# " + page["title"]]
    if page.get("fields"):
        out.append(render_table({"columns": ["Field", "Value"],
                                 "rows": [{"Field": k, "Value": v} for k, v in page["fields"].items()]}))
    out += render_blocks(page.get("blocks", []))
    out += render_sections(page.get("sections", []), 2)
    return "\n\n".join(out) + "\n"
