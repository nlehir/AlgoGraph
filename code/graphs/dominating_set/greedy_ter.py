"""
   Third greedy heuristic: the degree of the nodes each computed again at each
   time step.
"""


from dominating_set.plots import plot_subset
import networkx as nx
from dominating_set.test_dominating import test_dominating


def greedy_ter(
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

    """
        greedy algorithm
    """

    print("\n======")
    print("greedy algorithm")
    print("======")

    selected_nodes = list()
    dominated_nodes = set()
    step = 0

    def get_next_node(dominated_nodes: set, nodes: nx.classes.reportviews.NodeView):
        """
        function used to select a new node in the algorithm
        """
        # built the reduced graph
        # consisting in the original graph deprived from dominated nodes
        reduced_graph = [node for node in nodes if node not in dominated_nodes]

        # build a new dictionary containing adjecency relations in the
        # reduced graph
        neighbors_reduced = neighbors.copy()
        for node in neighbors_reduced:
            for ngbr in neighbors_reduced[node]:
                if ngbr in dominated_nodes:
                    print(f"remove {ngbr} from neighbors of {node}")
                    neighbors_reduced[node].remove(ngbr)

        neighbors_in_reduced_graph = {
            node: neighbors_reduced[node] for node in reduced_graph
        }

        # sort that dictionary as before
        sorted_nodes_reduced = sorted(
            neighbors_in_reduced_graph,
            key=lambda node: len(neighbors_in_reduced_graph[node]),
            reverse=True,
        )
        return sorted_nodes_reduced[0]

    while len(dominated_nodes) < n_nodes:
        selected_node = get_next_node(dominated_nodes, nodes)
        print(selected_nodes)

        # update graph
        selected_nodes.append(selected_node)
        print(f"\nadd {selected_node} to the dominating set")
        # update the list of dominated nodes
        dominated_nodes.add(selected_node)
        print(f"add {selected_node} to the list of dominated nodes")
        # print('neighbors : ')
        for neighbor in neighbors[selected_node]:
            if neighbor not in dominated_nodes:
                # update the list of not dominated nodes
                dominated_nodes.add(neighbor)
                print(f"add {neighbor} to the list of dominated nodes")
        # see how many more nodes we have to dominate
        print(f"still have to dominate {n_nodes-len(dominated_nodes)} nodes")
        step += 1
        plot_subset(
            step=step,
            edges=edges_list,
            dominated_nodes=dominated_nodes,
            selected_nodes=selected_nodes,
            graph_name=graph_name,
            graph_type=graph_type,
            method="ter"
        )
    test_dominating(
        G=G,
        selected_nodes=selected_nodes,
        method="ter",
    )
