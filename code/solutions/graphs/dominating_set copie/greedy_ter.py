"""
   greedy algorithm to try to find a minimal dominating set
"""

import os
import pickle

from plot_graph.plot_graph import plot_subset
from read_params import read_params
from test_dominating import test_dominating


def process_graph(graph_name: str) -> None:
    # load graph data
    with open(f"data/{graph_name}_neighbors", "rb") as f:
        neighbors = pickle.load(f)

    with open(f"data/{graph_name}_edges", "rb") as f:
        edges_list = pickle.load(f)

    # clean folder
    dir_name = f"images/{graph_name}"
    for filename in os.listdir(dir_name):
        if "initial" not in filename and "ter" in filename:
            path_to_file = os.path.join(dir_name, filename)
            os.remove(path_to_file)

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

    def get_next_node(dominated_nodes: list, nodes: list):
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


def main() -> None:
    params = read_params()
    n_nodes = params[0]
    max_successors = params[1]
    parameters = f"n={n_nodes}_maxs={max_successors}"
    process_graph(parameters)


if __name__ == "__main__":
    main()
