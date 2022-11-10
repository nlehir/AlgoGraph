import pickle

from plot_graph import plot_graph

# edges is a list of all edges
with open(f"data/edges", "rb") as f:
    edges = pickle.load(f)


# reformat edges as a list of tuples
edges = [set(edge) for edge in edges]

# plot initial graph
plot_graph(edges, "initial graph")

"""
    build complement graph
"""

# build the list of all nodes
# we assume there are no isolated nodes
nodes = list()
for edge in edges:
    for edge_node in edge:
        if edge_node not in nodes:
            nodes.append(edge_node)

# build all edges
all_edges = [
    set([i, j]) for i in range(1, len(nodes) + 1) for j in range(i + 1, len(nodes) + 1)
]

# choose complement edges
complementary_edges = [edge for edge in all_edges if edge not in edges]

# plot complement graph
plot_graph(complementary_edges, "complement graph")
