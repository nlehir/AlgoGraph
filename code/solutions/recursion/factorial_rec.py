"""
Compute the factorial with a recursion
"""
import math
from termcolor import colored


def factorial_rec(n):
    if n == 1:
        return 1
    else:
        return factorial_rec(n - 1) * n


def test_function(to_test):
    """Function to test recursive method
    by comparing with the factorial function
    from the math module

    :to_test: int

    """
    recursive = factorial_rec(to_test)
    math_function = math.factorial(to_test)
    if recursive == math_function:
        print(colored(f"n={to_test} result ok: {math_function}", "blue", attrs=["bold"]))
    else:
        print(colored(f"n={to_test} wrong result: {math_function} vs "+
                      f"{recursive} (recursive)",
                      "yellow",
                      attrs=["bold"]))


test_function(10)
test_function(5)
