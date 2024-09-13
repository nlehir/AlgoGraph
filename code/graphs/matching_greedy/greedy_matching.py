"""
Functions used for the greedy matching algorithm
"""
from matching_greedy.test_matching import test_matching
from matching_greedy.plots import show_matching
import networkx as nx

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
    for edge in edges_list:
        print(edge)
        if edge[0] in matched_nodes:
            pass
        elif edge[1] in matched_nodes:
            pass
        else:
            matched_nodes += edge
            matching.append(set(edge))
            show_matching(
                    nodes=nodes,
                    edges_list=edges_list,
                    matching=matching,
                    index=index,
                    graph_name=graph_name,
                    graph_type=graph_type,
                    )
        index += 1

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
