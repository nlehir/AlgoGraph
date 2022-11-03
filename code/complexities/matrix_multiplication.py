"""
    measure the complexity of matrix multiplication
"""

from time import time

import matplotlib.pyplot as plt
import numpy as np

matrix_sizes = range(0, 5000, 500)
times = list()

for n in matrix_sizes:
    # generate random matrices
    a = np.random.rand(n, n)
    b = np.random.rand(n, n)
    t0 = time()
    c = np.matmul(a, b)
    computation_time = time() - t0
    times.append(computation_time)
    print(n, computation_time)

title = "Computation time of matrix multiplication"
filename = "matrix_multiplication.pdf"
plt.plot(matrix_sizes, times, "o")
plt.xlabel("matrix size")
plt.ylabel("computation time")
plt.title(title)
plt.savefig("images/" + filename)
plt.close()
