"""
    naive fibonacci
"""


def bad_fibonacci(n: int) -> int:
    # we could also start from 0
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return bad_fibonacci(n - 1) + bad_fibonacci(n - 2)


print(bad_fibonacci(35))
