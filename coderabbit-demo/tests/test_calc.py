import pytest
from src.calc import mean, divide

def test_mean_basic():
    assert mean([1, 2, 3]) == 2

def test_mean_empty_iterable_behaviour():
    assert mean([]) == 0.0

def test_divide_basic():
    assert divide(10, 2) == 5

def test_divide_zero_division():
    assert divide(1, 0) == float("inf")
