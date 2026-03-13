\# PAFactory



PAFactory is a Windows-first local pipeline for turning a fixed corpus of trading books and later related text sources into a structured, reviewable expert-knowledge base.



The initial foundation corpus is the four Al Brooks books. The 2012 trilogy is treated as the canonical structural backbone. The 2009 book is treated as predecessor and lineage reference.



\## Current status



Phase 1 is mechanically successful enough to baseline.



Confirmed on the current local machine:

\- active database: `db/expert\\\\\\\_factory.db`

\- first successfully processed source: `brooks\\\\\\\_trends\\\\\\\_2012`

\- page, section, and chunk JSON outputs were created

\- no Obsidian notes were written yet

\- no log files were present in `logs\\\\\\\\`



Phase 1 proved the local project spine and basic extraction flow. It did not yet prove high-quality semantic extraction, canonicalization quality, or production-ready note writing.



\## Project goals



\- keep the project local-first

\- preserve source provenance

\- build a canonical machine-readable knowledge layer

\- build a human-readable Obsidian knowledge layer

\- later export approved distilled knowledge to runtime systems such as Mem0 / OpenClaw



\## Canonical source hierarchy



1\. `brooks\\\\\\\_trends\\\\\\\_2012`

2\. `brooks\\\\\\\_trading\\\\\\\_ranges\\\\\\\_2012`

3\. `brooks\\\\\\\_reversals\\\\\\\_2012`

4\. `brooks\\\\\\\_bar\\\\\\\_by\\\\\\\_bar\\\\\\\_2009` as lineage reference



\## Repository policy



This repository is the canonical project spine for:

\- code

\- schema

\- templates

\- configs

\- runbooks

\- continuity files

\- phase plans



This repository should not contain:

\- copyrighted source PDFs

\- full extracted book text

\- local database files

\- generated run artifacts

\- real local vault contents

\- secrets



\## Top-level files



\- `PROJECT\\\\\\\_STATE.md` — current factual project state

\- `FILE\\\\\\\_MAP.md` — file and folder purpose map

\- `RUNBOOK.md` — operational steps and recovery guidance

\- `CHANGELOG.md` — project change history

\- `docs/architecture.md` — system architecture

\- `docs/decisions.md` — important design decisions

\- `docs/phase-01-manual.md` — recovered Phase 1 implementation record

\- `docs/phase-02-plan.md` — Phase 2 target plan



\## Core folders



\- `config/` — config templates and controlled project settings

\- `db/` — SQLite schema

\- `docs/` — architecture, decisions, phase documents

\- `scripts/` — local pipeline scripts

\- `templates/` — Obsidian and related note templates



\## Local-only folders



These are expected locally but should not be committed:

\- `inbox/`

\- `archive/`

\- `failed/`

\- `runs/`

\- `logs/`

\- `extracted/`

\- `knowledge/`

\- `vault/`

\- local `.db` files

\- local source PDFs



\## Phase 1 commands



Initialize the database:



python scripts\\init\_db.py --db db\\expert\_factory.db --schema db\\schema.sql



Register source:

&#x20; 1. Copy `config/sources.example.yaml` → `config/sources.yaml`

&#x20; 2. `python scripts\\register\_source.py --pdf inbox\\Brooks\_2012\_Trading\_Price\_Action\_Trends.pdf --db db\\expert\_factory.db --config config\\sources.yaml`



python scripts\\run\_pipeline.py --pdf inbox\\Brooks\_2012\_Trading\_Price\_Action\_Trends.pdf --db db\\expert\_factory.db --config config\\sources.yaml

