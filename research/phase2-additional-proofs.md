# Supplementary exact derivations and source-table provenance

## Section 5 axis generating function

For the unrestricted steps (1,1),(1,−a),a≥1, let b_N count words ending at height zero after N steps. Choosing k downward steps, their positive sizes sum to N−k. Hence b_0=1 and b_N=Σ_(k=1..floor(N/2)) binom(N,k)binom(N−k−1,k−1), giving 1,0,2,3,10,25,... .

The stated source OGF is correct. A rigorous analytic coefficient derivation uses a circle |u|=R>1. The step Laurent series u+1/(u−1) converges there, and for sufficiently small |z| so does its word geometric series. Thus B(z) is the contour constant term of

  (u−1)/[(u−1)−z(u²−u+1)].

After dividing by u in the contour integrand, the poles inside the fixed circle are u=0 and α=(1+z−sqrt((1+z)(1−3z)))/(2z), with α→1. The residues are respectively 1/(1+z) and 1/[2 sqrt((1+z)(1−3z))]−1/[2(1+z)]. The other quadratic root diverges. Therefore

  B(z)=1/[2(1+z)] + 1/[2 sqrt(1−2z−3z²)].

Analytic equality near zero proves equality of formal coefficients. This is an independent derivation of the source formula, not a novelty claim. It also corrects two provisional example terms in the agent's draft report (12,30 were arithmetic transcription mistakes; the displayed sum gives10,25).

## Section 20 Riordan interpretation

The tree theorem with A={1,2,...} gives E=1+(zE)²/(1−zE), uniquely E(0)=1. Let M count ordinary Motzkin paths by length; the standard first-return decomposition gives M=1+zM+z²M². Motzkin excursions with no horizontal step at height zero have R=1/(1−z²M), by decomposition into a sequence of arches U (Motzkin excursion) D. Eliminating M gives z(1+z)R²−(1+z)R+1=0. The same equation follows for E, and uniqueness at zero proves E=R. Thus both reflected axis models in §20 enumerate Riordan paths. This supplies an equality proof; a direct local excursion-to-Motzkin bijection is not claimed. OEIS A005043 primary entry checked16 October2026 for this definition.

## All ten numerical source arrays

697 printed numeric body entries were extracted spatially from Ham's PDF text bounding boxes, mapped to column positions from the sorted horizontal axis, and retained as mathematical data in experiments/source_tables.json. No PDF or prose was copied into tracked files. The source PDF SHA-256 is recorded there. Printed axis labels are separately retained so that data coordinates do not silently inherit the duplicate12 at ordinal13 in Tables6 and7.

Counts by table:64,51,45,82,78,106,105,66,49,51. `python3 -m experiments.table_audit` independently recomputes every recorded value using finite transition recurrences; all agree. This is a claim about printed entries, not about interpreting every blank as zero. Sparse regions and table7's truncated visible range are retained exactly. `reviews/phase2-tables.md` independently remapped every numeric body token, checked the PDF hash and completeness, visually confirmed both label errors, and verified finite height bounds and small explicit words.

For up1/vertical-down models every vertex satisfies0≤y≤x, and same-column descending order is topological. For table7, arbitrary positive upward jumps and down1 steps may leave that wedge. To count any visible endpoint with x≤N,y≤Y, any intermediate height h is at mostY+N, since the remaining at mostN steps can decrease height only one each. That bound captures all words to visible endpoints and avoids truncation bias.

Source figures were inspected through their complete numeric extraction; the full source page containing Tables6–8 was additionally rendered and visually reviewed by the table reviewer. The fixture lets verification run from a fresh checkout without a PDF cache. Exact extraction is specific to this PDF version rather than a general PDF-table recognition claim.

## Two near-top slices and a vertical initial column

In §6 the unit-horizontal allowed increments are +1,0,−2,−4,... . Relative to the all-up path, a zero step has deficit1 and a −2k step has deficit2k+1. To end at height N−2 requires exactly two zero steps, giving binomial(N,2) for N≥2. To end at N−3 requires either three zero steps, or one −2 step after at least two upsteps. Thus the nonnegative count is binomial(N,3)+(N−2) for N≥3: the −2 step can occupy positions3,...,N. The source's two alternative identifiers remain unresolved. Counting all N possible positions would incorrectly drop the boundary condition. The deficit-two flat-only argument has no such boundary problem.

For the reflected vertical model of §19 at x=0, only positive odd vertical steps are possible. Their compositions of height y have OGF (1-z²)/(1-z-z²), giving countF_y for y≥1 and exceptional origin count1. This explains the Fibonacci assertion with its initial convention; adding horizontal steps changes the model and is not being done here.
