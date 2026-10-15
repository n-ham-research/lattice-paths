# Research phase 3 handover —16 October2026

## Main outcome

This pass supplies a precise obstruction for actual counting trajectories, geometric extensions including rational cones, and labelled endpoint-data reconstruction. These are proved results beyond the old factorial explanation; their exact historical priority remains unresolved. The main manuscript has been refocused around these questions and remains seven pages. A separate four-page mathematical briefing is ready for the author's review, but has not been sent.

## 1. Actual trajectories: a stronger proved obstruction

With finitely supported nonnegative jump weights, a nonextinct triangular trajectory cannot be eventually constant per residue class modulo any fixed q. No positivity of every endpoint or residue is required. The proof uses a full-predecessor interior for each residue: its summed residue values multiply by total step weight K, whereas total path mass increases by at most K. Increasing copies of the same residue values eventually contradict this mass bound.

There is an explicit finite certificate. If support extremes are m,M, put L=max(0,M),R=max(0,1−m). For b≥max(q−1,L+R+q−2) and h=q(ceil((b+1)/q)+1)−1, uniform rows b..h force row b zero. There are at most2q rows. This is sufficient, not proved optimal. Infinite support and signed weights are outside the argument. See phase3-trajectories.md and the stronger general theorem in phase3-growing-windows.md.

Full labelled endpoint rows recover jump weights on W_N=[1−N,N] by two explicit corner equations per layer when the preceding two boundary counts are nonzero. Ordinary indicator counts with0,1∈D satisfy the pivots. The theorem itself holds over a field conditional on pivots, but that indicator guarantee requires ordinary counting/characteristic zero; positive characteristic can cancel counts. A final review caught this qualification, repaired in both documents with a regression case. This is elementary specialized elimination, not claimed a new general inverse-graph theorem.

Nonextinction alone does not identify D: {0} and Z_(≤0) give identical entire arrays. Positive reachability does not transfer the structural finite horizon: q5,D={−5,−3,0,1,4,6} is residue-uniform through6, nonperiodic on W6, with all endpoints positive; it fails uniformity at7. The infinite-support actual-trajectory converse for q>1 remains open.

## 2. Boundary geometry and verification horizons

For arbitrary finite interval layers, the boundary comparison graph joins differences y−a_r+q and y−b_r. Over a commutative ring, structural preservation is exactly weight constancy on each component. It forces periodicity on observable differences exactly when every observable residue fiber is connected (nonzero ring for universal necessity). This is a direct equality-constraint parameterization; by itself not a novelty claim.

Scalar rigidity now holds for every widening funnel I_n=[cn,cn+s_n], integer c and arbitrary nondecreasing widths starting s0=0, even with unbounded jumps in width. Exact forced window is [c−s_(N−1),c+s_N]. This includes two-sided integer cones. Nonmonotone bounded periodic layers can fail: alternate {0} and{0,1}, weights f0=f1=1,f−1=0. All transfers and actual rows are constant, while the observable kernel is not. See phase3-geometry.md and phase3-horizons.md.

For actual finite-range trajectories the geometric theorem is stronger in a different direction: for I_n=[A_n,B_n], the core is J_n=I_n∩[A_(n−1)+M,B_(n−1)+m]. Uniform rows b..h with q-point cores and floor(|I_h|/q)>ceil(|I_b|/q) force row b zero. Diverging widths with bounded successive endpoint movements guarantee these conditions eventually. Thus rational or real cones of distinct slopes, with bounded periodic boundary offsets, are covered. This is not a general-q structural converse for those cones; that remains open.

The structural triangle's first informative horizon q is exact; earlier target cells are singleton. For q≥3,N=q−1 an explicit nonperiodic observable indicator passes vacuously. For small moduli some earlier equivalences are themselves vacuous, so avoid overstating a least horizon. General-q integer-cone rigidity after ceil(q/width-slope) is still conjectural beyond its first horizon. No finite computation promotes it to a theorem.

## 3. Nontrivial original family and multivariate refinement

H2019-23-01 is now established: nonnegative up1/vertical negative-multiple paths to(mn,0) have the same number as sylvester classes of m-packed words of length mn. The proof uses the actual definitions and Novelli–Thibon §5.3,(182),x=2, then Lagrange inversion to recover H=1+tH^m(2H−1). It does not use an OEIS match or construct a direct class bijection. The separately listed unassigned identifiers in23-02 remain unresolved. The source's (186), if read in the same polynomial normalization, gives a different second coefficient; the proof avoids it and records the normalization/possible-error caveat rather than relying on it.

The complete downstep/tree-degree/Dyck-ascent/polygon-face profile is counted by N!/((u+1)!∏r_a!), u=Σar_a,N=u+Σr_a. The cycle-lemma proof and inverse order are explicit. For nonempty polygon profiles a≥1, boundary sides u+2, diagonals Σr_a−1 and face sizes a+2. Empty objects have a separate formal convention. These are classical refinements in our coordinates, not certified new combinatorics. Blob primary definitions from Read1986 were not obtained; blob and reflected positive-row claims remain unresolved. A direct local Riordan map was not completed. See phase3-combinatorics.md.

## 4. Targeted originality and earlier algebraic work

The novelty ledger phase3-novelty-ledger.md compares exact statements with inspected primary material. Cell-indicator invariant subspaces and profile formulas are established background; component graphs and weighted extensions are direct consequences. Funnel rigidity, the finite-window converse, actual-trajectory obstruction and corner recovery are independently proved but have unresolved priority. The mass and elimination arguments are short enough to be familiar observations; unsuccessful searches are not originality evidence.

A targeted v1/v2/v3 comparison is recorded in phase3-east-ham-versions.md, including a newly cached/hash-pinned v2. Old factorial results and the constrained walk category are prior work. The earlier empty-set code observation is outside v1 §4's explicit nonempty-step hypothesis: a program-domain handling issue, not a counterexample to its paper theorem. The endpoint monoid alone loses generator information; the full labelled graph already determines counts. Useful algebra must organize equivalences or quotients, not claim extra count information beyond that graph. No new algebraic classification from a bare submonoid is established.

## 5. Updated audit dispositions

Original150-ID extraction and phase2 status snapshot remain unchanged. Current phase3-claim-status.json changes only23-01 from unresolved to established:

| Cumulative category |Count|
|---|---:|
| Established/answered under explicit conventions |58|
| Literal source claims disproved |19|
| Unresolved |61|
| Verified finite numerical-table claims |10|
| Context |2|

131 IDs have been fully or partially investigated, unchanged. Among61 unresolved,44 have partial investigation and17 remain uninvestigated. These are not58 new theorems, and this pass deliberately did not maximize sequence-resolution counts. New structural results are separate research statements, not invented additional original IDs.

## 6. Exact computation and independent reviews

New committed checks:256 binary inverse windows W5 with0,1 present;252 finite-support certificates (all63 nonempty subsets of[-2,3],q1..4); one signed rational inverse; invisible-negative-jump comparison through8; q5 positive uniform-prefix example through7. Weighted geometry checks cover2,955 rational transfer/component cases,672 integer cones and70 widening funnels. Independent weighted explicit words through5 verify endpoint rows/reconstruction. Sharp pre-horizon and nonmonotone examples, invalid inverse data and the positive-characteristic pivot limitation have regression tests.

Three refinement tests cover all excursion profiles through7, direct sylvester-congruence components for m1..4,n0..3,mn≤8 plus m1,n4/5, and exact two-formula comparison m1..8,n0..20. All earlier checks, including697 printed source values and phase2 exhaustive cases, remain. One command scripts/validate.sh runs the full suite, exact scripts, status/evidence checks and both LaTeX builds.

Actual phase3 agents: trajectory3 (trajectory author), geometry3 (geometry author), combinatorics3 (profiles/packed definitions), fresh_review3 (fresh proof/transcription). They supplied initially separate proof/counterexample/generalization reviews, with further direct coordinator scrutiny. Reviews caught inverse-operation order, empty-profile polygon scope, positive-characteristic pivots and overbroad 'all §23 resolved' wording; all repaired. Task paths, source scope, overlapping one-off versus committed checks and shared-model limitations are in review-log.md and ai-contributions.md. AI agreement is not proof or external peer review.

## 7. Publication structure and briefing

Main paper: weighted boundary geometry; finite structural rigidity/funnels; actual finite-range mass obstruction; labelled inverse data/counterexamples; brief known profile/packed context. Old factorial/tree details stay as supporting research/source files. No separate bijective paper is justified yet. See publication-structure-phase3.md.

The four-page briefing at briefing/main.tex states motivation linked to East–Ham, strongest results/proof ideas, exact limitations, primary reading boundaries, AI disclosure and specific questions for James. It is a mathematical discussion document, not a promotional claim. It has not been sent and James is not a coauthor. Local TeX builds were used; native editor tools were not exposed. No installation, external contact or publication submission occurred.

## 8. Assessment and recommended next questions

We now have a focused package worth discussing, especially because the remaining uncertainty is mathematical recognition/novelty rather than missing definitions or unverifiable numerics. It is **not yet established** that these arguments support a genuinely new standalone publication. Before further large computation, seek recognition of the exact finite-window and mass-obstruction statements and ask whether their combination has useful consequences. The briefing is ready for the author's review before any decision to approach James.

Best next questions: infinite-support actual trajectory converse under substantive reachability assumptions; optimal finite certificates; general-q cone connectivity and rational-boundary components; useful kernel/category equivalences; direct packed-class map; actual primary blob definition. Do not infer that positivity already solves the inverse residue problem or let classical profile enumeration become the paper's principal novelty claim. The pre-existing untracked lattice-paths.zip remains untouched.

## 9. Final validation

The complete `scripts/validate.sh` suite passed both in the working tree and in a clean export of all staged tracked files, without local reference caches or existing build products. All 27 unit tests passed, together with the retained exhaustive/source-array checks and the new exact trajectory, geometry and combinatorial checks described above. Both documents compiled without undefined references or overfull-box warnings: seven manuscript pages and four briefing pages. All eleven rendered pages were visually inspected with no clipping or overlap found. Generated PDFs and caches remain ignored; the source and reproducible build scripts are tracked.
