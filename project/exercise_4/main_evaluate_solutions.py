import numpy as np

from utils import evaluate_solution

from nic import random_sign

def main():
    rng = np.random.default_rng()
    evaluate_solution(
            solution_name="random_sign",
            solution=random_sign,
            rng=rng,
            )


if __name__ == "__main__":
    main()
