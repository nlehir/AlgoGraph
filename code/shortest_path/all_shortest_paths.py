""""
    return one shortest path
"""
from termcolor import colored

# the graph is undirected
neighboring_nodes = [
    [1, 3, 4],  # neighbors of 0
    [0, 2, 3],  # neighbors of 1
    [1, 5],  # neighbors of 2
    [0, 1, 5, 6],  # neighbors of 3
    [0, 6],  # neighbors of 4
    [2, 3, 6],  # neighbors of 5
    [4, 5, 3, 7],  # neighbors of 6
    [6],
]  # neighbors of 7

number_of_nodes = 7

shortest_paths = [[] for i in range(number_of_nodes + 1)]
shortest_paths[0] = [[0]]


for step in range(1, number_of_nodes + 1):
    print(
        colored(f"\n---\nbuild paths of length : {step}\n---", "blue", attrs=["bold"])
    )
    for node in range(1, number_of_nodes + 1):
        if shortest_paths[node] == []:
            for neighbor in neighboring_nodes[node]:
                shtr_pths_to_ngbr = shortest_paths[neighbor]
                if shtr_pths_to_ngbr != [] and len(shtr_pths_to_ngbr[0]) == step:
                    """
                        EDIT
                    """
                    print(f"node : {node}")
                    print(f"neighbor : {neighbor}")
                    print(f"shortest paths to neighbor : {shtr_pths_to_ngbr}")
                    print(
                        colored(
                            f"build one shortest path to {node}",
                            "green",
                            attrs=["bold"],
                        )
                    )
                    for path in shtr_pths_to_ngbr:
                        new_shortest_path = path + [3]
                        shortest_paths[node].append(path)
                        print("add : ")
                        print(new_shortest_path)


def print_shortest_paths(destination):
    print(f"the shortest paths to {destination} are")
    print(shortest_paths[destination])


print_shortest_paths(1)
print_shortest_paths(2)
print_shortest_paths(3)
print_shortest_paths(4)
print_shortest_paths(5)
print_shortest_paths(6)
print_shortest_paths(7)
