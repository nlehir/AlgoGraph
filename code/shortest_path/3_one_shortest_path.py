""""
    return one shortest path for each node.

    Dynamic programming: keep the information about all found shortests paths
    at each iteration and build from this information iteratively.
"""

from termcolor import colored

from input_graphs import G2, G, pos, pos2
from utils import highlight_path

"""
Choose the graph to process
"""
GRAPH = G2
POS = pos2
# GRAPH = G
# POS = pos


def print_one_shortest_path(
    destination: int,
    paths: dict[int, list[int]],
) -> None:
    path = paths[destination]
    print(f"one shortest path to {destination} is :")
    print(path)


def plot_one_shortest_path(destination, shortest_path):
    path_length = len(shortest_path) - 1
    title = (
        "Build one shortest path per node:\n"
        f"Path length: {path_length}\n"
        f"One shortest path from 0 to {destination}: {shortest_path}\n"
        f"Graph name: {GRAPH.name}"
    )
    fig_name = f"{GRAPH.name}_one_shortest_path_length_{path_length}_from_0_to_{destination}.pdf"
    folder = "3_one_shortest_path"
    highlight_path(
        G=GRAPH,
        path=shortest_path,
        pos=POS,
        title=title,
        fig_name=fig_name,
        folder=folder,
    )


def main():
    number_of_nodes = len(GRAPH)
    # initialize shortest path to list() for each node
    # We could initialize to None, but then linters are not happy.
    # Put the found shortest paths in a dict.
    one_shortest_path = {node: list() for node in GRAPH}
    # Initialize the shortest path to 0 (beginning of all paths)
    one_shortest_path[0] = [0]

    for path_length in range(1, number_of_nodes):
        print(
            colored(
                f"\n---\nbuild paths of length : {path_length}\n---",
                "blue",
                attrs=["bold"],
            )
        )
        for node in range(1, number_of_nodes):
            # we haven't found a shortest path to this node yet
            # In python, we can consider the boolean value
            # of any object. For instance:
            # bool(list()) will return False (empty list)
            # and bool([1]) will return True (non empty list)
            if not one_shortest_path[node]:
                # check which new shortest paths we can now build
                for neighbor in GRAPH.neighbors(node):
                    path = one_shortest_path[neighbor]
                    # there is a shortest path to this neighbor
                    # of the length we are looking for.
                    # The len() function returns the length
                    # of the python list. For instance,
                    # len([0]) = 1. But mathematically, we consider that
                    # [0] is a path of length 0.
                    if path and len(path) - 1 == path_length - 1:
                        """
                        EDIT
                        """
                        one_shortest_path[node] = path + [1]
                        print(one_shortest_path[node])

    for node in range(1, number_of_nodes):
        print_one_shortest_path(destination=node, paths=one_shortest_path)
        plot_one_shortest_path(destination=node, shortest_path=one_shortest_path[node])


if __name__ == "__main__":
    main()
