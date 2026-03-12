# architecture

## Summary
PAFactory is a **local-first creation stack** for building a source-grounded Price Action Expert.

The architecture is intentionally layered.

## Layer 1 — Source layer
Purpose:
- preserve local source identity
- process PDFs into structured extraction artifacts
- support provenance and later reprocessing

Components:
- local PDF files in `inbox/`
- `register_source.py`
- `extract_pdf.py`
- `segment_source.py`
- SQLite `sources`, `runs`, `source_passages`
- generated page/section/chunk JSON

## Layer 2 — Knowledge construction layer
Purpose:
- derive candidate knowledge objects
- normalize terms
- merge overlapping concepts
- preserve nuance/conflict notes

Components:
- `knowledge/candidates/`
- `knowledge/canonical/`
- `knowledge/review/`
- future merge logic
- future ontology object records

Status:
- scaffold exists
- semantic quality not yet proven

## Layer 3 — Human-facing knowledge layer
Purpose:
- expose curated canonical knowledge in readable form
- support review and manual refinement

Components:
- `templates/`
- `vault/`
- `write_obsidian.py`

Status:
- structure exists
- no notes confirmed written yet

## Layer 4 — Runtime memory layer
Purpose:
- export distilled, approved knowledge to runtime systems

Components later:
- Mem0 export payloads
- OpenClaw expert/subagent integration

Status:
- not implemented in Phase 1

## Canonical source hierarchy
1. `brooks_trends_2012`
2. `brooks_trading_ranges_2012`
3. `brooks_reversals_2012`
4. `brooks_bar_by_bar_2009`

This hierarchy is encoded in config and must stay stable unless a decision record changes it.

## Data flow
1. PDF is copied into `inbox/`
2. source is registered against `sources.yaml`
3. page text is extracted to `extracted/pages`
4. pages are segmented into `sections` and `chunks`
5. DB stores run and passage metadata
6. later phases create canonical objects and notes
7. later approved knowledge is exported to runtime memory systems

## Current architectural gap
Phase 1 proved the mechanical extraction path, but not the semantic layer. The next work must harden classification and ontology extraction before broadening the corpus.
