# Intersection Of two curves in Pure numpy
[![PyPI](https://img.shields.io/pypi/v/intersection.svg)](https://pypi.org/project/intersection/)
[![Changelog](https://img.shields.io/github/v/release/sukhbinder/intersection?include_prereleases&label=changelog)](https://github.com/sukhbinder/intersection/releases)
[![Tests](https://github.com/sukhbinder/intersection/workflows/Test/badge.svg)](https://github.com/sukhbinder/intersection/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/sukhbinder/intersection/blob/main/LICENSE)


Inspired from [this](http://uk.mathworks.com/matlabcentral/fileexchange/11837-fast-and-robust-curve-intersections) matlab implementation, wrote this python implementation of how to detect intersection of two curves.


![image](https://raw.githubusercontent.com/sukhbinder/intersection/master/images/curve_intersection_python.png)


## Example usage

```python
from intersect import intersection

a, b = 1, 2
phi = np.linspace(3, 10, 100)
x1 = a*phi - b*np.sin(phi)
y1 = a - b*np.cos(phi)

x2 = phi
y2 = np.sin(phi)+2
x, y, i, j = intersection(x1, y1, x2, y2)

print(f"curves intersect at elements {i, j}, corresponding to coordinates {x,y}")
plt.plot(x1, y1, c="r")
plt.plot(x2, y2, c="g")
plt.plot(x, y, "*k")
plt.show()


```

## Install
To install

```bash

pip install intersect

```
