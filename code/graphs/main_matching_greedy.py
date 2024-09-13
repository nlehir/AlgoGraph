"""
   Greedy algorithm to to find a maximal matching
   in a generated graph.
"""

from dominating_set.plots import plot_initial_graph
from matching_greedy.greedy_matching import match_greedy
from params import GRAPH_TYPE, PARAMS
from utils import clean_folder, define_graph


def main() -> None:
    graph_dict = define_graph(
        graph_type=GRAPH_TYPE,
        params=PARAMS,
    )
    G = graph_dict["G"]
    graph_name = graph_dict["graph_name"]

    clean_folder(
        graph_name=graph_name,
        problem="matching_greedy",
    )
    plot_initial_graph(
        G=G,
        graph_name=graph_name,
        graph_type=GRAPH_TYPE,
    )

    match_greedy(
        G=G,
        graph_name=graph_name,
        graph_type=GRAPH_TYPE,
    )


if __name__ == "__main__":
    main()
