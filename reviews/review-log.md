# Internal review log — 16 October 2026

Actual identities are Codex agent task paths; exact backend model/version was not exposed. Agents inherited the same model context and tools, so these are separate internal analyses with shared-model limitations, not three different AI systems, external peer review or human sign-off.

| Agent | Role and supplied context | Actual work and findings | Record |
|---|---|---|---|
| /root | Coordinator/authoring assistant; user handover, sources and later agent reports | Derived layer and six model formulas, wrote independent engine, exact tests, manuscript and audit; found known A005165 proof; inspected all rendered manuscript pages and original PDF page 5 | foundation.md, tests, manuscript |
| /root/proof_review | Proof inference reviewer; source §24–27 initially; later foundation.md and engine; coordinator separately supplied OEIS lead | Independently derived six models; DP through n=8, explicit paths through n=4; checked zero/empty layers and recurrences; independently fetched attribution; supplied nested-set extension and signed involution; flagged positive q/initial block uniformity wording | independent-initial-audit.md |
| /root/east_ham | Counterexample reviewer after independent source/code audit; manuscript/foundation/engine; instructed not to read other review first | Independent Cartesian-product enumeration through n=6, 159 endpoint assertions plus totals; tried empty layers, n=0, parity, incoming DAG-start edges. Found duplicate-height API mismatch; no mathematical falsification | counterexample-review.md |
| /root/inventory | Generalization reviewer after complete source inventory; manuscript/foundation; instructed not to read other reviews before findings | Reconstructed six proofs; independent residue DP q=1..5,n=0..12 (65 columns, all heights), identified coset extinction example; discussed weighted/block generalizations and necessary caveats | generalization-review.md |

## Disposition

All six manuscript models survive these internal checks. Source assertions remain separately corrected or unresolved. No result is claimed new. The duplicate-height defect is repaired by rejecting repeated region heights consistently in both APIs; regression test test_duplicate_region_is_rejected passes. Added q>=1 and clarified that block preservation needs initial within-block uniformity. The sign-reversing involution remains in research/review notes pending additional independent audit and literature comparison; it has not been promoted into the manuscript.

Final coordinator checks: five unittest methods pass; exact checked-in evidence matches regenerated values; inventory validator confirms 41 sections/150 unique claims; latexmk/BibTeX build succeeds with no unresolved references, citations or overfull boxes. All three rendered manuscript pages inspected after final layout change. Fresh-export checks recorded in handover.md. Agreement and finite checks are not the proof: direct inductive and extension-counting arguments are in the manuscript.

# Phase 2 review record

Date16 October2026. Exact model version not exposed. All task-path identities below are actual internal agents; no diversity of backend models or external peer review is implied.

| Agent | Initially separate task and later review | Record / findings |
|---|---|---|
| /root/classification_phase2 | Derived interval criterion/finite rigidity, inspected East–Ham v1; independently reviewed tree/Dyck proof before other reviews | phase2-proof.md; accepted maps, GFs and exact size conventions; own classification exhaustive38,220/393,216 cases |
| /root/bijections_phase2 | Derived classical tree/Dyck and later polygon maps; independently counterexample-reviewed classification, without other review text | phase2-counterexample.md;21,732 finite masks, boundary cases and independent necessity proof, no counterexample |
| /root/audit_phase2 | Remaining-family derivations/falsifications; independent generalization review of classification/tree notes, then ledger/supplementary proofs | phase2-generalization.md;996 finite masks, exact hypotheses accepted. phase2-ledger.md approves cumulative counts with source/live-OEIS caveats |
| /root/phase2_independent_proof | Fresh proof agent, given classification/tree notes and no other review findings; later polygon and manuscript transcription | phase2-independent-proof.md;5,456 masks,626 excursions, polygon recursion through e25. Caught missing present-target-cell qualifier in manuscript quotient recurrence |
| /root/bijections_phase2 | Separate focused source-array review after own initial math | phase2-tables.md: all697 numeric tokens independently spatially remapped; source page10 visually checked; exact bounds and independent words pass |
| /root | Integration and direct mathematical scrutiny of all promoted statements; supplementary contour/Riordan/algebra notes; source p40 and final manuscript visual review | Refined claims/status policy; corrected §5 provisional arithmetic terms10,25 and retained §6 nonnegative position constraint; repaired quotient qualifier and added mask regression |

Disposition: interval criterion/finite converse/infinite classification and classical tree/Dyck/polygon proofs accepted as mathematically established within precise scope. Their exact proofs, not reviewer agreement or finite checks, justify this. Source comparison identifies classical backgrounds and v1 prior results; finite-rigidity historical priority remains unresolved. Polygon coefficient parity repair stays in research notes; no OEIS edit submitted. Algebraic/involution note is standard explanatory material, not promoted as a novel theorem.

The quotient transcription defect is repaired: recurrence only for nonempty target residue cells; absent cells zero only as bookkeeping. `test_residue_quotient.py` compares all residue-union masks q1..4 through column8 against full DP. Review report records the repair independently. A further focused review approved the57 established/answered,19 literal-disproof ledger policy; this is not57 new theorems. Final validation and rendered-page scope are in handover-phase2.md.
