""""
    Check if there is a path of a certain
    length to arrive to a destination
"""
from termcolor import colored

neighboring_nodes = [
    [1, 3, 4],  # neighbors of 0
    [0, 2, 3],  # neighbors of 1
    [1, 5],  # neighbors of 2
    [0, 1, 5],  # neighbors of 3
    [0],  # neighbors of 4
    [2, 3],
]  # neighbors of 5


def exists_path(destination, path_length, depth):
    padding = "---" * depth
    if path_length == 0:
        exists = False
    else:
        exists = False
    if exists:
        print(padding + f" destination {destination}, length {path_length}")
    return exists


def test_existence(destination, path_length):
    if exists_path(destination, path_length, 0):
        print(
            colored(
                f"there is a path of length {path_length} from 0 to {destination}\n",
                "blue",
                attrs=["bold"],
            )
        )
    else:
        print(
            colored(
                f"no path of length {path_length} from 0 to {destination}\n",
                "yellow",
                attrs=["bold"],
            )
        )


# test_existence(5, 5)
test_existence(5, 4)
test_existence(5, 3)
test_existence(5, 2)
test_existence(5, 1)
