"""
Functions used for the greedy matching algorithm
"""
import networkx as nx

from matching_greedy.plots import show_matching
from matching_greedy.test_matching import test_matching


def match_greedy(
        G: nx.Graph,
        graph_name: str,
        graph_type: str,
        ) -> None:
    edges_list = G.edges
    nodes = G.nodes
    """
    Apply greedy algorithm on the generated graph.
    EDIT: add the algorithm
    """
    print("\n======")
    print("greedy algorithm")
    print("======")
    index = 1
    matched_nodes = list()
    matching = list()
    show_matching(
            nodes=nodes,
            edges_list=edges_list,
            matching=matching,
            index=index,
            graph_name=graph_name,
            graph_type=graph_type,
            )

    print(f"number of nodes in matching: {2*len(matching)}")
    # quick test
    if len(matching) * 2 == len(matched_nodes):
        print("number of matched nodes equals 2 times size of matching : ok")
    else:
        print("inconsistent number of edges in the matching and matched nodes")

    test_matching(
            G=G,
            matching=matching,
            )
