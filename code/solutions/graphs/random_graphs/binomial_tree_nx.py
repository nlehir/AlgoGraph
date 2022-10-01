import networkx as nx
import matplotlib.pyplot as plt

n=5
graph_name = "binomial_tree"
graph = nx.generators.classic.binomial_tree(n)
nx.draw_networkx(graph)
plt.title(f"binomial tree of order {n}")
plt.tight_layout()
plt.axis('off')
plt.savefig(graph_name+".pdf")
plt.close()

n=30
graph_name = "ladder_graph"
graph = nx.generators.classic.ladder_graph(n)
nx.draw_networkx(graph)
plt.title(f"ladder graph of length {n}")
plt.tight_layout()
plt.axis('off')
plt.savefig(graph_name+".pdf")
plt.close()
