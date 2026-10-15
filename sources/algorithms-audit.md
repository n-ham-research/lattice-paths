# Original algorithm availability and inspection audit

Date: 16 October 2026. Auditor: Codex research subagent `/root/east_ham`; model version not exposed. No external peer review implied.

## Provenance and licence

* Source: [Nicholas C. Ham, lattice-path-algorithms](https://gitlab.com/n-ham-paper-files/lattice-path-algorithms).
* Public HTTPS clone succeeded after retry with network permission; initial sandbox attempt failed DNS resolution.
* Inspected commit: `e470a327c0f9fa29f52cd9b287bfc132af7a6749`, author timestamp `2019-05-11T12:46:06+10:00`, subject “added link to arXived version of paper”.
* Local clone: `.local/references/algorithms/`, an ignored reference cache, not project source.
* `LICENSE.md`, README and source headers state copyright 2018 Nicholas C. Ham, **Creative Commons Attribution-ShareAlike 4.0 International**. This is a checked licence declaration, not an assumption that public availability permits unrestricted copying.
* No original C++ source was copied into the project's implementation. The project Python implementation is to be independently derived from mathematical definitions. Any later redistribution/adaptation of the original code needs separate attention to attribution and ShareAlike terms.

The repository README associates algorithms 1–3 with East–Ham. The [arXiv version record](https://arxiv.org/abs/1811.05735) states the algorithm section was removed in v2; use v1 when locating the corresponding textual algorithm exposition.

## Files actually inspected

Read the complete `algorithms.h` (601 lines), all three executable drivers, README, Makefile, licence declaration and supplied input. The project contains finite-step C++11 algorithms and TikZ output, not an infinite-step symbolic enumeration package.

| Function | Actual inspected behavior |
|---|---|
| `algorithm1` | Builds endpoint sets at exact lengths 0 through q and accumulated graphs. Graph vertex labels are the greatest attained length up to that horizon, **not path counts**. Extends only from vertices attainable at the preceding exact length and tests each new vertex against linear constraints. |
| `algorithm2` | Sorts step directions using floating-point angles, seeks an open-half-plane witness, and classifies a finite unconstrained step set FPP or IPP. It does not decide constrained FPP for arbitrary boundaries. |
| `algorithm3` | Calls algorithm2 to obtain a progress vector, estimates a sufficient length horizon from minimum/maximum dot products, obtains endpoint/length layers via algorithm1, then sums predecessor counts in layer order. Stores counts as `long long int`. |
| Drivers | Read `input.txt`, default q=10 for algorithms 1 and 3 (command-line override supported), write `output.txt` with TikZ. Each run overwrites that file. |

Constraints use `double` slopes/intercepts and comparisons with y versus ax+b. Vertical bounds require source modification as described in the README. A finite truncation of an infinite step set is not justified merely by invoking this code: the finite transitions relevant to the region must first be derived mathematically.

## Reproduction performed

In the ignored original clone, `make` compiled all three programs with g++ using `-O3 -std=c++11 -Wall -Wextra -pedantic`. `make test` ran all three successfully on the supplied input. The Makefile's test target only executes the programs; it asserts no expected numerical outputs, so this is a build/smoke check.

An independently written temporary C++ harness outside the repository included the original header and made the following explicit assertions:

* X={(1,0),(0,1)}: algorithm2 returns FPP; algorithm3 at q=6 labels (2,2) with 6 and (3,3) with 20, agreeing with binomial coefficients.
* X={(1,0),(-1,0)}: algorithm2 returns IPP.
* For the north/east set, algorithm1 at q=4 labels (2,2) with 4, confirming that its labels are lengths rather than the count 6.
* Empty step set: algorithm2 returns **IPP**, whereas mathematically FPP holds (only the empty word reaches the origin). This is an observed edge-case defect. The code's comment permits finite step sets without an explicit nonempty restriction.

The harness was compiled with C++11 warnings enabled and passed its asserted checks. Temporary harness path during this session: `/tmp/lattice-path-original-audit.cc`; it is not part of the committed project or a durable regression suite. No original program was used as the oracle for the project's factorial tests.

## Limits and improvement opportunities

1. Signed fixed-width counts can overflow (21! already exceeds a signed 64-bit integer); arbitrary-precision integers are needed for the new exact engine. This is a source-level limit, not a claim of an observed overflowing run.
2. Floating-point direction and boundary tests can misclassify near-collinear or large-coordinate cases. Exact integer determinants and rational inequalities would support reliable audits.
3. `algorithm3` does not check the returned FPP/IPP status before using the vector and dividing by the minimum progress. Its mathematical progress-bound method needs a positive separating functional; use on IPP inputs is unsupported and potentially invalid. Such an input was not run in this audit.
4. Input parsing does not validate nonnegative q, missing files or the origin's membership in the boundary set. Callers must enforce these assumptions.
5. In `Step` ordering, equal displacement but different bend amount can be distinct set entries, while edge ordering ignores drawing properties. Input should contain one entry per mathematical displacement to prevent multiplicity/drawing conventions contaminating counts.
6. Minimum/maximum progress start at 500 and −500 rather than infinities. For a valid positive functional, the 500 minimum can enlarge the horizon unnecessarily; exact extrema from the first step are clearer. Empty sets need a separate branch.

The new implementation can reproduce the intended positive-progress counting independently with exact arithmetic and explicit finite layer bounds. No claim is made that all original algorithms are correct on all advertised inputs, or that the small audit above constitutes their complete verification.
