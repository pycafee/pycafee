"""This module concentrates all distributions functions
"""

# Function list:
#
#     - ShapiroWilkNormalityTest(AlphaManagement, NDigitsManagement)
#         - shapiro_wilk(self, x_exp, alfa=None, n_digits=None, conclusion=None, details=None)
#         - shapiro_wilk_to_csv(self, file_name=None, sep=",")
#         - shapiro_wilk_to_xlsx(self, file_name=None, sheet_names=None)
#         - get_shapiro_wilk_tabulated_value(self, n_rep, alfa=None)
#         - draw_shapiro_wilk_tabulated_values(self, show=True)
#         - __str__(self)
#         - __repr__(self)

#########################################
################ Imports ################
#########################################

###### Standard ######
from collections import namedtuple


###### Third part ######
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import shapiro as shapiro_wilk_scipy

###### Home made ######

from pycafee.database_management import management
from pycafee.utils import checkers
from pycafee.utils import general
from pycafee.utils import helpers
from pycafee.utils.helpers import AlphaManagement, NDigitsManagement

###########################################
################ Functions ################
###########################################


class ShapiroWilkNormalityTest(AlphaManagement, NDigitsManagement):
    """
    This class instantiates an object to perform the Shapiro Wilk Normality test.

    Attributes
    ----------
    alfa : float
        The level of significance.
    language : str
        The language code used for the interface.
    msg : str
        The test result expressed in text.
    n_digits : int
        The number of digits that are displayed.
    p_value : float
        The estimated p-value for the data set.
    statistic : float
        The calculated value of the test statistic.
    tabulated : float
        The tabulated value for the pair (number of observations and level of significance).
    x_exp : np.ndarray
        The experimental data where the test was applied.


    Methods
    -------
    shapiro_wilk(x_exp, alfa=None, n_digits=None, conclusion=None, details=None)
        Performs the Shapiro Wilk test.
    shapiro_wilk_to_csv(file_name=None, sep=",")
        Exports the results to a pre-formatted csv file.
    shapiro_wilk_to_xlsx(file_name=None, sheet_names=None)
        Exports the results to a pre-formatted xlsx file.
    get_shapiro_wilk_tabulated_value(n_rep, alfa=None)
        Finds the tabulated value for a pair of alpha and number of observations
    draw_shapiro_wilk_tabulated_values(show=True)
        Draws a plot with the tabulated data.

    """



    shapiro_wilk_table = {
        'n_rep': [
                3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
                32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50
                ],
        0.01 : [
                0.753, 0.687, 0.686, 0.713, 0.730, 0.749, 0.764, 0.781, 0.792, 0.805, 0.814, 0.825, 0.835, 0.844, 0.851, 0.858,
                0.863, 0.868, 0.873, 0.878, 0.881, 0.884, 0.888, 0.891, 0.894, 0.896, 0.898, 0.900, 0.902, 0.904, 0.906, 0.908,
                0.910, 0.912, 0.914, 0.916, 0.917, 0.919, 0.920, 0.922, 0.923, 0.924, 0.926, 0.927, 0.928, 0.929, 0.929, 0.930,
                ],
        0.02 : [
                0.756, 0.707, 0.715, 0.743, 0.760, 0.778, 0.791, 0.806, 0.817, 0.828, 0.837, 0.846, 0.855, 0.863, 0.869, 0.874,
                0.879, 0.884, 0.888, 0.892, 0.895, 0.898, 0.901, 0.904, 0.906, 0.908, 0.910, 0.912, 0.914, 0.915, 0.917, 0.919,
                0.920, 0.922, 0.924, 0.925, 0.927, 0.928, 0.929, 0.930, 0.932, 0.933, 0.934, 0.935, 0.936, 0.937, 0.937, 0.938
                ],
        0.05 : [
                0.767, 0.748, 0.762, 0.788, 0.803, 0.818, 0.829, 0.842, 0.850, 0.859, 0.866, 0.874, 0.881, 0.887, 0.892, 0.897,
                0.901, 0.905, 0.908, 0.911, 0.914, 0.916, 0.918, 0.920, 0.923, 0.924, 0.926, 0.927, 0.929, 0.930, 0.931, 0.933,
                0.934, 0.935, 0.936, 0.938, 0.939, 0.940, 0.941, 0.942, 0.943, 0.944, 0.945, 0.945, 0.946, 0.947, 0.947, 0.947
                ],
        0.10 : [
                0.789, 0.792, 0.806, 0.826, 0.838, 0.851, 0.859, 0.869, 0.876, 0.883, 0.889, 0.895, 0.901, 0.906, 0.910, 0.914,
                0.917, 0.920, 0.923, 0.926, 0.928, 0.930, 0.931, 0.933, 0.935, 0.936, 0.937, 0.939, 0.940, 0.941, 0.942, 0.943,
                0.944, 0.945, 0.946, 0.947, 0.948, 0.949, 0.950, 0.951, 0.951, 0.952, 0.953, 0.953, 0.954, 0.954, 0.955, 0.955
                ],
        0.50 : [
                0.959, 0.935, 0.927, 0.927, 0.928, 0.932, 0.935, 0.938, 0.940, 0.943, 0.945, 0.947, 0.950, 0.952, 0.954, 0.956,
                0.957, 0.959, 0.960, 0.961, 0.962, 0.963, 0.964, 0.965, 0.965, 0.966, 0.966, 0.967, 0.967, 0.968, 0.968, 0.969,
                0.969, 0.970, 0.970, 0.971, 0.971, 0.972, 0.972, 0.972, 0.973, 0.973, 0.973, 0.974, 0.974, 0.974, 0.974, 0.974
                ],
        0.90 : [
                0.998, 0.987, 0.979, 0.974, 0.972, 0.972, 0.972, 0.972, 0.973, 0.973, 0.974, 0.975, 0.975, 0.976, 0.977, 0.978,
                0.978, 0.979, 0.980, 0.980, 0.981, 0.981, 0.981, 0.982, 0.982, 0.982, 0.982, 0.983, 0.983, 0.983, 0.983, 0.983,
                0.984, 0.984, 0.984, 0.984, 0.984, 0.985, 0.985, 0.985, 0.985, 0.985, 0.985, 0.985, 0.985, 0.985, 0.985, 0.985
                ],
        0.95 : [
                0.999, 0.992, 0.986, 0.981, 0.979, 0.978, 0.978, 0.978, 0.979, 0.979, 0.979, 0.980, 0.980, 0.981, 0.981, 0.982,
                0.982, 0.983, 0.983, 0.984, 0.984, 0.984, 0.985, 0.985, 0.985, 0.985, 0.985, 0.985, 0.986, 0.986, 0.986, 0.986,
                0.986, 0.986, 0.987, 0.987, 0.987, 0.987, 0.987, 0.987, 0.987, 0.987, 0.988, 0.988, 0.988, 0.988, 0.988, 0.988
                ],
        0.98 : [
                1.000, 0.996, 0.991, 0.986, 0.985, 0.984, 0.984, 0.983, 0.984, 0.984, 0.984, 0.984, 0.984, 0.985, 0.985, 0.986,
                0.986, 0.986, 0.987, 0.987, 0.987, 0.987, 0.988, 0.988, 0.988, 0.988, 0.988, 0.988, 0.988, 0.988, 0.989, 0.989,
                0.989, 0.989, 0.989, 0.989, 0.989, 0.989, 0.989, 0.989, 0.990, 0.990, 0.990, 0.990, 0.990, 0.990, 0.990, 0.990
                ],
        0.99 : [
                1.000, 0.997, 0.993, 0.989, 0.988, 0.987, 0.986, 0.986, 0.986, 0.986, 0.986, 0.986, 0.987, 0.987, 0.987, 0.988,
                0.988, 0.988, 0.989, 0.989, 0.989, 0.989, 0.989, 0.989, 0.990, 0.990, 0.990, 0.900, 0.990, 0.990, 0.990, 0.990,
                0.990, 0.990, 0.990, 0.990, 0.991, 0.991, 0.991, 0.991, 0.991, 0.991, 0.991, 0.991, 0.991, 0.991, 0.991, 0.991
                ],
        'Note':
                "*the critical value for alpha equal to 0.99 with 30 observations probably has a typo. The correct value is probably 0.990 instead of 0.900."
    }


    def __init__(self, alfa=None, language=None, n_digits=None, **kwargs):
        super().__init__(alfa=alfa, language=language, n_digits=n_digits, **kwargs)
        self.msg = None
        self.statistic = None
        self.tabulated = None
        self.p_value = None
        self.x_exp = None


    # with some tests, with text, with database, with docstring
    def draw_shapiro_wilk_tabulated_values(self, show=True):
        """Draw a plot with the Shapiro-Wilk *tabulated data*.

        Parameters
        ----------
        show : bool (default True)
            Whether or not to display the graph with the tabulated values.

        Returns
        -------
        ax : matplotlib.axes._subplots.AxesSubplot
            The axis of the graph. This parameter is only valid if show = False.
        tabulated : dict
            The tabulated data used to draw the graph.

        Notes
        -----
        The Shapiro Wilk tabulated data can be found at BRATLEY et al [1]_.

        References
        ----------
        .. [1] BRATLEY, P.; FOX, B. L.; SCHRAGE, L. E. A Guide to Simulation. 1. ed. New York: Springer, 1983 (Appendix A).

        Examples
        --------

        **Ploting the Shapiro Wilk tabulated values**

        >>> from easy_stat.functions.distributions import ShapiroWilkNormalityTest
        >>> shapiro_wilk = ShapiroWilkNormalityTest()
        >>> shapiro_wilk.draw_shapiro_wilk_tabulated_values()

        .. image:: img/draw_shapiro_wilk_tabulated_values.png
           :alt: Graph showing the tabulated values of the Shapiro Wilk test for different alpha values
           :align: center


        **Saving the Shapiro Wilk tabulated values**

        >>> from easy_stat.functions.distributions import ShapiroWilkNormalityTest
        >>> import matplotlib.pyplot as plt
        >>> shapiro_wilk = ShapiroWilkNormalityTest()
        >>> shapiro_wilk.draw_shapiro_wilk_tabulated_values(show=False)
        >>> plt.savefig("shapiro_wilk.png")


        **Getting the data used to draw the graph**

        >>> from easy_stat.functions.distributions import ShapiroWilkNormalityTest
        >>> import matplotlib.pyplot as plt
        >>> shapiro_wilk = ShapiroWilkNormalityTest()
        >>> axes, table = shapiro_wilk.draw_shapiro_wilk_tabulated_values(show=False)
        >>> print(table.keys())
        dict_keys(['n_rep', 0.01, 0.02, 0.05, 0.1, 0.5, 0.9, 0.95, 0.98, 0.99, 'Note'])

        """

        fk_id_function = management._query_func_id("draw_shapiro_wilk_tabulated_values")
        messages = management._get_messages(fk_id_function, self.language)

        ### Checking the show parameter ###
        checkers._check_is_bool(show, "show", self.language)

        ### The values tabled in a dictionary ###
        shapiro_wilk_table = ShapiroWilkNormalityTest.shapiro_wilk_table

        ### Make the plot ###
        fig, ax = plt.subplots(figsize=(12,6))
        ax.plot(shapiro_wilk_table['n_rep'], shapiro_wilk_table[0.01], marker='o', label=f'{messages[1][0][0]} = 1%')
        ax.plot(shapiro_wilk_table['n_rep'], shapiro_wilk_table[0.02], marker='o', label=f'{messages[1][0][0]} = 2%')
        ax.plot(shapiro_wilk_table['n_rep'], shapiro_wilk_table[0.05], marker='o', label=f'{messages[1][0][0]} = 5%')
        ax.plot(shapiro_wilk_table['n_rep'], shapiro_wilk_table[0.10], marker='o', label=f'{messages[1][0][0]} = 10%')
        ax.plot(shapiro_wilk_table['n_rep'], shapiro_wilk_table[0.50], marker='o', label=f'{messages[1][0][0]} = 50%')
        ax.plot(shapiro_wilk_table['n_rep'], shapiro_wilk_table[0.90], marker='o', label=f'{messages[1][0][0]} = 90%')
        ax.plot(shapiro_wilk_table['n_rep'], shapiro_wilk_table[0.95], marker='o', label=f'{messages[1][0][0]} = 95%')
        ax.plot(shapiro_wilk_table['n_rep'], shapiro_wilk_table[0.98], marker='o', label=f'{messages[1][0][0]} = 98%')
        ax.plot(shapiro_wilk_table['n_rep'], shapiro_wilk_table[0.99], marker='o', label=f'{messages[1][0][0]} = 99%')
        trans = ax.get_xaxis_transform() # x in data untis, y in axes fraction
        ax.annotate(
                messages[2][0][0],
                xy=(17.5, -0.075 ), xycoords=trans, fontsize='x-small')
        ax.legend()
        ax.set_title(messages[3][0][0])
        ax.set_xticks([3, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],fontsize='xx-large')
        fig.tight_layout()


        ## If show equals True, display the graph ##
        if show:
            plt.show()

        return ax, shapiro_wilk_table

    # with test, with text, with database, wtih docstring
    def get_shapiro_wilk_tabulated_value(self, n_rep, alfa=None):
        """This function gets the tabulated value of the Shapiro Wilk test.

        Parameters
        ----------
        alfa : float (default = 0.05)
            The significance level.
        n_rep : int
            The total number of observations.

        Returns
        -------
        tabulated : float or None.
            The tabulated value for the requested confidence level.

        Notes
        -----
        The tabulated value is returned only if the number of observations is at least ``3`` (``n_rep >= 3``).

        If the number of repetitions is higher than ``50`` (``n_rep > 50``),  the function returns the tabulated value for ``50`` (``n_rep = 50``) observations.

        This function has tabulated values for the following confidence levels [1]_:
            - 99% (ɑ = 0.01);
            - 98% (ɑ = 0.02);
            - 95% (ɑ = 0.05);
            - 90% (ɑ = 0.10);
            - 50% (ɑ = 0.50);

        The function returns None for other confidence levels.

        References
        ----------
        .. [1] BRATLEY, P.; FOX, B. L.; SCHRAGE, L. E. A Guide to Simulation. 1. ed. New York: Springer, 1983 (Appendix A).


        Examples
        --------

        **Getting tabulated value for 5% of significance and 5 observations**

        >>> from easy_stat.functions.distributions import ShapiroWilkNormalityTest
        >>> shapiro_wilk = ShapiroWilkNormalityTest()
        >>> tabulated_value = shapiro_wilk.get_shapiro_wilk_tabulated_value(n_rep=5)
        >>> print(tabulated_value)
        ShapiroWilkResult(tabulate=0.762, alpha=0.05)


        **Getting tabulated value for 1% of significance and 10 observations**

        >>> from easy_stat.functions.distributions import ShapiroWilkNormalityTest
        >>> shapiro_wilk = ShapiroWilkNormalityTest()
        >>> tabulated_value = shapiro_wilk.get_shapiro_wilk_tabulated_value(n_rep=10, alfa=0.01)
        >>> print(tabulated_value)
        ShapiroWilkResult(tabulate=0.781, alpha=0.01)

        """

        fk_id_function = management._query_func_id("get_shapiro_wilk_tabulated_value")
        messages = management._get_messages(fk_id_function, self.language)

        ### The values tabled in a dictionary ###
        shapiro_wilk_table = {
            'n_rep': [
                    3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
                    32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50
                    ],
            0.01 : [
                    0.753, 0.687, 0.686, 0.713, 0.730, 0.749, 0.764, 0.781, 0.792, 0.805, 0.814, 0.825, 0.835, 0.844, 0.851, 0.858,
                    0.863, 0.868, 0.873, 0.878, 0.881, 0.884, 0.888, 0.891, 0.894, 0.896, 0.898, 0.900, 0.902, 0.904, 0.906, 0.908,
                    0.910, 0.912, 0.914, 0.916, 0.917, 0.919, 0.920, 0.922, 0.923, 0.924, 0.926, 0.927, 0.928, 0.929, 0.929, 0.930,
                    ],
            0.02 : [
                    0.756, 0.707, 0.715, 0.743, 0.760, 0.778, 0.791, 0.806, 0.817, 0.828, 0.837, 0.846, 0.855, 0.863, 0.869, 0.874,
                    0.879, 0.884, 0.888, 0.892, 0.895, 0.898, 0.901, 0.904, 0.906, 0.908, 0.910, 0.912, 0.914, 0.915, 0.917, 0.919,
                    0.920, 0.922, 0.924, 0.925, 0.927, 0.928, 0.929, 0.930, 0.932, 0.933, 0.934, 0.935, 0.936, 0.937, 0.937, 0.938
                    ],
            0.05 : [
                    0.767, 0.748, 0.762, 0.788, 0.803, 0.818, 0.829, 0.842, 0.850, 0.859, 0.866, 0.874, 0.881, 0.887, 0.892, 0.897,
                    0.901, 0.905, 0.908, 0.911, 0.914, 0.916, 0.918, 0.920, 0.923, 0.924, 0.926, 0.927, 0.929, 0.930, 0.931, 0.933,
                    0.934, 0.935, 0.936, 0.938, 0.939, 0.940, 0.941, 0.942, 0.943, 0.944, 0.945, 0.945, 0.946, 0.947, 0.947, 0.947
                    ],
            0.10 : [
                    0.789, 0.792, 0.806, 0.826, 0.838, 0.851, 0.859, 0.869, 0.876, 0.883, 0.889, 0.895, 0.901, 0.906, 0.910, 0.914,
                    0.917, 0.920, 0.923, 0.926, 0.928, 0.930, 0.931, 0.933, 0.935, 0.936, 0.937, 0.939, 0.940, 0.941, 0.942, 0.943,
                    0.944, 0.945, 0.946, 0.947, 0.948, 0.949, 0.950, 0.951, 0.951, 0.952, 0.953, 0.953, 0.954, 0.954, 0.955, 0.955
                    ],
            0.50 : [
                    0.959, 0.935, 0.927, 0.927, 0.928, 0.932, 0.935, 0.938, 0.940, 0.943, 0.945, 0.947, 0.950, 0.952, 0.954, 0.956,
                    0.957, 0.959, 0.960, 0.961, 0.962, 0.963, 0.964, 0.965, 0.965, 0.966, 0.966, 0.967, 0.967, 0.968, 0.968, 0.969,
                    0.969, 0.970, 0.970, 0.971, 0.971, 0.972, 0.972, 0.972, 0.973, 0.973, 0.973, 0.974, 0.974, 0.974, 0.974, 0.974
                    ],
            0.90 : [
                    0.998, 0.987, 0.979, 0.974, 0.972, 0.972, 0.972, 0.972, 0.973, 0.973, 0.974, 0.975, 0.975, 0.976, 0.977, 0.978,
                    0.978, 0.979, 0.980, 0.980, 0.981, 0.981, 0.981, 0.982, 0.982, 0.982, 0.982, 0.983, 0.983, 0.983, 0.983, 0.983,
                    0.984, 0.984, 0.984, 0.984, 0.984, 0.985, 0.985, 0.985, 0.985, 0.985, 0.985, 0.985, 0.985, 0.985, 0.985, 0.985
                    ],
            0.95 : [
                    0.999, 0.992, 0.986, 0.981, 0.979, 0.978, 0.978, 0.978, 0.979, 0.979, 0.979, 0.980, 0.980, 0.981, 0.981, 0.982,
                    0.982, 0.983, 0.983, 0.984, 0.984, 0.984, 0.985, 0.985, 0.985, 0.985, 0.985, 0.985, 0.986, 0.986, 0.986, 0.986,
                    0.986, 0.986, 0.987, 0.987, 0.987, 0.987, 0.987, 0.987, 0.987, 0.987, 0.988, 0.988, 0.988, 0.988, 0.988, 0.988
                    ],
            0.98 : [
                    1.000, 0.996, 0.991, 0.986, 0.985, 0.984, 0.984, 0.983, 0.984, 0.984, 0.984, 0.984, 0.984, 0.985, 0.985, 0.986,
                    0.986, 0.986, 0.987, 0.987, 0.987, 0.987, 0.988, 0.988, 0.988, 0.988, 0.988, 0.988, 0.988, 0.988, 0.989, 0.989,
                    0.989, 0.989, 0.989, 0.989, 0.989, 0.989, 0.989, 0.989, 0.990, 0.990, 0.990, 0.990, 0.990, 0.990, 0.990, 0.990
                    ],
            0.99 : [
                    1.000, 0.997, 0.993, 0.989, 0.988, 0.987, 0.986, 0.986, 0.986, 0.986, 0.986, 0.986, 0.987, 0.987, 0.987, 0.988,
                    0.988, 0.988, 0.989, 0.989, 0.989, 0.989, 0.989, 0.989, 0.990, 0.990, 0.990, 0.900, 0.990, 0.990, 0.990, 0.990,
                    0.990, 0.990, 0.990, 0.990, 0.991, 0.991, 0.991, 0.991, 0.991, 0.991, 0.991, 0.991, 0.991, 0.991, 0.991, 0.991
                    ],
            'Note':
                    "*the critical value for alpha equal to 0.99 with 30 observations probably has a typo. The correct value is probably 0.990 instead of 0.900."
        }

        ### checking alpha value ###
        if alfa is None:
            alfa = self.alfa
        else:
            ## should be float ##
            checkers._check_is_float(alfa, "alfa", self.language)
            ## should be in the range (0,1) ##
            checkers._check_data_in_range(alfa, "alfa", 0.0, 1.0, self.language)

        ### checking the number of observations ###
        checkers._check_is_integer(n_rep, "n_rep", self.language)

        ### Getting the tabulated values ###
        if n_rep < 3:
            try:
                raise ValueError(messages[1][0][0])
                # raise ValueError("Error: very small number of observations")
            except ValueError:
                message1 = messages[2][0][0]
                general._display_one_line_attention(f"{message1} '{n_rep}'",)
                raise
        elif n_rep < 51: ## if n_rep is between 3 and 50 return the tabulated value ##
            if alfa == 0.01:
                tabulated = shapiro_wilk_table[0.01][n_rep - 3]
            elif alfa == 0.02:
                tabulated = shapiro_wilk_table[0.02][n_rep - 3]
            elif alfa == 0.05:
                tabulated = shapiro_wilk_table[0.05][n_rep - 3]
            elif alfa == 0.1:
                tabulated = shapiro_wilk_table[0.10][n_rep - 3]
            elif alfa == 0.5:
                tabulated = shapiro_wilk_table[0.50][n_rep - 3]
            else:
                tabulated = None # if you don't have a tabulated value for the chosen alpha value, return None #
        else: ## if n_rep is higher than 50, return tabulated value for 50 observations ##
            if alfa == 0.01:
                tabulated = shapiro_wilk_table[0.01][-1]
            elif alfa == 0.02:
                tabulated = shapiro_wilk_table[0.02][-1]
            elif alfa == 0.05:
                tabulated = shapiro_wilk_table[0.05][-1]
            elif alfa == 0.1:
                tabulated = shapiro_wilk_table[0.10][-1]
            elif alfa == 0.5:
                tabulated = shapiro_wilk_table[0.50][-1]
            else:
                tabulated = None # if you don't have a tabulated value for the chosen alpha value, return None #

        ### return the tabulated value and the graph axis ###
        result = namedtuple(messages[3][0][0], (messages[3][1][0], messages[3][2][0]))
        return result(tabulated, alfa)
    #
    # with some test, with text, with database, wtih docstring
    def shapiro_wilk(self, x_exp, alfa=None, n_digits=None, conclusion=None, details=None):
        """This function is just a wraper around scipy.stats.shapiro() [1]_ to perform the Shapiro Wilk normality test, but with some improvements.

        Parameters
        ----------
        x : numpy array
            One dimension :doc:`numpy array <numpy:reference/generated/numpy.array>` with at least 3 sample data.
        alfa : float, optional
            The level of significance (*ɑ*). Default is ``None`` which results in ``0.05``.
        n_digits : int, optional
            The maximum number of decimal places be shown. Default is ``None`` which results in ``4`` decimal places.
        conclusion : str, optional
            This parameter determines how to perform the comparison test to perform the Normality test. If ``conclusion = 'tabulate'`` (or ``None``, e.g, the default), the comparison test is made between the tabulated value (with *ɑ* significance level) and the calculated value of the test statistic. If ``'p_value'``, the comparison test is performed between the p-value and the adopted significance level (*ɑ*).
            **Both results should lead to the same conclusion.**
        details : string, optional
            The ``'details'`` parameter determines the amount of information presented about the hypothesis test. If ``'details' = 'short'`` (or ``None``, e.g, the default), a simplified version of the test result is returned. If ``'details' = 'full'``, a detailed version of the hypothesis test result is returned.

        Returns
        -------
        statistic : float
            The test statistic.
        tabulated : float or None
            The tabulated value for alpha equal to ``1%``, ``2%``, ``5%``, ``10%`` or ``50%``. Other values will return ``None``.
        p_value : float
            The p-value for the hypothesis test.
        conclusion : str
            The test conclusion (e.g, normal/ not normal).

        See Also
        --------
        anderson_darling : Performs the Anderson-Darling normality test (not implemented yet)
        kolmogorov_smirnov : Performs the Kolmogorov-Smirnov normality test (not implemented yet)
        lilieffors : Performs the Lilieffors normality test (not implemented yet)

        Notes
        -----
        The tabulated values [2]_ include samples with sizes between ``3`` and ``50``, for *ɑ* equal to ``1%``, ``2%``, ``5%``, ``10%`` or ``50%``. For data with a sample size higher than ``50``, the tabulated value returned is the value for ``50`` samples.

        The parameter ``conclusion`` uses the hypothesis test for normality test as follows:

        .. admonition:: \u2615

           H0: data comes from normal distribution.

           H1: data does not come from normal distribution.

        By default (``conclusion='tabulate'``), the conclusion is based on the comparison between the tabulated value (at *ɑ* significance level) and statistic of the test:

        .. admonition:: \u2615

           if tabulated <= statistic:
               Data is Normal
           else:
               Data is not Normal

        The other option (``conclusion='p_value'``) makes the conclusion comparing the p-value with *ɑ*:

        .. admonition:: \u2615

           if p-value >= *ɑ*:
               Data is Normal
           else:
               Data is not Normal

        Note that, if *ɑ* is not ``1%``, ``2%``, ``5%``, ``10%`` or ``50%``, the conclusion will always be performed using the p-value.

        The ``n_digits`` parameter does not influence any calculation, it just truncates the number of decimal places returned for the ``statistic``, ``tabulated`` and ``p_value`` parameters.

        References
        ----------
        .. [1] https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html
        .. [2] BRATLEY, P.; FOX, B. L.; SCHRAGE, L. E. A Guide to Simulation. 1. ed. New York: Springer, 1983 (Appendix A).

        Examples
        --------

        >>> from easy_stat.functions.distributions import ShapiroWilkNormalityTest
        >>> import numpy as np
        >>> import scipy.stats as stats
        >>> x = stats.norm.rvs(loc=5, scale=3, size=100, random_state=42)
        >>> normality_shapiro_wilk = ShapiroWilkNormalityTest()
        >>> results, conclusion = normality_shapiro_wilk.shapiro_wilk(x)
        >>> print(results)
        ShapiroWilkResult(Statistic=0.9898, Tabulated=0.947, p_value=0.6551, Alpha=0.05)
        >>> print(conclusion)
        Data is Normal at a 95.0% of confidence level.

        >>> from easy_stat.functions.distributions import ShapiroWilkNormalityTest
        >>> import numpy as np
        >>> import scipy.stats as stats
        >>> x = np.array([1.90642, 2.22488, 2.10288, 1.69742, 1.52229, 3.15435, 2.61826, 1.98492, 1.42738, 1.99568])
        >>> normality_shapiro_wilk = ShapiroWilkNormalityTest()
        >>> results, conclusion = normality_shapiro_wilk.shapiro_wilk(x)
        >>> print(results)
        ShapiroWilkResult(Statistic=0.9266,Tabulated=0.781, p_value=0.4161, Alpha=0.05)
        >>> print(conclusion)
        Data is Normal at a 99.0% of confidence level.

        >>> from easy_stat.functions.distributions import ShapiroWilkNormalityTest
        >>> import numpy as np
        >>> import scipy.stats as stats
        >>> x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        >>> normality_shapiro_wilk = ShapiroWilkNormalityTest()
        >>> results, conclusion = normality_shapiro_wilk.shapiro_wilk(x, alfa=0.10, details="full")
        >>> print(results)
        ShapiroWilkResult(Statistic=0.9698, Tabulated=0.869, p_value=0.889, Alpha=0.1)
        >>> print(conclusion)
        Since the tabulated value (0.869) <= statistic (0.9698), we have NO evidence to reject the hypothesis of data normality, according to the Shapiro-Wilk test at a 90.0% of confidence level.

        >>> from easy_stat.functions.distributions import ShapiroWilkNormalityTest
        >>> import numpy as np
        >>> import scipy.stats as stats
        >>> x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        >>> normality_shapiro_wilk = ShapiroWilkNormalityTest()
        >>> results, conclusion = normality_shapiro_wilk.shapiro_wilk(x, conclusion="p_value", details="full")
        >>> print(results)
        ShapiroWilkResult(Statistic=0.9698, Tabulated=0.842, p_value=0.889, Alpha=0.05)
        >>> print(conclusion)
        Since p-value (0.889) >= alpha (0.05), we have NO evidence to reject the hypothesis of data normality, according to the Shapiro-Wilk test at a 95.0% of confidence level.

        >>> from easy_stat.functions.distributions import ShapiroWilkNormalityTest
        >>> import numpy as np
        >>> import scipy.stats as stats
        >>> x = np.array([1,1.2,1.6,1.8, 2, 2.2, 3, 5, 7, 7.2, 8.2, 8.4, 8.6, 9])
        >>> normality_shapiro_wilk = ShapiroWilkNormalityTest()
        >>> results, conclusion = normality_shapiro_wilk.shapiro_wilk(x, details="full")
        >>> print(results)
        ShapiroWilkResult(Statistic=0.8413, Tabulated=0.874, p_value=0.0169, Alpha=0.05)
        >>> print(conclusion)
        Since the tabulated value (0.874) > statistic (0.8413), we HAVE evidence to reject the hypothesis of data normality, according to the Shapiro-Wilk test at a 95.0% of confidence level.

        """
        fk_id_function = management._query_func_id("shapiro_wilk")
        messages = management._get_messages(fk_id_function, self.language, "shapiro_wilk")

        ### getting the default alpha value ###
        if alfa is None:
            alfa = self.alfa
        else:
            checkers._check_is_float(alfa, "alfa", self.language)
            checkers._check_data_in_range(alfa, "alfa", 0.0, 1.0, self.language)
            self.alfa = alfa

        ### getting the default n_digits value ###
        if n_digits is None:
            n_digits = self.n_digits
        else:
            checkers._check_is_integer(n_digits, "n_digits", self.language)
            checkers._check_is_positive(n_digits, "n_digits", self.language)

        ### checking input data ###
        checkers._check_is_numpy_1_D(x_exp, "x_exp", self.language)
        self.x_exp = x_exp

        ### checking the conclusion parameter ###
        if conclusion is None:
            conclusion = "tabulate"
        else:
            checkers._check_is_str(conclusion, "conclusion", self.language)
            if conclusion == "tabulate":
                conclusion = "tabulate"
            elif conclusion == "p_value":
                conclusion = "p_value"
            else:
                try:
                    raise ValueError(messages[1][0][0])
                except ValueError:
                    general._display_one_line_attention(f"{messages[2][0][0]} '{conclusion}'",)
                    raise

        ### checking the details parameter ###
        if details == None:
            details = "short"
        else:
            checkers._check_is_str(details, "details", self.language)
            if details == "short":
                details = "short"
            elif details == "full":
                details = "full"
            else:
                try:
                    raise ValueError(messages[3][0][0])
                except ValueError:
                    general._display_one_line_attention(f"{messages[4][0][0]} {details}")
                    raise

        ### getting the tabulated value ###
        result = self.get_shapiro_wilk_tabulated_value(n_rep=x_exp.size, alfa=alfa)
        tabulated = result[0] # interessa apenas o primero valor

        ### calculating the test statistic value ###
        statistic, p_value = shapiro_wilk_scipy(x_exp)

        ### writing the test conclusion ###
        if conclusion == "tabulate":
            ## The test conclustion based on tabulated value depends on whether tabulated value exists. If not, make the conclusion with the same p-value ##
            if tabulated is None:
                # If there is no tabulated value, it first throws a warning
                general._display_warn(
                    aviso = f"     {messages[5][0][0]}",
                    texto = f"{messages[6][0][0]} = {alfa} {messages[6][2][0]}"
                )

                # then make the test #
                if p_value >= alfa:
                    if details == 'full':
                        msg = f"{messages[7][0][0]}{helpers._truncate(p_value, self.language, decs=n_digits)}{messages[7][2][0]}{alfa}{messages[7][4][0]} {100*(1-alfa)}{messages[7][6][0]}"
                        # general._display_one_line_attention(msg)
                    else:
                        msg = f"{messages[8][0][0]} {100*(1-alfa)}{messages[8][2][0]}"
                        # general._display_one_line_attention(msg)
                else:
                    if details == 'full':
                        msg = f"{messages[9][0][0]}{helpers._truncate(p_value, self.language, decs=n_digits)}{messages[9][2][0]}{alfa}{messages[9][4][0]} {100*(1-alfa)}{messages[9][6][0]}"
                        # general._display_one_line_attention(msg)
                    else:
                        msg = f"{messages[10][0][0]} {100*(1-alfa)}{messages[10][2][0]}"
                        # general._display_one_line_attention(msg)
            else: # if there is a tabulated value
                if tabulated <= statistic:
                    if details == 'full':
                        msg = f"{messages[11][0][0]}{helpers._truncate(tabulated, self.language, decs=n_digits)}{messages[11][2][0]}{helpers._truncate(statistic, self.language, decs=n_digits)}{messages[11][4][0]} {100*(1-alfa)}{messages[11][6][0]}"
                        # general._display_one_line_attention(msg)
                    else:
                        msg = f"{messages[8][0][0]} {100*(1-alfa)}{messages[8][2][0]}"
                        # general._display_one_line_attention(msg)
                else:
                    if details == 'full':
                        msg = f"{messages[12][0][0]}{helpers._truncate(tabulated, self.language, decs=n_digits)}{messages[12][2][0]}{helpers._truncate(statistic, self.language, decs=n_digits)}{messages[12][4][0]} {100*(1-alfa)}{messages[12][6][0]}"
                        # general._display_one_line_attention(msg)
                    else:
                        msg = f"{messages[10][0][0]} {100*(1-alfa)}{messages[10][2][0]}"
                        # general._display_one_line_attention(msg)
        else: # se é pra utilizar o p-valor mesmo
            if p_value >= alfa:
                if details == 'full':
                    msg = f"{messages[7][0][0]}{helpers._truncate(p_value, self.language, decs=n_digits)}{messages[7][2][0]}{alfa}{messages[7][4][0]} {100*(1-alfa)}{messages[7][6][0]}"
                    # general._display_one_line_attention(msg)
                else:
                    msg = f"{messages[8][0][0]} {100*(1-alfa)}{messages[8][2][0]}"
                    # general._display_one_line_attention(msg)
            else:
                if details == 'full':
                    msg = f"{messages[9][0][0]}{helpers._truncate(p_value, self.language, decs=n_digits)}{messages[9][2][0]}{alfa}{messages[9][4][0]} {100*(1-alfa)}{messages[9][6][0]}"
                    # general._display_one_line_attention(msg)
                else:
                    msg = f"{messages[10][0][0]} {100*(1-alfa)}{messages[10][2][0]}"
                    # general._display_one_line_attention(msg)

        result = namedtuple(messages[13][0][0], (messages[14][0][0], messages[15][0][0], messages[16][0][0], messages[17][0][0]))
        self.msg = msg
        self.statistic = statistic
        self.tabulated = tabulated
        self.p_value = p_value
        return result(helpers._truncate(statistic, self.language, decs=n_digits), helpers._truncate(tabulated, self.language, decs=n_digits), helpers._truncate(p_value, self.language, decs=n_digits), self.alfa), self.msg

    # with some test, with text, with database, wtih docstring
    def shapiro_wilk_to_xlsx(self, file_name=None, sheet_names=None):
        """This method exports the data to excel type files.
        This function is just a wraper around :doc:`pd.DataFrame.to_excel <pandas:reference/api/pandas.DataFrame.to_excel>` [1]_ to export ``.xlsx`` files.

        Parameters
        ----------
        file_name : str, optional
            The name of the file to be exported, without its extension (default is ``None`` which results in a file name ``'shapiro_wilk.xlsx'``).
        sheet_names : list of two strings, optional
            A list containing the name of the worksheets where the data will be saved:

                * The first element corresponds to the name of the worksheet where the calculated data will be saved (default is ``None`` which means ``'shapiro_wilk'``).

                * The second element corresponds to the name of the worksheet where the supplied data will be saved (default is ``None`` which means ``'data'``).

        Returns
        -------
        df_list : A list of two pandas DataFrame
            The first element is a ``pd.DataFrame`` with the Shapiro Wilk calculated data.
            The second element is a ``pd.DataFrame`` with the supplied data.

        Notes
        -----
        The ``shapiro_wilk()`` method needs to be applied beforehand.

        If a spreadsheet with the same name already exists in the current directory and this files contains tabs with conflicting names, the new tabs will be inserted into the file with different names, preserving the original data.

        References
        ----------
        .. [1] https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html

        Examples
        --------

        >>> from easy_stat.functions.distributions import ShapiroWilkNormalityTest
        >>> import numpy as np
        >>> my_data = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        >>> normality_shapiro_wilk = ShapiroWilkNormalityTest()
        >>> normality_shapiro_wilk.shapiro_wilk(my_data)
        >>> normality_shapiro_wilk.shapiro_wilk_to_xlsx()
        >>>
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            The data has been exported to file shapiro_wilk.xlsx
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


        Download the exported file by :download:`clicking here <assets/shapiro_wilk.xlsx>`.

        >>> from easy_stat.functions.distributions import ShapiroWilkNormalityTest
        >>> import numpy as np
        >>> my_data = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        >>> normality_shapiro_wilk = ShapiroWilkNormalityTest(language='pt-br')
        >>> normality_shapiro_wilk.shapiro_wilk(my_data)
        >>> normality_shapiro_wilk.shapiro_wilk_to_xlsx(file_name="my_data")
        >>>
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            Os dados foram exportados para o arquivo my_data.xlsx
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


        Download the exported file by :download:`clicking here <assets/my_data.xlsx>`.


        >>> from easy_stat.functions.distributions import ShapiroWilkNormalityTest
        >>> import numpy as np
        >>> my_data = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        >>> normality_shapiro_wilk = ShapiroWilkNormalityTest()
        >>> normality_shapiro_wilk.shapiro_wilk(my_data)
        >>> normality_shapiro_wilk.shapiro_wilk_to_xlsx(file_name="my_new_data", sheet_names=["my_test", "my_data"])
        >>>
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            The data has been exported to file my_new_data.xlsx
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        Download the exported file by :download:`clicking here <assets/my_new_data.xlsx>`.


        """
        if self.msg is None:
            fk_id_function = management._query_func_id("ShapiroWilkNormalityTest")
            messages = management._get_messages(fk_id_function, self.language)
            general._display_one_line_attention(messages[1][0][0])
        else:
            # quering
            fk_id_function = management._query_func_id("shapiro_wilk_to_xlsx")
            messages = management._get_messages(fk_id_function, self.language)

            # batizando o nome do arquivo
            if file_name is None:
                file_name = "shapiro_wilk"
            else:
                checkers._check_is_str(file_name, 'file_name', self.language)
                helpers._check_forbidden_character(file_name, "file_name", self.language)
            ## verificando o sheet_names
            if sheet_names is None:
                sheet_names = [
                    "shapiro_wilk",
                    "data"
                ]
            else:
                # verificando se é uma lista
                checkers._check_is_list(sheet_names, "sheet_names", self.language)
                # verificando se a lista tem 2 elementos
                if len(sheet_names) != 2:
                    try:
                        raise ValueError(messages[1][0][0])
                    except ValueError:
                        # "query"
                        sheet_names = [f"  --->  {sheet}" for sheet in sheet_names]
                        msg = [
                            f"{messages[2][0][0]} 'sheet_names' {messages[2][2][0]}: {len(sheet_names)}",
                            sheet_names
                            ]
                        msg = general._flatten_list_of_list_string(msg)
                        msg = list(msg)
                        general._display_n_line_attention(msg)
                        raise
                # verficanado se cada elemento da lista é uma string valida
                for sheet_name in sheet_names:
                    checkers._check_is_str(sheet_name, "sheet_names", self.language)
                    helpers._check_forbidden_character(sheet_name, "sheet_names", self.language)

            ### pegando o df_summary e o df_data
            ## datafram com os dados
            df_data = pd.DataFrame(columns=["data"], data=self.x_exp)

            df_shapiro_wilk = pd.DataFrame(columns=[messages[3][0][0], messages[4][0][0]])
            df_shapiro_wilk[messages[3][0][0]] = [
                        messages[5][0][0],
                        messages[6][0][0],
                        messages[7][0][0],
                        messages[8][0][0],
                        messages[9][0][0],
                        ]

            df_shapiro_wilk[messages[4][0][0]] = [
                        self.statistic,
                        self.tabulated,
                        self.p_value,
                        self.alfa,
                        self.msg,
                        ]

            df_list = [df_shapiro_wilk, df_data]
            #
            result = helpers._export_to_xlsx(df_list, file_name=file_name, sheet_names=sheet_names, language=self.language)
            return df_list

    # with some test, with text, with database, wtih docstring
    def shapiro_wilk_to_csv(self, file_name=None, sep=","):
        """Export the data to csv file
        This function is just a wraper around :doc:`pd.DataFrame.to_csv <pandas:reference/api/pandas.DataFrame.to_csv>` [1]_ to export ``.csv`` files.

        Parameters
        ----------
        file_name : str, optional
            The name of the file to be exported, without its extension (default is ``None``, which results in a file named ``'shapiro_wilk.csv'``)
        sep : str of length 1, optional
            Field delimiter for the output file (default is ``None``, which uses the comma (``','``)). This is the ``sep`` parameter of the ``pd.DataFrame.to_csv()`` pandas method.

        Returns
        -------
        df : ``pd.DataFrame``
            A DataFrame containing the data used to export the ``csv`` file.

        Notes
        -----
        The ``shapiro_wilk()`` method needs to be applied beforehand.

        If there is a file with the same name passed through the ``file_name`` parameter in the current directory, the file will be exported with a different name.

        References
        ----------
        .. [1] https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html


        Examples
        --------

        >>> from easy_stat.functions.distributions import ShapiroWilkNormalityTest
        >>> import numpy as np
        >>> my_data = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        >>> normality_shapiro_wilk = ShapiroWilkNormalityTest()
        >>> normality_shapiro_wilk.shapiro_wilk(my_data)
        >>> normality_shapiro_wilk.shapiro_wilk_to_csv()
        >>>
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            The 'shapiro_wilk.csv' was exported!
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


        Download the exported file by :download:`clicking here <assets/shapiro_wilk.csv>`.


        >>> from easy_stat.functions.distributions import ShapiroWilkNormalityTest
        >>> import numpy as np
        >>> my_data = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        >>> normality_shapiro_wilk = ShapiroWilkNormalityTest(language='pt-br')
        >>> normality_shapiro_wilk.shapiro_wilk(my_data)
        >>> normality_shapiro_wilk.shapiro_wilk_to_csv(file_name="my_data", sep=';')
        >>>
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            O arquivo 'my_data.csv' foi exportado!
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        Download the exported file by :download:`clicking here <assets/my_data.csv>`.

        """

        if self.msg is None:
            fk_id_function = management._query_func_id("ShapiroWilkNormalityTest")
            messages = management._get_messages(fk_id_function, self.language)
            general._display_one_line_attention(messages[1][0][0])

        else:
            # batizando o nome do arquivo
            if file_name is None:
                file_name = "shapiro_wilk"
            else:
                # checking the fle_name
                checkers._check_is_str(file_name, 'file_name', self.language)
                helpers._check_forbidden_character(file_name, "file_name", self.language)

            # quering
            fk_id_function = management._query_func_id("shapiro_wilk_to_csv")
            messages = management._get_messages(fk_id_function, self.language, "shapiro_wilk_to_csv")

            # criando o data frame para exportar via csv
            data_index = list(np.arange(1, self.x_exp.size + 1))
            x_exp = list(self.x_exp)
            df = pd.DataFrame(columns=[messages[1][0][0], messages[2][0][0]])
            df[messages[1][0][0]] = [
                        messages[3][0][0],
                        messages[4][0][0],
                        messages[5][0][0],
                        messages[6][0][0],
                        messages[7][0][0],
                        '-',
                        messages[8][0][0],
                        ] + data_index

            df[messages[2][0][0]] = [
                        self.statistic,
                        self.tabulated,
                        self.p_value,
                        self.alfa,
                        self.msg,
                        '-',
                        messages[9][0][0],
                        ] + x_exp

            # exporting
            result = helpers._export_to_csv(df, file_name=file_name, sep=sep, language=self.language)
            return df



    def __str__(self):
        if self.msg is None:
            fk_id_function = management._query_func_id("ShapiroWilkNormalityTest")
            messages = management._get_messages(fk_id_function, self.language)
            return messages[1][0][0]
        else:
            return self.msg

    def __repr__(self):
        fk_id_function = management._query_func_id("ShapiroWilkNormalityTest")
        messages = management._get_messages(fk_id_function, self.language)
        return messages[2][0][0]





# Ooh, I see you, see you, see you every time https://youtu.be/rl9FFZZnWWo?t=35
