import pickle
import os
from plot_graph.plot_graph import plot_initial_graph

edges = [
    [0, 1],
    [0, 2],
    [0, 3],
    [0, 13],
    [0, 11],
    [0, 12],
    [0, 4],
    [0, 5],
    [6, 5],
    [6, 2],
    [6, 1],
    [6, 12],
    [6, 13],
    [6, 11],
    [6, 3],
    [6, 4],
    [6, 5],
    [0, 7],
    [7, 8],
    [7, 9],
    [7, 14],
    [7, 15],
    [7, 16],
    [7, 17],
    [7, 18],
    [7, 10],
]

nodes = [node for node in range(19)]

successors = dict()
for node in nodes:
    successor_of_node = list()
    for edge in edges:
        if edge[0] == node:
            successor_of_node.append(edge[1])
        elif edge[1] == node:
            successor_of_node.append(edge[0])
    successors[node] = successor_of_node


with open(f"data/custom_neighbors", "wb") as f:
    pickle.dump(successors, f)

with open(f"data/custom_edges", "wb") as f:
    pickle.dump(edges, f)

dir_name = f"images/custom"
if not os.path.exists(dir_name):
    os.makedirs(dir_name)
for filename in os.listdir(dir_name):
    path_to_file = os.path.join(dir_name, filename)
    os.remove(path_to_file)
plot_initial_graph(edges, "custom")
