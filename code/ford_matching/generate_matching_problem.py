import pickle
import numpy as np
import os
import networkx as nx
import matplotlib.pyplot as plt

"""
This time the graph is oriented
"""

if not os.path.exists("data/"):
    os.makedirs("data")
if not os.path.exists("images/"):
    os.makedirs("images")


def generate_matching_problem(nb_nodes_group_1: int,
                              nb_nodes_group_2: int,
                              nb_edges: int):
    """
    nb_nodes: number of inner nodes in the graph (meaning we don't take
    the sink and the source into account.

    max_edges: maximum number of edges. There might be less edges
    in the final graph as we remove self loops.
    """
    flow_network = f"network_{nb_nodes_group_1}_{nb_nodes_group_2}_nodes_edges_{nb_edges}"

    # create graph
    G = nx.DiGraph()

    # capacities of the network
    # capacities beetwwen inner nodes
    # initialize them to 0
    inner_capacities = np.zeros((nb_nodes_group_1+nb_nodes_group_2,
                                 nb_nodes_group_1+nb_nodes_group_2))

    for node in range(nb_nodes_group_1):
        G.add_node(f"1-{node}")

    for node in range(nb_nodes_group_1, nb_nodes_group_1+nb_nodes_group_2):
        G.add_node(f"2-{node}")

    # add edges
    for edge in range(nb_edges):
        node_1 = np.random.randint(0, nb_nodes_group_1)
        node_2 = np.random.randint(
            nb_nodes_group_1, nb_nodes_group_1 + nb_nodes_group_2)
        inner_capacities[node_1][node_2] = 1
        G.add_edge(f"1-{node_1}", f"2-{node_2}")

    # introduce the source
    G.add_node("Source")
    source_group_1_capacities = np.ones(nb_nodes_group_1)
    source_group_2_capacitires = np.zeros(nb_nodes_group_2)
    source_capacities = np.concatenate((source_group_1_capacities,
                                        source_group_2_capacitires))
    for node in range(nb_nodes_group_1):
        G.add_edge(f"Source", f"1-{node}")

    # introduce the sink
    G.add_node("Sink")
    sink_group_2_capacities = np.ones(nb_nodes_group_2)
    sink_group_1_capacities = np.zeros(nb_nodes_group_1)
    sink_capacities = np.concatenate(
        (sink_group_1_capacities, sink_group_2_capacities))
    for node in range(nb_nodes_group_1, nb_nodes_group_1+nb_nodes_group_2):
        G.add_edge(f"2-{node}", f"Sink")

    # visualize the graph
    dir_name = "images/" + flow_network
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    plt.title("initial graph")
    pos = dict()
    pos = nx.spring_layout(G, seed=1)

    # set up node positions
    for node in range(nb_nodes_group_1):
        pos[f"1-{node}"] = (30, node/nb_nodes_group_1*100)

    for node in range(nb_nodes_group_1, nb_nodes_group_1+nb_nodes_group_2):
        pos[f"2-{node}"] = (70, (node-nb_nodes_group_1)/nb_nodes_group_2*100)

    pos["Source"] = (0, 50)
    pos["Sink"] = (100, 50)


    node_color = "#b6cef2"
    edge_color = "#1b50a1"
    nx.draw(G,
            pos,
            node_size=160,
            node_color=node_color,
            edge_color=edge_color,
            font_size=6,
            width=1,
            with_labels=True)
    # plt.tight_layout()
    plt.savefig(dir_name+"/initial_graph_nx.pdf")
    plt.close()

    # store data
    nodes_1 = [x for x in range(1, nb_nodes_group_1 + 1)]
    with open("data/" + flow_network + "_nodes_1", "wb") as f:
        pickle.dump(nodes_1, f)

    nodes_2 = [x for x in range(
        nb_nodes_group_1, nb_nodes_group_1 + nb_nodes_group_2)]
    with open("data/" + flow_network + "_nodes_2", "wb") as f:
        pickle.dump(nodes_2, f)

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


generate_matching_problem(15, 15, 30)
