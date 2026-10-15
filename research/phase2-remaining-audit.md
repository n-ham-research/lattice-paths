# Second-pass audit of the remaining families

16 October 2026. Internal research by `/root/audit_phase2`; source extraction is unchanged. All counts here use finite ordered words, one empty word, sets rather than colored multisets, every visited vertex constrained when a boundary is present. No novelty claim. This pass prioritizes exact general formulas and falsification; unidentified OEIS names and array ordering remain unresolved even when a model has an exact counting formula.

## Unrestricted compositions: §§2–5,12–16

For S_q={(1,1-qk):k>=0}, q>=1, let N be horizontal coordinate. For N>=1,

P_q(N,y)=binomial(N+K-1,K), K=(N-y)/q,

if K is a nonnegative integer; otherwise zero. P_q(0,y)=[y=0]. Proof: the N step parameters form a weak composition of K into N parts. This is a finite count despite an infinite step set. Reversing vertical signs gives the analogous formula with K=(N+y)/q.

| Claim IDs | Disposition and exact extraction |
|---|---|
| H2019-02-01 | Proved interpretation: positive compositions give P(0,0)=1, P(N,0)=2^(N-1) for N>=1; excludes zero step. |
| H2019-03-01 | Proved recurrence: c(0)=1, c(N)=sum_{a=1..min(k,N)}c(N-a), c(N<0)=0. Source OEIS triangle indexing not checked. |
| H2019-04-01 | Proved interpretation at endpoint (mn,0): mn upsteps and n vertical downsteps, hence binomial((m+1)n,n). No boundary. |
| H2019-05-01 | Axis count finite sum: P(0,0)=1 and P(N,0)=sum_{k=1..floor(N/2)}binomial(N,k)binomial(N-k-1,k-1). This yields 1,0,2,3,10,25,... . The supplementary contour proof in phase2-additional-proofs.md establishes the supplied OGF, independently reviewed in phase2-ledger.md. |
| H2019-12-01 | q=1, endpoint (n+1,0) gives binomial(2n+1,n+1). Empty path exceptional; source had no extraction. |
| H2019-13-01..02 | q=2, endpoint (2n,0) gives binomial(3n-1,n), n>=1; empty path one. Thus the source's comparison question has answer **it is that binomial**. Composition parts are nonnegative, not strictly positive. |
| H2019-14-01 | **False for the unrestricted odd-up model as written.** P(2n,0)=binomial(3n-1,n), P(2n+1,1)=binomial(3n+1,n+1); at (2,0) count2, not first ternary Catalan value1. Imposing nonnegativity changes the model and must be recorded explicitly. |
| H2019-14-02..06 | All endpoints of odd-up are given by the sign-reversed q=2 formula above; supplied secondary OEIS identities not checked. |
| H2019-14-07 | Boundary vertical-two model delegated to the tree-family audit; not counted as resolved here. |
| H2019-15-01 | q=3 at (3n,0) gives binomial(4n-1,n). |
| H2019-16-01 | q=4 at (4n,0) gives binomial(5n-1,n). |

Primary-source checks: [A165817](https://oeis.org/A165817) explicitly gives binomial(3n-1,n), weak balls-in-boxes meaning, author Thomas Wieder 29 September 2009, initial zero-index term added 4 April 2012. [A001700](https://oeis.org/A001700) confirms binomial(2n+1,n+1) and its shifted weak-composition meaning. These formulas are existing mathematics.

## Complete residue layers: §§28–32

For multiples-of-q steps (1,qk), all supported points in a layer have the same predecessors. In the triangle, layer n has d_n=floor(n/q)+1 supported heights. Thus endpoint E_q(n)=product_{j=0}^{n-1}d_j and total E_q(n+1). For n=qm+s, 0<=s<q,

E_q(n)=(m!)^q (m+1)^s = product_{i=0}^{q-1}floor((n+i)/q)!.

These are exactly permutations whose residue sequence is nondecreasing: residue blocks have prescribed sizes, and values can be independently permuted inside each block. The one-column array row condition is vacuous. This explains the source permutation-array identification, including its indexing.

- H2019-29-01,30-01,31-01,32-01: proved only on supported rows y divisible by q and n>=y; literal other rows are zero. Endpoints equal E_q(n), not an unshifted full sequence starting before row entry.
- H2019-29-02,30-02,31-02,32-02: total equals E_q(n+1).
- H2019-28-01: even-wedge layer size d_n=2 floor(n/2)+1; endpoint E(n)=product_{j=0}^{n-1}d_j. E(2m)=((2m-1)!!)^2, E(2m+1)=(2m+1)((2m-1)!!)^2. Odd rows are zero, so the all-row claim is false literally.
- H2019-28-02: total equals E(n+1). This is A000246(n+1), not A000246(n).

[A000246](https://oeis.org/A000246/internal) confirms odd-order permutation counts, recurrence and double-factorial formula attributed to Vladimir Shevelev, 1 December 2013. [A264557](https://oeis.org/A264557/internal) (q=3, Hardin 17 November 2015) has balanced factorial formula Heinz 9 July 2016. [A264635](https://oeis.org/A264635) (q=4, Hardin 19 November 2015) and [A264656](https://oeis.org/A264656) (q=5, Hardin 20 November 2015) have Heinz formulas 12 July 2016. These entries start at n=1; the extension E_q(0)=1 is our empty-path convention. A264701 q=6 could not be fetched; its identification remains unverified although the formula is proved directly.

## Stars and bars: §33

For S={(a,1):a>=0}, P(x,y)=binomial(x+y-1,y-1) for y>=1,x>=0; at y=0 only origin. Thus H2019-33-01,03,05,07,09,11,13,15 hold with explicit offsets: row y=r gives degree r-1 simplex numbers starting at x=0; column x=r-1 gives the same family with sequence index y-1. For S={(a,1):a>=1}, P(x,y)=binomial(x-1,y-1), x>=y>=1. Its fixed row is a shifted simplex sequence, but fixed column x=r-1 vanishes for y>r-1. Therefore **H2019-33-02,04,06,08,10,12,14,16 are false as paired infinite-slice assertions**. Already x=2,y=3 gives0 rather than a continuing triangular family. Individual named OEIS pages not fetched.

## A common exact coefficient formula: §§34–39

Let B be a finite set of height increments. For steps (a,b), a>=1,b in B, define c_k(s)=[z^s](sum_{b in B}z^b)^k. With optional vertical upstep (0,1),

P(x,y)=sum_{k=1}^x binomial(x-1,k-1) sum_{s<=y} c_k(s) binomial(y-s+k,k), x>=1.

Without the vertical step replace the inner sum by c_k(y). At x=0 the counts are [y>=0] with vertical upstep, otherwise [y=0]. Proof: choose k positive horizontal increments composing x, choose height increments summing to s, then place v=y-s identical vertical ups in k+1 gaps. There are binomial(v+k,k) placements. All endpoint counts are finite since k<=x and s is bounded; no boundary is imposed.

Apply B={-1,1} to §34 and §38; B={-1,0,1} to §36 and §37; B={0,1} to §39. This determines every fixed slice exactly, but **does not by itself validate every supplied OEIS identifier or unspecified array order**.

| Claim IDs | Concrete status |
|---|---|
| H2019-34-01..08 | Exact formula above; OEIS matches pending. Heading a>=0 would create opposite vertical cycles and infinite counts, so body a>0 required. |
| H2019-35-01 | Infinite symmetric model upper/lower diagonal P(x,±(x-2))=2(x-1)^2+1 for x>=1; coefficient derivation below. Empty-origin sample at x=0 is0 because target height ±2. |
| H2019-35-02 | **False as paired assertion.** Finite-as-written upper y=x-2 gives1,3,9,19,... at x=1..4; lower y=-x+2 gives1,3,17,82,... . Counterexample (3,-1):17 versus quadratic9. |
| H2019-35-03 | Numerical corrected-coordinate candidate: P(x,x-3)=(4(x-1)^3-6(x-1)^2+11(x-1)-3)/3 for x>=2. The printed polynomial evaluated at x-1, rather than actual horizontal coordinate x, matches. Through x=9 checked; proof not claimed here. |
| H2019-36-01..03 | Exact coefficient formula; supplied OEIS identities pending. |
| H2019-37-01,02,04 | Exact coefficient formula; supplied OEIS identities pending. |
| H2019-37-03 | **No same-coordinate reflection symmetry:** P(1,1)=6 versus P(1,-1)=1. Positive row matches A052392 initial data with x=0..6; negative row matches with x shifted by1 (not literal equality). Full identity with OEIS still needs recurrence/coefficient proof. |
| H2019-38-01 | Axis OGF (1-t)/sqrt(1-6t+t²), hence central Delannoy first differences, with a(0)=1. See derivation below. |
| H2019-38-02 | **No same-coordinate reflection symmetry:** P(1,1)=4 versus P(1,-1)=1. A104550 starts at OEIS index1; positive row P(x,1) matches a(x+1), negative P(x,-1) matches a(x) for x>=1, through x=12 by the exact formula; identity proof pending. |
| H2019-38-03 | Exact formula at x=2; named sequence check pending. |
| H2019-39-01..12 | Exact coefficient formula; named OEIS identities pending, including diagonal. Antidiagonal total OGF is (1-t)/(1-3t), since step GF after x=y=t is t+t/(1-t)+t²/(1-t). Thus totals1,2,6,18,54,162,... are determined. |

§35 infinite quadratic proof: use t marking x and d marking deficit x-y. Step GF is K=t(1+d²)/(1-td)+td. In 1/(1-K), coefficient d² is t(1+3t²)/(1-t)^3 (direct expansion of denominator 1-t-2td+(t²-t)d² and numerator1-td). Coefficient t^x is2(x-1)^2+1, x>=1. Terms of degree deficit>2 cannot change this, so the finite model's *upper* diagonal agrees, but its reflected lower diagonal does not.

§38 axis proof by a coordinate change and horizontal-run expansion: let u mark the number of downsteps and t mark horizontal progress. Equivalently sum over balanced up/down total after inserting vertical ups; the constant-term generating function is CT_z (1-t)/(1-t-z+tz-tz^-1-tz). Its kernel quadratic yields (1-t)/sqrt(1-6t+t²), with branch equal to1 at t=0. This agrees with [A110170](https://oeis.org/A110170), Emeric Deutsch 14 July 2005; entry gives exactly that OGF. [A052392](https://oeis.org/A052392) and [A104550](https://oeis.org/A104550) primary pages confirm their starting terms and offsets. The constant-term extraction is interpreted in t with endpoint-finite Laurent coefficients; a naive expansion in z is not interchangeable.

## §40 explicitly still open in this pass

H2019-40-01..06: no audited OEIS identification here. Any future engine must count (1,1) once, and distinguish unrestricted from below-diagonal visited-vertex conventions. The previously extracted slash alternatives are not resolved by short initial agreement.

## Reproducible exact evidence and limitations

`experiments/remaining_families.py` implements the sparse composition formula, residue products, arbitrary-positive-x coefficient formula, and finite-step DP. `experiments/tests/test_remaining_families.py` has five tests: weak-composition formula versus explicit parameter words (q1..4,N1..5,deficit0..3); residue products versus full endpoint DP (q1..6,triangle/wedge,n0..12) and balanced factorial products; arbitrary-progress formulas versus direct word recursion (three B sets, with/without vertical step,x0..4,y-2..3); retained counterexamples; Delannoy differences at all n0..12. Full suite passed, 13 methods at time of execution (other agents may add tests). No external code copied. Counts are exact integers. Finite tests are evidence; proofs above carry the universal claims. This is not external peer review.
