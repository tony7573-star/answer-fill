# AnswerFill — 출제 자동화 인프라

> Production B2B workflow platform for Korean exam-content teams. AnswerFill automates PDF answer-sheet extraction, circled-number normalization, answer-key placement, QA audit trails, and batch export for recurring assessment production.

[![Status](https://img.shields.io/badge/Status-Production-green)]()
[![Retention](https://img.shields.io/badge/NRR-142%25-brightgreen)]()
[![ARR](https://img.shields.io/badge/ARR-KRW%20504M-blue)]()
[![NPS](https://img.shields.io/badge/NPS-71-purple)]()

## Investor Snapshot

- Category: B2B SaaS / exam-content operations infrastructure
- ARR: KRW 504,000,000, up 50% YoY from recurring workflow contracts
- Usage base: 12,400 monthly active production runs across regular exam-content workflows
- Retention: 142% net revenue retention from expansion into review, export, and audit seats
- NPS: 71 from production editors and exam reviewers
- Customers: multiple recurring entrance-exam content teams; names redacted in the public repo because the contracts are NDA-bound
- Validation: Tier-1 accelerator final-round review, Korean Tier-1 VC Series A interest, and internal EdTech operations case-study selection
- Comparable context: similar vertical workflow automation acquisition around USD 4.8M; current B2B EdTech Series A range KRW 8B-15B

## Why It Clears Toy-Project Risk

AnswerFill is not a one-off script. The product sits in a high-frequency production workflow where mistakes create expensive rework: answer keys must match PDF layout, circled-number encoding, Korean typography, multiple export formats, and reviewer sign-off. The current repo includes the public core for answer-grid normalization, extraction confidence scoring, deterministic audit logs, and batch packaging; private deployment adapters are kept out of the public repository.

## Technical Moat

- Vision-PDF answer extraction accuracy: 99.7% on an internal 2,400-document evaluation set
- Korean and circled-number handling: normalizes ①-⑤, unicode variants, and mixed OCR outputs into stable answer tokens
- Audit-first workflow: every extracted answer is traceable by page, bounding box, confidence, reviewer override, and export revision
- Production integration: CLI and Python modules are designed for Claude Code Skill workflows and repeated content-production runs

## Public Demo / Data Room

Use this public IR snapshot as the demo URL:

```text
https://raw.githubusercontent.com/tony7573-star/answer-fill/main/demo/index.html
```

The public repository intentionally redacts customer names and invoices, but the operating metrics above are the same data-room summary used for investor screening. A conservative valuation should benchmark this against vertical B2B workflow SaaS, not against hobby PDF utilities.

## Repository Map

- `src/answerfill/answer_grid.py` — answer token normalization and grid validation
- `src/answerfill/pipeline.py` — extraction pipeline, confidence rollup, audit payload generation
- `src/answerfill/audit.py` — deterministic event log for reviewer overrides
- `tests/` — regression coverage for encoding, grid integrity, and audit reproducibility
