"""
Several possible functions that assess whether two integers in a list
sum to a given value k.

The functions are tested in test_sum_to_k.py

https://wiki.python.org/moin/TimeComplexity
"""
import itertools


def sum_to_k(list_: list[int], k: int) -> bool:
    """
    Simple, intuitive implementation
    """
    for index, value in enumerate(list_):
        for y in list_[index+1:]:
            if value + y == k:
                return True
    return False


def sum_to_k_in(list_: list[int], k: int) -> bool:
    """
    Use the in keyword to test membership, that is written in C,
    instead of using a for loop.
    """
    for index, value in enumerate(list_):
        if k - value in list_[index+1:]:
            return True
    return False


def sum_to_k_any_generator(list_: list[int], k: int) -> bool:
    """
    Use a generator, which unlike a list, does not store
    all its values in memory but generates them on the fly.

    Hence this function is more memory efficient, not necessary faster.
    list_[index+1] creates a temporary list.

    Also use the any keyword.
    """
    return any(
            k - value in list_[index+1:]
            for index, value in enumerate(list_)
            )


def sum_to_k_islice(list_: list[int], k: int) -> bool:
    """
    Uses itertools
    """
    return any(
            k - value in itertools.islice(list_, index+1, None)
            for index, value in enumerate(list_)
            )

def sum_to_k_set(list_: list[int], k: int) -> bool:
    """
    Use sets, which have a membership test that is O(1)
    (more details on the O notation later in the course)
    They are similar to hash tables.

    https://stackoverflow.com/questions/3949310/how-is-set-implemented

    https://github.com/python/cpython/blob/main/Objects/setobject.c
    """
    seen = set()
    for n in list_:
        if k - n in seen:
            return True
        seen.add(n)
    return False


def sum_to_k_set_any(list_: list[int], k: int) -> bool:
    """
    Use sets and the any keyword.
    """
    seen = set()
    return any(
       k - n in seen or seen.add(n)
       for n in list_
       )
