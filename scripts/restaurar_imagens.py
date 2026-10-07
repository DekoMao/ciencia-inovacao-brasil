from pathlib import Path
import base64
root=Path(__file__).resolve().parents[1]
for p in (root/'infograficos').glob('*.png.base64'):
    target=p.with_suffix('')
    target.write_bytes(base64.b64decode(p.read_text()))
    print(target)
