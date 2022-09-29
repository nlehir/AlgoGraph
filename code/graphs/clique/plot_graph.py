import networkx as nx
import matplotlib.pyplot as plt

# plotting params
alpha = 0.7
node_size = 200
edge_color = "#145e24"
node_color = "#1b8f34"


def plot_graph(edges: list[set], graph_name: str) -> None:
    print("plot graph")
    G = nx.Graph()

    G.add_edges_from(edges)

    # visualize the graph
    graph_name = f"images/{graph_name}.pdf"

    plt.title(graph_name, fontsize=9)
    # we give a seed to the layout engine
    # in order to always have the same layout
    # fot a given  graph.
    # Otherwise, a random seed is used.
    pos = nx.spring_layout(G, seed=1)
    # if you want a circular layout
    # pos=nx.circular_layout(G)
    nx.draw(
        G,
        pos=pos,
        node_size=node_size,
        node_color=node_color,
        edge_color=edge_color,
        font_size=8,
        width=1,
        alpha=alpha,
        with_labels=True,
    )

    plt.tight_layout()
    plt.axis("off")
    plt.savefig(graph_name)
    plt.close()
