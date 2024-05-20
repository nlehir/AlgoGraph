import networkx as nx
from networkx.algorithms.matching import is_matching
from termcolor import colored


def test_matching(
        nodes: list[int],
        edges_list: list[list],
        matching: list[set],
        ) -> None:
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges_list)

    edges_set = set()
    for edge in matching:
        edges_set.add(tuple(edge))
    if is_matching(G=G, matching=edges_set):
        pass
        # print(
        #     colored("selected of nodes is a matching", "blue", attrs=["bold"])
        # )
    else:
        print(
            colored(
                "selected of nodes is not a matching",
                "yellow",
                attrs=["bold"],
            )
        )
