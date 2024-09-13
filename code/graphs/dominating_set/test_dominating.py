import networkx as nx
from networkx.algorithms.dominating import is_dominating_set
from termcolor import colored


def test_dominating(
    G: nx.Graph,
    selected_nodes: list[int],
    method: str,
) -> None:
    if is_dominating_set(G, selected_nodes):
        message = (
                f"selected set of nodes is a dominating set.\n"
                f"method: {method}\n"
                f"Dominated the graph with {len(selected_nodes)} nodes"
                )
        message = colored(message, color="blue")
        print(message)
    else:
        message = (
                f"selected set of nodes is not a dominating set.\n"
                )
        message = colored(message, color="yellow")
        print(message)
