"""
    memoized fibonacci
"""

m = 200
intermediate_values = [None for i in range(1, m + 1)]


def memo_fibonacci(n: int) -> int:
    """
        EDIT THIS FUNCTION
    """
    if intermediate_values[n] is None:
        if n == 1 or n == 2:
            intermediate_values[n] = 1
        else:
            intermediate_values[n] = memo_fibonacci(n // 2) + 1
    return intermediate_values[n]


print(memo_fibonacci(25))
