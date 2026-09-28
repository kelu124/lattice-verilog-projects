# Build the GitHub Pages site (docs/) from the JSON in data/. docs/ is generated: never edit it by hand.
# `make lpfs` rescans the local clones (original_sources/) into data/lpfs.json first.
SK := .claude/skills

.PHONY: docs lpfs catalogue pages

docs: catalogue pages
	python3 $(SK)/review-gateware-project/gen_lpf_catalogue.py

catalogue:
	python3 $(SK)/review-gateware-project/gen_catalogue.py

pages:
	python3 $(SK)/documentation/gen_site.py

lpfs:
	python3 $(SK)/review-gateware-project/scan_lpfs.py
	python3 $(SK)/review-gateware-project/gen_lpf_catalogue.py

.PHONY: usage check
usage:
	python3 $(SK)/review-gateware-project/scan_core_usage.py

check:
	python3 $(SK)/documentation/check_data.py
