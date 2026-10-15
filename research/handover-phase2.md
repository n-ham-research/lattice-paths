# Research phase 2 handover — 16 October 2026

## Outcome and status counts

The pass establishes a finite structural rigidity theorem beyond the elementary factorial principles, supplies explicit classical tree/Dyck/polygon bijections, corrects additional source assertions and reproduces every printed numerical table entry. Priority for the rigidity theorem remains unresolved; no new-theorem claim based on unsuccessful searches is made.

The immutable inventory still has150 IDs. The cumulative ledger phase2-claim-status.json gives:

| Disposition | Number |
|---|---:|
| Established or answered under explicit extraction/index/support conventions |57|
| Literal source assertion disproved, with corrected variants separate |19|
| Unresolved |62|
| Table claims checked as finite numerical data |10|
| Context/research-direction entries |2|

131 entries have received independent full or partial investigation:121 mathematical claims plus10 numerical table claims. Of62 unresolved,45 were investigated but not fully resolved and17 remain uninvestigated. This is not131 solved claims or57 new theorems:57 includes answered questions such as §13's binomial comparison and §39's unidentified antidiagonal sums. Relative to the24 mathematical IDs investigated in pass1, this pass adds107 investigated IDs:41 established/answered,15 disproved,10 data and41 still unresolved. The source snapshot remains unchanged; current statuses are separate. Named OEIS alternatives remain unresolved where only the path formula is proved. For q6 the source-described residue-array object is proved directly, but its live OEIS page was not fetched.

## Strongest structural theorem

For D⊆Z, f=1_D and full triangle I_n={0,...,n}, preservation of **every** residue-constant input modulo q by all transitions through N≥q is equivalent to f being residue-constant on [1−N,N]. The infinite converse characterizes exactly unions of full residue classes. For N<q the condition is vacuous, showing the horizon bound matters. A general interval-pair criterion reduces preservation to the boundary equalities f(y−a_r+q)=f(y−b_r). Complete proofs, hypotheses, counterexamples and targeted source comparisons are in phase2-classification.md; accepted manuscript Section4 states them precisely.

This is a transition-space classification, not a characterization from one initial counting trajectory or all factorial-valued sequences. Missing target cells are assigned zero only for bookkeeping; the quotient formula applies to present target cells. An independent manuscript review caught that qualification and a regression test now covers it. The affine-shear equivalence is proved in the notes; arbitrary slopes/cones remain open.

## Bijections and generating functions

The excursion ↔ degree-restricted plane-tree ↔ restricted-ascent Dyck maps are explicit inverses, including empty objects, zero-height increments and size profiles. They are classical (Hackl–Heuberger–Prodinger; Brak–Iliev–Prellberg), with independent application to §§6–11 and17–23. Weighted equation E=1+Σ_a q_a x^a E^(a+1) unifies the axis models. Both §17 variants have Fuss counts at horizontal coordinate mn; only total step lengths differ. Vertical multiples give H=1+tH^m(2H−1) and a finite Lagrange coefficient formula.

Classical dissection duality (Curien–Kortchemski Proposition2.2), with an explicit consecutive-leaf-interval inverse, resolves §18: excursion lengthN ↔ total polygon edges N+1; downsteps correspond to faces. Empty paths correspond to a formal edge, not an ordinary polygon. A parity condition repairs the flagged finite coefficient sum on OEIS A067955, without any external submission. Full proof phase2-polygons.md; no novelty claim. The Motzkin/Riordan axis equality follows proved GF elimination; a direct local Motzkin bijection remains open. Blob and packed-word identities are not promoted from a sequence name.

## Additional proofs and counterexamples

The composition formula unifies §§12–16 (with explicit coordinates). Unrestricted §14 is not ternary Catalan: P(2,0)=2, rather than1. Source §13's binomial comparison is indeed binomial(3n−1,n). Arbitrary-positive-horizontal increments plus optional vertical upsteps admit one coefficient formula covering §§34,36–39. §38 axis gives central Delannoy first differences. §39 antidiagonal totals are1,2,6,18,... with OGF(1−t)/(1−3t). The §5 displayed OGF is proved by an exact contour/constant-term calculation, reviewed separately.

Support corrections for §§28–32 include unreachable fixed rows and column shifts; residue-array interpretation is by explicit within-block permutations. §33 positive-horizontal-increment fixed columns terminate, disproving eight bundled infinite-sequence assertions. §35's asymmetric finite set gives17 at(3,−1), rather than the stated quadratic9. §§37–38 positive/negative rows differ at equal coordinates but may match a named sequence with different offsets; these ambiguous claims remain unresolved, not falsely counted as disproofs merely for a missing shift. Details and exact claim IDs are in phase2-remaining-audit.md and phase2-claim-status.json.

## Historical priority corrections

East–Ham **v1 Example3.14**, equations(3.15)–(3.16), already contains complete-triangle factorial counts, nonzero-triangle totals/top counts and the full alternating endpoint formula. The initial v3-only search missed this. Rorabaugh's2015 OEIS proof remains earlier evidence for the axis interpretation. Source hashes and targeted reading scope are in sources/README.md; coordinator visually confirmed v1 p40. Generic equitable partitions, transfer matrices, tree encodings, polygon duality and local signed cancellation are attributed as standard. The signed append/delete involution is correct but elementary; no reason emerged to prioritize it as a standalone contribution.

## Exact verification scope

- Six factorial models: original DP0..12 and explicit words0..5 retained.
- Tree/Dyck maps: all binary Dyck candidates through semilength7 and independently generated excursions; exact inverse and degree/ascent statistics.
- Rigidity: committed exhaustive38,220 triangular indicator/modulus cases and393,216 interval cases. Separate reviewers independently checked21,732,996 and5,456 smaller cases. These scopes overlap and are not summed as distinct instances.
- All697 printed numeric entries across Tables1–10 independently recomputed; separate spatial extraction review confirms completeness and source hash. Axis position13 is labelled12 in Tables6 and7. Blanks are not asserted zero. Table7 finite cap justified despite unbounded upward increments.
- Direct polygon geometry:472 diagonal subsets, even-sided boundary polygons through10 total edges; matches corrected coefficient sum and shifted Table4. Formal size1 separate.
- Composition q1..4,length1..5,deficit0..3 vs explicit parameter words; residue triangle/cone q1..6,columns0..12; arbitrary-progress models three increment sets, with/without vertical step,x0..4,y−2..3 vs independent word recursion; Delannoy differences0..12; §5 bridge coefficients0..15; GF specializations and absent-cell quotient masks. Exact scopes in test source.

From the repository root, run `./scripts/validate.sh` (or invoke its absolute path from elsewhere). It validates150 IDs/evidence links/status totals, runs all unittest methods, regenerates old evidence in check mode, compares all tables, runs exhaustive classification and builds LaTeX. Both module/direct evidence entry points pass. Final fresh-export and visual checks are recorded below. External data caches are not needed.

## Reviews and provenance

Proof, counterexample and generalization review files document initially separate analyses and actual task identities. A fresh additional proof agent checked the classification/tree maps and polygon proof; source-table and cumulative-ledger reviews add focused checks. Agents share model context; these are internal reviews, not external peer review. The exact backend model was not exposed. All changes and checks are traceable in ai-contributions.md and review-log.md. No human mathematical certification is invented.

## Is there a substantive paper yet?

There is now a proved structural converse and a coherent seven-page research draft, plus mathematically useful classical unifications. This meets the next milestone of rigorous mathematics beyond factorial products. It does **not** yet establish sufficient originality for publication. The classification is narrow and may be an elementary known consequence; the bijections are classical. The package is useful for an exploratory discussion with James, but a confident invitation around a new result needs a sharper novelty assessment or stronger consequences. No contact or coauthorship assumption has occurred. A concise potential-sharing note is mathematical-summary.md.

Next: compare exact finite rigidity with primary Toeplitz/equitable-partition literature; classify genuinely varying geometric windows; test whether additional reachability hypotheses yield converses from one actual counting trajectory; construct direct intermodel Fuss bijections; resolve blob/packed-word sizes from primary definitions. No factorial benchmarking or publication submission was undertaken. A pre-existing untracked lattice-paths.zip was preserved untouched.

## Final validation

All20 unittest methods pass. Full validation also passes the exact evidence check, all697 table entries, the38,220/393,216 exhaustive classification cases, source-ID/status/evidence-link checks and latexmk/BibTeX. A staged-file export in a new /tmp directory passes the same full command with no source cache, pre-existing build products or user archive. The final seven-page PDF was rendered and all pages inspected; a final bibliographic author-name correction was rebuilt and its affected page re-inspected. There are no unresolved citation/reference or overfull-box warnings. Downloaded PDFs, original external implementation and the user's zip remain outside tracked files.
