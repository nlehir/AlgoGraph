from typing import Callable
import os
import networkx as nx
import matplotlib.pyplot as plt
from matching_greedy.greedy_matching_structures import match_greedy_list_list, match_greedy_set_set, match_greedy_set_list
from utils import clean_name

"""
Gnp random graph
https://networkx.org/documentation/stable/reference/generated/networkx.generators.random_graphs.gnp_random_graph.html
"""

from collections.abc import Callable
from time import time

# number of tests per function and size list
NB_TESTS = 100
P_EDGE = 0.04


def plot_function_curve(
        func_name: str,
        func: Callable,
        n_list: list,
        ) -> None:
    print(f"\n{func_name}\n---")
    times = list()
    for n in n_list:
        print(f"   n={n}")
        times_for_n = list()
        """
        Average the computation time over random inputs
        (See later in the course for more explanations)
        """
        for test_index in range(NB_TESTS):
            if test_index % (NB_TESTS//10) == 0:
                print(f"       test {test_index}/{NB_TESTS}")
            G = nx.generators.gnp_random_graph(n, P_EDGE)
            tic = time()
            matching = func(edges_list = G.edges)
            toc = time()
            elapsed_time = toc-tic
            times_for_n.append(elapsed_time)
        average_time_for_n = sum(times_for_n)/NB_TESTS
        times.append(average_time_for_n)
    plt.plot(n_list, times, label=func_name)


def main() -> None:
    n_list = [100, 500,  1000, 1500, 2000, 2500, 3000, 3500,  4000]
    n_list = [10, 100, 1000]
    functions = dict()
    functions["match_greedy_set_set"] = match_greedy_set_set
    functions["match_greedy_list_list"] = match_greedy_list_list
    functions["match_greedy_set_list"] = match_greedy_set_list
    for func_name in functions:
        plot_function_curve(
                func_name=func_name,
                func=functions[func_name],
                n_list=n_list,
                )

    title = (
            "Speed comparison, "
            f"\naveraged over {NB_TESTS} random inputs"
            f"\nGnp graph, p={P_EDGE:.3E}"
            )
    plt.title(title)
    plt.legend(loc="best")
    plt.yscale("log")
    plt.xscale("log")
    plt.ylabel("computation time (s)")
    plt.xlabel("Number of nodes in the graph n")
    plt.tight_layout()
    fig_name = f"speed_comparison_p_{P_EDGE:.3E}"
    fig_name = clean_name(fig_name)
    fig_path = os.path.join(
            "matching_greedy",
            "images",
            f"{fig_name}.pdf",
            )
    plt.savefig(fig_path)
    plt.close("all")


if __name__ == "__main__":
    main()
