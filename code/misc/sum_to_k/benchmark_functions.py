"""
Compare the speeds of the various functions defined in functions.py
"""

import matplotlib.pyplot as plt
from collections.abc import Callable
import numpy as np
from time import time
from functions import (
        sum_to_k,
        sum_to_k_in,
        sum_to_k_any_generator,
        sum_to_k_islice,
        sum_to_k_set,
        sum_to_k_set_any,
        )

# number of tests per function and size list
NB_TESTS = 100
rng = np.random.default_rng()


def plot_function_curve(
        func_name: str,
        func: Callable,
        n_list: list,
        ) -> None:
    print(func_name)
    times = list()
    for n in n_list:
        # print(f"   n={n}")
        times_for_n = list()
        """
        Average the computation time over random inputs
        (See later in the course for more explanations)
        """
        lists_ = rng.integers(
                low=0,
                high=10,
                size=(NB_TESTS, n),
                )
        ks = rng.integers(low=0, high = 20, size=NB_TESTS)
        for index in range(NB_TESTS):
            list_= lists_[index].tolist()
            k = ks[index]
            tic = time()
            func(list_=list_, k=k)
            toc = time()
            elapsed_time = toc-tic
            times_for_n.append(elapsed_time)
        average_time_for_n = sum(times_for_n)/NB_TESTS
        times.append(average_time_for_n)
    plt.plot(n_list, times, label=func_name)


def main() -> None:
    n_list = [10, 100, 1000, 10000]
    functions = dict()
    functions["sum_to_k"] = sum_to_k
    functions["sum_to_k_in"] = sum_to_k_in
    functions["sum_to_k_any_generator"] = sum_to_k_any_generator
    functions["sum_to_k_islice"] = sum_to_k_islice
    functions["sum_to_k_set"] = sum_to_k_set
    functions["sum_to_k_set_any"] = sum_to_k_set_any
    for func_name in functions:
        plot_function_curve(
                func_name=func_name,
                func=functions[func_name],
                n_list=n_list,
                )

    title = (
            "Speed comparison, "
            f"\naveraged over {NB_TESTS} random inputs"
            )
    plt.title(title)
    plt.legend(loc="best")
    plt.yscale("log")
    plt.xscale("log")
    plt.ylabel("computation time (s)")
    plt.xlabel("list size n")
    fig_name = "speed_comparison.pdf"
    plt.savefig(fig_name)
    plt.close("all")



if __name__ == "__main__":
    main()
