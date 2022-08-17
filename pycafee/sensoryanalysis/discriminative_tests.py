"""This module focuses on discriminative sensory analysis tests

These tests are usually separated into two groups (difference tests and sensitivity test), but else will be added as a single group in this module. Each class will have a single test.

Difference tests:

- paired comparison;
- triangular;
- duo-trio;
- multiple comparison;
- ordering;
- A or Not-A;
- two out of five.

Sensitivity tests:

- Limits;
- constant stimulation;
- dilution.


"""


#########################################
################ Imports ################
#########################################

###### Standard ######
from collections import namedtuple

###### Third part ######
import numpy as np
import pandas as pd
from tabulate import tabulate
import scipy.stats as stats

###### Home made ######


from pycafee.utils import helpers
from pycafee.utils import general
from pycafee.utils import checkers

from pycafee.utils.helpers import AlphaManagement, NDigitsManagement, LanguageManagement



from pycafee.database_management import management

###########################################
################ Functions ################
###########################################



class TriangleTest(AlphaManagement, NDigitsManagement):


    def __init__(self, name=None, alfa=None, language=None, n_digits=None, **kwargs):
        super().__init__(alfa=alfa, language=language, n_digits=n_digits, **kwargs)
        self.conclusion = None
        self.statistic = None
        self.critical = None
        self.x_exp = None




    def get_number_assessors(self, pd=None, beta=None, alfa=None):
        """This function returns the minimum number of assessors to perform the triangular test.

        Parameters
        ----------
        pd : ``str``
            The proportion of the population represented by the assessors that can distinguish between the two products. It can be:

            * ``50%``;
            * ``40%``;
            * ``30%`` (default);
            * ``20%``;
            * ``10%``;

        alfa: ``float``
            The probability of concluding that a perceptible difference exists when, in reality, one does not (Type I Error). It can be:

            * ``0.20``;
            * ``0.10``;
            * ``0.05`` (default);
            * ``0.01``;
            * ``0.001``;

        beta: ``float``
            The probability of concluding that no perceptible difference exists when, in reality, one does (Type II Error). It can be:

            * ``0.20``;
            * ``0.10``;
            * ``0.05`` (default);
            * ``0.01``;
            * ``0.001``;

        Returns
        -------
        n_assessors: ``int``
            The minimum number of assessors to perform the triangular test

        References
        ----------
        .. [1] Standard Test Method for Sensory Analysis—Triangle Test, Designation: E1885 − 04, 2011.


        Examples
        --------


        """

        # ----- checking alpha value ----- #
        if alfa is None:
            alfa = self.alfa
        else:
            # --- should be float --- #
            checkers._check_is_float(alfa, "alfa", self.language)
            # --- should be in the range (0,1) --- #
            checkers._check_data_in_range(alfa, "alfa", 0.0, 1.0, self.language)

        ### checking the pd ###
        if pd is None:
            pd = "30%"
        else:
            checkers._check_is_str(pd, "pd", language=self.language)

            alloweds = ["10%", "20%", "30%", "40%", "50%"]

            if pd not in alloweds:
                fk_id_function = management._query_func_id("generic")
                messages = management._get_messages(fk_id_function, self.language, "generic")
                try:
                    error = messages[3][0][0]
                    raise ValueError(error)
                except ValueError:
                    msg = [f"{messages[4][0][0]} 'pd' {messages[4][2][0]}:"]
                    for item in alloweds:
                        msg.append(f"   --->    {item}")
                    msg.append(f"{messages[4][4][0]}:")
                    msg.append(f"   --->    {pd}")
                    general._display_n_line_attention(msg)
                    raise









        inputs = {
            "pd": pd,
            "alfa": alfa,
            "beta": beta
            }

        if beta == 0.20:
            position = 0
        elif beta == 0.10:
            position = 1
        elif beta == 0.05:
            position = 2
        elif beta == 0.01:
            position = 3
        elif beta == 0.001:
            position = 4
        else:
            position = 4


        minimum_number_of_assessors = {
            "50%": {
                0.20: [7, 12, 16, 25, 36],
                0.10: [12, 15, 20, 30, 43],
                0.05: [16, 20, 23, 35, 48],
                0.01: [25, 30, 35, 47, 62],
                0.001: [36, 43, 48, 62, 81],
            },
            "40%": {
                0.20: [12, 17, 25, 36, 55],
                0.10: [17, 25, 30, 46, 67],
                0.05: [23, 30, 40, 57, 79],
                0.01: [35, 47, 56, 76, 102],
                0.001: [55, 68, 76, 102, 130]
            },
            "30%": {
                0.20: [20, 28, 39, 64, 97],
                0.10: [30, 43, 54, 81, 119],
                0.05: [40, 53, 66, 98, 136],
                0.01: [62, 82, 97, 131, 181],
                0.001: [93, 120, 138, 181, 233]
            },
            "20%": {
                0.20: [39, 64, 86, 140, 212],
                0.10: [62, 89, 119, 178, 260],
                0.05: [87, 117, 147, 213, 305],
                0.01: [136, 176, 211, 292, 397],
                0.001: [207, 257, 302, 396, 513]
            },
            "10%": {
                0.20: [149, 238, 325, 529, 819],
                0.10: [240, 348, 457, 683, 1011],
                0.05: [325, 447, 572, 828, 1181],
                0.01: [525, 680, 824, 1132, 1539],
                0.001: [803, 996, 1165, 1530, 1992]
            }
        }

        output = minimum_number_of_assessors[pd][alfa][position]

        return output, inputs






# print(get_number_assessors(pd="10%", alfa=0.05, beta=0.05))

# def minimum_of_correct_responses(n, alfa, which=None):
#
#
#     if n == 6 and alfa == 0.001:
#         raise ValueError
#
#
#
#
#     def _min_responses(n, alfa):
#         # t values
#         z = round(stats.t.ppf(1-alfa, 1000000),2)
#         # calculating the minimum
#         min = (n/3) + z*np.sqrt(2*n)/3
#         # rounding to nearest whole number greater than min
#         min_correct = int(min + 0.5) + 1
#         return min_correct
#
#
#     # getting the critical value position based on significance level
#     if alfa == 0.20:
#         position = 0
#     elif alfa == 0.10:
#         position = 1
#     elif alfa == 0.05:
#         position = 1
#     elif alfa == 0.01:
#         position = 3
#     elif alfa == 0.001:
#         position = 4
#     else:
#         raise ValueError
#
#
#
#     # critical values
#     critical = {
#         6: [4, 5, 5, 6, "X"],
#         7: [4, 5, 5, 6, 7],
#         8: [5, 5, 6, 7, 8],
#         9: [5, 6, 6, 7, 8],
#         10: [6, 6, 7, 8, 9],
#         11: [6, 7, 7, 8, 10],
#         12: [6, 7, 8, 9, 10],
#         13: [7, 8, 8, 9, 11],
#         15: [8, 8, 9, 10, 12],
#         14: [7, 8, 9, 10, 11],
#         16: [8, 9, 9, 11, 12],
#         17: [8, 9, 10, 11, 13],
#         18: [9, 10, 10, 12, 13],
#         19: [9, 10, 11, 12, 14],
#         20: [9, 10, 11, 13, 14],
#         21: [10, 11, 12, 13, 15],
#         22: [10, 11, 12, 14, 15],
#         23: [11, 12, 12, 14, 16],
#         24: [11, 12, 13, 15, 16],
#         25: [11, 12, 13, 15, 17],
#         26: [12, 13, 14, 15, 17],
#         27: [12, 13, 14, 16, 18],
#         28: [12, 14, 15, 16, 18],
#         29: [13, 14, 15, 17, 19],
#         30: [13, 14, 15, 17, 19],
#         31: [14, 15, 16, 18, 20],
#         32: [14, 15, 16, 18, 20],
#         33: [14, 15, 17, 18, 21],
#         34: [15, 16, 17, 19, 21],
#         35: [15, 16, 17, 19, 22],
#         36: [15, 17, 18, 20, 22],
#         37: [16, 17, 18, 20, 22],
#         38: [16, 17, 19, 21, 23],
#         39: [16, 18, 19, 21, 23],
#         40: [17, 18, 19, 21, 24],
#         41: [17, 19, 20, 22, 24],
#         42: [18, 19, 20, 22, 25],
#         43: [18, 19, 20, 23, 25],
#         44: [18, 20, 21, 23, 26],
#         45: [19, 20, 21, 24, 26],
#         46: [19, 20, 22, 24, 27],
#         47: [19, 21, 22, 24, 27],
#         48: [20, 21, 22, 25, 27],
#         54: [22, 23, 25, 27, 30],
#         60: [24, 26, 27, 30, 33],
#         66: [26, 28, 29, 32, 35],
#         72: [28, 30, 32, 34, 38],
#         78: [30, 32, 34, 37, 40],
#         84: [33, 35, 36, 39, 43],
#         90: [35, 37, 38, 42, 45],
#         96: [37, 39, 41, 44, 48],
#         102: [39, 41, 43, 46, 50]
#     }
#
#
#     if which == "original":
#         if n not in critical.keys():
#             min_responses = _min_responses(n, alfa)
#         else:
#             min_responses = critical[n][position]
#     else:
#         min_responses = _min_responses(n, alfa)
#
#
#
#     return min_responses
#
#
#
#
# enes = [7, 8, 9, 10, 11, 12, 13, 15, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
#         29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 54,
#         60, 66, 72, 78, 84, 90, 96, 102]
#
# for ene in enes:
#     print(minimum_of_correct_responses(n=ene, alfa=0.05))

# n_panelists = 500
#
#
# data = np.arange(100, 1000)
# while len(data) < n_panelists*3:
#     data = np.repeat(data, 2)
#
# print(len(data))
#
#
# # print(data)
# np.random.seed(42)
# ale = np.random.choice(data, n_panelists*3, replace=False)
#
# ale = np.array_split(ale, 3)


# combinations = ["ABB", "AAB", "ABA", "BAA", "BBA", "BAB"]
#
# def repeat_items(l, c):
#     return l * (c // len(l)) + l[:(c % len(l))]
#
# all_combinations = repeat_items(combinations, n_panelists)
#
# df = pd.DataFrame(columns=["Panelist", "Sample 1", "Sample 2", "Sample 3"])
# df["Panelist"] = range(1, n_panelists+1)
# first = []
# second = []
# third = []
#
# for i in range(n_panelists):
#     first.append(f"{all_combinations[i][0]} - {ale[0][i]}")
#     second.append(f"{all_combinations[i][1]} - {ale[1][i]}")
#     third.append(f"{all_combinations[i][2]} - {ale[2][i]}")
#
#
#
# df["Sample 1"] = first
# df["Sample 2"] = second
# df["Sample 3"] = third
#
#
#
#
#
#
# # df["First"] =
# print(df)
















#






























#
