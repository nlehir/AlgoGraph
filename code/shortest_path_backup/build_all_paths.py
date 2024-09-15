""""
    Build all the paths from 0
"""

# the graph is undirected
neighboring_nodes = [
    [1, 3, 4],  # neighbors of 0
    [0, 2, 3],  # neighbors of 1
    [1, 5],  # neighbors of 2
    [0, 1, 5],  # neighbors of 3
    [0],  # neighbors of 4
    [2, 3],
]  # neighbors of 5

# paths of length 0
# a path will be coded as a list
# we will have a list of paths lengths
# each path length corresponds to a list
# so we have a list of lists of lists
paths = [[[0]]]

for path_length in range(1, 6):
    print(f"building paths of length {path_length}")
    new_paths = list()
    """
    EDIT
    """
    for path in paths[path_length - 1]:
        for ngbr in neighboring_nodes[path[-1]]:
            new_paths.append([1])
    # append the paths to the list of paths
    paths.append(new_paths)


print(f"paths of length 1 : {paths[1]}")
print(f"paths of length 2 : {paths[2]}")
print(f"paths of length 4 : {paths[4]}")
