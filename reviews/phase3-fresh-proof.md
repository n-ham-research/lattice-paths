# Fresh Phase 3 proof review

16 October 2026. Reviewer: internal AI agent `/root/fresh_review3`. Exact backend model identity is unavailable and is not asserted. This is internal AI review, not external peer review.

## Independence and verdict

Supplied task: independently reconstruct the finite-support obstruction and its finite certificate, endpoint inversion, weighted graph characterization, and arbitrary widening funnel theorem before manuscript briefing. I read the three Phase 3 research notes and repository instructions before any Phase 3 review text. I did not read other Phase 3 reviews. Phase 2 background was consulted in a truncated combined display; this review does not certify that ledger or its literature audit.

**Approve the mathematical arguments under their stated hypotheses.** No blocking proof defect found. This verdict does not establish novelty, independently certify the cited literature, or settle the explicitly open infinite-support actual-trajectory converse.

## Reconstructed arguments and attempted boundary objections

For T1, choose the starting uniform row sufficiently late that it and each later source row contain every residue, and every later target has an interior representative of every residue. Finite support supplies these representatives. Their recurrence gives exact residue mass growth by K. Nonnegative weights separately give total endpoint mass growth at most K. A uniform row has at least floor((n+1)/q) copies of each residue mass. Cancelling the common positive factor K^(n-B) contradicts unbounded width. Zero residue masses cause no problem: nonnegative nonzero rows still have positive total residue mass. Extinction is absorbing by the recurrence. Signed weights invalidate the comparison, and the note correctly excludes them from T1.

For T1f, B >= q-1 makes C_B well-defined, while B >= L+R+q-2 gives q interior targets starting with transition B+1. The final row satisfies floor((H+1)/q) = ceil((B+1)/q)+1, whereas the initial total-to-residue ratio is at most ceil((B+1)/q). This is a strict contradiction for positive C_B. If B+1=aq+r with 0<=r<q, the number H-B+1 is q+1 when r=0 and 2q-r+1 otherwise, hence at most 2q. The q=1 case and zero initial uniform row are included. No claim of optimality follows.

For T2, at transition n the top equation introduces only f(n), with coefficient p_(n-1)(0), and the bottom introduces only f(1-n), with coefficient p_(n-1)(n-1). Every other difference belongs to the previous recovered window. The base transition identifies f(0),f(1). Thus full labelled rows, including previous-row interiors, determine the observable window by induction. This works over any field and permits signed weights when pivots remain nonzero. It is a sufficient pivot condition, not a necessity theorem. The invisible-negative-jump example correctly shows why nonextinction alone is insufficient. The q=1 indicator-weight corollary uses the interior endpoint y=1 at each n>=2 and correctly forces n! and then both new indicator weights to equal one.

For the weighted graph theorem, telescoping a single residue-cell sum leaves precisely w(y-a_r+q)-w(y-b_r). Testing source-cell indicators is sufficient and necessary for the entire invariant subspace. Ring addition permits cancellation, including positive characteristic; no division or positivity is used. Empty source cells impose no edges, isolated observable differences remain free, and zero rings need the stated qualification for the disconnected-fiber counterexample.

For widening funnels after the shear, transition [0,M] to [0,K] supplies all adjacent pairs along each congruence class modulo M+1 in [-M,K]. The old connected window [-s_(n-2),M] is nested inside the new window and contains at least M+1 consecutive integers. Thus it intersects every new congruence chain, so every new vertex joins the old component. This remains valid for zero widths, repeated widths, and arbitrarily large width jumps. Monotonicity is essential to this argument. Unbounded monotone widths exhaust both ends of Z. Bounded monotone integer widths stabilize, leaving only the limiting finite observable window constrained. This is structural preservation of all constant inputs, not an accidental-origin-trajectory classification.

The profile rotation proof handles repeated letters and N=0: total increment -1 excludes a nontrivial rotational period. The generating-function manipulation for the packed-word identification is algebraically consistent. These are classical applications; I have not independently re-read primary formula (182), so source identification remains contingent on the separate source review. Blob terminology and direct congruence-class bijections remain unresolved as stated.

## Executed corroboration and limits

Ran `python3 experiments/trajectory_inverse.py`: 256 binary inverse cases, 252 finite-support obstruction cases, one signed rational reconstruction, one nonidentifiability comparison, and one nonperiodic uniform-prefix counterexample passed. This is rerunning the committed implementation, not an independent exhaustive verifier and not a replacement for the arguments above. No contact with other people, commit, or publication action was performed.

## Independent addendum: general growing windows

After the first verdict, I received and read `research/phase3-growing-windows.md`, without consulting any other review. **Approve this extension under its stated hypotheses.** The full-predecessor core is exactly the intersection of the target interval and all supported predecessor translates: its lower bound uses the maximum jump and its upper bound the minimum jump. Having q consecutive targets provides one representative of each residue. This yields the same exact residue-mass multiplier K even when intervals move and their residue-cell populations change. Any consecutive integer interval of length ell has each residue multiplicity between floor(ell/q) and ceil(ell/q), independently of its position. Thus the finite multiplicity-gap contradiction remains valid without nested intervals, monotone widths, or a fixed origin.

For the endpoint-movement corollary, let D_A,D_B bound the absolute successive movements. The core's signed length is at least

    |I_(n-1)| - C,
    C = max(D_A,M) - min(-D_B,m).

This explicit nonnegative constant justifies the asserted bound. Diverging widths therefore ensure a core of at least q consecutive integers eventually. Choose B after both eventual uniformity and this core condition hold, then choose H with floor(|I_H|/q)>ceil(|I_B|/q). The finite theorem forces the late row zero, and the recurrence makes extinction permanent.

Fixed real slopes with a<c and bounded perturbations suffice: rounding changes successive movements by a bounded amount, and the width grows linearly up to a bounded error. Periodicity of the bounded perturbations and rationality of slopes are unnecessary for this obstruction, as the note correctly acknowledges. Restricting to nonempty admitted layers is necessary. Nonnegative weights and finite support remain essential hypotheses of this particular proof; it makes no signed-weight or infinite-support claim. I found no counterexample or missing condition. This addendum is a proof reconstruction, with no new computational or literature certification.

## Final narrow manuscript transcription review

Reviewed `paper/sections/07-general-results.tex`, `09-actual-trajectories.tex`, `10-inverse-enumeration.tex`, `11-combinatorial-context.tex`, and `briefing/main.tex`. The weighted graph and funnel statements match the reviewed arguments. The finite mass multiplicity inequality, triangle b/h bounds, full-row inverse caveat, and distinction between finite-prefix evidence and an infinite-support converse are preserved. No novelty inflation was found.

Two corrections were reported to the coordinator before final acceptance:

1. The inverse theorem is valid over any field conditional on its nonzero pivots, but the following claim that indicator weights with 0,1 in D guarantee those pivots needs characteristic zero, or explicit ordinary integer/rational counting. In characteristic two, D={-1,0,1,2} has p_1=(1,1) and p_2=(2,2,2)=0, so the n=3 pivots vanish. The all-zero and all-one words establish positivity only in ordinary counting, not nonvanishing in arbitrary characteristic. This affects both section 10 and the briefing.
2. Section 11's opening claim that all of Section 23 is resolved is broader than the established axis-extraction packed-word family. Blob terminology and other rows remain unresolved. Narrow that sentence to the proved family.

A minor clarity correction was also requested: explicitly write I_n=[A_n,B_n] intersect Z in the mass theorem before using those endpoint symbols. Subject to these corrections, the reviewed transcription is approved. The original research-note verdict is unchanged; its unweighted pivot guarantee was in ordinary counting, while field generality was conditional on pivots.

### Repair verification

Re-read the targeted repaired sentences in sections 09, 10, 11 and the briefing. The interval endpoints are now explicit; indicator pivot guarantees are restricted to ordinary counts/characteristic zero with positive-characteristic cancellation stated; and the Section 23 claim is narrowed to its axis-extraction packed-word family. All requested transcription repairs are verified. Inspected the new characteristic-two regression and ran `python3 -m unittest experiments.tests.test_phase3_inverse`: four tests passed. Also reran `experiments/trajectory_inverse.py` successfully. No outstanding defect from this review remains; transcription approval is now unconditional within the stated review scope.
