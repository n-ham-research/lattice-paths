# Counterexample review

Date: 16 October 2026. Reviewer: Codex subagent `/root/east_ham`, acting as the counterexample reviewer in a separate review pass. Exact model version was not exposed. This agent also previously inspected East–Ham literature and the original algorithms; this is therefore an independent reasoning pass and role, not an independent human expert or external peer review. No proof-review audit was read before recording these findings.

## Material and scope

Read `paper/main.tex`, all included sections, `research/foundation.md`, `experiments/lattice_paths.py`, `experiments/sequences.py`, and `experiments/tests/test_paths.py`. Attacked the six unit-horizontal constructions, the generic layer lemmas, initial indices, forbidden residues, empty layers, zero counts, arbitrary topological placement of the origin, and duplicate height inputs. Findings refer to the initial review snapshot; subsequent corrections should be logged below.

## Mathematical findings

No counterexample was found to the manuscript's six **qualified** model statements or either layer principle.

* n=0: all six models have exactly one empty path at height zero. The products and column-total formulae give one. The alternating-factorial endpoint statement correctly starts at n=1 and treats P_0(0)=1 separately; A_0=0 must not replace that origin count.
* The triangle with all integer increments has P_n(y)=n! and total (n+1)!, not total n!.
* The odd-increment cone has the same endpoint counts only on y≡n (mod 2). The wedge endpoint y=n−1 is always zero, so unqualified diagonal-factorial claims fail. This exclusion is already recorded in the manuscript.
* Deleting the increment zero does not preserve constant indegree at every target: newly introduced extreme heights have one additional predecessor compared with old heights. Constant **outdegree** gives the asserted totals. Cone column two is (2,1,2,1,2), disproving endpoint uniformity. The manuscript handles this distinction correctly.
* Nonzero-increment boundary formulae need n≥1: the displayed factors involving (n−1)! are invalid expressions at n=0. The manuscript has the necessary range. The cone boundary count corresponds to (2n−2)!!, while its total is (2n)!!.
* In the triangle parity models, odd increments force y≡n (mod 2), and even increments force even y. Thus odd rows in the even model and the diagonal y=n−1 in the odd model give explicit zero counterexamples to unqualified source wording. Both qualified models give B_n at reachable endpoints and B_(n+1) as the total.
* Empty intermediate layers do not invalidate the layer lemmas. For predecessor regularity, a later nonempty layer immediately after an empty one necessarily has d_j=0; its count and product vanish. Choices of d_j on an empty target layer are vacuous but any later nonempty layer restores the zero factor. For successor regularity, the first empty target layer after a nonempty layer forces e_j=0; later vacuous parameters cannot revive a zero total. Zero predecessor counts likewise propagate correctly. The requirement V_0={o} prevents an empty initial layer.
* Simplicity and edges exclusively between consecutive layers are material assumptions: parallel edges would require multiplicities in the degree count, and skip edges would add paths absent from the product. They are stated.

## Actual independent computation

A temporary harness at `/tmp/lattice_countercheck.py` enumerated entire Cartesian products of the allowed column-height sets, then tested adjacent differences. This differs structurally from both recursive explicit generation and dynamic programming. For **all six models and every column 0 through 6**, endpoint dictionaries agreed with `unit_columns`. There were 159 explicit endpoint formula assertions, and every column total was checked against its claimed independent factorial/product expression. All passed. The harness was run with `python3`; an initial attempt using the unavailable `python` executable did not execute any checks.

These finite checks attempt falsification and do not prove the general formulae. The proofs were scrutinised separately against the structural arguments above. No experimental claim beyond these exact ranges is made by this review.

## Implementation finding requiring correction

**Duplicate heights cause disagreement between the two counting interfaces.** The callback

```python
heights = lambda x: [0] if x == 0 else [0, 0]
```

with every vertical difference allowed gives `unit_columns(1, heights, allowed)[-1] == {0: 1}`, but `list(explicit_paths(1, heights, allowed)) == [(0, 0), (0, 0)]`. The explicit generator counts the same geometric word twice while the dictionary-based DP collapses duplicate targets. This violates the project's no-multiplicity convention unless callbacks are required and checked to return distinct heights. The six built-in models use duplicate-free ranges and are unaffected. Recommended fix: validate distinct heights consistently in both APIs (and document that requirement), or deduplicate in both. Add one targeted regression check for the chosen behavior.

The generic DAG interface already rejects repeated vertices. It accepts a topological list in which the start has incoming edges, but this is **not a bug**: every vertex before the start retains count zero, so it contributes no additional path to the start. An actual check on vertices [(-1,0),(0,0),(1,0)] with unit-right edges returned counts 0,1,1. No preceding vertex can be reachable from the start without a rejected backward edge. Rejecting origin incoming edges is unnecessary for the documented paths-from-start semantics.

## Disposition

Mathematical manuscript: no falsification found within the stated scope. Experimental engine: resolve duplicate-height inconsistency before describing the generic interfaces as mutually validating on arbitrary supported callbacks. No novelty conclusion follows from this review.
