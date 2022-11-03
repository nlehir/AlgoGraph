"""
   compute the number of operations in fast exponentiation
"""

import matplotlib.pyplot as plt


def fast_exponentiation(a: int, n: int) -> tuple[int, int]:
    """
    EDIT THIS FUNCTION
    """
    if n == 0:
        return (1, 0)
    (expo, counter) = fast_exponentiation(a, n // 2)
    if n % 2 == 0:
        return (expo**2, counter)
    else:
        return (a * expo**2, counter)


min_exponent = 1
max_exponent = 5**8
step = int(max_exponent / 10)
exponents = range(min_exponent, max_exponent + 2, step)

times = list()
a = 5

for exponent in exponents:
    power_of_a, counter = fast_exponentiation(a, exponent)
    times.append(counter)

title = "Fast exponentiation complexity"
filename = "fast_exp_complexity.pdf"
plt.plot(exponents, times, "o")
plt.xlabel("Exponent")
plt.ylabel("Number of multiplications")
plt.title(title)
plt.savefig("images/{filename}")
plt.close()
