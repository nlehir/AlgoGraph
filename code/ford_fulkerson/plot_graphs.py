"""
    Utility functions in order to
    visualize the graphs
"""

import os

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def show_residual_network_nx(
    G_residual: nx.DiGraph,
    pos: dict,
    residual_capacities: np.ndarray,
    dir_name: str,
    step: int,
) -> None:
    edges_width = list()
    edges_colors = list()
    edge_labels = dict()

    for edge in G_residual.edges:
        reverse = False
        if edge[0] == "Source":
            node = int(edge[1].split("-")[1])
            residual_capacity = residual_capacities[0, node + 1]
        elif edge[0] == "Sink":
            reverse = True
            node = int(edge[1].split("-")[1])
            residual_capacity = residual_capacities[-1, node + 1]
        elif edge[1] == "Sink":
            node = int(edge[0].split("-")[1])
            residual_capacity = residual_capacities[node + 1, -1]
        elif edge[1] == "Source":
            reverse = True
            node = int(edge[0].split("-")[1])
            residual_capacity = residual_capacities[node + 1, 0]
        else:
            node_1 = int(edge[0].split("-")[1])
            node_2 = int(edge[1].split("-")[1])
            residual_capacity = residual_capacities[node_1 + 1, node_2 + 1]
        if residual_capacity != 0:
            if reverse:
                edges_width.append(1)
                edges_colors.append("#67d627")
            else:
                edges_width.append(1)
                edges_colors.append("#f5b342")
        else:
            edges_width.append(0.01)
            edges_colors.append("#1b50a1")

        edge_labels[edge] = residual_capacity

    node_color = "#b6cef2"
    plt.title(f"residual graph step {step}")
    nx.draw(
        G_residual,
        pos,
        node_size=160,
        node_color=node_color,
        font_size=6,
        edge_color=edges_colors,
        width=edges_width,
        with_labels=True,
    )
    nx.draw_networkx_edge_labels(G_residual, pos, edge_labels=edge_labels, font_size=6)
    fig_path = os.path.join(dir_name, f"step_{step}__residual.pdf")
    plt.savefig(fig_path)
    plt.close()


def highlight_path(
    G_residual: nx.DiGraph,
    pos: dict,
    augmenting_path: list[int],
    dir_name: str,
    step: int,
    nodes: list[int],
    path_capacity: float,
) -> None:
    print(f"highlight path {augmenting_path}")

    # reformat augmenting path
    augmenting_path_edges = list()
    for index in range(len(augmenting_path) - 1):
        augmenting_path_edges.append(
            [augmenting_path[index], augmenting_path[index + 1]]
        )

    # print(augmenting_path_edges)
    edges_width = list()
    edges_colors = list()
    edge_labels = dict()
    for edge in G_residual.edges:
        if edge[0] == "Source":
            node = int(edge[1].split("-")[1])
            parsed_edge = [0, node + 1]
        elif edge[0] == "Sink":
            node = int(edge[1].split("-")[1])
            parsed_edge = [len(nodes) + 1, node + 1]
        elif edge[1] == "Sink":
            node = int(edge[0].split("-")[1])
            parsed_edge = [node + 1, len(nodes) + 1]
        elif edge[1] == "Source":
            node = int(edge[0].split("-")[1])
            parsed_edge = [node, 0]
        else:
            node_1 = int(edge[0].split("-")[1])
            node_2 = int(edge[1].split("-")[1])
            parsed_edge = [node_1 + 1, node_2 + 1]
        if parsed_edge in augmenting_path_edges:
            edges_width.append(1)
            edges_colors.append("#d627c2")
            edge_labels[edge] = path_capacity
            # print(parsed_edge)
        else:
            edges_width.append(0.01)
            edges_colors.append("#1b50a1")

    node_color = "#b6cef2"
    plt.title(f"augmenting path step {step}")
    nx.draw(
        G_residual,
        pos,
        node_size=160,
        node_color=node_color,
        font_size=6,
        edge_color=edges_colors,
        width=edges_width,
        with_labels=True,
    )
    nx.draw_networkx_edge_labels(G_residual, pos, edge_labels=edge_labels, font_size=6)
    fig_path = os.path.join(dir_name, f"step_{step}_augmenting.pdf")
    plt.savefig(fig_path)
    plt.close()


def build_residual_graph(
    G: nx.DiGraph,
    nodes: list[int],
    residual_capacities: np.ndarray,
    capacities: np.ndarray,
) -> nx.DiGraph:
    G_residual = G.copy()
    for node_1 in range(len(nodes) + 2):
        for node_2 in range(len(nodes) + 2):
            if not node_1 == node_2:
                residual_capacity = residual_capacities[node_1, node_2]
                initial_capacity = capacities[node_1, node_2]
                # set label
                if node_1 == 0:
                    label_1 = "Source"
                    label_2 = f"i-{node_2-1}"
                elif node_1 == len(nodes) + 1:
                    label_1 = "Sink"
                    label_2 = f"i-{node_2-1}"
                elif node_2 == 0:
                    label_1 = f"i-{node_1-1}"
                    label_2 = "Source"
                elif node_2 == len(nodes) + 1:
                    label_1 = f"i-{node_1-1}"
                    label_2 = "Sink"
                else:
                    label_1 = f"i-{node_1-1}"
                    label_2 = f"i-{node_2-1}"

                # process graph
                edge = (label_1, label_2)
                if residual_capacity == 0:
                    if edge in G_residual.edges:
                        G_residual.remove_edge(label_1, label_2)
                if residual_capacity != 0:
                    if initial_capacity == 0:
                        G_residual.add_edge(label_1, label_2)
    return G_residual
