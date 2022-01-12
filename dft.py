import math

from scipy.stats import norm
from math import sqrt


def f(p1, n):
    p0 = 0.5
    q0 = 0.5
    q1 = 1 - p1
    alf = 0.01
    x1 = norm.ppf(1 - (alf / 2)) * math.sqrt((p0 * q0) / (p1 * q1)) + (0.95 * n * (p0 - p1)) / math.sqrt(
        n * p1 * q1 * 0.95 * 0.05)
    x2 = norm.ppf(alf/2) * math.sqrt((p0 * q0) / (p1 * q1)) +  (0.95 * n * (p0 - p1)) / math.sqrt(
        n * p1 * q1 * 0.95 * 0.05)

    res = norm.cdf(x1) - norm.cdf(x2)
    return res


print(f(0.53, 1000))
