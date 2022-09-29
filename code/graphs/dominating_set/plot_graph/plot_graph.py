import networkx as nx
import os
import matplotlib.pyplot as plt

# plotting params
alpha = 0.7
node_size = 200
edge_color = "#1b50a1"
node_color = "#b6cef2"


def plot_subset(step,
                nodes,
                edges,
                dominated_nodes,
                selected_nodes,
                graph_name,
                method="standard"):
    """
    function to highlight the dominated nodes
    and save the graph image
    """
    # print("plot graph")
    G = nx.Graph()

    # reformat edges as a list of tuples
    edges = [set(edge) for edge in edges]

    # set colors
    # dominated_nodes_color=["#8332a8"]
    # dominated_nodes_color=["#D8D56d"]
    dominated_nodes_color = ["#d5628c"]
    # selected_nodes_color = ["#a69e35"]
    selected_nodes_color = ["#c5cf3a"]

    # remove the selected nodes from
    # the dominated nodes for plotting
    dominated_nodes_strict = [node for node in dominated_nodes if node not in
                              selected_nodes]

    G.add_edges_from(edges)

    # visualize the graph
    dir_name = f"images/{graph_name}"
    if method == "standard":
        graph_name = f"{dir_name}/greedy_{step}.pdf"
    elif method == "bis":
        graph_name = f"{dir_name}/greedy_bis_{step}.pdf"
    elif method == "ter":
        graph_name = f"{dir_name}/greedy_ter_{step}.pdf"
    else:
        raise ValueError("wrong algorithm method")

    graph_title = f"""Subset size: {len(selected_nodes)}
    Algo step: {step}
    Method: {method}"""

    plt.title(graph_title, fontsize=9)
    # we give a seed to the layout engine
    # in order to always have the same layout
    # fot a given  graph.
    # Otherwise, a random seed is used.
    pos = nx.spring_layout(G, seed=1)
    # if you want a circular layout
    # pos=nx.circular_layout(G)
    nx.draw(G,
            pos=pos,
            node_size=node_size,
            node_color=node_color,
            edge_color=edge_color,
            font_size=8,
            width=1,
            alpha=alpha,
            with_labels=True)

    # draw selected nodes
    nx.draw_networkx_nodes(G,
                           pos,
                           nodelist=selected_nodes,
                           node_color=selected_nodes_color,
                           node_size=100,
                           alpha=alpha)

    # draw dominated nodes
    nx.draw_networkx_nodes(G,
                           pos,
                           nodelist=dominated_nodes_strict,
                           node_color=dominated_nodes_color,
                           node_size=100,
                           alpha=alpha)

    plt.tight_layout()
    plt.axis('off')
    plt.savefig(graph_name)
    plt.close()


def plot_initial_graph(edges,
                       graph_name):
    """
    function to show the initial graph
    and save a representation to a pdf file
    """
    # print("plot graph")
    G = nx.Graph()

    # reformat edges as a list of tuples
    edges = [set(edge) for edge in edges]

    G.add_edges_from(edges)

    # visualize the graph
    dir_name = f"images/{graph_name}"
    graph_name = f"{dir_name}/graph_initial.pdf"
    graph_title = f"\nInitial graph"

    plt.title(graph_title, fontsize=9)
    # we give a seed to the layout engine
    # in order to always have the same layout
    # fot a given  graph.
    # Otherwise, a random seed is used.
    pos = nx.spring_layout(G, seed=1)
    # if you want a circular layout
    # pos=nx.circular_layout(G)
    nx.draw(G,
            pos=pos,
            node_size=node_size,
            node_color=node_color,
            edge_color=edge_color,
            font_size=8,
            width=1,
            alpha=alpha,
            with_labels=True)

    plt.tight_layout()
    plt.axis('off')
    plt.savefig(graph_name)
    plt.close()
