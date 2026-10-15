# Phase 4 — identifiable observations, widening funnels, and scalar rigidity

16 October 2026. Research agent `/root/inverse4`. Independently derived arguments, not a novelty claim; separate internal review is required before promotion. Nicholas Ham remains sole human author. This note changes no original-inventory disposition.

## Model

Paths start at layer zero at height zero, the empty path has weight one, steps are `(1,d)` with time-independent weight `f(d)`, and every integer-layer vertex must belong to its permitted finite layer `I_n`. Weight means the product along a word; endpoint weight is the sum over valid words. No segment constraint is imposed. A step set has indicator weights, not multiplicities. All finite-horizon sums are finite even for infinite support. Labelled means the endpoint's height is known. Field statements allow signed weights and nonzero characteristic unless explicitly restricted; ordered-kernel statements use nonnegative real weights.

## I1. Exact observation fibers: a useful criterion, not new linear algebra

Let all labelled endpoint rows `p_0,...,p_N` be specified and known to arise from some kernel. Put `U=union_(1<=n<=N)(I_n-I_(n-1))`. Form the matrix whose rows are indexed by `(n,y)`, columns by `d in U`, and entries are

`A(p)[(n,y),d] = p_(n-1)(y-d)` if `y-d in I_(n-1)`, and zero otherwise.

Let `b[(n,y)]=p_n(y)`. Over any field, the complete fiber of kernels on `U` producing these same rows is exactly

`{g: A(p)g=b} = f + ker A(p)`.

**Proof.** Necessity is the endpoint recurrence. Conversely a solution `g` produces the prescribed row zero and, inductively, if its preceding row is the prescribed one then its next row is `A(p)g=b`. Thus all rows agree. Values outside `U` are free. This induction is essential: the observation map itself is nonlinear in its unknown kernel, but its *full-data fibers* are affine. ∎

Consequently a linear statistic `ell(f)` is identified by these data among unrestricted field-valued kernels exactly when `ell` annihilates `ker A(p)`, equivalently when its coefficient vector belongs to the row space of `A(p)`. In particular a coordinate `f(d)` is identified exactly when the unit vector at `d` belongs to that row space. All visible coordinates are identified exactly when `A(p)` has full column rank. For indicator or nonnegative admissible kernels the exact fiber is the displayed affine space intersected with `{0,1}^U` or `R_(>=0)^U`; rank is sufficient, but no longer necessary, for uniqueness within those restricted classes.

This gives a precise periodicity diagnostic. Let `B_q f=0` express equality of coordinates in the same residue class on `U`. Every field-valued compatible kernel is periodic on `U` iff a compatible periodic kernel `f_*` exists and `ker A(p) subset ker B_q`. This is the standard affine-fiber criterion, not an independent substantial theorem. It distinguishes whether observed regularity identifies periodicity from whether some periodic model can fit it.

### Partial or aggregated observations require care

If every predecessor row appearing in a selected collection of transition measurements is independently known, retain just those rows of `A(p)` (or their specified linear combinations). The same row-space test identifies exactly the linear statistics implied by those measurements, when predecessor arrays are treated as fixed. This is not the same as a genuinely partial single-trajectory observation problem: unobserved intermediate counts are then unknown functions of `g`, and extra consistency equations cannot be discarded.

For example in the triangle, if only the endpoint at `(2,0)` is observed, its count is `f(0)^2+f(1)f(-1)`. Its fiber is generally quadratic, not affine. Thus we do not claim that deleting rows from a full-trajectory matrix solves arbitrary sparse, row-total, residue-sum or diagonal observation problems. Their exact equivalence relation is equality of the corresponding path-sum polynomials, with any admissibility restrictions imposed. This is precise but usually not a useful classification; further broad work on arbitrary compression is not justified here.

## I2. Corner reconstruction survives arbitrary widening funnels

Let `I_n=[cn,cn+s_n]` with integer `c`, `0=s_0<=s_1<=...<=s_N`. No bound on the successive increases is required. Write `h(d)=f(c+d)` and `r_n(y)=p_n(cn+y)`, so

`r_n(y)=sum_(z=0)^s_(n-1) r_(n-1)(z) h(y-z)`.

**Theorem.** Complete labelled rows through `N>=1` determine `h` on exactly the geometrically observable interval

`[-s_(N-1), s_N]`

provided both preceding corner counts `r_(n-1)(0)` and `r_(n-1)(s_(n-1))` are nonzero for every `2<=n<=N`. The proof works over any field. Outside that interval no difference occurs, so no full labelled data through `N` can identify an unrestricted kernel there. The condition is sufficient, not necessary.

**Proof.** Row one gives `h(y)=r_1(y)` for `0<=y<=s_1`. Suppose all of `[-a,b]` is known, where `a=s_(n-2)` and `b=s_(n-1)`, and put `k=s_n`, `delta=b-a`. The new observable interval is `[-b,k]`. First recover the new negative block with targets

`y=delta-1,delta-2,...,0`

using

`h(y-b) = [r_n(y)-sum_(z=0)^(b-1) r_(n-1)(z)h(y-z)]/r_(n-1)(b)`.

At the first target the smallest other argument is `-a`, already known; subsequently the already recovered negative values fill the gap. The largest argument in these sums is at most `delta-1<=b`, so no new positive value enters. Then recover the new positive block with targets

`y=b+1,b+2,...,k`

using

`h(y) = [r_n(y)-sum_(z=1)^b r_(n-1)(z)h(y-z)]/r_(n-1)(0)`.

All smaller arguments in these sums are known. Empty blocks and `b=0` cause no problem. This proves the induction. The interval of all geometrically possible differences at transition `n` is `[-s_(n-1),s_n]`, nested by monotonicity, proving exact geometric visibility. ∎

This strengthens the triangle reconstruction without changing the essential elimination method. It also shows that a sudden widening does not by itself destroy identifiability: the newly available endpoints supply exactly the extra extreme equations. It does **not** say corner observations alone suffice, because the coefficients use the complete preceding rows. Positivity of all needed corner counts is an observation assumption; merely having a nonzero row is insufficient. For indicator kernels containing every relative jump in `[0,s_n-s_(n-1)]` at each stage, paths along the two boundaries give pivots, but this sufficient support requirement is not needed in the theorem.

## I3. A direct bridge between actual scalar rigidity and inverse enumeration

The Phase 3 widening-funnel theorem says that all layer transitions preserve constant inputs iff `h` is constant on `[-s_(N-1),s_N]`. That structural result combines with one-dimensional actual data to give the following converse with much less information than full endpoint labels.

**Corollary (nonnegative real kernels).** On a widening funnel as above, the following are equivalent:

1. Each actual row through `N` is constant and nonzero.
2. For some `alpha>0`, `h(d)=alpha` on the entire observable interval `[-s_(N-1),s_N]`.

In this case its common endpoint value is

`r_n(y)=alpha^n product_(j=0)^(n-1)(s_j+1)`.

**Proof.** If each preceding actual row is a nonzero scalar times the constant vector, a constant next row means precisely that this transition sends the constant vector to a constant vector. Thus every transfer preserves the one-dimensional constant subspace. Phase 3's complete funnel boundary proof then forces a common kernel value on the observable interval. Row one is nonzero and every visible value in it equals `alpha`, hence `alpha>0`. Conversely a constant kernel on the observable interval gives the displayed formula by immediate induction. ∎

This statement is not merely identifiability from a list of known counts: scalar uniformity itself identifies the *shape* of the kernel, and one row sum determines `alpha=P_1/(s_1+1)`. It therefore gives a precise compressed inverse theorem. Full rows are unnecessary once this strong regularity assumption is imposed. It extends the old triangle factorial observation to every monotone funnel, arbitrary jumps in width, and real nonnegative weights. For unbounded widths, the observable intervals exhaust `Z`; an infinite nonextinct scalar-uniform trajectory forces a globally constant positive kernel. For step sets this is `D=Z`, regardless of shear `c`. A constant-width-zero funnel only observes the single jump `c`, so global conclusions require unbounded widths.

The analogous assertion for `q>1` does **not** follow: a single nonzero vector in a `q`-dimensional residue subspace need not test its invariance. Phase 3's positive `q=5` uniform prefix remains an exact counterexample to transferring the structural finite horizon. This note does not settle the infinite-support `q>1` converse.

## I4. Unlabelled data have an unavoidable reflection ambiguity

In the triangle define `f^R(d)=f(1-d)`. Reflect each vertex `(n,y)` to `(n,n-y)`. Its increment becomes `1-d`, its vertices stay in the triangle, and this is an involution on valid words. Consequently

`p_n^(f^R)(y)=p_n^f(n-y)` for every `n,y`.

Thus all row multisets and row totals coincide at every horizon. Distinct step sets such as `{0,1,2}` and `{-1,0,1}` are indistinguishable from this information even though both contain `0,1` and every endpoint is positively reachable. No theorem asserting exact labelled-kernel recovery from row multisets or row totals is possible without addressing this symmetry. We do **not** assert reflection is the only ambiguity. Residue sums are permuted by `r -> n-r (mod q)`, so this is a statement about their unlabelled versions or row totals, not automatically equality of their fixed residue labels. Bottom and top diagonal sequences are similarly interchanged, not separately fixed.

## I5. Exact ordered-kernel equivalence and geometric visibility

Let `0<=f<=g` pointwise and let `T` be any collection of finitely many labelled target endpoints; arbitrary finite layers are allowed. For an infinite target collection the same assertion holds target by target. Define a `g`-positive valid word to be one using only jumps with `g(d)>0`.

**Proposition.** The observations at every endpoint in `T` agree for `f` and `g` iff every `g`-positive valid word ending in `T` uses only jumps `d` for which `f(d)=g(d)`.

**Proof.** For each valid word, its `f`-weight is at most its `g`-weight. Equality of the sums of these nonnegative differences is equivalent to equality for every word. A word with positive `g`-weight has equal products iff all its factors agree, since each factor ratio lies in `[0,1]`. A zero-`g` word contributes zero to both sums. ∎

For step sets `D subset E` this says exactly that they have identical observations iff every observed `E`-path uses only jumps of `D`. It precisely describes nonidentifiability among ordered models and turns geometry into a path-language visibility test. It does not classify incomparable kernels, where compensating contributions can occur. Geometry can expose genuinely invisible jumps: `{0}` and `{0,-1}` have identical full labelled trajectories on `[0,n]`, but differ already at layer one on `[-n,0]`. The initial vertex and the vertex convention are unchanged; only the allowed region changes.

## Literature comparison and scope

Inspected primary source on 16 October 2026: Liu–Siemons, *Unlocking the Walk Matrix of a Graph*, [arXiv:1911.00062v3](https://arxiv.org/html/1911.00062v3), Theorems 1.2 and 6.1 and the latter's proof. Their finite undirected simple graphs have fixed vertex sets; full walk-matrix rank at least `n-1` recovers adjacency. Their walk-equivalence characterization compares adjacency restricted to the walk-generated space. This is relevant established inverse-walk theory. I1 is elementary linear algebra for an expanding Toeplitz model, not a competing general inverse-graph theorem. I2 is an explicit corner-elimination specialization; I3 combines the previously proved funnel geometry with actual scalar observations. No inspected theorem is claimed to certify their novelty. The geometric and data hypotheses differ, but a specialist may recognize these as familiar consequences. This targeted inspection adds a precise equivalence comparison rather than repeating a broad search. No further source theorem was needed for the proofs here.

## Exact checks and limitations

`python3 experiments/phase4_inverse.py` checks all 70 nondecreasing four-layer width tails with values `0,...,4`, hence includes plateaus and width jumps; source `s_0=0` is fixed. In each case it reconstructs positive rational weights `(|d|+2)/(|d|+3)` on the exact observable interval, and independently verifies the constant-kernel formula with `alpha=2/3`. It checks all 256 binary assignments on triangle `W_4=[-3,4]` against the reflection identity through layer four, and one exact quadratic partial-observation example. These are finite exact-arithmetic checks, not proofs. The conceptual proofs above are the arguments. The script is distinct from Phase 3's retained tests and does not claim arbitrary partial-observation classification or progress settling `q>1` at infinite horizon.

Two additional unit tests in `experiments/tests/test_phase4_inverse.py` independently enumerate every weighted jump word through four layers for widths `(0,0,2,2,4)`, compare endpoint sums and reconstruct the exact kernel, and reject malformed rows, zero pivots and a deliberately inconsistent interior observation. Both pass.
