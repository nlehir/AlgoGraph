from typing import Callable
import networkx as nx
import os
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
NB_TESTS = 10

def clean_filename(name: str) -> str:
    name = name.replace(".", "_")
    name = name.replace(" ", "_")
    return name

def plot_function_curve(
        func_name: str,
        func: Callable,
        n_list: range,
        p: float,
        ) -> None:
    """
    p is the proba of the Gnp
    """
    print(f"\n  {func_name}\n---")
    times = list()
    for n in n_list:
        print(f"    n={n}")
        times_for_n = list()
        """
        Average the computation time over random inputs
        (See later in the course for more explanations)
        """
        for test_index in range(NB_TESTS):
            if test_index % (NB_TESTS//10) == 0:
                print(f"      test {test_index}/{NB_TESTS}")
            G = nx.generators.gnp_random_graph(n=n, p=p)
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


def benchmark_p(p: float) -> None:
    print(f"p: {p:.2f}\n---")
    n_list = range(100, 1800, 400)
    functions = dict()
    functions["match_greedy_set_set"] = match_greedy_set_set
    functions["match_greedy_list_list"] = match_greedy_list_list
    functions["match_greedy_set_list"] = match_greedy_set_list
    for func_name in functions:
        plot_function_curve(
                func_name=func_name,
                func=functions[func_name],
                n_list=n_list,
                p=p,
                )

    title = (
            "Speed comparison, "
            f"\naveraged over {NB_TESTS} random inputs"
            f"\nGnp graph, p={p:.2f}"
            )
    plt.title(title)
    plt.legend(loc="best")
    plt.yscale("log")
    plt.xscale("log")
    plt.ylabel("computation time (s)")
    plt.xlabel("Number of nodes in the graph n")
    fig_name = f"speed_comparison_p_{p:.2f}"
    fig_name = clean_filename(fig_name)
    fig_path = os.path.join(f"{fig_name}.pdf")
    plt.tight_layout()
    plt.savefig(fig_path)
    plt.close("all")

def main() -> None:
    p_list = [0.1, 0.2, 0.3, 0.4, 0.5]
    for p in p_list:
        benchmark_p(p=p)

if __name__ == "__main__":
    main()
