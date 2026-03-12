# CHANGELOG

## 2026-03-12 — Continuity recovery baseline
### Added
- continuity pack drafted from recovered Phase 1 evidence
- canonical project state documentation
- file map, runbook, architecture, and decisions records
- explicit distinction between repo spine and local artifacts

### Confirmed
- active DB is `db/expert_factory.db`
- first processed source was `brooks_trends_2012`
- pages, sections, and chunks were generated for Trends
- no Obsidian notes were written yet
- no log files were present in `logs/`

### Clarified
- 2012 trilogy is canonical backbone
- 2009 book is lineage/reference
- GitHub repo should remain code/docs/config only
- generated corpus artifacts and PDFs must stay out of Git

## Earlier project history
### Phase 1 design decisions established in chat
- Windows-first local creation stack
- Python + SQLite + Obsidian architecture
- watched-folder friendly workflow
- text-first extraction
- later semantic layer built on top of source-grounded artifacts

### Phase 1 package created
- project scaffold
- starter scripts
- schema
- templates
- user guide PDF and markdown docs
