# Independent generalization review

Date: 16 October 2026 (Australia/Melbourne). Reviewer: Codex subagent `/root/inventory`, delegated generalization reviewer. Exact underlying model version was not exposed. This is an internal AI-assisted mathematical review, not external peer review. The reviewer read `research/foundation.md` and all manuscript section files before reading any other review; no other review was consulted in producing these findings.

## Verdict and scope

The two layer principles and all six distinct proved step-set models are mathematically sound under the stated conventions. No blocking defect was found. The manuscript appropriately separates these elementary consequences from the unresolved residue-class programme and makes no novelty claim. Its strongest useful structural distinction is between uniform indegree (endpoint products) and uniform outdegree (total products). The nonzero-increment families illustrate why those hypotheses cannot be conflated.

I independently reconstructed the layer inductions, the complete-column reachability arguments, the forbidden-zero subtraction, and the parity products. In particular, a fixed row can start at a factorial tail, and column totals can differ by an index shift; the manuscript does not claim equality without these qualifications. The origin exceptions are explicit.

## Weakest assumptions and safe extensions

1. **Completeness is unnecessary.** Constant indegree alone preserves a uniform previous endpoint count. This is already correctly stated. More generally, for a particular previous count vector p, uniformity in the next layer means exactly that the adjacency matrix times p is constant. Regular indegree is sufficient, and necessary when p is a nonzero constant vector; it is not necessary for arbitrary nonuniform p. Thus a classification of all multiplicative sequences should distinguish structural regularity from accidental equality along one trajectory.

2. **Finite ambient layers can be weakened, but the present assumption is useful.** The endpoint-product induction needs only finite indegrees d_j and a singleton initial layer, even if an ambient layer is infinite. The total-product statement needs a finite initial reachable set and finite outdegrees e_j; then finitely many reachable endpoints occur at each finite depth. There is no need to complicate the manuscript with these extensions unless an application uses them.

3. **Multiple initial states require a specified initial weight.** Uniform initial count c would multiply each endpoint product by c. An arbitrary initial count vector needs the full transfer operator. The present singleton start avoids a hidden initialization problem.

4. **Block transfer is the natural next framework.** If every vertex in a target block has the same number of predecessors in each source block, count-per-vertex vectors evolve by a finite matrix. This is the equitable-partition mechanism already proposed in the notes. A worthwhile theorem would characterize translation-defined step sets and changing boundary windows for which a bounded number of residue blocks suffices, or prove a genuinely useful converse. Merely restating matrix multiplication would not be a substantive new result.

5. **Weights and parallel steps are possible but change the counted objects.** Uniform weighted incoming sums would give weighted products. A multigraph counts different edges as distinct choices. The present simple-graph and set-of-displacements assumptions correctly prevent the repeated vector (1,1) in a union from being counted twice.

## Residue extension checked independently

For step set `{(1,q*a):a in Z}` in `0<=y<=x`, q a positive integer, the reached heights in column n are exactly the multiples of q in `[0,n]`. Every such target has every reached predecessor. Therefore the common endpoint count is

`product_{j=1}^n (floor((j-1)/q)+1) = (m!)^q (m+1)^s`, where `n=q*m+s`, `0<=s<q`.

This candidate statement in the foundation notes follows directly from the proved complete-layer principle. I independently checked the endpoint recurrence against this formula for all q=1,...,5 and n=0,...,12: 65 columns, including every integer height in each window and the zero counts at inaccessible residues. This temporary check was written directly from predecessor congruence and did not import the project's engine. It checks a candidate extension, not 65 independent terms of any historical OEIS claim; the source inventory's verified-term fields remain zero.

For a general coset `a+q*Z`, possible heights in column n have residue `n*a mod q`. Any two consecutive feasible residue layers connect completely. However, a geometrically nonempty later residue slice need not be reachable if an earlier slice was empty. Example: q=3, a=2 in the triangle has no endpoint in column 1, but the congruence slice in column 2 contains height 1. All actual column-2 path counts are still zero. A future theorem must require all preceding feasible layers to be nonempty or explicitly retain the zero product after extinction. The notes already warn about early empty layers; keep that warning when formalizing the extension.

## Limits and priorities

The source inventory contains many claims outside the proved six models. This review does not certify any unexamined Catalan, permutation-order, or modular-array identification. The source §28 permutation interpretation especially needs independent scrutiny rather than inference from its first few values. No new sequence identification or external literature result is introduced by this review.

The immediate promising extension is a precise moving-window/coset classification, accompanied by a literature search for known factorial-product enumerations and equitable path-counting constructions. Existing monoid finiteness theory helps justify that counts exist; it does not by itself give these boundary-dependent product enumerations. The elementary product theorem and the qZ extension should be described as explanatory foundations unless a substantive new classification survives literature review.
