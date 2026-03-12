# phase-01-manual

## Goal
Establish the local Windows creation stack and prove one-book ingestion end to end.

## Intended Phase 1 deliverables
- project root structure
- Python virtual environment
- required packages installed
- SQLite DB initialized
- one foundation PDF registered
- page JSON produced
- section JSON produced
- chunk JSON produced
- starter templates in place
- optional pipeline and watcher available

## What actually happened
### Confirmed done
- root structure exists
- `.venv` exists
- dependencies installed
- `db/expert_factory.db` initialized and active
- `brooks_trends_2012` processed successfully
- pages/sections/chunks JSON created
- knowledge and vault folder structure exists

### Confirmed not done
- no Obsidian notes written
- no logs present in `logs/`
- no validated concept extraction or merge quality
- no Mem0/OpenClaw work

## Key commands used
```powershell
python scripts\init_db.py --db db\expert_factory.db --schema db\schema.sql
python scripts\register_source.py --pdf inbox\Brooks_2012_Trading_Price_Action_Trends.pdf --db db\expert_factory.db --config config\sources.yaml
python scripts\extract_pdf.py --pdf inbox\Brooks_2012_Trading_Price_Action_Trends.pdf --out extracted\pages --db db\expert_factory.db --source-id brooks_trends_2012
python scripts\segment_source.py --pages extracted\pages\brooks_trends_2012.pages.json --out-dir extracted --db db\expert_factory.db --source-id brooks_trends_2012
```

## Phase 1 findings
### Good enough to continue
- extraction is usable for text-first books
- contents and glossary are detectable
- canonical source policy is already encoded

### Not good enough yet
- section classification needs hardening
- front matter handling needs cleanup
- logging/reporting needs to exist or docs must stop promising logs
- live note writing needs proof

## Lessons learned
1. keep DB path consistent
2. keep source IDs stable
3. inspect JSON manually after each run
4. do not broaden to all four books before hardening extraction quality
5. do not rely on chat memory for project state; commit continuity files

## Phase 1 final status
**Successful as a baseline scaffold. Incomplete as an expert-knowledge pipeline.**
