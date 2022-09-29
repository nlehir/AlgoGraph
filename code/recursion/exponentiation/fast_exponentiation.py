"""
    Fast exponentiation algorithm
"""
from termcolor import colored
# from time import time
# import math


def fast_exponentiation(a: int, n: int) -> int:
    """
        EDIT THIS FUNCTION
    """
    if n == 0:
        return 1
    if n % 2 == 0:
        return fast_exponentiation(a, n-1)
    else:
        return fast_exponentiation(a, n-1)


def test_fast_exp(a: int, n: int) -> None:
    """
    Tests the correctness recursive method
    by comparing with the power function
    from the math module (standard library)

    Also compares computation times.

    :param a (int): integer to be exponentiated
    :param n (int): power

    """
    # fast exp
    recursive = fast_exponentiation(a, n)
    # double splat
    double_splat = a**n
    if recursive == double_splat:
        print(colored(f"a={a}, n={n} result ok: {double_splat}", "blue", attrs=["bold"]))
    else:
        print(colored(f"a={a}, n={n} wrong result: {double_splat} vs " +
                      f"{recursive} (recursive)",
                      "yellow",
                      attrs=["bold"]))


test_fast_exp(16, 31)
test_fast_exp(16, 51)
test_fast_exp(36, 61)
