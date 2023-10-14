from typing import Callable
import networkx as nx
from networkx.algorithms.dominating import dominating_set
import matplotlib.pyplot as plt
from matching_functions_benchmark import match_greedy_list_list, match_greedy_set_set, match_greedy_set_list
from test_matching import test_matching

"""
Gnp random graph
https://networkx.org/documentation/stable/reference/generated/networkx.generators.random_graphs.gnp_random_graph.html
"""

from collections.abc import Callable
import numpy as np
from time import time

# number of tests per function and size list
NB_TESTS = 100
P_EDGE = 0.04

def clean_filename(name: str) -> str:
    name = name.replace(".", "_")
    name = name.replace(" ", "_")
    return name

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
            test_matching(
                    nodes=G.nodes,
                    edges_list=G.edges,
                    matching=list(matching),
                    )
            elapsed_time = toc-tic
            times_for_n.append(elapsed_time)
        average_time_for_n = sum(times_for_n)/NB_TESTS
        times.append(average_time_for_n)
    plt.plot(n_list, times, label=func_name)


def main() -> None:
    n_list = [100, 500,  1000, 1500, 2000, 2500, 3000, 3500,  4000]
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
    fig_name = f"speed_comparison_p_{P_EDGE:.3E}.pdf"
    fig_name = clean_filename(fig_name)
    plt.savefig(fig_name)
    plt.close("all")


if __name__ == "__main__":
    main()
