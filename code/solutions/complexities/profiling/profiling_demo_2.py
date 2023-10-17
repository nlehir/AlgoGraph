import cProfile
import os
import sys
import time

import numpy as np

pr = cProfile.Profile()
pr.enable()

# code to analyse
matrix_sizes = range(0, 3000, 500)
times = []

for n in matrix_sizes:
    # random matrices
    a = np.random.rand(n, n)
    b = np.random.rand(n, n)
    t0 = time.time()
    c = np.matmul(a, b)
    computation_time = time.time() - t0
    times.append(computation_time)
    print(n, computation_time)

pr.disable()
stats_file = open(f"{os.path.basename(__file__)}.txt", "w")
sys.stdout = stats_file
pr.print_stats(sort="time")
sys.stdout = sys.__stdout__
