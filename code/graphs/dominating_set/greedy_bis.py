"""
   second greedy algorithm to find a dominating set

   Nodes that are already dominated can still be added.
"""

from plot_graph.plot_graph import plot_subset
from test_dominating import test_dominating


def greedy_bis(
        neighbors: dict,
        edges_list: list,
        graph_name: str,
        ) -> None:
    # size of the graph (number of nodes)
    nodes = neighbors.keys()
    n_nodes = len(neighbors)

    """
        sort the nodes by degree
        aka the number of neighbors
        """
    sorted_nodes = sorted(
        neighbors, key=lambda node: len(neighbors[node]), reverse=True
    )
    # sorted does not modify the original sequence
    # it returns a list

    print("=====")
    print("sorted dictionary of neighbors by degree of the node")
    print("=====")

    for node in sorted_nodes:
        print(f"node  {node}")
        print(f"neighbors {neighbors[node]}")

    print("\n======")
    print("greedy algorithm")
    print("======")

    selected_nodes = list()
    dominated_nodes = list()
    step = 0

    """
    Add the algorithm
    """
    plot_subset(
        step,
        sorted_nodes,
        edges_list,
        dominated_nodes,
        selected_nodes,
        graph_name,
        method="bis",
    )
    test_dominating(
            nodes=list(nodes),
            edges_list=edges_list,
            selected_nodes=selected_nodes,
            )
