"""
Test the solution defined in {file_name}.py

In order test, run pytest

Replace the module name (here, nic) by your module name.
"""
from nic import (
        choose_sign,
        )

from params import SCALE_X, SCALE_B, N_NUMBERS

import numpy as np

def test_choose_sign() -> None:
    rng = np.random.default_rng()

    numbers = rng.normal(
            loc=0,
            scale=SCALE_X,
            size=N_NUMBERS,
            )
    b = rng.normal(
            loc=0,
            scale=SCALE_B,
            )
    signs = choose_sign(numbers=numbers, b=b)

    assert type(signs) == np.ndarray
    assert len(signs) == len(numbers)
    assert np.all(np.unique(signs) == np.array([-1, 1]))
