import pickle
import matplotlib.pyplot as plt


def plot_computation_times(n_min: int, n_max: int) -> None:
    folder = f"./computation_times_{n_min}_{n_max}/"
    with open(folder+"fastexp", "rb") as handle:
        fast_exp_times = pickle.load(handle)

    with open(folder+"double_splat", "rb") as handle:
        double_splat_times = pickle.load(handle)

    with open(folder+"pow", "rb") as handle:
        pow_times = pickle.load(handle)

    with open(folder+"naive", "rb") as handle:
        naive_times = pickle.load(handle)

    nb_computations = len(fast_exp_times)
    # fast exp
    fast_exp_averages = list()
    for index in range(1, nb_computations+1):
        average_time = 1e6*sum(fast_exp_times[:index])/index
        fast_exp_averages.append(average_time)

    # double splat
    double_splat_averages = list()
    for index in range(1, nb_computations+1):
        average_time = 1e6*sum(double_splat_times[:index])/index
        double_splat_averages.append(average_time)

    # pow
    pow_averages = list()
    for index in range(1, nb_computations+1):
        average_time = 1e6*sum(pow_times[:index])/index
        pow_averages.append(average_time)

    # naive
    naive_averages = list()
    for index in range(1, nb_computations+1):
        average_time = 1e6*sum(naive_times[:index])/index
        naive_averages.append(average_time)

    plt.plot(range(nb_computations), fast_exp_averages, label="fast exp")
    plt.plot(range(nb_computations),
             double_splat_averages, label="double splat")
    plt.plot(range(nb_computations), pow_averages, label="pow")
    plt.plot(range(nb_computations), naive_averages, label="naive")
    plt.xlabel("number of computations")
    plt.ylabel("average computing time (mus)")
    plt.legend(loc="best")
    title = (
        "exponentiation : averaged computation time comparison"
        f"\n exponent in range [{n_min}, {n_max}]"
    )

    plt.title(title)
    plt.savefig(f"computation_times_{n_min}_{n_max}.pdf")
    plt.close()


# plot_computation_times(80, 100)
# plot_computation_times(40, 60)
plot_computation_times(10, 20)
