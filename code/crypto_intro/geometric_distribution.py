"""
    geometric distribution
"""

import math

import matplotlib.pyplot as plt
import numpy as np

def cumulative_distribution_function(q, k) -> float:
    return 1 - pow(q, k)

def main():
    total_nb_keys = math.factorial(26)
    stopping_keys = math.factorial(20)

    p = stopping_keys / total_nb_keys
    print(p)
    q = 1 - p

    nb_steps = 100
    nmax = 1e8
    step = nmax / nb_steps
    x_step = np.arange(1, nmax, step)
    y_values = cumulative_distribution_function(q=q, k=x_step)

    plt.plot(x_step, y_values)
    plt.title(f"cumulative distribution function p={p:0.2e}")
    plt.ylabel("probability of finding a stopping key before number of attempts")
    plt.xlabel("number of attempts")
    plt.savefig("cumulative distribution function.pdf")

if __name__ == "__main__":
    main()
