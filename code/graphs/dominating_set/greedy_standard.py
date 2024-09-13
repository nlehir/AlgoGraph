"""
   greedy algorithm to try to find a minimal dominating set

   Degree based heuristic:
       - nodes are sorted by degree
       - then added sequentially to the selected set
       (that will be the final dominating set) if they
       are not already dominated.
"""

import networkx as nx

from dominating_set.plots import plot_subset
from dominating_set.test_dominating import test_dominating


def greedy_standard(
    G: nx.Graph,
    graph_name: str,
    graph_type: str,
) -> None:
    neighbors = nx.to_dict_of_lists(G)
    edges_list = G.edges
    nodes = G.nodes
    n_nodes = len(nodes)

    """
    EDIT:
        sort the nodes by degree
        aka the number of neighbors
        """

    selected_nodes = list()
    dominated_nodes = set()
    step = 0

    """
    EDIT: add the algorithm
    """
    plot_subset(
        step=step,
        edges=edges_list,
        dominated_nodes=dominated_nodes,
        selected_nodes=selected_nodes,
        graph_name=graph_name,
        graph_type=graph_type,
    )
    test_dominating(
        G=G,
        selected_nodes=selected_nodes,
        method="standard",
    )
