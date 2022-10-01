import networkx as nx
import matplotlib.pyplot as plt
from networkx.convert import to_dict_of_lists, to_edgelist
from networkx.convert_matrix import to_numpy_array

"""
    https://networkx.org/documentation/stable/reference/convert.html
"""

n_nodes = 20
n_edges = 40
G = nx.generators.random_graphs.gnm_random_graph(n_nodes, n_edges)

print("G nodes")
print(G.nodes)
for node in G.nodes:
    print(node)

print("\nG edges")
print(G.edges)

print("\nG as dictionary of lists")
print(to_dict_of_lists(G))

print("\nG as a numpy array")
print(to_numpy_array(G))
