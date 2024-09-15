import networkx as nx
import os
import matplotlib.pyplot as plt

TITLE_FONTSIZE = 8

def create_folder_if_missing(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def plot_initial_graph(
        G: nx.Graph,
        name: str,
        ):
    pos = nx.spring_layout(G, seed=1)
    title = name
    plt.title(title, fontsize=TITLE_FONTSIZE)
    nx.draw(
        G,
        pos,
        node_size=160,
        # node_color=node_color,
        # edge_color=edge_color,
        font_size=6,
        width=1,
        with_labels=True,
    )
    create_folder_if_missing(folder_name="images")
    fig_path = os.path.join("images", f"{name}.pdf")
    plt.savefig(fig_path)
    plt.close()
    return pos

def highlight_path(
        G: nx.Graph,
        path: list,
        pos,
        title: str,
        fig_name: str,
        folder: str,
        ) -> None:
    """
    Use set for edges, otherwise some edges
    will not be highlighted due to the order
    of the nodes in the edges.
    """
    path_edges = list()
    for index in range(len(path) - 1):
        edge_tuple = path[index], path[index + 1]
        path_edges.append(set(edge_tuple))

    edges_colors = list()
    for edge in G.edges:
        if set(edge) in path_edges:
            # print(f"edge {edge} in the path")
            edges_colors.append("#d627c2")
        else:
            edges_colors.append("#1b50a1")

    node_color = "#b6cef2"
    plt.title(title, fontsize=TITLE_FONTSIZE)
    nx.draw(
        G,
        pos,
        node_size=160,
        node_color=node_color,
        font_size=6,
        edge_color=edges_colors,
        # width=edges_width,
        with_labels=True,
    )
    subfolder = os.path.join(
            "images",
            folder,
            )
    create_folder_if_missing(folder_name=subfolder)
    fig_path = os.path.join(subfolder, fig_name)
    plt.savefig(fig_path)
    plt.close()
