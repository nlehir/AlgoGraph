"""
Example polynomial fits on some data, with various degrees
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_polynom_fit(polynom, x, y):
    """
    Plot the result of fitting the polynom
    to the training set
    """
    degree = len(polynom) - 1
    title = f"Polynomial fit on data, degree={degree}\n"
    filename = f"Fit_degree_{degree}.pdf"
    xlim_left = 0.9 * min(x)
    xlim_right = 1.1 * max(x)
    x_plot = np.linspace(xlim_left, xlim_right, 500)
    plt.plot(x, y, "o", markersize=3, alpha=0.8, label="data")
    plt.plot(
        x_plot,
        np.polyval(polynom, x_plot),
        "-",
        markersize=3,
        alpha=0.5,
        label="Polynomial fit",
    )
    plt.legend(loc="best")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(xlim_left, xlim_right)
    # plt.ylim(ylim_bottom, ylim_top)
    plt.title(title)
    plt.savefig(filename)
    plt.close()


def generate_data():
    x = np.linspace(1, 50, 20)
    y = (x / 10) ** 2 + 2 * (x / 5) ** 3
    return x, y


def main():
    x, y = generate_data()
    degree = 3
    polynom = np.polyfit(x, y, degree)
    plot_polynom_fit(polynom, x, y)

    degree = 2
    polynom = np.polyfit(x, y, degree)
    plot_polynom_fit(polynom, x, y)


if __name__ == "__main__":
    main()
