# FILE_MAP

## Root
`C:\PAFactory`

## Top-level folders

### `config/`
Configuration for sources, ontology families, and export rules.
- `sources.yaml`
- `families.yaml`
- `export_rules.yaml`

### `db/`
Database artifacts and schema.
- `schema.sql` — canonical schema file tracked in Git
- `expert_factory.db` — active local DB, not for Git

### `docs/`
Human-facing implementation docs.
- `PHASE_1_QUICKSTART.md`
- `PHASE_1_USER_GUIDE.md`
- `Price_Action_Expert_Factory_Phase_1_User_Guide.pdf`

### `scripts/`
Operational Python scripts.
- `init_db.py` — initialize SQLite schema
- `register_source.py` — register a source PDF against configured source IDs
- `extract_pdf.py` — page-level extraction
- `segment_source.py` — section/chunk generation
- `run_pipeline.py` — orchestrator for Phase 1
- `watch_inbox.py` — watched-folder automation entry point
- `write_obsidian.py` — note-writing scaffold
- `_common.py` — shared helpers

### `templates/`
Markdown note templates.
- `source_book.md`
- `concept.md`
- `pattern.md`
- `setup.md`
- `principle.md`
- `context_rule.md`
- `nuance_note.md`

### `extracted/`
Generated extraction artifacts.
- `pages/`
- `sections/`
- `chunks/`
- `figures/`

Confirmed files:
- `pages/brooks_trends_2012.pages.json`
- `sections/brooks_trends_2012.sections.json`
- `chunks/brooks_trends_2012.chunks.json`

### `knowledge/`
Downstream knowledge objects.
- `candidates/`
- `canonical/`
- `review/`
- `exports/`

These folders exist. Semantic quality/status remains to be validated in Phase 2.

### `vault/`
Obsidian target structure.
- `00_System/`
- `01_Sources/`
- `02_Glossary/`
- `03_Concepts/`
- `04_Patterns/`
- `05_Setups/`
- `06_Procedures/`
- `07_Principles/`
- `08_Context_Rules/`
- `09_Nuance_Conflicts/`
- `10_Review/`

No notes have been confirmed written yet.

### `inbox/`
Local source drop folder.
Confirmed file:
- `Brooks_2012_Trading_Price_Action_Trends.pdf`

### `archive/`, `failed/`, `runs/`, `logs/`
Operational folders.
- `runs/` exists
- `logs/` exists but contained no files at the time of recovery

## Important repo boundary
Track:
- code
- docs
- configs (template-safe)
- schema
- templates
- continuity files

Do not track:
- PDFs
- extracted book JSON
- DB files
- local vault content
- generated run artifacts

## Important path note
Two roots appear in project history:
- guide/example root: `D:\PriceActionExpertFactory`
- actual recovered local root: `C:\PAFactory`

All future docs should clearly distinguish between:
- **example path in old manual**
- **actual current local working root**
