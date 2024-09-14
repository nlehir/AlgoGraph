import numpy as np

def random_sign(numbers: np.ndarray, b: float):
    rng = np.random.default_rng()
    signs = rng.integers(low=0, high=2, size=len(numbers))
    signs = 2 * (signs-1/2)
    return signs

choose_sign = random_sign
