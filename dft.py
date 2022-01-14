import math
import numpy as np
from scipy.stats import norm
from math import sqrt
import matplotlib.pyplot as plt


def calc_beta(p1, n):
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


def plot_values(iterations, color):
    values = np.arange(0.48, 0.52, 0.001)
    beta_values = []
    for p1 in values:
        beta_values.append(calc_beta(p1, iterations))
    beta_values = np.array(beta_values)
    plt.plot(values, beta_values, label=f"{iterations//1000}k iterations")


plot_values(1000, "b")
plot_values(10000, "r")
plot_values(100000, "g")
plt.legend(loc="upper left")
plt.xlabel("$p_1$")
plt.ylabel("$\\beta(p_1)$")
plt.show()
