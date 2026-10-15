# Exact experiments

Python 3.10+, standard library only. Run from repository root:

```
./scripts/validate.sh
```

`lattice_paths.py` counts finite DAGs supplied in topological order, including vertical edges, and provides a unit-horizontal adapter using step-membership predicates. Infinite step sets are never enumerated: finite region vertex pairs determine relevant transitions. The caller must justify that its finite domain contains all paths to the requested endpoints; an arbitrary box truncation is not such a justification. Cyclic/infinite-count models are deliberately rejected by the DAG interface.

`explicit_paths` generates complete words independently of DP for columns 0..5. All six §24–27 models have exact DP columns 0..12 recorded in results.json and formula assertions at every height. Additional tests cover Catalan excursions with vertical steps and aggregation. These 13-column checks are not 13 terms of every shifted horizontal subsequence. No other conjecture is marked computationally reproduced by this script. Sequence finite differences are heuristic diagnostics only. No external algorithm source has been copied.

The evidence generator supports both `python3 -m experiments.verify --check` and `python3 experiments/verify.py --check` from the repository root. Validation includes all experiment suites, retained-source table checks, exhaustive residue-classification checks and the LaTeX build.

Phase2 adds explicit invertible tree/Dyck maps, direct polygon-diagonal enumeration, unrestricted composition formula checks, every printed source table value and exact residue-rigidity tests. Source arrays are retained as numeric facts, with printed labels separate from coordinate positions; no cache is required. The classification script exhausts finite indicator windows, including inaccessible/empty cases, rather than fitting sampled counting sequences. See handover-phase2.md for exact scopes and reviewers' independent one-off checks.

Phase3 adds finite-range actual-trajectory certificates, exact endpoint inversion (including signed rational weights), boundary-component equivalence, arbitrary widening funnels, full excursion profiles and direct packed-word congruence enumeration. The validation command runs all these committed scripts plus both the main paper and four-page briefing builds. See handover-phase3.md for exact domains and cautions about positive-characteristic pivots, unproved general-q cone converses, and unresolved novelty.

Phase4 adds `phase4_obstruction.py` (2040 binary origin/support/modulus cases,144 homogeneous restarted sharpness cases,12 varying-kernel cases,420 binomial exclusions), `phase4_inverse.py` (70 widening funnels,70 constant-kernel formulas,256 reflection cases,one nonlinear sparse-data example), and `phase4_infinite.py` (16 parity binary seeds,64 modulus-three binary seeds,650 rational parameter instances,independent weighted words through5 and exact Q(sqrt2) sharpness). These are exact finite corroborations; the universal statements have separate proofs. Two new unittest methods independently enumerate weighted words on a funnel with plateaus/jumps and check rejection of invalid inverse data.
