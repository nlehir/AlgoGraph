"""
    measure the complexity of a simple loop
"""

import matplotlib.pyplot as plt
import os
from time import time

min_size = 1
max_size = 10**7
step = int(max_size / 5)
sizes = range(min_size, max_size + 2, step)
times = list()

for size in sizes:
    print(str(size) + " multiplications")
    tic = time()
    for j in range(size):
        x = 2 * 3
    toc = time()
    times.append(toc - tic)


title = "Computation time of a sequence of multiplications"
filename = "linear.pdf"
plt.plot(sizes, times, "o")
plt.xlabel("number of multiplications")
plt.ylabel("computation time (seconds)")
plt.title(title)
if not os.path.exists("./images/"):
    os.mkdir("./images")
plt.savefig(f"images/{filename}")
plt.close()
