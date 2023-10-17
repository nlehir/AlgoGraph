"""
Generate graph data to perform the max matching greedy
algorithm. We generate:
    - a dictionary of neighbors
    - a list of edges
    # TODO: unify with the file used in the dominating set problem <30-09-22, yourname> #
"""

import os
import pickle
import random

import matplotlib.pyplot as plt
import networkx as nx
from read_params import read_params

if not os.path.exists("data/"):
    os.makedirs("data")

if not os.path.exists("images/"):
    os.makedirs("images")


def generate_problem_instance(n_nodes: int, max_successors: int):
    """
    Function used to generate an instance of the matching set problem.
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
    successors = {}
    for node in range(1, n_nodes + 1):
        nb_of_successors = random.randint(1, max_successors)
        # avoid node linked to itsself
        successors_of_node = random.sample(range(1, n_nodes + 1), nb_of_successors)
        # print(successors)
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

    edges_list = []
    # build list of edges
    # the edges will just be used for plotting.
    # so we will not keep both
    # [node_A, node_B] and
    # [node_B, node_A]
    for node in range(1, n_nodes + 1):
        for successor_of_node in successors[node]:
            if [node, successor_of_node] not in edges_list:
                # remove duplicate edges (undirected graph)
                if [successor_of_node, node] not in edges_list:
                    # remove self edge
                    if node is not successor_of_node:
                        edges_list.append([node, successor_of_node])

    print("edges")
    print(edges_list)

    G = nx.Graph()
    for edge in edges_list:
        G.add_edge(edge[0], edge[1])

    # save data
    graph_name = f"n={n_nodes}_maxs={max_successors}"

    nodes = [x for x in range(1, n_nodes + 1)]
    with open(f"data/{graph_name}_nodes", "wb") as f:
        pickle.dump(nodes, f)

    with open(f"data/{graph_name}_neighbors", "wb") as f:
        pickle.dump(successors, f)

    with open(f"data/{graph_name}_edges", "wb") as f:
        pickle.dump(edges_list, f)

    # visualize the graph
    # choose colors
    node_color = "#b6cef2"
    edge_color = "#1b50a1"

    # create directory for the graph
    dir_name = "images/" + graph_name + "/"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    image_name = f"images/{graph_name}/initial_graph.pdf"

    plt.title("initial graph")
    # we give a seed to the layout engine
    # in order to always have the same layout
    # fot a given  graph.
    # Otherwise, a random seed is used.
    pos = nx.spring_layout(G, seed=1)
    # if you prefer a circular layout
    # pos=nx.circular_layout(G)
    nx.draw(
        G,
        pos,
        node_size=160,
        node_color=node_color,
        edge_color=edge_color,
        font_size=6,
        width=1,
        with_labels=True,
    )
    plt.tight_layout()
    plt.savefig(image_name)
    plt.close()


params = read_params()
nb_nodes = params[0]
max_successors = params[1]
generate_problem_instance(nb_nodes, max_successors)
