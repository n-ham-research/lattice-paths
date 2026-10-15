# Phase 4: sharpened finite-range obstruction and its boundaries

16 October 2026. Internal AI derivation by `/root/obstruction4`, with independent parallel insight from the coordinator. These are proved research statements pending the separately logged adversarial reviews, not certified novelty. No original inventory disposition changes are claimed here.

## Model

At layer n the admitted integer heights are I_n={0,...,n}. A path starts at height 0 in layer 0; its steps are (1,d), vertex constraints hold at every layer, the empty path has weight 1, and path weights multiply. For a homogeneous nonnegative finitely supported kernel f, put S={d:f(d)>0}, m=min S, M=max S. The recurrence is p_n(y)=sum_{z=0}^{n-1}f(y-z)p_{n-1}(z). We also explicitly distinguish a restarted experiment with an arbitrary prescribed nonnegative row at a later layer b. A q-uniform row is constant on each congruence class modulo q; the common values are c_n(r).

## O4.1. A stronger finite certificate

Write L=max(0,M), R=max(0,1-m), and v=max(M,1-m)>=1. Let

    b >= max(q-1,L+R+q-2),    T=ceil(q/v).

If rows b,...,b+T are q-uniform, then row b is zero. Thus at most **ceil(q/v)+1 <= q+1 rows** suffice, improving the earlier 2q-row certificate. This applies to the actual origin trajectory and, more generally, to arbitrary nonnegative initial data in layer b. No positive lower bound on all endpoints or all residue values is assumed.

### Proof: full convolution and forbidden boundary contributions

For n>b, the full-predecessor core [L,n-R] contains at least q consecutive integers. Evaluating the recurrence at one core target of every residue gives

    c_n(s)=sum_{d in S}f(d)c_{n-1}(s-d).

At any target y in I_n, the actual recurrence is the same sum with terms having y-d outside I_{n-1} removed. Equality with the full-convolution value and nonnegativity imply that **every removed summand is zero**. In particular, a positive source residue value and a positive step weight can never produce a missing predecessor contribution at any target of the resulting residue.

Choose any positive c_b(r). First suppose d>0 belongs to S. At every subsequent uniform row the full convolution propagates positivity from residue r to residue r+d. Use the representatives r in {0,...,q-1}. If r+d>=q, the target y=(r+d) mod q has predecessor y-d=r-kq<0 for some positive integer k. Its missing summand f(d)c_{n-1}(r) would be positive, impossible. Consequently along this propagation we must have the ordinary integer representative increase by d without wrapping: r_t=r+td<=q-1. This is impossible after T_d=ceil(q/d) transitions.

If instead d<=0, let delta be the least nonnegative distance from the top of the current row to an active residue. After applying d, the top moves by 1, so its least distance must be delta+1-d, without wrapping modulo q. Indeed if delta+1-d>=q, take the largest target of the resulting residue; its predecessor exceeds n-1, creating a positive missing summand. Hence delta_t=delta_0+t(1-d)<=q-1, impossible after ceil(q/(1-d)) transitions.

Choose d=M if v=M>0, and d=m otherwise. The corresponding contradiction occurs within T=ceil(q/v) transitions. Since the selected summand is positive at every step, it cannot disappear before the contradiction. Thus no positive starting residue exists. ∎

This proof is local at the two boundaries; it avoids comparing the maximum and minimum numbers of residue representatives. It also explains why larger jumps give shorter certificates.

## O4.2. What is sharp, and what is not

For prescribed later initial rows, the certificate is sharp for every q>=1 and v>=1. Set d=1-v, S={d}, and choose b a sufficiently large multiple of q. Prescribe p_b(y)=1 exactly when y is congruent to b modulo q, otherwise zero. Let t>=0. Under the single step d, the actual row is the translated initial indicator, truncated to [0,b+t]. For

    0 <= t < ceil(q/v)

the row is q-uniform: its largest positive endpoint is b+t(1-v), whose distance from the new top b+t is tv<q, and there are no missing positive endpoints below it in that residue. At t=ceil(q/v), an additional target of that residue exists above the translated support and has zero weight, while lower targets remain positive (take b large). The row fails uniformity. All core hypotheses hold if b is large enough, for instance b=q(2q+v+2).

Thus ceil(q/v)+1 cannot be shortened uniformly over arbitrary restarted nonnegative data, even for a single-step kernel. **This is not an optimality example for the homogeneous origin trajectory.** The origin start severely restricts which initial rows can arise. The exact optimal origin-start block length for general finite supports remains open in this note.

### An exact origin-start natural restriction

If S is a nonempty subset of {0,1}, the actual origin trajectory has **no q-uniform row at n>=q+1**. Thus a single sufficiently late row already excludes that support class, and n=q+1 is sharp as a universal forbidden-row threshold.

Proof. Write a=f(0), b=f(1). When a,b>0, p_n(y)=binom(n,y)a^(n-y)b^y. At n>=q+1, equality of endpoints 0,q gives (b/a)^q=1/binom(n,q); equality at 1,q+1 gives (b/a)^q=n/binom(n,q+1). Together these require binom(n,q+1)/binom(n,q)=n, whereas the left side is (n-q)/(q+1)<n. If exactly one of a,b is positive, the only positive endpoint has another representative of its residue when n>=q, so uniformity fails. At n=q with a=b>0, the only repeated residue consists of endpoints 0,q, which have equal counts. ∎

This distinction prevents incorrectly advertising restarted-data sharpness as optimality of the original origin-start theorem.

## O4.3. Constant transition weights are unnecessary for eventual obstruction

Let f_n>=0 vary by layer, with all supports contained in one fixed finite interval [m,M]. If some f_n is zero then the row becomes zero. Otherwise K_n=sum_d f_n(d)>0. In a late uniform block with full q-point cores,

    C_n=K_n C_{n-1},    P_n<=K_n P_{n-1},

where C_n is the sum of residue values and P_n the total weight. The products of K_n cancel in the Phase 3 mass argument. Consequently the previous 2q-row finite certificate, and eventual extinction on expanding interval windows, remain valid. Homogeneity is therefore not an essential assumption of the original mass theorem.

There is a slightly sharper elementary nonhomogeneous estimate in the triangle. For an active residue at layer n define its least representative r_n and its least top distance delta_n, both in [0,q-1]. A positive chosen edge d from an active residue forces r_n+d<q and delta_n+1-d<q, by the same missing-contribution argument. Either expression may be negative, in which case reduction modulo q only increases it. Hence r_{n+1}>=r_n+d and delta_{n+1}>=delta_n+1-d. Their sum increases by at least 1 at every transition, but is at most 2q-2. Thus **2q consecutive uniform rows force zero**, with no homogeneous step choice required. This recovers the previous universal bound directly. The edge d may vary, provided a positive edge is available at every step and full cores exist.

The nonhomogeneous 2q bound is sharp over prescribed initial rows: take b divisible by q, initial indicator of residue 0, first q-1 steps d=1, then q-1 steps d=0. There are 2q-1 uniform nonzero rows, indexed t=0,...,2q-2. A next step 0 or 1 fails uniformity. Choose b>=2q so all core conditions hold. As above, this is a restarted-data example, not an origin-start example.

## Exact failures and unresolved relaxations

* **Infinite support:** f(d)=1 for every integer d gives p_n(y)=n! for every admitted endpoint. Thus finite support cannot simply be omitted. This is periodic and does not answer the infinite-support converse for q>1.
* **No common finite support envelope in the nonhomogeneous case:** f_n(d)=1 for 1-n<=d<=n gives the same n! rows, although every individual layer's support is finite. A fixed global range bound is essential to the stated eventual obstruction.
* **Bounded boundary width:** I_n={0}, f(0)=1 gives nonzero uniform rows forever. The width-growth hypothesis cannot be dropped.
* **Moving geometry:** the Phase 3 full-core/multiplicity theorem already handles growing intervals with bounded endpoint motion. The new q/v certificate uses the triangular boundary speeds 0 and 1 and is not asserted unchanged for arbitrary geometries.
* **Signed weights:** nonnegativity is essential to both proofs (a missing sum need not have zero individual terms). This alone is not a counterexample to the theorem. Exhausting {-1,0,1}-valued kernels on [-2,3], q=1,2,3 through layer 24 found no kernel with the last eight rows nonzero and uniform; that bounded search does not establish a signed theorem. A signed finite-support eventual counterexample or proof remains open here.
* **Nonconsecutive uniform rows:** the present arguments require consecutive uniform rows in order to propagate residue values. No theorem or infinite sparse-row counterexample is claimed after removing that assumption. This remains an explicit limit of this investigation.

## A useful inverse diagnostic, beyond eventual extinction

For observed nonzero uniform rows b,...,b+t under the full-core assumptions for a proposed finite support, O4.1 implies

    t < ceil(q/v).

Equivalently t*v<q whenever t>=1. Thus a block of t+1 observed uniform rows excludes every proposed nonnegative homogeneous finite kernel whose extreme outward speed v satisfies t*v>=q, provided its boundary core threshold is met. This turns the obstruction into an exclusion certificate for an inverse problem: it rejects an entire range-bounded kernel class without reconstructing any individual weights. It does not identify the true support or prove infinite periodicity from a finite observation.

In particular, two consecutive sufficiently late nonzero uniform rows force -q+2<=m<=M<=q-1. This is stronger than merely saying finite supports fail eventually: large-magnitude candidates are excluded immediately. For t=q, all finite homogeneous candidates meeting the core condition are excluded.

## Literature and novelty boundary

The targeted searches “killed random walk expanding boundary uniform distribution” and “Toeplitz positive constant eigenvector finite section boundary” did not locate an exact matching result; the unrelated hits are not mathematical evidence of novelty.

Directly inspected primary background: Gregory F. Lawler and Vlada Limic, *Random Walk: A Modern Introduction*, author-hosted PDF, <https://www.math.uchicago.edu/~lawler/srwbook.pdf>, §5.2 pp.112–114 and §12.4.1 pp.272–273. Section 5.2 formulates symmetric increment laws with independent killing; §12.4.1 represents a walk killed on exiting a fixed finite set by a substochastic restricted matrix, then obtains Perron–Frobenius asymptotics under irreducibility/aperiodicity. These are established killed-walk frameworks, whereas O4.1 concerns exact residue-uniform rows on a growing directed triangle and needs no irreducibility. The inspected passages do not state the finite q/v certificate. This limited distinction is not proof that the certificate is new or unavailable elsewhere in that book or literature. Specialist recognition remains the recommended next step.
