import networkx as nx
from networkx.algorithms.dominating import dominating_set
import matplotlib.pyplot as plt
from plot_graph import plot_graph

"""
Gnp random graph
https://networkx.org/documentation/stable/reference/generated/networkx.generators.random_graphs.gnp_random_graph.html
"""

nb_nodes = 100
p_edge = 0.3
name = "gnp"

nb_trials = 1000

dominating_set_sizes = list()
for test in range(nb_trials):
    print(f"test id: {test}")
    G = nx.generators.gnp_random_graph(nb_nodes, p_edge)
    if test == 1 or test == 2:
        plot_graph(G, name, test)
    D = dominating_set(G)
    dominating_set_sizes.append(len(D))

means = [sum(dominating_set_sizes[:k]) / k for k in range(1, nb_trials)]
plt.plot(range(1, nb_trials), means)
title = (
    "Mean dominating set size\n"
    "PCG\n"
    f"{nb_nodes} nodes, p_edge: {p_edge}\n"
    "Greedy algorithm"
)
plt.title(title)
plt.xlabel("number of trials")
plt.ylabel("Dominating set size")
plt.tight_layout()
plt.savefig(f"convergence_{name}_p_edge_{p_edge}.pdf")
plt.close()
