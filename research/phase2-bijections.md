# Phase 2: excursions, degree-restricted plane trees and restricted Dyck ascents

16 October 2026. Derived by internal agent `/root/bijections_phase2` independently of the phase-2 counting agent. These are explicit applications of classical bijections, not novelty claims. Status: complete proof supplied below, pending separate internal review. Original secondary row/column and polygon/blob/packed-word identifications remain unresolved unless explicitly stated here.

## Precise uniform construction

Let A be any subset of the nonnegative integers. An excursion is a finite word in {+1} union {-a:a in A}, with nonnegative partial sums and total zero. Steps form a set. The empty word is admitted. A zero height increment is a genuine single step. Write u for the number of +1 steps and r_a for the number of -a steps. Necessarily u=sum a r_a. The length is N=u+sum r_a. The construction concerns endpoints at height zero only.

**Theorem (classical explicit bijection).** Such excursions correspond bijectively to rooted ordered trees with N+1 vertices whose positive outdegrees belong to A+1={a+1:a in A}. The excursion has u+1 leaves, and r_a vertices of outdegree a+1. They also correspond bijectively to Dyck paths of semilength N all of whose nonempty maximal ascents have lengths in A+1.

**Forward map and proof.** Reverse the excursion and negate each increment. Its partial sum at position j equals the original excursion height at position N-j, hence is nonnegative; its increments are -1 or a. Append one final -1. Interpret each increment s as a preorder vertex of degree s+1. Start with one unfilled root slot; consume the next slot and insert its ordered children, visiting the leftmost remaining slot next. The number of available slots is one plus the increment sum, hence positive until the last vertex, and zero at the end. This constructs a unique finite plane tree. The appended -1 is the last leaf. Leaves correspond to original +1 steps together with this last leaf; positive degrees correspond to -a steps.

For degrees d_1,...,d_(N+1), form U^(d_1) D ... U^(d_(N+1)) D and remove its last D. At the ends of the earlier blocks the height is the sum of d_i-1, which is nonnegative. Within a block the path first rises, then descends by one, so the whole retained word is Dyck. There are sum d_i=N upsteps and N retained downsteps. Every nonzero d_i creates one maximal ascent of length d_i, because each block ends in D.

**Inverse.** Append D to the Dyck word and split at every D. The lengths of the intervening U blocks, including zero lengths, give the degree list. The Dyck prefix inequalities give positive slot counts before the final vertex. Delete its final degree zero; replace each remaining degree d by 1-d and reverse the list. This reconstructs the original excursion. Thus the maps are inverse, not just equinumerous generating function manipulations. The empty excursion maps to the one-vertex tree and empty Dyck word.

**Weights and generating function.** Let x mark original +1 steps and q_a mark -a. Root decomposition of the corresponding tree, assigning leaf weight x, gives T=x+sum_a q_a T^(a+1). Since T=xE, the excursion series satisfies

    E = 1 + sum_(a in A) q_a x^a E^(a+1).

This is a multivariate formal identity (finitely many monomials contribute to any fixed full size profile). For unit-horizontal steps set x=z and q_a=z, obtaining E=1+sum_a (zE)^(a+1), with a unique solution E(0)=1 even if 0 is in A. For vertical downward steps set q_a=1, x=z, **only when A excludes zero**; otherwise repeated zero-displacement vertical steps make horizontal-coordinate counts infinite. For positive A, fixed horizontal coordinate n admits only finitely many words: u=n, each downstep consumes at least one of n height units, so at most n downsteps. Thus the infinite degree set causes no finiteness problem.

## Applications with corrected indexing

Every parameter m in the following table is an integer m>=1 (source §23 restricts m>=3). All series below count excursions at (n,0), with z marking the original horizontal coordinate n, not an unspecified external sequence index.

| Source | A and horizontal convention | Excursion equation | Exact interpretation |
|---|---|---|---|
| §§6–11 | A={mk:k>=0}, all steps have x increment 1; m>=1 | E=1+zE/(1-(zE)^m) | Dyck semilength n with ascents 1 modulo m; plane trees with positive outdegrees 1 modulo m, n edges |
| §18 | A={2k:k>=1}, all x increments 1 | E=1+(zE)^3/(1-(zE)^2) | Plane trees with positive odd degrees >=3; Dyck semilength n with odd ascents >=3 |
| §20 | A={1,2,...}, all x increments 1 | E=1+(zE)^2/(1-zE) | Plane trees without unary vertices, n edges; Dyck semilength n with no ascents of length 1 |
| §17 first | A={m}, downward x increment 0 | E=1+z^m E^(m+1) | Full ordered (m+1)-ary trees; n must be divisible by m |
| §17 second | A={mk-1:k>=1}, all x increments 1 | E=1/(1-(zE)^m), equivalently E=1+z^m E^(m+1) | Positive tree degrees divisible by m; n must be divisible by m |
| §19 first | A={2k-1:k>=1}, downward x increment 0 | E=1+zE^2/(1-z^2E^2) | Trees with all positive degrees even; horizontal n equals leaves minus 1 |
| §§21–23 | A={mk:k>=1}, downward x increment 0 | E=1+z^m E^m(2E-1) | Trees with positive degrees 1 modulo m, excluding degree 1; horizontal n equals leaves minus 1 and is divisible by m |

For §6 take m=2, giving exactly E=1+zE/(1-z^2E^2). Thus the displayed source GF is rigorously correct for the axis extraction with the empty path included. For §§7–11 the semilength is exactly original n; there is no shift. For §20 the series starts 1,0,1,1,3,6,15,... and is the degree-restricted tree series; numerical comparison alone is not being used to prove the Motzkin interpretation.

Both §17 models have the **same horizontal-coordinate axis series**, despite having different total step lengths. At original endpoint (mn,0), each has count binomial((m+1)n,n)/(mn+1). For the first model every word has total length (m+1)n; the second model has total length mn by definition. This resolves the potentially misleading statement in the inventory that their horizontal scales differ: their step-length scales differ, but the corrected axis coordinate is mn for both. The algebraic reduction of the second equation follows from E(1-(zE)^m)=1.

For §§21–23 put t=z^m and H(t)=E(z). Then H=1+tH^m(2H-1). Lagrange inversion with W=H-1 gives, for n>=1,

    [t^n]H = (1/n)[v^(n-1)](1+v)^(mn)(1+2v)^n
            = (1/n) sum_(j=0)^(n-1) binomial(n,j) 2^j binomial(mn,n-1-j).

This supplies a finite exact formula and an explicit tree interpretation for every m>=1, with the empty excursion coefficient 1. It does not yet identify the source's blobs or Sylvester classes. The latter require matching their precise size statistics against the cited primary paper, not extrapolating a sequence name.

Reflected models: reversing the word and negating its heights maps excursions to excursions and exchanges up/down signs while preserving each step's horizontal displacement and original total horizontal coordinate. Consequently each paired reflected model in §§6,18,19,20,22 has the same axis series. This argument does **not** establish any claimed equalities for positive endpoint rows.

## Primary-source comparison and boundary

- Hackl, Heuberger and Prodinger, *Counting Ascents in Generalized Dyck Paths*, AofA 2018, Proposition 2 explicitly states and proves the preorder degree correspondence for Łukasiewicz excursions. Primary full text: https://drops.dagstuhl.de/storage/00lipics/lipics-vol110-aofa2018/LIPIcs.AofA.2018.26/LIPIcs.AofA.2018.26.pdf ; preprint https://arxiv.org/abs/1801.02996 . The reversal and size-weight bookkeeping above are independent explicit derivations adapting that classical construction to Ham's down-jump and vertical-step conventions. No novelty is claimed.
- Brak, Iliev and Prellberg, *An infinite family of adsorption models and restricted Lukasiewicz paths*, arXiv:1105.0306v2 (2011), https://arxiv.org/abs/1105.0306 , explicitly studies restricted Łukasiewicz excursions, algebraic series and a bijection with rise-restricted Dyck paths. Its abstract and metadata were checked; detailed theorem-by-theorem equivalence for arbitrary noninterval degree sets has not been claimed.
- Novelli and Thibon, *Hopf Algebras of m-permutations, (m+1)-ary trees, and m-parking functions*, arXiv:1403.5962v3 (2020), https://arxiv.org/abs/1403.5962 , discusses both m-permutations and packed-word analogues. Abstract/metadata only checked here. Its m-permutation result cannot silently be substituted for the source's m-packed-word assertion.

The bijection and series are known machinery; useful project progress is the uniform exact interpretation and indexing for numerous source models. A publishable new theorem has not been established by this investigation.

## Reproducible independent checks

`experiments/tree_bijections.py` implements both maps via degrees, including validity checks. `experiments/tests/test_tree_bijections.py` enumerates every binary word of length 2n for 0<=n<=7, retains Dyck words by independent prefix checks, verifies both inverse identities and the ascent/outdegree statistic, then compares the image sets with separately recursively generated nonnegative excursions of length n with all increments <=1. Two unittest methods pass. This tests every allowed-degree restriction implicitly by retaining each exact step/degree multiset. No claim that these finite checks replace the proof is intended.

## Final phase-2 disposition

Precise mathematical statements passed the independent internal reviews linked in reviews/review-log.md. Classical correspondence and source attribution are retained; no first-priority claim is made. The manuscript restricts its quotient recurrence to nonempty target cells, with absent cells zero only as bookkeeping. Complete proof notes and unresolved identifications remain distinct.
