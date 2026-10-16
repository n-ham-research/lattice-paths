# Focused pre-sharing proof audit

Nicholas Ham's lattice-path research — 16 October 2026. Disposition: the stated results are suitable for specialist mathematical scrutiny. This is not external peer review, novelty certification or publication approval. Nicholas Ham remains sole author. No correspondence was sent.

## Scope and outcome

Three initially separate internal AI analyses reconstructed the strongest arguments before consulting the other Phase5 reports: `/root/audit5` (inference, boundaries, inverse and composition), `/root/seed5` (counterexamples and small-modulus algebra), `/root/novelty5` (generalization/source comparison and independent proof scrutiny). The coordinator checked their conclusions against the final source. Shared context/model limitations remain; backend versions were not exposed. Earlier reports are retained in the repository, and the package includes these three focused reports under `audit-details/`.

No substantive proof defect was found. Editorial repairs explicitly add N≥1 to funnel statements, define the observation map and geometric difference set, and keep coefficient/observation assumptions visible. A slightly shorter conceptual boundary formulation is now explicit: **full-core equality forces every omitted nonnegative summand to vanish; repeating one extreme supported jump eventually forces such an omission.** The audit did not infer a stronger theorem from proof agreement.

## Assumptions and limitations, by manuscript statement

| Statement | Required assumptions and data | Conclusion and exact limits |
|---|---|---|
| Proposition3.1: boundary criterion | Finite integer source/target intervals; q≥1; commutative-ring weights; every residue-constant input | Exact adjacent comparison identity. Empty source cells impose no comparison. It is cancellation, not an actual-trajectory converse. |
| Theorem3.2 / Proposition3.3: triangular rigidity | Fixed homogeneous kernel; triangle; all-input preservation throughN≥q | q-periodic onW_N=[1−N,N]. All horizons exhaustZ. N<q is vacuous; an actual origin trajectory alone does not test every input. |
| Theorem3.4: widening-funnel structural converse | N≥1; integer shearc;0=s0≤...≤sN; all constant inputs; ring coefficients | Constant kernel on[c−s_(N−1),c+sN]. Arbitrary jumps/plateaus allowed. Nonmonotone geometry requires a separate test; global constancy needs unbounded widths. |
| Theorem4.1 / Proposition4.2: mass obstruction | Nonnegative real weights, finite nonempty support[m,M]; every block row containsq residues; every intervening full-predecessor core hasq consecutive vertices; strict multiplicity gap | First block row is zero. Diverging widths plus bounded endpoint motions give eventual extinction. Signed coefficients, absent cores and bounded widths do not inherit the conclusion from this proof. Products extend the argument to a common bounded range of layer-dependent kernels. |
| Theorem4.3: shorter certificate | Triangle; homogeneous nonnegative finite nonempty support;L=max(0,M),R=max(0,1−m),v=max(M,1−m);b≥max(q−1,L+R+q−2) | Uniform rowsb..b+ceil(q/v) force rowb zero. Valid for arbitrary prescribed nonnegative rowb. Restarted-data sharpness is not origin-start optimality. |
| Theorem5.1: triangular reconstruction | Compatible complete labelled rows throughN≥1; field; preceding two boundary pivots nonzero for2≤n≤N | Unique weights onW_N only. Full preceding rows supply coefficients. Indicator0,1 guarantees pivots in ordinary counting, not after arbitrary positive-characteristic reduction. |
| Theorem5.2: funnel reconstruction | N≥1;integerc;monotone widths; compatible complete labelled rows;both preceding corners nonzero | Unique weights on exactly[c−s_(N−1),c+sN]. Sudden widening/plateaus permitted. Pivots are sufficient, not necessary; corner sequences alone do not supply interior coefficients. |
| Proposition5.3: scalar compressed inverse | N≥1;monotone funnel;nonnegative real homogeneous kernel;every actual row constant and nonzero | Constant positive kernel on observable window;α^n∏(s_j+1) counts. Uses a one-dimensional input subspace and does not directly generalize toq>1. |
| Full-data affine fibers | Fixed known complete predecessor rows; unrestricted field-valued kernels | Compatible kernels are A(p)g=p; row-space criteria identify linear statistics. Indicator/nonnegative admissibility changes uniqueness tests. Hidden intermediate rows generally produce polynomial fibers. |
| Theorem6.1: parity compressed inverse | Triangle;homogeneous nonnegative weights;f0=f1=t>0;every row throughN is2-uniform | Constant visible kernel forN≥6 real,N≥5 rational,N≥3 indicator, each sharp. Finite-prefix examples are not persistent trajectories. Unequal initial weights,eventual-only uniformity,signed coefficients remain outside this theorem. |
| Proposition6.2: periodic bootstrap | Field;nonzero boundary pivots;actual uniformity throughN;periodic seedW_m withq≤m≤N | Extends periodicity toW_N. Does not produce a seed for arbitraryq. |
| Proposition6.3: modulus-three converse | Ordinary indicator counts;0,1∈D;every row throughN≥4 is3-uniform |3-periodic visible kernel,sharp horizon4;all horizons allow masks(1,1,x). Not a result for arbitrary real weights or eventual uniformity. |
| Reflection | Triangle;fixed homogeneous kernel;retain consistent weighted/support edges | Involutive covariant weighted walk-category isomorphism under(n,y)↦(n,n−y),d↦1−d. Totals/multisets preserved; endpoint labels,residue labels and bottom/top diagonals permuted. No classification of all ambiguities. |

Here “uniform throughN” means all rows from the origin throughN, not merely an observed late block. The finite-range theorem instead permits arbitrary later initial data. Every finite endpoint sum is finite even when the homogeneous support is infinite.

## Reconstructed proofs and adversarial checks

**Boundary certificate.** At transitionn=b+1 the stated threshold makes[L,n−R] contain at leastq vertices. Each residue therefore has a target receiving the full convolution. Since all source residue values are nonnegative, equality of a boundary target with the core value forces each missing predecessor term to be zero. A positive stepd cannot propagate a least residue representative beyondq−1; a nonpositive step increases the least distance from the moving top by1−d and cannot wrap. Repeating the extreme attainingv gives the certificate. This uses no reachability or positivity of every residue. For a single jump1−v from a large residue-zero prescribed row, the top gap remains belowq for exactlyceil(q/v) rows, then a missing representative appears. This verifies the advertised restarted sharpness.

**Small moduli.** The reviewers separately reconstructed the forced pairsx,c,a and the row-five factor, rather than inferring the real theorem from rational sampling. Exact arithmetic inQ(√2) independently reproduced the positive five-row exceptional prefix and the forced negative next value7−5√2. The rationalx=1/2 prefix and binary{0,1} examples prove the respective shorter horizons cannot work. Forq3, binary bounds forcea=b andA=B; row4 makesc=0 impossible. The bootstrap compares with the periodic continuation; actual agreement of known kernels supplies all preceding rows, despite the observation itself being compressed. Each boundary has an interior endpoint of its residue becausem≥q.

**Funnel recovery.** With known window[−a,b], a descending sequence of targetsb−a−1,...,0 isolates each new negative coefficient using the previous top pivot. Ascending targetsb+1,...,k then isolate each positive coefficient using the previous bottom pivot. All other arguments are already known at each step. This holds when a block is empty, the previous width iszero, widths plateau or the new width jumps. No unavailable interior information was assumed: complete rows are explicitly required.

**Reflection.** A reflected edge has jump1−d and retains its chronological position. Empty words and concatenation are preserved in the same order; the functor is covariant, not a path-order reversal. Weights agree factor by factor. The concrete sets{0,1,2} and{−1,0,1} have row-two counts(1,2,2) and(2,2,1), respectively, while both reach all triangular endpoints positively. Fixed-label residue sums generally do not agree.

**Missing assumptions.** Deleting0,1∈D without a replacement admitsD={2}: all positive rows are zero although the kernel is not periodic. This is an extinction counterexample, not evidence that the assumption is essential under nonextinction. First-row positivity at both endpoints is exactly0,1∈D in the indicator model. Necessity under weaker nonextinct reachability remains open. The real equal-weight hypothesis is retained.

## General modulus and novelty

The selective investigation did not produce a new arbitrary-q converse. Finite branching plus the proved bootstrap shows that, for fixedq in the indicator0,1 class, an all-horizon converse is equivalent to existence of some finite identifying seed horizon. The package's `general-q-note.md` proves this compactness consequence. It provides no bound, decision algorithm or finite-state model. No broad modulus sweep was launched.

The novelty assessment identifies invariant subspaces, affine fibers, elimination and graph relabelling as established mechanisms. Precise expanding-window certificates and compressed seed tests still require recognition. Earlier tree reconstruction already uses one starting root, so “one origin” alone is not a novelty distinction. No result is certified original by this audit.

## Computational and document verification

The focused package uses only Python3.10+ and its standard library. It includes exactly the domains listed in `verification/EXPECTED.txt`, including independent word comparisons and exactQ(√2) arithmetic. It is a subset of the repository's29-test/full historical suite, not a claim that all historical checks ship in this small package. Universal claims rest on the proofs, not finite agreement. Final build, rendered-page and clean-extraction outcomes are recorded in the Phase5 handover and package verification record.

Recommendation: ready for the author's decision to request specialist feedback using the four-page briefing. This is readiness for discussion, not a completed novelty audit or submission recommendation. The email remains a draft; no external action is authorized or performed by this package.
