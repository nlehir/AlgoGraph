""""
    Check if there is a path of a certain
    length to arrive to a destination
"""
from termcolor import colored

from input_graphs import G, pos, G2, pos2

"""
Choose the graph to process
"""
GRAPH = G2
POS = pos2
# GRAPH = G
# POS = pos


def exists_path(destination: int, path_length: int) -> bool:
    """
    EDIT
    """
    if path_length == 0:
        exists = False
    else:
        exists = False   
    if exists:
        print(f"found path to {destination}, length {path_length}")
    return exists


def test_existence(destination: int, path_length: int) -> None:
    print(f"\nLook for a path of length {path_length} from 0 to {destination}")
    if exists_path(destination, path_length):
        print(
            colored(
                f"there is a path of length {path_length} from 0 to {destination}",
                "blue",
                attrs=["bold"],
            )
        )
    else:
        print(
            colored(
                f"no path of length {path_length} from 0 to {destination}",
                "yellow",
                attrs=["bold"],
            )
        )


def main():
    test_existence(destination=5, path_length=5)
    test_existence(destination=5, path_length=4)
    test_existence(destination=5, path_length=3)
    test_existence(destination=5, path_length=2)
    test_existence(destination=5, path_length=1)

if __name__ == "__main__":
    main()
