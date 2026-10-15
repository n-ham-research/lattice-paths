# Foundational derivations (2026-10-16)

Status: elementary derivations of source observations, not novelty claims. All regions are convex and impose the restriction throughout; vertices suffice because segments joining points in a convex region remain in it. Paths are finite words, start at (0,0), have dx=1, and the empty path counts once. Let P_n(y) count endpoints and T_n=sum_y P_n(y).

## Layer principles

In a simple directed layered graph with finite layers V_0={o}, edges only from V_{j-1} to V_j, and constant indegree d_j on V_j, every endpoint in V_n has product_{j=1}^n d_j paths. Induction: previous counts are uniform; sum d_j copies of their common value. This includes zero d_j, empty layers (endpoint assertion vacuous), and n=0 (empty product 1). It need not be complete bipartite.

Dually, if every vertex of V_{j-1} has e_j successors in V_j, then T_n=product e_j. Count outgoing extensions of each path; endpoint counts need not be uniform. Nonzero-step constructions use this second principle.

A finite block partition permits count-per-vertex vectors: if each vertex in block b of V_j has c_j(b,a) predecessors in block a of V_{j-1}, uniformity within each block is preserved and q_j=C_j q_{j-1}. This is a transfer-matrix observation, not a novelty claim. Row sums suffice for uniformity given a uniform previous vector; they are necessary if that common previous value is nonzero. Zero previous counts remove necessity. Seek nontrivial residue-block classifications rather than marketing this induction as new mathematics.

## Complete-layer models (§24)

All integer dy in 0<=y<=x: V_n has n+1 vertices, d_n=n, so P_n(y)=n! and T_n=(n+1)!. For fixed y>=0 begin at n=y; no shift-free statement that every row begins at 0!.

Odd dy in -x<=y<=x: reachable heights are y=-n,-n+2,...,n; all consecutive reachable layers connect completely. Again d_n=n, P_n(y)=n! on this parity class, zero elsewhere, T_n=(n+1)!. Diagonal y=n+a is reachable only for even a<=0 and n>=-a/2; horizontal y=r requires n>=|r| and n congruent r mod 2. Other diagonals are zero, not factorial sequences.

## Deleted horizontal steps (§24 third model, §25)

All nonzero dy in 0<=y<=x: a height y in column n-1 has exactly n successors in 0..n. Hence T_n=n!. The new top has every predecessor, so P_n(n)=T_{n-1}=(n-1)! for n>=1. Existing heights satisfy P_n(y)=T_{n-1}-P_{n-1}(y).

Let A_0=0 and A_m=sum_{k=1}^m (-1)^{m-k} k!. Since P_1(0)=0, induction gives P_n(0)=A_{n-1} for n>=1. P_0(0)=1 is exceptional. For an existing height r>=1, P_r(r)=(r-1)! followed by the same subtractive recurrence. Thus P_n(2)=A_{n-1} for n>=2, and P_n(3)=P_n(1) for n>=3. The top-minus-one sequence satisfies P_n(n-1)=(n-1)!-(n-2)! for n>=2.

Direct combinatorial subtraction: append the unique step to a target y to every path in the previous column except those already at y. Those excluded words would require the forbidden zero vertical increment. This explains positivity without signed objects. An append/remove sign-reversing involution for a more general nested-height model is derived in reviews/independent-initial-audit.md; its literature comparison and further independent review remain pending. Rorabaugh's 2015 OEIS A005165 proof already gives this lattice explanation.

## Double factorial (§26)

All nonzero dy in -x<=y<=x: every old endpoint has 2n successors, so T_n=2^n n!. New extrema each have P_n(±n)=T_{n-1}=2^{n-1}(n-1)! for n>=1. Existing heights obey P_n(y)=T_{n-1}-P_{n-1}(y), with P_n(-y)=P_n(y). The graph is NOT constant-indegree on all endpoints: column 2 is [2,1,2,1,2] for heights -2..2. For n>=2, P_n(n-1)=2^{n-1}(n-1)!-2^{n-2}(n-2)!. Central fixed rows follow the recurrence once introduced. These formulas explain the source's boundary and central-row observations without asserting unchecked OEIS identifications.

## Parity products (§27)

Odd dy in 0<=y<=x: reachable y congruent n mod 2. There are floor(n/2)+1 such heights, and every reachable predecessor connects to all of them. At step j, indegree is floor((j+1)/2). Thus the common endpoint count is B_n=floor(n/2)! ceil(n/2)!, with B_{2m}=(m!)^2 and B_{2m+1}=m!(m+1)!. Column totals are B_{n+1}, not B_n. Diagonal y=n-a is reachable only if a is even; a=1 is a counterexample to the literal unrestricted claim.

Even dy in the same triangle: reachable heights even only; the predecessor count is again floor((j+1)/2), giving the SAME B_n and T_n=B_{n+1}. Odd horizontal rows are zero. This establishes every actual step-set variant in §24 and §27, not just one preferred example.

## Residue extension (candidate programme)

For integer q>=1 and dy in q Z in the triangle, reachable heights are multiples of q. Complete layers give P_n(qr)=product_{j=1}^n (floor((j-1)/q)+1). If n=qm+s, 0<=s<q, this is (m!)^q (m+1)^s. Prove/verify/compare literature before manuscript promotion. For dy congruent a mod q, reachable heights satisfy y congruent na mod q; layer cardinalities depend periodically on n and the boundary. Their products may vanish if early reachable layers are empty. This encompasses parity examples and suggests a useful classification problem. The product formula itself is elementary.
