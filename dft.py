import math
import numpy as np
from scipy.stats import norm
from math import sqrt
import matplotlib.pyplot as plt


def f(p1, n):
    p0 = 0.50
    q0 = 1 - p0
    q1 = 1 - p1
    alf = 0.01
    x1 = norm.ppf(1 - (alf / 2)) * math.sqrt((p0 * q0) / (p1 * q1)) + (0.95 * n * (p0 - p1)) / math.sqrt(
        n * p1 * q1 * 0.95 * 0.05)
    x2 = norm.ppf(alf / 2) * math.sqrt((p0 * q0) / (p1 * q1)) + (0.95 * n * (p0 - p1)) / math.sqrt(
        n * p1 * q1 * 0.95 * 0.05)

    res = norm.cdf(x1) - norm.cdf(x2)
    return res


values = np.arange(0.48, 0.52, 0.001)
f_res = []
for p1 in values:
    f_res.append(f(p1, 1000))
    # print(f(p1, 1000))

res = np.array(f_res)
plt.plot(values, res)
plt.show()
