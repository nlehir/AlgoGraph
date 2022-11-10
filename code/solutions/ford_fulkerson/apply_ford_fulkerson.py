"""
Load flow network and apply Ford Fulkerson
"""

import os
import pickle

import ford_functions
from read_params import read_params


def process_network(nb_nodes: int, nb_edges: int, capacity_max: int) -> None:
    flow_network = f"network_{nb_nodes}_nodes_edges_{nb_edges}_capmax_{capacity_max}"
    dir_name = "images/" + flow_network + "/"

    # load data
    with open(f"data/{flow_network}_nodes", "rb") as f:
        nodes = pickle.load(f)

    with open(f"data/{flow_network}_inner_capacities", "rb") as f:
        inner_capacities = pickle.load(f)

    with open(f"data/{flow_network}_source_capacities", "rb") as f:
        source_capacities = pickle.load(f)

    with open(f"data/{flow_network}_sink_capacities", "rb") as f:
        sink_capacities = pickle.load(f)

    with open(f"data/{flow_network}_G", "rb") as f:
        G = pickle.load(f)

    with open(f"data/{flow_network}_pos", "rb") as f:
        pos = pickle.load(f)

    # create directory if necessary
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    # clean directory
    for image in os.listdir(dir_name):
        if "initial" not in image:
            os.remove(dir_name + image)

    # apply Ford Fulkerson
    ford_functions.apply_ford_fulkerson(
        nodes, inner_capacities, source_capacities, sink_capacities, dir_name, G, pos
    )


params = read_params()
nb_nodes = int(params["nb_nodes"])
nb_edges = int(params["nb_edges"])
capacity_max = int(params["capacity_max"])
process_network(nb_nodes, nb_edges, capacity_max)
