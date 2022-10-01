import cProfile
import os
import sys

pr = cProfile.Profile()
pr.enable()


# code to analyse
def bad_fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        return bad_fibonacci(n - 1) + bad_fibonacci(n - 2)


print(bad_fibonacci(30))

pr.disable()
stats_file = open(f"{os.path.basename(__file__)}.txt", 'w')
sys.stdout = stats_file
pr.print_stats(sort='time')
sys.stdout = sys.__stdout__
