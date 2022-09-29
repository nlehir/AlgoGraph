""""
    return one shortest path
"""
from termcolor import colored

# the graph is undirected
neighboring_nodes = [
    [1, 3, 4],  # neighbors of 0
    [0, 2, 3],  # neighbors of 1
    [1, 5],  # neighbors of 2
    [0, 1, 5],  # neighbors of 3
    [0],  # neighbors of 4
    [2, 3],
]  # neighbors of 5


one_shortest_path = [None] * 6
one_shortest_path[0] = [0]


for step in range(1, 6):
    print(
        colored(f"\n---\nbuild paths of length : {step}\n---", "blue", attrs=["bold"])
    )
    for node in range(1, 6):
        if one_shortest_path[node] is None:
            for neighbor in neighboring_nodes[node]:
                c = one_shortest_path[neighbor]
                if c is not None and len(c) == step:
                    """
                    EDIT
                    """
                    print(f"node : {node}")
                    print(f"neighbor : {neighbor}")
                    print(f"path to neighbor : {c}")
                    print(
                        colored(
                            f"build one shortest path to {node}",
                            "green",
                            attrs=["bold"],
                        )
                    )
                    one_shortest_path[node] = c + [1]
                    print(one_shortest_path[node])


def print_one_shortest_path(destination: int) -> None:
    print(f"one shortest path to {destination} is :")
    print(one_shortest_path[destination])


print_one_shortest_path(1)
# print_one_shortest_path(2)
# print_one_shortest_path(3)
# print_one_shortest_path(4)
# print_one_shortest_path(5)
