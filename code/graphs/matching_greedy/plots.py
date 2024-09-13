import matplotlib.pyplot as plt
from utils import define_fig_path
import networkx as nx

def show_matching(
        nodes: nx.classes.reportviews.NodeView,
        edges_list: nx.classes.reportviews.EdgeView,
        matching: list[set],
        index: int,
        graph_name: str,
        graph_type: str,
        ) -> None:
    """
    function to highlight the matching edges
    and save the graph image
    """
    G = nx.Graph()

    # set colors
    edge_colors = list()
    unmatched_edge_color = "#1b50a1"
    matched_edge_color = "#eb6b34"
    node_color = "#b6cef2"
    matched_nodes_colors = [
        "#34eb64",
        "#e8eb34",
        "#eb8f34",
        "#eb34d9",
        "#eb345f",
        "#3499eb",
        "#4710eb",
        "#e4ebe5",
        "#71ebe5",
        "#d6eb34",
        "#c9eb34",
        "#D8D56d",
        "#d5628c",
        "#37abc6",
        "#75a738",
        "#eb34d6",
    ]

    # build the graph
    for edge in edges_list:
        G.add_edge(edge[0], edge[1])

    # we use sets because
    # G.edges can change the indexing in the edges
    for edge in G.edges:
        if set(edge) in matching:
            edge_colors.append(matched_edge_color)
        else:
            edge_colors.append(unmatched_edge_color)

    # visualize the graph
    graph_title = (
            f"\nMatching size: {len(matching)}"
            f"\nAlgo step: {index}"
            f"\nNb nodes: {len(nodes)}"
            f"\nGraph type: {graph_type}"
            )

    plt.title(graph_title, fontsize=9)
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
        node_size=200,
        node_color=node_color,
        edge_color=edge_colors,
        font_size=8,
        width=1,
        with_labels=True,
    )

    colored = list()
    matched_nodes_colors_copy = matched_nodes_colors.copy()
    for node_1 in G.nodes:
        for node_2 in G.nodes:
            if set([node_1, node_2]) in matching:
                if set([node_1, node_2]) not in colored:
                    # if there are no more colors available,
                    # update the list
                    if len(matched_nodes_colors_copy) == 0:
                        matched_nodes_colors_copy = matched_nodes_colors.copy()
                    # choose a color from the list
                    color = matched_nodes_colors_copy.pop()
                    # update the list of colored nodes
                    colored.append(set([node_1, node_2]))
                    nx.draw_networkx_nodes(
                        G,
                        pos,
                        nodelist=[node_1, node_2],
                        node_color=color,
                        node_size=200,
                        alpha=0.8,
                    )

    plt.tight_layout()
    plt.axis("off")
    fig_path = define_fig_path(
        problem="matching_greedy",
        graph_name=graph_name,
        method="greedy",
        step=index,
    )
    plt.savefig(fig_path)
    plt.close()
