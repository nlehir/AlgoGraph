"""
    greedy algorithm to find a minimal dominant set
"""

import os
import pickle

from matching_functions import match_greedy_list, match_greedy_set
from read_params import read_params


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
    match_greedy_list(edges_list, nodes, dir_name)
    match_greedy_set(edges_list, nodes, dir_name)


def main() -> None:
    params = read_params()
    nb_nodes = params[0]
    max_successors = params[1]
    match_graph(nb_nodes, max_successors)

if __name__ == "__main__":
    main()
