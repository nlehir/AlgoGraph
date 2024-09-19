import numpy as np
from params import SCALE_X, SCALE_B, N_TESTS, N_NUMBERS
from time import time

def compute_score(numbers: np.ndarray, signs:np.ndarray, b: float):
    return np.abs(b + np.sum(numbers * signs))

def evaluate_solution(
        solution_name: str,
        solution,
        rng,
        ):
    scores = list()
    runtimes = list()
    print(f"\nTesting solution {solution_name}")
    for trial in range(N_TESTS):
        if trial % (N_TESTS//10) == 0:
            print(f"trial {trial}/{N_TESTS}")
        numbers = rng.normal(
                loc=0,
                scale=SCALE_X,
                size=N_NUMBERS,
                )
        b = rng.normal(
                loc=0,
                scale=SCALE_B,
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
    average_score = sum(scores)/N_TESTS
    average_runtime = sum(runtimes)/N_TESTS
    message = (
            f"Solution: {solution_name}\n"
            f"Average score over {N_TESTS} trials: {average_score:.4f}\n"
            f"Average running time: {average_runtime:.4E} s"
            )
    print(message)
