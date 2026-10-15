# Explicit polygon-dissection interpretation for §18 / A067955

16 October 2026. Internal authoring agent `/root/bijections_phase2`. Complete elementary proof supplied; pending independent review. This composes two classical bijections and makes no novelty claim.

## Objects and conventions

Fix a convex polygon with its vertices in a specified cyclic order and a fixed base side, oriented to distinguish the order of the other boundary sides. A dissection is a set of distinct internal diagonals whose interiors are pairwise disjoint; shared endpoints are permitted. Reflections and rotations are not identified. The fixed base side is not an additional choice multiplied into the count: one uses the same prescribed side for every dissection of that polygon. Count **all distinct graph edges**, namely boundary sides plus diagonals, each once. Every bounded face must have an even number of sides, hence at least four.

Ordinary polygons have at least three vertices. The one-edge object used below is a separate formal degenerate object, not an ordinary polygon or a digon. It accounts for the empty path and the first sequence term only.

A plane tree means a finite rooted ordered tree. Its allowed outdegrees are zero (leaves) or odd integers >=3. Thus “all nodes have odd outdegree greater than two” in the OEIS comment must refer to nonleaf nodes; literal inclusion of leaves would leave no finite trees. Let L be its leaves, I its internal vertices, and N=L+I-1 its tree edges.

## Forward dual map from polygons to trees

Put one internal tree vertex in each bounded face. Put a leaf beyond each polygon boundary side other than the base side. Across every diagonal join the two incident face vertices. Across every nonbase boundary side join the incident face vertex to its corresponding leaf. Root at the face incident to the base side, and order children by their sides along the face boundary, starting immediately after its parent side. For the root, the parent side is the base side.

The graph on face vertices joined across diagonals is connected: a generic arc between interior points crosses a sequence of adjacent faces. It has I-1 edges, because each newly inserted noncrossing diagonal increases the number of faces by one. Thus it is a tree. Adding boundary leaves preserves the tree property. At each face exactly one side is its parent side, so a face with f sides becomes a vertex with f-1 children. Even face sizes therefore become odd positive outdegrees >=3. Every nonbase boundary side contributes exactly one leaf, so a polygon with B boundary sides has L=B-1 leaves. No root leaf is retained at the base side.

## Explicit inverse, with uniqueness proof

Given a nonleaf tree, list its leaves from left to right and let their number be L. Take the fixed convex (L+1)-gon with boundary vertices 0,1,...,L in that order and base side (0,L). More generally reconstruct a subtree with L' consecutive leaves on an interval of polygon vertices [a,a+L'].

If the subtree is a leaf, its interval has length one and it represents the boundary side (a,a+1); it creates no face. Otherwise let its ordered children have positive leaf counts L_1,...,L_d, with d>=2, and let s_0=a and s_j=a+L_1+...+L_j. Draw the root face with vertices

    s_0,s_1,...,s_d,

whose base is (s_0,s_d). Its d other sides are (s_(j-1),s_j). A child that is a leaf has L_j=1 and its side is an actual boundary side. An internal child has at least two leaves and its side is a diagonal bounding the subpolygon with consecutive vertices s_(j-1),...,s_j. Recursively reconstruct that child's subtree inside that subpolygon.

The intervals of siblings have disjoint interiors, while descendant intervals are nested. Their chords therefore do not cross. The constructed faces fill the original polygon: the root face and the child subpolygons partition it, and induction fills each child subpolygon. Every internal vertex of degree d creates exactly a (d+1)-gon. With odd d>=3, every face is even-sided and at least four-sided.

Reading the face incident to a base side recovers precisely these consecutive child intervals, in order. Thus the dual construction recovers the input tree. Conversely the leaf counts of the ordered components beyond a face's nonparent sides determine its successive root-face vertices, so the inverse reconstructs every given dissection. The maps are mutual inverses; neither equinumerosity nor equality of generating functions is being substituted for invertibility.

## Composition with the excursion map and exact shift

Take a nonempty nonnegative excursion starting at (0,0), using (1,1) and (1,-2k), k>=1, and ending at (N,0). Let u be its upsteps and r its downsteps, so N=u+r and r>=1. Reverse and negate its height increments, append -1, and interpret each resulting increment s as a preorder degree s+1, as proved in `phase2-bijections.md`. The resulting tree has L=u+1 leaves and I=r internal vertices, with degrees 2k+1.

Its polygon therefore has

    boundary sides B=L+1=u+2,
    diagonals I-1=r-1,
    total graph edges B+(I-1)=u+r+1=N+1.

Each original downstep -2k corresponds to one (2k+2)-sided face. In particular every face is even, and the number of downsteps is the number of faces. The original excursion has height balance u=sum 2k, so B is even; this agrees with the polygon-side parity forced by an all-even dissection.

Conversely, take an ordinary even-faced dissection with e total graph edges. Its dual tree has e vertices and e-1 edges. The inverse preorder construction gives exactly a length e-1 excursion over +1 and negative even increments. Thus, if a(e) denotes the indexed A067955 count, the rigorous statement is

    P((0,0) -> (N,0)) = a(N+1),

with a(1)=1 supplied by the separate degenerate single-edge object. For N>0 the bijection is with ordinary polygons only; the minimum possible N is 3, corresponding to the undissected quadrilateral. No ordinary polygon realizes e=1,2,3. The empty excursion maps to the one-vertex tree and then, by explicit separate convention, to the formal one-edge object.

Examples: N=3 gives U U D_2 and the quadrilateral (e=4). N=5 gives U^4 D_4 and the undissected hexagon (e=6). At N=6 the three excursions with two D_2 steps correspond to the three quadrangulations of a hexagon by a halving diagonal (e=7).

The original OEIS conjecture starts the path at (1,0), ending at (e,0). Translating the start to (0,0) produces exactly the length e-1 convention above. Thus the shift resolves the source extraction ambiguity rather than changing the mathematical claim.

## Generating functions and a corrected finite coefficient formula

Let E(z) count excursions by N and let G(z) count polygon graph edges e, including the formal single edge. The explicit size-preserving maps give G=zE. Root decomposition yields

    E=1+(zE)^3/(1-(zE)^2),
    G=z+z G^3/(1-G^2),
    (1+z)G^3-zG^2-G+z=0.

The last polynomial is the one already recorded in A067955; it is not claimed new. The ordinary-polygon generating function alone is G-z.

Lagrange inversion, G=z(1+G^3/(1-G^2)), gives a(1)=1 and, for e>=2,

    a(e)=(1/e) sum binomial(e,j) binomial((e-3-j)/2,j-1),

where the sum is restricted to integers 1<=j<=floor((e-1)/3) **and j≡e-1 (mod 2)**. All binomial arguments in the restricted sum are nonnegative integers. Indeed expansion first chooses j powers of G^3/(1-G^2), and the remaining exponent e-1-3j must be an even nonnegative integer. The resulting coefficient is binomial(j+(e-1-3j)/2-1,j-1). The currently displayed OEIS finite sum carries an explicit warning that it seems wrong; it omits this parity restriction and also does not supply the exceptional a(1). This note does not claim to have submitted an OEIS correction or established first priority for the corrected formula.

## Primary-source comparison

- [OEIS A067955](https://oeis.org/A067955), inspected 16 October 2026: counts even-faced dissections by boundary sides plus diagonals, offset 1; its tree comment uses n-1 tree edges; Nicholas Ham's 24 August 2015 comment gives the path conjecture from (1,0) to (n,0). The entry already records the same cubic and a series-reversion form. The matching first nontrivial hexagon example is also recorded there. The entry's one-edge term is treated here by an explicit formal convention rather than asserted to be an ordinary polygon.
- Curien and Kortchemski, *Random Non-Crossing Plane Configurations: A Conditioned Galton–Watson Tree Approach*, Random Structures & Algorithms 45 (2014), 236–260; [author-hosted primary paper](https://igor-kortchemski.perso.math.cnrs.fr/articles/Noncrossingconfigs.pdf), Proposition 2.2, published page 240, and [arXiv:1201.3354](https://arxiv.org/abs/1201.3354). The proposition identifies polygon dissections with plane trees having the prescribed number of leaves and no unary vertices. Its preceding construction removes the base-side dual edge and roots at the adjacent face corner. Our even-degree restriction, total-edge bookkeeping, and interval reconstruction are explicit elementary specializations of this classical correspondence. This is not the duality-preserving noncrossing-tree theorem from the separate quadrangulation literature.

The primary paper's relevant dual-tree statement and construction were inspected through its extracted full text; no claim of reading the full probability paper is made. The explicit proof above was derived independently and does not reproduce external code or figures.

## Independent finite polygon enumeration

The independent check, now preserved in `experiments/polygon_dissections.py`, enumerates 472 diagonal subsets on fixed convex polygons with B=4,6,8,10, subject to B+(number of diagonals)<=10. Pairs a<b and c<d were rejected when a<c<b<d or c<a<d<b. Each surviving diagonal split its containing face, and the final face vertex counts were tested for evenness. This enumeration uses polygon diagonals directly, not the plane-tree recurrence or excursion engine. It gave counts by total edges

    e=4:1, 6:1, 7:3, 8:1, 9:8, 10:13,

and zero for the other ordinary sizes through 10. These agree with the axis counts of Table 4 shifted by one. Even-faced dissections necessarily have an even boundary polygon, since summing face degrees gives B+2(number of diagonals); hence no odd-sided polygons were omitted. The finite check supports the construction but does not replace its proof. `experiments/tests/test_polygon_dissections.py` asserts this exact scope, compares every size 2..10 against both the corrected parity formula and the Table 4 shift, and checks that the formal size-one object is separate. Two unittest methods pass. No manuscript change was made.

## Final phase-2 disposition

Precise mathematical statements passed the independent internal reviews linked in reviews/review-log.md. Classical correspondence and source attribution are retained; no first-priority claim is made. The manuscript restricts its quotient recurrence to nonempty target cells, with absent cells zero only as bookkeeping. Complete proof notes and unresolved identifications remain distinct.
