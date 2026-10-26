"""Package the unpacked Forge mod files into the downloadable jar."""
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'NTMstructure-1_12_2-2_0_2-CE.jar'
files = [ROOT / 'META-INF' / 'MANIFEST.MF', ROOT / 'mcmod.info', ROOT / 'pack.mcmeta']
for folder in ('assets', 'net'):
    files.extend(sorted(path for path in (ROOT / folder).rglob('*') if path.is_file()))

with zipfile.ZipFile(OUT, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as jar:
    for path in files:
        jar.write(path, path.relative_to(ROOT).as_posix())

with zipfile.ZipFile(OUT) as jar:
    assert jar.testzip() is None
    assert len(jar.namelist()) == len(files)
print(f'Built {OUT.name} with {len(files)} entries')
