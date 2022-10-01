"""
    naive fibonacci
"""


def bad_fibonacci(n: int, depth: int) -> int:
    padding = "---"*depth
    if n == 1:
        print(padding+f" n={n}, base case")
        return 1
    elif n == 2:
        print(padding+f" n={n}, base case")
        return 1
    else:
        print(padding+f" n={n}, recursion")
        depth += 1
        return bad_fibonacci(n - 1, depth) + bad_fibonacci(n - 2, depth)


print(bad_fibonacci(10, 0))
