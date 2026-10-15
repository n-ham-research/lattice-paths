# Phase 4 independent inference review

16 October 2026. Actual internal agent `/root/infinite4`, author of the separate modulus-two note. Context supplied: research/phase4-obstruction.md and research/phase4-inverse.md, the standing project instructions and Phase 3 background. I did not read other Phase 4 review reports before these findings. Exact backend model version is unavailable; this is internal AI scrutiny, not external peer review or evidence of model diversity.

## Sharpened obstruction

I independently reconstructed O4.1 from the full-core identity and the fact that a sum of nonnegative missing contributions can vanish only term by term. A positive active residue transported repeatedly by a fixed positive jump cannot wrap its least representative across zero; for a nonpositive jump, its distance from the advancing top cannot wrap. The extreme outward speed v=max(M,1−m) is always at least one for integer support. Thus T=ceil(q/v) transitions are sufficient, including the q=1 endpoint and jumps larger than q. I found no proof gap.

I checked that the restarted single-step example has no lower missing active endpoints: its translated residue support, truncated below zero, fills that residue until the upper top-distance reaches q. Its role is explicitly only restarted-data optimality, not origin-start optimality. The binomial-row application for support contained in {0,1} correctly compares two independent repeated-residue equalities, with a separate deterministic-step case. The q+1 origin threshold is sharp at equal positive weights and n=q.

The nonhomogeneous active-residue proof is sound: reducing a negative proposed least representative or top distance modulo q can only increase the relevant quantity. Each selected positive edge increases their sum by at least one. The restarted ordering of q−1 jumps one followed by q−1 jumps zero gives 2q−1 uniform rows. Common support-envelope and full-core conditions remain explicit. Signed weights and nonconsecutive uniform rows are still unresolved in this note; failure of the positive proof is not advertised as a counterexample.

Independent one-off exact check (not an extra committed test): all 63 nonempty subsets of [-2,3], q=1,…,5, and all 2^q−1 nonempty binary active-residue initial rows, at each theorem's smallest allowed b. For each case I iterated the actual restarted recurrence through T=ceil(q/v); all 3,591 cases failed uniformity within the predicted interval. This check is finite corroboration, not the proof.

## Inverse enumeration and funnel geometry

I1 correctly linearizes full-data fibers only after predecessor rows are fixed. The induction proving sufficiency prevents the usual mistake of treating the nonlinear observation map itself as linear. The row-space, affine-periodicity and constrained-fiber qualifications are accurate. Partial unknown-trajectory observations are explicitly not solved by deleting matrix rows; the degree-two example shows why.

I2's widening-funnel inversion works with plateaus, sudden width jumps and width zero. For the negative block, the first target delta−1 has smallest other argument −a, and subsequent targets use already recovered values. No new positive extreme enters that block. Positive recovery uses targets b+1 upward and only previously recovered smaller arguments. These targets exist by monotone widths. Conditional corner pivots and exact geometric visibility are correctly separated from necessity of those pivots.

I3 follows because a nonzero scalar actual input tests the entire one-dimensional constant subspace. Applying the already proved monotone-funnel graph result then gives a constant kernel throughout the observable interval. The nonnegative-real and nonzero-row conditions make alpha positive. The statement explicitly avoids the invalid analogous inference in a higher-dimensional residue subspace. I4's reflection changes each jump to 1−d; labelled endpoints are reflected, so row multisets/totals agree while fixed residue labels need not. I5's ordered-kernel criterion follows term by term with no cancellation, and its restriction to comparable kernels is essential and explicit.

I also ran `python3 experiments/phase4_inverse.py`: 70 reconstruction cases, 70 scalar-funnel formula cases, 256 binary reflection cases and the nonlinear sparse-observation example pass. These are the author's committed checks rerun independently, not additional independent enumerations.

## Disposition

Accept the exact mathematical statements within their stated scope. No defect requiring repair found. The strongest distinction is between the actual-trajectory sharpened boundary certificate, the special compressed scalar inverse theorem, and standard full-fiber linear algebra. Novelty remains unresolved. Neither the comparisons with killed-walk or inverse-graph literature nor agreement among internal agents establish priority.
