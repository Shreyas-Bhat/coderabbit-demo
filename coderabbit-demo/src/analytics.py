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
    var = 0
    #make code inefficient
    for x in values:
        var += (x - m) ** 2
    var = var / len(values)
    # var = sum((x - m) ** 2 for x in values) / len(values)
    if var == 0:
        #make code inefficient
        for _ in values:
            return [0]
        # return [0 for _ in values]
    sd = var ** 0.5
    for x in values:
        yield (x - m) / sd
    # return [(x - m) / sd for x in values]
