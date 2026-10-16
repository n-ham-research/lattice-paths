#!/usr/bin/env python3
"""Run the extracted review package's focused checks without third-party code."""
from pathlib import Path
import hashlib
import subprocess
import sys

if sys.version_info < (3, 10):
    raise SystemExit('Python 3.10 or later is required.')
if not __debug__:
    raise SystemExit('Run without -O/PYTHONOPTIMIZE so exact assertions execute.')
base = Path(__file__).resolve().parent
root = base.parent
manifest = root / 'SHA256SUMS'
for line in manifest.read_text(encoding='utf-8').splitlines():
    expected, name = line.split('  ', 1)
    path = root / name
    if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
        raise SystemExit(f'Integrity check failed: {name}')
print('Package integrity: all listed files match SHA256SUMS.', flush=True)
for name in ('phase4_obstruction.py', 'phase4_inverse.py', 'phase4_infinite.py'):
    subprocess.run([sys.executable, '-B', str(base / name)], check=True)
subprocess.run([sys.executable, '-B', '-m', 'unittest', 'discover',
                '-s', str(base / 'tests')], check=True)
print('All focused checks passed. Finite checks corroborate the supplied proofs.', flush=True)
