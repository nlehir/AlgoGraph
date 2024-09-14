import numpy as np

from utils import evaluate_solution

from nic import random_sign

from params import (
        N_NUMBERS,
        NUMBERS_RANGE,
        B_RANGE,
        N_TESTS,
        )

def main():
    rng = np.random.default_rng()
    evaluate_solution(
            solution_name="random_sign",
            solution=random_sign,
            rng=rng,
            numbers_range=NUMBERS_RANGE,
            b_range=B_RANGE,
            n_tests=N_TESTS,
            n_numbers=N_NUMBERS,
            )


if __name__ == "__main__":
    main()
