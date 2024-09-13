"""
   second greedy algorithm to find a dominating set

   Nodes that are already dominated can still be added.
"""

from dominating_set.plots import plot_subset
import networkx as nx
from dominating_set.test_dominating import test_dominating


def greedy_bis(
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
    # sorted is not in place

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

    for node in sorted_nodes:
        step += 1
        # stop if the set is dominating
        if len(dominated_nodes) < n_nodes:
            # update our selected subset
            selected_nodes.append(node)
            print(f"\nadd {node} to the dominating set")
            # update the list of dominated nodes
            if node not in dominated_nodes:
                dominated_nodes.add(node)
            print(f"add {node} to the list of dominated nodes")
            # print('neighbors : ')
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
                method="bis"
            )
    test_dominating(
        G=G,
        selected_nodes=selected_nodes,
        method="bis",
    )
