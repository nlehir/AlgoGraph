import matplotlib.pyplot as plt
import numpy as np

from insertion_sort import insertion_sort

"""
    We will statistically check the number of
    operations performed by insertionSort
    as a function of the size of the list.

    Thus we will need to use a large number
    of random list. We will use the discrete
    uniform distribution to generate random lists
    as numpy arrays.
"""
number_of_tests = 100


def number_of_operations(n: int) -> float:
    """
    :n integer: size of the list

        function used to monitor the
        average number of elementary operations performed
        as a function of the size of the list n.
    """
    counters = list()
    for _ in range(number_of_tests):
        uniform_llist = np.random.randint(0, 1001, n).tolist()
        """
        EDIT
        """
        counters.append(3)
    average = 5
    print(
        f"for n={n}, {average} operations "
        + f"performed on average on {number_of_tests} instances."
    )
    return average

def main() -> None:
    """
        Compute the average number of operations
        for several values of n
    """
    n_max = 200
    step = int(n_max / 10)
    n_range = range(1, n_max, step)
    experimental_values = [number_of_operations(n) for n in n_range]
    plt.plot(n_range, experimental_values, "o", color="teal", label="experiment")

    """
        Compute theoretical values
    """
    """
    EDIT
    """
    values_of_n = range(1, n_max)
    theoretical_values = [2**n for n in values_of_n]

    """
        Plot the results.
    """
    plt.xticks(range(0, n_max, step))
    plt.plot(values_of_n, theoretical_values, "--r", label="theoretical")
    plt.legend(loc="best")
    plt.title("Average-case complexity of Insertion Sort")
    plt.xlabel("size of the list to sort (integer)")
    plt.ylabel("average number of operations to perform insertion sort")
    plt.savefig("complexity.pdf")

if __name__ == "__main__":
    main()
