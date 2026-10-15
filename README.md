# Lattice paths

Mathematical research by **Nicholas Ham** in enumerative combinatorics, lattice paths, generating functions and algebraic combinatorics. Starting sources: [Ham's 2019 conjectures](https://n-ham.com/old-website/pdfs/Lattice%20Path%20Conjectures.pdf) and [East–Ham, arXiv:1811.05735v3](https://arxiv.org/abs/1811.05735v3).

Phase2 establishes an exact finite **residue-rigidity classification** for growing triangular layers, plus explicit classical excursion/tree/Dyck/polygon bijections. The cumulative150-claim ledger records **57 established/answered,19 disproved,62 unresolved,10 numerical-table claims verified and2 context entries**. Of150 IDs,131 received full or partial investigation; this is not131 solved claims. All697 printed table values agree with exact recomputation, with two axis-label typos recorded.

The seven-page manuscript distinguishes historical factorial results, classical bijections and the independently proved classification whose priority remains unresolved. No novelty or submission-readiness claim is made.

## Reading order

- [Current handover](research/handover-phase2.md), [mathematical summary](research/mathematical-summary.md), [first-pass handover](research/handover.md), [roadmap](research/roadmap.md).
- [Complete conjecture inventory](research/conjecture-inventory.md), [machine-readable extraction](research/conjecture-inventory.json), [subsequent audit](research/conjecture-audit.md), [current claim statuses](research/phase2-claim-status.json).
- [Foundation proofs](research/foundation.md), [literature and East–Ham analysis](research/literature-review.md), [generalizations](research/generalizations.md).
- [Internal reviews](reviews/review-log.md), [source provenance](sources/README.md), [original algorithms audit](sources/algorithms-audit.md).
- Manuscript source `paper/main.tex`; compiled output `paper/build/main.pdf` (ignored build product).

## Reproduce

Python 3.10+ standard library, pdfLaTeX, BibTeX and latexmk (TeX Live with AMS, geometry, hyperref, Latin Modern):

```sh
./scripts/validate.sh
```

No source cache or network is needed for these checks. PDFs and historical code are ignored under `.local/references/`; retrieval links and hashes are recorded. Independent code uses finite DAGs and step-membership predicates, with explicit scope limits; see [experiments](experiments/README.md). It does not solve every infinite-step problem.

This is separate from [symmetric-games](https://github.com/n-ham-research/symmetric-games), whose audit/provenance conventions informed the infrastructure. Licensing is reserved; see LICENSE. James East has not been contacted. No submission is authorized.
