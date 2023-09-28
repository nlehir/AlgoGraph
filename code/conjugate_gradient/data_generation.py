"""
Data generation for OLS speed benchmarking
"""

import numpy as np

from config import LINEAR_TERM_RANGE, INPUTS_TYPE
from prng import rng


def generate_inputs(n: int, d: int) -> np.ndarray:
    if INPUTS_TYPE == "standard_normal":
        X = rng.normal(size=(n, d))
    elif INPUTS_TYPE == "binary":
        X = rng.integers(low=0, high=2, size=(n, d))
    elif INPUTS_TYPE == "minus_one":
        X = 2 * rng.integers(low=0, high=2, size=(n, d)) - 1
    elif INPUTS_TYPE == "uniform":
        X = rng.uniform(low=-LINEAR_TERM_RANGE, high=LINEAR_TERM_RANGE, size=(n, d))
    else:
        raise ValueError("Unknown input type")
    return X


def add_noise_to_y(y: np.ndarray, sigma: float) -> np.ndarray:
    n = len(y)
    noise = rng.normal(0, sigma, size=(n, 1))
    y += noise
    return y


def generate_outputs(X: np.ndarray, sigma: float) -> np.ndarray:
    d = X.shape[1]
    theta = rng.uniform(low=-LINEAR_TERM_RANGE, high=LINEAR_TERM_RANGE, size=(d, 1))
    y = X @ theta
    y = add_noise_to_y(y=y, sigma=sigma)
    return y


def generate_data(n: int, d: int, sigma: float) -> tuple:
    X = generate_inputs(n=2 * n, d=d)
    y = generate_outputs(X=X, sigma=sigma)

    X_train = X[:n]
    X_test = X[n:]
    y_train = y[:n]
    y_test = y[n:]
    return X_train, X_test, y_train, y_test
