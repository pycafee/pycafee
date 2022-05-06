
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
from pycafee.functions import functions
from pycafee.utils import helpers
from pycafee.utils import general
from pycafee.utils import checkers
from pycafee.functions.distributions import ShapiroWilkNormalityTest
from pycafee.functions.functions import multimode

os.system('cls')
print(">>>")

x = np.array([1,2,3,4,5,6,5,5,3,4,6,7,8])
teste = ShapiroWilkNormalityTest()
print(teste.shapiro_wilk(x))

teste.draw_shapiro_wilk_tabulated_values()
plt.show()


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
