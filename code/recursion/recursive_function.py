"""
   recursive function with two arguments
"""


def recursive_function(n, m):
    if n == 0 or m == 0:
        return n + m
    return recursive_function(n - 1, m) + recursive_function(n, m - 1)


print(recursive_function(30, 30))
