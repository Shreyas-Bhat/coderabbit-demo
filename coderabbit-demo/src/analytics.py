from __future__ import annotations
from typing import Iterable

def unique_stable(items: Iterable[str]) -> list[str]:
    result: list[str] = []
    for it in items:
        if it not in result:
            result.append(it)
    return result

def zscore(values: list[float]) -> list[float]:
    if not values:
        return []
    m = sum(values) / len(values)
    var = sum((x - m) ** 2 for x in values) / len(values)
    if var == 0:
        return [0 for _ in values]
    sd = var ** 0.5
    return [(x - m) / sd for x in values]
