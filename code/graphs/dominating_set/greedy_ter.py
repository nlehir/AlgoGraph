"""
   Third greedy heuristic: the degree of the nodes each computed again at each
   time step.
"""


from plot_graph.plot_graph import plot_subset
from test_dominating import test_dominating


def greedy_ter(
        neighbors: dict,
        edges_list: list,
        graph_name: str,
        ) -> None:
    # size of the graph (number of nodes)
    nodes = neighbors.keys()
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
    dominated_nodes = list()
    step = 0

    def get_next_node(dominated_nodes: list, nodes: list) -> int:
        """
        function used to select a new node in the algorithm
        """
        # built the reduced graph
        # consisting in the original graph deprived from dominated nodes
        """
        EDIT
        """
        reduced_graph = [node for node in nodes]

        # build a new dictionary containing adjecency relations in the
        # reduced graph
        neighbors_reduced = neighbors.copy()
        """
        EDIT LOOP
        """
        for node in neighbors_reduced:
            for ngbr in neighbors_reduced[node]:
                if ngbr in dominated_nodes:
                    print(f"remove {ngbr} from neighbors of {node}")
                    pass

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
        selected_node = get_next_node(dominated_nodes, list(nodes))
        print(selected_nodes)

        # update graph
        selected_nodes.append(selected_node)
        print(f"\nadd {selected_node} to the dominating set")
        # update the list of dominated nodes
        dominated_nodes.append(selected_node)
        print(f"add {selected_node} to the list of dominated nodes")
        # print('neighbors : ')
        for neighbor in neighbors[selected_node]:
            if neighbor not in dominated_nodes:
                # update the list of not dominated nodes
                dominated_nodes.append(neighbor)
                print(f"add {neighbor} to the list of dominated nodes")
        # see how many more nodes we have to dominate
        print(f"still have to dominate {n_nodes-len(dominated_nodes)} nodes")
        step += 1
        plot_subset(
            step,
            sorted_nodes,
            edges_list,
            dominated_nodes,
            selected_nodes,
            graph_name,
            method="ter",
        )
    test_dominating(nodes, edges_list, selected_nodes)
