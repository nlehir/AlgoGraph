"""
Test insertion_sort sorts the lists correclty

To test, run pytest
"""
from insertion_sort import (
        insertion_sort,
        )


INPUT_LISTS = [
        [1, 4, 3, 2],
        [-1, 4, 3, -2],
        [-10, -22.2, 3, 12],
        ]


def test_insertion_sort() -> None:
    for list_ in INPUT_LISTS:
        sorted_by_insertion_sort = insertion_sort(list_)[1]
        assert sorted_by_insertion_sort == sorted(list_)
