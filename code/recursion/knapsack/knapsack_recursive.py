"""
    recursive function to see if a certain value is contained in a sublist
    (subset sum problem)
"""


def exists_sublist(values_list: list, target_value: int) -> bool:
    """
        Checks if the list of values can be used in order
        to obtain a certain targe.

        :param values_list (list): list of available objects
        :target_value (int): target

        EDIT THIS FUNCTION
    """
    if len(values_list) == 0:
        return target_value == 0
    else:
        return (1==2) or (2==3)


def test_list_target(values: list, target_value: int):
    if exists_sublist(values, target_value):
        print(f"{values} contains a sublist of value {target_value}")
    else:
        print(f"{values} does NOT contain a sublist of value {target_value}")


values_1 = [2, 7, -1, 9]
target_value_1 = 16
target_value_2 = 4
values_2 = [1, 23, 14, 7, -17, 3, 5, 179, 358, 25, 11, 2, -36, 17, 34, 23, -76]
target_value_3 = 65
target_value_4 = -31
target_value_5 = 1980

test_list_target(values_1, target_value_1)
test_list_target(values_1, target_value_2)
test_list_target(values_2, target_value_3)
test_list_target(values_2, target_value_4)
test_list_target(values_2, target_value_5)
