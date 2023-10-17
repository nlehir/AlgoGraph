import networkx as nx
from networkx.algorithms.dominating import dominating_set, is_dominating_set

G = nx.generators.random_graphs.gnm_random_graph(20, 80)
D = dominating_set(G)

print(f"Dominating set: {D}")
print(is_dominating_set(G, D))
