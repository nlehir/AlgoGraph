"""
Profile the speed of solving a linear system
(which is equivalent to OLS) for the scikit default implementation
and a conjugate gradient algorithm implementation from scipy.

https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.cg.html
"""

import os

import numpy as np
import xarray as xa

from config import N_REPEATS, SIGMA, INPUTS_TYPE
from plots import plot_results
from profile_solvers import (
    profile_cg_one_time,
    profile_scikit_one_time,
)
from utils import clean_filename, save_pickle, print_colored, create_folder_if_missing


def profile_speed_one_time(n: int, d: int, estimator: str) -> tuple:
    if estimator == "scikit":
        time, mse = profile_scikit_one_time(n=n, d=d)
    elif estimator == "cg":
        time, mse = profile_cg_one_time(n=n, d=d)
    else:
        raise ValueError("Unknown estimator")
    return time, mse


def profile_speed(n: int, d: int, estimator: str) -> tuple:
    """
    Profile the speed of the estimator

    Repeat the experiment multiple times
    and average the MSEs and computation times.
    """
    print(f"       {estimator}")
    times = np.zeros(N_REPEATS)
    mses = np.zeros(N_REPEATS)
    for index, _ in enumerate(times):
        time, mse = profile_speed_one_time(n=n, d=d, estimator=estimator)
        times[index] = time
        mses[index] = mse
    mean_time = times.mean()
    mean_mse = mses.mean()
    return mean_time, mean_mse


def main() -> None:
    # d_list = [100, 2500, 5000]
    # d_list = [10, 400, 800]
    # d_binary = [10, 100, 200, 300, 400]
    d_binary = [100, 200]
    # d_normal = [10, 500, 1000, 1500]
    # d_uniform = [10, 200, 400, 600, 800, 1000]
    # d_list = [10, 200, 300, 400, 500, 600, 700]

    d_list = d_binary

    n_list = [5000, 10000]

    print_colored(f"Input type: {INPUTS_TYPE}")
    print_colored(f"Sigma: {SIGMA}")

    # initialize data structures
    zeros = np.zeros(shape=(len(n_list), len(d_list)))
    computation_times_scikit = xa.DataArray(
        zeros.copy(), dims=("n", "d"), coords={"n": n_list, "d": d_list}
    )
    mses_scikit = xa.DataArray(
        zeros.copy(), dims=("n", "d"), coords={"n": n_list, "d": d_list}
    )
    computation_times_cg = xa.DataArray(
        zeros.copy(), dims=("n", "d"), coords={"n": n_list, "d": d_list}
    )
    mses_cg = xa.DataArray(
        zeros.copy(), dims=("n", "d"), coords={"n": n_list, "d": d_list}
    )

    # fill data structures
    for n in n_list:
        print(f"{n=}")
        for d in d_list:
            print(f"  {d=}")
            time_scikit, mse_scikit = profile_speed(n=n, d=d, estimator="scikit")
            time_cg, mse_cg = profile_speed(n=n, d=d, estimator="cg")

            computation_times_scikit.loc[dict(n=n, d=d)] = time_scikit
            computation_times_cg.loc[dict(n=n, d=d)] = time_cg

            mses_scikit.loc[dict(n=n, d=d)] = mse_scikit
            mses_cg.loc[dict(n=n, d=d)] = mse_cg

    # Save
    folder = "results"
    create_folder_if_missing("results")

    c_time_scikit_filename = f"computation_times_scikit_sigma_{SIGMA}"
    c_time_scikit_filename = f"{clean_filename(c_time_scikit_filename)}.pickle"
    save_pickle(computation_times_scikit, os.path.join(folder, c_time_scikit_filename))

    c_time_cg_filename = f"computation_times_cg_sigma_{SIGMA}"
    c_time_cg_filename = f"{clean_filename(c_time_cg_filename)}.pickle"
    save_pickle(computation_times_cg, os.path.join(folder, c_time_cg_filename))

    mse_scikit_filename = f"mses_scikit_sigma_{SIGMA}"
    mse_scikit_filename = f"{clean_filename(mse_scikit_filename)}.pickle"
    save_pickle(mses_scikit, os.path.join(folder, mse_scikit_filename))

    mse_cg_filename = f"mses_cg_sigma_{SIGMA}"
    mse_cg_filename = f"{clean_filename(mse_cg_filename)}.pickle"
    save_pickle(mses_cg, os.path.join(folder, mse_cg_filename))

    plot_results()


if __name__ == "__main__":
    main()
