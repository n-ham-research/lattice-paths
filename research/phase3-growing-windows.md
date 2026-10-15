# Finite-range obstruction on general growing windows

16 October2026. Coordinator derivation extending T1's proof; independent reviews are recorded in phase3-proof.md, phase3-generalization.md and phase3-fresh-proof.md. No novelty claim. This bridges the actual-trajectory and geometric questions, and includes rational cones and bounded periodic boundary offsets.

Let I_n=[A_n,B_n]∩Z be finite nonempty integer intervals, with a specified finite nonnegative initial row (in particular the origin empty path when I_0={0}). Let f:Z→R_{>=0} have finite nonempty support S, K=sum f>0, m=min S,M=max S. The only edges are from z in I_(n−1) to y in I_n with weight f(y−z). Define the full-predecessor core

 J_n = I_n ∩ [A_(n−1)+M, B_(n−1)+m].

For y in J_n, all supported predecessors y−d lie in I_(n−1). Suppose rows B,...,H are constant per residue modulo q, each row has all q residue cells, and J_n contains q consecutive integers for B<n<=H. If

 floor(|I_H|/q) > ceil(|I_B|/q),

then row B is zero.

Proof. Write c_n(s) for the common endpoint weight in residue s and C_n=sum_s c_n(s). An interior target for each residue gives c_n(s)=sum_d f(d)c_(n−1)(s−d), hence C_n=K C_(n−1). Total weight P_n is at most K P_(n−1). If C_B>0, then

 floor(|I_H|/q) C_H <= P_H <= K^(H−B)P_B
 <= K^(H−B) ceil(|I_B|/q) C_B.

Substitute C_H=K^(H−B) C_B and cancel the positive quantity. This contradicts the strict width inequality. If C_B=0, nonnegativity makes row B zero. No path-set enumeration or asymptotic estimate is used. ∎

Consequently, if |I_n| tends to infinity and every J_n contains q consecutive integers eventually, an eventually residue-uniform actual trajectory must become extinct. Choose any sufficiently late B; unbounded eventual widths give a later H with the strict inequality, then apply the finite statement.

A convenient verifiable geometric condition is |I_n|→∞ with bounded successive endpoint movements: |A_n−A_(n−1)| and |B_n−B_(n−1)| are uniformly bounded. Indeed

 min(B_n,B_(n−1)+m) − max(A_n,A_(n−1)+M) +1
 >= |I_(n−1)| − C,

for a fixed finite C depending only on movement bounds and m,M. Thus J_n contains q consecutive integers for all sufficiently large n. This includes intervals [ceil(an+b+alpha_n),floor(cn+d+beta_n)] for rational a<c (indeed real fixed slopes), with bounded periodic perturbations alpha_n,beta_n. Such layers eventually have diverging widths and bounded endpoint movements. Restrict to horizons with nonempty layers and an admitted initial position; no monoid closure is assumed. Genuine two-sided cones are included.

This is an obstruction for finite nonnegative support and actual trajectories, **not** a structural-periodicity converse for all q>1 on rational cones. The latter remains an unresolved separate problem. For signed weights the comparisons fail; for infinite support a full-predecessor core may not exist. For bounded widths the multiplicity gap need not arise, so uniform nonextinct trajectories are possible (e.g. I_n={0},f(0)=1).

The triangle T1f is recovered by A_n=0,B_n=n: its core is [max(0,M), n−max(0,1−m)], and the same min/max multiplicity gap yields the explicit late block of at most2q rows. The general proof is a positive-kernel mass estimate rather than a novel claim based solely on rewriting geometry. Its exact prior status remains to be compared with positive operator/substochastic-kernel literature.
