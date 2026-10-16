#!/usr/bin/env python3
"""Bundle the discussion documents and standalone exact checks; no network."""
from pathlib import Path
import hashlib
import shutil
import zipfile

root = Path(__file__).resolve().parents[1]
output = root / 'external-review' / 'build'
folder = output / 'lattice-paths-review'
if folder.exists():
    shutil.rmtree(folder)
folder.mkdir(parents=True)
files = {
    'external-review/README.md': 'README.md',
    'external-review/open-questions.md': 'open-questions.md',
    'external-review/references.md': 'references.md',
    'research/phase5-proof-audit.md': 'proof-audit.md',
    'research/phase5-general-q.md': 'general-q-note.md',
    'research/phase5-novelty-ledger.md': 'novelty-assessment.md',
    'external-review/verify.py': 'verification/verify.py',
    'external-review/EXPECTED.txt': 'verification/EXPECTED.txt',
    'external-review/verification-status.md': 'verification/status.md',
    'paper/build/main.pdf': 'manuscript.pdf',
    'briefing/build/main.pdf': 'briefing.pdf',
    'LICENSE': 'LICENSE',
    'scripts/build.sh': 'source/scripts/build.sh',
    'paper/main.tex': 'source/paper/main.tex',
    'paper/preamble.tex': 'source/paper/preamble.tex',
    'paper/references.bib': 'source/paper/references.bib',
    'briefing/main.tex': 'source/briefing/main.tex',
}
for name in ('inference', 'counterexamples', 'generalization'):
    files[f'reviews/phase5-{name}.md'] = f'audit-details/{name}.md'
for name in ('phase4_obstruction.py', 'phase4_inverse.py', 'phase4_infinite.py'):
    files[f'experiments/{name}'] = f'verification/{name}'
files['experiments/tests/test_phase4_inverse.py'] = 'verification/tests/test_phase4_inverse.py'
for section in ('01-introduction', '02-preliminaries', '07-general-results',
                '08-conclusion', '09-actual-trajectories',
                '10-inverse-enumeration', '12-parity-inverse'):
    files[f'paper/sections/{section}.tex'] = f'source/paper/sections/{section}.tex'
for source, target in files.items():
    dest = folder / target
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(root / source, dest)
entries = sorted(p for p in folder.rglob('*') if p.is_file())
(folder / 'SHA256SUMS').write_text(''.join(
    f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(folder).as_posix()}\n'
    for p in entries), encoding='utf-8')
archive = output / 'lattice-paths-review.zip'
with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED) as z:
    for path in sorted(p for p in folder.rglob('*') if p.is_file()):
        info = zipfile.ZipInfo(path.relative_to(output).as_posix(), (2026, 10, 16, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        z.writestr(info, path.read_bytes())
print(f'Created {archive} ({archive.stat().st_size} bytes).')
