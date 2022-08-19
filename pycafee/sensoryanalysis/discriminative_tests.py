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
        self.df_table = None



    # with tests, with text, with database, with docstring
    def get_number_assessors(self, pd=None, beta=None, alfa=None):
        """This function returns the minimum number of assessors to perform the triangular test [1]_.

        Parameters
        ----------
        pd : ``str``, optional
            The proportion of the population represented by the assessors that can distinguish between the two products. It can be:

            * ``50%``;
            * ``40%``;
            * ``30%`` (default);
            * ``20%``;
            * ``10%``;


        alfa : ``float``, optional
            The probability of concluding that a perceptible difference exists when, in reality, one does not (Type I Error). It can be:

            * ``0.20``;
            * ``0.10``;
            * ``0.05`` (default);
            * ``0.01``;
            * ``0.001``;


        beta : ``float``, optional
            The probability of concluding that no perceptible difference exists when, in reality, one does (Type II Error). It can be:

            * ``0.20``;
            * ``0.10``;
            * ``0.05`` (default);
            * ``0.01``;
            * ``0.001``;


        Returns
        -------
        n_assessors : ``int``
            The minimum number of assessors to perform the triangular test
        inputs : ``dict``
            A dictionary with the parameters used to obtain the minimum value of assessors


        References
        ----------
        .. [1] Standard Test Method for Sensory Analysis—Triangle Test, Designation: E1885 − 04, 2011.


        Examples
        --------

        >>> from pycafee.sensoryanalysis.discriminative_tests import TriangleTest
        >>> tringular = TriangleTest()
        >>> result, input = tringular.get_number_assessors()
        >>> print(result)
        TriangleTest(minimum_number_of_assessors=66)
        >>> print(input)
        {'pd': '30%', 'alfa': 0.05, 'beta': 0.05}


        >>> from pycafee.sensoryanalysis.discriminative_tests import TriangleTest
        >>> tringular = TriangleTest()
        >>> result, input = tringular.get_number_assessor(pd="10%", alfa=0.01)
        >>> print(result)
        TriangleTest(minimum_number_of_assessors=824)
        >>> print(input)
        {'pd': '10%', 'alfa': 0.01, 'beta': 0.05}


        >>> from pycafee.sensoryanalysis.discriminative_tests import TriangleTest
        >>> tringular = TriangleTest(language="pt-br")
        >>> result, input = tringular.get_number_assessors(pd="20%", alfa=0.05, beta=0.10)
        >>> print(result)
        TesteTriangular(numero_minimo_de_avaliadores=117)
        >>> print(input)
        {'pd': '20%', 'alfa': 0.05, 'beta': 0.1}


        """

        # ----- checking alpha value ----- #
        if alfa is None:
            alfa = self.alfa
        else:
            # --- should be float --- #
            checkers._check_is_float(alfa, "alfa", self.language)
            # --- should be in the range (0,1) --- #
            checkers._check_data_in_range(alfa, "alfa", 0.0, 1.0, self.language)
            # --- must be in --- #
            alloweds = [0.20, 0.10, 0.05, 0.01, 0.001]
            helpers._raises_wrong_param("alfa", alloweds, alfa, self.language)

        # ----- checking beta value ----- #
        if beta is None:
            beta = 0.05
        else:
            # --- should be float --- #
            checkers._check_is_float(beta, "beta", self.language)
            # --- should be in the range (0,1) --- #
            checkers._check_data_in_range(beta, "beta", 0.0, 1.0, self.language)
            # --- must be in --- #
            alloweds = [0.20, 0.10, 0.05, 0.01, 0.001]
            helpers._raises_wrong_param("beta", alloweds, beta, self.language)


        # ----- checking the pd value ----- #
        if pd is None:
            pd = "30%"
        else:
            # --- should be str --- #
            checkers._check_is_str(pd, "pd", language=self.language)
            # --- must be in --- #
            alloweds = ["10%", "20%", "30%", "40%", "50%"]
            helpers._raises_wrong_param("pd", alloweds, pd, self.language)

        fk_id_function = management._query_func_id("discriminative_tests")
        messages = management._get_messages(fk_id_function, self.language, "discriminative_tests")
        # ----- grouping entries into a dictionary ----- #
        inputs = {
            "pd": pd,
            messages[1][2][0]: alfa,
            messages[1][3][0]: beta
            }

        # ----- getting the position for each beta value ----- #
        if beta == 0.20:
            position = 0
        elif beta == 0.10:
            position = 1
        elif beta == 0.05:
            position = 2
        elif beta == 0.01:
            position = 3
        else:
            position = 4

        # ----- dictionary with the data ----- #
        n_assessors = {
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

        # ----- getting the results ----- #
        minimum_number_of_assessors = n_assessors[pd][alfa][position]

        result = namedtuple(messages[1][0][0], (messages[1][1][0],))
        return result(minimum_number_of_assessors), inputs


    # with tests, with text, with database, with docstring
    def minimum_of_correct_responses(self, n_of_assessors, alfa=None, which=None):
        """This functions returns the minimum number of correct responses required for significance at the stated α level for the corresponding number of assessors.

        Parameters
        ----------
        n_of_assessors : ``int``
            The number of assessors (greater than 6)

        alfa : ``float``, optional
            The significance level. It can be:

            * ``0.20``;
            * ``0.10``;
            * ``0.05`` (default);
            * ``0.01``;
            * ``0.001``;


        which : ``str``, optional
            A forma de obter o resultado.

            * If ``"function"`` (default), the equation given in [1]_ is used;
            * If ``"original"``, the tabulated values provided by [1]_ are used;


        Returns
        -------
        min_responses : ``int``
            The minimum number of correct responses required for significance at the stated α level
        inputs : ``dict``
            A dictionary with the parameters used to obtain the result


        Notes
        -----
        In cases where the original values are not available, the value is returned using ``which="function"`` instead of ``which="original"``.

        In a small number of combinations between the level of significance and the number of assessors, there are discrepancies between the original results and the respective calculated values. In all cases the difference is one less right answer, that is, the original values are more conservative than the values obtained with the equation.


        The minimum number of correct answers is estimated using the following relationship:

        .. math::
                min = \\frac{n_{assessors + t_{\\infty} \\sqrt{2n_{assessors}}}}{3}

        where :math:`t_{\\infty}` is the value of the one-sided student t distribution for infinite degrees of freedom (1000000) rounded to 2 decimal places. The value of t is obtained using ``stats.t.ppf(1-alfa, 1000000)``


        References
        ----------
        .. [1] Standard Test Method for Sensory Analysis—Triangle Test, Designation: E1885 − 04, 2011.


        Examples
        --------

        >>> from pycafee.sensoryanalysis.discriminative_tests import TriangleTest
        >>> tringular = TriangleTest()
        >>> result = tringular.minimum_of_correct_responses(10)
        >>> print(result)
        TriangleTest(minimum_of_correct_responses=7)
        >>> print(inputs)
        {'alpha': 0.05, 'which': 'original'}


        >>> from pycafee.sensoryanalysis.discriminative_tests import TriangleTest
        >>> tringular = TriangleTest(language="pt-br")
        >>> result, inputs = tringular.minimum_of_correct_responses(36)
        >>> print(result)
        TesteTriangular(minimo_de_respostas_corretas=18)
        >>> print(inputs)
        {'alfa': 0.05, 'which': 'original'}


        >>> from pycafee.sensoryanalysis.discriminative_tests import TriangleTest
        >>> tringular = TriangleTest()
        >>> result, inputs = tringular.minimum_of_correct_responses(36, alfa = 0.01)
        >>> print(result)
        TriangleTest(minimum_of_correct_responses=20)
        >>> print(inputs)
        {'alpha': 0.01, 'which': 'original'}


        """
        # ----- checking n_of_assessors value ----- #
        checkers._check_is_integer(n_of_assessors, "n_of_assessors", self.language)
        checkers._check_value_is_equal_or_higher_than(n_of_assessors, "n_of_assessors", 6, language=self.language)

        # ----- checking alpha value ----- #
        if alfa is None:
            alfa = self.alfa
        else:
            # --- should be float --- #
            checkers._check_is_float(alfa, "alfa", self.language)
            # --- should be in the range (0,1) --- #
            checkers._check_data_in_range(alfa, "alfa", 0.0, 1.0, self.language)
            # --- must be in --- #
            alloweds = [0.20, 0.10, 0.05, 0.01, 0.001]
            helpers._raises_wrong_param("alfa", alloweds, alfa, self.language)



        # ----- checking which value ----- #
        if which is None:
            which = "original"
        else:
            # --- should be str --- #
            checkers._check_is_str(which, "which", self.language)
            # --- must be in --- #
            alloweds = ["function", "original"]
            helpers._raises_wrong_param("which", alloweds, which, self.language)


        # ----- getting the position for each alfa value ----- #
        if alfa == 0.20:
            position = 0
        elif alfa == 0.10:
            position = 1
        elif alfa == 0.05:
            position = 2
        elif alfa == 0.01:
            position = 3
        else:
            position = 4

        # critical values
        critical = {
            6: [4, 5, 5, 6],
            7: [4, 5, 5, 6, 7],
            8: [5, 5, 6, 7, 8],
            9: [5, 6, 6, 7, 8],
            10: [6, 6, 7, 8, 9],
            11: [6, 7, 7, 8, 10],
            12: [6, 7, 8, 9, 10],
            13: [7, 8, 8, 9, 11],
            15: [8, 8, 9, 10, 12],
            14: [7, 8, 9, 10, 11],
            16: [8, 9, 9, 11, 12],
            17: [8, 9, 10, 11, 13],
            18: [9, 10, 10, 12, 13],
            19: [9, 10, 11, 12, 14],
            20: [9, 10, 11, 13, 14],
            21: [10, 11, 12, 13, 15],
            22: [10, 11, 12, 14, 15],
            23: [11, 12, 12, 14, 16],
            24: [11, 12, 13, 15, 16],
            25: [11, 12, 13, 15, 17],
            26: [12, 13, 14, 15, 17],
            27: [12, 13, 14, 16, 18],
            28: [12, 14, 15, 16, 18],
            29: [13, 14, 15, 17, 19],
            30: [13, 14, 15, 17, 19],
            31: [14, 15, 16, 18, 20],
            32: [14, 15, 16, 18, 20],
            33: [14, 15, 17, 18, 21],
            34: [15, 16, 17, 19, 21],
            35: [15, 16, 17, 19, 22],
            36: [15, 17, 18, 20, 22],
            37: [16, 17, 18, 20, 22],
            38: [16, 17, 19, 21, 23],
            39: [16, 18, 19, 21, 23],
            40: [17, 18, 19, 21, 24],
            41: [17, 19, 20, 22, 24],
            42: [18, 19, 20, 22, 25],
            43: [18, 19, 20, 23, 25],
            44: [18, 20, 21, 23, 26],
            45: [19, 20, 21, 24, 26],
            46: [19, 20, 22, 24, 27],
            47: [19, 21, 22, 24, 27],
            48: [20, 21, 22, 25, 27],
            54: [22, 23, 25, 27, 30],
            60: [24, 26, 27, 30, 33],
            66: [26, 28, 29, 32, 35],
            72: [28, 30, 32, 34, 38],
            78: [30, 32, 34, 37, 40],
            84: [33, 35, 36, 39, 43],
            90: [35, 37, 38, 42, 45],
            96: [37, 39, 41, 44, 48],
            102: [39, 41, 43, 46, 50]
        }

        fk_id_function = management._query_func_id("discriminative_tests")
        messages = management._get_messages(fk_id_function, self.language, "discriminative_tests")

        # ----- grouping entries into a dictionary ----- #
        inputs = {
            messages[1][2][0]: alfa,
            "which": which
        }

        if which == "function":
            min_responses = _min_responses(n_of_assessors, alfa)
        else:
            if n_of_assessors in critical.keys():
                try:
                    min_responses = critical[n_of_assessors][position]

                except IndexError: # requeried due to n_of_assessors = 6 and alfa = 0.001 is missing
                    min_responses = _min_responses(n_of_assessors, alfa)
                    general._display_warn(messages[2][0][0], messages[2][1][0])
                    inputs["which"] = "function"
            else: # for missing n_of_assessors values
                min_responses = _min_responses(n_of_assessors, alfa)
                aviso = f"{messages[2][2][0]} {n_of_assessors}{messages[2][4][0]}"
                general._display_warn(messages[2][0][0], aviso)
                inputs["which"] = "function"

        result = namedtuple(messages[1][0][0], (messages[1][4][0],))
        return result(min_responses), inputs


    # with tests, with text, with database, with docstring
    def make_combinations(self, n_of_assessors, seed=None, shuffle=None, reorder=None):
        """This function creates a dataframe with all the combinations to apply the triangle test.


        Parameters
        ----------
        n_of_assessors : ``int``
            The number of assessors (greater than 6)
        seed : ``int`` (positive), optional
            The seed that controls the randomness of the output.

            * If ``None`` (default), three-digit numbers are randomly generated without a specific seed;
            * If a number, three-digit numbers are generated using randomness specified by the seed (which can be used to replicate the random results).


        shuffle : ``bool``, optional
            Whether permutations between ``"A"`` and ``"B"`` should be randomized or not.

            * If ``True`` (default), the six possible combinations will be randomized. The ``seed`` parameter controls the randomness of this parameter;
            * If ``False``, the combinations follow the following pattern: ``"AAB", "ABA", "ABB", "BBA", "BAB", "BAA"``.

        reorder : ``bool``, optional
            Whether the table should should be randomized or not.

            * If ``True``, the table will be randomized. The ``seed`` parameter controls the randomness of this parameter;
            * If ``False`` (default), the table will keep the original pattern.


        Returns
        -------
        min_responses : ``pd.DataFrame``
            The dataframe with all the combinations required to prepare the Triangle Test
        inputs : ``dict``
            A dictionary with the parameters used to obtain the table



        References
        ----------
        .. [1] Standard Test Method for Sensory Analysis—Triangle Test, Designation: E1885 − 04, 2011.


        Examples
        --------

        >>> from pycafee.sensoryanalysis.discriminative_tests import TriangleTest
        >>> tringular = TriangleTest()
        >>> result, inputs = tringular.make_combinations(42, seed=42, shuffle=True, reorder=False)
        >>> print(result.head(6))
           Panelist Sample 1 Sample 2 Sample 3
        0         1    B-516    B-523    A-666
        1         2    A-903    B-866    B-759
        2         3    A-953    B-390    A-944
        3         4    B-698    A-380    A-762
        4         5    A-895    A-682    B-819
        5         6    B-791    A-719    B-796
        >>> print(inputs)
        {'n_of_assessors': 42, 'seed': 42, 'shuffle': True, 'reorder': False}


        >>> from pycafee.sensoryanalysis.discriminative_tests import TriangleTest
        >>> tringular = TriangleTest()
        >>> result, inputs = tringular.make_combinations(42, seed=42, shuffle=False, reorder=False)
        >>> print(result.head(6))
           Panelist Sample 1 Sample 2 Sample 3
        0         1    A-516    A-523    B-666
        1         2    A-903    B-866    A-759
        2         3    A-953    B-390    B-944
        3         4    B-698    B-380    A-762
        4         5    B-895    A-682    B-819
        5         6    B-791    A-719    A-796
        >>> print(inputs)
        {'n_of_assessors': 42, 'seed': 42, 'shuffle': False, 'reorder': False}


        >>> from pycafee.sensoryanalysis.discriminative_tests import TriangleTest
        >>> tringular = TriangleTest()
        >>> result, inputs = tringular.make_combinations(42, seed=42, shuffle=False, reorder=True)
        >>> print(result.head(6))
           Panelist Sample 1 Sample 2 Sample 3
        0         1    A-174    B-548    A-462
        1         2    A-245    B-457    A-672
        2         3    A-772    B-465    B-492
        3         4    A-474    B-657    B-839
        4         5    B-895    A-682    B-819
        5         6    B-283    B-257    A-945
        >>> print(inputs)
        {'n_of_assessors': 42, 'seed': 42, 'shuffle': False, 'reorder': True}


        """

        # ----- checking n_of_assessors value ----- #
        checkers._check_is_integer(n_of_assessors, "n_of_assessors", self.language)
        checkers._check_value_is_equal_or_higher_than(n_of_assessors, "n_of_assessors", 6, language=self.language)

        # ----- checking seed value ----- #
        if seed is None:
            seed = np.random.randint(1,100)
        else:
            checkers._check_is_integer(seed, "seed", self.language)
            checkers._check_value_is_equal_or_higher_than(seed, "seed", 0, language=self.language)

        # ----- checking shuffle value ----- #
        if shuffle is None:
            shuffle = True
        else:
            checkers._check_is_bool(shuffle, "shuffle", self.language)

        # ----- checking reorder value ----- #
        if reorder is None:
            reorder = False
        else:
            checkers._check_is_bool(reorder, "reorder", self.language)


        # ----- creating the three digit random numbers ----- #
        data = np.arange(100, 1000)

        # --- Checking if the amount of unique numbers is less than the amount that will be used --- #
        # --- If not, we will replicate all 900 numbers until the correct amount is reached --- #
        while len(data) < n_of_assessors*3:
            data = np.repeat(data, 2)

        # ----- getting random sequence ----- #
        rng = np.random.default_rng(seed)
        random_sequence = rng.choice(data, n_of_assessors*3, replace=False)

        # ----- splitting the random numbers into 3 columns ----- #
        random_sequence = np.array_split(random_sequence, 3)

        # ----- all permutations ----- #
        combinations = ["AAB", "ABA", "ABB", "BBA", "BAB", "BAA"]


        # ----- if shuffle is True, we need to shuffle the list ----- #
        if shuffle:
            combinations = list(rng.choice(combinations, len(combinations), replace=False))

        # ------ Now we need to repeat the combinations to get one combination to each panelist ----- #
        all_combinations = _repeat_items(combinations, n_of_assessors)

        # ----- quering ----- #
        fk_id_function = management._query_func_id("discriminative_tests")
        messages = management._get_messages(fk_id_function, self.language, "discriminative_tests")
        panelist = messages[3][0][0]
        sample = messages[3][1][0]

        # ----- making the DataFrame ----- #
        df = pd.DataFrame(columns=[panelist, f"{sample} 1", f"{sample} 2", f"{sample} 3"])
        df[panelist] = range(1, n_of_assessors+1)
        first = []
        second = []
        third = []

        for i in range(n_of_assessors):
            first.append(f"{all_combinations[i][0]}-{random_sequence[0][i]}")
            second.append(f"{all_combinations[i][1]}-{random_sequence[1][i]}")
            third.append(f"{all_combinations[i][2]}-{random_sequence[2][i]}")

        df[f"{sample} 1"] = first
        df[f"{sample} 2"] = second
        df[f"{sample} 3"] = third

        # reording the df
        if reorder:
            df = df.sample(frac=1, random_state=seed).reset_index(drop=True)
            df[panelist] = range(1, n_of_assessors+1)

        inputs = {
            "n_of_assessors": n_of_assessors,
            "seed": seed,
            "shuffle": shuffle,
            "reorder": reorder,
        }

        self.df_table = df

        return df, inputs


















#














# with tests, with docstring
def _min_responses(n_assessors, alfa):
    """This functions calculates the minimum number of correct responses based on the number of assessors and alfa value [1]_.

    Parameters
    ----------
    n_assessors : ``int``
        The number of assessors.
    alfa : ``float``
        The significance level.


    Returns
    -------
    min_correct: ``int``
        The minimum number of correct answers


    Notes
    -----
    The minimum number of correct answers is estimated using the following relationship:

    .. math::
            min = \\frac{n_{assessors + t_{\\infty} \\sqrt{2n_{assessors}}}}{3}

    where :math:`t_{\\infty}` is the value of the one-sided student t distribution for infinite degrees of freedom (1000000) rounded to 2 decimal places. The value of t is obtained using ``stats.t.ppf(1-alfa, 1000000)``


    References
    ----------
    .. [1] Standard Test Method for Sensory Analysis—Triangle Test, Designation: E1885 − 04, 2011.


    Examples
    --------

    >>> from pycafee.sensoryanalysis.discriminative_tests import _min_responses
    >>> result = _min_responses(48, 0.05)
    >>> print(result)
    22

    """
    # t values
    t = round(stats.t.ppf(1-alfa, 1000000),2)
    # calculating the minimum
    min = (n_assessors/3) + t*np.sqrt(2*n_assessors)/3
    # rounding to nearest whole number greater than min
    min_correct = int(min + 0.5) + 1
    return min_correct



# with some tests
def _repeat_items(lista, elemts):
    """This function returns a repetition of ``elemts`` elements of a list ``list``.

    Parameters
    ----------
    lista: ``list``
        The list that will be repeated
    elemts: ``int``
        The number of list elements with repeated items

    Returns
    -------
    lista: ``list``
        A list of repeated elements


    Examples
    --------

    >>> repeat_items([1,2], 3)
    [1, 2, 1]

    >>> repeat_items([1,2], 6)
    [1, 2, 1, 2, 1, 2]

    >>> repeat_items(["A", "B", "C", "D"], 12)
    ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D']

    >>> repeat_items(["A", "B", "C", "D"], 2)
    ['A', 'B']

    """
    return lista * (elemts // len(lista)) + lista[:(elemts % len(lista))]










#
