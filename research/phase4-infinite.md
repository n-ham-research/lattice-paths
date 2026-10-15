# Phase 4: sharp small-modulus actual-trajectory converses

16 October 2026. Derived by actual internal agent `/root/infinite4`. These are focused results for moduli two and three, not a solution of the general-q problem. Historical priority is unresolved; no novelty claim. The exact calculations below are proofs, whereas the committed checks are supporting evidence. Independent adversarial review is requested separately.

## Conventions

At layer n the allowed vertices are (n,y), 0≤y≤n. Start at (0,0), empty word weight one. A jump is (1,d), d∈Z, with a time-independent weight f(d); the weight of a path is the product of its jump weights and all vertices must lie in the allowed triangle. Distinct jumps are not multiplicities. Infinite support is allowed: each finite endpoint sum is finite. Set

    p_n(y)=Σ_{z=0}^{n−1} p_{n−1}(z)f(y−z).

A row is 2-uniform when p_n(y)=p_n(y+2) whenever both endpoints exist. The visible difference window through N is W_N=[1−N,N]∩Z. All counts in this note are exact ordinary real/rational sums, not positive-characteristic reductions.

## Theorem: compressed uniformity identifies the kernel in modulus two

Suppose f:Z→R_{≥0}, f(0)=f(1)=t>0, and N≥6. If the actual rows through N are 2-uniform, then

    f(d)=t for every d∈W_N.

Consequently, if all actual rows are 2-uniform, then f is constant on all of Z. The full labelled endpoint values beyond row one are unnecessary for this conclusion: their 2-uniformity flags suffice under the specified coefficient and initial-weight assumptions. This is stronger than full-data uniqueness alone and links compressed residue regularity with inverse enumeration.

The optimal initial horizon is:

| Coefficients, with f(0)=f(1)=t>0 | Sufficient N | Optimality |
|---|---:|---|
| Nonnegative real weights | 6 | An irrational positive prefix survives through 5 |
| Nonnegative rational weights | 5 | A rational nonconstant prefix survives through 4 |
| Indicator weights, 0,1∈D (t=1) | 3 | D={0,1} survives through 2 |

In each row, “sufficient N” means that uniformity through N identifies f on W_N, and for every later N uniformity through N identifies W_N. “Optimality” is for this exact finite-prefix statement. The counterexamples below have finite support but are used only as finite prefixes, never as infinite-support/all-horizon counterexamples. For indicators, the all-horizon conclusion is D=Z, the only 2-periodic step set containing both zero and one.

### Proof: normalization and forced first four rows

Divide the kernel by t; each n-step count is divided by t^n, preserving uniformity. Thus assume f(0)=f(1)=1. Set x=f(−1). Row two has values

    (1+x, 2, 1+f(2)).

Its 2-uniformity forces f(2)=x. Nonnegativity gives x≥0. Write u=x+1>0. The interior row-three values at heights 1 and 2 are both

    C=x²+2x+3=u²+2>0.

The two boundary comparisons then force

    f(−2)=f(3)=c=(x²−x+2)/(x+1).

Thus row three is constant, equal to C. At row four the even interior count is 2uC, while both odd counts equal (2+x+c)C. Equality of each even boundary with the even interior forces

    f(−3)=f(4)=a=(3x−1)/(x+1).

These are the full row-four constraints; no untested interior condition is omitted.

At row five, compare heights 1 and 3. They involve only already determined weights. Taking row-four even value A=2uC and odd value B=(2+x+c)C, subtraction gives

    p_5(1)−p_5(3)
      = A(a−c)+B(c−x)
      = C[c²−(4x+2)c+x²+2x+2]
      = −2C (x−1)²(x²+2x−1)/(x+1)².

Hence 2-uniformity through five forces x=1 or x=√2−1; the other quadratic root is negative. Over rational weights only x=1 is possible. If x=1, then c=a=1, so all weights on W_4 equal one; the row-five boundary comparisons force its two new weights to equal one too.

### The exceptional real branch is excluded at six

Write s=√2. The branch x=s−1 has

    c=3s−3,    a=3−2s.

The first five rows can indeed be 2-uniform. Their even/odd common values are:

| n | Even height value | Odd height value |
|---:|---:|---:|
| 1 | 1 | 1 |
| 2 | s | 2 |
| 3 | 4 | 4 |
| 4 | 8s | 16s−8 |
| 5 | 96−32s | 96−32s |

At row five, the middle value is 96−32s and the bottom count before adding the new jump f(−4) is 24s. The coefficient of f(−4) is 8s. Thus

    f(−4)=f(5)=b=6s−7.

Reflection symmetry f(d)=f(1−d) guarantees reflected endpoint counts, so both extremes have the same forced value. Direct substitution in the recurrence verifies the entire table, including both row-five parity classes, not only the single interior equation used above.

Row five is scalar, with positive common value T=96−32s. Consequently, at row six,

    p_6(2)/T = x+1+1+x+c+a = 3s,
    p_6(0)/T = 1+x+c+a+b+f(−5) = 8s−7+f(−5).

Uniformity forces f(−5)=7−5s<0, contradicting nonnegativity (50>49). Hence the exceptional real branch is impossible through six. This proves x=1 and constancy through W_5; row six then determines its new boundary weights as one.

### Propagation to every later horizon

Once f=1 on W_m for m≥3, the actual endpoint rows through m are the same as those for the all-one kernel: p_n(y)=n!. For the next row all interior heights 1,…,m use only known weights, hence have count (m+1)!. Each of the two boundary heights has an interior height of the same parity, since m+1≥4. Uniformity therefore makes both new boundary counts (m+1)!; the corresponding pivot m! is nonzero, and each new extreme weight must equal one. Induction gives the finite and infinite conclusions. Undo the normalization to recover f=t. ∎

### Shorter indicator proof

For indicator weights, row two gives f(−1)=f(2)=x∈{0,1}. If x=0, then row three requires f(−2)=f(3)=2, impossible. Hence x=1, and row three forces f(−2)=f(3)=1. Propagate as above. Thus the all-horizon infinite-support indicator converse is solved here for q=2 under 0,1∈D, not just for q=1. No positivity assumption about later endpoints is separately needed: zero and one jumps already provide it.

## Sharp counterexamples and their exact scope

**Indicators, horizon two.** D={0,1} gives p_2=(1,2,1), which is 2-uniform, while its visible kernel on W_2 is not 2-periodic. It fails at row three.

**Rational weights, horizon four.** Take f(0)=f(1)=1 and

    f(−1)=f(2)=1/2,
    f(−2)=f(3)=7/6,
    f(−3)=f(4)=1/3,

and zero elsewhere. All these weights are nonnegative. The displayed first-four-row formulas prove 2-uniformity through four, with every endpoint strictly positive. The row-five interior obstruction is nonzero, independently of the two new weights. Thus no nonnegative extension can preserve row-five uniformity.

**Real weights, horizon five.** Take the symmetric kernel on W_5 specified by the exceptional branch above and zero elsewhere. All listed weights are strictly positive: s−1>0, 3s−3>0, 3−2s>0 and 6s−7>0. The table proves strict positivity and 2-uniformity through five. Every continuation satisfying row-six uniformity would need a negative weight. Thus positivity of every finite observed endpoint does not shorten the real horizon from six to five.

These finite-prefix examples preserve the earlier warning that eventual/finite positivity must not be treated as an automatic general-q converse. They do not resolve general q≥4, unequal real initial weights, eventual rather than all-row uniformity, or layer-dependent kernels.

## A second exact indicator result: modulus three

**Theorem.** Let f=1_D with 0,1∈D. If actual rows through N≥4 are 3-uniform, then f is 3-periodic on W_N. In particular, all-horizon 3-uniformity implies that D is a union of residue classes modulo three. The only possibilities containing zero and one are D=Z or D={d:d≡0 or1 mod3}. The finite initial horizon four is optimal.

**Proof.** Write a=f(−1), b=f(2), A=f(−2), B=f(3). Row two is (1+a,2,1+b). Equality of the two endpoints at row three is

    3(a−b)+(1+b)A−(1+a)B=0.

If a=1,b=0 the left side is at least one; if a=0,b=1 it is at most minus one. Thus a=b=x. Then A=B=c since 1+x>0. Row three has values (P,Q,Q,P), where

    P=1+3x+(1+x)c,    Q=3+2x+x².

Comparing the endpoints of each repeated residue at row four gives

    f(−3)=f(4)=c+(Q/P)(1−c).

If c=0, Q/P equals 3 for x=0 and 3/2 for x=1, both impossible for indicator weights. Thus c=1, and the two new extreme weights equal one. This is precisely the 3-periodic kernel with residue values (1,1,x) throughout W_4.

For propagation, compare with its globally 3-periodic continuation. Such a kernel structurally preserves residue-constant functions by the established sliding-sum theorem, so its actual rows are 3-uniform. The two kernels agree on W_m, hence all their actual rows through m agree. At row m+1≥5, every interior endpoint uses known weights, so their interior counts agree. Each boundary has an interior endpoint in the same residue (heights three and m−2 respectively). Actual uniformity fixes both boundary counts too. The nonzero boundary pivots supplied by zero and one jumps force the next two extreme weights to agree with the periodic continuation. Induction proves the finite and infinite conclusions.

For optimality, D={0,1} has all-positive binomial rows, and through row three the only repeated residue consists of its two equal endpoints. Nevertheless f(−2)=0≠1=f(1), so the visible kernel is not 3-periodic. ∎

The propagation argument is a general bootstrap principle: an actually uniform positive-pivot prefix whose visible kernel is already q-periodic at a horizon m≥q forces q-periodicity at every later uniform row. The difficult general-q issue is establishing a periodic seed from actual uniformity. The q=5 positive nonperiodic prefix from Phase 3 shows that the structural horizon q cannot serve as a universal actual-trajectory bootstrap horizon.

## Actual contribution and source comparison boundary

This is an elementary finite calculation followed by the existing endpoint-uniqueness induction. Its potential value is the distinction between **identifiable full data** and **a very compressed regularity observation**: in this specified class, initial equal weights and parity-uniformity alone recover every observable weight. It is a genuine inverse consequence, but not claimed a new general inverse-operator theorem.

No additional primary-literature result is invoked in this proof. The existing Phase 3 primary comparison (Liu–Siemons walk matrices, Blåsten–Isozaki–Lassas–Lu discrete heat inverse problems) concerns different finite graph/source data and does not certify originality of this specialization. Specialist recognition remains preferable to treating this short calculation as a priority claim. No new original-inventory ID is resolved by this structural result.

## Executed exact checks

`python3 experiments/phase4_infinite.py` passes:

- All 16 assignments of the four binary weights on W_3 other than 0,1; the all-one assignment is the unique 2-uniform-through-three survivor.
- All 64 assignments of the six binary weights on W_4 other than 0,1; exactly two 3-uniform-through-four survivors, both 3-periodic on that window.
- 650 rational parameter instances x=k/(2d), 1≤d≤20, d≤k≤4d; duplicates are intentionally counted as parameter instances. These verify all forced rows through four and the factored interior obstruction at five.
- Independent explicit weighted words through layer five for the rational sharp example, compared against endpoint DP.
- Exact arithmetic in Q(√2) for the entire exceptional positive prefix through five and the necessarily negative next weight 7−5√2.

The first check is exhaustive on the stated binary window. The rational parameter sampling and single algebraic branch are not exhaustive real-kernel searches; the proof supplies the real quantifier.
