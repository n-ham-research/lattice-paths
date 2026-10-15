# Complete source conjecture inventory

Source: Nicholas Ham, *Lattice path conjectures* (11 May 2019), all 41 sections and all ten tables. This is a transcription audit, not a verification report. Every source claim remains unresolved here and every independently reproduced term count is **0**; consult `conjecture-audit.md` for subsequent mathematical evidence. OEIS identifiers are source attributions, not independently validated descriptions. No novelty claim is made.

The companion `conjecture-inventory.json` contains structured models and individually identified claims. Its `source_text_line` refers to the locally retained layout text. Source sections 1 and 41 contain context and tables rather than new conjectures. Some claims bundle explicitly paired rows or symmetric diagonals; each named slice is preserved.

## Counting conventions and unresolved indexing

For a step set S and region R, P_S,R(x,y) counts finite ordered words in S starting at (0,0), all of whose partial sums lie in R and whose sum is (x,y). The empty word contributes one at the origin. These are the working conventions; the original document often leaves them implicit. Restrictions apply to every visited vertex, not only the final endpoint. All regions used here are convex, so segments between admissible vertices also remain in the region.

A row fixes y and varies x; a column fixes x and varies y; a diagonal y=x+a is sampled by increasing x; a column total sums all reachable heights in that column. When a source does not state the endpoint extraction, this inventory says so rather than assuming the x-axis. Reachable-only sampling is distinct from sampling every integer coordinate. Infinite step sets require a separate local finiteness argument. Unrestricted column sums can be infinite even when endpoint counts are finite.

The source repeatedly calls column totals the same sequence as endpoint counts without giving an offset. Initial zeros, parity, residue classes and factorial tails must be resolved separately. Zero-height steps (1,0) are legitimate; a zero-displacement step (0,0) creates infinitely many words.

## 1. Introduction

Priority: later. Source text starts at line 13.

**Conventions / ambiguities.** Context, algorithmic motivation, and open Euclid-orchard direction; no numerical sequence assertion.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-01-01 | Equal counting functions permit substitution of a cheaper counting algorithm when inputs and conventions correspond. | algorithmic observation | — | 0 | source context |
| H2019-01-02 | Seek sequence connections for step sets contained in Euclid’s orchard, higher-dimensional or rational-lattice analogues. | research question | — | 0 | source context |

- H2019-01-01: An equality alone gives no algorithmic speedup without a complexity analysis.

**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 2. Powers of 2

Priority: later. Source text starts at line 42.

- **positive-horizontal**: S = `{(a,0): a in Z_>0}`; R = `Z^2 (no boundary stated)`.

**Conventions / ambiguities.** Source writes Z_+ without defining whether zero is excluded. Zero would give a zero step and infinite counts. Endpoint/index not specified.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-02-01 | Horizontal compositions are associated with powers of two. | Endpoint (n,0); source does not state offset. | A000079 | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 3. k-generalised Fibonacci numbers

Priority: later. Source text starts at line 47.

- **bounded-horizontal**: S = `{(a,0):1<=a<=k}, k in Z_>0`; R = `Z^2 (no boundary stated)`.

**Conventions / ambiguities.** The role of k and indexing in A092921 require checking.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-03-01 | Bounded positive horizontal increments yield a k-step Fibonacci family. | Endpoint (n,0), k fixed | A092921 | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 4. binomial((m+1)n,n)

Priority: later. Source text starts at line None.

- **vertical-fixed**: S = `{(1,1),(0,-m)}, m in Z_>0`; R = `Z^2 (no boundary stated)`.

**Conventions / ambiguities.** Endpoint absent. Natural proposed reading is ((mn),0), with mn upsteps and n downsteps; do not equate x=n with sequence index n.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-04-01 | Unconstrained counts are associated with binomial((m+1)n,n). | Likely endpoint (mn,0), not explicitly specified | A000984, A005809, A005810 | 0 | unresolved |

- H2019-04-01: Identifiers correspond in source to m=1,2,3 respectively.

**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 5. An algebraic ordinary generating function

Priority: later. Source text starts at line 62.

- **up-arbitrary-down**: S = `{(1,1)} union {(1,-a):a in Z_>0}`; R = `Z^2 (no boundary stated)`.

**Conventions / ambiguities.** Endpoint and starting sequence index absent.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-05-01 | Proposed OGF is (1/2)*(1/(x+1)+1/sqrt(1-2*x-3*x^2)). | Unspecified endpoint slice, probably y=0 | A246437 | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 6. Ordered odd trees

Priority: later. Source text starts at line 67.

- **even-down-zero**: S = `{(1,1)} union {(1,-2*k):k in Z_>=0}`; R = `y>=0`.
- **even-up-zero**: S = `{(1,-1)} union {(1,2*k):k in Z_>=0}`; R = `y>=0`.

**Conventions / ambiguities.** The first primary slice is not explicitly stated; zero-height steps (1,0) are included. Reversal/reflection does not automatically preserve arbitrary endpoint slices.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-06-01 | The principal series satisfies A(x)=1+x*A(x)/(1-x^2*A(x)^2), associated with ordered odd trees. Model: `even-down-zero`. | Primary slice unspecified, probably y=0 | A101785 | 0 | unresolved |
| H2019-06-02 | The near-top diagonal may have triangular numbers. Model: `even-down-zero`. | y=x-2 | A000217 | 0 | unresolved |
| H2019-06-03 | The next diagonal may match either cited sequence. Model: `even-down-zero`. | y=x-3 | A003600, A283551 | 0 | unresolved |
| H2019-06-04 | Sums over each finite column may give the cited sequence. Model: `even-down-zero`. | sum over all endpoints (x,y), x fixed | A143017 | 0 | unresolved |
| H2019-06-05 | The reflected step model may give the same ordered-odd-tree sequence. Model: `even-up-zero`. | y=0 | A101785 | 0 | unresolved |

- H2019-06-02: Tentative source match checked there only to value 91; not independent verification.

**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 7. Dyck ascents congruent to 1 modulo 3

Priority: later. Source text starts at line 81.

- **mod-3-down**: S = `{(1,1)} union {(1,-3*k):k in Z_>=0}`; R = `y>=0`.

**Conventions / ambiguities.** Principal endpoint slice and map from horizontal coordinate to Dyck semilength absent. In §11 the intended parameter m needs a positive-integer domain.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-07-01 | Counts are associated with Dyck paths whose ascent lengths are 1 modulo 3. | Primary slice unspecified, probably y=0 | A212383 | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 8. Dyck ascents congruent to 1 modulo 4

Priority: later. Source text starts at line 87.

- **mod-4-down**: S = `{(1,1)} union {(1,-4*k):k in Z_>=0}`; R = `y>=0`.

**Conventions / ambiguities.** Principal endpoint slice and map from horizontal coordinate to Dyck semilength absent. In §11 the intended parameter m needs a positive-integer domain.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-08-01 | Counts are associated with Dyck paths whose ascent lengths are 1 modulo 4. | Primary slice unspecified, probably y=0 | A212384 | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 9. Dyck ascents congruent to 1 modulo 5

Priority: later. Source text starts at line 93.

- **mod-5-down**: S = `{(1,1)} union {(1,-5*k):k in Z_>=0}`; R = `y>=0`.

**Conventions / ambiguities.** Principal endpoint slice and map from horizontal coordinate to Dyck semilength absent. In §11 the intended parameter m needs a positive-integer domain.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-09-01 | Counts are associated with Dyck paths whose ascent lengths are 1 modulo 5. | Primary slice unspecified, probably y=0 | A212385 | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 10. Dyck ascents congruent to 1 modulo 6

Priority: later. Source text starts at line 99.

- **mod-6-down**: S = `{(1,1)} union {(1,-6*k):k in Z_>=0}`; R = `y>=0`.

**Conventions / ambiguities.** Principal endpoint slice and map from horizontal coordinate to Dyck semilength absent. In §11 the intended parameter m needs a positive-integer domain.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-10-01 | Counts are associated with Dyck paths whose ascent lengths are 1 modulo 6. | Primary slice unspecified, probably y=0 | A212386 | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 11. Dyck ascents congruent to 1 modulo m

Priority: later. Source text starts at line None.

- **mod-m-down**: S = `{(1,1)} union {(1,-m*k):k in Z_>=0}`; R = `y>=0`.

**Conventions / ambiguities.** Principal endpoint slice and map from horizontal coordinate to Dyck semilength absent. In §11 the intended parameter m needs a positive-integer domain.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-11-01 | Counts are associated with Dyck paths whose ascent lengths are 1 modulo m. | Primary slice unspecified, probably y=0 | — | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 12. binomial(2n+1,n+1)

Priority: later. Source text starts at line 113.

- **up-nonpositive**: S = `{(1,1)} union {(1,1-k):k in Z_>0}`; R = `Z^2 (no boundary stated)`.

**Conventions / ambiguities.** No region or endpoint specified; (1,0) is allowed.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-12-01 | Counts are associated with binomial(2n+1,n+1). | Unspecified slice/index | A001700 | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 13. Compositions into 2n parts

Priority: later. Source text starts at line 118.

- **up-odd-down**: S = `{(1,1)} union {(1,1-2*k):k in Z_>0}`; R = `Z^2 (no boundary stated)`.

**Conventions / ambiguities.** The title says compositions of n into 2n parts, impossible for positive parts when n>0; weak compositions versus another total require resolution.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-13-01 | A composition-counting sequence is suggested. | Unspecified slice/index | A165817 | 0 | unresolved |
| H2019-13-02 | The author asks why the formula is not binomial(3n-1,n). | comparison question | — | 0 | unresolved |

- H2019-13-02: Question, not an assertion of equality.

**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 14. Ternary and noncrossing trees

Priority: later. Source text starts at line 125.

- **odd-up**: S = `{(1,-1)} union {(1,2*k-1):k in Z_>0}`; R = `Z^2 (no boundary stated)`.
- **vertical-two**: S = `{(1,1),(0,-2)}`; R = `y>=0`.

**Conventions / ambiguities.** The first model has no nonnegative boundary in the text; its fixed-column endpoints are unbounded above. Do not silently impose y>=0.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-14-01 | The two low rows are associated with binomial(3n,n)/(2n+1). Model: `odd-up`. | rows y=0 and y=1 separately | A001764 | 0 | unresolved |
| H2019-14-02 | Tentative fixed-column sequence match. Model: `odd-up`. | column x=3, y increasing | A000217 | 0 | unresolved |
| H2019-14-03 | Tentative fixed-column sequence match. Model: `odd-up`. | column x=4, y increasing | A062748 | 0 | unresolved |
| H2019-14-04 | Tentative fixed-column sequence match. Model: `odd-up`. | column x=5, y increasing | A005718 | 0 | unresolved |
| H2019-14-05 | Tentative fixed-column sequence match. Model: `odd-up`. | column x=6, y increasing | A062749 | 0 | unresolved |
| H2019-14-06 | Tentative near-top diagonal match. Model: `odd-up`. | y=x-1 | A127927 | 0 | unresolved |
| H2019-14-07 | Nonnegative vertical-down paths give the ternary-tree sequence. Model: `vertical-two`. | y=0, coordinate/index not stated | A001764 | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 15. binomial(4n-1,n)

Priority: later. Source text starts at line 138.

- **sparse-down**: S = `{(1,1)} union {(1,1-3*k):k in Z_>0}`; R = `Z^2 (no boundary stated)`.

**Conventions / ambiguities.** Endpoint/index not specified.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-15-01 | Counts are associated with binomial(4n-1,n). | Unspecified slice/index | A262977 | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 16. binomial(5n-1,n)

Priority: later. Source text starts at line 143.

- **sparse-down**: S = `{(1,1)} union {(1,1-4*k):k in Z_>0}`; R = `Z^2 (no boundary stated)`.

**Conventions / ambiguities.** Endpoint/index not specified.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-16-01 | Counts are associated with binomial(5n-1,n). | Unspecified slice/index | A163455 | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 17. Pfaff–Fuss–Catalan sequences

Priority: later. Source text starts at line 148.

- **vertical-m**: S = `{(1,1),(0,-m)}, m in Z_>0`; R = `y>=0`.
- **unit-x-m**: S = `{(1,1)} union {(1,1-m*k):k in Z_>0}, m in Z_>0`; R = `y>=0`.

**Conventions / ambiguities.** Source does not state endpoint extraction/index for either model. Models use different horizontal scales. Later OEIS list is not explicitly assigned to parameter values.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-17-01 | The nonnegative model is associated with the Pfaff–Fuss–Catalan family. Model: `vertical-m`. | Primary slice unspecified, likely y=0 | A000108, A001764, A002293, A002294 | 0 | unresolved |
| H2019-17-02 | The nonnegative model is associated with the Pfaff–Fuss–Catalan family. Model: `unit-x-m`. | Primary slice unspecified, likely y=0 | A000108, A001764, A002293, A002294 | 0 | unresolved |
| H2019-17-03 | Additional unassigned family identifiers are listed. Model: `vertical-m`. | Parameter assignment/extraction absent | A002295, A002296, A007556, A062994, A059967, A062744, A230388 | 0 | unresolved |
| H2019-17-04 | A possible Pfaff–Fuss–Catalan triangle is suggested. Model: `vertical-m`. | Full array? unspecified | A062993 | 0 | unresolved |

- H2019-17-01: Source assigns m=1,2,3,4 respectively; Tables 1–3 use first model with m=2,3,4.
- H2019-17-02: Source assigns m=1,2,3,4 respectively; Tables 1–3 use first model with m=2,3,4.

**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 18. Even-sided polygon dissections

Priority: later. Source text starts at line 167.

- **even-down-positive**: S = `{(1,1)} union {(1,-2*k):k in Z_>0}`; R = `y>=0`.
- **even-up-positive**: S = `{(1,-1)} union {(1,2*k):k in Z_>0}`; R = `y>=0`.

**Conventions / ambiguities.** Excludes horizontal zero-height steps, unlike §6; source associates polygon dissections by total edges (sides plus diagonals).

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-18-01 | Counts are associated with even-sided polygon dissections indexed by total edges. Model: `even-down-positive`. | Primary slice unspecified, probably y=0; Table 4 | A067955 | 0 | unresolved |
| H2019-18-02 | Several candidate matches remain indistinguishable in available data. Model: `even-down-positive`. | y=x-6 | A055998, A027379, A167544, A141214 | 0 | unresolved |
| H2019-18-03 | Tentative diagonal match. Model: `even-down-positive`. | y=x-7 | A028563 | 0 | unresolved |
| H2019-18-04 | Three reflected-model rows may yield the dissection sequence. Model: `even-up-positive`. | rows y=0,1,3 separately | A067955 | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 19. Even trees

Priority: later. Source text starts at line 179.

- **vertical-odd-down**: S = `{(1,1)} union {(0,1-2*k):k in Z_>0}`; R = `y>=0`.
- **vertical-odd-up**: S = `{(1,-1)} union {(0,2*k-1):k in Z_>0}`; R = `y>=0`.

**Conventions / ambiguities.** First-model primary slice not explicitly identified; Table 5 resolves the array, not its indexing against OEIS.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-19-01 | Counts are associated with even trees. Model: `vertical-odd-down`. | Primary slice unspecified; Table 5 | A049124 | 0 | unresolved |
| H2019-19-02 | Two rows of the reflected model may match even trees. Model: `vertical-odd-up`. | rows y=0,1 separately | A049124 | 0 | unresolved |
| H2019-19-03 | Vertical-only initial-column paths are associated with Fibonacci numbers. Model: `vertical-odd-up`. | x=0, y increasing | A000045 | 0 | unresolved |
| H2019-19-04 | A tentative next-column match is given. Model: `vertical-odd-up`. | x=1, y increasing | A029907 | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 20. Motzkin sums / Riordan numbers

Priority: later. Source text starts at line 189.

- **arbitrary-down**: S = `{(1,1)} union {(1,-k):k in Z_>0}`; R = `y>=0`.
- **arbitrary-up**: S = `{(1,-1)} union {(1,k):k in Z_>0}`; R = `y>=0`.

**Conventions / ambiguities.** Source says Motzkin paths of length n with k horizontal steps at level 0 but does not define the correspondence or role of k; Tables 6–7 have a duplicated column label 12 near their end.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-20-01 | The models are associated with Motzkin sums / Riordan-number sequences. Model: `arbitrary-down`. | Primary extraction unspecified; Table 6 | A097609, A005043 | 0 | unresolved |
| H2019-20-02 | The second model is proposed as another realization. Model: `arbitrary-up`. | Primary extraction unspecified; Table 7 | A097609, A005043 | 0 | unresolved |
| H2019-20-03 | The second-model row is associated with generalized ballot numbers / first differences of Motzkin sums. Model: `arbitrary-up`. | y=2 | A002026 | 0 | unresolved |
| H2019-20-04 | Several OEIS alternatives are listed for a fixed column. Model: `arbitrary-up`. | x=3, y increasing | A022856, A152948, A089071, A133263, A238531 | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 21. Little Schröder numbers

Priority: later. Source text starts at line 200.

- **vertical-any-down**: S = `{(1,1)} union {(0,-z):z in Z_>0}`; R = `y>=0`.

**Conventions / ambiguities.** Endpoint/index not explicit.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-21-01 | Counts are associated with little Schröder (super-Catalan) numbers. | Primary slice unspecified; Table 8 | A001003 | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 22. Blobs with 2n+1 edges

Priority: later. Source text starts at line 206.

- **vertical-even-down**: S = `{(1,1)} union {(0,-2*z):z in Z_>0}`; R = `y>=0`.
- **vertical-even-up**: S = `{(1,-1)} union {(0,2*k):k in Z_>0}`; R = `y>=0`.

**Conventions / ambiguities.** Indexing and meaning of blobs must be obtained from the sequence reference.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-22-01 | Counts are associated with blobs having 2n+1 edges. Model: `vertical-even-down`. | Primary slice unspecified; Table 9 | A003168 | 0 | unresolved |
| H2019-22-02 | Three reflected-model rows may give the blob sequence. Model: `vertical-even-up`. | rows y=0,1,2 separately | A003168 | 0 | unresolved |
| H2019-22-03 | Tentative first-column match (other candidates were still possible). Model: `vertical-even-up`. | x=1, y increasing | A001792 | 0 | unresolved |
| H2019-22-04 | Two tentative second-column alternatives. Model: `vertical-even-up`. | x=2, y increasing | A049611, A084851 | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 23. Sylvester classes of m-packed words

Priority: later. Source text starts at line None.

- **vertical-multiple-down**: S = `{(1,1)} union {(0,-m*z):z in Z_>0}, integer m>=3`; R = `y>=0`.

**Conventions / ambiguities.** Only m=3 is explicitly assigned an identifier.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-23-01 | The family is associated with Sylvester classes of m-packed words. | Primary slice unspecified; m=3 shown in Table 10 | A243659 | 0 | unresolved |
| H2019-23-02 | Additional family identifiers are listed without parameter assignment. | Unspecified parameter/extraction | A243667, A243668 | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 24. Factorials

Priority: first. Source text starts at line 225.

- **odd-wedge**: S = `{(1,2*a-1),(1,1-2*a):a in Z_>0}`; R = `-x<=y<=x`.
- **all-triangle**: S = `{(1,a):a in Z}`; R = `0<=y<=x`.
- **nonzero-triangle**: S = `{(1,a),(1,-a):a in Z_>0}`; R = `0<=y<=x`.

**Conventions / ambiguities.** Diagonal/row sequences require reachable vertices only and offsets. Column totals are separate quantities. Source has stray a in all-triangle diagonal sentence.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-24-01 | Odd-step wedge diagonals are associated with factorials. Model: `odd-wedge`. | y=x+a, fixed integer a, reachable points only | A000142 | 0 | unresolved |
| H2019-24-02 | Odd-step wedge column totals are associated with factorials. Model: `odd-wedge`. | sum_y P(n,y) | A000142 | 0 | unresolved |
| H2019-24-03 | Even-height rows are associated with even factorials. Model: `odd-wedge`. | y=2a, fixed integer a, admissible x | A010050 | 0 | unresolved |
| H2019-24-04 | Odd-height rows are associated with odd factorials. Model: `odd-wedge`. | y=2a+1, fixed integer a, admissible x | A009445 | 0 | unresolved |
| H2019-24-05 | All-step triangle top diagonal gives factorials. Model: `all-triangle`. | y=x | A000142 | 0 | unresolved |
| H2019-24-06 | All-step triangle fixed positive rows give factorials. Model: `all-triangle`. | y=a, fixed positive integer a | A000142 | 0 | unresolved |
| H2019-24-07 | All-step triangle column totals give factorials. Model: `all-triangle`. | sum_y P(n,y) | A000142 | 0 | unresolved |
| H2019-24-08 | Nonzero-step triangle top diagonal gives factorials with an explicit endpoint shift. Model: `nonzero-triangle`. | P(n+1,n+1) | A000142 | 0 | unresolved |

- H2019-24-01: Odd-step reachability forces y=x mod 2; odd a gives an identically zero diagonal. Negative even a has a nonzero starting offset.
- H2019-24-02: Source says trivially equal; compare offset independently.
- H2019-24-06: Starting x=a may yield a factorial tail rather than the complete sequence.

**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 25. Alternating factorials

Priority: second. Source text starts at line 240.

- **nonzero-triangle**: S = `{(1,a),(1,-a):a in Z_>0}`; R = `0<=y<=x`.

**Conventions / ambiguities.** Text calls endpoints (0,n+1) the x-axis: these lie on the y-axis and outside the triangle except the origin. Plausible intended endpoints are (n+1,0); preserve defect rather than silently repairing.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-25-01 | Axis counts are associated with alternating factorials. | Text says x-axis but writes P(0,n+1) | A005165 | 0 | unresolved |
| H2019-25-02 | Row two is also associated with alternating factorials. | y=2 | A005165 | 0 | unresolved |
| H2019-25-03 | Top diagonal gives factorials. | P(n+1,n+1) | A000142 | 0 | unresolved |
| H2019-25-04 | Column totals give factorials. | sum_y P(n,y) | A000142 | 0 | unresolved |
| H2019-25-05 | Rows one and three have two cited candidate identifications. | y=1 and y=3 separately | A153229, A058006 | 0 | unresolved |
| H2019-25-06 | Three candidate identifications are given for the next diagonal. | y=x-1 | A001563, A094258, A094304 | 0 | unresolved |

- H2019-25-01: Endpoint typo needs explicit correction before verification.

**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 26. Even double factorials

Priority: second. Source text starts at line 250.

- **nonzero-wedge**: S = `{(1,a),(1,-a):a in Z_>0}`; R = `-x<=y<=x`.

**Conventions / ambiguities.** Every asserted sequence needs its own starting coordinate and index shift.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-26-01 | The two boundary diagonals yield even double factorials. | y=x and y=-x separately | A000165 | 0 | unresolved |
| H2019-26-02 | Column totals also yield even double factorials. | sum_y P(n,y) | A000165 | 0 | unresolved |
| H2019-26-03 | The two inward neighboring diagonals have the cited identification. | y=x-1 and y=1-x separately | A014481 | 0 | unresolved |
| H2019-26-04 | Rows one and minus one have the cited identification. | y=1 and y=-1 separately | A290044 | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 27. Squared and adjacent factorial products

Priority: second. Source text starts at line 258.

- **odd-triangle**: S = `{(1,2*a-1),(1,1-2*a):a in Z_>0}`; R = `0<=y<=x`.
- **even-triangle**: S = `{(1,2*a):a in Z}`; R = `0<=y<=x`.

**Conventions / ambiguities.** Odd model has y=x mod 2. Even model has y=0 mod 2, so odd-height rows are zero. Endpoints near the origin, factorial tails, and column shifts require care.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-27-01 | Even-height rows are associated with (n!)^2. Model: `odd-triangle`. | y=2a, fixed integer a>=0; reachable x only | A001044 | 0 | unresolved |
| H2019-27-02 | Odd-height rows are associated with n!(n+1)!. Model: `odd-triangle`. | y=2a+1, fixed integer a>=0; reachable x only | A010790 | 0 | unresolved |
| H2019-27-03 | Diagonal extraction is proposed to interleave squared and adjacent factorial products. Model: `odd-triangle`. | y=x-a, a>=0; even/odd sequence index | A001044, A010790, A010551 | 0 | unresolved |
| H2019-27-04 | Column totals give the interleaved sequence. Model: `odd-triangle`. | sum_y P(n,y) | A010551 | 0 | unresolved |
| H2019-27-05 | The even-step triangle fixed rows also give the interleaved sequence. Model: `even-triangle`. | y=a, fixed integer a | A010551 | 0 | unresolved |
| H2019-27-06 | The even-step triangle column totals give the interleaved sequence. Model: `even-triangle`. | sum_y P(n,y) | A010551 | 0 | unresolved |

- H2019-27-03: Odd a gives inaccessible diagonal in odd-step model; source does not resolve this.
- H2019-27-05: Only even nonnegative a are reachable.

**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 28. Permutations of odd order

Priority: later. Source text starts at line None.

- **even-wedge**: S = `{(1,2*a):a in Z}`; R = `-x<=y<=x`.

**Conventions / ambiguities.** All odd-height rows vanish. The permutation description must be tested, not inferred from superficial initial agreement.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-28-01 | Fixed rows are associated with counts of odd-order permutations in S_n. | y=a, fixed integer a | A000246 | 0 | unresolved |
| H2019-28-02 | Column totals are associated with the same sequence. | sum_y P(n,y) | A000246 | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 29. Permutation arrays with column condition modulo 3

Priority: later. Source text starts at line 281.

- **multiple-3-triangle**: S = `{(1,3*a):a in Z}`; R = `0<=y<=x`.

**Conventions / ambiguities.** Only heights divisible by 3 are reachable. Source’s n by 1 array description uses row condition modulo 2 and column condition modulo 3; exact OEIS definition not independently retrieved.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-29-01 | Fixed nonnegative rows are associated with the titled modular permutation-array count. | y=a, fixed integer a>=0 | A264557 | 0 | unresolved |
| H2019-29-02 | Column totals are associated with the same sequence. | sum_y P(n,y) | A264557 | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 30. Permutation arrays with column condition modulo 4

Priority: later. Source text starts at line 288.

- **multiple-4-triangle**: S = `{(1,4*a):a in Z}`; R = `0<=y<=x`.

**Conventions / ambiguities.** Only heights divisible by 4 are reachable. Source’s n by 1 array description uses row condition modulo 2 and column condition modulo 4; exact OEIS definition not independently retrieved.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-30-01 | Fixed nonnegative rows are associated with the titled modular permutation-array count. | y=a, fixed integer a>=0 | A264635 | 0 | unresolved |
| H2019-30-02 | Column totals are associated with the same sequence. | sum_y P(n,y) | A264635 | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 31. Permutation arrays with column condition modulo 5

Priority: later. Source text starts at line 295.

- **multiple-5-triangle**: S = `{(1,5*a):a in Z}`; R = `0<=y<=x`.

**Conventions / ambiguities.** Only heights divisible by 5 are reachable. Source’s n by 1 array description uses row condition modulo 2 and column condition modulo 5; exact OEIS definition not independently retrieved.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-31-01 | Fixed nonnegative rows are associated with the titled modular permutation-array count. | y=a, fixed integer a>=0 | A264656 | 0 | unresolved |
| H2019-31-02 | Column totals are associated with the same sequence. | sum_y P(n,y) | A264656 | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 32. Permutation arrays with column condition modulo 6

Priority: later. Source text starts at line 302.

- **multiple-6-triangle**: S = `{(1,6*a):a in Z}`; R = `0<=y<=x`.

**Conventions / ambiguities.** Only heights divisible by 6 are reachable. Source’s n by 1 array description uses row condition modulo 2 and column condition modulo 6; exact OEIS definition not independently retrieved.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-32-01 | Fixed nonnegative rows are associated with the titled modular permutation-array count. | y=a, fixed integer a>=0 | A264701 | 0 | unresolved |
| H2019-32-02 | Column totals are associated with the same sequence. | sum_y P(n,y) | A264701 | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 33. Unit vertical progress

Priority: later. Source text starts at line 309.

- **nonnegative-horizontal**: S = `{(a,1):a in Z_>=0}`; R = `Z^2 (no boundary stated)`.
- **positive-horizontal**: S = `{(a,1):a in Z_>0}`; R = `Z^2 (no boundary stated)`.

**Conventions / ambiguities.** The parenthetic positive-increment alternative has different offsets and support. Pairing horizontal and vertical slices does not imply equal indexing.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-33-01 | The paired fixed row and fixed column are associated with a simplex-number sequence. Model: `nonnegative-horizontal`. | y=3 and x=2 separately | A000217 | 0 | unresolved |
| H2019-33-02 | The paired fixed row and fixed column are associated with a simplex-number sequence. Model: `positive-horizontal`. | y=3 and x=2 separately | A000217 | 0 | unresolved |
| H2019-33-03 | The paired fixed row and fixed column are associated with a simplex-number sequence. Model: `nonnegative-horizontal`. | y=4 and x=3 separately | A000292 | 0 | unresolved |
| H2019-33-04 | The paired fixed row and fixed column are associated with a simplex-number sequence. Model: `positive-horizontal`. | y=4 and x=3 separately | A000292 | 0 | unresolved |
| H2019-33-05 | The paired fixed row and fixed column are associated with a simplex-number sequence. Model: `nonnegative-horizontal`. | y=5 and x=4 separately | A000332 | 0 | unresolved |
| H2019-33-06 | The paired fixed row and fixed column are associated with a simplex-number sequence. Model: `positive-horizontal`. | y=5 and x=4 separately | A000332 | 0 | unresolved |
| H2019-33-07 | The paired fixed row and fixed column are associated with a simplex-number sequence. Model: `nonnegative-horizontal`. | y=6 and x=5 separately | A000389 | 0 | unresolved |
| H2019-33-08 | The paired fixed row and fixed column are associated with a simplex-number sequence. Model: `positive-horizontal`. | y=6 and x=5 separately | A000389 | 0 | unresolved |
| H2019-33-09 | The paired fixed row and fixed column are associated with a simplex-number sequence. Model: `nonnegative-horizontal`. | y=7 and x=6 separately | A000579 | 0 | unresolved |
| H2019-33-10 | The paired fixed row and fixed column are associated with a simplex-number sequence. Model: `positive-horizontal`. | y=7 and x=6 separately | A000579 | 0 | unresolved |
| H2019-33-11 | The paired fixed row and fixed column are associated with a simplex-number sequence. Model: `nonnegative-horizontal`. | y=8 and x=7 separately | A000580 | 0 | unresolved |
| H2019-33-12 | The paired fixed row and fixed column are associated with a simplex-number sequence. Model: `positive-horizontal`. | y=8 and x=7 separately | A000580 | 0 | unresolved |
| H2019-33-13 | The paired fixed row and fixed column are associated with a simplex-number sequence. Model: `nonnegative-horizontal`. | y=9 and x=8 separately | A000581 | 0 | unresolved |
| H2019-33-14 | The paired fixed row and fixed column are associated with a simplex-number sequence. Model: `positive-horizontal`. | y=9 and x=8 separately | A000581 | 0 | unresolved |
| H2019-33-15 | The paired fixed row and fixed column are associated with a simplex-number sequence. Model: `nonnegative-horizontal`. | y=10 and x=9 separately | A000582 | 0 | unresolved |
| H2019-33-16 | The paired fixed row and fixed column are associated with a simplex-number sequence. Model: `positive-horizontal`. | y=10 and x=9 separately | A000582 | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 34. Horizontal progress and unit up/down increments

Priority: later. Source text starts at line 321.

- **positive-x-unit-y**: S = `{(a,1),(a,-1):a in Z_>0}`; R = `Z^2 (no boundary stated)`.

**Conventions / ambiguities.** Heading says a>=0 but body says a>0. Including a=0 gives (0,1),(0,-1) cycles, hence infinitely many words at every reachable endpoint. Inventory adopts body model and flags incompatible heading.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-34-01 | The whole count array may match a cited triangle. | Full array, ordering unspecified | A025177 | 0 | unresolved |
| H2019-34-02 | Symmetric rows have the cited candidate identification. | y=+1 and y=-1 separately | A025179 | 0 | unresolved |
| H2019-34-03 | Symmetric rows have the cited candidate identification. | y=+2 and y=-2 separately | A025180 | 0 | unresolved |
| H2019-34-04 | Symmetric rows have the cited candidate identification. | y=+3 and y=-3 separately | A025181 | 0 | unresolved |
| H2019-34-05 | The author expects the row family to continue. | General fixed y=+k and y=-k, k>=1 | — | 0 | unresolved |
| H2019-34-06 | Near-boundary diagonals have the cited candidate identification. | y=x-2 and y=-x+2 separately | A000124 | 0 | unresolved |
| H2019-34-07 | Near-boundary diagonals have the cited candidate identification. | y=x-3 and y=-x+3 separately | A000292 | 0 | unresolved |
| H2019-34-08 | Near-boundary diagonals have the cited candidate identification. | y=x-4 and y=-x+4 separately | A086274 | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 35. Quadratic diagonal counts

Priority: later. Source text starts at line 337.

- **infinite-unit-y-plus-flat**: S = `{(a,1),(a,-1):a in Z_>0} union {(1,0)}`; R = `Z^2 (no boundary stated)`.
- **finite-as-written**: S = `{(1,0),(1,1),(2,1),(3,1),(1,-1),(1,-2),(1,-3)}`; R = `Z^2 (no boundary stated)`.
- **finite-cubic**: S = `{(1,0),(1,1),(2,1),(3,1),(4,1),(1,-1)}`; R = `Z^2 (no boundary stated)`.

**Conventions / ambiguities.** Finite alternative as printed is not symmetric under y reflection. Raw PDF text confirms cubic coefficient 4/3 (layout extraction garbles it).

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-35-01 | The two named diagonals are associated with a(n)=2*n^2+1. Model: `infinite-unit-y-plus-flat`. | y=x-2 and y=-x+2 separately | A058331 | 0 | unresolved |
| H2019-35-02 | The two named diagonals are associated with a(n)=2*n^2+1. Model: `finite-as-written`. | y=x-2 and y=-x+2 separately | A058331 | 0 | unresolved |
| H2019-35-03 | A cubic formula (4/3)*x^3-2*x^2+(11/3)*x-1 is tentatively suggested. Model: `finite-cubic`. | y=x-3, variable x as printed | — | 0 | unresolved |

- H2019-35-01: Variable n may be shifted from x; finite model must be independently checked on both diagonals.
- H2019-35-02: Variable n may be shifted from x; finite model must be independently checked on both diagonals.

**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 36. Branches in ordered trees

Priority: later. Source text starts at line 344.

- **arbitrary-x-three-y**: S = `{(a,0),(a,1),(a,-1):a in Z_>0}`; R = `Z^2 (no boundary stated)`.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-36-01 | Axis counts are associated with total branches in ordered trees. | y=0 | A051924 | 0 | unresolved |
| H2019-36-02 | The two neighboring rows have the cited identification. | y=+1 and y=-1 separately | A076540 | 0 | unresolved |
| H2019-36-03 | The two near-boundary diagonals have the cited identification. | y=x-2 and y=-x+2 separately | A084849 | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 37. Vertical upstep plus three horizontal-progress types

Priority: later. Source text starts at line 351.

- **vertical-plus-three-y**: S = `{(0,1)} union {(a,0),(a,1),(a,-1):a in Z_>0}`; R = `Z^2 (no boundary stated)`.

**Conventions / ambiguities.** The model is not invariant under y reflection; y=+1 and y=-1 equality cannot be presumed. Whole-array ordering absent. Each fixed endpoint has finitely many paths despite an unbounded positive vertical step.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-37-01 | The full count array may match a cited triangle. | Full array, ordering unspecified | A054120 | 0 | unresolved |
| H2019-37-02 | Axis counts have the cited identification. | y=0 | A054122 | 0 | unresolved |
| H2019-37-03 | Rows of heights plus/minus one are given the same candidate identification. | y=+1 and y=-1 separately | A052392 | 0 | unresolved |
| H2019-37-04 | A fixed column has the cited identification. | x=3, y increasing | A054121 | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 38. First differences of central Delannoy numbers

Priority: later. Source text starts at line 360.

- **vertical-plus-two-y**: S = `{(0,1)} union {(a,1),(a,-1):a in Z_>0}`; R = `Z^2 (no boundary stated)`.

**Conventions / ambiguities.** The step set is not symmetric under y reflection. Header references A001850, while the claimed difference sequence is A110170; offsets need checking.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-38-01 | Axis counts are associated with first differences of central Delannoy numbers. | y=0 | A110170, A001850 | 0 | unresolved |
| H2019-38-02 | Rows plus/minus one have the same cited candidate identification. | y=+1 and y=-1 separately | A104550 | 0 | unresolved |
| H2019-38-03 | A fixed column has the cited identification. | x=2, y increasing | A005893 | 0 | unresolved |

- H2019-38-01: A001850 names the parent sequence, not an asserted equal counting sequence.

**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 39. Vertical upstep with horizontal or northeast progress

Priority: later. Source text starts at line 367.

- **vertical-plus-nonnegative-y**: S = `{(0,1)} union {(a,0),(a,1):a in Z_>0}`; R = `Z^2 (no boundary stated)`.

**Conventions / ambiguities.** Support is the nonnegative quadrant without a separately stated constraint; all slice offsets remain to be checked.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-39-01 | A fixed row has the cited identification. | y=1 | A001792 | 0 | unresolved |
| H2019-39-02 | A fixed row has the cited identification. | y=2 | A001793 | 0 | unresolved |
| H2019-39-03 | A fixed row has the cited identification. | y=3 | A001794 | 0 | unresolved |
| H2019-39-04 | A fixed row has the cited identification. | y=4 | A006974 | 0 | unresolved |
| H2019-39-05 | A fixed row has the cited identification. | y=5 | A006975 | 0 | unresolved |
| H2019-39-06 | A fixed row has the cited identification. | y=6 | A006976 | 0 | unresolved |
| H2019-39-07 | A fixed row has the cited identification. | y=7 | A209404 | 0 | unresolved |
| H2019-39-08 | A fixed column has the cited identification. | x=2, y increasing | A001105 | 0 | unresolved |
| H2019-39-09 | A fixed column has the cited identification. | x=3, y increasing | A002492 | 0 | unresolved |
| H2019-39-10 | A fixed column has the cited identification. | x=4, y increasing | A072819 | 0 | unresolved |
| H2019-39-11 | A diagonal may match the cited sequence. | y=x+2 | A275827 | 0 | unresolved |
| H2019-39-12 | Antidiagonal totals form an unidentified sequence. | sum over x+y=a, fixed integer a | — | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 40. Symmetric variable-length positive increments

Priority: later. Source text starts at line None.

- **positive-L**: S = `{(1,a),(a,1):a in Z_>0}`; R = `Z^2 (no boundary stated)`.
- **positive-L-below**: S = `{(1,a),(a,1):a in Z_>0}`; R = `y<=x`.

**Conventions / ambiguities.** The repeated vector (1,1) is one step, not two colors. Several slash-separated OEIS alternatives are tentative; array linearization and slice offsets are unspecified.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-40-01 | The unrestricted diagonal may match the cited sequence. Model: `positive-L`. | y=x | A171155 | 0 | unresolved |
| H2019-40-02 | The unrestricted paired row/column has several candidate matches. Model: `positive-L`. | y=3 and x=3 separately | A022856, A089071, A152948, A133263 | 0 | unresolved |
| H2019-40-03 | The unrestricted full array may match a cited triangle. Model: `positive-L`. | Full array, ordering unspecified | A047080 | 0 | unresolved |
| H2019-40-04 | The boundary-restricted diagonal has three candidate matches. Model: `positive-L-below`. | y=x | A082582, A086581, A025242 | 0 | unresolved |
| H2019-40-05 | A restricted row has two candidate matches. Model: `positive-L-below`. | y=3 | A000124, A152947 | 0 | unresolved |
| H2019-40-06 | Another restricted row has the cited candidate match. Model: `positive-L-below`. | y=4 | A177787 | 0 | unresolved |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.

## 41. Calculated values

Priority: later. Source text starts at line 396.

- **table-1**: S = `{(1,1),(0,-2)}`; R = `y>=0`.
- **table-2**: S = `{(1,1),(0,-3)}`; R = `y>=0`.
- **table-3**: S = `{(1,1),(0,-4)}`; R = `y>=0`.
- **table-4**: S = `{(1,1)} union {(1,-2k):k>0}`; R = `y>=0`.
- **table-5**: S = `{(1,1)} union {(0,1-2k):k>0}`; R = `y>=0`.
- **table-6**: S = `{(1,1)} union {(1,-k):k>0}`; R = `y>=0`.
- **table-7**: S = `{(1,-1)} union {(1,k):k>0}`; R = `y>=0`.
- **table-8**: S = `{(1,1)} union {(0,-k):k>0}`; R = `y>=0`.
- **table-9**: S = `{(1,1)} union {(0,-2k):k>0}`; R = `y>=0`.
- **table-10**: S = `{(1,1)} union {(0,-3k):k>0}`; R = `y>=0`.

**Conventions / ambiguities.** Ten printed arrays supply computational evidence only. The source does not specify a machine-readable table or algorithm version. This inventory has read every table caption and displayed array, but does not claim independent reproduction.

| Claim | Statement | Extraction | Source OEIS | Verified terms | Status |
|---|---|---|---|---:|---|
| H2019-41-01 | Table 1 prints endpoint counts for the model of section 17. Model: `table-1`. | Finite printed endpoint array | — | 0 | source context |
| H2019-41-02 | Table 2 prints endpoint counts for the model of section 17. Model: `table-2`. | Finite printed endpoint array | — | 0 | source context |
| H2019-41-03 | Table 3 prints endpoint counts for the model of section 17. Model: `table-3`. | Finite printed endpoint array | — | 0 | source context |
| H2019-41-04 | Table 4 prints endpoint counts for the model of section 18. Model: `table-4`. | Finite printed endpoint array | — | 0 | source context |
| H2019-41-05 | Table 5 prints endpoint counts for the model of section 19. Model: `table-5`. | Finite printed endpoint array | — | 0 | source context |
| H2019-41-06 | Table 6 prints endpoint counts for the model of section 20. Model: `table-6`. | Finite printed endpoint array | — | 0 | source context |
| H2019-41-07 | Table 7 prints endpoint counts for the model of section 20. Model: `table-7`. | Finite printed endpoint array | — | 0 | source context |
| H2019-41-08 | Table 8 prints endpoint counts for the model of section 21. Model: `table-8`. | Finite printed endpoint array | — | 0 | source context |
| H2019-41-09 | Table 9 prints endpoint counts for the model of section 22. Model: `table-9`. | Finite printed endpoint array | — | 0 | source context |
| H2019-41-10 | Table 10 prints endpoint counts for the model of section 23. Model: `table-10`. | Finite printed endpoint array | — | 0 | source context |


**Literature / generalization.** Source-only attribution so far. Compare the displayed models via their finite predecessor sets, transfer operators, and coefficient extractions; search exact OEIS definitions before assigning a combinatorial interpretation. Factorial families receive priority in the separate audit.
