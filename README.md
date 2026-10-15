# Lattice paths

Mathematical research by **Nicholas Ham** in enumerative combinatorics, lattice paths, generating functions and algebraic combinatorics. Starting sources: [Ham's 2019 conjectures](https://n-ham.com/old-website/pdfs/Lattice%20Path%20Conjectures.pdf) and [East–Ham, arXiv:1811.05735v3](https://arxiv.org/abs/1811.05735v3).

Phase3 focuses on **structural versus actual residue compression**: weighted boundary/funnel rigidity, finite-range trajectory obstructions on general growing windows and labelled endpoint-data reconstruction. The main paper remains seven pages; a separate four-page mathematical briefing states the strongest results and open questions. Historical priority and standalone publication value remain unresolved.

The cumulative150-claim ledger records **58 established/answered,19 disproved,61 unresolved,10 numerical-table claims verified and2 context entries**. Of150 IDs,131 received full or partial investigation; this is not131 solved claims. This pass newly resolves the packed-word axis family using its primary definition and formula. All697 printed source-table values remain reproduced.

## Reading order

- [Current handover](research/handover-phase3.md), [phase2 handover](research/handover-phase2.md), [mathematical summary](research/mathematical-summary.md), [first-pass handover](research/handover.md), [roadmap](research/roadmap.md).
- [Complete conjecture inventory](research/conjecture-inventory.md), [machine-readable extraction](research/conjecture-inventory.json), [subsequent audit](research/conjecture-audit.md), [current claim statuses](research/phase3-claim-status.json).
- [Foundation proofs](research/foundation.md), [literature and East–Ham analysis](research/literature-review.md), [generalizations](research/generalizations.md).
- [Internal reviews](reviews/review-log.md), [source provenance](sources/README.md), [original algorithms audit](sources/algorithms-audit.md).
- Main manuscript `paper/main.tex` → `paper/build/main.pdf`; four-page briefing `briefing/main.tex` → `briefing/build/main.pdf` (ignored build products).
- [Novelty ledger](research/phase3-novelty-ledger.md), [proposed publication structure](research/publication-structure-phase3.md).

## Reproduce

Python 3.10+ standard library, pdfLaTeX, BibTeX and latexmk (TeX Live with AMS, geometry, hyperref, Latin Modern):

```sh
./scripts/validate.sh
```

No source cache or network is needed for these checks. PDFs and historical code are ignored under `.local/references/`; retrieval links and hashes are recorded. Independent code uses finite DAGs and step-membership predicates, with explicit scope limits; see [experiments](experiments/README.md). It does not solve every infinite-step problem.

This is separate from [symmetric-games](https://github.com/n-ham-research/symmetric-games), whose audit/provenance conventions informed the infrastructure. Licensing is reserved; see LICENSE. James East has not been contacted. No submission is authorized.
