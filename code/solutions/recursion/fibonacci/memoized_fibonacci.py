"""
    memoized fibonacci
"""

m = 200
intermediate_values = [None for i in range(1, m + 1)]


def memo_fibonacci(n: int) -> int:
    # the value is not known yet
    if intermediate_values[n] is None:
        # base cases
        if n == 1 or n == 2:
            intermediate_values[n] = 1
        else:
            # fill the missing value
            intermediate_values[n] = memo_fibonacci(n - 1) + memo_fibonacci(n - 2)
    return intermediate_values[n]


print(memo_fibonacci(25))
