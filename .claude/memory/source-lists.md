---
name: source-lists
description: Where lists of ULX3S projects come from (ulx3s.github.io "Projects and examples", emard/ulx3s links, GitHub search) and when each was last harvested — used to re-sync the collection.
metadata:
  type: reference
---

| Source | Harvested | Result |
|---|---|---|
| https://ulx3s.github.io/ section "Projects and examples" (between "ULX3S manual" and "Gitee examples") | 2026-09-27 | 69 git URLs; 68 cloned. `emard/ulx3s-examples` is 404 (use `ulx3s/ulx3s-examples`). Not clonable: BLE gist (vmedea), YouTube logic-analyzer video, bonfirecpu.eu blog, nxlab.fer.hr FPGArduino page |
| emard/ulx3s README + MANUAL links | 2026-09-27 | candidates in [[projects]] |
| emard/ulx3s-bin folder sources | 2026-09-27 | see docs/projects/emard__ulx3s-bin.md |
| GitHub search (repos/topics/code for ulx3s) | 2026-09-27 (in progress) | see [[projects]] |

The ulx3s.github.io page also has a "Gitee examples" section (Chinese mirror/examples), not yet harvested.

**How to apply:** to refresh the collection, re-fetch these sources, diff the list against
`sources.tsv`, clone new ones with `clone.sh`, and add a row for each here with the new date.
Many ulx3s.github.io entries list two URLs (an original and an `ulx3s/` or `emard/` fork); both
were cloned, and the registry notes which copy has the ULX3S port.
