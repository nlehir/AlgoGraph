"""
    greedy algorithm to find a minimal dominant set
"""

import os
import pickle

from matching_algorithm import match_greedy
from params import N_NODES, MAX_SUCCESSORS


def match_graph(nb_nodes: int, max_nb_of_successors: int) -> None:
    """
    perform a matching algorithm on the loaded graph.
    """
    graph_name = f"n={nb_nodes}_maxs={max_nb_of_successors}"

    with open(f"data/{graph_name}_nodes", "rb") as f:
        nodes = pickle.load(f)

    with open(f"data/{graph_name}_edges", "rb") as f:
        edges_list = pickle.load(f)

    dir_name = f"images/{graph_name}/"

    # create directory of necessary
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # clean directory
    for image in os.listdir(dir_name):
        if "initial" not in image:
            os.remove(dir_name + image)

    # apply greedy algorithm
    match_greedy(edges_list, nodes, dir_name)


def main() -> None:
    match_graph(nb_nodes = N_NODES, max_nb_of_successors=MAX_SUCCESSORS)

if __name__ == "__main__":
    main()
