"""
Functions used for the greedy matching algorithm
"""
import matplotlib.pyplot as plt

import networkx as nx


def show_matching(
        nodes: list[int],
        edges_list: list[list],
        matching: list[set],
        index: int,
        dir_name: str) -> None:
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
    graph_name = dir_name + "match_greedy_" + str(index) + ".pdf"
    graph_title = f"\nMatching size: {len(matching)}\nAlgo step: {index}\nNb nodes: {len(nodes)}"

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
    plt.savefig(graph_name)
    plt.close()


def match_greedy_list_list(edges_list: list[list]) -> list:
    matched_nodes = list()
    matching = list()
    for edge in edges_list:
        if edge[0] in matched_nodes:
            pass
        elif edge[1] in matched_nodes:
            pass
        else:
            matched_nodes += edge
            matching.append(set(edge))
    return matching


def match_greedy_set_list(edges_list: list[list]) -> list:
    matched_nodes = set()
    matching = list()
    for edge in edges_list:
        if edge[0] in matched_nodes:
            pass
        elif edge[1] in matched_nodes:
            pass
        else:
            # add the nodes to the list of matched nodes
            matched_nodes.update(set(edge))
            matching.append(edge)
    return matching


def match_greedy_set_set(edges_list: list[list]) -> list:
    matched_nodes = set()
    matching = set()
    for edge in edges_list:
        if edge[0] in matched_nodes:
            pass
        elif edge[1] in matched_nodes:
            pass
        else:
            # add the nodes to the list of matched nodes
            matched_nodes.update(set(edge))
            matching.add(edge)
    return list(matching)

