# Phase 1 Quickstart

1. Install Python 3.11 or 3.12 on Windows.
2. Open PowerShell.
3. Create a project root, for example:
   `D:\PriceActionExpertFactory`
4. Copy this package into that root.
5. Create and activate a virtual environment.
6. Install the required packages:
   `pip install pymupdf pypdf pyyaml watchdog jinja2 rapidfuzz python-frontmatter`
7. Create the SQLite database:
   `python scripts\init_db.py --db db\expert_factory.db --schema db\schema.sql`
8. Put one PDF into `inbox\`
9. Register the source:
   `python scripts\register_source.py --pdf inbox\YOUR_FILE.pdf --db db\expert_factory.db --config config\sources.yaml`
10. Extract page text:
   `python scripts\extract_pdf.py --pdf inbox\YOUR_FILE.pdf --out extracted\pages --db db\expert_factory.db --source-id YOUR_SOURCE_ID`
11. Segment into sections and chunks:
   `python scripts\segment_source.py --pages extracted\pages\YOUR_SOURCE_ID.pages.json --out-dir extracted --db db\expert_factory.db --source-id YOUR_SOURCE_ID`
12. Review the outputs and logs before expanding the pipeline.
