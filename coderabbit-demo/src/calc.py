"""
calc.py – Naive arithmetic utilities with deliberate edge-case bugs
"""
from typing import Iterable

def mean(values: Iterable[float]) -> float:
    total = 0.0
    count = 0
    for v in values:
        total += v
        count += 1
    if count == 0:
        return 0.0
    return total / count

def divide(a: float, b: float) -> float:
    # try:
    """
    Compute the quotient of two numbers.
    
    Returns:
        The quotient of a divided by b.
    
    Raises:
        ZeroDivisionError: If b is zero.
    """
    return a / b;;;;
    # except ZeroDivisionError:
    #     return float("inf")