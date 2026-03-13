# RUNBOOK

## Purpose

Operational runbook for the local Windows pipeline.

## Preconditions

* repo/package copied into local working root
* Python environment active
* dependencies installed
* `db/schema.sql` present
* `config/sources.yaml` matches actual file names
* target PDF copied into `inbox/`

## Standard Phase 1 run order

### 1\. Initialize DB

```powershell
python scripts\\init\_db.py --db db\\expert\_factory.db --schema db\\schema.sql
```

### 2\. Register source

```powershell
Copy config/sources.example.yaml → config/sources.yaml (once)

python scripts\\register\_source.py --pdf inbox\\Brooks\_2012\_Trading\_Price\_Action\_Trends.pdf --db db\\expert\_factory.db --config config\\sources.yaml```

### 3\. Extract pages

```powershell
python scripts\\extract\_pdf.py --pdf inbox\\Brooks\_2012\_Trading\_Price\_Action\_Trends.pdf --out extracted\\pages --db db\\expert\_factory.db --source-id brooks\_trends\_2012
```

### 4\. Segment to sections and chunks

```powershell
python scripts\\segment\_source.py --pages extracted\\pages\\brooks\_trends\_2012.pages.json --out-dir extracted --db db\\expert\_factory.db --source-id brooks\_trends\_2012
```

## Optional Phase 1 orchestration

```powershell
python scripts\\run\_pipeline.py --pdf inbox\\Brooks\_2012\_Trading\_Price\_Action\_Trends.pdf --root C:\\PAFactory --source-id brooks\_trends\_2012
```

## Optional inbox watcher

```powershell
python scripts\\watch\_inbox.py --root C:\\PAFactory
```

## Inspection routine after each run

1. inspect DB
2. inspect page JSON
3. inspect sections JSON
4. inspect chunks JSON
5. confirm outputs exist in the expected folders
6. only then proceed to the next book

## Minimum success criteria

* DB initializes
* source registers without error
* page JSON created
* section JSON created
* chunk JSON created
* outputs look human-plausible

## Known Phase 1 realities

* logs were expected by the guide but no log files were present in `logs/`
* section labeling is usable but imperfect
* note writing is not yet proven in live use

## Common failure patterns

### Database mismatch

Symptom: `no such table: sources`
Cause: wrong DB file path used after initializing a different DB
Fix: use the same DB path consistently: `db\\expert\_factory.db`

### Source ID mismatch

Symptom: registration/extraction uses unknown or unstable IDs
Fix: always use IDs from `config/sources.yaml`

### Guide path mismatch

Symptom: docs refer to `D:\\PriceActionExpertFactory` but actual project is in `C:\\PAFactory`
Fix: use actual local root for commands; keep docs explicit about which is example vs actual

### Weak section classification

Symptom: front matter or glossary pages mislabeled as chapter body or contents
Fix: treat as a Phase 2 hardening task, not a Phase 1 blocker

## Recommended next processing order

1. `brooks\_trends\_2012`
2. `brooks\_trading\_ranges\_2012`
3. `brooks\_reversals\_2012`
4. `brooks\_bar\_by\_bar\_2009`

## Do not change yet

* source IDs
* source priority order
* ontology family names
* schema without a documented decision

