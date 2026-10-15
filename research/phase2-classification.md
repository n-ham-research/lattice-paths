# Phase 2: exact residue classification for interval layers

16 October 2026. Derived by `/root/classification_phase2`; candidate results pending independent internal review. These results concern preservation of an entire space of block-constant inputs, not necessity for the counts obtained from one initial path. No novelty claim is made.

## Conventions and standard background

Fix an integer q≥1, a set D⊆Z and f=1_D. Steps are the distinct vectors (1,d), d∈D; thus length equals horizontal displacement and the zero vector is excluded even if 0∈D. Paths are words starting at (0,0), with the empty word counted once. At column n all vertices must lie in a prescribed finite integer interval I_n; boundary constraints are vertex constraints. Interpolated segments also lie in the convex hull of two successive interval layers, but no arbitrary segment constraint is assumed. An interval may be empty. Finiteness follows from the finite number of vertices at each of finitely many columns.

For source I and target J define (Tp)(y)=Σ_{z∈I} f(y−z)p(z). Let V_q(I) consist of functions constant on each nonempty residue cell I∩(r+qZ). We call T residue-regular if T(V_q(I))⊆V_q(J). This is equivalent to constancy, for each source residue r, of its predecessor count on each target residue. The equivalence follows by testing the indicator of each source cell; it is the standard equitable-partition invariant-subspace criterion, adapted to rectangular matrices and incoming edges. Coefficients of p are endpoint counts per vertex, not totals in a residue cell.

Prior background: Bailey, Cameron, Gavrilyuk and Goryainov, [Equitable partitions of Latin-square graphs](https://research-repository.st-andrews.ac.uk/bitstream/handle/10023/19043/bcgg_reviseSep_2.pdf), §2, explicitly gives equivalence between equitable partitions and invariance of the span of cell indicators. The available search extract of §2 was inspected; the PDF open timed out, so no claim of full-paper reading. Godsil–Royle, *Algebraic Graph Theory* (2001), §9.3 is the standard book reference identified there. Francis–Smith–Webb, [General Equitable Decompositions for Graphs with Symmetries](https://arxiv.org/abs/1809.07186), abstract inspected, concerns decomposition over graph automorphisms; no exact interval-rigidity theorem was found there. We do not attribute our elementary transfer identity as new.

## A. Complete criterion for any pair of interval layers

For each nonempty source residue cell write its smallest and largest elements as a_r and b_r; hence b_r=a_r+(m_r−1)q. Then T is residue-regular **if and only if**

    f(y−a_r+q) = f(y−b_r)                         (A)

for every nonempty source residue cell and every integer y such that y,y+q∈J. Empty source or target layers make the conditions vacuous.

Proof. The predecessor count from that source cell is C_r(y)=Σ_{k=0}^{m_r−1} f(y−a_r−kq). Subtraction cancels all interior summands:

    C_r(y+q)−C_r(y)=f(y−a_r+q)−f(y−b_r).

Thus (A) is exactly equality at neighboring points of each target residue cell. Such points form a finite arithmetic progression, so neighboring equality is equivalent to constancy throughout the cell. Testing source cell indicators gives necessity and linearity gives sufficiency. ∎

This is a condition directly on the allowed-jump indicator at two boundary differences. It covers arbitrary independently moving endpoints a_n,b_n by applying it to each pair I_{n−1},I_n. It gives a complete finite decision procedure and avoids calculating all predecessor sums. It does not assert that every sequence of moving intervals forces a periodic D: narrow target cells can make all conditions vacuous.

If regularity holds, the quotient entry M(s,r) is C_r(y) for any y∈J with residue s. For q-periodic f this simplifies to M(s,r)=m_r f(s−r). Empty target residues carry no endpoint value and may be assigned zero as a bookkeeping convention.

## B. Finite triangular rigidity

Let I_n={0,…,n}. For n≥1 let T_n map functions on I_{n−1} to functions on I_n. For N≥q the following are equivalent:

1. Every transition T_n, 1≤n≤N, is residue-regular modulo q.
2. On the exact observable difference window W_N={1−N,…,N}, f is constant on each residue class modulo q.

Outside W_N, D is unrestricted. For N<q, all the target residue cells are singletons, so every D passes and there is no periodicity conclusion.

Proof of 2⇒1. Every difference y−z occurring in these transitions lies in W_N. If y≡y' modulo q then f(y−z)=f(y'−z) for each z individually. Hence all predecessor counts agree.

Proof of 1⇒2, negative differences. For q≤n≤N−1 and 0≤y≤n−q, write the predecessor equality for T_n and for T_{n+1}, using the source cell r≡n modulo q and the same targets y,y+q. The second source cell adds exactly the new point n. Subtracting the equalities therefore gives

    f(y+q−n)=f(y−n).

Taking the union over n gives f(t+q)=f(t) for every 1−N≤t≤−q. (If N=q this range is empty.) Consequently f is constant on each residue class among the nonpositive integers in W_N. This set contains a representative of every residue since N≥q.

Proof of 1⇒2, positive differences. Fix 1≤d≤N. If d<q choose r=q−d; otherwise choose r=0. Put y=d+r−q. Then 0≤r≤q−1, y≥0, and y+q=d+r≤N, so (A) for T_N and source residue r gives

    f(d)=f(y−b_r).

Here 1−N≤y−b_r≤0. The lower bound follows from y≥0 and b_r≤N−1. For d<q, y=0; for d≥q, r=0 and b_0≥N−q, so y−b_0≤d−N≤0. Also y−b_r≡d modulo q. Thus every positive d agrees with a nonpositive representative of its residue, proving 2. ∎

In particular, at N=q there are precisely the q independent equality constraints f(q−r)=f(−r), 0≤r<q. Each further layer extends the window by one difference at either end. This is a finite obstruction theorem, not just an infinite-limit observation.

## C. Infinite triangular classification and consequences

All T_n preserve residue-block-constant functions modulo q **if and only if** D is a union of complete residue classes modulo q.

Proof. Sufficiency is immediate. For necessity, any two congruent integers lie in W_N for sufficiently large N≥q; Theorem B makes their indicators equal. ∎

Consequences:

- For q=1, the only structurally uniform triangular models are D=Z and D=∅.
- A finite nonempty D has no such fixed finite residue compression for every triangular layer. An infinite D with even one isolated deletion from a periodic set also eventually fails unless the deletion preserves q-periodicity.
- If D has least positive period h, the admissible q are precisely multiples of h. The set of integer periods is a subgroup of Z: closed under differences, and the least positive member divides every member by division with remainder. The exceptional constant indicators D=Z and D=∅ have every positive period and h=1.
- For D=qZ the original start is block-constant, so quotient recursion indeed governs actual counts. More generally the start on I_0 is always block-constant, and the matrix formula M_n(s,r)=m_{n−1,r}1_D(s−r) gives the exact q-dimensional endpoint recurrence for any union of cosets. Previously proved single-coset factorial products are special cases; no converse classifying all factorial sequences follows.
- The affine shear y'=y+cn maps the triangle to intervals [cn,(c+1)n] and D to D+c. It preserves residues up to an n-dependent relabeling, so the same classification holds there. We do not assert it for arbitrary slopes or two-sided cones.

## Counterexamples and limits

**One trajectory is weaker.** D=∅ or a step set whose paths die out produces zero endpoint values in later layers, concealing arbitrary transition irregularity. More concretely D={−1} admits no positive-length path in the triangle, so all actual endpoint counts are uniform in every residue cell for all n. Nevertheless D is not q-periodic for any q and fails structural residue-regularity. Thus Theorem C cannot be stated as a classification solely from the origin's observed counts.

**One transition is weaker.** q=1, I={0,1}, J={0,1,2}, and D={−1,1} give predecessor sums 1,1,1. The relevant indicator has period 2 on [−1,2], not period 1. The earlier transition I={0},J={0,1} is not regular, since f(0)=0≠1=f(1). All growing transitions, not one wide transition, are essential.

**Arbitrary moving layers can be vacuous.** If every target interval has at most q points, every target residue cell is a singleton; any D preserves block constancy. This excludes an unrestricted converse for moving endpoints.

**Extinction and missing cells.** An existing target residue cell can have zero predecessors; its endpoint count is zero. A residue cell absent from a source interval is not a free input variable. The exact criterion ignores absent source cells rather than assuming a positive common count.

## Targeted priority search and source correction

Queries on 16 October 2026: “Toeplitz matrix equitable partition residue classes interval periodic diagonals”; “equitable partition Toeplitz matrices periodic residue partition necessary sufficient”; “lattice walks residue classes uniform endpoint counts periodic step set triangle”. These located generic equitable-partition results and unrelated Toeplitz/triangular-walk work, but no inspected primary source stating Theorem B or C. This is limited negative search evidence and does **not** establish novelty. An exact theorem may be regarded as an elementary consequence of sliding sums; publication value needs further consequences and comparison by a specialist.

The specifically requested [East–Ham v1](https://arxiv.org/abs/1811.05735v1), 14 November 2018, was downloaded into ignored `.local/references/` and converted with `pdftotext -layout`. Targeted inspection covered Example 3.14, equations (3.15)–(3.16), surrounding Example 3.17, and the algorithm-section introduction; not a full reading of all 63 pages. **Example 3.14 already gives the complete-triangle endpoint a!, the nonzero-triangle top (a−1)!, total a!, the subtraction recurrence and the full alternating-factorial endpoint formula.** These must be credited as prior East–Ham results in addition to Rorabaugh's earlier 2015 OEIS proof for the axis sequence. The initial v3-only comparison therefore missed important prior work. Example 3.17 already proves the nonnegative-increment Catalan triangle recurrence. The v1 category remark likewise already proposes constrained walks as morphisms.

PDF SHA-256: `15e150fdb767663d517513d14ced7daa166069949d56248b1d01a39ab2b3cf90`.
Extracted-text SHA-256: `015feb93d5335828563397885527c7fe53a02dba4a6c42f485e87f5d404b9b5c`.

No downloaded source is intended for version control. The PDF contains overlapping duplicated text in portions of its text layer; formulas were reconstructed from repeated extracts, with numerical statements matching the already independently proved foundation. Visual inspection of the source formula would further strengthen that provenance check.

## Computational evidence

`python3 experiments/phase2_classification.py` completed successfully. It independently evaluates predecessor counts and compares them with the claimed finite classification for every binary indicator on W_N, N=1,…,6, and q=1,…,7: 38,220 indicator/modulus cases. It also compares direct sums with criterion (A) for all 512 indicators on [−4,4], every ordered pair among the 15 nonempty subintervals of [−2,2] plus an empty interval, and q=1,2,3: 393,216 cases. Differences just outside the directly observable window in (A) occur only when a target neighbor exists, which guarantees those boundary differences are themselves directly observable. These are exhaustive finite checks, not the proof or evidence about untested sizes.

## Final phase-2 disposition

Precise mathematical statements passed the independent internal reviews linked in reviews/review-log.md. Classical correspondence and source attribution are retained; no first-priority claim is made. The manuscript restricts its quotient recurrence to nonempty target cells, with absent cells zero only as bookkeeping. Complete proof notes and unresolved identifications remain distinct.
