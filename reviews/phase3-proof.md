# Phase 3 independent proof review: geometry and combinatorics

16 October 2026. Reviewer: internal AI agent `/root/trajectory3`, distinct from the authors of the two reviewed notes. Supplied context: `AGENTS.md`, phase-2 background, and the phase-3 user request. Reviewed `research/phase3-geometry.md` and `research/phase3-combinatorics.md`; no other phase-3 review text was read. This is internal AI scrutiny, not external peer review or a novelty certification.

**Verdict: geometry proofs pass. Profile counting and packed-word generating-function identification pass, with two small presentation corrections required before promotion:** remove the final leaf before reverse-negating the preorder word; restrict polygon statistics to nonempty profiles. No substantive theorem defect found. The q>1 cone extrapolation remains unproved and must remain excluded.

## Geometry: independently checked arguments

For each source residue cell, summing weights and taking target difference q cancels every interior term, leaving exactly w(y−a_r+q)−w(y−b_r). Cell-indicator inputs therefore turn full-space preservation into edge equalities. Transitive closure is exactly constancy on graph components. Necessity and sufficiency use the additive group and do not require weights to be indicators, positive, rational, or characteristic zero. Testing indicators as functions valued in the same ring is valid. Disconnected congruence fibers admit a 0/1 counterexample over every nonzero ring. The zero-ring qualification in the note is appropriate.

For the widening-funnel result after shear, put M=s_{n−1}, K=s_n. Its difference window is [−M,K], and the new edges are {t,t+M+1} for every t∈[−M,K−M−1]. These are all consecutive edges within each residue class modulo M+1. When n=1, M=0 and [0,s_1] is connected, including s_1=0. For n≥2 the old window [−s_{n−2},M] is nested in the new one, is connected by induction, and has s_{n−2}+M+1≥M+1 consecutive integers. It meets every new residue class, connecting every new vertex to the old component. This validates arbitrary monotone width jumps and plateaux. Constant weights suffice directly. Unbounded nondecreasing widths exhaust Z at both ends. The integer-cone theorem is the special case s_n=kn.

The observable window is exact. No conclusion about values outside it is available at finite horizon. Neither the graph proof nor the funnel proof implies a classification for one actual origin trajectory; the distinction is retained correctly.

## Profile enumeration: independent proof check and correction

The displayed degree multiset has u+1 leaves and r_a vertices of degree a+1, hence N+1 vertices and degree-minus-one total −1. The first-global-minimum rotation argument is correct even with zero increments and repeated degrees. A proper period is impossible since it would divide total −1. The multinomial count divided by N+1 gives exactly N!/((u+1)!∏_a r_a!), including the empty excursion.

The written inverse operation has its order reversed. A correct inverse is: **delete the final −1 leaf of the preorder degree-minus-one word, then reverse the remaining word and negate every increment**. For example, tree word (1,−1,−1) becomes excursion (1,−1); reverse-negating first and deleting the last entry would fail. This is a local wording repair, not a change to the formula or the valid underlying bijection.

For polygon statistics, require a≥1 and a nonempty profile r≥1. Then face count r, face sides a+2, boundary sides u+2 and diagonals r−1 are consistent with Euler's relation. The empty profile has no ordinary polygon dissection and must not be assigned −1 diagonals. The general excursion formula continues to include that empty case.

## Packed-word identification and source scope

Directly inspected the [Novelli–Thibon v3 primary HTML](https://arxiv.org/html/1403.5962v3), §§2.7, 5.1 and 5.3: relation (31), the degree/multiplicity definition, formula (182), and surrounding (183)–(186). The note's definitions and x=2 interpretation are supported. Source scope was these passages, not a full-paper review.

Independently expanding F(z)=((1−z)/(1−2z)) proves the stated alternating binomial coefficient formula. Lagrange inversion for Z=tF(Z)^m gives [t^n]F(Z)=[z^n]F(z)^(mn+1)/(mn+1). The algebraic substitution H=F(Z) gives Z=(H−1)/(2H−1), hence H=1+tH^m(2H−1). All denominators used as formal series have nonzero constant term; the unique constant-one solution exists. Thus the axis identification is exact with horizontal coordinate mn, not just a sequence match. No direct path-to-class bijection has been proved, and none is needed for the counting claim.

The note's caution about source (186) is justified: at x=2 its displayed inverse has quadratic coefficient 1+2m, whereas the preceding polynomial gives m+2. This discrepancy must stay recorded as an apparent convention/formula inconsistency; the project's proof correctly uses (182) instead. Blob terminology and the three reflected positive rows are not resolved by this argument. The proposed axis-only audit disposition is appropriately narrow.

## Executed corroboration and limitations

Executed `python3 experiments/phase3_geometry.py`: 2,955 rational weighted graph comparisons, 672 integer-cone checks, and 70 widening-funnel checks passed. The host emitted three harmless stream-fd warnings before successful completion; no arithmetic assertion failed. Executed `python3 -m unittest experiments.tests.test_combinatorial_refinements -v`: all three methods passed, covering profile enumeration through seven steps, direct congruence cases stated in the note, and finite-formula comparison for m=1,...,8,n=0,...,20.

Tests corroborate the conceptual proofs. No optimal general horizon, q>1 funnel theorem, source-level blob definition, new combinatorial bijection, or mathematical originality is certified by this review.

## Independent follow-up: general growing interval windows

Reviewed `research/phase3-growing-windows.md` as a separate coordinator-authored extension. **Verdict: proof and stated corollaries pass.** No other review text was read for this follow-up, and I made no changes to the research statement.

The full-predecessor core is exactly

    J_n = I_n ∩ [A_{n−1}+M, B_{n−1}+m].

Indeed the smallest possible predecessor y−d is y−M and the largest is y−m. Thus membership is necessary and sufficient for every supported predecessor to be admitted by the previous interval. The core is an integer interval, so having q consecutive integers supplies one target in every residue. Since all previous residue cells exist and their endpoint values are uniform, interior recurrence gives the fixed circulant residue convolution. Summing over residues multiplies C_n by K even when some residue values vanish. Nonnegative total mass grows by at most K. Each residue cell of a length-L interval has size between floor(L/q) and ceil(L/q), independently of the interval's translation. The displayed strict width gap therefore contradicts C_B>0 exactly as claimed. The hypothesis that all residue cells exist ensures C_B=0 is equivalent to a zero row; positivity then makes zero persistent.

For completeness, if endpoint movements are bounded by V_A,V_B≥0, an explicit valid constant in the core-length lower bound is

    C = max(V_A,M) − min(−V_B,m).

Use max(A_n,A_{n−1}+M)≤A_{n−1}+max(V_A,M) and min(B_n,B_{n−1}+m)≥B_{n−1}+min(−V_B,m). Thus diverging widths imply every core eventually contains q consecutive integers. Eventual uniformity and diverging widths allow a finite H with the required gap for any sufficiently late B, proving extinction. This argument requires no monotonicity of widths or endpoint positions.

Floors/ceilings of fixed real affine functions with bounded periodic offsets have bounded successive endpoint movements and width (c−a)n+O(1)→∞ when a<c. Hence rational slopes, two-sided cones and the indicated periodic boundary perturbations all satisfy the corollary after layers become nonempty. In fact bounded offsets alone suffice for bounded successive movements; periodicity is a valid narrower example. The source explicitly distinguishes this actual-trajectory finite-support obstruction from an unproved structural classification for rational cones.

Checked the triangular specialization: J_n=[max(0,M), n−max(0,1−m)], reproducing the earlier T1f core and width multiplicities. Signed-weight and infinite-support exclusions are necessary for this proof; the bounded-width example is valid. No finite computation is needed to supplement these elementary inequalities. This review does not certify novelty of the positive-kernel mass argument.
