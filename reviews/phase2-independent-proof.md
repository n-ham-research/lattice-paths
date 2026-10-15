# Phase 2 independent proof review

16 October 2026. Reviewer: internal AI agent `/root/phase2_independent_proof`. Exact model version is not exposed and is not asserted. This is internal mathematical review, not human approval or external peer review.

## Context and verdict

Read `AGENTS.md`, `research/handover.md`, `research/conjecture-audit.md`, `research/phase2-classification.md` and `research/phase2-bijections.md`. Did not read other phase-2 review reports or implementation/test files before producing these findings. The usual review-log reading was deferred to preserve the explicitly requested fresh-review separation. Reconstructed proofs from the statements and ran independently written exact checks. No new primary-source inspection was performed, so this report certifies mathematical arguments under their stated definitions, not literature completeness or transcription of original source models.

**Verdict: approve the mathematical classification and explicit bijection results for manuscript promotion**, retaining their structural scope, precise indexing and existing no-novelty qualification. No proof defect or counterexample was found. Application rows should explicitly share the hypothesis that m is a positive integer; the vertical single-downstep row is false as a finite count if m=0. This is a presentation boundary, since the construction already excludes zero vertical displacement when counting by horizontal coordinate.

## Reconstructed classification argument

For a source residue progression a,a+q,...,b, the difference of predecessor sums at y+q and y is exactly f(y-a+q)-f(y-b). Residue indicator functions form a basis of the block-constant space, so this cancellation proves both directions of criterion A, including absent source cells and singleton target cells. No assumption about the one actual origin trajectory is needed or permissible here.

For the finite triangular converse, compare regularity at transitions n and n+1 on source residue n modulo q. Their source cells differ by the single point n. Whenever q≤n≤N-1 and 0≤y≤n-q, subtraction gives f(y-n+q)=f(y-n). The corresponding lower arguments cover [-n,-q]; their union is exactly [1-N,-q]. These relations connect every congruent pair among [1-N,0]. When N=q that interval already contains exactly one representative of each residue and needs no connections.

Every positive d≤N is then attached to this nonpositive base by the last transition: take r=q-d when d<q, otherwise r=0, and y=d+r-q. The source residue r exists because N≥q; the target pair y,y+q exists because d+r≤N. Its smallest source vertex is r, so the first boundary argument is d. Its largest vertex b_r makes the second argument y-b_r lie in [1-N,0], with the same residue as d. For d≥q, the required upper bound follows from b_0≥N-q. This proves the entire observable-window statement, not merely its negative half.

Sufficiency follows term by term because every used difference lies in [1-N,N]. At N<q all target cells are singletons. The window is exact: its extrema occur at y=0,z=N-1 and y=N,z=0 in the final transition, while differences outside it are invisible. Passing to arbitrarily large N proves the full infinite classification. A nonempty finite set cannot be periodic with a positive period. The admissible periods and affine integer shear claims follow directly from indicator periodicity and the layerwise residue relabeling.

The distinction between regularity of the entire input space and uniformity of the one trajectory is essential. D={-1} is a valid counterexample to the latter converse. Likewise a single transition cannot replace the nested collection. The conclusions do not extend automatically to arbitrary moving intervals or sloping cones.

## Reconstructed bijections and formal series

Reversing and negating an excursion gives a nonnegative Łukasiewicz prefix with steps at least -1 and total zero. Appending -1 gives precisely a preorder tree degree sequence: one plus each partial increment sum is the available-slot count, positive before the final entry and zero afterwards. The last entry is a leaf. Thus original upsteps correspond to all leaves except this last one, and each original -a corresponds to degree a+1.

The degree encoding U^(d_1)D ... U^(d_(N+1))D, with its last D removed, has N rises and N falls. All complete nonfinal blocks end at nonnegative heights; their interiors cannot dip below the block endpoint. Each positive degree is exactly one maximal ascent because consecutive blocks are separated by a D. Conversely appending D and splitting at each D, including empty U blocks, uniquely recovers degrees. The final block has degree zero, including the empty-path case. The inverse reversal restores the excursion and all statistics.

Tree root decomposition gives T=x+sum q_a T^(a+1). Every tree has one more leaf than the original upstep count, hence T=xE and E=1+sum q_a x^a E^(a+1). This remains a valid full-profile formal identity when 0 belongs to A, provided a grading counting all steps is used. With unit horizontal steps the terms have strictly positive z-degree, so E(0)=1 uniquely determines coefficients. With vertical downsteps, 0 must be absent; positive downsteps consume height and their number is bounded by the number of upsteps. This proves the needed finiteness even for infinite A.

All displayed application equations follow from geometric sums under the stated positive-m convention. In particular the §§21–23 equation follows by multiplying E-1=(zE)^m E/(1-(zE)^m); the resulting identity is E-1=z^m E^m(2E-1). Lagrange inversion with W=E-1 yields exactly the displayed finite sum. The second §17 equation reduces to E=1+z^m E^(m+1), explaining equality of horizontal-coordinate series despite different total word lengths. Reversal and sign change preserves nonnegativity of excursions and horizontal displacement; it supplies no corresponding positive-endpoint result.

## Independent exact checks

One-off Python code was run directly, independently of repository implementations. It enumerated all binary indicators on [1-N,N] for q=1,...,4 and N=1,...,5: 5,456 instances. For every instance it explicitly computed predecessor sums for every source and target residue in every transition and compared regularity with window periodicity (or automatic acceptance when N<q). Every instance passed.

A second independent recursion enumerated all nonnegative excursions with steps at most +1 and length N for N=0,...,7. Counts were 1,1,2,5,14,42,132,429, totaling 626. Each excursion was converted to degrees and a Dyck word, all prefix/size conditions were checked, and splitting the Dyck word recovered the original excursion. Image sizes equaled excursion counts. Retaining exact step/degree profiles checks all restrictions A on these finite instances simultaneously. These are corroborating finite checks, not substitutes for the reconstructed proofs. The one-off code is not claimed as a committed regression test.

## Promotion and novelty limits

Theorems A–C and the explicit classical maps are suitable for a carefully scoped manuscript. They do not establish a converse for observed counts, a universal classification for moving intervals, a classification of factorial sequences, or the original polygon/blob/packed-word identifications. The supplied priority search is limited negative evidence; elementary cancellation and standard Łukasiewicz/tree/Dyck machinery cannot support a novelty claim without substantially more comparison. This reviewer independently approves mathematical correctness, not publication novelty or the completeness of source attribution.

## Independent follow-up: polygons and manuscript transcription

Read `research/phase2-polygons.md`, `paper/sections/07-general-results.tex`, and `paper/sections/05-catalan-families.tex` on the coordinator's follow-up request. No other reviewer reports were read first.

**Polygon verdict: approve the mathematics**, retaining notes-only status until any separate source/novelty requirements are satisfied. The inverse really is explicit: the ordered children partition the consecutive nonbase boundary sides into intervals of their leaf counts. Their endpoint chords delimit the unique root face, and recursion uniquely fills the child polygons. Disjoint or nested leaf intervals preclude crossing chords. An internal child has at least three leaves in this degree-restricted family, so its chord is a genuine diagonal; a leaf yields one boundary edge. Consequently the maps are inverse, with no accidental rotation/reflection quotient or extra base-side multiplicity.

The statistics reconstruct correctly: L=u+1, I=r, B=L+1=u+2, and the number of diagonals is I-1. Hence graph edges equal N+1, tree vertices equal graph edges, and a downstep -2k corresponds to a face of size 2k+2. The single-edge term is a declared formal object only. The smallest ordinary dissection is the quadrilateral at e=4. Summing even face sizes proves B even, independently confirming the permitted ambient polygons.

For G=zE the displayed cubic follows directly. Lagrange expansion chooses j internal-root terms and then exponent e-1-3j from (1-v^2)^(-j). It is nonzero precisely when that exponent is nonnegative and even. This yields both the stated j range and j congruent to e-1 modulo 2, with the stated integer upper binomial argument. The exceptional e=1 term is necessary. An independently written root-degree convolution, using allowed degrees 0,3,5,..., agrees with the finite binomial formula for every e=2,...,25; the initial e=1,...,10 counts are 1,0,0,1,0,1,3,1,8,13. This does not independently certify the note's descriptions of OEIS or the cited paper, which this reviewer has not inspected.

**Manuscript verdict: faithful proof transcription except for one required scope clarification.** Section 05 preserves the reviewed maps, weights, positivity condition, horizontal indexing and Lagrange formula. Its m≥1 hypothesis is explicit. Section 07 preserves the boundary criterion and finite/infinite rigidity proof correctly. However the displayed quotient recurrence must be explicitly restricted to nonempty target residue cells. An absent target cell has no per-endpoint value; assigning it zero for bookkeeping does not make the unmasked recurrence true there. Concrete boundary example: q=3, D=Z, n=1, s=2 gives no target vertex but displayed RHS 1 from the initial source. Suggested repair: introduce the recurrence with “For each nonempty target residue cell s” and retain zero assignment solely as bookkeeping (or explicitly insert a target-presence indicator). This does not affect the substantive theorem or any actual existing endpoint count. No other mathematical transcription issue was found in these two sections.

### Quotient transcription repair verified

Re-inspected Section 07 after the coordinator's repair: it now explicitly states the recurrence “for every nonempty target residue cell” and says absent-cell zero values are bookkeeping without applying the recurrence to them. This resolves the sole required transcription clarification above; mathematical promotion approval is now unconditional within the report's existing scope and novelty limits.

Inspected `experiments/tests/test_residue_quotient.py` and ran `python3 -m unittest experiments.tests.test_residue_quotient` successfully (one test). It compares the quotient with full endpoint DP for every union-of-residues mask, q=1,...,4, and columns 1,...,8, and checks zero bookkeeping in absent target cells. The presence condition s≤n is exactly correct for canonical residues 0≤s<q in the triangular target. No additional changes were required.
