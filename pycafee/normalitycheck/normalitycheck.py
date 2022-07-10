"""This module performs a normality check based on a user choice

"""

##########################################
################ Summmary ################
##########################################

# - NormalityCheck(AlphaManagement, NDigitsManagement)
#     - __init__(self, alfa=None, language=None, n_digits=None, **kwargs)
#     - fit(self, x_exp, test=None, alfa=None, n_digits=None, comparison=None, details=None)
#     - __str__(self)
#     - __repr__(self)

#########################################
################ Imports ################
#########################################

###### Standard ######

###### Third part ######

###### Home made ######
from pycafee.database_management import management

from pycafee.normalitycheck.abdimolin import AbdiMolin
from pycafee.normalitycheck.andersondarling import AndersonDarling
from pycafee.normalitycheck.kolmogorovsmirnov import KolmogorovSmirnov
from pycafee.normalitycheck.lilliefors import Lilliefors
from pycafee.normalitycheck.shapirowilk import ShapiroWilk

from pycafee.utils import checkers
from pycafee.utils import general
from pycafee.utils.helpers import AlphaManagement
from pycafee.utils.helpers import NDigitsManagement

###########################################
################ Functions ################
###########################################



class NormalityCheck(AlphaManagement, NDigitsManagement):
    """This class instantiates an object to apply a Normality test on a dataset

    Attributes
    ----------
    critical : ``float``
        The critical value for the test at ``ɑ`` significance level
    msg : ``str``
        A message describing the test
    normality_test : ``str``
        The chosen test
    p_value : ``float``
        The p-value for the hypothesis test.
    statistic : ``float``
        The estimated statistic of the normality test
    x_exp : :doc:`numpy array <numpy:reference/generated/numpy.array>`
        The data provided


    """


    def __init__(self, alfa=None, language=None, n_digits=None, **kwargs):
        super().__init__(alfa=alfa, language=language, n_digits=n_digits, **kwargs)
        self.msg = None
        self.statistic = None
        self.critical = None
        self.p_value = None
        self.x_exp = None
        self.normality_test = None


    def fit(self, x_exp, test=None, alfa=None, n_digits=None, comparison=None, details=None):
        """This function aggregates all available Normality tests.

        Parameters
        ----------
        x_exp : ``numpy array``
            One dimension :doc:`numpy array <numpy:reference/generated/numpy.array>` with at least ``3`` sample data, except for the Lilliefors and Abdi-Molin tests, which must have at least ``4`` samples.
        test : ``str``, optional
            The test that will be applied:

            * If ``"shapiro-wilk"``, ``"sw"`` or ``None``, the function will apply the :ref:`Shapiro Wilk normality <shapiro_wilk>` test;
            * If ``"abdi-molin"`` or ``"am"``, the function will apply the :ref:`Abdi Molin normality <abdi_molin>` test;
            * If ``"anderson-darling"`` or ``"ad"``, the function will apply the :ref:`Anderson Darling normality <anderson_darling>` test;
            * If ``"kolmogorov-smirnov"`` or ``"ks"``, the function will apply the :ref:`Kolmogorov Smirnov normality <kolmogorov_smirnov>` test;
            * If ``"lilliefors"`` or ``"li"``, the function will apply the :ref:`Lilliefors normality <lilliefors>` test;

        alfa : ``float``, optional
            The level of significance (``ɑ``). Default is ``None`` which results in ``0.05`` (``ɑ = 5%``).
        comparison : ``str``, optional
            This parameter determines how to perform the comparison test to perform the Normality test.

            * If ``comparison = "critical"`` (or ``None``, e.g, the default), the comparison test is made between the critical value (with ``ɑ`` significance level) and the calculated value of the test statistic.
            * If ``"p-value"``, the comparison test is performed between the p-value and the adopted significance level (``ɑ``). This parameter does not influence the result if ``test = "abdi-molin"``.

            **Both results should lead to the same conclusion.**

        details : ``str``, optional
            The ``details`` parameter determines the amount of information presented about the hypothesis test.

            * If ``details = "short"`` (or ``None``, e.g, the default), a simplified version of the test result is returned.
            * If ``details = "full"``, a detailed version of the hypothesis test result is returned.
            * if ``details = "binary"``, the conclusion will be ``1`` (:math:`H_0` is rejected) or ``0`` (:math:`H_0` is accepted).


        Returns
        -------
        result : ``tuple`` with
            statistic : ``float``
                The test statistic.
            critical : ``float`` or ``None``
                Each test has a different set of critical values, but all contain critical values for alpha equal to ``1%``, ``5%`` or ``10%``. For more details, see the specific details for each test in its respective documentation.
            p_value : ``float`` or ``None``
                The p-value for the hypothesis test.
        conclusion : ``str`` or ``int``
            The test conclusion (e.g, Normal/ not Normal).

        See Also
        --------
        pycafee.normalitycheck.abdimolin.AbdiMolin.fit
        pycafee.normalitycheck.andersondarling.AndersonDarling.fit
        pycafee.normalitycheck.lilliefors.Lilliefors.fit
        pycafee.normalitycheck.kolmogorovsmirnov.KolmogorovSmirnov.fit
        pycafee.normalitycheck.shapirowilk.ShapiroWilk.fit


        Examples
        --------

        **Checking data normality with default values**

        >>> from pycafee.normalitycheck import NormalityCheck
        >>> import numpy as np
        >>> x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        >>> normality_test = NormalityCheck()
        >>> result, conclusion = normality_test.fit(x)
        >>> print(result)
        ShapiroWilkResult(Statistic=0.9698116779327393, Critical=0.842, p_value=0.8890941739082336, Alpha=0.05)
        >>> print(conclusion)
        Data is Normal at a 95.0% of confidence level.

        |

        **Checking data normality using the** ``Shapiro Wilk`` **test at** ``ɑ = 10%`` **in portuguese** (``"pt-br"``)

        >>> from pycafee.normalitycheck import NormalityCheck
        >>> import numpy as np
        >>> x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        >>> normality_test = NormalityCheck(language="pt-br")
        >>> result, conclusion = normality_test.fit(x, test="sw", alfa=0.1)
        >>> print(result)
        ShapiroWilkResultado(Estatistica=0.9698116779327393, Critico=0.869, p_valor=0.8890941739082336, Alfa=0.1)
        >>> print(conclusion)
        Os dados são Normais com 90.0% de confiança.


        |

        **Checking data normality using the** ``Lilliefors`` **test with** ``details = "full"``

        >>> from pycafee.normalitycheck import NormalityCheck
        >>> import numpy as np
        >>> x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        >>> normality_test = NormalityCheck()
        >>> result, conclusion = normality_test.fit(x, test="li", details="full")
        >>> print(result)
        LillieforsResult(Statistic=0.15459867079959644, Critical=0.258, p_value=0.7104644322958894, Alpha=0.05)
        >>> print(conclusion)
        Since the critical value (0.258) >= statistic (0.154), we have NO evidence to reject the hypothesis of data normality, according to the Lilliefors test at a 95.0% of confidence level.

        |

        **Checking data normality using the** ``Anderson Darling`` **test with** ``conclusion = "p-value"``

        >>> from pycafee.normalitycheck import NormalityCheck
        >>> import numpy as np
        >>> x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        >>> normality_test = NormalityCheck()
        >>> result, conclusion = normality_test.fit(x, test="ad", details="full", comparison="p-value")
        >>> print(result)
        AndersonDarlingResult(Statistic=0.22687861079050364, Critical=None, p_value=0.7479231606974011, Alpha=0.05)
        >>> print(conclusion)
        Since p-value (0.747) >= alpha (0.05), we have NO evidence to reject the hypothesis of data normality, according to the AndersonDarling test at a 95.0% of confidence level.


        |

        **Checking data normality using the** ``Kolmogorov Smirnov`` **test at** ``ɑ = 1%``

        >>> from pycafee.normalitycheck import NormalityCheck
        >>> import numpy as np
        >>> x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        >>> normality_test = NormalityCheck()
        >>> result, conclusion = normality_test.fit(x, test="ks", details="full", comparison="p-value")
        >>> print(result)
        KolmogorovSmirnovResult(Statistic=0.15459867079959644, Critical=0.41, p_value=0.9706128123504146, Alpha=0.05)
        >>> print(conclusion)
        Since p-value (0.97) >= alpha (0.05), we have NO evidence to reject the hypothesis of data normality, according to the Kolmogorov Smirnov test at a 95.0% of confidence level.


        |

        **Checking data normality using the** ``Abdi Molin`` **test with default values**

        >>> from pycafee.normalitycheck import NormalityCheck
        >>> import numpy as np
        >>> x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        >>> normality_test = NormalityCheck()
        >>> result, conclusion = normality_test.fit(x, test="am")
        >>> print(result)
        AbdiMolinResult(Statistic=0.15459867079959644, Critical=0.2616, p_value=None, Alpha=0.05)
        >>> print(conclusion)
        Data is Normal at a 95.0% of confidence level.



        """
        normality_tests = [
                "am", "abdi-molin",
                "ad", "anderson-darling",
                "ks", "kolmogorov-smirnov",
                "li", "lilliefors",
                "sw", "shapiro-wilk"
                ]
        fk_id_function = management._query_func_id("NormalityCheck")
        messages = management._get_messages(fk_id_function, self.language, "NormalityCheck")
        if test is not None:
            checkers._check_is_str(test, "test", self.language)
            if test not in normality_tests:
                try:
                    error = messages[3][0][0]
                    raise ValueError(error)
                except ValueError:
                    test_names = []
                    for item in normality_tests:
                        test_names.append(f"    --->   {item}")
                    msg = [
                        f"{messages[4][0][0]} 'test' {messages[4][2][0]} '{test}'",
                        f"{messages[4][4][0]}:",
                        test_names
                        ]
                    msg = general._flatten_list_of_list_string(msg)
                    msg = list(msg)
                    general._display_n_line_attention(msg)
                    raise
        if (test is None or test == "sw" or test == "shapiro-wilk"):
            normality_test = ShapiroWilk(language=self.language, n_digits=self.n_digits)
            result, conclusion = normality_test.fit(
                        x_exp=x_exp, alfa=alfa, comparison=comparison, details=details
                    )
            self.normality_test = "Shapiro-Wilk"

        elif (test == "am" or test == "abdi-molin"):
            normality_test = AbdiMolin(language=self.language, n_digits=self.n_digits)
            if comparison is not None:
                general._display_n_line_warn(
                    [
                    messages[5][0][0],
                    messages[6][0][0],
                    messages[7][0][0]
                    ])

            result, conclusion = normality_test.fit(
                        x_exp=x_exp, alfa=alfa, details=details
                    )
            self.normality_test = "Abdi-Molin"

        elif (test == "ad" or test == "anderson-darling"):
            normality_test = AndersonDarling(language=self.language, n_digits=self.n_digits)
            result, conclusion = normality_test.fit(
                        x_exp=x_exp, alfa=alfa, comparison=comparison, details=details
                    )
            self.normality_test = "Anderson-Darling"

        elif (test == "ks" or test == "kolmogorov-smirnov"):
            normality_test = KolmogorovSmirnov(language=self.language, n_digits=self.n_digits)
            result, conclusion = normality_test.fit(
                        x_exp=x_exp, alfa=alfa, comparison=comparison, details=details
                    )
            self.normality_test = "Kolmogorov-Smirnov"

        else:
            normality_test = Lilliefors(language=self.language, n_digits=self.n_digits)
            result, conclusion = normality_test.fit(
                        x_exp=x_exp, alfa=alfa, comparison=comparison, details=details
                    )
            self.normality_test = "Lilliefors"

        self.statistic = result[0]
        self.critical = result[1]
        self.p_value = result[2]
        self.x_exp = x_exp
        self.msg = conclusion

        return result, conclusion




    def __str__(self):
        if self.msg is None:
            fk_id_function = management._query_func_id("NormalityCheck")
            messages = management._get_messages(fk_id_function, self.language, "NormalityCheck")
            return messages[1][0][0]
        else:
            return self.msg

    def __repr__(self):
        fk_id_function = management._query_func_id("NormalityCheck")
        messages = management._get_messages(fk_id_function, self.language, "NormalityCheck")
        return messages[2][0][0]





































#
