"""
   Greedy algorithms to to find a minimal dominating set
   in a generated graph.
"""

from dominating_set.greedy_standard import greedy_standard
from dominating_set.greedy_bis import greedy_bis
from dominating_set.greedy_ter import greedy_ter
from params import GRAPH_TYPE, PARAMS
from utils import define_graph
from dominating_set.plots import plot_initial_graph


def main() -> None:
    graph_dict = define_graph(
        graph_type=GRAPH_TYPE,
        params=PARAMS,
    )
    G = graph_dict["G"]
    graph_name = graph_dict["graph_name"]

    plot_initial_graph(
            G=G,
            graph_name=graph_name,
            graph_type=GRAPH_TYPE,
            )

    greedy_standard(
        G=G,
        graph_name=graph_name,
        graph_type=GRAPH_TYPE,
    )

    # greedy_bis(
    #     G=G,
    #     graph_name=graph_name,
    #     graph_type=GRAPH_TYPE,
    # )

    greedy_ter(
        G=G,
        graph_name=graph_name,
        graph_type=GRAPH_TYPE,
    )



if __name__ == "__main__":
    main()
