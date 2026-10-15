# Phase 3 independent generalization review

Reviewer: internal AI agent `/root/geometry3`, 16 October 2026. Supplied context: root request naming `research/phase3-trajectories.md` and `research/phase3-combinatorics.md`; phase-2 project conventions; no other phase-3 review was read before these findings. This is internal AI review, not external peer review. Reviewer independently derived the boundary-graph/funnel results elsewhere, so is independent of the authors of these two notes but not independent of the overall project.

**Verdict: approve the precise proved statements for promotion, retaining the stated open problems and novelty limits. No mathematical blocking defect found.** One wording clarification in the profile bijection is recommended before promotion.

## Trajectory obstruction and finite bound

T1's proof is sound for arbitrary finite nonempty support with nonnegative real weights; it does not need individual endpoint positivity or positive weights on every residue. The interior bounds are correct: y≥max(0,M) and y≤n−max(0,1−m) guarantee 0≤y−d≤n−1. A block of q consecutive such positions supplies every residue. Summing the residue convolution really gives C_n=K C_(n−1), while truncating admissible extensions gives P_n≤K P_(n−1). Comparing P_n with floor((n+1)/q)C_n is valid because every residue cell has at least that many positions and every c_n(s)≥0. Cancellation of K powers is justified by K>0. No hidden reachability hypothesis occurs.

T1f's horizon also checks. B≥q−1 supplies all source residues, and B≥L+R+q−2 makes every n≥B+1 have q interior representatives. H+1=q(ceil((B+1)/q)+1), so the claimed contradiction is exact. If B+1=aq+r with 0≤r<q, H−B=q for r=0 and 2q−r otherwise; therefore H≤B+2q−1. The inclusive block contains at most 2q rows. This is a sufficient certificate, not an optimality assertion. The theorem deliberately does not cover signed weights or infinite support, and promotion should preserve those restrictions.

## Inverse data

T2's induction has exactly two unknown observable differences per new layer. The top equation isolates f(n) with coefficient p_(n−1)(0), and the bottom isolates f(1−n) with coefficient p_(n−1)(n−1). Every displayed remaining weight is already in W_(n−1), including the n=2 boundary case. Full previous endpoint rows are needed; the note correctly avoids claiming reconstruction from just two edge sequences. The argument works over a field with invertible nonzero pivots; it should not be generalized to arbitrary rings merely by saying pivots are nonzero. The unweighted condition 0,1∈D supplies nonzero pivots by valid all-zero/all-one words. The invisible-negative-jump example is valid, and the scalar q=1 consequence is correctly restricted to indicator weights and uniformity from the start. No infinite-support q>1 converse follows from these results; the note appropriately leaves it open.

## Profile and packed-word identification

The profile count is correct, including a=0 and the empty profile: the tree word has N+1 letters and sum −1; its counts are u+1 leaves and r_a degrees a+1. The first-global-minimum rotation argument gives exactly one good marked cut. Distinctness of all rotations follows because a proper repeated word would make its repetition count divide the total −1. Dividing the multinomial count by N+1 gives N!/((u+1)!∏r_a!). Polygon vertex/edge/diagonal bookkeeping also checks when a≥1.

Minor clarification: the sentence “Reverse-negate and delete the final leaf” should specify **delete the final −1 leaf of the good preorder increment word, then reverse and negate the remaining word**. This order yields the stated excursion immediately; after reversing the full word the deleted leaf is at the beginning, not the final position. This is wording ambiguity, not a defect in the enumeration.

I independently opened the primary [Novelli–Thibon arXiv v3 HTML](https://arxiv.org/html/1403.5962v3), inspected §§5.1 and 5.3, and checked (182), (184)–(186). The primary m-packed definition is exactly length mn with all multiplicities divisible by m. At x=2, expansion of ((1−z)/(1−2z))^(mn+1) gives (182), since the second binomial top is (m+1)n−k. The Lagrange derivative identity and substitution Z=(H−1)/(2H−1) are algebraically correct. Both formal series have constant term 1, and the equation determines coefficients successively, proving all coefficients equal. Source lists omit the degree-zero term; the project's inclusion of it explains the apparent extra initial 1. The (186) caution is justified: its inverse has coefficient t² equal to 1+mx, whereas (182)'s degree-two coefficient is m+x. The discrepancy disappears for m=1 but occurs generally. Do not use (186) for this identification.

This supports establishing H2019-23-01 under its exact degree convention. Equality of counts supplies no direct bijection, no positive-row interpretation, and no definition of the historical blob family; those limits must remain explicit. The profile theorem is classical and the packed-word match is an identification against an existing primary formula, not a novel enumeration.

## Executed corroboration

Ran `python3 experiments/trajectory_inverse.py`: 256 binary inverse cases, 252 finite-support certificate cases, one signed rational inverse case, one nonidentifiability comparison, and the explicit nonperiodic uniform-prefix example pass. Ran `python3 -m unittest discover -s experiments/tests -p '*refinement*'`: three tests pass. These checks corroborate rather than replace the foregoing proof review.

## Additional independent review: general growing windows

At the coordinator's subsequent request I separately read `research/phase3-growing-windows.md`, without consulting other reviews. **Verdict: approve its finite-core/width-gap theorem and stated geometric consequences.**

The core J_n=I_n∩[A_(n−1)+M,B_(n−1)+m] is exactly the set of targets with all supported predecessors admitted. Nonempty interval cores containing q consecutive integers supply every residue, including sources with unequal residue multiplicities. With every observed row having all q cells, c_n(s) is defined unambiguously. Summing the full convolution gives C_H=K^(H−B)C_B, while endpoint multiplicities lie between floor(|I_n|/q) and ceil(|I_n|/q); the displayed strict width gap therefore yields the claimed contradiction. Nonnegativity ensures C_B=0 implies that row vanishes, and a zero row remains zero. No hidden assumption of positive mass in each residue, monotone endpoints, or positive individual endpoint entries is needed.

The bounded-movement estimate can be made explicit. If |A_n−A_(n−1)|≤D_A and |B_n−B_(n−1)|≤D_B, take

    C=max(D_A,M)−min(−D_B,m) ≥ 0.

Then the displayed lower bound for the untruncated core width is exactly |I_(n−1)|−C. Even when its right side is negative the inequality for endpoint difference remains true; once it is at least q the actual intersection is nonempty with at least q integers. Width divergence therefore ensures the requisite eventual core condition.

For rounded affine endpoints with real fixed slopes a<c and bounded periodic offsets, endpoint movements are uniformly bounded (each rounding changes a real difference by at most one, while bounded offsets have bounded successive differences). Width equals (c−a)n+O(1), so it diverges. Rational cones, two-sided cones, and bounded periodic boundary offsets are thus covered. No finite-denominator property is needed. Eventual nonempty layers and an admitted initial position are correctly imposed separately; the finite theorem applies starting at any sufficiently late uniform row. In fact the extinction consequence only needs widths unbounded along a late subsequence, provided the full-predecessor cores already exist eventually; the stated stronger divergence assumption is safe.

Counterexample checks of the assumptions: bounded-width intervals {0} with f(0)=1 give a nonextinct uniform trajectory and no width gap, as stated. If cores are absent, I_n=[0,n] with support {1} has a nonextinct trajectory but is not eventually residue-uniform, so this familiar example does not contradict the theorem. Signed weights and infinite support remain explicitly excluded from the mass comparison. The triangle specialization of J_n and the at-most-2q-row bound agree with the independently checked T1f result above. No additional brute-force tests are needed for this direct generalization of the exact reviewed identity.
