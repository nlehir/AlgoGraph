import networkx as nx
import os
from termcolor import colored

def clean_name(name):
    name = name.replace('.', "_")
    name = name.replace(" ", "_")
    return name

def create_folder_if_missing(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def define_graph_name(params, graph_type):
    parsed_parameters = [f"{key}={params[key]}" for key in params]
    params_str = "_".join(parsed_parameters)
    name = f"{graph_type}_{params_str}"
    name = clean_name(name=name)
    return name

def define_graph(graph_type: str, params: dict) -> dict:
    if graph_type == "PCG":
        G = nx.generators.powerlaw_cluster_graph(
                **params
        )
    else:
        message = "Unknown graph type: {graph_type}"
        message = colored(message, color="yellow")
        raise ValueError(message)
    graph_name = define_graph_name(params=params, graph_type=graph_type)
    output = dict(
            G=G,
            graph_name=graph_name,
            )
    return output

def define_fig_path(
        problem,
        graph_name,
        method,
        step,
        initial=False,
        ):
    fig_name = f"{method}_{step}.pdf"
    if initial == True:
        fig_name = f"initial_graph.pdf"
    dir_name = os.path.join(
            problem,
            "images",
            f"{graph_name}",
            )
    create_folder_if_missing(folder_name=dir_name)
    fig_path = os.path.join(dir_name, fig_name)
    return fig_path
