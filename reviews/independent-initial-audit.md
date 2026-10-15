# Independent initial proof audit: Ham §§24–27

Reviewer: `/root/proof_review`, Codex agent (model version not exposed), 2026-10-16 Australia/Melbourne. Role: independently derive every inference and identify indexing and support failures. This is internal AI review, not external peer review. No novelty claim is certified here.

Source: `.local/references/ham-2019.txt`, numbered §§24–27, read directly. The mathematical arguments below were derived independently of a manuscript. A coordinator separately reported a prior exact-model proof in OEIS A005165 attributed to Danny Rorabaugh (2015); that attribution needs primary-source verification in the literature record.

## Conventions and verified mechanisms

Every step increases x by one. Count all finite vertex sequences from (0,0), retaining only vertices in the stated closed region. A region bounded by the straight lines in these sections is convex, so the vertex condition also ensures each entire segment remains inside. The empty path contributes one. Write P_n(k) for endpoint counts and T_n for their sum. Undefined endpoint counts are zero. These conventions must precede every identity.

For complete consecutive layers V_n of sizes m_n, with V_0 a singleton, every vertex of V_n has product(m_j, j=0,...,n-1) paths. The total is the same product through j=n. More generally, constant indegree d_n at every vertex of V_n implies uniform endpoint count product(d_i, i=1,...,n), by induction from the singleton initial layer. Zero factors and unreachable layers are permitted. Finiteness of layers, or finite indegrees and well-defined sums, is necessary. This is an elementary graph fact, not evidence of novelty.

For nested finite height sets H_0⊆H_1⊆... with H_0={0}, and all transitions except equal heights, let m_n=|H_n|. Every old height has m_n−1 outgoing edges. Consequently

    T_n=(m_n−1)T_{n−1},
    P_n(k)=T_{n−1}−P_{n−1}(k).

The second equation uses the zero convention for newly admitted heights. It does not imply uniformity of endpoints. It supplies a broad total-count theorem and an alternating endpoint formula. For k first admitted at time b≥1,

    P_n(k)=sum_{r=b}^n (−1)^(n−r) T_{r−1}  (n≥b).

For the initial height,

    P_n(0)=(−1)^n + sum_{r=1}^n (−1)^(n−r) T_{r−1}.

Proof is direct unrolling; equivalently paths to k and paths obtained by appending a permitted final jump to k partition all paths to the preceding layer, according to whether their current final height equals k. This gives a subtraction-free combinatorial partition underlying the alternating recurrence. It does not by itself constitute a new explicit sign-reversing involution.

## Section 24: three distinct models

1. All integer vertical increments in 0≤y≤x. H_n={0,...,n}; all consecutive layers are complete. Thus P_n(k)=n! for 0≤k≤n, and T_n=(n+1)!. The initial user-supplied endpoint induction is correct. Column sums are factorials with a shift, not n! at column n. A fixed nonnegative row k gives n! starting at n=k; negative rows contain no vertices. Every diagonal y=x−a with a≥0 gives n! once n≥a.

2. Odd vertical increments in −x≤y≤x. Reachability forces k≡n (mod 2). The reachable layer is {−n,−n+2,...,n}, size n+1, and consecutive reachable layers are complete. Therefore P_n(k)=n! for |k|≤n and k≡n (mod 2), and zero otherwise; T_n=(n+1)!. Fixed even/odd rows give even/odd factorial subsequences after the starting index imposed by |k|. The literal assertion that every diagonal y=x+a, a∈Z, gives factorials fails: a>0 is outside the region and odd a has the wrong parity. Correct diagonals have even a≤0. For example y=x−1 has no paths whatsoever.

3. All nonzero integer increments in 0≤y≤x. Here T_n=n! but endpoint counts are not uniform: P_2(0),P_2(1),P_2(2)=(1,0,1). The top endpoint satisfies P_n(n)=T_{n−1}=(n−1)! for n≥1. Thus the original endpoint (n+1,n+1) does indeed give n!. This third model must never be treated as complete layers.

## Section 25: alternating factorials

Use model 24.3. For n≥1,

    P_n(0)=A_{n−1},  A_m=sum_{j=1}^m (−1)^(m−j) j!, A_0=0.

This follows from P_1(0)=0 and P_n(0)=(n−1)!−P_{n−1}(0). Note exceptional P_0(0)=1. Also P_n(2)=P_n(0) for n≥2: both equal 1 at n=2 and thereafter obey the same recurrence. P_n(3)=P_n(1) for n≥3, since both equal 2 at n=3. Explicitly

    P_n(1)=sum_{j=0}^{n−1}(−1)^(n−1−j)j!  (n≥1).

The adjacent diagonal satisfies P_n(n−1)=(n−1)!−(n−2)! for n≥2, with P_1(0)=0. All OEIS candidates for these secondary rows must be disambiguated by direct definitions, rather than selecting one because of a few terms. The text's “x-axis ... (0,0) to (0,n+1)” is a coordinate error: every nonempty path has positive x, so the literal vertical endpoint is impossible. The intended horizontal endpoint is (n+1,0), which gives A_n. The column sum is n!, and the top endpoint (n+1,n+1) gives n!.

## Section 26: even double factorials

All nonzero integer increments in −x≤y≤x have m_n=2n+1. Hence

    T_n=(2n)!!=2^n n!,
    P_n(±n)=(2n−2)!!  (n≥1).

The original diagonal claim has an unavoidable shift: at (1,1), the endpoint count is 1 whereas 2!!=2. The top and bottom endpoints at column n+1 give (2n)!!. The endpoint at height n−1 is (2n−2)!!−(2n−4)!! for n≥2. Symmetry gives the other adjacent diagonal. Heights ±1 agree, with

    P_n(1)=sum_{r=1}^n (−1)^(n−r)(2r−2)!!  (n≥1).

The same general nested-set proof handles this entire section, including its nonuniform endpoint profile.

## Section 27: factorial products and missing parity conditions

Define Q_n=floor(n/2)! ceil(n/2)!. For odd increments in 0≤y≤x the reachable heights satisfy k≡n (mod 2); layer size is floor(n/2)+1. Consecutive reachable layers are complete, so

    P_n(k)=Q_n for 0≤k≤n and k≡n (mod 2), otherwise 0;
    T_n=Q_{n+1}.

Thus P_{2m}(2a)=(m!)² whenever 0≤a≤m, and P_{2m+1}(2a+1)=m!(m+1)! whenever 0≤a≤m. These identities explain the fixed-row assertions with all offsets explicit. Diagonal y=x−a works only for even a≥0: odd a produces zero at every column. For instance y=x−1 is a counterexample to the unrestricted original assertion. The column total is a one-position shift of the endpoint sequence, not the same indexed formula.

For even increments including zero, again in 0≤y≤x, reachable heights are precisely the even heights. Consecutive reachable layers are complete with the same sizes, so P_n(k)=Q_n for even k in the region and zero for odd k; T_n=Q_{n+1}. Consequently the original claim “y=a where a∈Z gives A010551” requires a≥0 even, with n≥a. Row y=1 is identically zero. The two models share totals and endpoint weights but have different support at odd n.

## Generalizations worth retaining

* Arbitrary finite regions sliced into complete residue layers give products of layer cardinalities. For a step set containing precisely the increments congruent to r modulo d, reachable heights at column n lie in nr modulo d; if all such increments are present then the allowed residue layers are complete. This explains parity without special-case intuition.
* Nested-set exclusion of equal heights gives product totals product(m_i−1), independently of the actual labels or shape of H_i. Thus both factorial and double-factorial totals are instances of an outdegree theorem. Constant outgoing degree controls totals even when incoming degrees fail to be constant.
* A partition into finitely many types with constant numbers of predecessors of each type gives a matrix recurrence for uniform counts within types. This is an elementary equitable-partition generalization; it needs literature checking and should not be called novel without stronger results.
* None of these statements suggests a faster factorial algorithm. Collapsing the first model is exactly repeated multiplication.

## Independent computational check

An inline Python 3 implementation compared direct enumeration of every height sequence through n=4 against a separately computed dynamic program, for all six models above. The dynamic program then checked every endpoint formula or total identity through n=8 (9 columns including the empty path). No test depended on repository experiment code. Every check passed. At column 4 the endpoint vectors were:

| Model | Endpoint counts in increasing height order |
|---|---|
| All integers, triangle | 24,24,24,24,24 |
| Odd increments, cone | 24,0,24,0,24,0,24,0,24 |
| Nonzero integers, triangle | 5,4,5,4,6 |
| Nonzero integers, cone | 48,40,42,41,42,41,42,40,48 |
| Odd increments, triangle | 4,0,4,0,4 |
| Even increments, triangle | 4,0,4,0,4 |

The verification confirms finite checks only; the proofs above establish the unlimited statements. Secondary OEIS identities have not been independently certified by this reviewer. Recommend accepting corrected elementary results as foundations, explicitly flagging support/index corrections, and reserving novelty for a later literature-reviewed strengthening.

## Follow-up audit of `research/foundation.md` (2026-10-16)

Read the full foundational note independently. All explicit factorial, double-factorial, parity-product, and row-recurrence inferences are correct under its stated conventions. The odd-cone diagonal bound n≥−a/2 correctly follows from −n≤n+a. The parity-product indegree floor((j+1)/2) is correct for both models. Empty-layer statements in the indegree theorem are valid: an empty final layer makes the assertion vacuous, and the first later nonempty layer has indegree zero, forcing every later reachable count to vanish. In the outdegree theorem, the transition from a nonempty layer to an empty layer forces outgoing degree zero; all subsequent totals remain zero. No nonempty-layer assumption needs adding.

Minor precision improvements: specify q∈Z_{>0} in the residue extension; qualify the block transfer recurrence by its required initial uniformity within blocks (automatic for the singleton V_0 in the present setup). The qZ formula is correct: write n=qm+s, then the q repeated factors 1,...,m and the s further copies of m+1 give (m!)^q(m+1)^s, including n=0. These are presentation improvements rather than mathematical failures.

### Explicit sign-reversing involution (resolved extension)

The note currently calls an involution on decorated signed words open. For nested sets and a height k first appearing at b≥1, it is elementary and explicit. Consider the disjoint signed union of all admissible paths of lengths j=b−1,...,n−1, with sign (−1)^(n−1−j). If a path ends at k, remove its final step. If it does not end at k and j<n−1, append the unique permitted step to k. Both operations preserve the permitted region and are inverses: at length b−1 the height k does not exist; after removal the preceding height differs from k because zero increments are forbidden. Each paired pair has opposite signs. The unpaired objects are positive paths of length n−1 not ending at k; appending k bijects them to paths of length n ending at k. This proves the displayed alternating sum without algebraic cancellation.

For k=0, extend the signed union to include one formal object of length −1 and sign (−1)^n. Pair it with the actual empty path. All other cases use the same append/remove rule. For n=0 the formal object alone represents the one empty target path. For n≥1 the survivors are the desired positive paths. This covers alternating factorials and arbitrary product totals. No novelty claim is made; compare with existing involution literature before promotion.

### Independently verified OEIS attribution

Fetched [OEIS A005165](https://oeis.org/A005165) directly using the web tool on 2026-10-16. Its comments attribute precisely this nonzero-increment triangle model, endpoint (n+1,0), to Nicholas Ham, 2015-08-23, and its induction proof to Danny Rorabaugh, 2015-11-30. The proof counts n choices for the n-th extension, obtains n! total paths through column n, and excludes paths ending at zero before the determined final step. This is the same recurrence used in the foundational note. Thus the known-proof attribution is independently confirmed, not merely a coordinator report. The source also supplies A_0=0 and A_n=n!−A_{n−1}. No long quotation is reproduced here.

### Engine inspection

Inspected `experiments/lattice_paths.py`. The unit-column DP and explicit path generator correctly encode the finite convex-region unit-horizontal models, and the general DAG routine checks self/backward edges before applying topological predecessor summation. Its allowance for a start occurring after other zero-initialized vertices does not create spurious paths. One low-priority API clarification: `heights(x)` should return distinct heights (and a fresh iterable when called again); a duplicate height would be deduplicated by the DP dictionary but enumerated twice by the explicit generator. Standard `range` model inputs meet this condition. No substantive correctness defect found for supplied models. Complexity claims were outside this review scope.
