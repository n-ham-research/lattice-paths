# Initial conjecture audit — 16 October 2026

Read alongside the complete 150-claim inventory. The inventory is a source-extraction snapshot: its zero verified-term fields deliberately remain unchanged. This ledger records subsequent proof/computational status. Model codes match experiments/lattice_paths.py. All proofs are in foundation.md and/or the manuscript; internal review files record independent checks. No novelty has been established.

| Original claim IDs | Model | Corrected established statement | Exact independent checks | Verdict / literature boundary |
|---|---|---|---|---|
| H2019-24-01..04 | 24-odd | Reachable endpoints P_n(y)=n!, y≡n mod 2, abs(y)≤n; total (n+1)!; even/odd horizontal rows sample even/odd factorial tails | Every height in columns 0..12; explicit paths 0..5 | Proved corrected support/indexing; literal all-integer diagonal assertion false |
| H2019-24-05..07 | 24-all | P_n(y)=n! for 0≤y≤n; total (n+1)! | Every height in columns 0..12; explicit paths 0..5 | Proved, factorial tails start when fixed height enters region |
| H2019-24-08; H2019-25-03..04 | 24-nonzero | P_n(n)=(n−1)! for n≥1; total n! | Top endpoints n=1..12 (12 terms); total n=0..12 (13 terms); explicit 0..5 | Proved; source's explicit top shift is correct |
| H2019-25-01 | 24-nonzero | P_(m+1)(0)=A_m, m≥0; P_0(0)=1 separate | m=0..11 (12 terms), checked against signed factorial sum; explicit columns 0..5 | Known, Rorabaugh 2015 OEIS A005165; source endpoint (0,n+1) is a typo |
| H2019-25-02 | 24-nonzero | P_n(2)=A_(n−1), n≥2 | DP recorded n=2..12 (11 terms); recurrence proof; explicit 2..5 | Proved from recurrence; OEIS A005165 definition confirmed |
| H2019-25-05..06 | 24-nonzero | Every existing row obeys P_n(y)=(n−1)!−P_(n−1)(y); rows 1,3 agree for n≥3; P_n(n−1)=(n−1)!−(n−2)!, n≥2 | All endpoint DP values recorded 0..12; reviewer recurrence derivation | Formula established; supplied alternative OEIS identifications not checked, remain unresolved |
| H2019-26-01..02 | 26-nonzero | T_n=(2n)!!; P_n(±n)=(2n−2)!! for n≥1 | Every height DP 0..12; explicit paths 0..5; top n=1..12 checked against formula | Proved; top/total shift differs |
| H2019-26-03..04 | 26-nonzero | Existing rows satisfy P_n(y)=2^(n−1)(n−1)!−P_(n−1)(y); reflection symmetry; near-top difference in foundation | All endpoint DP values recorded 0..12; reviewer derivation | Recurrence established; A014481/A290044 matches remain unchecked |
| H2019-27-01..03 | 27-odd | P_n(y)=B_n=⌊n/2⌋!⌈n/2⌉! on y≡n mod 2 in triangle; otherwise 0 | Every height DP 0..12: seven even columns, six odd; explicit 0..5 | Proved support-corrected formula; odd-offset diagonal claim false |
| H2019-27-04 | 27-odd | T_n=B_(n+1) | n=0..12 (13 terms) recorded; follows proved endpoint formula | Proved shift; A010551 formula independently checked on OEIS |
| H2019-27-05..06 | 27-even | P_n(y)=B_n on even nonnegative y≤n; total B_(n+1) | Every height DP 0..12; explicit 0..5 | Proved support-corrected formula; odd horizontal rows false literally |

For a horizontal row r, the number of verified reachable terms depends on r; no finite test validates all infinitely many rows separately. Instead, universal support and formulas are proved. Exact column data allows any tested row/diagonal to be reconstructed. `tests/test_paths.py` asserts the central formulas; secondary row recurrence derivations are mathematical evidence, not claimed extra automated formula assertions.

## Concrete counterexamples preserved

- §24 odd cone: P_1(0)=0, so diagonal y=x−1 is not factorial; positive-offset diagonals are outside the region.
- §24 complete triangle: T_1=2 while P_1(1)=1. Endpoint and total are different factorial indices.
- §25 literal endpoint (0,n+1) is unreachable for every n≥0; intended x-axis endpoint is (n+1,0). P_0(0)=1 is not A_0=0.
- §26 column 2 has counts [2,1,2,1,2] at heights −2..2: constant outdegree does not imply constant indegree or endpoint uniformity. T_2=8, P_2(2)=2.
- §27 odd triangle: P_2(1)=0 on diagonal y=x−1. Even triangle: P_1(1)=0, contradicting an all-integer fixed-row claim. T_2=2 while B_2=1.
- Original GitLab algorithm2 on the empty step set returns IPP, though the origin has just the empty word (FPP); see sources/algorithms-audit.md.

## Outstanding verification

All other original sections remain extracted/unresolved; no general claim that their tables have been reproduced. The Catalan DAG test is an engine sanity check, not a complete audit of §§14/17. Original Tables 1–10 were read and inventoried but not independently recomputed in full. Precise source-vs-corrected formulations, OEIS histories and literature priority are distinct tasks. No human author approval of proofs is recorded.

## Phase 2 superseding status ledger

The initial ledger above is retained as the first-pass record. Current cumulative claim-by-claim dispositions are in phase2-claim-status.json and summarized in handover-phase2.md. All ten source tables have now been independently reproduced (697 printed values), and multiple nonfactorial families have proofs/counterexamples. Historical attribution is expanded by East–Ham v1 Example3.14. The original extraction inventory remains unchanged.

## Phase 3 superseding status

Current phase3-claim-status.json establishes only H2019-23-01 anew, by actual primary m-packed-word definitions/formula182 and a formal generating-series proof. Cumulative58 established/answered,19 literal disproofs,61 unresolved,10 verified table claims,2 context;131 fully/partially investigated. New structural/trajectory theorems are separate research statements, not extra original claim IDs. Phase2 snapshot is retained. See handover-phase3.md for domain, novelty and review limits.

## Phase 4 disposition check

The original150 claims retain exactly their Phase3 dispositions in phase3-claim-status.json:58 established/answered,19 disproved,61 unresolved,10 verified-data,2 context;131 investigated. New obstruction, funnel inverse and small-modulus compressed theorems are separate structural research, not extra solved original IDs. No inventory or prior snapshot was rewritten. See handover-phase4.md.

## Phase 5 preservation

All original dispositions remain in phase3-claim-status.json without change:58 established/answered,19 disproved,61 unresolved,10 numerical,2 context;131 fully/partly investigated. This pass audits and prepares existing structural results for discussion. The general-q compactness reformulation is not a new original claim resolution. The broader combinatorial programme remains separate.
