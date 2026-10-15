# Independent phase-2 ledger and supplementary-proof review

16 October 2026. Reviewer `/root/audit_phase2`; internal AI review, no human or external sign-off. Read the complete status ledger, original inventory entries for the audited families, remaining-family and bijection notes, supplementary proofs, and polygon note. Scope: detect overclaimed statuses and verify the newly supplied derivations, not independently recheck every unexamined OEIS entry or all numeric table extraction.

## Verdict

**Approve the status policy and aggregate arithmetic, with the specific wording corrections and qualification below.** Recomputed directly from the 150 ledger records: 57 proved, 19 disproved, 62 unresolved, 10 verified-data, 2 context; 131 investigated; unresolved split 45 investigated and17 uninvestigated. Original IDs are preserved. These are cumulative statuses, not57 newly proved conjectures: the proved bucket includes the answered comparison question H2019-13-02 and supplied formula for previously unidentified totals H2019-39-12, and includes prior-pass results.

No theorem-status overclaim was found in the main claimed formulas under the ledger's explicit repaired support/extraction/index policy. The unresolved bucket appropriately retains named identifiers when only a general model formula was proved (§3; secondary §14; §§34,36,37,39; §38 secondary rows/column). H2019-37-03 and38-02 correctly remain unresolved rather than disproved because unequal counts at the same coordinate do not exclude shifted matches to the same OEIS sequence. The 19 disproved entries have concrete model/support counterexamples; repaired formulas are separately flagged rather than silently replacing literal assertions.

## Required factual cleanup

- H2019-06-03 still said binomial(N,3)+N when this review read the ledger. The nonnegative formula is binomial(N,3)+(N-2), N>=3, as correctly explained in the supplementary proof. Coordinator was already correcting this. It remains unresolved because source identifier alternatives were not disambiguated.
- The provisional remaining-family report's §5 sample terms1,0,2,3,12,30 are arithmetic transcription mistakes. Its finite sum, and the supplementary proof's corrected1,0,2,3,10,25, are correct. Coordinator informed; no further mathematical consequence follows from those two draft terms.

## OEIS naming boundary

H2019-32-02 is counted proved even though A264701 could not be fetched. Its supplied source definition (one-column permutation arrays with residues nondecreasing modulo6) does have the exact balanced-factorial count by the explicit residue-block argument. Therefore its **mathematical assertion by the supplied definition is proved**, but do not present this as an independent inspection of the A264701 entry, history or offset. The source-definition versus live-entry boundary should remain explicit. The same generic explanatory note attached to all28–32 total entries unnecessarily mentions q6 even for other q; tailoring it would improve clarity but does not alter the counts.

Similarly, §33 simplex formulas prove the mathematical simplex-number assertions; their eight named OEIS pages were not separately fetched in this pass. Their standard meanings are used, not a claimed fresh history audit. No limited negative literature search establishes novelty.

## Supplementary proofs reconstructed independently

**§5 contour proof:** On |u|=R>1 the downstep series converges, and a sufficiently small |z| makes the word geometric series uniformly convergent on the contour. Every coefficient has finite axis count. The integrand is (u-1)/(u[(u-1)-z(u²-u+1)]). Its pole at0 has residue1/(1+z). The root alpha tending1 is inside the fixed contour, the other root tends infinity, and the alpha residue is1/(2sqrt(1-2z-3z²))-1/(2(1+z)). Their sum is the stated OGF. This supplies a universal identity and validates H2019-05-01. The finite composition sum is independently correct.

**§20 Riordan:** First-return Motzkin decomposition M=1+zM+z²M² and a sequence of arches R=1/(1-z²M) give z(1+z)R²-(1+z)R+1=0. Eliminating the denominator from E=1+(zE)²/(1-zE) gives that same polynomial. Its coefficient at the linear unknown near E=1,z=0 is nonzero, so the formal solution is unique. Thus both axis realizations give Riordan counts; no explicit local Motzkin bijection is being claimed.

**§6 near top:** deficit2 can only be two flat steps; every placement is nonnegative, hence binomial(N,2). Deficit3 is three flats or one -2 jump. In the latter case that jump must occur after at least two +1 steps, giving N-2 positions. Thus corrected formula binomial(N,3)+N-2 is exact. At N=3 it gives2, agreeing with the all-flat word and UUD_2, whereas unrestricted +N would give4.

**§19 initial column:** With horizontal coordinate0 only positive odd vertical steps occur. A sequence of such increments has generating function1/(1-(z+z³+...))=(1-z²)/(1-z-z²), whose coefficients are1 at0 and F_y for y>=1. All partial heights are nonnegative automatically. This validates H2019-19-03 with its empty-word exception.

**§39 antidiagonal:** Substitute both coordinate variables=t in the step series. Vertical up contributes t, positive horizontal flats contribute t/(1-t), and positive horizontal/up contributes t²/(1-t); the total is2t/(1-t). The word series is(1-t)/(1-3t), giving1,2,6,18,... . This validates the supplied formula for H2019-39-12, without pretending that the source originally asserted that formula.

## Scope limits

The ledger's number investigated counts partial work: an exact endpoint formula can count as investigation even if an OEIS identification stays unresolved. It must not be paraphrased as131 solved claims. Numerical table verification remains verified-data rather than proved. I did not redo the table fixture mapping or source PDF spatial extraction in this review; those have their separate reviewer. Polygon proof was checked at the level of the stated dual/inverse and size bookkeeping and appears sound, but priority claims remain excluded.

## Coordinator disposition

Coordinator reported the §6-03 ledger formula corrected to binomial(N,3)+N-2, agreed to describe57 as established/answered source claims rather than new theorems or conjectures, and retained the q6 boundary that the source-described combinatorial object is proved while the live OEIS entry was not fetched. With those qualifications, the aggregate report is approved. This disposition records the coordinator's actual report rather than inventing a human sign-off.
