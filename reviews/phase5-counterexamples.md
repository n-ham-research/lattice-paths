# Phase 5 — independent focused counterexample and seed audit

16 October 2026. Actual internal reviewer `/root/seed5`; exact backend version unavailable. Supplied Phase5 request, AGENTS, Phase4 handover, status/audit/review history and Phase4 proof notes. Did not read another Phase5 review before this initial assessment. Shared model/context limitations apply; this is not external peer review.

## Disposition

The q=2 and q=3 statements, exceptional real branch, seed bootstrap and their stated optimality survive this review within their current hypotheses. No corrected theorem or additional small-modulus theorem is needed. Novelty remains unassessed by this mathematical audit.

## Independent calculation checks

Re-derived row two as (1+x,2,1+x), then row-three interior C=x²+2x+3 and c=(x²-x+2)/(x+1). Row four has even value 2(x+1)C and odd value (2+x+c)C; its boundary equations give a=(3x-1)/(x+1). Substituting c into the row-five interior obstruction yields -2C(x-1)²(x²+2x-1)/(x+1)². Since x≥0, only x=1 and x=√2-1 survive. The latter is irrational, so is unavailable in the rational theorem.

Independently implemented arithmetic pairs (A,B) for A+B√2 using Fraction, without importing the repository's calculation engine. Recomputed the full exceptional rows: (1,1); (√2,2,√2); scalar4; alternating8√2 and16√2-8; scalar96-32√2. The row-six comparison is 3√2=8√2-7+f(-5), forcing 7-5√2<0. All earlier listed weights are positive. This verifies the exact real counterexample through five and its failed nonnegative continuation, rather than relying on decimal approximation.

For q=3, independently subtracted the row-three endpoints to obtain 3(a-b)+(1+b)A-(1+a)B. Binary bounds exclude a≠b. Once a=b=x, equality forces A=B=c. At row four the extreme weights equal c+(Q/P)(1-c), P=1+3x+(1+x)c and Q=3+2x+x². If c=0 the value is3 or3/2, excluded by indicator weights; if c=1 it is1. This is the asserted (1,1,x) periodic seed.

Independent binary assignment enumeration, again written directly from the recurrence rather than using the committed small-modulus script, checked all16 assignments on W_3 with f0=f1=1: exactly the all-one seed survives parity uniformity. All64 assignments on W_4 give exactly two q=3 survivors, both asserted periodic masks. These checks support the algebra, not its universal proof.

The examples D={0,1} through rows2 (q2) and3 (q3) have binomial rows with the requisite repeated-endpoint equality but nonperiodic visible kernels. The rational x=1/2 example gives c=7/6,a=1/3, and its row-five obstruction is nonzero. Together with the exact irrational branch these establish only the advertised finite-prefix horizon optimalities.

## Bootstrap assumptions and boundaries

At an extension from W_m, every interior target uses known coefficients. The boundary comparison targets q and m+1-q are interior when m≥q; there is no accidental use of an absent endpoint. Repeated zero/one words make the two coefficients of the new extremes strictly positive. The q-periodic comparison kernel preserves the actual residue-constant rows, and agreement on W_m means the two models have identical full previous rows. This last step is legitimate even though observations are compressed: the kernel agreement, rather than an assumed measurement, supplies the full rows for the proof.

Retain indicator weights and 0,1 present for the q3 result, and nonnegative equal positive first-step weights for the real/rational parity result. Removing 0,1 without another condition allows D={2}, whose extinct trajectory is uniformly zero. No nonextinct replacement theorem has been proved. The new research note phase5-general-q.md records a compactness equivalence but not a solution for q≥4.

## Finite-support proof scrutiny

Read phase4-obstruction.md independently. The full core [L,n-R] has at least q vertices at n=b+1 because b≥L+R+q-2. Thus convolution is indeed available in every target residue. With nonnegative weights, a forbidden predecessor with positive source residue cannot be canceled. For positive d, the least residue representative must advance by d without an upper wrap; for d≤0 the least top distance must advance by1-d without a wrap. Both use representatives of every residue, guaranteed by b≥q-1. Choosing the support extreme with speed v forces a contradiction in ceil(q/v) transitions. The restarted initial row is arbitrary nonnegative; no origin-reachability property enters.

The single-jump sharpness example d=1-v preserves the active residue through t<ceil(q/v) because its top gap tv is below q. At the next transition a new endpoint of that residue lies above the translated support. Large b ensures a positive representative remains below and all core thresholds hold. This proves restarted-data sharpness, never origin-start sharpness. The q1 case is included (one nonzero uniform row before failure). No flaw found in this scope.

## Limits and provenance

No literature search was needed for this algebraic audit; it supplies no source-based novelty judgment. One attempted optional symbolic check found sympy unavailable; no installation was made. The actual independent arithmetic checks used Python's standard library only. No external messages sent, authorship changed, or manuscript edited by this reviewer.
