"""
   Third greedy heuristic: the degree of the nodes each computed again at each
   time step.
"""


import networkx as nx

from dominating_set.plots import plot_subset
from dominating_set.test_dominating import test_dominating


def greedy_ter(
    G: nx.Graph,
    graph_name: str,
    graph_type: str,
) -> None:
    neighbors = nx.to_dict_of_lists(G)
    edges_list = G.edges
    nodes = G.nodes
    n_nodes = len(nodes)

    """
    EDIT: add the algorithm
    """

    selected_nodes = list()
    dominated_nodes = set()
    step = 0


    plot_subset(
        step=step,
        edges=edges_list,
        dominated_nodes=dominated_nodes,
        selected_nodes=selected_nodes,
        graph_name=graph_name,
        graph_type=graph_type,
        method="ter"
    )
    test_dominating(
        G=G,
        selected_nodes=selected_nodes,
        method="ter",
    )
