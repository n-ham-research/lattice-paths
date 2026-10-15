#!/usr/bin/env python3
"""Validate structural completeness of source extraction, not mathematical truth."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'research/conjecture-inventory.json').read_text())
assert [s['number'] for s in data['sections']]==list(range(1,42))
claims=[c for s in data['sections'] for c in s['claims']]
assert len({c['id'] for c in claims})==len(claims)
for s in data['sections']:
    models={m['id'] for m in s['models']}
    for c in s['claims']:
        assert c['model'] is None or c['model'] in models, c['id']
        assert c['source_section']==s['number']
print(f"Inventory: {len(data['sections'])} sections, {len(claims)} uniquely identified claims")
ledger=json.loads((root/'research/phase2-claim-status.json').read_text())
from collections import Counter
assert {c['id'] for c in ledger['claims']}=={c['id'] for c in claims}
assert len(ledger['claims'])==len(claims)
assert dict(Counter(c['status'] for c in ledger['claims']))==ledger['summary']['by_status']
assert sum(c['investigated'] for c in ledger['claims'])==ledger['summary']['investigated']
for claim in ledger['claims']:
    for evidence in claim['evidence']:
        assert (root/evidence).is_file(), (claim['id'],evidence)
print('Cumulative claim ledger matches source IDs, evidence files and status totals')
