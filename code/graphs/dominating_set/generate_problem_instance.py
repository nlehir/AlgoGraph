import os
import pickle
import random

from plot_graph.plot_graph import plot_initial_graph
from read_params import read_params


def generate_problem_instance(n_nodes: int, max_successors: int):
    """
    Function used to generate an instance of the dominating set problem.
    We use undirected graphs, edges are not directed.

    Parameters
    ----------
        n_nodes : number of nodes in the graph.

        max_successors : HALF maximum number of neighbors for each node.
        this comes from the way we build the graph. For a given node,
        say node_A,
        we pick a random number of successors, smaller than max_successors.
        But node_A might also be picked as a successor by other nodes in
        the graph. Since we are working in a undirected graph, the concept
        of successor is not perfeclty relevant. We should just see it
        as a convenient quantity when building the graph.
        But we will store the final result as
        "neighbor".

    Output:
    -------
        saves a representation of the graph.
        saves graph data (list of edges, list of successors)
        in a pickle file (binary file)
    """
    msg = (
        f"\ngenerate problem instance for {n_nodes} nodes and at most "
        f"{max_successors} successors per node"
    )
    print(msg)
    successors = dict()
    for node in range(1, n_nodes + 1):
        nb_of_successors = random.randint(1, max_successors)
        successors_of_node = random.sample(range(1, n_nodes + 1), nb_of_successors)
        # avoid node linked to itsself
        if node in successors_of_node:
            successors_of_node.remove(node)
        successors[node] = successors_of_node

    # we are working with an undirected graph.
    # As a consequence,
    # if node_A is successor of node_B, then
    # node_B is also successor of node_A
    for node in successors:
        for successor in successors[node]:
            if node not in successors[successor]:
                successors[successor].append(node)
    # at this point, we have neighbors, rather than
    # successors

    edges_list = list()
    # build list of edges
    # the edges will just be used for plotting.
    # so we will not keep both edges [node_A, node_B] and
    # [node_B, node_A]
    for node in range(1, n_nodes + 1):
        for successor_of_node in successors[node]:
            # we use an undirected graph
            if [successor_of_node, node] not in edges_list:
                edges_list.append([node, successor_of_node])

    print("edges")
    print(edges_list)

    parameters = f"n={n_nodes}_maxs={max_successors}"
    with open(f"data/{parameters}_neighbors", "wb") as f:
        pickle.dump(successors, f)

    with open(f"data/{parameters}_edges", "wb") as f:
        pickle.dump(edges_list, f)

    dir_name = f"images/{parameters}"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    for filename in os.listdir(dir_name):
        path_to_file = os.path.join(dir_name, filename)
        os.remove(path_to_file)
    plot_initial_graph(edges_list, parameters)


params = read_params()
generate_problem_instance(params[0], params[1])
