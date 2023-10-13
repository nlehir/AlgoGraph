"""
   greedy algorithms to to find a minimal dominating set
"""

import os
import pickle

from read_params import read_params
from greedy_standard import greedy_standard
from greedy_bis import greedy_bis
from greedy_ter import greedy_ter


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


    greedy_standard(
            neighbors=neighbors,
            edges_list=edges_list,
            graph_name=graph_name,
            )

    # greedy_bis(
    #         neighbors=neighbors,
    #         edges_list=edges_list,
    #         graph_name=graph_name,
    #         )

    # greedy_ter(
    #         neighbors=neighbors,
    #         edges_list=edges_list,
    #         graph_name=graph_name,
    #         )


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
