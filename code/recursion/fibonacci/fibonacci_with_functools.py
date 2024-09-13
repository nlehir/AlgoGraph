"""
Caching is remembering

Functools uses a data structure that is similar to a dict
to store values.
"""

import functools

@functools.cache
def fibo_cached(n) -> int:
    if n <= 1:
        return n
    else:
        return fibo_cached(n-1) + fibo_cached(n-2)


n = 100
print("fibonacci cached")
print(f"{n=}")
print(fibo_cached(n))
