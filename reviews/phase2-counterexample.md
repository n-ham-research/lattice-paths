# Phase-2 independent counterexample review

16 October 2026. Reviewer: `/root/bijections_phase2`. Supplied context: coordinator's proposed finite/infinite residue-preservation classification and, subsequently, `research/phase2-classification.md`. I did not read other phase-2 reviews before these findings. Same-model internal AI review, not external peer review or author sign-off. No novelty determination.

## Classification verdict

**Pass for the precise structural statements A–C as written**, including the N>=q condition and the requirement to preserve the entire space of residue-constant input vectors at every transition. I found no mathematical counterexample. This verdict does not classify a single counting trajectory, establish an algorithmic complexity improvement, or assert novelty.

Before reading the proof file, I independently expressed the condition as follows. For every n=1,...,N, y=0,...,n-q, and r=0,...,q-1, require

    sum_(0<=z<n, z≡r mod q) f(y-z)
      = sum_(0<=z<n, z≡r mod q) f(y+q-z).

All observable differences lie in [1-N,N]. I exhaustively tested **every one of 21,732 indicator patterns** across q=1,...,4 and N=q,...,6. In every case this condition was equivalent to f(k)=f(k+q) for 1-N<=k<=N-q. Thus both necessity and sufficiency survived exhaustive finite-pattern falsification, rather than checking only selected periodic examples.

The one-off independent Python check used `itertools.product((0,1), repeat=2*N)` and a dictionary indexed by the exact window. It evaluated the predecessor sums directly, without using the proposed telescoping criterion or the author's proof. The final assertion compared the structural criterion with the independently evaluated adjacent-period identities. It completed successfully with output `Exhaustive patterns checked: 21732`. This was a review experiment, not a committed regression test; the mathematical proof supplies the universal result.

## Proof audit and edge cases

1. For arbitrary interval pairs, the stated boundary identity is correct: in C_r(y+q)-C_r(y), exactly f(y-a_r+q) enters and f(y-b_r) leaves. The argument tests each nonempty source cell separately, so it neither assumes every residue exists nor inadvertently uses cell totals as per-vertex values.
2. In the finite theorem, the negative-difference subtraction uses two transitions for the same two output heights and the same source residue. The second source interval adds just n in that residue. The union of extracted identities is exactly t∈[1-N,-q], which connects all congruent nonpositive points in the window. It does not silently omit an endpoint.
3. For positive differences d<q the choice r=q-d gives y=0; for d>=q the choice r=0 gives y=d-q. In both cases the indicated source residue exists because N>=q, both target heights lie in [0,N], and y-b_r lies in the nonpositive part of the window with the same residue as d. Thus the positive/negative gluing step is sound.
4. Base N=q has q independent equalities f(-r)=f(q-r), 0<=r<q. For q=1,N=1 this is precisely f(0)=f(1), not an assumption about negative jumps outside the observable range.
5. N<q is genuinely exceptional: every target residue cell is a singleton. For example q=3,N=2 leaves preservation vacuous, while period-3 agreement on [-1,2] would require f(-1)=f(2). The theorem correctly avoids that false conclusion.
6. The observable window is exact: at transition N, its extremes are differences 0-(N-1)=1-N and N-0=N. Values outside cannot be constrained by the hypothesis.
7. D empty and D=Z pass; any finite nonempty D eventually fails the structural condition. This conclusion is compatible with the empty model's trajectory and with extinct trajectories such as D={-1}.
8. The single-transition counterexample q=1, source {0,1}, target {0,1,2}, D={-1,1} has direct predecessor sums (1,1,1); its previous transition has output (0,1) and fails. This correctly shows why the collection of all growing transitions is essential.
9. The infinite result follows by exhausting all integers with the finite windows; it does not require a bounded jump set or a maximal/minimal allowed jump.
10. The affine shear statement preserves residue cells via a layer-dependent permutation and adds c to the jumps. It is correct as stated and does not justify an arbitrary-slope generalization.

An alternative independent necessity proof is available by induction on N. At N=q the q constraints above establish the base. Given periodicity on [2-N,N-1], compare y=0 and q in T_N for the source residue containing N-1; all old terms cancel, isolating the new low difference 1-N. Compare y=N-q and N in the source residue containing 0; the old terms cancel and isolate the new high difference N. This provides a separate way to check the finite rigidity argument.

## Scope of algebra review

The coordinator mentioned a separate algebra/incidence proposal but has not yet supplied it at the time of this review. No verdict on that proposal is implied here. In particular, the elementary preservation result alone does not prove a new incidence-algebra representation theorem or improved path-counting algorithm.
