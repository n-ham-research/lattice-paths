# Lattice paths: mathematical discussion package

Nicholas Ham — 16 October 2026. Prepared for possible discussion with James East; not sent. Nicholas Ham is the sole author. Originality and publication value remain unresolved.

Start with **briefing.pdf** (four pages). It presents the questions, short proofs and recognition/development prompts. **manuscript.pdf** (nine pages) gives the full mathematical argument. No software installation is needed to read either document.

The main results concern a nonnegative finite-range obstruction with a support-dependent uniform-row certificate; actual-uniformity converses for small moduli; and recovery of jump weights on widening funnels under nonzero boundary pivots. Reflection explains a limitation of row totals and unlabelled data. Restarted-data sharpness does not establish optimality from the origin. All-prefix uniformity is distinct from eventual uniformity.

## Contents

- `briefing.pdf`, `manuscript.pdf`: documents for discussion.
- `proof-audit.md`: assumptions, limitations, adversarial checks and dispositions.
- `open-questions.md`, `general-q-note.md`, `novelty-assessment.md`, `references.md`: unresolved mathematics and the precise literature-comparison boundary.
- `verification/`: a small Python standard-library bundle, including exact arithmetic and independent word enumeration.
- `source/`: the LaTeX sources and optional document build script.
- `SHA256SUMS`: integrity hashes for every other packaged file.
- `LICENSE`: existing author-rights statement; packaging does not change licensing.

## Reproduce the focused evidence

Python 3.10 or later, standard library only. From the extracted package directory:

```sh
python3 verification/verify.py
```

This checks integrity, then runs finite-support/restarted sharpness cases, widening-funnel inversion and reflection cases, the small-modulus calculations (including exact arithmetic in Q(sqrt(2))), and two independent-word/invalid-data unit tests. It requires no network, repository checkout, TeX or third-party Python packages. Exact domains and expected output are in `verification/EXPECTED.txt`. These checks corroborate the proofs; they do not prove their universal quantifiers.

This is a focused subset of the repository's evidence, not the complete historical 150-claim audit or all 29 repository unit tests. The original conjecture programme remains separate: 58 established/answered, 19 disproved, 61 unresolved, 10 numerical claims and 2 context entries, unchanged this pass.

To rebuild the PDFs, optionally run `bash source/scripts/build.sh` with Python 3, pdfLaTeX, BibTeX and latexmk, plus the usual AMS/geometry/hyperref/Latin Modern TeX packages. This is unnecessary for inspecting the mathematics or running the evidence.

## Status and assistance

The source contains proofs and explicit counterexamples. Separate internal AI analyses reconstructed the key arguments; they are not external peer review or human mathematical sign-off. OpenAI Codex assisted with mathematics, source comparisons, implementations and writing. The audit records shared-model limitations and actual checks. The remaining purpose is specialist scrutiny: recognition of prior results and advice on worthwhile development, rather than endorsement of a completed discovery. No external correspondence or submission is included.
