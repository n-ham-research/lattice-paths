# Lattice paths

Mathematical research by **Nicholas Ham** in enumerative combinatorics, lattice paths, generating functions and algebraic combinatorics. Starting sources: [Ham's 2019 conjectures](https://n-ham.com/old-website/pdfs/Lattice%20Path%20Conjectures.pdf) and [East–Ham, arXiv:1811.05735v3](https://arxiv.org/abs/1811.05735v3).

Phase5 prepares the existing rigidity and inverse results for **external mathematical scrutiny**. The polished manuscript remains nine pages and the James East briefing four. A focused adversarial audit retains the theorem assumptions; novelty remains unresolved. A small discussion package includes PDFs, sources, primary links and standard-library exact checks. An accompanying email is drafted locally and has not been sent.

The cumulative150-claim ledger records **58 established/answered,19 disproved,61 unresolved,10 numerical-table claims verified and2 context entries**. Of150 IDs,131 received full or partial investigation; this is not131 solved claims. Phase3 resolved the packed-word axis family; Phases4–5 leave those dispositions unchanged while treating structural theorems separately. All697 printed source-table values remain reproduced.

## Reading order

- [Current handover](research/handover-phase5.md), [phase4 handover](research/handover-phase4.md), [phase3 handover](research/handover-phase3.md), [phase2 handover](research/handover-phase2.md), [mathematical summary](research/mathematical-summary.md), [first-pass handover](research/handover.md), [roadmap](research/roadmap.md).
- [Complete conjecture inventory](research/conjecture-inventory.md), [machine-readable extraction](research/conjecture-inventory.json), [subsequent audit](research/conjecture-audit.md), [current claim statuses](research/phase3-claim-status.json).
- [Foundation proofs](research/foundation.md), [literature and East–Ham analysis](research/literature-review.md), [generalizations](research/generalizations.md).
- [Internal reviews](reviews/review-log.md), [source provenance](sources/README.md), [original algorithms audit](sources/algorithms-audit.md).
- Main manuscript `paper/main.tex` → `paper/build/main.pdf`; four-page briefing `briefing/main.tex` → `briefing/build/main.pdf` (ignored build products).
- [Focused proof audit](research/phase5-proof-audit.md), [novelty assessment](research/phase5-novelty-ledger.md), [general-q note](research/phase5-general-q.md), [publication structure](research/publication-structure-phase4.md).

## Discussion package

After building the PDFs, run `python3 scripts/build_review_package.py`. This creates the ignored `external-review/build/lattice-paths-review.zip`; extract it and run `python3 verification/verify.py` with Python3.10+ only. The package does not require the full environment or network. See [package README](external-review/README.md) and [unsent email draft](external-review/email-draft.txt).

## Reproduce

Python 3.10+ standard library, pdfLaTeX, BibTeX and latexmk (TeX Live with AMS, geometry, hyperref, Latin Modern):

```sh
./scripts/validate.sh
```

No source cache or network is needed for these checks. PDFs and historical code are ignored under `.local/references/`; retrieval links and hashes are recorded. Independent code uses finite DAGs and step-membership predicates, with explicit scope limits; see [experiments](experiments/README.md). It does not solve every infinite-step problem.

This is separate from [symmetric-games](https://github.com/n-ham-research/symmetric-games), whose audit/provenance conventions informed the infrastructure. Licensing is reserved; see LICENSE. James East has not been contacted. No submission is authorized.
