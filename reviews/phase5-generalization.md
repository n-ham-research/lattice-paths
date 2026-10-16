# Phase 5 focused scope and generalization audit

16 October 2026. Actual internal reviewer `/root/novelty5`; exact backend model/version unavailable. Supplied Phase 5 request, AGENTS.md, prior handover/claim-audit/status/review log, Phase 4 mathematical notes and current manuscript. Initial audit performed without reading the other Phase 5 review reports. Shared tools and prior model context limit independence; this is not external peer review. No new theorem is proposed here.

## Boundary certificate reconstructed

I reconstructed the proof from the recurrence, not from finite tests. With support [m,M], the full-predecessor core at transition into row n is [max(0,M), n−max(0,1−m)]. The stated b bound guarantees at least q consecutive core targets for every transition after row b. Every residue therefore has a full-convolution representative. A boundary target with the same residue has the same output; subtracting its restricted sum from the full sum gives a sum of omitted nonnegative terms equal to zero.

If source residue r is active and d>0 is supported, its least representative r lies in [0,q−1]. If r+d≥q, the least representative of the target residue has predecessor r−kq<0 for k≥1; the omitted contribution is strictly positive. Hence r+d<q. The next active residue has representative r+d. Repeating a single positive d can survive fewer than ceil(q/d) transitions from any initial r. For d≤0, use the least distance δ from the moving top. A permitted transition changes that distance by 1−d; any wrap creates an omitted predecessor above the old top. Thus δ+(1−d)<q is necessary at every transition. Taking d=M or m realizes v=max(M,1−m) and gives exactly the stated contradiction after ceil(q/v) transitions.

This proof needs neither an origin-generated initial row nor every residue positive: one active residue and one positive supported weight suffice. It does need nonnegative values, homogeneous supported jump for the propagation chain, consecutive uniform rows, and the full-core threshold. “Arbitrary prescribed nonnegative data at b” is valid because the proof starts with that row; uniformity of b is still required. No conditional distribution normalization is used.

Sharpness scope is correct: a late prescribed residue-zero row and one jump 1−v yield ceil(q/v) nonzero uniform rows, not ceil(q/v)+1. This cannot establish optimality for a delta mass at the origin. No promotion of restarted sharpness is justified. A concise conceptual summary is: **full-core equality makes every boundary omission impossible for an active residue; one extreme jump eventually forces such an omission.** This is already the short proof, rather than a consequence of asymptotic mixing.

## Reconstruction and observations

The widening-funnel proof handles arbitrary nondecreasing width jumps. After shear, at transition n put a=s_(n−2), b=s_(n−1), k=s_n. Existing weights occupy [−a,b]. Descending targets y=b−a−1,...,0 solve the new arguments y−b with pivot p_(n−1)(b): every other argument is greater than y−b and at most b. Ascending targets y=b+1,...,k then solve f(y) with pivot p_(n−1)(0), using only smaller already known arguments. Plateaus and zero initial widths make a block empty, not singular. The interval of observable differences is exactly [−s_(N−1),s_N]. Restoring the shear adds c.

Both nonzero pivots are sufficient field hypotheses, not claimed necessary. Full previous endpoint rows are genuinely used. Two corner sequences alone do not supply their interior summands. Positivity from indicator jumps 0,1 is an ordinary characteristic-zero fact; the conditional field statement must not replace it by an unconditional positive-characteristic assertion.

For prescribed full rows, A(p)g=p is linear because each previous row is known; induction proves sufficiency. The row-space criterion concerns unrestricted field-valued fibers. Intersecting with nonnegative or binary kernels may give uniqueness without full rank. If intermediate rows are unobserved, replacing them by fixed coefficients is invalid; the existing manuscript explicitly avoids this. Reflection preserves row totals and multisets, whereas fixed coordinate observations are generally permuted.

## Small-modulus assumptions and exact algebra

I rechecked the displayed normalized parity algebra: row two forces equal adjacent exterior weights x; row three gives c=(x²−x+2)/(x+1); row four gives a=(3x−1)/(x+1). Substituting the latter two in A(a−c)+B(c−x) gives the stated factor. Nonnegative x permits precisely 1 and sqrt(2)−1. On the latter branch c=3sqrt(2)−3, a=3−2sqrt(2), b=6sqrt(2)−7 are positive; the scalar fifth row forces the sixth new lower weight to be 7−5sqrt(2)<0. The three coefficient-class horizons are therefore consistent with the proof, not merely rational sampling.

For q=3 the binary equation 3(a−b)+(1+b)A−(1+a)B=0 excludes a≠b by a signed gap of at least one. With a=b=x and A=B=c, c=0 forces the next binary weight to be 3 or 3/2; hence c=1. The resulting seed has exactly the announced residue mask. The D={0,1} examples demonstrate the sharp finite-prefix horizons in their respective classes. The seed bootstrap uses an interior endpoint in each new boundary residue and nonzero pivots; m≥q supplies those representatives. Neither argument proves the arbitrary-q seed theorem.

The assumptions f(0)=f(1)>0 or indicator 0,1∈D are not dispensable from these established statements. Without any nonextinction qualification, D={2} supplies a nonperiodic kernel and an extinct, hence uniform, origin trajectory at every positive layer. This only demonstrates that unrestricted removal is false; it does not settle whether a suitably nonextinct replacement hypothesis suffices. The equal-real-weight hypothesis is stronger than positive reachability and remains explicit.

## Reflection checked as a functor

An edge from (n,y) to (n+1,y+d) maps to an edge from (n,n−y) to (n+1,n+1−y−d), with jump 1−d. Both vertices stay in their triangular layers. The transformed weight f^R(1−d)=f(d), so products are unchanged. Applying twice is the identity. Edge order is unchanged; concatenation maps to concatenation and empty words to identities. Thus this is an involutive covariant weighted-category isomorphism for arbitrary allowed starting vertices. It reverses each origin row, rather than preserving its endpoint labels. Individual residue sums may be permuted. No claim of classifying all observation equivalences follows.

## Literature and disposition

The directly inspected primary statements and exact scope are recorded in research/phase5-novelty-ledger.md. Standard invariant-space criteria, affine inverse fibers, elimination and graph relabelling should be presented as established mechanisms. The precise geometric certificate and compressed seed calculations remain candidates for recognition, with no priority certification. No mathematical defect requiring a theorem withdrawal was found in these statements. Recommend external specialist scrutiny with the assumptions and restarted/origin distinction retained. This audit did not execute the entire validation suite or inspect the final rendered PDFs; those remain coordinator checks.
