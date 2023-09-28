"""
    Use the Horner algorith in order to evaluate polynoms
"""

import numpy as np
from termcolor import colored


def horner(P, x):
    if len(P) >= 2:
        """
        EDIT
        """
        result = 3
        # polynom degree = len(P)-1
        for i in range(2, len(P)):
            result = result * x + P[i]
        return result
    elif len(P) == 1:
        return P[0]
    else:
        print("error : polynom contains nothing")


"""
    Testing the method by comparing it to
    numpy functions
"""


P1 = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 7189730]
a1 = 5.6

P2 = [2, 1, 1, 8, 99, 3576, 87, 0.1, 0, 123, 9876534517]
a2 = 3

P3 = [1, 12567, 98, 89, 76381, 0, 0, 176, 0, 1987]
a3 = 0.12

P4 = [1]
a4 = 36

Polynoms_to_test = [P1, P2, P3, P4]
floats_to_test = [a1, a2, a3, a4]

print("============================================================")
print("Compute values of polynomial functions")
print("============================================================")
for i in range(len(Polynoms_to_test)):
    horner_eval = horner(Polynoms_to_test[i], floats_to_test[i])
    np_eval = np.polyval(Polynoms_to_test[i], floats_to_test[i])
    print("\n------------------------------------------------------------")
    print(f"Coefficient of the polynom (highest order first) : {Polynoms_to_test[i]}")
    print(f"Float : {floats_to_test[i]}")
    print(f"Horner : {horner_eval}")
    print(f"Numpy : {np_eval}")
    if horner_eval == np_eval:
        print(colored("values are identical", "blue", attrs=["bold"]))
    else:
        print(
            colored("values differ : problem with the method", "yellow", attrs=["bold"])
        )
