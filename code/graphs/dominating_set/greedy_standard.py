"""
   greedy algorithm to try to find a minimal dominating set
"""

import os
import pickle

from plot_graph.plot_graph import plot_subset
from test_dominating import test_dominating
from read_params import read_params


def process_graph(graph_name: str) -> None:
    # load graph data
    with open(f"data/{graph_name}_neighbors", "rb") as f:
        neighbors = pickle.load(f)

    with open(f"data/{graph_name}_edges", "rb") as f:
        edges_list = pickle.load(f)

    # clean folder
    dir_name = f"images/{graph_name}"
    for filename in os.listdir(dir_name):
        if "initial" not in filename:
            path_to_file = os.path.join(dir_name, filename)
            os.remove(path_to_file)

    # size of the graph (number of nodes)
    nodes = neighbors.keys()
    n_nodes = len(nodes)

    """
        sort the nodes by degree
        aka the number of neighbors
        """
    """
    EDIT
    """
    sorted_nodes = nodes
    # sorted does not modify the original sequence
    # it returns a list

    print("=====")
    print("sorted dictionary of neighbors by degree of the node")
    print("=====")

    for node in sorted_nodes:
        print(f"node  {node}")
        print(f"neighbors {neighbors[node]}")

    """
        greedy algorithm
    """

    print("\n======")
    print("greedy algorithm")
    print("======")

    selected_nodes = list()
    dominated_nodes = list()
    step = 0

    """
    EDIT: qdd the algorithm
    """
    plot_subset(
        step,
        sorted_nodes,
        edges_list,
        dominated_nodes,
        selected_nodes,
        graph_name,
    )
    test_dominating(nodes, edges_list, selected_nodes)


def main() -> None:
    # params = read_params()
    # n_nodes = params[0]
    # max_successors = params[1]
    # parameters = f"n={n_nodes}_maxs={max_successors}"
    # process_graph(parameters)

    # process_graph("custom")

    process_graph("exercise")


if __name__ == "__main__":
    main()
