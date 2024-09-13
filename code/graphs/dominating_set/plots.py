import matplotlib.pyplot as plt
import networkx as nx

from utils import define_fig_path

# plotting params
alpha = 0.7
node_size = 200
edge_color = "#1b50a1"
node_color = "#b6cef2"


def plot_subset(
    step: int,
    edges,
    dominated_nodes: set,
    selected_nodes: list,
    graph_name: str,
    graph_type: str,
    method="standard",
):
    """
    Highlight the dominated nodes
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
    dominated_nodes_strict = [
        node for node in dominated_nodes if node not in selected_nodes
    ]

    G.add_edges_from(edges)

    # visualize the graph

    graph_title = (
        f"Subset size: {len(selected_nodes)}"
        f"\nalgo step: {step}"
        f"\nmethod: {method}"
        f"\ngraph type: {graph_type}"
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
        node_size=node_size,
        node_color=node_color,
        edge_color=edge_color,
        font_size=8,
        width=1,
        alpha=alpha,
        with_labels=True,
    )

    # draw selected nodes
    nx.draw_networkx_nodes(
        G,
        pos,
        nodelist=selected_nodes,
        node_color=selected_nodes_color,
        node_size=100,
        alpha=alpha,
    )

    # draw dominated nodes
    nx.draw_networkx_nodes(
        G,
        pos,
        nodelist=dominated_nodes_strict,
        node_color=dominated_nodes_color,
        node_size=100,
        alpha=alpha,
    )

    plt.tight_layout()
    plt.axis("off")
    fig_path = define_fig_path(
        problem="dominating_set",
        graph_name=graph_name,
        method=method,
        step=step,
    )
    plt.savefig(fig_path)
    plt.close()


def plot_initial_graph(
    G: nx.Graph,
    graph_name: str,
    graph_type: str,
):
    """
    function to show the initial graph
    and save a representation to a pdf file
    """
    edges = G.edges

    print("Plot initial graph")
    # reformat edges as a list of tuples
    edges = [set(edge) for edge in edges]

    G.add_edges_from(edges)

    graph_title = f"Initial graph\n{graph_type} graph"

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
        node_size=node_size,
        node_color=node_color,
        edge_color=edge_color,
        font_size=8,
        width=1,
        alpha=alpha,
        with_labels=True,
    )

    fig_path = define_fig_path(
        problem="dominating_set",
        graph_name=graph_name,
        method=None,
        step=None,
        initial=True,
    )

    plt.tight_layout()
    plt.axis("off")
    plt.savefig(fig_path)
    plt.close()
