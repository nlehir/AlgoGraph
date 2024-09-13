"""
   greedy algorithm to try to find a minimal dominating set

   Degree based heuristic:
       - nodes are sorted by degree
       - then added sequentially to the selected set
       (that will be the final dominating set) if they
       are not already dominated.
"""

import networkx as nx

from dominating_set.plots import plot_subset
from dominating_set.test_dominating import test_dominating


def greedy_standard(
    G: nx.Graph,
    graph_name: str,
    graph_type: str,
) -> None:
    neighbors = nx.to_dict_of_lists(G)
    edges_list = G.edges
    nodes = G.nodes
    n_nodes = len(nodes)

    """
        sort the nodes by degree
        aka the number of neighbors
        """
    sorted_nodes = sorted(
        neighbors, key=lambda node: len(neighbors[node]), reverse=True
    )

    print("=====")
    print("sorted dictionary of neighbors by degree of the node")
    print("=====")

    for node in sorted_nodes:
        print(f"node  {node}")
        print(f"neighbors {neighbors[node]}")

    print("\n======")
    print("greedy algorithm")
    print("======")

    selected_nodes = list()
    dominated_nodes = set()
    step = 0

    """
    EDIT: add the algorithm
    """
    for node in sorted_nodes:
        # stop if the set is dominating
        if node not in dominated_nodes:
            step += 1
            # update our selected subset
            selected_nodes.append(node)
            print(f"\nadd {node} to the set of selected nodes")
            # update the list of dominated nodes
            dominated_nodes.add(node)
            print(f"add {node} to the list of dominated nodes")
            for neighbor in neighbors[node]:
                if neighbor not in dominated_nodes:
                    # update the list of not dominated nodes
                    dominated_nodes.add(neighbor)
                    print(f"add {neighbor} to the list of dominated nodes")
            # see how many more nodes we have to dominate
            print(f"still have to dominate {n_nodes-len(dominated_nodes)} nodes")
            plot_subset(
                step=step,
                edges=edges_list,
                dominated_nodes=dominated_nodes,
                selected_nodes=selected_nodes,
                graph_name=graph_name,
                graph_type=graph_type,
            )
    test_dominating(
        G=G,
        selected_nodes=selected_nodes,
        method="standard",
    )
