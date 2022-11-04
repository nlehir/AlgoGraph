"""
Load flow network and apply Ford Fulkerson
# TODO: refacto <30-09-22, yourname> #
"""

import os
import pickle

import ford_functions


def apply_algorithm(nb_nodes_group_1, nb_nodes_group_2, nb_edges):
    flow_network = (
        f"network_{nb_nodes_group_1}_{nb_nodes_group_2}_nodes_edges_{nb_edges}"
    )
    dir_name = "images/" + flow_network + "/"

    with open("data/" + flow_network + "_nodes_1", "rb") as f:
        nodes_1 = pickle.load(f)

    with open("data/" + flow_network + "_nodes_2", "rb") as f:
        nodes_2 = pickle.load(f)

    with open("data/" + flow_network + "_inner_capacities", "rb") as f:
        inner_capacities = pickle.load(f)

    with open("data/" + flow_network + "_source_capacities", "rb") as f:
        source_capacities = pickle.load(f)

    with open("data/" + flow_network + "_sink_capacities", "rb") as f:
        sink_capacities = pickle.load(f)

    with open("data/" + flow_network + "_G", "rb") as f:
        G = pickle.load(f)

    with open("data/" + flow_network + "_pos", "rb") as f:
        pos = pickle.load(f)

    # create directory of necessary
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # clean directory
    for image in os.listdir(dir_name):
        if "initial" not in image:
            os.remove(dir_name + image)

    # apply Ford Fulkerson
    ford_functions.apply_ford_fulkerson(
        nodes_1,
        nodes_2,
        inner_capacities,
        source_capacities,
        sink_capacities,
        G,
        pos,
        dir_name,
    )


apply_algorithm(15, 15, 30)
