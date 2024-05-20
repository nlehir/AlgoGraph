"""
    Use the Horner algorithm in order to evaluate polynoms
"""

import numpy as np
from termcolor import colored


def horner(P: list[int], x: float) -> float:
    """
    Fix this function

    P contains the list of the coefficients of the
    polynom, highest order first (P[0])
    """
    result = 0
    for coeff in P:
        result = result * x + coeff
    return result


def main() -> None:
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

if __name__ == "__main__":
    main()
