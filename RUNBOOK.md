# RUNBOOK

## Purpose
Operational runbook for the local Windows pipeline.

## Preconditions
- repo/package copied into local working root
- Python environment active
- dependencies installed
- `db/schema.sql` present
- `config/sources.yaml` matches actual file names
- target PDF copied into `inbox/`

## Standard Phase 1 run order

### 1. Initialize DB
```powershell
python scripts\init_db.py --db db\expert_factory.db --schema db\schema.sql
```

### 2. Register source
```powershell
python scripts\register_source.py --pdf inbox\Brooks_2012_Trading_Price_Action_Trends.pdf --db db\expert_factory.db --config config\sources.yaml
```

### 3. Extract pages
```powershell
python scripts\extract_pdf.py --pdf inbox\Brooks_2012_Trading_Price_Action_Trends.pdf --out extracted\pages --db db\expert_factory.db --source-id brooks_trends_2012
```

### 4. Segment to sections and chunks
```powershell
python scripts\segment_source.py --pages extracted\pages\brooks_trends_2012.pages.json --out-dir extracted --db db\expert_factory.db --source-id brooks_trends_2012
```

## Optional Phase 1 orchestration
```powershell
python scripts\run_pipeline.py --pdf inbox\Brooks_2012_Trading_Price_Action_Trends.pdf --root C:\PAFactory --source-id brooks_trends_2012
```

## Optional inbox watcher
```powershell
python scripts\watch_inbox.py --root C:\PAFactory
```

## Inspection routine after each run
1. inspect DB
2. inspect page JSON
3. inspect sections JSON
4. inspect chunks JSON
5. confirm outputs exist in the expected folders
6. only then proceed to the next book

## Minimum success criteria
- DB initializes
- source registers without error
- page JSON created
- section JSON created
- chunk JSON created
- outputs look human-plausible

## Known Phase 1 realities
- logs were expected by the guide but no log files were present in `logs/`
- section labeling is usable but imperfect
- note writing is not yet proven in live use

## Common failure patterns
### Database mismatch
Symptom: `no such table: sources`
Cause: wrong DB file path used after initializing a different DB
Fix: use the same DB path consistently: `db\expert_factory.db`

### Source ID mismatch
Symptom: registration/extraction uses unknown or unstable IDs
Fix: always use IDs from `config/sources.yaml`

### Guide path mismatch
Symptom: docs refer to `D:\PriceActionExpertFactory` but actual project is in `C:\PAFactory`
Fix: use actual local root for commands; keep docs explicit about which is example vs actual

### Weak section classification
Symptom: front matter or glossary pages mislabeled as chapter body or contents
Fix: treat as a Phase 2 hardening task, not a Phase 1 blocker

## Recommended next processing order
1. `brooks_trends_2012`
2. `brooks_trading_ranges_2012`
3. `brooks_reversals_2012`
4. `brooks_bar_by_bar_2009`

## Do not change yet
- source IDs
- source priority order
- ontology family names
- schema without a documented decision
