import networkx as nx
from networkx.algorithms.dominating import dominating_set
import matplotlib.pyplot as plt
from plot_graph import plot_graph

"""
Gaussian random partition graph
https://networkx.org/documentation/stable/reference/generated/networkx.generators.community.gaussian_random_partition_graph.html
"""


nb_nodes = 100
mean_cluster_size = 10
name = "grp"

nb_trials = 1000

dominating_set_sizes = list()
for test in range(nb_trials):
    print(f"test id: {test}")
    G = nx.generators.gaussian_random_partition_graph(
        nb_nodes, mean_cluster_size, 0.1, 0.1, 0.1
    )
    if test == 1 or test == 2:
        plot_graph(G, name, test)
    D = dominating_set(G)
    dominating_set_sizes.append(len(D))

means = [sum(dominating_set_sizes[:k]) / k for k in range(1, nb_trials)]
plt.plot(range(1, nb_trials), means)
title = (
    "Mean dominating set size\n"
    "Gaussian random partition graph\n"
    f"{nb_nodes} nodes, mean cluster size {mean_cluster_size}\n"
    "Greedy algorithm"
)
plt.title(title)
plt.xlabel("number of trials")
plt.ylabel("Dominating set size")
plt.tight_layout()
plt.savefig(f"convergence_{name}_{nb_nodes}_nodes_mcs_{mean_cluster_size}.pdf")
plt.close()
