# Independent phase-2 proof review

16 October 2026. Reviewer: `/root/classification_phase2`, a separate internal Codex agent; actual backend version not exposed. Assigned classification derivation separately, then asked by coordinator to review `research/phase2-bijections.md`. Read that note, its two implementation/test files, and original Ham source text §§6–23. Did not read other agents' review reports before deriving these findings. This is internal AI review, not external peer review or human approval. Classification in the reviewer's own note is not independently reviewed here.

## Verdict

The stated excursion/tree/Dyck bijection and generating-function specializations survive proof review. No mathematical correction is required in the inspected version. They provide rigorous source interpretation using classical machinery, with no established novelty.

## Independent inference checks

For an excursion s_1,…,s_N, the reversed negative word has prefix sums H_(N−j), hence is nonnegative. Its appended −1 has total −1 and all earlier prefix sums nonnegative. The preorder slot count is one plus this sum: it stays positive until the final vertex and then vanishes. This establishes the tree construction without relying on enumeration. The final vertex necessarily has degree zero, because it must remove the final available slot. Removing it and reversing the transformation reconstructs the original excursion.

The degree encoding U^(d_1)D…U^(d_(N+1))D with the final D removed has N upsteps and N downsteps. At every completed retained block the height is the degree-minus-one prefix sum, nonnegative; intermediate prefixes only rise. Splitting an arbitrary Dyck word after appending D recovers exactly one degree list with a final zero. Every positive degree forms exactly one maximal ascent, so degree restrictions and ascent restrictions match individually, not only numerically. Empty words and A containing zero were separately checked.

Leaf count is u+1 and positive-degree multiplicity r_a is exact. Root decomposition gives T=x+Σq_a T^(a+1); dividing by x using T=xE gives E=1+Σq_a x^a E^(a+1). For unit-horizontal steps, x=q_a=z marks every original step once. For vertical downsteps, x=z,q_a=1 marks the horizontal endpoint; positive a bounds the number of downsteps by the number of upsteps, so no infinite-fibre issue arises. The zero case must be excluded for vertical steps, as the note does.

Source §§6–11 use zero or negative multiples of m and therefore degrees 1 modulo m, as stated. Source §§18–20 remove the appropriate zero or unary cases. Source §17's two models do produce the same axis equation E=1+z^m E^(m+1) with support at horizontal coordinates divisible by m; their total step lengths differ. For §§21–23, Σ_(k≥1)z^(mk)E^(mk+1)=tE^(m+1)/(1−tE^m), and rearrangement gives E=1+tE^m(2E−1). The displayed Lagrange coefficient follows from W=t(1+W)^m(1+2W), with n≥1. No indexing error found.

The reflection statement remains valid with vertical steps: reverse the order, negate only vertical displacements, and retain every horizontal displacement; height prefixes are original suffix heights, and total horizontal coordinate is preserved.

## Limits and opportunities

The present maps explicitly identify every excursion family with degree-restricted trees and ascent-restricted Dyck paths. Equal series for the two §17 models does not itself supply a direct invertible map between those two step conventions; such a map remains an additional worthwhile question, not an omission invalidating the theorem. Polygon, blob, packed-word and non-axis claims remain unproved by these maps; the note says so. Literature claims were checked for internal accuracy and limited reading disclosures, but this review did not independently read all cited papers and does not certify priority.

Implementation inspection agrees with the proof. The committed tests independently enumerate Dyck words and bounded excursions through original length 7, preserving exact ascent/degree multisets. This review's primary mathematical validation is the complete argument above, not a second invocation of those same tests.
