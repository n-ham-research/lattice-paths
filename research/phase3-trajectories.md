# Phase 3: actual trajectories, finite-support obstruction, and endpoint inversion

16 October 2026. Derived by internal AI agent `/root/trajectory3`; proofs are research candidates pending the separately recorded independent reviews. No novelty claim. This note answers the actual-trajectory and inverse-data parts of Priority 1, with a precise obstruction rather than an unproved infinite-support converse.

## Model and observation data

At integer layer n the permitted vertices are I_n={0,...,n}. Paths start at (0,0), use distinct steps (1,d) with d in D⊆Z, and obey the vertex constraint at every layer. The empty path has count 1. Endpoints are labelled; p_n(y) denotes the number of words ending at (n,y). We also permit rational weights f(d), multiplying weights along words; all sums for finite n are finite even for infinite support. The recurrence is

    p_n(y) = sum_{z=0}^{n-1} f(y-z) p_{n-1}(z).

A row is q-residue-uniform if p_n(y)=p_n(y+q) whenever both positions occur. This concerns only the actual trajectory from the origin. It does not test arbitrary initial inputs. We say the trajectory is nonextinct if every row is nonzero. Once a row vanishes, every later row vanishes.

## T1. Finite-support obstruction, without positivity of individual endpoint counts

**Theorem.** Suppose f:Z→R_{≥0} has finite nonempty support and q≥1 is fixed. If the actual endpoint rows are q-residue-uniform for all sufficiently large n, then the trajectory becomes identically zero. In particular, no finite nonempty step set D admits a nonextinct eventually residue-uniform counting trajectory in the growing triangle.

This is substantially stronger than observing that full residue-space preservation excludes finite nonempty D: here only one trajectory is assumed uniform, and neither reachability of all residues nor positivity at every endpoint is needed.

**Proof.** Write m=min supp(f), M=max supp(f), K=Σ_d f(d)>0. Set L=max(0,M), R=max(0,1−m). For sufficiently large n, the interval [L,n−R] has at least q integers. Every target y in that interval has y−d∈[0,n−1] for every d in supp(f). Let c_n(s) be the common count in residue s, once all q residue cells exist. Choose an interior y of each residue s. The recurrence gives

    c_n(s) = sum_d f(d)c_{n-1}(s-d).

Summing over all q residues, C_n:=Σ_s c_n(s) satisfies C_n=K C_{n-1}. The ordinary total P_n:=Σ_y p_n(y), by contrast, satisfies P_n≤K P_{n-1}, since any path has total extension weight at most K. If a sufficiently late uniform row B is nonzero, C_B>0 and for all n≥B,

    floor((n+1)/q) C_n ≤ P_n ≤ K^{n-B}P_B,
    C_n=K^{n-B}C_B.

Hence floor((n+1)/q)≤P_B/C_B, impossible as n→∞. Therefore such a row B is zero. ∎

**What the argument uses.** Finite support supplies interior representatives of every residue where the convolution is untruncated. Nonnegative weights supply P_n≤K P_{n-1} and comparisons between totals and residue values. Indicator weights are unnecessary. The argument does not extend as stated to infinite support or signed weights.

### T1f. Explicit finite observation certificate

Let

    B ≥ max(q−1, L+R+q−2),
    H = q(ceil((B+1)/q)+1)−1.

If every row B,...,H is residue-uniform, then row B is zero. In particular H≤B+2q−1: at most 2q successive sufficiently late uniform rows force extinction under the finite-support hypothesis.

**Proof.** Each n≥B+1 satisfies n−R−L+1≥q, so every transition has q consecutive interior targets. If C_B>0, the previous proof applied only to this finite block gives

    floor((H+1)/q) ≤ P_B/C_B ≤ ceil((B+1)/q).

But the left side is ceil((B+1)/q)+1. Contradiction. The upper bound on H follows by writing B+1=aq+r, 0≤r<q. ∎

This is an explicit obstruction, not a claim that the horizon is optimal. It answers the question about uniformity over arbitrarily long intervals: for a fixed finite support, arbitrarily long nonzero uniform intervals cannot occur, even if uniformity is not assumed between those intervals. A single nonzero late uniform block of the stated length already contradicts finite support.

## T2. Full labelled endpoint data identifies the observable jump weights

**Theorem.** Let N≥1. Suppose rows p_0,...,p_N arise from a time-independent rational jump weight f and

    p_{n-1}(0) != 0 and p_{n-1}(n−1) != 0,  2≤n≤N.

Then those data uniquely determine f on W_N={1−N,...,N}. Values outside W_N cannot be observed in these transitions. In the unweighted setting, the natural support condition 0,1∈D guarantees the required nonzero boundary pivots for every N: the all-zero and all-one increment words remain valid.

**Proof and reconstruction.** First f(0)=p_1(0), f(1)=p_1(1). Inductively suppose f is known on W_{n-1}={2−n,...,n−1}. The top endpoint equation has just one unknown:

    f(n) = [p_n(n) − Σ_{z=1}^{n-1} p_{n-1}(z) f(n−z)] / p_{n-1}(0).

The bottom endpoint equation similarly gives

    f(1−n) = [p_n(0) − Σ_{z=0}^{n-2} p_{n-1}(z) f(−z)] / p_{n-1}(n−1).

Every weight in the displayed sums belongs to W_{n-1}. The nonzero pivots determine the two new extreme differences. This recovers W_n and proves uniqueness by induction. No difference outside W_N occurs in any transition through N, so changes there leave all observed rows unchanged. ∎

The theorem uses full endpoint rows: although the new equations are at the boundaries, their known coefficients include the previous row's interior endpoint counts. It does not claim that two edge sequences alone identify f. Nonzero boundary pivots are a transparent sufficient condition, not a necessary identifiability criterion. Rationality is convenient for exact arithmetic; the proof works over any field with those pivots nonzero.

**Failure without suitable reachability.** D={0} and D=Z_{≤0} have the same full endpoint array for all n: p_n(0)=1 and p_n(y)=0 for y>0. Every negative jump is invisible because no positive height is reachable. Both trajectories are nonextinct. Thus nonextinction alone does not identify the step set even from all labelled endpoint data. This example is not residue-uniform at large n and therefore is not a counterexample to any proposed uniform-trajectory converse.

**Scalar consequence.** For q=1, if all actual rows are uniform and the trajectory is nonextinct, then D=Z. Indeed p_1(0)=p_1(1)≠0 forces 0,1∈D. Inductively assume f=1 on W_{n−1} and p_{n−1}=(n−1)! at every endpoint. For n≥2 the target y=1 uses only differences in W_{n−1}, so uniformity forces p_n(y)=n! everywhere. The two boundary equations then force f(n)=f(1−n)=1. This proves the claim by induction. The extinct alternative is unrestricted beyond the actual visible constraints. This scalar statement is elementary and should not be oversold as a new factorial theorem.

## Open infinite-support converse; finite evidence is kept separate

For q>1 the implications

    nonextinct + actual residue-uniform trajectory ⇒ periodic D

and the same implication with 0,1∈D remain **unproved here**. T1 eliminates all finite nonempty candidate counterexamples and T2 shows that full endpoint data can identify D under natural reachability, but identifiability by itself does not imply periodicity from a compressed uniformity property.

Exploratory branch-and-prune searches with 0,1∈D found the following: for q=1,2,3 at N=5,7,9 and q=4 at N=6,8,10, all surviving finite trajectories were periodic on W_N. For q=5,N=6 an exceptional nonperiodic indicator survives, showing that the all-input finite theorem cannot simply be transferred with the same short horizon. One explicit support on W_6={−5,...,6} is

    D∩W_6 = {−5,−3,0,1,4,6}.

Its rows through n=6 are residue-uniform modulo 5, but f(−4)=0≠1=f(1). Since 0,1∈D, every endpoint at every layer is positively reachable using only those two increments; consequently this finite-horizon obstruction survives the strongest elementary positivity assumptions. This is finite evidence only and is checked directly by the committed experiment. In these exploratory tests the exception does not survive through N=8. Searches are not used as a theorem. Eventual positivity alone has not been proved sufficient for an infinite-support converse.

## Targeted primary-literature comparison

Searches on 16 October 2026 included “inverse problem directed lattice paths recover step set endpoint counts”, “lattice walks inverse enumeration step set identifiability triangular boundary”, “inverse problems graph walk counts reconstruct adjacency matrix Krylov controllability”, and “inverse lattice walk step distribution endpoint probabilities identifiability absorbing boundaries”. These are limited searches, not evidence of originality.

- Fenjin Liu and Johannes Siemons, [Unlocking the walk matrix of a graph](https://arxiv.org/abs/1911.00062), v3, 6 July 2020. The abstract was directly inspected. It studies a fixed finite undirected graph, walk matrices from a vertex subset, spectral decomposition, and recovery of its adjacency matrix when the walk matrix has rank at least n−1. T2 instead recovers the diagonals of a time-independent Toeplitz kernel acting on expanding triangular layers, from labelled origin endpoint rows and two explicit nonzero pivots. This is a difference in hypotheses/data, not proof that T2 is new or deeper. The elementary triangular elimination should be positioned as a specialized inverse-enumeration observation.
- Emilia Blåsten, Hiroshi Isozaki, Matti Lassas and Jinpeng Lu, [Inverse Problems for Discrete Heat Equations and Random Walks for a Class of Graphs](https://doi.org/10.1137/21M1439936). The publisher abstract was directly inspected. It considers finite weighted graphs, source-to-solution data on a vertex subset, and recovery under a Two-Points Condition. These are substantial inverse-problem results with different observation data. No full-text comparison was performed and no assertion of non-overlap of all consequences is justified.

Neither inspected abstract addresses T1's finite-support obstruction for residue-uniform trajectories on an expanding triangle. A targeted specialist comparison with finite-range walks, killed convolution kernels, and quasi-stationary/uniform distributions remains necessary. The proof of T1 is short enough that it may be a familiar mass-growth observation; absence from these searches is not a novelty finding.

## Reproducible exact checks

`python3 experiments/trajectory_inverse.py` verifies:

1. Reconstruction on all 256 binary weight assignments to W_5 with f(0)=f(1)=1.
2. The explicit T1f implication for each of the 63 nonempty supports D⊆{−2,−1,0,1,2,3}, q=1,...,4: 252 cases, each checked through its exact B,H.
3. One signed rational-weight reconstruction on W_5.
4. One invisible-negative-jump data comparison through layer 8.
5. The displayed q=5,N=6 nonperiodic uniform finite trajectory.

These checks are corroboration of the proofs and counterexample, not infinite verification. There are no changes to the 150-claim audit dispositions in this note: these are new research statements rather than a resolution of an identified original claim.
