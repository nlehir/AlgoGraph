# import time
# import matplotlib.pyplot as plt
# from numpy.polynomial import Polynomial as P
from random import shuffle


def function_1(n: int) -> None:
    """
    compute the time complexity of running
    this function as a function of n.
    """
    temp_list = list()
    for i in range(n**2):
        temp = 0
        for j in range(i):
            temp += j
        temp_list.append(temp)
    sum(temp_list)
    

def function_2(n: int) -> None:
    """
    compute the time complexity of running
    this function as a function of n.

    do not hesitate to do some reseach about the
    complexity of the functions used and to average
    the measured times over a number of trials if necessary.
    """
    print(n)
    for i in range(n):
        temp_list = [j+i for j in range(n)]
        shuffle(temp_list)
        max(temp_list)
