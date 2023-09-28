"""
Compare scikit linear regreession and
conjugate gradient from scikpy to solve OLS

For both estimators, the estimator is computed on a train set
and its score is evaluated on a test set.
"""


from time import time

import numpy as np
from scipy.sparse.linalg import cg
from sklearn.linear_model import LinearRegression

from config import SIGMA
from data_generation import generate_data


def compute_mse(y_pred: np.ndarray, y_true: np.ndarray) -> float:
    residuals = y_pred - y_true
    n = len(residuals)
    return np.linalg.norm(residuals) / n


def profile_scikit_one_time(n: int, d: int) -> tuple:
    X_train, X_test, y_train, y_test = generate_data(n=n, d=d, sigma=SIGMA)

    # solve and time on train set
    tic = time()

    est = LinearRegression()
    est.fit(X=X_train, y=y_train)

    toc = time()
    elapsed_time = toc - tic

    # compute mse on the test set
    y_pred = est.predict(X_test)
    mse = compute_mse(y_pred=y_pred, y_true=y_test)

    return elapsed_time, mse


def profile_cg_one_time(n: int, d: int) -> tuple:
    X_train, X_test, y_train, y_test = generate_data(n=n, d=d, sigma=SIGMA)

    # solve and time on train set
    tic = time()

    A = X_train.T @ X_train
    b = X_train.T @ y_train
    theta, _ = cg(A=A, b=b)

    toc = time()
    elapsed_time = toc - tic

    # compute mse on the test set
    theta=np.reshape(a=theta, newshape=((d, 1)))
    y_pred_test = X_test @ theta
    mse = compute_mse(y_pred=y_pred_test, y_true=y_test)

    return elapsed_time, mse
