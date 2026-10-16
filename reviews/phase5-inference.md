# Phase 5 independent inference audit

16 October 2026. Reviewer: Codex task `/root/audit5`. This is an internal AI review, not external peer review or human author sign-off. The backend model identifier was not exposed. I read the Phase 5 user request, AGENTS.md, Phase 4 handover, conjecture audit, Phase 3 status snapshot, review log, the current relevant manuscript sections, and the Phase 4 obstruction/inverse/algebraic notes. I did not read other Phase 5 review reports before this reconstruction. No new literature theorem was read or priority determination attempted. Previous source-reading claims in the archive are not my independent source verification.

## Verdict

The sharp triangular finite-support certificate, its restarted-data sharpness example, widening-funnel reconstruction and weighted category reflection have complete elementary proofs under their stated hypotheses. I found no substantive error. One minor statement repair is advisable: explicitly require `N>=1` in finite-horizon funnel statements, because their observable window uses `s_(N-1)`. Keep integer shear `c`, fixed homogeneous kernel, and complete compatible labelled rows explicit. The proof below independently tracks all new unknowns, including jumps in width and plateaus. It does not infer corner-only recovery or certify novelty.

## 1. Boundary certificate reconstructed

Assumptions: triangle `I_n={0,...,n}`; integer `q>=1`; a time-independent nonnegative real kernel with finite nonempty positive support S, extremes m,M; arbitrary nonnegative initial row at b, followed by the usual transfer recurrence. Define `L=max(0,M)`, `R=max(0,1-m)`, `v=max(M,1-m)>=1`, and assume `b>=max(q-1,L+R+q-2)`. Every row from b through `b+ceil(q/v)` must be q-uniform. Neither origin generation nor positivity in every residue is required.

At transition n, the full-predecessor core is `[L,n-R]`. Its size is `n-R-L+1`, at least q for every `n>=b+1`. Every residue is represented in each source and target row. Write c_n(r) for its common value. Evaluation at a core target proves the cyclic convolution

`c_n(s)=sum_(d in S) f(d)c_(n-1)(s-d)`.

At any other target the actual sum is obtained by deleting predecessor terms. Both sums equal c_n(s), so each deleted term is zero individually. This is the precise place nonnegativity enters; it applies to an arbitrary initial row.

Here is a short conceptual formulation: **a positive residue and any supported jump propagate to a positive residue, but a boundary wrap of the corresponding extreme representative is forbidden.**

For a supported `d>0`, let r be the least representative of an active source residue. If `r+d>=q`, the least target y of residue r+d has predecessor `y-d=r-kq<0`, so a positive term would have been deleted. Therefore `r+d<q`, and the next least representative is exactly r+d. Repeated use of this same jump forces `r_t=r_0+td<=q-1`, impossible when `t=ceil(q/d)`.

For a supported `d<=0`, measure the least nonnegative distance delta from the source top to its active residue. The next top is one higher. If `delta+1-d>=q`, the largest target of the resulting residue would require a predecessor strictly above the preceding top. Hence `delta+1-d<q`, and successive distances are exactly `delta_t=delta_0+t(1-d)<=q-1`. This fails after `ceil(q/(1-d))` transitions.

Choose d=M when `v=M>0`, otherwise d=m. The contradiction occurs within `ceil(q/v)` transitions. A positive starting residue cannot die before this contradiction: the same positive summand in the full cyclic convolution propagates it. Thus c_b is identically zero. The initial row is zero.

This formulation suggests shortening exposition to: establish the deleted-positive-term lemma once, then give the two one-line potential functions `r_t` and `delta_t`. The present manuscript already essentially follows this proof. No asymptotic argument or positivity of all residue classes is needed.

### Exact restarted sharpness

Fix any positive integers q,v. Take the single unit-weight jump `d=1-v` and b a sufficiently large multiple of q, for example `b=q(2q+v+2)`. Start with value one precisely at heights congruent to zero modulo q. At elapsed time t the positive heights form that initial arithmetic progression translated by `t(1-v)`, restricted below by zero. Since d is nonpositive, final nonnegativity also ensures every intermediate vertex is nonnegative. The largest positive height is `b+t(1-v)`, at top distance tv. There are no holes below it in its residue.

Consequently for `0<=t<ceil(q/v)` every admitted vertex in the positive residue has value one, and all other residues have value zero: these are exactly `ceil(q/v)` consecutive nonzero uniform rows. At the next time the top distance is at least q, so at least one higher representative of that same residue is admitted but zero, while a lower representative is positive. Uniformity fails. The displayed b satisfies the theorem's full-core threshold. This includes q=1 and v=1 without exceptional treatment.

The construction prescribes a late row, usually not an origin-generated row. It proves sharpness over restarted data only. It supplies no optimal origin-start bound and no lower bound for an arbitrary fixed kernel.

## 2. Funnel elimination reconstructed

Assumptions: integers `N>=1,c`, monotone nonnegative widths `0=s_0<=...<=s_N`, origin start, a fixed field-valued kernel, and complete compatible labelled endpoint rows. For every transition n>=2, both preceding endpoint counts are nonzero. The condition is sufficient, not necessary. No positivity or characteristic restriction is needed after these nonzero pivots are assumed.

Shearing to c=0 replaces f(d) by h(d)=f(c+d). The geometrically visible differences through N are exactly `[-s_(N-1),s_N]`: each transition sees `[-s_(n-1),s_n]`, and these intervals are nested. Row one gives h on `[0,s_1]` directly.

At stage n, put `a=s_(n-2), b=s_(n-1), k=s_n`. All h on `[-a,b]` are known. The missing negative block is `[-b,-a-1]`. Select targets `y=b-a-1,b-a-2,...,0`, and isolate the source endpoint z=b. In its equation the unknown is h(y-b), with coefficient p_(n-1)(b). Every other argument y-z is strictly larger, at most b, and either initially known or previously recovered in this descending order. Every selected target lies in `[0,k]` because `0<=a<=b<=k`.

Afterwards h on `[-b,b]` is known. Select targets `y=b+1,...,k`, isolate source z=0, and divide by p_(n-1)(0). All other arguments y-z are smaller than y and at least 1, hence already known in ascending order. This recovers the missing positive block `[b+1,k]`. Empty blocks require no equation. In particular b=0, a=b, k=b and arbitrarily large k-b all cause no problem.

Thus every geometrically visible weight is uniquely determined. Outside the displayed window no transfer coefficient ever queries h, so unrestricted field-valued weights there are free. This is geometric invisibility, not a claim every visible weight is identifiable when pivots vanish.

Full preceding rows supply the coefficients, even though the selected equations target new extremes. Two boundary sequences alone do not supply them. Nonzero rows do not imply nonzero corner pivots. Over positive characteristic, indicator kernels containing 0,1 need not have nonzero pivots because counts can cancel. Ordinary nonnegative counting guarantees need to stay distinct from the field theorem.

The affine full-data fiber claim is also correct: for prescribed complete rows, the recurrence is linear in kernel coordinates; a solution recreates all the prescribed rows by induction. Unobserved intermediate rows would instead be kernel-dependent, so general partial observations do not inherit that affine description. No silent uniqueness claim from row sums or multisets is justified by this proof.

## 3. Reflection and composition reconstructed

Objects are admitted triangular vertices `(n,y)`. A morphism is an admissible directed word from a specified starting vertex to a specified ending vertex; identities are empty words and composition is concatenation in path order. This includes arbitrary admitted starting vertices, not just the origin. For step sets use only the allowed jumps; for weighted categories one may retain all edges with their weights, or retain the nonzero support, consistently on both sides.

Map vertices by `R(n,y)=(n,n-y)` and each jump d by `1-d`. If a step starts at `(n,y)` and ends at `(n+1,y+d)`, its reflected displacement is `(n+1-y-d)-(n-y)=1-d`. Thus endpoints match and each intermediate vertex stays in the triangle. Applying R twice is the identity. The empty word stays empty. For composable words u,v, the reflected word of their concatenation is exactly the concatenation of their reflected words, in the same order. There is no reversal of chronological order and no contravariance.

Set `f^R(e)=f(1-e)`. Then `f^R(1-d)=f(d)`, factor by factor, so R preserves word weights and length. This proves an involutive weighted category isomorphism between the f and f^R models.

For origin observations the origin is fixed, and `p_n^(f^R)(y)=p_n^f(n-y)`. Row totals and row multisets agree. Endpoint labels are reversed; fixed residue labels are permuted by `r -> n-r mod q`; bottom and top sequences are interchanged. Individual labelled values, fixed-label residue sums and fixed diagonals are not generally preserved. For example `{0,1,2}` gives row two `(1,2,2)`, whereas its reflected set `{-1,0,1}` gives `(2,2,1)`. Both contain 0,1 and hence have positive ordinary counts at every triangular vertex. Reflection is therefore a genuine nonidentifiability obstruction for totals/multisets, without implying that all such ambiguities are reflections.

## Limits of this audit

I reconstructed the arguments symbolically, including the relevant edge cases; I did not run another exhaustive computation because it would add little to these short proofs. This report does not audit the q=2/q=3 seed algebra (assigned separately), infer general-q results, validate source priority, or replace compilation/render inspection. The original 150-claim disposition ledger is unchanged. Readiness to request specialist scrutiny is compatible with unresolved novelty; it is not a claim of publication readiness.
