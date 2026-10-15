# Literature review and prior-result boundaries

Audit date: 16 October 2026. Internal research notes, not an exhaustive novelty search.

## East–Ham: source and reading coverage

James East and Nicholas Ham, *Lattice paths and submonoids of Z²*, [arXiv:1811.05735v3](https://arxiv.org/abs/1811.05735v3), revised 27 May 2021. The complete 36-page v3 was read, including Sections 1–3, Appendix A (joint with Stewart Wilcox), acknowledgements and bibliography. Local extracted text: `.local/references/east-ham.txt` (untracked source cache). The arXiv record distinguishes the 63-page v1 from v2/v3, which remove the algorithms section and many examples. The GitLab code implements the older algorithms, so algorithm numbering must not be confused with v3 theorem numbering.

### Conventions that affect this project

* A step set is a subset of Z² excluding the zero vector; it may be infinite. Walks are **words**, so distinct orderings of steps are distinct paths even if they share an endpoint. The empty word counts once at the origin. The path length is the number of letters, not the horizontal displacement.
* The free monoid F_X maps onto the endpoint submonoid A_X by summing letters. The fibre cardinality π_X(A) counts walks of **all lengths**, and may be infinite.
* Section 3 constrains **every visited lattice vertex**, including the origin and endpoint, to a set C. For a convex planar region, vertex containment also implies segment containment; that implication should not be silently used for arbitrary C.
* For arbitrary C containing O, constrained words and endpoints need not form monoids. Lemma 3.2 supplies monoid closure when C is an additive submonoid. Translation invariance of unconstrained counts is lost under constraints (Remark 3.4).
* The unconstrained graph is a Cayley graph with vertex labels equal to fibre sizes. The constrained graph is generally **not** a Cayley graph, even when its reachable endpoints form a monoid.
* FPP means every reachable endpoint has finitely many paths; BPP bounds lengths separately for each endpoint; IPP means every reachable endpoint has infinitely many paths. Finite length does not imply finitely many paths when the alphabet is infinite.

### Results worth citing precisely

| v3 identifier | Content relevant here | Limitation |
|---|---|---|
| Example 2.3 | X={1}×Z has infinitely many unconstrained paths to every (a,b) with a≥2, although every such path has length a | Direct warning against dropping the wedge restriction from Section 24 |
| Example 2.4 | Several infinite positive step sets have binomial-coefficient counts | Infinite sets can have finite fibres, but require justification |
| Lemma 2.5 | IPP iff π_X(O)≥2 iff π_X(O)=∞ | Unconstrained; repeating a nonempty zero-sum word produces infinitely many paths |
| Theorem 2.19 | IPP iff O∈Conv(X), iff A_X has nontrivial units, iff its Cayley graph has a nontrivial directed cycle | Uses the convex hull itself, not its closure; acyclicity alone does not ensure finite fibres for infinite X |
| Theorem 2.27; Corollary 2.29 | Cone ⇒ strong line ⇒ line conditions, with corresponding FPP ⇒ BPP ⇒ not IPP; all become equivalent for finite X, giving FPP/IPP dichotomy | Infinite X exhibits strict implications; cannot infer FPP solely from x-positive steps |
| Theorems 2.31, 2.34 | Characterise when A_X is a group; for nonempty X this is equivalent to O∈Rel-Int(Conv(X)) | These are structural, not factorial enumeration formulae |
| Proposition 2.43; Appendix A | Complete the finiteness/geometric combination analysis; the appendix constructs BPP without FPP or strong line condition | Shows why a general enumeration engine needs explicit scope limits |
| Example 3.3(i),(iii) | X={(1,0),(0,1)} and X={1}×N yield the Catalan triangle in C={(a,b)∈N²:b≤a} | These are nonnegative vertical increments, not the unrestricted integer increments of the factorial model |
| Theorem 3.6 | Constrained hierarchy, and finite-X equivalence of FPP and BPP | Constrained FPP/IPP dichotomy fails even for finite X |
| Propositions 3.10, 3.11 | Restricted implications among constrained IPP, convex hulls and units, plus a group characterisation using reachable endpoints | Replacing X by itself in unconstrained criteria is generally invalid |
| Theorem 3.13 | For finitely many admissible steps Y, constrained FPP iff O∉Conv(Y) iff Y satisfies the line condition | Requires C an additive submonoid and finite Y |
| Lemma 3.16; Theorem 3.18 | A reachable interior point of a lattice cone contained in C makes all steps admissible; for finite X yields strengthened FPP criteria | Both reachability and finiteness hypotheses matter |

### Algebraic direction supported by the paper

The factorial wedge C={(n,k):0≤k≤n} is an additive submonoid; its constrained word language is therefore a submonoid by Lemma 3.2. For X={1}×Z, the constrained endpoint monoid is C. Nevertheless, these facts alone do not determine its path counts: the same abstract endpoint monoid can admit different generating sets and fibre sizes. The useful bridge is the **labelled transition structure**, retaining the words rather than only endpoints.

Remark 3.4 explicitly suggests the category with objects C and morphisms constrained walks between arbitrary pairs of vertices. Composition is concatenation. This is an attributed starting point for future work, not a newly proposed connection. Layered transfer matrices and partitions of layers with constant numbers of incoming edges provide a finite-dimensional route to counting; constant indegree is the one-cell case. A classification of translation-defined step sets and boundaries producing such partitions might be useful, but no novelty or classification theorem has been established here.

## Factorial and alternating factorial prior evidence

The constant-indegree product lemma follows immediately by induction, or by applying each layer's incidence matrix to a constant vector. It should be presented as an elementary counting principle, not as a novel theorem based on the limited search undertaken here. Complete bipartite layers are sufficient but unnecessary. For positive path counts uniform in the preceding layer, constant indegree is also necessary for uniformity in the next layer; if all previous counts are zero this converse fails.

[OEIS A005165](https://oeis.org/A005165) contains Ham's 23 August 2015 lattice-path conjecture for nonzero vertical increments between y=0 and y=x, and Danny Rorabaugh's 30 November 2015 induction proof. Its mechanism is n! total paths to column n followed by exclusion of those at height zero before the final down-step. Consequently the Section 25 base model and recurrence A_n=n!−A_(n−1) are **already proved in a public primary contribution**, not new results of this project. The endpoint is (n+1,0), and the stated range n>1 avoids the exceptional initial alignment; preserve this shift when citing it.

[OEIS A010551](https://oeis.org/A010551), inspected on the audit date, records a(n)=floor(n/2)! floor((n+1)/2)! and parity-preserving permutations (Avi Peretz, 22 February 2001), together with other interpretations. The current entry contains no Ham attribution or lattice-path proof located in this inspection. This identifies the Section 27 interlaced sequence, but does not prove any particular path model or establish its novelty. In particular a(2m)=(m!)² and a(2m+1)=m!(m+1)!; indexing must be specified before comparing individual columns.

## Search coverage and next steps

Primary material directly examined: the complete East–Ham v3, original GitLab source and licence, and the two OEIS entries above. Web searches for Ham/factorial lattice paths and graded graphs with constant indegree found no additional directly applicable primary theorem during this initial audit. This is **not** evidence of novelty or an exhaustive literature review. Before a novelty claim, inspect the additional examples and algorithm discussion in East–Ham v1; trace the specific OEIS entries for every Section 24–27 formulation and their histories; examine standard transfer-matrix and equitable-partition sources; and seek a theorem with substantive content beyond the elementary product rule. Catalan, Fuss–Catalan, Motzkin, Schröder and other inventory families remain to receive targeted literature audits.
