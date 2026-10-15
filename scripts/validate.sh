#!/usr/bin/env bash
set -euo pipefail
root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"
python3 scripts/check_inventory.py
python3 -m unittest discover -s experiments/tests
python3 -m experiments.verify --check
python3 -m experiments.table_audit
python3 -m experiments.phase2_classification
python3 -m experiments.trajectory_inverse
python3 -m experiments.phase3_geometry
python3 -m experiments.phase4_obstruction
python3 -m experiments.phase4_inverse
python3 -m experiments.phase4_infinite
./scripts/build.sh
