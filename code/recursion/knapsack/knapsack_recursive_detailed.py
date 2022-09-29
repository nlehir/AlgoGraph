"""
    recursive function to see if a certain value is contained in a sublist
    (subset sum problem)
"""
from termcolor import colored


def exists_sublist(values_list, target_value, depth):
    """
        Checks if the list of values can be used in order
        to obtain a certain targe.

        :param values_list (list): list of available objects
        :target_value (int): target
        :depth (int): padding depth
    """
    padding = "---"*depth
    print(colored(padding + f" depth {depth}", "blue"))
    print(padding + f" values : {values_list}")
    print(padding + f" target : {target_value}")
    depth += 1
    if len(values_list) == 0:
        if not target_value == 0:
            print(
                padding+f" empty list and target value {target_value} nonzero : ", end="")
            print(colored("go back\n", "blue", attrs=["bold"]))
        return target_value == 0
    else:
        return (1==2) or (2==3)


def test_list_target(values, target_value):
    if exists_sublist(values, target_value, 0):
        print(colored(f"{values} contains a sublist of value {target_value}",
                      "green",
                      attrs=["bold"]))
    else:
        print(colored(f"{values} does NOT contain a sublist of value {target_value}",
                      "yellow",
                      attrs=["bold"]))


values_1 = [2, 7, -1, 9]
target_value_1 = 16
target_value_2 = 4
values_2 = [1, 23, 14, 7, -17, 3, 5, 179, 358, 25, 11, 2, -36, 17, 34, 23, -76]
target_value_3 = 65

test_list_target(values_1, 16)
test_list_target(values_1, 20)
# test_list_target(values_1, 4)
# test_list_target(values_2, 65)
# test_list_target(values_2, -31)
# test_list_target(values_2, 1980)
