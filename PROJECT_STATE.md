# PROJECT_STATE

## Snapshot date
2026-03-12

## Project identity
- Project name: `PAFactory`
- Purpose: local-first pipeline for building a source-grounded Price Action Expert
- Canonical spine: GitHub repo
- Human-facing knowledge layer: Obsidian vault
- Runtime memory layer later: Mem0 / OpenClaw

## Current phase
**Phase 1 complete enough to baseline, not complete enough to trust semantically.**

## What Phase 1 was supposed to do
Phase 1 was intended to establish the local Windows creation stack and prove the basic ingestion path for one foundation PDF:
- project structure
- Python environment
- SQLite DB
- source registration
- page extraction
- section and chunk creation
- starter templates
- optional pipeline orchestration and inbox watcher

## What Phase 1 actually did
Confirmed from local artifacts:
- `db/expert_factory.db` exists and is the active DB
- first processed source was `Brooks_2012_Trading_Price_Action_Trends.pdf`
- extracted artifacts exist for `brooks_trends_2012`
- generated folders exist for candidates, canonical, review, exports, runs, and vault
- no Obsidian notes were written
- no files were present in `logs/`

## Phase 1 outputs confirmed
- `extracted/pages/brooks_trends_2012.pages.json`
- `extracted/sections/brooks_trends_2012.sections.json`
- `extracted/chunks/brooks_trends_2012.chunks.json`

## Phase 1 quality assessment
### Strengths
- page extraction is usable
- contents and glossary are detectable
- introduction/body text is readable enough for further work
- source IDs and source priority are already defined
- schema and script spine are in place

### Weaknesses
- section classification is still rough
- some front matter is misclassified
- some low-text pages are still treated as chapter body
- no run logging exists yet despite the manual expecting logs
- no verified semantic extraction quality yet
- no verified note writing yet

## Canonical source policy
Locked unless explicitly changed by a later decision record:
1. `brooks_trends_2012` — canonical
2. `brooks_trading_ranges_2012` — canonical
3. `brooks_reversals_2012` — canonical
4. `brooks_bar_by_bar_2009` — lineage_reference

## Environment state observed
- Windows local project root: `C:\PAFactory`
- Python virtual environment present: `.venv`
- repo includes scripts, templates, configs, docs
- local DB file exists but must remain untracked

## Risks entering Phase 2
1. continuity loss across sessions if repo docs are not updated
2. semantic work started too early on noisy sectioning
3. generated artifacts accidentally committed
4. confusion between guide example path and actual local root
5. over-trusting Phase 1 outputs before validation of candidate extraction

## Entry criteria for Phase 2
Required before Phase 2 is considered active:
- continuity pack committed
- repo made private
- `.gitignore` verified against local artifacts
- actual Phase 1 state documented
- Phase 2 plan approved against real outputs

## Exit criteria for Phase 2
Target only; not yet completed:
- improved sectioning and content classification
- first candidate extraction pass
- first ontology object records
- first review queue behavior
- first controlled Obsidian note writing
