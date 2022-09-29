"""
    memoized fibonacci
"""

m = 200
intermediate_values = [None for i in range(1, m + 1)]


def memo_fibonacci(n, depth):
    padding = "---"*depth
    if intermediate_values[n] is None:
        if n == 1 or n == 2:
            print(padding+f" n={n}, base case")
            intermediate_values[n] = 1
        else:
            print(padding+f" n={n}, recursion")
            depth += 1
            intermediate_values[n] = memo_fibonacci(
                n - 1, depth) + memo_fibonacci(n - 2, depth)
    return intermediate_values[n]


print(memo_fibonacci(25, 0))
