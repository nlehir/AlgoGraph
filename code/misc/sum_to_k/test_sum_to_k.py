"""
Test our functions defined in functions.py
to assess whether two integers in a list
sum to a given value k.

We only test lists that have more than 3 elements.

To test, run pytest
"""
from functions import (
        sum_to_k,
        sum_to_k_in,
        sum_to_k_any_generator,
        sum_to_k_islice,
        sum_to_k_set,
        sum_to_k_set_any,
        )


TRUE_TUPLES = [
        ([10, 15, 3, 7], 17),
        ([12, 2, 3, 7, 10], 14),
        ([12, 2, 3, 7, 10], 13),
        ([3, 0, 1], 3),
        ([3, 0, 1], 1),
        ]

FALSE_TUPLES = [
        ([3, 0, 1], 6),
        ([3, 0, 1], 0),
        ([3, 0, 1], 9),
        ([10, 15, 3, 7], 6),
        ([10, 15, 3, 7], 0)
        ]


def test_sum_to_k() -> None:
    for list_, value in TRUE_TUPLES:
        assert sum_to_k(list_, value)
    for list_, value in FALSE_TUPLES:
        assert not sum_to_k(list_, value)

def test_sum_to_k_in() -> None:
    for list_, value in TRUE_TUPLES:
        assert sum_to_k_in(list_, value)
    for list_, value in FALSE_TUPLES:
        assert not sum_to_k_in(list_, value)

def test_sum_to_k_any_generator() -> None:
    for list_, value in TRUE_TUPLES:
        assert sum_to_k_any_generator(list_, value)
    for list_, value in FALSE_TUPLES:
        assert not sum_to_k_any_generator(list_, value)

def test_sum_to_k_islice() -> None:
    for list_, value in TRUE_TUPLES:
        assert sum_to_k_islice(list_, value)
    for list_, value in FALSE_TUPLES:
        assert not sum_to_k_islice(list_, value)

def test_sum_to_k_set() -> None:
    for list_, value in TRUE_TUPLES:
        assert sum_to_k_set(list_, value)
    for list_, value in FALSE_TUPLES:
        assert not sum_to_k_set(list_, value)

def test_sum_to_k_set_any() -> None:
    for list_, value in TRUE_TUPLES:
        assert sum_to_k_set_any(list_, value)
    for list_, value in FALSE_TUPLES:
        assert not sum_to_k_set_any(list_, value)
