
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
from easy_stat.functions import functions
from easy_stat.utils import helpers
from easy_stat.utils import general
from easy_stat.utils import checkers
from easy_stat.functions.distributions import ShapiroWilkNormalityTest
from easy_stat.functions.functions import multimode

os.system('cls')
print(">>>")


test = helpers.NDigitsManagement()
print(test.__str__())

# print(test.language)
# print(test.get_language())
# test.set_language('pt-br')
# print(test.language)
# print(test.get_language())
# print(test.__str__())
# print(test.__repr__())

































def draw_scatter_plot(x_exp, name, decimal_separator='.', local="pt_BR"):
    """
    """
    checkers._check_is_str(name, "name")
    plot_design = {
        "scatter": ['o', 'None', 'k', 50],
    }
    default_locale = helpers._change_locale(decimal_separator, local)


    fig, ax = plt.subplots(figsize=(8,6))
    ax.scatter(np.arange(1, x_exp.size + 1), x_exp,
            marker=plot_design["scatter"][0],
            c=plot_design["scatter"][1],
            edgecolors=plot_design["scatter"][2],
            s=plot_design["scatter"][3],
            label=name)

    ax.set_xlabel("Unordered data")
    ax.set_ylabel("Data")
    ax.legend()
    plt.show()

    helpers._change_locale_back_to_default(default_locale)































#
