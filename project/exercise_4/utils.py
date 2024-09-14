import numpy as np
from time import time

def compute_score(numbers: np.ndarray, signs:np.ndarray, b: float):
    return np.abs(b + np.sum(numbers * signs))

def evaluate_solution(
        solution_name: str,
        solution,
        rng,
        numbers_range,
        b_range,
        n_tests,
        n_numbers,
        ):
    scores = list()
    runtimes = list()
    print(f"\nTesting solution {solution_name}")
    for trial in range(n_tests):
        if trial % (n_tests//10) == 0:
            print(f"trial {trial}/{n_tests}")
        numbers = rng.uniform(
                low=-numbers_range,
                high=numbers_range,
                size=n_numbers,
                )
        b = rng.uniform(
                low=-b_range,
                high=b_range,
                )
        tic = time()
        signs = solution(
                numbers=numbers,
                b=b,
                )
        toc = time()
        score = compute_score(
                numbers=numbers,
                signs=signs,
                b=b,
                )
        runtime = toc-tic
        scores.append(score)
        runtimes.append(runtime)
    average_score = sum(scores)/n_tests
    average_runtime = sum(runtimes)/n_tests
    message = (
            f"Solution: {solution_name}\n"
            f"Average score over {n_tests} trials: {average_score:.4f}\n"
            f"Average running time: {average_runtime:.4E} s"
            )
    print(message)
