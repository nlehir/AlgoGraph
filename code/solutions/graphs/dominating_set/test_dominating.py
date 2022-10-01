from termcolor import colored
import networkx as nx
from networkx.algorithms.dominating import is_dominating_set


def test_dominating(nodes, edges_list, selected_nodes) -> None:
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
