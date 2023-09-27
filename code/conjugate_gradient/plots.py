"""
Plot the benchmarking results
"""

import os
from sre_constants import IN

import matplotlib.pyplot as plt
import xarray as xa

from speed_benchmarks.config import INPUTS_TYPE, LINEAR_TERM_RANGE, N_REPEATS, SIGMA, INPUTS_TYPE
from utils.utils import clean_filename, create_folder_if_missing, load_pickle


def plot_results_one_variable_one_n(
    n: int,
    scikit_data: xa.DataArray,
    cg_data: xa.DataArray,
    axs,
) -> None:
    d_list = cg_data.coords["d"].data
    axs[0].plot(d_list, scikit_data, linestyle="dashed", marker="o", label=f"n={n}")
    axs[1].plot(d_list, cg_data, linestyle="dashed", marker="o", label=f"n={n}")


def plot_results_one_variable(variable: str) -> None:
    # laod data
    folder = os.path.join("speed_benchmarks", "results")
    scikit_path = os.path.join(folder, f"{variable}_scikit_sigma_{SIGMA}")
    cg_path = os.path.join(folder, f"{variable}_cg_sigma_{SIGMA}")
    scikit_path = f"{clean_filename(scikit_path)}.pickle"
    cg_path = f"{clean_filename(cg_path)}.pickle"

    scikit_data = load_pickle(scikit_path)
    cg_data = load_pickle(cg_path)

    fig, axs = plt.subplots(1, 2)

    n_list = cg_data.coords["n"].data
    for n in n_list:
        scikit_data_n = scikit_data.sel(dict(n=n))
        cg_data_n = cg_data.sel(dict(n=n))
        plot_results_one_variable_one_n(
            n=n, scikit_data=scikit_data_n, cg_data=cg_data_n, axs=axs
        )

    fig_title = (
        "Comparison between scikit and cg\n"
        "Resolution of OLS\n"
        f"{N_REPEATS} repeats per simulation\n"
        r"$\sigma=$"
        f"{SIGMA:.2E}\n"
    )
    if INPUTS_TYPE == "uniform":
        fig_title += (
                f"{INPUTS_TYPE} inputs"
                r"$\in$"
                f"[-{LINEAR_TERM_RANGE}, {LINEAR_TERM_RANGE}]\n"
                )
    else:
        fig_title += f"{INPUTS_TYPE} inputs\n"

    if variable == "computation_times":
        y_label = "Computation time (s)"
        fig_title += "Computation time (s)"
    elif variable == "mses":
        y_label = "test MSE"
        fig_title += "test MSE"
    else:
        raise ValueError("Unknown variable")

    # set figure
    axs[0].set_title("scikit")
    axs[0].set_xlabel("dimensionality (d)")
    axs[0].legend(loc="best")
    axs[0].set_ylabel(y_label)

    axs[1].set_title("cg")
    axs[1].legend(loc="best")
    axs[1].set_xlabel("dimensionality (d)")
    axs[1].set_ylabel(y_label)

    axs[0].set_yscale("log")
    axs[1].set_yscale("log")

    fig.suptitle(fig_title, fontsize=10)

    plt.tight_layout()

    # save
    folder = os.path.join("speed_benchmarks", "images")
    fig_name = f"{variable}_sigma_{SIGMA}_{INPUTS_TYPE}_inputs"
    fig_name = clean_filename(fig_name)

    # pdf
    fig_name_pdf = f"{fig_name}.pdf"
    fig_path_pdf = os.path.join(folder, fig_name_pdf)
    plt.savefig(fig_path_pdf)

    # png
    fig_name_png = f"{fig_name}.png"
    png_folder = os.path.join(folder, "png")
    create_folder_if_missing(png_folder)
    fig_path_png = os.path.join(png_folder, fig_name_png)
    plt.savefig(fig_path_png)


def plot_results() -> None:
    variables = ["computation_times", "mses"]
    for variable in variables:
        plot_results_one_variable(variable=variable)
