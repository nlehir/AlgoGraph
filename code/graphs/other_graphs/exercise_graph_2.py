import pickle
import random

import numpy as np
from graphviz import Graph

dot = Graph(comment="Graph used to study the dominating set problem")


# number of nodes
n = 100
# max_number_of_successors
m = 6

successors = {}
for node in range(1, n + 1):
    nb_of_successors = random.randint(1, m)
    # avoid node linked to itsself
    successors_of_node = random.sample(range(1, n + 1), nb_of_successors)
    print(successors)
    successors[node] = successors_of_node

# print(successors)

edges_list = []
# build list of edges
for node in range(1, n + 1):
    for successor_of_node in successors[node]:
        print([node, successor_of_node])
        if [node, successor_of_node] not in edges_list:
            # print(node)
            edges_list.append([node, successor_of_node])

print(edges_list)
print(len(edges_list))

for edge in edges_list:
    dot.edge(str(edge[0]), str(edge[1]), color="darkolivegreen4", penwidth="1.1")

with open("data/exercise_2_successors", "wb") as f:
    pickle.dump(successors, f)

with open("data/exercise_2_edges", "wb") as f:
    pickle.dump(edges_list, f)

# visualize the graph
graph_name = "graphs/exercise_2"
dot.render(graph_name)
