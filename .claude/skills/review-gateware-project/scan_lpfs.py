#!/usr/bin/env python3
"""Scan every *.lpf (ECP5 constraint file) in original_sources/ into data/lpfs.json.

usage: scan_lpfs.py      -> writes data/lpfs.json; then run gen_lpf_catalogue.py to render docs/methodology/lpf-catalogue.md

One JSON entry per distinct file content (sha256); every copy (repo, path, URL at the pinned commit) is listed
under it. For each LPF: signals (active LOCATE lines vs commented-out ones), IO standards, clock FREQUENCY,
SYSCONFIG, part numbers named in comments, peripheral chips inferred from signal names, the board/revision
inferred by matching (signal, site) pairs against reference LPFs, and the device (FPGA size -> LUT count)
from the LPF comments, a build file next to it, or the repo's catalogue row. Nothing is guessed silently:
every inferred field carries its evidence. Dates: per-file dates are unknown (shallow clones); the repo's
pinned commit date is given instead.
"""
import csv, glob, hashlib, json, os, re, sys, datetime
from collections import Counter, defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SRC = os.path.join(ROOT, "original_sources")
MEM = os.path.join(ROOT, ".claude", "memory")
OUT_JSON = os.path.join(ROOT, "data", "lpfs.json")

# ECP5 LUT4 counts (Lattice ECP5/ECP5-5G family data sheet)
LUTS = {"12k": 12000, "25k": 24000, "45k": 44000, "85k": 84000}

# Reference LPFs: (board, rev, slug, path). Matched on (signal, site) pairs.
REFERENCES = [
    ("ULX3S", "v2.x/v3.0.x (ulx3s_v20)", "emard__ulx3s", "doc/constraints/ulx3s_v20.lpf"),
    ("ULX3S", "v1.7 patched (ulx3s_v17patch)", "emard__ulx3s", "doc/constraints/prototype/ulx3s_v17patch.lpf"),
    ("ULX3S", "v3.1.4 (ulx3s_v314)", "emard__ulx3s", "doc/constraints/prototype/ulx3s_v314.lpf"),
    ("ULX3S", "v3.1.6/v3.1.7 (ulx3s_v316)", "emard__ulx3s", "doc/constraints/prototype/ulx3s_v316.lpf"),
]

REV_BY_FILE = {"20": "v2.x/v3.0.x (ulx3s_v20, file name)", "17": "v1.7 (file name)", "314": "v3.1.4 (ulx3s_v314, file name)",
               "316": "v3.1.6/v3.1.7 (ulx3s_v316, file name)", "317": "v3.1.7 (file name)", "002": "v0.0.2 (file name)"}

# peripheral / chip tags from signal names (lower-case, before any [index])
CHIPS = [
    ("sdram", r"^(sdram|dram|sdr)_|^dr_"),
    ("ddr3", r"^(ddram|ddr3|ddr)_"),
    ("hyperram", r"hyperram|^hram|^hr_|^hr\d_"),
    ("psram", r"psram|^qpi_|^ram_(sio|cs|sck)"),
    ("sram", r"^sram_"),
    ("spi-flash", r"^flash_|spiflash|spi_flash|^qspi"),
    ("sdcard", r"^sd_|^sdcard|^sd\d_|^mmc"),
    ("esp32-wifi", r"^wifi_|^esp32|^esp_"),
    ("hdmi-dvi", r"^gpdi|hdmi|^dvi|^tmds"),
    ("usb", r"^usb"),
    ("ftdi-uart", r"^ftdi_|^uart|^ser_|^rs232|^serial"),
    ("oled-lcd", r"^oled|^lcd|^tft|^st7789|^disp"),
    ("adc", r"^adc"),
    ("dac", r"^dac"),
    ("audio", r"^audio|^spdif|^i2s|^aud_|^sound"),
    ("ethernet", r"^eth|rgmii|rmii|^mdio|^mdc$|^phy_|^enet"),
    ("rtc-power", r"rtc|^shutdown"),
    ("i2c", r"i2c|_scl$|_sda$"),
    ("camera", r"^cam|ov7670|ov5640|^dcmi"),
    ("sensor", r"accel|gyro|^imu|^mpu|^bme|^bmp|^temp|^lis3|^lsm|sensor"),
    ("vga", r"^vga|^red|^green|^blue|^hsync|^vsync"),
    ("ps2", r"ps2"),
    ("led", r"^led|^rgb"),
    ("button", r"^btn|^button|^key"),
    ("switch", r"^sw(\d|$)|^dip"),
    ("gpio-header", r"^gp\d*$|^gn\d*$|^gpio|^pmod|^j\d+_|^io\d|^p\d+_"),
    ("serdes-pcie-sata", r"pcie|sata|serdes|^refclk"),
    ("radio-antenna", r"^ant_|antenna|^rf_"),
    ("jtag", r"jtag|^tck$|^tms$|^tdi$|^tdo$"),
]
PARTNO = re.compile(r"\b(?:[A-Z]{2,5}\d{3,}[A-Z0-9-]*|ESP32(?:-[A-Z0-9]+)?|LFE5U[A-Z0-9-]*|W25Q\d+\w*|IS42S\w+|AS4C\w+)\b")
SIZE_RE = re.compile(r"(?:LFE5UM?5?G?-|--|\bDEVICE\s*[:?]?=\s*|FPGA_SIZE\s*[:?]?=\s*|\b)(12|25|45|85)[FK]\b", re.I)
SIZE_RE2 = re.compile(r"--(um5g-|um-)?(12|25|45|85)k\b|LFE5UM?5?G?-(12|25|45|85)F|FPGA_SIZE\s*\??=\s*(12|25|45|85)\b|DEVICE\s*\??=\s*(?:LFE5UM?5?G?-)?(um5g-|um-)?(12|25|45|85)[kF]?\b")
BOARD_WORDS = [  # (regex on path, board), first match wins
    (r"ulx4m", "ULX4M"), (r"ulx3s", "ULX3S"), (r"ulx2s", "ULX2S"), (r"orangecrab", "OrangeCrab"),
    (r"icesugar.?pro", "iCESugar-Pro"), (r"icepi", "IcePi Zero"), (r"greybadge", "GreyBadge 2025"),
    (r"colorlight|5a-75|(^|[/_-])i[59]([/_.-]|$)", "Colorlight"),
    (r"hadbadge|had2019|had19", "Hackaday 2019 badge"), (r"butterstick", "ButterStick"), (r"ecpix", "ECPIX-5"),
    (r"versa", "Versa ECP5"), (r"trellisboard", "TrellisBoard"), (r"fleafpga|flea_ohm", "FleaFPGA Ohm/Uno"),
    (r"pergola", "Pergola"), (r"logicbone", "Logicbone"), (r"ecp5.?evn|evaluation", "ECP5 Evaluation board"),
    (r"ffm-lfe5u", "FFM-LFE5U module"), (r"cynthion", "Cynthion"),
]


def read_tsv(name):
    with open(os.path.join(MEM, name)) as f:
        return {r["slug"]: r for r in csv.DictReader(f, delimiter="\t")}


def blob_url(url, commit, path):
    u = url[:-4] if url.endswith(".git") else url.rstrip("/")
    if "codeberg.org" in u:
        return f"{u}/src/commit/{commit}/{path}"
    if "gitlab.com" in u:
        return f"{u}/-/blob/{commit}/{path}"
    return f"{u}/blob/{commit}/{path}"


LOC = re.compile(r'LOCATE\s+COMP\s+"([^"]+)"\s+SITE\s+"([^"]+)"', re.I)
IOB = re.compile(r'IOBUF\s+PORT\s+"([^"]+)"\s+(.*?);', re.I)
FREQ = re.compile(r'FREQUENCY\s+(?:PORT|NET)\s+"([^"]+)"\s+([\d.]+\s*[MK]?HZ)', re.I)


def base(sig):
    return re.sub(r"\[.*", "", sig).lower()


def parse(text):
    active, commented, iostd, freqs, sysconf, parts = {}, {}, Counter(), [], [], set()
    for raw in text.splitlines():
        line = raw.strip()
        is_c = line.startswith("#") or line.startswith("//")
        body = line.lstrip("#/ ").strip()
        for sig, site in LOC.findall(body):
            (commented if is_c else active)[sig] = site.upper()
        if not is_c:
            for sig, attrs in IOB.findall(body):
                m = re.search(r"IO_TYPE\s*=\s*(\w+)", attrs, re.I)
                if m:
                    iostd[m.group(1).upper()] += 1
            for sig, f in FREQ.findall(body):
                freqs.append(f"{sig} {f.upper().replace(' ', '')}")
            if body.upper().startswith("SYSCONFIG"):
                sysconf.append(body.rstrip(";"))
        if is_c:
            parts.update(p for p in PARTNO.findall(raw) if not re.match(r"^(SITE|LOCATE|IOBUF|PORT|COMP)", p))
    return active, commented, iostd, freqs, sysconf, sorted(parts)


def chips_of(signals):
    found = defaultdict(set)
    for s in signals:
        b = base(s)
        for tag, rx in CHIPS:
            if re.search(rx, b):
                found[tag].add(b)
                break
    return {t: sorted(v)[:8] for t, v in sorted(found.items())}


def device_from(text, lpf_path, row_fpga):
    m = SIZE_RE2.search(text)
    if m:
        size = next(g for g in m.groups() if g and g.isdigit())
        return f"{size}k", "LPF text"
    d = os.path.dirname(lpf_path)
    for cand in sorted(glob.glob(os.path.join(d, "*")) + glob.glob(os.path.join(d, "..", "*")))[:60]:
        n = os.path.basename(cand).lower()
        if os.path.isfile(cand) and (n.startswith("makefile") or n.endswith((".mk", ".sh", ".ldf", ".py", ".xml", ".json", "apio.ini"))) and os.path.getsize(cand) < 200_000:
            try:
                t = open(cand, errors="ignore").read()
            except OSError:
                continue
            ms = set(next(g for g in mm if g and g.isdigit()) for mm in SIZE_RE2.findall(t))
            if len(ms) == 1:
                return f"{ms.pop()}k", f"build file {os.path.relpath(cand, SRC)}"
            if len(ms) > 1:
                return "/".join(f"{s}k" for s in sorted(ms, key=int)), f"build file {os.path.relpath(cand, SRC)} (several sizes)"
    sizes = re.findall(r"\b(12|25|45|85)F\b", row_fpga or "")
    if sizes:
        uniq = sorted(set(sizes), key=int)
        return "/".join(f"{s}k" for s in uniq), "repo catalogue row (repo-level, not this file)"
    return "unknown", "not found"


def find_lpfs():
    out = []
    for d, dirs, files in os.walk(SRC):
        dirs[:] = [x for x in dirs if x != ".git"]
        out += [os.path.join(d, f) for f in files if f.lower().endswith(".lpf")]
    return sorted(out)


def main():
    sources = read_tsv("sources.tsv")
    cat = {r["slug"]: dict(r, functions=", ".join(r.get("functions", [])))
           for r in json.load(open(os.path.join(ROOT, "data", "catalogue.json")))["repos"]}
    refs = []
    for board, rev, slug, path in REFERENCES:
        p = os.path.join(SRC, slug, path)
        if os.path.isfile(p):
            a, c, *_ = parse(open(p, errors="ignore").read())
            refs.append((board, rev, {(s.lower(), site) for s, site in {**c, **a}.items()}, p))
    groups = {}
    for p in find_lpfs():
        if not os.path.isfile(p):
            continue
        rel = os.path.relpath(p, SRC)
        slug, path = rel.split("/", 1)
        raw = open(p, "rb").read()
        sha = hashlib.sha256(raw).hexdigest()[:16]
        src = sources.get(slug, {})
        row = cat.get(slug, {})
        dev, dev_ev = device_from(raw.decode("utf-8", errors="ignore"), p, row.get("fpga"))
        copy = {"repo": slug, "path": path,
                "url": blob_url(src.get("url", ""), src.get("commit", ""), path) if src else None,
                "repo_last_commit": src.get("upstream_date") or "unknown",
                "device": dev, "luts": [LUTS[d] for d in re.findall(r"(12k|25k|45k|85k)", dev)] or None,
                "device_evidence": dev_ev}
        if sha in groups:
            groups[sha]["copies"].append(copy)
            continue
        text = raw.decode("utf-8", errors="ignore")
        active, commented, iostd, freqs, sysconf, parts = parse(text)
        pairs = {(s.lower(), site) for s, site in active.items()}
        best, compat = 0.0, []
        if pairs:
            for board, rev, rp, _ in refs:
                score = len(pairs & rp) / len(pairs)
                if score > best + 1e-9:
                    best, compat = score, [(board, rev)]
                elif abs(score - best) < 1e-9 and score > 0:
                    compat.append((board, rev))
        low = rel.lower()
        path_board = next((b for rx, b in BOARD_WORDS if re.search(rx, low)), None)
        if best >= 0.9:
            board = compat[0][0]
            rev = [r for _, r in compat]
            ev = f"{best:.0%} of active (signal, site) pairs match reference LPF(s)"
        else:
            row_txt = f"{row.get('board_rev', '')} {row.get('name', '')}".lower()
            row_board = next((b for rx, b in BOARD_WORDS if re.search(rx, row_txt)), None)
            board = path_board or row_board or "unknown"
            v = re.findall(r"v(\d{2,3})", os.path.basename(low))
            rev = [REV_BY_FILE.get(v[0], f"v{v[0]} (file name)")] if v else ["unknown"]
            ev = ("file path/name" if path_board else "repo catalogue board_rev/name (repo-level)" if row_board else "not found") + (f"; best ULX3S reference match {best:.0%}" if pairs else "")
        groups[sha] = {
            "sha256_16": sha, "name": os.path.basename(path), "lines": text.count("\n"), "empty": not text.strip(),
            "kind": "empty" if not text.strip() else "pin-map" if active else "no-pins (timing/IP/tool-generated or all commented out)",
            "fpga_family": "ECP5" if "NOT ECP5" not in (row.get("fpga") or "") else (row.get("fpga") or "").split(" - ")[0],
            "board": board, "board_rev": rev, "board_evidence": ev,
            "board_description": row.get("name", ""),
            "signals_active": len(active), "signals_commented": len(commented),
            "chips": chips_of(active), "chips_commented_only": {k: v for k, v in chips_of(commented).items() if k not in chips_of(active)},
            "part_numbers_in_comments": parts[:30],
            "io_standards": dict(iostd.most_common()), "clocks": freqs[:8], "sysconfig": sysconf[:2],
            "copies": [copy],
        }
    entries = sorted(groups.values(), key=lambda e: (-len(e["copies"]), e["name"]))
    for e in entries:
        e["copy_count"] = len(e["copies"])
        e["repo_last_commit_max"] = max(c["repo_last_commit"] for c in e["copies"])
        devs = sorted({d for c in e["copies"] for d in c["device"].split("/") if d != "unknown"}, key=lambda d: int(d[:-1]))
        e["devices_seen"] = devs or ["unknown"]
        e["luts_seen"] = [LUTS[d] for d in devs if d in LUTS] or None
    total = sum(e["copy_count"] for e in entries)
    doc = {"generated": datetime.date.today().isoformat(),
           "schema": "lattice-verilog-projects/lpfs/v1", "generator": ".claude/skills/review-gateware-project/scan_lpfs.py",
           "notes": ["One entry per distinct LPF content; `copies` lists every repo/path with a URL at the pinned commit.",
                     "Per-file last-change dates are unknown (shallow clones): `repo_last_commit` is the repo's pinned commit date.",
                     "`board`/`board_rev` come from matching (signal, site) pairs against emard/ulx3s reference LPFs when >= 90 %, else from the path or the repo's catalogue row (see `board_evidence`).",
                     "per-copy `device`/`luts` come from the LPF text, a build file next to it, or the repo's catalogue row (see `device_evidence`); LUT4 counts: 12k=12000, 25k=24000, 45k=44000, 85k=84000.",
                     "`chips` are inferred from active signal names (the matched names are listed); `chips_commented_only` from commented-out LOCATE lines."],
           "files_scanned": total, "distinct_lpfs": len(entries), "lpfs": entries}
    with open(OUT_JSON, "w") as f:
        json.dump(doc, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print(f"wrote {os.path.relpath(OUT_JSON, ROOT)} ({total} files, {len(entries)} distinct)")


if __name__ == "__main__":
    main()
