import csv
from pathlib import Path
from typing import List

def read_numbers(path: str) -> List[float]:
    p = Path(path)
    rows = csv.reader(p.read_text().splitlines())
    out = []
    for r in rows:
        if not r:
            continue
        out.append(float(r[0]))
    return out

def write_numbers(path: str, values: List[float]) -> None:
    p = Path(path)
    with p.open("w") as f:
        w = csv.writer(f)
        for v in values:
            w.writerow([v])
