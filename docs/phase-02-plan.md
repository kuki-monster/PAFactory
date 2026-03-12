# phase-02-plan

## Phase 2 objective
Turn the Phase 1 mechanical pipeline into a controlled semantic pipeline for the Brooks foundation corpus.

## Phase 2 scope
1. harden section/content classification
2. introduce candidate extraction for concepts/definitions/principles/context rules
3. create first canonical object schema in practice
4. write first controlled Obsidian notes
5. introduce review queue behavior based on actual uncertainty
6. improve run logging/reporting

## Phase 2 is not for
- full OpenClaw integration
- Mem0 export at scale
- ingesting all secondary materials yet
- relying on embeddings before the symbolic layer is stable

## Proposed workstreams

### Workstream A — Extraction hardening
- improve front-matter detection
- distinguish contents vs glossary vs chapter body more reliably
- handle low-text pages explicitly
- make section grouping less coarse

### Workstream B — Candidate extraction
Start with a limited object set:
- concept
- definition
- principle
- context_rule

Avoid full pattern/setup/procedure breadth until the first extraction pass is validated.

### Workstream C — Review workflow
- define `candidate`, `approved`, `review_needed`, `rejected`
- send ambiguous cases to `knowledge/review/`
- make review reasons explicit

### Workstream D — Obsidian note writing
- prove `write_obsidian.py` against a staging subset
- write only a few note types first
- do not target the live knowledge base broadly until output quality is acceptable

### Workstream E — Logging
- create actual run logs or stop claiming they exist
- add per-run summaries to `runs/`

## Phase 2 recommended order
1. harden Trends processing first
2. rerun Trends cleanly
3. extract first candidate objects from Trends only
4. inspect quality manually
5. only then ingest Trading Ranges
6. then Reversals
7. 2009 book last as lineage/reference

## Entry criteria
- continuity pack committed
- repo private
- Phase 1 baseline accepted as factual

## Exit criteria
- improved sectioning on Trends
- first candidate object files generated and judged acceptable
- first notes written to a staging vault path
- repeatable rerun process documented
- one clear list of remaining blockers before full corpus expansion

## Success standard
At the end of Phase 2, the project should produce a **small number of believable canonical knowledge objects** from Trends, with source grounding and review discipline.
