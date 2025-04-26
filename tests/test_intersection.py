import pytest
from intersect import intersection

import numpy as np


def test_basic():
    a, b = 1, 2
    phi = np.linspace(3, 10, 100)
    x1 = a * phi - b * np.sin(phi)
    y1 = a - b * np.cos(phi)

    x2 = phi
    y2 = np.sin(phi) + 2
    x, y, i, j = intersection(x1, y1, x2, y2)

    assert pytest.approx(x) == np.array([6.10765984, 8.36483107])
    assert pytest.approx(y) == np.array([1.82539714, 2.87208714])
    assert pytest.approx(i) == np.array([18.19901912, 85.79448352])
    assert pytest.approx(j) == np.array([43.95118922, 75.87403944])


def test_bug_overlapping_lines():
    """
    more info https://github.com/sukhbinder/intersection/issues/1
    """
    x1 = [0.0, 0.0, 1.0, 1.0, 1.0, 2.0, 2.0, 2.0]
    y1 = [100.0, 25.0, 25.0, 25.0, 20.0, 20.0, 20.0, 0.0]
    x2 = [0.0, 0.0, 2.0, 2.0, 2.0, 4.0, 4.0, 4.0]
    y2 = [0.0, 10.0, 10.0, 10.0, 20.0, 20.0, 20.0, 100.0]
    x, y, i, j = intersection(x1, y1, x2, y2)

    assert pytest.approx(x) == np.array([2.0, 2.0, 2.0])
    assert pytest.approx(y) == np.array([20.0, 10.0, 20.0])
