import networkx as nx
from networkx.algorithms.matching import is_matching
from termcolor import colored


def test_matching(
        G: nx.Graph,
        matching: list[set],
        ) -> None:
    edges_set = set()
    for edge in matching:
        edges_set.add(tuple(edge))
    if is_matching(G=G, matching=edges_set):
        message = (
            "selected of nodes is a matching\n"
            f"matching size: {len(edges_set)}"
                )
        message = colored(message, color="blue")
        print(message)
    else:
        print(
            colored(
                "selected of nodes is not a matching",
                "yellow",
                attrs=["bold"],
            )
        )
