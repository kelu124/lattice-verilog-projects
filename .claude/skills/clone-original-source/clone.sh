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
mkdir -p "$SRC"
[ -f "$LOCK" ] || printf 'slug\turl\tcommit\tupstream_date\tcloned_on\n' > "$LOCK"

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
    done ;;
  --update)
    slug="${2:?usage: clone.sh --update <slug>}"
    url="$(awk -F'\t' -v s="$slug" '$1==s{print $2}' "$LOCK")"
    [ -n "$url" ] || { echo "unknown slug $slug" >&2; exit 1; }
    br="$(git -C "$SRC/$slug" rev-parse --abbrev-ref HEAD)"
    git -C "$SRC/$slug" fetch --quiet "${DEPTH[@]}" origin "$br"
    git -C "$SRC/$slug" reset --quiet --hard FETCH_HEAD
    pin "$slug" "$url" ;;
  ""|-h|--help)
    sed -n '2,3p' "$0"; echo "usage: clone.sh <git-url> | --restore | --update <slug>"; exit 0 ;;
  *)
    url="$1"; slug="$(slug_of "$url")"
    if [ -d "$SRC/$slug/.git" ]; then echo "$slug already cloned (use --update)"; else git clone --quiet "${DEPTH[@]}" "$url" "$SRC/$slug"; fi
    pin "$slug" "$url" ;;
esac
