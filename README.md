# PAFactory

Local-first Windows pipeline for building a source-grounded **Price Action Expert** from the Brooks foundation books and later related articles, transcripts, and Q&A material.

This repository is the **canonical project spine** for the factory itself:
- code
- configuration templates
- schema
- docs and runbooks
- templates
- continuity/state files

This repository is **not** the corpus store.

## What this project is

The goal is to build a repeatable creation stack that:
1. ingests source PDFs locally on Windows
2. extracts page, section, and chunk artifacts
3. stores run state in SQLite
4. later extracts candidate knowledge objects and merges them into a canonical ontology
5. later writes curated notes to Obsidian
6. later exports approved distilled knowledge to Mem0 / OpenClaw

## Canonical source hierarchy

The initial foundation corpus is fixed:
1. **Trading Price Action Trends (2012)** — canonical priority 1
2. **Trading Price Action Trading Ranges (2012)** — canonical priority 2
3. **Trading Price Action Reversals (2012)** — canonical priority 3
4. **Reading Price Charts Bar by Bar (2009)** — lineage/reference only

The 2012 trilogy is the canonical structural backbone. The 2009 book is retained as predecessor/reference support.

## Current project state

Phase 1 has been implemented as a starter local pipeline.

### Confirmed working in Phase 1
- Windows project spine exists
- Python virtual environment exists
- SQLite database exists: `db/expert_factory.db`
- `brooks_trends_2012` was processed successfully
- page JSON exists
- section JSON exists
- chunk JSON exists
- `runs/`, `knowledge/`, and `vault/` folder structure exists

### Not yet completed in Phase 1
- no Obsidian notes were written
- no run logs were produced in `logs/`
- no proven concept extraction / merge quality yet
- no Mem0 export
- no OpenClaw integration

## Repo boundary

Track in Git:
- `config/`
- `db/schema.sql`
- `docs/`
- `scripts/`
- `templates/`
- continuity files such as `PROJECT_STATE.md`, `FILE_MAP.md`, `RUNBOOK.md`, `CHANGELOG.md`, `architecture.md`, `decisions.md`

Do **not** track:
- copyrighted PDFs
- full extracted book text
- local database files
- generated run artifacts
- local Obsidian vault contents
- secrets or machine-specific config

## Recommended local root

Current local project root observed in practice:
- `C:\PAFactory`

Original Phase 1 guide example path:
- `D:\PriceActionExpertFactory`

From this point forward, project docs should acknowledge both:
- **canonical repo name**: `PAFactory`
- **current local working root**: `C:\PAFactory`

## Quickstart

1. Create and activate `.venv`
2. Install dependencies
3. Initialize DB:
   `python scripts\init_db.py --db db\expert_factory.db --schema db\schema.sql`
4. Put one configured PDF in `inbox\`
5. Register source:
   `python scripts\register_source.py --pdf inbox\Brooks_2012_Trading_Price_Action_Trends.pdf --db db\expert_factory.db --config config\sources.yaml`
6. Extract pages:
   `python scripts\extract_pdf.py --pdf inbox\Brooks_2012_Trading_Price_Action_Trends.pdf --out extracted\pages --db db\expert_factory.db --source-id brooks_trends_2012`
7. Segment into sections/chunks:
   `python scripts\segment_source.py --pages extracted\pages\brooks_trends_2012.pages.json --out-dir extracted --db db\expert_factory.db --source-id brooks_trends_2012`

## Phase roadmap

- **Phase 1** — local scaffold, one-book proof, page/section/chunk extraction
- **Phase 2** — harden extraction, candidate extraction, first ontology objects, first note writing
- **Phase 3** — merge/canonicalization, review workflow, Obsidian refinement
- **Phase 4** — Mem0/OpenClaw bridge

## Immediate next step

Before Phase 2, stabilize continuity:
- commit the continuity pack
- keep repo private
- treat GitHub as the canonical project spine
- harden Phase 1 against the actual outputs, not the ideal plan
