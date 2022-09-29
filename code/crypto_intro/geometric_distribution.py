"""
    geometric distribution
"""

import math
import numpy as np
import matplotlib.pyplot as plt

total_nb_keys = math.factorial(26)
stopping_keys = math.factorial(20)

p = stopping_keys / total_nb_keys
print(p)
q = 1 - p


def cumulative_distribution_function(k):
    return 1 - pow(q, k)


nb_steps = 100
nmax = 1e8
step = nmax / nb_steps
x_step = np.arange(1, nmax, step)
y_values = cumulative_distribution_function(x_step)

plt.plot(x_step, y_values)
plt.title(f"cumulative distribution function p={p:0.2e}")
plt.ylabel("probability of finding key before number of attempts")
plt.xlabel("number of attempts")
plt.savefig("cumulative distribution function.pdf")
