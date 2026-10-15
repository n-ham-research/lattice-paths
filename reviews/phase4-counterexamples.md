# Phase 4 independent counterexample and proof review

16 October 2026. Reviewer `/root/obstruction4`, a separate internal AI agent. Read research/phase4-inverse.md and research/phase4-infinite.md directly before reading any other Phase 4 review. Full project context and theorem statements were available; this is internal adversarial review, not external peer review or a novelty assessment.

## Inverse observations and geometry: accepted with scope retained

I independently checked I1's two directions. The fiber is affine only after **every preceding labelled row is fixed**: the inductive converse is necessary and correct. The note correctly rejects applying a row-deletion rank test to arbitrary partial trajectory data; its example p_2(0)=f(0)^2+f(1)f(-1) is exact. The row-space and periodic-compatible-fiber tests follow ordinary finite-dimensional linear algebra; intersecting with nonnegative or indicator constraints can identify coordinates even when rank fails.

For I2, set a=s_(n-2),b=s_(n-1). At the first negative-block target y=b-a-1 the smallest other argument is y-b+1=-a, and the largest is y<=b. Descending targets therefore introduce just one new negative weight at a time. The subsequent positive targets introduce one new positive weight and otherwise use recovered coordinates. This handles plateaus, b=0, and width jumps without a hidden slope bound. The top and bottom predecessor pivots are correctly assumed; no unsupported implication from nonextinction is used. This proof works in arbitrary characteristic conditional on pivots.

I3 is a legitimate compressed inverse result: a nonzero scalar preceding row tests the entire one-dimensional constant-input subspace. It then invokes the proved funnel connectivity theorem rather than falsely testing a q-dimensional space with a single vector. Its positive common value is forced already by the nonnegative first-row observation. Unbounded widths are correctly required before promoting finite visibility to all integers.

Reflection in I4 changes displacement d to 1-d and hence proves all-row multiset/total ambiguity for the stated positively reachable pair. Fixed residue labels and individual diagonals need not agree; the text correctly qualifies this. I5 uses termwise nonnegative differences. For a g-positive word, ratios f(d)/g(d) lie in [0,1], whose product equals one exactly when every factor is one. This proves both implications, including repeated jumps. The ordered-kernel restriction is essential and explicitly retained.

Executed the committed inverse experiment: all 70 widening funnels, 70 constant formulas, 256 reflection assignments and the partial-observation example passed. These computations supplement the proof and do not classify all compressed-data fibers.

## Modulus-two compressed converse: accepted

Independently traced the normalized recurrence through the claimed algebra:

1. Row two forces f(2)=f(-1)=x, with positive boundary pivot x+1.
2. Both middle row-three counts are C=x^2+2x+3; each boundary equality forces c=(x^2-x+2)/(x+1).
3. Both interior even row-four counts are 2(x+1)C and odd values are (2+x+c)C; the boundary constraints force a=(3x-1)/(x+1).
4. Row-five heights 1 and 3 introduce no new extreme weights. Their difference is A(a-c)+B(c-x), and substituting c,a factors as -2C(x-1)^2(x^2+2x-1)/(x+1)^2. Thus nonnegative x leaves exactly x=1 and x=sqrt(2)-1. Rational weights eliminate the latter.
5. On the exceptional branch, the listed positive weights give row three 4, row four parity values 8sqrt(2) and16sqrt(2)-8, and scalar row five 96-32sqrt(2). At row six the relevant known sums are 3sqrt(2) and8sqrt(2)-7; their difference forces the new negative extreme 7-5sqrt(2)<0. This excludes the branch solely by nonnegativity.
6. Once the visible weights are all one, each new boundary has a same-parity interior comparator and a nonzero factorial pivot, so induction extends identification on the entire visible window. The scaling f/t correctly multiplies row n by t^(-n).

The indicator bound N=3 follows because x=0 would force c=2. The rational prefix x=1/2 is nonnegative and survives through four. The irrational prefix survives through five with every endpoint positive. These show optimality for the stated finite-prefix classes; they do not show an all-horizon nonperiodic example. The assumption f(0)=f(1)>0 is substantive and correctly appears in every theorem statement. No conclusion is claimed for unequal weights or q>=3.

Executed the committed exact experiment: all16 binary assignments,650 rational parameter instances, independent weighted words through five and the Q(sqrt(2)) branch passed. SymPy is unavailable in this environment; no dependency was installed. I checked the displayed identities by substitution/algebra and the existing exact routines, not by an unexecuted symbolic-CAS claim.

## Own obstruction result correction and limits

During drafting O4.3 I initially wrote that both least representatives propagate without wrapping for arbitrary signed displacement. That was too strong: a negative displacement can wrap its lower representative upward, while a positive displacement can do the same to the top distance. I corrected this before the final note: upper wrapping is prohibited, lower reduction only adds q, giving r_next>=r+d and delta_next>=delta+1-d. Their sum increases **at least** one, which suffices for the2q bound. The independently valid variable-K mass proof is also retained. The homogeneous O4.1 proof only uses positive d for the lower representative or d<=0 for top distance, where the relevant increment is positive and the issue does not arise.

The sharp q/v examples concern prescribed later rows; they must not be described as origin-start optimality. The exact origin-start threshold for support contained in{0,1} is separately proved and is much stronger. Signed finite-support eventual obstruction and infinitely many separated uniform rows remain open here; failure of a proof's positivity step is not presented as a theorem counterexample.

No mathematical defect remains identified in I1–I5 or the q=2 theorem after this review. Historical originality remains unresolved, and no original-inventory disposition changes follow automatically from these new structural results.
