"""
Test the parcours function defined in {file_name}.py

In order test, run pytest

Replace the module name (here, nic) by your module name.
"""
from nic import (
        parcours,
        )

import numpy as np

LOC = 0
SCALE = 1000
SIZE = 1000

def test_parcours() -> None:
    rng = np.random.default_rng()
    houses = rng.normal(loc=LOC, scale=SCALE, size=SIZE)
    final_order = parcours(houses)
    assert type(final_order) == list
    assert len(final_order) == len(houses)
    """
    Due to rounding errors coming from floating point
    numbers, we test if the sums are approximately equal.
    """
    assert np.isclose(np.sum(final_order), np.sum(houses))
