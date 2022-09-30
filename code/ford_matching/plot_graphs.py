"""
    Utility functions in order to
    visualize the graphs
"""
import networkx as nx
import matplotlib.pyplot as plt


def highlight_path(G_residual,
                   pos,
                   augmenting_path,
                   dir_name,
                   step,
                   nodes,
                   nodes_1,
                   nodes_2,
                   path_capacity):
    print(f"highlight path {augmenting_path}")

    # reformat augmenting path
    augmenting_path_edges = list()
    for index in range(len(augmenting_path)-1):
        augmenting_path_edges.append(
            [augmenting_path[index], augmenting_path[index+1]])

    edges_width = list()
    edges_colors = list()
    for edge in G_residual.edges:
        if edge[0] == "Source":
            node_group_1 = int(edge[1].split('-')[1])
            parsed_edge = [0, node_group_1+1]
        elif edge[0] == "Sink":
            node_group_2 = int(edge[1].split('-')[1])
            parsed_edge = [len(nodes)+1, node_group_2+1]
        elif edge[1] == "Sink":
            node_group_2 = int(edge[0].split('-')[1])
            parsed_edge = [node_group_2+1, len(nodes)+1]
        elif edge[1] == "Source":
            node_group_1 = int(edge[0].split('-')[1])
            parsed_edge = [node_group_1, 0]
        elif edge[0].split('-')[0] == "2":
            node_group_2 = int(edge[0].split('-')[1])
            node_group_1 = int(edge[1].split('-')[1])
            parsed_edge = [node_group_2+1, node_group_1+1]
        else:
            node_group_1 = int(edge[0].split('-')[1])
            node_group_2 = int(edge[1].split('-')[1])
            parsed_edge = [node_group_1+1, node_group_2+1]
        if parsed_edge in augmenting_path_edges:
            edges_width.append(1)
            edges_colors.append("#d627c2")
        else:
            edges_width.append(0.01)
            edges_colors.append("#1b50a1")

    node_color = "#b6cef2"
    plt.title(f"augmenting path step {step}")
    nx.draw(G_residual,
            pos,
            node_size=160,
            node_color=node_color,
            font_size=6,
            edge_color=edges_colors,
            width=edges_width,
            with_labels=True)
    plt.savefig(dir_name+f"/step_{step}_augmenting.pdf")
    plt.close()


def build_residual_graph(G,
                         nodes_1,
                         nodes_2,
                         residual_capacities,
                         capacities):
    G_residual = G.copy()
    nodes = nodes_1+nodes_2
    for node_1 in range(len(nodes)+2):
        for node_2 in range(len(nodes)+2):
            if not node_1 == node_2:
                residual_capacity = residual_capacities[node_1, node_2]
                initial_capacity = capacities[node_1, node_2]
                if node_1 == 0:
                    label_1 = "Source"
                    label_2 = f"1-{node_2-1}"
                elif node_1 == len(nodes)+1:
                    label_1 = "Sink"
                    label_2 = f"2-{node_2-1}"
                elif node_2 == 0:
                    label_1 = f"1-{node_1-1}"
                    label_2 = "Source"
                elif node_2 == len(nodes)+1:
                    label_1 = f"2-{node_1-1}"
                    label_2 = "Sink"
                else:
                    if node_1 < node_2:
                        label_1 = f"1-{node_1-1}"
                        label_2 = f"2-{node_2-1}"
                    elif node_2 < node_1:
                        label_1 = f"2-{node_1-1}"
                        label_2 = f"1-{node_2-1}"

                # process
                edge = (label_1, label_2)
                if residual_capacity == 0:
                    if edge in G_residual.edges:
                        G_residual.remove_edge(label_1, label_2)
                if residual_capacity != 0:
                    if initial_capacity == 0:
                        G_residual.add_edge(label_1, label_2)

    return G_residual


def show_flow(flow, dir_name, step, flow_value, nodes_1, nodes_2):

    # copy of the graph to edit the plot

    # we dont want node 1 to be the sink
    nodes = nodes_1+nodes_2
    for node_1 in range(len(nodes)+1):
        for node_2 in range(1, len(nodes)+2):
            if not node_1 == node_2:
                edge_flow = flow[node_1, node_2]
                if edge_flow > 0:
                    if node_1 == 0:
                        label_1 = "Source"
                        label_2 = "1- {}".format(node_2-1)
                    elif node_2 == len(nodes)+1:
                        label_1 = "2- {}".format(node_1-1)
                        label_2 = "Sink"
                    else:
                        if node_1 < node_2:
                            label_1 = "1- {}".format(node_1-1)
                            label_2 = "2- {}".format(node_2-1)
                        elif node_2 < node_1:
                            label_1 = "2- {}".format(node_1-1)
                            label_2 = "1- {}".format(node_2-1)


def show_residual_network_nx(G_residual, pos, residual_capacities, capacities, nodes_1,
                             nodes_2,
                             dir_name, step):

    edges_width = list()
    edges_colors = list()

    for edge in G_residual.edges:
        reverse = False
        if edge[0] == "Source":
            node_group_1 = int(edge[1].split('-')[1])
            residual_capacity = residual_capacities[0, node_group_1+1]
        elif edge[0] == "Sink":
            reverse = True
            node_group_2 = int(edge[1].split('-')[1])
            residual_capacity = residual_capacities[-1, node_group_2+1]
        elif edge[1] == "Sink":
            node_group_2 = int(edge[0].split('-')[1])
            residual_capacity = residual_capacities[node_group_2+1, -1]
        elif edge[1] == "Source":
            reverse = True
            node_group_1 = int(edge[0].split('-')[1])
            residual_capacity = residual_capacities[node_group_1+1, 0]
        elif edge[0].split('-')[0] == "2":
            reverse = True
            node_group_2 = int(edge[0].split('-')[1])
            node_group_1 = int(edge[1].split('-')[1])
            residual_capacity = residual_capacities[node_group_2 +
                                                    1, node_group_1+1]
        else:
            node_group_1 = int(edge[0].split('-')[1])
            node_group_2 = int(edge[1].split('-')[1])
            residual_capacity = residual_capacities[node_group_1 +
                                                    1, node_group_2+1]
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

    node_color = "#b6cef2"
    plt.title(f"residual graph step {step}")
    nx.draw(G_residual,
            pos,
            node_size=160,
            node_color=node_color,
            font_size=6,
            edge_color=edges_colors,
            width=edges_width,
            with_labels=True)
    # plt.tight_layout()
    plt.savefig(dir_name+f"/step_{step}__residual.pdf")
    plt.close()
