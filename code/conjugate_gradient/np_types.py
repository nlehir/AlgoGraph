import numpy as np

d = 100

rng = np.random.default_rng()

X_int8 = rng.integers(low=0, high=2, size=(d, d)).astype(np.int8)

A_float64 = rng.uniform(low=0, high=10, size=(d, d))

print(f"\nType of X_int8 @ A_float64: {(X_int8 @ A_float64).dtype}")

print(f"X_int8:\n{X_int8}")
print(f"\nX_int8 @ X_int8.T:\n{X_int8 @ X_int8.T}")

X_float64 = X_int8.astype(np.float64)
print(f"\nX_float64 @ X_float64.T:\n{X_float64 @ X_float64.T}")
