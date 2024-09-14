"""
Test the solution defined in {file_name}.py

In order test, run pytest

Replace the module name (here, nic) by your module name.
"""
from nic import (
        choose_sign,
        )

from params import (
        N_NUMBERS,
        NUMBERS_RANGE,
        B_RANGE,
        )

import numpy as np

def test_choose_sign() -> None:
    rng = np.random.default_rng()

    numbers = rng.uniform(
            low=-NUMBERS_RANGE,
            high=NUMBERS_RANGE,
            size=N_NUMBERS,
            )
    b = rng.uniform(
            low=-B_RANGE,
            high=B_RANGE,
            )

    signs = choose_sign(numbers=numbers, b=b)

    assert type(signs) == np.ndarray
    assert len(signs) == len(numbers)
    assert np.all(np.unique(signs) == np.array([-1, 1]))
