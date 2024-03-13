import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


def plot_arrays(x_input, y_input, x_label, y_label, title, save_dir=None, marker='.'):
    fig = plt.figure()
    plt.scatter(x_input, y_input, marker=marker)
    from numpy.polynomial.polynomial import polyfit
    x_input = np.array(x_input)
    y_input = np.array(y_input)
    correlation = stats.pearsonr(x_input, y_input)
    r_coeff = np.around(correlation[0], 3)
    p_value = np.around(correlation[1], 3)
    if p_value < 0.0001:
        p_value = 0.0001
    b, m = polyfit(x_input, y_input, 1)
    plt.plot(x_input, b + m * x_input, '-', color='grey')
    fig.suptitle(title + f" (r = {r_coeff}, p = {p_value})")
    plt.xlabel(x_label, fontsize=14)
    plt.ylabel(y_label, fontsize=14)
    plt.xticks(fontsize=14)
    if save_dir is not None:
        plt.savefig(save_dir, dpi=300)
    else:
        plt.show()
    plt.close()