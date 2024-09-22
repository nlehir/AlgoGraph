""""
    return all shortest paths found for each node.

    In this graph, all edges have a length of 1, which simplifies the
    algorithm.

"""
from termcolor import colored

from utils import highlight_path

from input_graphs import G, pos, G2, pos2

"""
Choose the graph to process
"""
GRAPH = G2
POS = pos2
# GRAPH = G
# POS = pos


def print_all_shortest_paths(
    destination: int,
    shortest_paths: dict[int, list[list[int]]],
        ):
    print(f"the shortest paths to {destination} are")
    print(shortest_paths[destination])


def plot_all_shortest_paths(
    destination: int,
    shortest_paths: dict[int, list[list[int]]],
        ):
    shortest_paths_to_dest = shortest_paths[destination]
    nb_shortest_paths_to_dest = len(shortest_paths_to_dest)
    for index, path in enumerate(shortest_paths_to_dest):
        path_length = len(path)-1
        title = (
                f"Build all shortest paths in {GRAPH.name}\n"
                f"Path length: {path_length}\n"
                f"Shortest path {index+1}/{nb_shortest_paths_to_dest} from 0 to {destination}: {path}"
                )
        fig_name = f"{GRAPH.name}_shortest_path_length_{path_length}_index_{index}_from_0_to_{destination}.pdf"
        folder = "all_shortest_paths"
        highlight_path(
                G=GRAPH,
                path=path,
                pos=POS,
                title=title,
                fig_name=fig_name,
                folder=folder,
                )


def main():
    number_of_nodes = len(GRAPH)
    # initialize the found shortest paths to list() for each node
    # each list will be the list of all found shortest paths to this node.
    # We could initialize to None, but then linters are not happy.
    # Put all found shortest paths inside a dict.
    shortest_paths = {node: list() for node in GRAPH}
    # Initialize the shortest path to 0 (beginning of all paths)
    shortest_paths[0] = [[0]]

    for k in range(1, number_of_nodes + 1):
        print(
            colored(f"\n---\nbuild paths of length : {k}\n---", "blue", attrs=["bold"])
        )
        for node in range(1, number_of_nodes):
            if shortest_paths[node] == list():
                for neighbor in GRAPH.neighbors(node):
                    shortest_paths_to_ngbr = shortest_paths[neighbor]
                    # look if there are shortest paths to nbgr
                    if shortest_paths_to_ngbr:
                        # check the length of these shortest paths
                        # in this specific graph, they all
                        # have the same length, because all
                        # eches are of length 1
                        if (len(shortest_paths_to_ngbr[0]) == k):
                            """
                            EDIT: add lines here
                            """

if __name__ == "__main__":
    main()

