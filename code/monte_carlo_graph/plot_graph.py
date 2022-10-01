import networkx as nx
import os
import matplotlib.pyplot as plt

def plot_graph(G: nx.Graph, graph_name: str, test: int) -> None:
    image_name = f"images/{graph_name}_{test}.pdf"
    plt.title(f"{graph_name}_{test}")
    # visualize the graph
    # choose colors
    node_color="#b6cef2"
    edge_color="#1b50a1"
    # we give a seed to the layout engine
    # in order to always have the same layout
    # fot a given  graph.
    # Otherwise, a random seed is used.
    pos=nx.spring_layout(G, seed=1)
    # pos=nx.spring_layout(G)
    # if you prefer a circular layout
    # pos=nx.circular_layout(G)
    nx.draw(G,
            pos,
            node_size=160,
            node_color=node_color,
            edge_color=edge_color,
            font_size=6,
            width=1,
            with_labels=True)
    plt.tight_layout()
    plt.savefig(image_name)
    plt.close()
