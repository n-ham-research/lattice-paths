# Phase 3: weighted boundary graphs and expanding cones

16 October 2026. Research derivation by `/root/geometry3`; no novelty claim. These statements concern preservation of the whole space of residue-constant functions, not a single trajectory. Internal review remains required.

## Model and exact weighted graph

Fix q≥1 and finite integer interval layers I_0,…,I_N. Paths use distinct steps (1,d); vertices satisfy the layer constraints; the start is (0,0) when 0∈I_0, the empty path has weight 1, and the weight of a word is the product of its jump weights w(d). We consider w:Z→R for a commutative ring R with identity. Finite layers make each endpoint sum finite, even when infinitely many jump weights are nonzero. Structural statements below apply independently of the chosen start. Arbitrary rational or integer signed weights are allowed.

For each transition, each nonempty source residue cell has endpoints a_r,b_r. For every y with y,y+q in its target interval, insert an undirected edge

    { y−a_r+q, y−b_r }.

Use as vertices the observable differences U=⋃_{n=1}^N(I_n−I_{n−1}); empty transitions contribute nothing. Both endpoints of every inserted edge belong to U: the upper endpoint uses target y+q and source a_r, and the lower uses target y and source b_r. Call this graph G_q.

**Exact graph theorem.** Every transfer preserves residue-constant functions iff w is constant on each connected component of G_q.

Indeed the coefficient of a source-cell indicator at target y is C_r(y)=Σ_{z∈cell r}w(y−z). Cancellation in the additive group of R gives

    C_r(y+q)−C_r(y)=w(y−a_r+q)−w(y−b_r).

Thus preservation is exactly equality on every edge, and edge equality is equivalent to component constancy. This proves the weighted result without positivity, division, or characteristic-zero assumptions. For an arbitrary semiring lacking cancellation the necessity argument need not hold.

Every edge joins congruent integers modulo q. Consequently structural regularity forces q-periodicity restricted to U, meaning w(u)=w(v) whenever u,v∈U are congruent, **iff each nonempty residue fiber of U is connected in G_q**. Necessity here means necessity uniformly over all weight functions: if a fiber is disconnected, assign weight 1 to one component and 0 to all others, over Z (or any nonzero ring). This is an exact constructive counterexample. For the zero ring the universal necessity qualification degenerates.

This is a graph reformulation of the phase-2 sliding-sum criterion, not an independent novelty claim. It does, however, give a complete parameterization of all finite-horizon admissible weights by one free ring value per graph component. In particular, over a field the dimension is exactly the number of components, including isolated observable differences.

## A proved geometric extension: all integer cones for uniformity

**Theorem.** Let a<b be integers and I_n=[an,bn]∩Z, n=0,…,N, N≥1. Put k=b−a. The transfers preserve constant functions (q=1) iff the jump weight w is constant throughout the exact observable window

    W_N=[a−k(N−1), a+kN]∩Z.

For infinitely many layers this is equivalent to w being constant on all of Z. The statement permits signed integer and rational weights. For indicator weights, the only infinite structurally uniform step sets are ∅ and Z.

**Proof.** Shear by y↦y−an. This sends layers to [0,kn], jumps d to d−a, and W_N to [−k(N−1),kN]. It suffices to prove the assertion for a=0.

At transition n, the source is [0,M] with M=k(n−1), and the target is [0,K] with K=kn. The graph has precisely the edges

    {t,t+M+1},  −M≤t≤K−1−M=k−1.

For n=1 these are the neighboring edges {t,t+1}, 0≤t≤k−1, so [0,k] is connected. Inductively assume the old window [−k(n−2),k(n−1)]=[−M+k,M] is connected. Its number of integers is 2M−k+1≥M+1 for n≥2. Thus it contains at least one representative of every residue modulo M+1. The new transition's edges connect every congruence class modulo M+1 within the new window [−M,K]: they are exactly all neighboring pairs of that residue class lying in this window. Every such class meets the old window; therefore adding the edges makes the new window connected. The graph theorem gives necessity; constant weights give sufficiency. The nested windows exhaust Z, proving the infinite statement. ∎

This includes genuine two-sided cones such as [−2n,3n], rather than only the width-one shear family established in phase 2. The finite window is sharp: jumps outside it never occur, and their weights remain unrestricted.

**One-transition obstruction persists at every width.** For k≥1, the transition [0,k]→[0,2k] preserves constant functions whenever w has period k+1 on [−k,2k]. Such weights need not be constant. For instance w(d)=1 exactly when d≡0 modulo k+1 gives constant predecessor sum 1 at every target. The initial transition {0}→[0,k] fails uniformity. Thus even a full-width cone transition does not alone imply the cone theorem.

## Unproved stronger candidate, deliberately excluded from theorem

For q>1, computations suggest that the cone theorem extends to q-periodicity on W_N once N≥ceil(q/k), with sharp vacuity before that horizon because every target residue cell is a singleton. At the first nonvacuous horizon m=ceil(q/k), all source residue cells are singletons; their graph edges directly give every neighboring q-pair throughout W_m. A uniform inductive proof for subsequent horizons has not yet been completed here. This candidate must not be promoted on the basis of graph computations. General rational slopes and nonlinearly moving boundaries also remain open in this note.

## Attribution and limits

The equitable-partition invariant-subspace criterion and the phase-2 cancellation identity are background/prior project results. The exact component reformulation and elementary integer-cone proof are independently derived here; a targeted primary-source search and internal reviews are still needed before any priority statement. No source-based novelty claim is made. This note does not classify factorial endpoint sequences or accidental uniformity along one initial path.

## Executed checks and search log

`python3 experiments/phase3_geometry.py` passes: 2,955 exact rational-weight comparisons of direct predecessor sums against component constancy, including empty intervals, signed weights −1/2 and 2/3, and q=1,2,3; plus 672 integer-cone connectivity checks with a=−3,…,3, k=1,…,8, N=1,…,12. These checks support rather than replace the proofs.

Targeted web queries on 16 October 2026 were `"Toeplitz" "constant row sums" "interval" periodic` and `"equitable partition" "Toeplitz"`. Results included the primary presentation [Orbits of a group acting on Γ form an equitable partition](https://www.mathnet.ru/PresentFiles/24428/presentation.pdf), whose search extract gives a symmetric Toeplitz determinant factorization through an equitable partition. Only that extract was inspected; it does not state the expanding-cone theorem. The other results concerned graph spectra and tridiagonal Toeplitz quotient matrices. This narrow search supplies no adequate novelty assurance; the elementary character of the proof remains a substantial publication-value limitation.

## Stronger proved geometry: arbitrarily widening funnels

The integer-cone theorem is a special case of the following more general result. Let integers 0=s_0≤s_1≤⋯≤s_N and layers I_n=[cn,cn+s_n] for a fixed integer c. Then all transfers preserve constant functions iff w is constant on

    [c−s_{N−1},c+s_N].

Widths may jump by arbitrarily large amounts. In particular no bounded-growth assumption is needed.

Proof: shear c to zero. At transition n put M=s_{n−1}, K=s_n. The new window is [−M,K], and the edges are every neighboring pair in each congruence class modulo M+1 within that window. For n=1, M=0 and these are ordinary adjacent edges, so the graph on [0,s_1] is connected. For n≥2 the old connected window [−s_{n−2},M] lies inside [−M,K] by monotonicity. It has s_{n−2}+M+1≥M+1 vertices and hence meets every residue modulo M+1. All new vertices are connected to it by the new edges. This proves connectedness inductively; constant weights suffice. ∎

If s_n is unbounded, these observable windows exhaust Z and the infinite classification again permits only constant w. If widths stay bounded, only their limiting finite window is forced. Nonmonotone widths require the general graph test; the proof uses nesting explicitly.
