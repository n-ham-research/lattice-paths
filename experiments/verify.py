"""Reproducible exact evidence; run --check to detect stale recorded results."""
import argparse
import json
from pathlib import Path
if __package__:
    from .lattice_paths import model, unit_columns
else:
    from lattice_paths import model, unit_columns


def evidence():
    result = {'scope': 'columns 0..12; explicit-path cross-check 0..5 in tests', 'models': {}}
    for name in ('24-all','24-odd','24-nonzero','26-nonzero','27-odd','27-even'):
        h,s = model(name)
        columns = unit_columns(12,h,s)
        result['models'][name] = {'total':[sum(c.values()) for c in columns],
                                  'bottom':[c.get(0,0) for c in columns],
                                  'top':[c.get(n,0) for n,c in enumerate(columns)],
                                  'columns': [{str(y):v for y,v in c.items()} for c in columns]}
    return json.dumps(result,indent=2)+'\n'

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    target=Path(__file__).with_name('results.json')
    if args.check:
        if target.read_text()!=evidence():
            raise SystemExit('Evidence is stale')
        print('Exact evidence agrees')
    else:
        target.write_text(evidence())
