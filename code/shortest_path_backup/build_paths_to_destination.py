""""
    Build all paths arriving to destination 5
"""

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
paths = [[[0]]]
paths_to_destination, path_length = list(), 0

while paths_to_destination == list():
    path_length += 1
    # build paths as before
    new_paths = list()
    for path in paths[path_length - 1]:
        for ngbr in neighboring_nodes[path[-1]]:
            new_paths.append(path + [ngbr])

    # append the paths to the list of paths as before
    paths.append(new_paths)
    # check is the path goes to the destination
    paths_to_destination = [path for path in paths[path_length] if path[-1] == 5]


print(paths_to_destination)
