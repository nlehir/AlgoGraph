from termcolor import colored

GRAPH_TYPE = "PCG"

if GRAPH_TYPE == "PCG":
    """
    https://networkx.org/documentation/stable/reference/generated/networkx.generators.random_graphs.powerlaw_cluster_graph.html
    """
    PARAMS = dict(
        n=40,
        m=3,
        p=0.1,
        seed=None,
    )
else:
    message = "Unknown graph type: {GRAPH_TYPE}"
    message = colored(message, color="yellow")
    raise ValueError(message)
