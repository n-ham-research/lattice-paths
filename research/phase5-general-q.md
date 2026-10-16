# Phase 5 — general modulus: a compactness reduction, not a converse

16 October 2026. Independent internal analysis by `/root/seed5`. No novelty claim and no general-q theorem is asserted.

## Model and the precise open problem

Use the origin-start, vertex-constrained triangle: row n has heights 0,...,n, p_0(0)=1, and p_n(y)=sum_z p_(n-1)(z) f(y-z). The homogeneous kernel is an indicator f:Z→{0,1}, with f(0)=f(1)=1. A row is q-uniform when any two admitted heights congruent modulo q have equal counts. The observed window through N is W_N=[1-N,N].

The open question for fixed q≥4 is whether uniformity of every actual row forces q-periodicity of f on Z. A finite positive prefix is not a counterexample to this all-horizon assertion. Phase3's q=5 example survives through six and fails at seven.

## Bootstrap revisited

Suppose m≥q, f is q-periodic on W_m, and all rows through a later horizon N are q-uniform. Extend its residue values periodically to g on Z. Sliding a source-residue sum by q changes the two extreme terms by weights agreeing modulo q, so g preserves q-uniform rows. Through m the actual f and g rows agree. At the next layer, all interior targets use only known differences. The bottom and top each have an interior target in the same residue, so uniformity fixes their counts too. The coefficients of the two unknown extreme weights are the preceding top and bottom counts, respectively; these are positive because repeated zero and repeated one jumps are admitted. Both extremes therefore agree with g. Induct.

This is an exact uniqueness argument for two new coefficients after a periodic seed. It does not show that the compressed observations force the seed.

## A qualitative equivalence by finite branching

For a fixed q, the following statements are equivalent:

1. Every all-horizon q-uniform indicator trajectory with f(0)=f(1)=1 has a globally q-periodic kernel.
2. There exists a finite H≥q such that every kernel q-uniform through H is q-periodic on W_H (and hence the same conclusion holds at every larger horizon).

Proof: (2) implies (1) by the bootstrap. Conversely, suppose no such H exists. At each N≥q there is a binary assignment on W_N producing uniform rows through N but not periodic there. Its restriction to W_q cannot be periodic: if it were, the bootstrap would make W_N periodic. Consider the rooted tree of these compatible assignments, retaining those whose W_q restriction is nonperiodic. Each extension chooses only the two new binary extreme weights, so branching is at most four. There are nodes at arbitrarily large depths; taking successively a child with arbitrarily deep descendants gives an infinite branch. The nested windows exhaust Z, defining an indicator kernel with 0,1 present, all rows uniform, and a nonperiodic W_q restriction. This contradicts (1). Thus (1) implies (2).

This is only compactness/König's lemma, an established principle. It supplies neither H nor a decision algorithm for existence of H. It explains why a finite seed theorem is the correct target, but it is not progress toward proving that target for any new modulus. Counts in this tree grow and need not have a finite-state quotient; calling the tree a finite automaton would be unjustified.

## The initial-step assumptions

The unqualified assertion obtained by deleting 0,1∈D is false: D={2} has p_n≡0 for every n≥1, hence all rows q-uniform for every q, but D is not q-periodic for any q≥1. This is an extinction counterexample, not a nonextinct counterexample.

Having both first-layer endpoints positive is equivalent to 0,1∈D for indicator kernels. Thus if the intended replacement hypothesis requires every admitted endpoint to have a positive count at every layer, it already implies the original assumption. The condition also gives the two nonzero extreme pivots in the bootstrap without an extra hypothesis.

These observations do not decide whether the all-horizon theorem remains true after replacing 0,1∈D by nonextinction, eventual positivity, or another weaker reachability condition. No such relaxation is promoted. The equal positive initial weights used in the real/rational parity theorem are likewise retained; the proof normalizes one common weight and does not address unequal ones.

## Recommendation

Keep the general-q seed question explicit for external discussion. The finite-branching reformulation and exact role of the pivots may help frame it, but no compelling new uniform algebraic restriction emerged in this limited analysis. Further modulus enumeration is not a substitute for such an argument. No new original 2019 claim is settled.
