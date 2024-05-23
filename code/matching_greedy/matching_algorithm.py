"""
Functions used for the greedy matching algorithm
"""
from test_matching import test_matching
from plots import show_matching

def match_greedy(
        edges_list: list[list],
        nodes: list[int],
        dir_name: str,
        ) -> None:
    """
    Apply greedy algorithm on the generated graph.
    EDIT: add the algorithm
    """
    print("\n======")
    print("greedy algorithm")
    print("======")
    matched_nodes = list()
    matching = list()
    index = 1
    show_matching(
            nodes=nodes,
            edges_list=edges_list,
            matching=matching,
            index=index,
            dir_name=dir_name,
            )

    print(f"number of nodes in matching: {2*len(matching)}")
    # quick test
    if len(matching) * 2 == len(matched_nodes):
        print("number of matched nodes equals 2 times size of matching : ok")
    else:
        print("inconsistent number of edges in the matching and matched nodes")

    test_matching(
            nodes=nodes,
            edges_list=edges_list,
            matching=matching,
            )
