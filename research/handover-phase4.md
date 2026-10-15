# Phase 4 handover — rigidity and inverse problems

16 October 2026. Nicholas Ham remains sole human author. Phase3 is approved by the user; this pass implements the Phase4 request. James East has not been contacted, authorship has not changed, and nothing has been submitted. Historical priority and publication value remain unresolved.

## 1. Sharpened finite-support obstruction and optimality

For a homogeneous nonnegative finite kernel with support extremes m,M on the triangle, put L=max(0,M), R=max(0,1−m), v=max(M,1−m)≥1. If b≥max(q−1,L+R+q−2), then q-uniform rows b,...,b+ceil(q/v) force row b zero. This improves the previous ≤2q-row certificate to ≤q+1 rows, often fewer. A full core gives residue convolution; every omitted boundary summand must be zero. Repeating a positive supported jump increases the least active residue representative without wrapping; repeating a nonpositive jump increases its distance from the moving top. Either direction gives the certificate. No positivity of every residue is assumed.

The bound ceil(q/v)+1 is exactly sharp for arbitrary prescribed later initial rows, via a single jump1−v and a sufficiently late residue-zero indicator. **This does not establish origin-start optimality.** For the natural origin class support⊆{0,1}, binomial comparisons prove no q-uniform row n≥q+1, and equal weights pass at n=q. The exact general origin-start block optimum remains open.

The earlier mass argument extends to layer-dependent kernels in one common finite support envelope by replacing K powers with products. Its ≤2q certificate is sharp for restarted data with varying0/1 jumps. An early auxiliary proof incorrectly asserted both boundary coordinates never wrap; independent review caught it. The corrected proof uses inequalities (negative values may wrap upward), and the original mass-product proof independently establishes the statement. All current statements retain the common range and nonnegative hypotheses. See phase4-obstruction.md.

## 2. The infinite-support question: actual small-modulus converses

For nonnegative real homogeneous weights with f(0)=f(1)=t>0, actual parity-uniformity through N≥6 forces f=t on W_N=[1−N,N]. The initial horizon is optimal: a positive irrational prefix survives through5 but its next required weight is negative. For rational weights the sharp horizon is5; for indicators containing0,1 it is3. Normalize t=1, put x=f(−1)=f(2); uniformity forces c=(x²−x+2)/(x+1) and a=(3x−1)/(x+1). A row5 interior difference factors as −2(x²+2x+3)(x−1)²(x²+2x−1)/(x+1)². The extra nonnegative real root x=√2−1 forces f(−5)=7−5√2 at row6, impossible. The rational prefix x=1/2 is a sharp counterexample through4. Binary values give the shorter proof through3.

For indicators with0,1∈D, actual3-uniformity through N≥4 forces3-periodicity on W_N; horizon4 is optimal. The seed calculation forces residue mask(1,1,x), x∈{0,1}. Thus all-horizon possibilities are Z or the union of classes0,1mod3. These are actual-trajectory converses, not all-input assumptions.

The unifying bootstrap: with nonzero boundary pivots, a q-periodic seed on W_m, m≥q, and continued actual q-uniformity force every new extreme weight to match its periodic continuation. Interior counts are known, and each boundary has an interior height of the same residue. This connects compressed regularity to inverse uniqueness.

Generalq≥4 indicators, unequal initial real weights, eventual instead of all-prefix uniformity, signed coefficients and layer-dependent kernels are not settled by these theorems. In particular finite positivity is not asserted sufficient. See phase4-infinite.md and manuscript Section6.

## 3. Full and compressed inverse data

Complete labelled rows on any interval geometry have exact affine fibers A(p)g=p, because prescribing the preceding rows makes the recurrence linear and induction ensures sufficiency. A linear statistic is identifiable among field-valued models precisely when its coefficients belong to the row space. Compatible indicator/nonnegative models require intersection with their admissible sets; rank is not a necessary condition for restricted-class uniqueness. Genuinely hidden intermediate rows give polynomial, generally nonaffine fibers. Deleting equations is not a solution to arbitrary sparse observations.

Corner recovery extends from triangles to every monotone widening funnel I_n=[cn,cn+s_n],0=s0≤...≤sN, with arbitrary width jumps. Under both preceding nonzero corner pivots, all weights on exactly[c−s_(N−1),c+s_N] are recovered. After shear, newly negative weights are solved descending from low endpoints, then newly positive weights ascending from high endpoints. Full previous rows are needed; two boundary sequences alone are not claimed enough. The field may have any characteristic conditional on pivots; indicator0,1 positivity guarantees are for ordinary counting/characteristic zero.

A compressed scalar inverse theorem joins this to geometry: all actual rows throughN are constant and nonzero iff f=α>0 on that entire observable window. Counts equal α^n∏_(j=0)^(n−1)(s_j+1). Uniformity identifies shape, one row sum fixes α, and unbounded widths give a global converse. The scalar argument tests a one-dimensional subspace and cannot simply be repeated for generalq.

For ordered nonnegative kernels f≤g, identical observations at specified endpoints hold exactly when every positive g-word to those endpoints uses only unchanged jumps. This gives an exact path-language visibility criterion within the ordered class, not for incomparable kernels. Geometry can expose previously invisible jumps, e.g. {0} and{0,−1} coincide on[0,n] but differ on[−n,0]. See phase4-inverse.md.

## 4. Counterexamples, algebraic structure and consequences

Reflection(n,y)↦(n,n−y), d↦1−d gives a weight-preserving involutive isomorphism of constrained-walk categories, including arbitrary starting vertices. It reverses each origin row. Thus {0,1,2} and{−1,0,1} give identical row multisets/totals forever despite full positive reachability; labelled counts distinguish them. Reflection is not claimed the only ambiguity. Fixed-label residue sums and individual diagonals are generally permuted, not equal. This supplies an exact algebraic explanation for a compressed inverse obstruction; endpoint monoids alone still lose word/generator information. See phase4-algebraic-observations.md.

No finite endpoint horizon can certify finite support: weights outside its observable difference set may be freely added. The shorter obstruction instead provides a useful exclusion certificate: t+1 nonzero uniform rows force tv<q for any proposed finite kernel meeting its core threshold. Two such rows already exclude all eligible supports with outward speedv≥q. The threshold depends on the proposed support, so this does not infer a global finite support bound from unknown tails.

Exact failures retained: infinite homogeneous f≡1 and finite-per-layer but unbounded-range f_n=1_[1−n,n] produce n! scalar rows; bounded layers{0} with f0=1 persist; rational and irrational parity prefixes show distinct sharp seed horizons; restarted sharpness does not imply origin sharpness; unlabelled observations lose reflection labels. Signed finite-support eventual uniformity and infinitely separated uniform rows remain open here; proof failure is not advertised as a counterexample.

## 5. Selected combinatorial work and original inventory

No direct packed-class/Riordan map or primary blob definition was obtained in this pass. The category reflection is the selected algebraic advance relevant to the inverse narrative; no new unrelated classical formula was forced into the manuscript. Phase3's packed-word generating-function resolution and profile bijections remain supporting records, with no new novelty claim.

All150 original claim dispositions are unchanged from phase3-claim-status.json:58 established/answered,19 disproved,61 unresolved,10 verified-data,2 context.131 are fully/partially investigated; among unresolved,44 partly investigated and17 untouched. The new structural theorems do not invent new original IDs. Prior status snapshots and original extraction remain intact.

## 6. Targeted novelty comparison

See phase4-novelty-ledger.md. Newly read primary statements: Blåsten–Isozaki–Lassas–Lu arXiv2107.00494v2 Condition1.4/Theorems1.5–1.8 and observation definitions (PDFpp1–9); de la Peña–Gzyl–McDonald arXivmath/0610821v1 introduction/Theorem1.1 (PDFpp1–3); Lawler–Limic §§5.2,12.4.1 selected pages. These are fixed-graph/hitting-data or killed-walk frameworks, not exact matches to the expanding jump-kernel observations. This comparison establishes neither novelty nor a theorem-level exclusion of every possible implication of earlier work. Full inverse proofs were not read. HTML access failed but primary PDFs were accessible to the coordinator; the fresh reviewer independently had cache misses and does not claim its own source verification.

Affine fibers and recursive elimination are established methods; scalar reduction/component bookkeeping are direct consequences; the exact shorter certificate, funnel recovery and small-modulus compressed tests have complete independent proofs but unresolved priority. The elementary nature of several arguments makes recognition especially valuable.

## 7. Mathematical narrative and external briefing

The main paper is retitled *Rigidity and Inverse Problems for Restricted Lattice-Path Enumeration*. It grows from7 to9 pages to include actual inverse bridges and sharp compressed tests. Classical combinatorial material is preserved in source/research files, removed from the main narrative. A four-page refined briefing gives the mass proof, shorter boundary proof, structural/funnel results, reconstruction, compressed converses, precise limitations, citations and AI disclosure. It separates two recognition questions from two development questions. It asks about a small number of mathematical statements, not verification of the entire archive. See publication-structure-phase4.md.

Recommendation: author-led external specialist feedback is now the better next step. Ask James whether the short results are recognizable and whether a periodic-seed theorem or useful observation equivalence is worth developing. Further internal work should follow a specific mathematical lead, rather than another broad search. The author will decide whether to share; no message was sent or drafted into an external service. Nicholas Ham remains sole author.

## 8. Exact verification and review provenance

Committed new checks:2040 cases(all255 nonempty supports in[−3,4],q1..8);144 restarted homogeneous sharpness cases(q,v1..12);12 varying-kernel sharpness cases(q1..12);420 binomial exclusions(q1..12,five weight pairs,n=q+1..q+7). Inversion checks70 nondecreasing four-layer width tails0..4,70 scalar formulas,256 binary reflection assignments onW4 andone nonlinear partial-observation example. Small-modulus checks16 binaryW3 assignments,64 binaryW4 assignments,650 rational parameter instances(not distinct rationals), explicit weighted words through5, and exactQ(√2) arithmetic. Two new unit methods independently enumerate weighted funnel words with plateaus/jumps and reject invalid inverse data.

Actual agents: obstruction4, inverse4, infinite4 authored separate research; then supplied initially separate cross-checks in phase4-counterexamples/generalization/inference.md without reading each other's review reports first. Fresh4 performed a further independent proof/transcription review, includingq3 and the final briefing. The coordinator checked all promoted proofs and transcriptions. Additional one-off review domains are recorded separately and not confused with committed tests. Backend model versions were not exposed; shared-model limitations remain. AI agreement is not external peer review or human sign-off. See review-log.md and ai-contributions.md.

## 9. Final reproducibility and document checks

`scripts/validate.sh` passed in the working tree and again in a clean export of all staged tracked files, without reference caches or existing build products. All29 unittest methods passed, together with the retained exact/exhaustive checks,697 source values and all new Phase4 scripts. Both PDFs built without undefined-reference or overfull-box warnings. All13 rendered pages were inspected:9 manuscript and4 briefing, with no overlap/clipping found. Local source and build scripts are retained; generated PDFs remain ignored. Native editor/compile tools were not exposed, so existing local TeX tools were used without installing anything. The pre-existing untracked lattice-paths.zip was left untouched and unstaged.
