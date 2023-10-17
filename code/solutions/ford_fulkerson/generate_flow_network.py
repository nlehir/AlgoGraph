import os
import pickle

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from read_params import read_params

# from random import randint


"""
This time the graph is oriented
"""

if not os.path.exists("data/"):
    os.makedirs("data")
if not os.path.exists("images/"):
    os.makedirs("images")


def generate_flow_network(nb_nodes: int, nb_edges: int, capacity_max: int) -> None:
    """
    nb_nodes: number of inner nodes in the graph
    (without source and sink)

    some edges will link nodes to source and sink.
    other edges will link nodes to nodes.

    max_edges: maximum number of edges. There might be less edges
    in the final graph as we remove self loops.

    capacity_max: maximum capacity of each edge in the graph.
    """
    flow_network = f"network_{nb_nodes}_nodes_edges_{nb_edges}_capmax_{capacity_max}"
    # create graph
    G = nx.DiGraph()

    """
    capacities of the network
    """
    # capacities beetwwen inner nodes
    # initialize them to 0
    inner_capacities = np.zeros((nb_nodes, nb_nodes))

    for _ in range(nb_edges):
        # add an edge
        node_1 = np.random.randint(0, nb_nodes)
        node_2 = np.random.randint(0, nb_nodes)
        # without self loops
        if not node_1 == node_2:
            capacity = np.random.randint(0, capacity_max + 1)
            inner_capacities[node_1][node_2] = capacity
            if capacity:
                print(f"link {node_1} to {node_2} with capacity {capacity}.")
                G.add_edge(f"i-{node_1}", f"i-{node_2}")

    # capacitites between nodes and source
    source_capacities = np.random.randint(0, capacity_max + 1, nb_nodes)
    for node in range(nb_nodes):
        if source_capacities[node]:
            # check if node is connected to other nodes
            # in the graph
            print(f"link source to {node} with capacity {source_capacities[node]}.")
            G.add_edge("Source", f"i-{node}")

    # capacitites between nodes and sink
    sink_capacities = np.random.randint(0, capacity_max + 1, nb_nodes)
    for node in range(nb_nodes):
        if sink_capacities[node]:
            # check if node is connected to other nodes in the graph
            # if sum(inner_capacities[:, node]):
            print(f"link {node} to sink with capacity {sink_capacities[node]}.")
            # draw the edge
            G.add_edge(f"i-{node}", "Sink")

    # visualize the graph
    dir_name = "images/" + flow_network
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    plt.title("initial graph")
    pos = dict()
    pos = nx.spring_layout(G, seed=1)

    # set up node positions
    min_scope = 30
    max_scope = 70
    for node in range(nb_nodes):
        pos[f"i-{node}"] = (
            np.random.uniform(min_scope, max_scope),
            node / nb_nodes * 100,
        )
    print(pos)

    pos["Source"] = (0, 50)
    pos["Sink"] = (100, 50)

    node_color = "#b6cef2"
    edge_color = "#1b50a1"
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
    edge_labels = dict()
    for edge in G.edges:
        print(edge)
        if edge[0] == "Source":
            node = int(edge[1].split("-")[1])
            edge_labels[edge] = source_capacities[node]
        elif edge[1] == "Sink":
            node = int(edge[0].split("-")[1])
            edge_labels[edge] = sink_capacities[node]
        else:
            node_1 = int(edge[0].split("-")[1])
            node_2 = int(edge[1].split("-")[1])
            edge_labels[edge] = inner_capacities[node_1][node_2]
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6)
    # plt.tight_layout()
    plt.savefig(dir_name + "/initial_graph_nx.pdf")
    plt.close()

    # store data
    nodes = [x for x in range(1, nb_nodes + 1)]
    with open("data/" + flow_network + "_nodes", "wb") as f:
        pickle.dump(nodes, f)

    with open("data/" + flow_network + "_inner_capacities", "wb") as f:
        pickle.dump(inner_capacities, f)

    with open("data/" + flow_network + "_source_capacities", "wb") as f:
        pickle.dump(source_capacities, f)

    with open("data/" + flow_network + "_sink_capacities", "wb") as f:
        pickle.dump(sink_capacities, f)

    with open("data/" + flow_network + "_G", "wb") as f:
        pickle.dump(G, f)

    with open("data/" + flow_network + "_pos", "wb") as f:
        pickle.dump(pos, f)


params = read_params()
nb_nodes = int(params["nb_nodes"])
nb_edges = int(params["nb_edges"])
capacity_max = int(params["capacity_max"])
generate_flow_network(nb_nodes, nb_edges, capacity_max)
