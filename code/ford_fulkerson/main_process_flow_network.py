"""
Load flow network and apply Ford Fulkerson
algorithm.
"""

import os
import pickle

import ford_functions
from params import CAPACITY_MAX, NB_EDGES, NB_NODES


def process_network(nb_nodes: int, nb_edges: int, capacity_max: int) -> None:
    flow_network = f"network_{nb_nodes}_nodes_edges_{nb_edges}_capmax_{capacity_max}"
    dir_name = os.path.join(
        "images",
        flow_network,
    )

    # load data
    nodes_path = os.path.join("data", f"{flow_network}_nodes")
    with open(nodes_path, "rb") as f:
        nodes = pickle.load(f)

    inner_capacities_path = os.path.join("data", f"{flow_network}_inner_capacities")
    with open(inner_capacities_path, "rb") as f:
        inner_capacities = pickle.load(f)

    source_capacities_path = os.path.join("data", f"{flow_network}_source_capacities")
    with open(source_capacities_path, "rb") as f:
        source_capacities = pickle.load(f)

    sink_capacities_path = os.path.join("data", f"{flow_network}_sink_capacities")
    with open(sink_capacities_path, "rb") as f:
        sink_capacities = pickle.load(f)

    G_path = os.path.join("data", f"{flow_network}_G")
    with open(G_path, "rb") as f:
        G = pickle.load(f)

    pos_path = os.path.join("data", f"{flow_network}_pos")
    with open(pos_path, "rb") as f:
        pos = pickle.load(f)

    # create directory if necessary
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # clean directory
    for image in os.listdir(dir_name):
        if "initial" not in image:
            image_path = os.path.join(dir_name, image)
            os.remove(image_path)

    # apply Ford Fulkerson
    ford_functions.apply_ford_fulkerson(
        nodes=nodes,
        inner_capacities=inner_capacities,
        source_capacities=source_capacities,
        sink_capacities=sink_capacities,
        dir_name=dir_name,
        G=G,
        pos=pos,
    )


def main() -> None:
    process_network(
        nb_nodes=NB_NODES,
        nb_edges=NB_EDGES,
        capacity_max=CAPACITY_MAX,
    )


if __name__ == "__main__":
    main()
