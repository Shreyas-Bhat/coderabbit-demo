from src.analytics import unique_stable, zscore

def test_unique_stable():
    data = ["a", "b", "a", "c", "b", "d"]
    assert unique_stable(data) == ["a", "b", "c", "d"]

def test_zscore_zero_variance():
    assert zscore([3, 3, 3]) == [0, 0, 0]

def test_zscore_len():
    v = [1.0, 2.0, 3.0]
    zs = zscore(v)
    assert len(zs) == len(v)
