"""
Study the speed of the greedy algorithm as a function of the data structure.
"""

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

