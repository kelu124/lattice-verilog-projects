#!/usr/bin/env bash
# Clone / restore / update upstream repos under original_sources/ and pin them
# in .claude/memory/sources.tsv  (columns: slug, url, commit, upstream_date, cloned_on)
set -euo pipefail
# Owner rule (2026-09-27): shallow clones only (--depth 1). Full history stats are kept in
# .claude/memory/history.tsv instead of in the clones.
DEPTH=(--depth 1)

ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
SRC="$ROOT/original_sources"
LOCK="$ROOT/.claude/memory/sources.tsv"
# Allowlist of submodules to fetch (owner rule 2026-09-27: only when explicitly gateware, e.g. USB cores).
SUBS="$ROOT/.claude/memory/submodules.tsv"
mkdir -p "$SRC"
[ -f "$LOCK" ] || printf 'slug\turl\tcommit\tupstream_date\tcloned_on\n' > "$LOCK"
[ -f "$SUBS" ] || printf 'slug\tpath\turl\tcommit\treason\n' > "$SUBS"
# ssh submodule URLs (git@host:) are fetched over https.
GITSUB=(-c url.https://github.com/.insteadOf=git@github.com: -c url.https://gitlab.com/.insteadOf=git@gitlab.com:)

fetch_sub() {  # slug path  -> shallow-fetch one submodule at the commit recorded by the superproject
  git "${GITSUB[@]}" -C "$SRC/$1" submodule update --quiet --init --depth 1 -- "$2"
}

slug_of() {  # https://github.com/Owner/Repo(.git) -> owner__repo
  local u="${1%.git}"; u="${u%/}"
  local repo="${u##*/}"; local rest="${u%/*}"; local owner="${rest##*/}"
  printf '%s__%s' "${owner,,}" "${repo,,}"
}

pin() {  # slug url
  local dir="$SRC/$1"
  local commit date
  commit="$(git -C "$dir" rev-parse HEAD)"
  date="$(git -C "$dir" log -1 --format=%cs)"
  grep -v -P "^\Q$1\E\t" "$LOCK" > "$LOCK.tmp" || true
  printf '%s\t%s\t%s\t%s\t%s\n' "$1" "$2" "$commit" "$date" "$(date +%F)" >> "$LOCK.tmp"
  { head -n1 "$LOCK.tmp"; tail -n +2 "$LOCK.tmp" | sort; } > "$LOCK"
  rm -f "$LOCK.tmp"
  echo "pinned $1 @ ${commit:0:12} (upstream last commit $date)"
}

case "${1:-}" in
  --restore)
    tail -n +2 "$LOCK" | while IFS=$'\t' read -r slug url commit _ _; do
      [ -z "$slug" ] && continue
      if [ ! -d "$SRC/$slug/.git" ]; then git clone --quiet "${DEPTH[@]}" "$url" "$SRC/$slug"; fi
      git -C "$SRC/$slug" fetch --quiet "${DEPTH[@]}" origin "$commit" 2>/dev/null || echo "WARN $slug: pinned commit not fetchable, staying on upstream HEAD" >&2
      git -C "$SRC/$slug" checkout --quiet "$commit" 2>/dev/null || true
      echo "restored $slug @ ${commit:0:12}"
    done
    tail -n +2 "$SUBS" | while IFS=$'\t' read -r slug path _ _ _; do
      [ -z "$slug" ] && continue
      fetch_sub "$slug" "$path" && echo "restored submodule $slug/$path" || echo "WARN $slug/$path: submodule fetch failed" >&2
    done ;;
  --submodule)
    slug="${2:?usage: clone.sh --submodule <slug> <path> <reason>}"; path="${3:?path}"; reason="${4:?reason (why it is gateware)}"
    [ -d "$SRC/$slug/.git" ] || { echo "$slug not cloned" >&2; exit 1; }
    url="$(git -C "$SRC/$slug" config -f .gitmodules --get-regexp '\.path$' | awk -v p="$path" '$2==p{print $1}' | sed 's/\.path$/.url/' | xargs -r git -C "$SRC/$slug" config -f .gitmodules --get)"
    [ -n "$url" ] || { echo "no submodule at $path in $slug" >&2; exit 1; }
    fetch_sub "$slug" "$path"
    commit="$(git -C "$SRC/$slug/$path" rev-parse HEAD)"
    grep -v -P "^\Q$slug\E\t\Q$path\E\t" "$SUBS" > "$SUBS.tmp" || true
    printf '%s\t%s\t%s\t%s\t%s\n' "$slug" "$path" "$url" "$commit" "$reason" >> "$SUBS.tmp"
    { head -n1 "$SUBS.tmp"; tail -n +2 "$SUBS.tmp" | sort; } > "$SUBS"; rm -f "$SUBS.tmp"
    echo "submodule $slug/$path @ ${commit:0:12} ($(du -sh "$SRC/$slug/$path" | cut -f1))" ;;
  --update)
    slug="${2:?usage: clone.sh --update <slug>}"
    url="$(awk -F'\t' -v s="$slug" '$1==s{print $2}' "$LOCK")"
    [ -n "$url" ] || { echo "unknown slug $slug" >&2; exit 1; }
    br="$(git -C "$SRC/$slug" rev-parse --abbrev-ref HEAD)"
    git -C "$SRC/$slug" fetch --quiet "${DEPTH[@]}" origin "$br"
    git -C "$SRC/$slug" reset --quiet --hard FETCH_HEAD
    pin "$slug" "$url" ;;
  ""|-h|--help)
    sed -n '2,3p' "$0"; echo "usage: clone.sh <git-url> | --restore | --update <slug> | --submodule <slug> <path> <reason>"; exit 0 ;;
  *)
    url="$1"; slug="$(slug_of "$url")"
    if [ -d "$SRC/$slug/.git" ]; then echo "$slug already cloned (use --update)"; else git clone --quiet "${DEPTH[@]}" "$url" "$SRC/$slug"; fi
    pin "$slug" "$url" ;;
esac
