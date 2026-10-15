# East–Ham versions and what algebra adds

16 October2026. Targeted comparison of all three arXiv versions, not a new full reading of every page.

| Material | v1 (14 Nov2018,63pp) | v2 (14 May2020,36pp) | v3 (27 May2021,36pp) |
|---|---|---|---|
| Free word monoid→embedded endpoint monoid; labelled Cayley picture | §2.1 | §2.1 | §2.1 |
| Constrained-word/endpoint monoid closure for additive constraints | §3.1, earlier numbering | Lemma3.2 | Lemma3.2 |
| Constraint loses translation invariance; category of all starting positions | §3.1 category remark | Remark3.4 | Remark3.4 |
| Explicit complete-triangle factorial and nonzero-step endpoint formulas | Example3.14, pp39–41,(3.15)–(3.16) | Removed from this shorter version | Absent; old version referenced in introduction |
| Catalan equivalence for nonnegative-increment steps | Example3.17 with proof/figure | Example3.3(iii), alongside (i) | Example3.3(iii), alongside (i) |
| Admissible-step/geometric finiteness theory | §3, earlier theorem numbers | §3.2–3.3 | §3.2–3.3 |
| Algorithm1/2/3 pseudocode and discussion | §4, pp46 onward | Removed; introduction points to code/old version | Same reference policy |

Directly read this pass: v2 §3.1 definitions, Lemma3.2 and Remark3.4; v1 §4 opening, §4.1 reachability description and §4.3 assumptions/admissible-step discussion; targeted v2/v3 text differences. Earlier passes read complete v3 and targeted v1 Example3.14. The v2/v3 category text at the inspected location is identical in the extracted sources; the comparison does not certify identical entire proofs or a complete change log. The arXiv version record itself states that v2 removed algorithms and examples.

New ignored v2 cache: PDF SHA-256 b2c5e3a69c6272996e41b5539c9fd5090b43256be31ad757bbcd374a76a04241; extracted text f689c5bf8a0867f862c7c97b9ce3f95041172ed1ddd790568ea41e7c41585d22. Source https://arxiv.org/abs/1811.05735v2 ; v1/v3 hashes remain in sources/README.md. No PDF or external code is tracked.

## A scope correction to the earlier code audit

The empty-step-set run still demonstrates missing input-domain handling in the historical implementation, but v1 §4 explicitly assumes a **nonempty finite** step set and an admissible first step. The earlier empty-input result is therefore not a counterexample to the mathematical algorithm under its stated paper hypotheses. Retain the observed program behavior with that qualification; do not call it a refuted theorem or an in-domain algorithm failure. Historical fixed-width arithmetic limitations likewise concern implementation range, not the exact mathematical recurrence.

## What can monoids explain?

The endpoint monoid alone is insufficient: in C={(x,y):0≤y≤x}, the generating sets {(1,0),(1,1)} and the same set with (2,1) added have identical endpoint monoid but counts2 versus3 at (2,1). Conversely a full labelled transition graph already determines every finite path count by definition, so no extra algebraic datum can change enumeration while that graph is fixed. Algebra can expose useful equivalences or compact representations, rather than contain information beyond this sufficient object.

Useful retained structure is the embedded endpoint grading, the chosen generator map from the free monoid, and the admissible-prefix language; or the constrained walk category with its displacement/length grading. A weighted graded category equivalence preserving the selected endpoints gives a bijection of morphisms and hence preserves counts. This is a standard consequence, not a new theorem.

The phase3 component graph parameterizes an algebra of admissible kernels: component-constant weights form a pointwise ring isomorphic to one copy of the coefficient ring per component. Indicator kernels are unions of components. Residue periodicity is forced exactly when component connectivity joins each observable residue fiber. This organizes finite-state reductions within the earlier labelled-word framework. It does not imply that a submonoid property alone forces the required partition regularity.

The inverse result supplies another precise limitation: sufficiently rich labelled endpoint rows plus nonzero edge pivots recover the observable generator weights; mere total counts, an unlabelled support monoid, or nonextinction do not. The unresolved algebraic question is to characterize natural graded word-category equivalences yielding new explicit fibre bijections or low-dimensional representations, rather than restating that a path graph counts its paths.
