# Lattice paths

Mathematical research by **Nicholas Ham** in enumerative combinatorics, lattice paths, generating functions and algebraic combinatorics. Starting sources: [Ham's 2019 conjectures](https://n-ham.com/old-website/pdfs/Lattice%20Path%20Conjectures.pdf) and [East–Ham, arXiv:1811.05735v3](https://arxiv.org/abs/1811.05735v3).

Initial milestone: all **41 numbered sections and 150 individual source claims** inventoried; six step-set models in §§24–27 explained with precise support and index shifts. Exact DP through column 12 agrees with explicit word enumeration through column 5. Several literal source claims require correction. The alternating-factorial construction already has a 2015 proof by Danny Rorabaugh on OEIS. No novelty or human mathematical sign-off is claimed.

## Reading order

- [Handover](research/handover.md), [roadmap](research/roadmap.md).
- [Complete conjecture inventory](research/conjecture-inventory.md), [machine-readable extraction](research/conjecture-inventory.json), [subsequent audit](research/conjecture-audit.md).
- [Foundation proofs](research/foundation.md), [literature and East–Ham analysis](research/literature-review.md), [generalizations](research/generalizations.md).
- [Internal reviews](reviews/review-log.md), [source provenance](sources/README.md), [original algorithms audit](sources/algorithms-audit.md).
- Manuscript source `paper/main.tex`; compiled output `paper/build/main.pdf` (ignored build product).

## Reproduce

Python 3.10+ standard library, pdfLaTeX, BibTeX and latexmk (TeX Live with AMS, geometry, hyperref, Latin Modern):

```sh
python3 scripts/check_inventory.py
python3 -m unittest discover -s experiments/tests
python3 experiments/verify.py --check
./scripts/build.sh
```

No source cache or network is needed for these checks. PDFs and historical code are ignored under `.local/references/`; retrieval links and hashes are recorded. Independent code uses finite DAGs and step-membership predicates, with explicit scope limits; see [experiments](experiments/README.md). It does not solve every infinite-step problem.

This is separate from [symmetric-games](https://github.com/n-ham-research/symmetric-games), whose audit/provenance conventions informed the infrastructure. Licensing is reserved; see LICENSE. James East has not been contacted. No submission is authorized.
