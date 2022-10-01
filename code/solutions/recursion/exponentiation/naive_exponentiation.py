"""
    normal naïve exponentiation
"""


def naive_exponentiation(a: int, n: int) -> int:
    exponentiated_a = a
    if n >= 2:
        for i in range(1, n):
            exponentiated_a *= a
        return exponentiated_a
    else:
        return a


# print(naive_exponentiation(5, 300000))
