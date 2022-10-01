import networkx as nx
from networkx.algorithms.dominating import dominating_set
import matplotlib.pyplot as plt
from plot_graph import plot_graph

"""
Powerlaw cluster graph
https://networkx.org/documentation/stable/reference/generated/networkx.generators.random_graphs.powerlaw_cluster_graph.html
"""

nb_nodes = 100
m_edges = 3
proba_triangle = 0.2
name = "pcg"

nb_trials = 1000

dominating_set_sizes = list()
for test in range(nb_trials):
    print(f"test id: {test}")
    G = nx.generators.powerlaw_cluster_graph(nb_nodes, m_edges, proba_triangle)
    if test == 1 or test == 2:
        plot_graph(G, "pcg", test)
    D = dominating_set(G)
    dominating_set_sizes.append(len(D))

means = [sum(dominating_set_sizes[:k]) / k for k in range(1, nb_trials)]
plt.plot(range(1, nb_trials), means)
title = (
    "Mean dominating set size\n"
    "PCG\n"
    f"{nb_nodes} nodes, m_edges: {m_edges}, proba_triangle: {proba_triangle}\n"
    "Greedy algorithm"
)
plt.title(title)
plt.xlabel("number of trials")
plt.ylabel("Dominating set size")
plt.tight_layout()
plt.savefig(f"convergence_{name}_m_edges_{m_edges}_p_triangle_{proba_triangle}.pdf")
plt.close()
