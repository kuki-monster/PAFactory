# decisions

## D-001 — GitHub repo is the canonical project spine
Status: accepted

The repo is the durable continuity backbone for the project factory itself.

Implication:
- code/docs/config/schema/templates belong in Git
- generated corpus artifacts do not

## D-002 — Local Windows execution remains primary
Status: accepted

The creation stack runs locally on Windows.

Implication:
- paths and runbooks must remain Windows-first
- no Docker requirement in the baseline

## D-003 — 2012 trilogy is canonical, 2009 is lineage/reference
Status: accepted

Canonical priority:
1. Trends 2012
2. Trading Ranges 2012
3. Reversals 2012
4. Bar by Bar 2009

Implication:
- naming, ontology, and merge policy prefer trilogy wording
- 2009 is support/lineage, not primary taxonomy

## D-004 — Obsidian is the human-facing knowledge layer
Status: accepted

Implication:
- notes should be written only after semantic quality is acceptable
- vault structure is part of the architecture, not an afterthought

## D-005 — Mem0 / OpenClaw come after curation
Status: accepted

Implication:
- raw document chunks do not go straight into runtime memory
- only approved distilled knowledge should be exported later

## D-006 — Phase 1 was a mechanical proof, not semantic proof
Status: accepted

Implication:
- do not treat current extracted outputs as trusted expert knowledge yet
- Phase 2 must harden extraction/classification and start controlled candidate extraction

## D-007 — Stable source IDs are mandatory
Status: accepted

Implication:
- `source_id` values in `config/sources.yaml` must not drift
- downstream DB/object references depend on stability

## D-008 — Repo must stay private
Status: proposed if not already done

Implication:
- reduce risk of accidental exposure
- avoid exposing evolving project internals and future artifacts

## D-009 — Guide example path and real working path must both be documented
Status: accepted

Observed:
- original manual used `D:\PriceActionExpertFactory`
- actual recovered working root is `C:\PAFactory`

Implication:
- future docs must state clearly whether a path is example or actual local root
