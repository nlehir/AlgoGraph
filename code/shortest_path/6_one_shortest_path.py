""""
    return one shortest path for each node.

    Dynamic programming: keep the information about all found shortests paths
    at each iteration and build from this information iteratively.
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


def print_one_shortest_path(
        destination: int,
        paths: list[list[int]],
        ) -> None:
    path = paths[destination]
    print(f"one shortest path to {destination} is :")
    print(path)


def plot_one_shortest_path(destination, shortest_path):
    path_length = len(shortest_path)-1
    title = (
            "Build all shortest paths:\n"
            f"Path length: {path_length}\n"
            f"One shortest path from 0 to {destination}: {shortest_path}\n"
            f"Graph name: {GRAPH.name}"
            )
    fig_name = f"{GRAPH.name}_one_shortest_path_length_{path_length}_from_0_to_{destination}.pdf"
    folder = "one_shortest_path"
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
    one_shortest_path = [list()] * number_of_nodes
    one_shortest_path[0] = [0]

    for step in range(1, number_of_nodes):
        print(
            colored(f"\n---\nbuild paths of length : {step}\n---", "blue", attrs=["bold"])
        )
        for node in range(1, number_of_nodes):
            # we haven't found a shortest path to this node yet
            if not one_shortest_path[node]:
                # check which new shortest paths we can now build
                for neighbor in GRAPH.neighbors(node):
                    c = one_shortest_path[neighbor]
                    if c is not None and len(c) == step:
                        """
                        EDIT
                        """
                        one_shortest_path[node] = c + [1]
                        print(one_shortest_path[node])

        
    for node in range(1, number_of_nodes):
        print_one_shortest_path(destination=node, paths=one_shortest_path)
        plot_one_shortest_path(destination=node, shortest_path=one_shortest_path[node])


if __name__ == "__main__":
    main()
