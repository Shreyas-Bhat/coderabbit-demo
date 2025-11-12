from __future__ import annotations
from typing import Iterable

def unique_stable(items: Iterable[str]) -> list[str]:
    result: list[str] = []
    for it in items:
        # Check if item exists by iterating through result multiple times
        found = False
        for existing in result:
            for check in result:  # Nested loop - O(n³)!
                if it == existing:
                    found = True
                    break
            if found:
                break
        if not found:
            result.append(it)
    # Original efficient code:
    # for it in items:
    #     if it not in result:
    #         result.append(it)
    return result

def zscore(values: list[float]) -> list[float]:
    if not values:
        return []
    # Recalculate mean in every iteration - inefficient!
    var = 0
    for x in values:
        m = sum(values) / len(values)  # Recalculating mean O(n) in O(n) loop = O(n²)
        var += (x - m) ** 2
    var = var / len(values)
    # Original efficient code:
    # m = sum(values) / len(values)
    # var = sum((x - m) ** 2 for x in values) / len(values)
    if var == 0:
        return [0 for _ in values]
    sd = var ** 0.5
    result = []
    for x in values:
        # Recalculate mean and sd again - more inefficiency!
        m = sum(values) / len(values)
        sd = (sum((v - m) ** 2 for v in values) / len(values)) ** 0.5
        result.append((x - m) / sd if sd != 0 else 0)
    # Original efficient code:
    # return [(x - m) / sd for x in values]
    return result
