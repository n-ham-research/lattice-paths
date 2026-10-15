# Phase 4 fresh independent adversarial proof review

16 October 2026. Reviewer: actual internal task `/root/fresh4`. Read the Phase 3 handover/audit/status and review instructions, then `research/phase4-obstruction.md`, `research/phase4-inverse.md`, `research/phase4-infinite.md`, and manuscript sections 09, 10 and 12. No other Phase 4 review reports were read before this assessment. Shared AI tools/model limitations apply; this is not external peer review and does not certify novelty.

## Initial disposition

The substantive statements examined have complete proofs under their stated hypotheses. No mathematical defect was found. Two manuscript synchronization issues were reported to the coordinator: section 10's old unqualified statement that no q>1 infinite-support converse is claimed, and section 12's old q>=3 scope limit, are obsolete once the new q=3 theorem is included. These are transcription/scope repairs, not counterexamples to the proved results.

## Obstruction

Independently checked the full-core threshold: `[L,n-R]` has at least q points at every transition after the displayed b. Uniformity therefore gives full residue convolution, even with initially zero residue values. The omitted-term argument uses nonnegative *individual* terms, and is invalid for general signed weights; the source correctly retains that restriction. A positive chosen edge persists through full convolution, so no silent loss of the propagated residue occurs. Least bottom representatives for d>0, and least top distances for d<=0, cannot wrap without a forbidden positive missing summand. Thus T=ceil(q/v) transitions is sufficient.

The restarted singleton construction was independently simulated for all q=1,...,12 and v=1,...,14 (168 parameter pairs): every row before T is uniform, and row T is not. The proof and paper explicitly distinguish this sharpness from origin-start optimality. The origin-start {0,1} binomial comparison is valid, including singleton-support cases; n=q with equal positive weights proves its threshold sharp.

For varying nonnegative kernels within a fixed support envelope the product-of-masses cancellation works, provided zero total weight is handled as immediate extinction. The stronger r+delta argument also checks: reduction modulo q only increases either raw representative when negative, and forbidden wrap prohibits values >=q, so their sum increases by at least one per transition. This is a restarted-data bound and is not asserted sharp for origin starts.

## Inverse data and funnels

The full observation fiber really is affine: induction is essential and is supplied. Deleting equations without knowing their predecessor arrays would not give the genuine partial-observation fiber; this limit is explicitly preserved. Row-space identifiability is over unrestricted field-valued models, with admissible intersections required for nonnegative/indicator models.

For widening funnels the negative-block order works with arbitrary width jumps: at the first target y=b-a-1 the smallest other argument is -a, and each later target uses only earlier recovered negative arguments. The positive block uses only smaller arguments. Plateaus, zero initial width, b=0 and empty blocks are harmless. Nonzero field pivots are assumed rather than inferred from reachability in positive characteristic. The scalar actual-data corollary correctly invokes the one-dimensional structural result and requires nonzero rows. Ordered-kernel equivalence uses finite sums of nonnegative word differences and is valid for every fixed finite endpoint horizon, including infinite jump support.

## Small moduli

Independently expanded the q=2 interior comparison algebra and checked its factorization against the recurrence at 30 distinct nonnegative rational x values using exact fractions. This is supporting arithmetic, not the proof of the identity; direct hand expansion of the rational expressions supplies that check. The nonnegative root alternatives are exactly 1 and sqrt(2)-1. Rational normalization preserves rationality because t is positive rational in that class. In the exceptional branch every listed coefficient is positive, row five is scalar, and the sixth-row equality needs 7-5sqrt(2)<0. Thus the three sharp thresholds (real 6, rational 5, indicator 3) are correct for the explicitly specified equal initial weights and all-prefix uniformity. They are not eventual-uniformity or general-q results.

For q=3 indicators, independently enumerated the 16 assignments of a,b,A,B in {0,1} and checked that equal row-three extremes force a=b and A=B. The formula P=1+3x+(1+x)c is positive; row-four equality forces the new extremes c+(Q/P)(1-c). The c=0 alternatives 3 and 3/2 are impossible indicator weights. Thus the periodic seed is established. Propagation compares with the globally periodic continuation, uses interior endpoints of the same residue and ordinary positive corner counts from jumps 0,1; no unsupported structural-to-actual converse is invoked. The {0,1} prefix through three proves optimality of the horizon four.

## Limitations and checks actually executed

One-off independent script `/tmp/fresh4check.py` used standard-library exact fractions and direct endpoint recurrences; it executed the 168 restarted cases, 30 rational identity instances and 16 q3 seed assignments above. An attempted symbolic-package import failed because SymPy is not installed; no symbolic computation is claimed. The reviewed repository script was read only after the proof assessment. No source or implementation files were changed by this reviewer. Literature priority was not independently searched and remains unresolved.

Final manuscript/briefing synchronization will be recorded below after those files settle.

## Final manuscript and briefing transcription

After the coordinator saved the rewritten four-part `briefing/main.tex`, I read it in full together with the finalized manuscript section 12. The two previously reported obsolete scope statements are repaired. The q=3 theorem and periodic-seed propagation match the research proof; q=2 coefficient domains and three sharp horizons are preserved. The briefing accurately distinguishes restarted-data sharpness from origin starts, all-prefix from eventual uniformity, and full labelled data from compression. The finite-range certificate retains the support-dependent core threshold and nonnegative homogeneous hypothesis; the layer-dependent extension is limited to the mass proof.

The funnel extension says “same recovery”, thereby inheriting the preceding nonzero-pivot restriction. An explicit repetition of that restriction would make the standalone paragraph clearer, but its current contextual statement is mathematically consistent. No blocking correction is required. The original disposition counts sum to 150 and are unchanged. Checked the committed obstruction script directly: its 255 support subsets and 144 restarted cases match the briefing (different from this reviewer's separate 168-case sweep). Parity/reflection/funnel domains and 650 rational parameter instances agree with their source scripts/notes.

The cited reading boundaries match the targeted-source ledger and do not assert whole-paper reading of new inverse sources. The new bibliographic entries' identifiers, titles and theorem ranges match that ledger. Independent attempted browser access to both new arXiv abstract/version URLs returned cache misses; consequently I have **not** independently certified the bibliography metadata or their theorem statements from primary pages in this fresh review. The coordinator's separately logged direct source inspection remains the evidence. No new literature verification or novelty conclusion is inferred from the failed access. Final source-level disposition: ready for coordinator's build/render validation.
