import cProfile
import os
import sys

import numpy as np

pr = cProfile.Profile()
pr.enable()

# code to analyse
a = 0
for step in range(2000):
    a = step**2
    b = np.random.rand(10, 10)
    d = b + 1
    c = np.matmul(b, d)

pr.disable()
stats_file = open(f"{os.path.basename(__file__)}.txt", "w")
sys.stdout = stats_file
pr.print_stats(sort="time")
sys.stdout = sys.__stdout__
