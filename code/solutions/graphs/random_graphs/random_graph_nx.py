import matplotlib.pyplot as plt
import networkx as nx

graph_name = "random_sparse_graph"
graph = nx.generators.random_graphs.gnm_random_graph(20, 30)
nx.draw_networkx(graph)
plt.title("random sparse graph")
plt.tight_layout()
plt.axis("off")
plt.savefig(graph_name + ".pdf")
plt.close()

dense_graph_name = "random_dense_graph"
dense_graph = nx.generators.random_graphs.dense_gnm_random_graph(10, 40)
nx.draw_networkx(dense_graph)
plt.title("random dense graph")
plt.tight_layout()
plt.axis("off")
plt.savefig(dense_graph_name + ".pdf")
plt.close()
