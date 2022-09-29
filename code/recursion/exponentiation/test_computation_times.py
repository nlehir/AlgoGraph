"""
    Fast exponentiation algorithm

    Test computation time for a large number of calculations
"""
from time import time
import pickle
from random import randrange
from naive_exponentiation import naive_exponentiation
from os import path, mkdir


def fast_exponentiation(a: int, n: int) -> int:
    if n == 0:
        return 1
    if n % 2 == 0:
        return fast_exponentiation(a, n // 2)**2
    else:
        return a * fast_exponentiation(a, n // 2)**2


def test_fast_exp(nb_of_tests: int, n_min: int, n_max: int) -> None:
    """
    Compares computation times between
    fast exponentiation, and built-in
    python functions.

    We measure average computing times
    and use enough computations to see convergence.

    :param nb_of_tests (int): number of tests
    :param n_min (int): minimum exponent in range
    :param n_max (int): maximum exponent in range
    :saves average computing times in files:
    """
    fastexp_times = list()
    double_splat_times = list()
    pow_times = list()
    naive_times = list()

    for index in range(int(nb_of_tests)):
        a = randrange(10, 40)
        n = randrange(n_min, n_max)
        # fast exp
        tic = time()
        _ = fast_exponentiation(a, n)
        toc = time()
        fastexp_time = toc-tic
        fastexp_times.append(fastexp_time)
        # double splat
        tic = time()
        _ = a**n
        toc = time()
        double_splat_time = toc-tic
        double_splat_times.append(double_splat_time)
        # pow
        tic = time()
        _ = pow(a, n)
        toc = time()
        pow_time = toc-tic
        pow_times.append(pow_time)
        # naive
        tic = time()
        _ = naive_exponentiation(a, n)
        toc = time()
        naive_time = toc-tic
        naive_times.append(naive_time)

    # average
    folder = f"./computation_times_{n_min}_{n_max}/"
    if not path.exists(folder):
        mkdir(folder)
    # save computation times
    with open(folder+"fastexp", "wb") as handle:
        pickle.dump(fastexp_times, handle)
    with open(folder+"double_splat", "wb") as handle:
        pickle.dump(double_splat_times, handle)
    with open(folder+"pow", "wb") as handle:
        pickle.dump(pow_times, handle)
    with open(folder+"naive", "wb") as handle:
        pickle.dump(naive_times, handle)


# test_fast_exp(1e4, 80, 100)
# test_fast_exp(1e4, 40, 60)
test_fast_exp(int(1e4), 10, 20)
