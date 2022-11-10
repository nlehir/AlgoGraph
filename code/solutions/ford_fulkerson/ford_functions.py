import networkx
import numpy as np
from plot_graphs import build_residual_graph, highlight_path, show_residual_network_nx
from termcolor import colored


def apply_ford_fulkerson(
    nodes: list[int],
    inner_capacities: np.ndarray,
    source_capacities: np.ndarray,
    sink_capacities: np.ndarray,
    dir_name: str,
    G: networkx.DiGraph,
    pos: dict,
) -> None:
    """
    Apply Ford Fulkerson algorithm.


    1) We first build a matrix containing all the capacities.
    ---------------------------------------------------------

    The capacities between the source and the inner nodes
    are contained on row 0.
    The capacities between inner nodes and the sink
    are contained on the last row.
    The capacities between inner nodes are contained between
    row 1 and row len(nodes)-1.

    2) We then perform the Ford Fulkerson algorithm
    -----------------------------------------------

    At each step of the algorithm, we do the following :

    --------
    a) Build the residual graph from the initial capacities and
    the current flow.
    - The function show_residual_network() plots the network.

    --------
    b) Look for augmenting paths in the residual graph.
    - The function find_augmenting_paths() looks for augmenting paths
    by performing a search in the graph.
    This could be optimized.
    - The function highlight_path() plots the chosen
    augmenting path.

    --------
    c) If we found an augmenting path, we modify the flow.
    - This is done in the function augment_flow()
    - The function check_flow() tests that the flow
    complies with the hypothesis of a flow network.

    d) Otherwise, we did not find an augmenting path.
    This means that our flow is optimal.
    """

    # build a complete matrix of capacities
    capacities = np.zeros((len(nodes) + 2, len(nodes) + 2))
    # add capacities between source and inner nodes
    capacities[0, 1:-1] = source_capacities
    # add capacities between inner nodes and sink
    capacities[1:-1, -1] = sink_capacities
    # add capacities between inner nodes
    capacities[1 : len(nodes) + 1, 1 : len(nodes) + 1] = inner_capacities

    # initial flow set to 0
    # the total number of vertices in the graph
    # is len(nodes)+2 since we must take into account
    # the source and the sink.
    flow = np.zeros((len(nodes) + 2, len(nodes) + 2))

    # Algorithm iterations
    step = 1
    while True:
        print(f"===================\nAlgorithm step : {step}")

        # compute the residual capacities
        residual_capacities = capacities - flow

        # build and show the residual network
        # it might have more edges since we changed the capacities
        G_residual = build_residual_graph(G, nodes, residual_capacities, capacities)
        show_residual_network_nx(G_residual, pos, residual_capacities, dir_name, step)

        # look for augmenting paths
        augmenting_paths = find_augmenting_paths(residual_capacities)
        # if there exists some augmenting paths,
        # then the return list is not empty
        if augmenting_paths:
            print("found augmenting paths in residual graph")
            # update the flow
            flow = augment_flow(
                flow,
                residual_capacities,
                augmenting_paths,
                dir_name,
                G_residual,
                pos,
                step,
                nodes,
            )
            residual_capacities = capacities - flow

            # verify if the flow matrix respects
            # the definition of a flow
            check_flow(flow, nodes, capacities)

            # compute the value of the flow
            # it corresponds to what goes out of the source
            flow_value = sum(flow[0, :])
            print(f"flow value {flow_value}\n\n\n")

            # update algo step
            step += 1
        else:
            print("\n=====================\n")
            print("found no augmenting path : flow is optimal")
            print(f"stopping at step {step}")
            print(f"flow value: {flow_value}")
            print("\n=====================\n")
            break


def check_flow(flow: np.ndarray, nodes: list[int], capacities: np.ndarray) -> None:
    """
    Check if the flow complies with the constraints
    of a flow network
    """
    print("---\nchecking flow")
    inner_flow = flow[1:-1, 1:-1]

    # -------------
    # First check
    # -------------
    # check if for all nodes u and v,
    # that are different from the source,
    # and different from the sink, we have
    # f(u,v)=-f(v,u)
    # We can do it using matrices
    antisymmetry_check = np.transpose(inner_flow) == -inner_flow
    flow_check_1 = antisymmetry_check.all()
    if flow_check_1:
        print(
            colored(
                "First check ok : flow matrix is antisymmetric.", "blue", attrs=["bold"]
            )
        )
    else:
        print(
            colored(
                "Flow not ok ! Not symmetrical.",
                "yellow",
                attrs=["bold"],
            )
        )

    # -------------
    # Second check
    # -------------
    # flow conservation
    flow_check_2 = list()
    for node in range(1, len(nodes) + 1):
        flow_check_2.append(sum(flow[:, node]) == 0)
    if all(flow_check_2):
        print(colored("Second check ok : flow is conserved.", "blue", attrs=["bold"]))
    else:
        print(
            colored(
                "Flow not ok ! flow not conserved.",
                "yellow",
                attrs=["bold"],
            )
        )

    # -------------
    # Third check
    # -------------
    # test that the flow on each edge does node exceed
    # the capacity of the edge
    comparison = flow <= capacities
    flow_check_3 = comparison.all()
    if flow_check_3:
        print(
            colored(
                "Third check ok : flow does not exceed capacity on each edge.",
                "blue",
                attrs=["bold"],
            )
        )
    else:
        print(
            colored(
                "Flow not ok ! The flow on one edge exceeds its capacity.",
                "yellow",
                attrs=["bold"],
            )
        )

    print("---\n")


def augment_flow(
    flow: np.ndarray,
    residual_capacities: np.ndarray,
    augmenting_paths: list[list],
    dir_name: str,
    G_residual: networkx.DiGraph,
    pos: dict,
    step: int,
    nodes: list[int],
) -> np.ndarray:
    """
    Augment the flow thanks to an augmenting path
    """
    print("---\naugment flow")

    # -----------
    # first choose an augmenting path randomly
    # from the ones we found.
    # you can also choose the last one, for instance
    augmenting_path = augmenting_paths.pop()
    # however, several options are possible as for the choice of the augmenting
    # path
    print(f"chosen augmenting path : {augmenting_path}")

    # compute the capacity of this path.
    augmenting_path_capacities = list()
    for node_index in range(len(augmenting_path) - 1):
        node_1 = augmenting_path[node_index]
        node_2 = augmenting_path[node_index + 1]
        augmenting_path_capacities.append(residual_capacities[node_1][node_2])
    # The capacit of a path is the minimum of the capacities
    # of each edge.
    path_capacity = min(augmenting_path_capacities)
    print(f"augmenting path capacity : {path_capacity}")

    # highlight this path in the graph
    highlight_path(
        G_residual, pos, augmenting_path, dir_name, step, nodes, path_capacity
    )

    # finally augment the flow
    nb_nodes = len(nodes) + 2
    added_flow_value = path_capacity
    added_flow = np.zeros((nb_nodes, nb_nodes))
    for node_index in range(len(augmenting_path) - 1):
        node_1 = augmenting_path[node_index]
        node_2 = augmenting_path[node_index + 1]
        added_flow[node_1, node_2] = added_flow_value
        added_flow[node_2, node_1] = -added_flow_value
    return flow + added_flow


def find_augmenting_paths(residual_capacities: np.ndarray) -> list[int]:
    """
    Look for an augmenting paths in the residual graph
    """
    # we want to go from the source to the sink
    # using edges in the residual graph
    last_index = residual_capacities.shape[1] - 1
    print("---\nLook for augmenting paths in the residual graph")
    print("source = 0")
    print(f"sink = {last_index}")
    print("---")
    augmenting_paths = list()
    stack = [(0, [0])]
    while stack:
        print(f"\npop last element from stack")
        (node, path) = stack.pop()
        # be careful, we put all the capacities in a single matrix
        # thus :
        # source is on rank 0
        # node 0 is on rank 1
        # node 1 is on rank 2
        # node 2 is on rank 3
        # node len(nodes) -1 is on rank len(nodes)
        # sink is on rank len(nodes)+1
        next_available_nodes = np.where(residual_capacities[node, :] > 0)[0]
        print(f"node: {node}")
        print(f"next available nodes: {next_available_nodes}")
        for next_node in next_available_nodes:
            print(f"  next node {next_node}")
            if next_node == last_index:
                new_augmenting_path = path + [next_node]
                print(f"  append {new_augmenting_path} to augmenting paths list")
                augmenting_paths.append(new_augmenting_path)
            else:
                # avoid loops !
                if next_node not in path:
                    new_path = path + [next_node]
                    print(f"  append {new_path} to stack")
                    stack.append((next_node, new_path))
    return augmenting_paths
