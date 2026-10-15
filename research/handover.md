# First-session handover — 16 October 2026

## Completed infrastructure

Public repository https://github.com/n-ham-research/lattice-paths, local clone /home/nick/Repositories/n-ham-research/lattice-paths. Verified organisation exists and authenticated n-ham has active admin membership and public-repository creation permission. Repository-local Git identity matches symmetric-games: Nicholas Ham <nicholas.charles.ham@gmail.com>. Main branch, reserved-rights licence consistent with reference project, research instructions, source/review/experiment separation, build/check scripts. No unnecessary CI/dependency stack.

## Sources obtained

Ham (11 May 2019), all 11 pages/41 sections including ten numerical arrays read by inventory agent; original PDF page 5 visually checked by coordinator. East–Ham arXiv:1811.05735v3 (27 May 2021), all 36 pages including appendix read by literature agent; conventions and exact theorem map in literature-review.md. Ignored PDFs/text hashes in sources/README.md. Original GitLab code available at e470a327c0f9fa29f52cd9b287bfc132af7a6749, CC BY-SA 4.0, built and inspected; no implementation copied. Its empty-step-set algorithm2 classification is wrong; other limitations are documented.

## Inventory

All numbered sections 1–41 and 150 individually identified claims extracted into conjecture-inventory.md/json, preserving supplied OEIS IDs, definitions and ambiguities. Section 1 is context and section 41 tables, not forty-one conjecture theorems. Extraction is separate from audit: source snapshot verified_terms=0; subsequent exact scopes and corrected proof statuses are in conjecture-audit.md. Most families and all ten full arrays still need independent reproduction and literature checks.

## Established foundation

Direct proofs and three internal review roles support:

- Constant indegree gives uniform endpoint products; constant outdegree gives total products. Completeness is sufficient, unnecessary.
- All-integer triangle and odd-increment cone: endpoint n! on precise support; column total (n+1)!.
- Nonzero-increment triangle: total n!, top endpoint (n−1)!, axis alternating factorial A_(n−1) for n≥1 with exceptional empty path. Alternating-factorial result already proved by Danny Rorabaugh in OEIS A005165, 30 November 2015 (Ham conjecture 23 August 2015).
- Nonzero-increment cone: total (2n)!!, extreme endpoint (2n−2)!! for n≥1; generally nonuniform.
- Odd/even-increment triangle variants: supported endpoint B_n=⌊n/2⌋!⌈n/2⌉!, total B_(n+1).

Six exact models checked at every height through column12; explicit words independently generated through column5. Three-page LaTeX manuscript includes only these elementary foundations, with Nicholas Ham as sole author and explicit prior attribution/no-novelty scope.

## Counterexamples and ambiguities

Odd-step diagonals with incompatible parity are zero; even-step odd horizontal rows are zero. Column totals have distinct shifts. §25 writes (0,n+1) while calling this the x-axis; correct intended endpoint is (n+1,0). §34 a=0 in heading would introduce cycles, unlike its positive-a actual definition. §35 alternative finite set is asymmetric. Many earlier sections omit endpoint extraction and zero conventions. Full details in conjecture-audit.md and inventory. No universal statement is rescued by silently dropping inaccessible points.

## Promising generalizations

Residue multiples qZ yield endpoint (m!)^q(m+1)^s for n=qm+s; independently checked q=1..5 through column12, kept in notes until source comparison. Nonzero jumps on nested finite height sets give products and alternating sums; append/remove signed involution derived in proof-review notes, pending further audit. Block predecessor regularity is a transfer-matrix principle; novelty would need a substantial classification or additional combinatorial insight. General coset layers may become extinct despite geometrically feasible later points.

## Recommended next investigation

Complete targeted OEIS/history checks for secondary §25–27 rows, inspect removed East–Ham v1 examples/algorithms, then formulate a precise residue/boundary classification and seek existing equitable-partition/transfer-matrix results. Reproduce original tables using proved finite domains before broader Catalan claims. No improved factorial algorithm has emerged: symmetry compression is ordinary sequential multiplication. Do not prioritize benchmarking yet.

## Validation and review

Five unittest methods pass; results.json regenerates exactly; inventory checker confirms 41 sections/150 distinct claims; latexmk/BibTeX succeeds, no unresolved references/citations or overfull boxes. All three final rendered pages visually inspected. A clean export was tested without source caches/build products (see final validation below). See reviews/review-log.md and research/ai-contributions.md for actual agent identities, contexts, one-off vs committed checks and limitations. No human sign-off, external peer review or novelty certification.

## Remaining boundaries

A credible initial foundation is complete, not the entire research programme. No James East contact; no assumed collaboration; no arXiv/journal submission. Journal/disclosure policies remain to be checked at submission. Manuscript licensing remains reserved. Main .tex project is multi-file and builds locally; native editor/compile tools were not exposed in this session.

## Final validation

Clean staged-file export to a new /tmp directory contained no .local source cache or pre-existing paper/build tree. Inventory validation, all five unittest methods, exact evidence regeneration check and a from-scratch latexmk/BibTeX build all passed there. The local final PDF has three pages and no overfull-box or unresolved-reference warning. Tracked files contain no downloaded PDFs or external algorithm source. Commit history on main identifies the published milestone.
