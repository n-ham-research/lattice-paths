# Phase 4 independent generalization / proof review

Reviewer: actual internal agent `/root/inverse4`, 16 October 2026. Supplied context: Phase 3 handover and mathematical notes; Phase 4 request; authored the separate widening-funnel inverse note. Read `research/phase4-infinite.md` and `research/phase4-obstruction.md` directly, not other Phase 4 review reports. The coordinator announced the target modulus-two horizons, but I reconstructed the elimination through row five before the detailed proof existed. This is internal AI checking, not external mathematical peer review; exact model version was not supplied.

## Modulus-two compressed inverse theorem

I independently obtained, after normalizing f(0)=f(1)=1 and writing x=f(-1)=f(2),

- f(-2)=f(3)=(x²-x+2)/(x+1);
- f(-3)=f(4)=(3x-1)/(x+1);
- p_3 is scalar with value C=x²+2x+3;
- the row-five difference p_5(1)-p_5(3) is `-2C(x-1)²(x²+2x-1)/(x+1)²`.

This checks the central polynomial and its real/rational split independently of the note's derivation. I then checked all substitutions for x=sqrt(2)-1: c=3sqrt(2)-3, a=3-2sqrt(2), the forced next value b=6sqrt(2)-7, and the row-six comparisons. With scalar row-five value T, the compared sums are 3sqrt(2) and 8sqrt(2)-7+f(-5), so the necessarily negative f(-5)=7-5sqrt(2) is correct. Every denominator divided by in the proof is positive under the hypotheses.

The induction after a constant window is valid because all next-row interior entries use already known differences and both new boundary entries have interior representatives of their parity. No unstated assumption of finite support is used: all finite recurrence sums are finite in this geometry. The indicator and rational sharp prefixes match the forced formulas. The equal positive initial weights, nonnegative real/rational coefficient domains, origin start, all-initial-rows requirement, and finite-prefix rather than infinite-counterexample scope are essential and are accurately stated. No assertion is justified for unequal initial weights, q>=3, signed weights, or merely eventual uniformity.

Disposition: proof accepted under the exact written hypotheses. The polynomial identity and elementary elimination may be familiar, so this review supplies no novelty certification.

## Sharpened homogeneous finite-support certificate

O4.1's full-core argument correctly upgrades missing nonnegative sums to zero individual summands. A fixed positive step d>0 propagates a positive residue's least representative upward without a wrap through q; a fixed d<=0 propagates its least distance from the moving top upward by 1-d without a wrap. These are precisely the *one-sided* directions in which missing contributions give contradictions. The selected extremal step has speed max(M,1-m), giving ceil(q/v) transitions. The source block's first row need not be generated from the origin.

The single negative-step restart example has uniform rows for t<ceil(q/v): top distance is tv<q, and the translated residue fills every admissible target of that residue. At the next transition a top representative is absent while lower ones remain positive for the chosen large b. Thus it establishes sharpness for arbitrary restarted data, not for origin-start data. The distinction is explicitly maintained. The weighted {0,1} binomial comparison and sharp n=q versus forbidden n>=q+1 threshold are correct.

The inverse range exclusion t*v<q follows exactly from the integer inequality t<ceil(q/v), conditional on the candidate core threshold. It does not rule out kernels whose support is too wide for that threshold, and the text correctly keeps the condition.

## Error found in the initial nonhomogeneous auxiliary argument

The first O4.3 draft asserted that for an arbitrary selected jump both least representative r and least upper distance delta evolve without modular wrapping. This is false: a negative step can wrap a least representative from 0 to q-1 while preserving uniformity, and a positive step can harmlessly wrap the upper distance downward. The homogeneous proof avoids this error by using only the appropriate one-sided coordinate for its fixed extreme jump.

I informed the coordinator immediately. The correct nonhomogeneous bound is still supplied by the Phase 3 mass proof: finite common support envelope gives full cores, C_n=K_n C_(n-1), P_n<=K_n P_(n-1), and the positive products cancel. The original at-most-2q-rows bound follows. The 0/1 restarted nonhomogeneous construction gives 2q-1 surviving uniform rows, so it independently shows this bound is sharp for restarted data. The invalid two-coordinate derivation must be removed; this review does not approve it.

## Limits retained

The signed and nonconsecutive extensions remain open, rather than falsely interpreting proof failure as a counterexample. Infinite-support factorial rows, individually finite but nonuniformly bounded time-dependent supports, and bounded-width geometry are valid failures of overly broad generalizations. The cited killed-walk comparison has carefully delimited source scope. These results do not settle optimal origin-start block length or general-q infinite-support converse.

### Verified repair

The revised O4.3 now uses the correct inequalities, not equalities: missing contributions force `r_n+d<q` and `delta_n+1-d<q`; negative values are permitted, and reduction modulo q only increases them. Therefore `r_(n+1)>=r_n+d` and `delta_(n+1)>=delta_n+1-d`, so their sum increases by at least one. This fully repairs the auxiliary proof and gives the same sharp restarted nonhomogeneous 2q bound directly. I read and checked this replacement after my initial report; no unresolved correctness issue remains in O4.3.
