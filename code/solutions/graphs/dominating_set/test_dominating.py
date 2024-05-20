import networkx as nx
from networkx.algorithms.dominating import is_dominating_set
from termcolor import colored


def test_dominating(
    nodes: list[int],
    edges_list: list[list[int]],
    selected_nodes: list[int],
) -> None:
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges_list)
    if is_dominating_set(G, selected_nodes):
        print(
            colored("selected set of nodes is a dominating set", "blue", attrs=["bold"])
        )
    else:
        print(
            colored(
                "selected set of nodes is not a dominating set",
                "yellow",
                attrs=["bold"],
            )
        )
