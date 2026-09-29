#!/bin/bash
# Clone a list of repos, pinning each (clone.sh) and pruning it right away (prune.py), so big batches fit on disk.
# usage: clone_batch.sh list.txt       (one "owner/repo" per line for GitHub, or a full https URL for other forges)
# Prints OK <slug> <size before> -> <size after> [SUBMODULES] | HAVE <slug> | FAIL <line>.
# Submodules are NOT fetched: review the SUBMODULES lines and fetch gateware ones with clone.sh --submodule.
# Gitee clones can fail once with a TLS error: re-run the list (already-cloned slugs print HAVE).
ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
cd "$ROOT" || exit 1
while read -r r; do
  [ -z "$r" ] && continue
  case "$r" in http*) url="$r" ;; *) url="https://github.com/$r" ;; esac
  u="${url%.git}"; u="${u%/}"; s="$(basename "$(dirname "$u")")__$(basename "$u")"; s="${s,,}"
  if grep -qP "^\Q$s\E\t" .claude/memory/sources.tsv; then echo "HAVE $s"; continue; fi
  if timeout 600 .claude/skills/clone-original-source/clone.sh "$url" >/dev/null 2>&1; then
    sz=$(du -sh "original_sources/$s" | cut -f1)
    .claude/skills/clone-original-source/prune.py --apply "$s" >/dev/null
    echo "OK $s $sz -> $(du -sh "original_sources/$s" | cut -f1) $([ -f "original_sources/$s/.gitmodules" ] && echo SUBMODULES)"
  else
    echo "FAIL $r"; rm -rf "original_sources/$s"
  fi
done < "$1"
