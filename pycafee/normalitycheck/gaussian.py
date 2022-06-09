"""
desc
"""

##########################################
################ Summmary ################
##########################################



#########################################
################ Imports ################
#########################################

###### Standard ######
from collections import namedtuple


###### Third part ######
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


###### Home made ######
from pycafee.database_management import management
from pycafee.functions import functions
from pycafee.utils.helpers import PlotsManagement, AlphaManagement, NDigitsManagement
from pycafee.utils import checkers
from pycafee.utils import general
from pycafee.utils import helpers
###########################################
################ Functions ################
###########################################


class Gaussian(PlotsManagement, AlphaManagement, NDigitsManagement):

    def __init__(self, language=None, alfa=None, n_digits=None, **kwargs):
        super().__init__(language=language, alfa=alfa, n_digits=n_digits,**kwargs)


    def kurtosis(self, x_exp, alfa=None, details=None):
        """This function applies the kurtosis test on a sample dataset using the method described by [1]_.


        Parameters
        ----------
        x_exp : ``numpy array``
            One dimension :doc:`numpy array <numpy:reference/generated/numpy.array>` with at least 4 sample data.
        alfa : ``float``, optional
            The level of significance (``ɑ``). Default is ``None`` which results in ``0.05`` (``ɑ = 5%``).
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
            critical : ``list`` of two ``floats``
                The critical values for the adopted significance level, where:

                * ``critical[0]`` is the lower critical value (always negative);
                * ``critical[1]`` is the upper critical value (always positive);

            which : ``str``
                The kind of comparison that was performed.
            alpha : ``float``
                The adopted level of significance.
        conclusion : ``str`` or ``int``
            The test conclusion (e.g, Normal/ not Normal).


        See Also
        --------
        pycafee.normalitycheck.shapirowilk.ShapiroWilk.fit


        Notes
        -----
        Kurtosis (:math:`K`) is estimated using the following equation:

        .. math::

            K=\\frac{n\\left(n+1\\right)}{(n-1)(n-2)(n-3)}\\sum_{i=1}^n\\left(\\frac{x_i - \\overline{x}}{s}\\right)^{4}-\\frac{3(n-1)^2}{(n-2)(n-3)}

        The standard deviation of kurtosis (:math:`K_{std}`) is estimated using the following equation:

        .. math::

            K_{std}=\\sqrt{\\frac{24n(n-1)^2}{(n-2)(n-3)(n+5)(n+3)}}

        and the test statistic (:math:`z_{K}`) is estimated through the following equation:

        .. math::

            z_{K} = \\frac{K-0}{K_{std}}


        The test hypotheses are as follows:

        .. admonition:: \u2615

           :math:`H_0:` the kurtosis is Normal

           :math:`H_1:` the kurtosis is Not Normal

        The comparison is performed between the calculated test ``statistic`` and the ``critical`` values (at alpha significance level) as follows:


        .. code:: python

           if critical.Lower <= statistic <= critical.Upper:
               the kurtosis is Normal
           else:
               the kurtosis is Not Normal

        The lower critical value is obtained with ``alfa/2`` and the upper critical value is obtained with ``1 - alfa/2`` significance level (e.g., two side distribution), using `stats.norm.ppf()` [2]_.


        References
        ----------

        .. [1] CORDER, G. W.; FOREMAN, D. I. NONPARAMETRIC STATISTICS A Step-by-Step Approach. 2. ed. New Jersey: John Wiley & Sons, 2014, p. 19, eq 2.5.

        .. [2] SCIPY. stats.norm.ppf. Available at: `https://docs.scipy.org <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html>`_. Access on: 10 May. 2022.


        Examples
        --------

        >>> from pycafee.normalitycheck.gaussian import Gaussian
        >>> import numpy as np
        >>> x_exp = np.array([1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8, 9])
        >>> test = Gaussian()
        >>> result, conclusion = test.kurtosis(x_exp, details='full')
        >>> print(result)
        KurtosisResult(Statistics=2.802450152883085, Critical=[-1.9599639845400545, 1.959963984540054], Alpha=0.05)
        >>> print(conclusion)
        Since the calculated statistic for the kurtosis (2.802) is a value higher than the upper critical value (1.959), we have evidence to reject the null hypothesis, and we can say that the distribution does not have kurtosis similar to the kurtosis of a Normal distribution (with 95.0% confidence).


        >>> from pycafee.normalitycheck.gaussian import Gaussian
        >>> import numpy as np
        >>> x_exp = np.array([90, 72, 90, 64, 95, 89, 74, 88, 100, 77, 57, 35, 100, 64, 95, 65, 80, 84, 90, 100, 76])
        >>> test = Gaussian(language='pt-br')
        >>> result, conclusion = test.kurtosis(x_exp)
        >>> print(result)
        ResultadoCurtose(Estatistica=1.186374537979677, Critico=[-1.9599639845400545, 1.959963984540054], Alfa=0.05)
        >>> print(conclusion)
        A Curtose é Normal (95.0% de confiança)


        """
        ### checking input data ###
        checkers._check_is_numpy_1_D(x_exp, "x_exp", self.language)
        self.x_exp = x_exp
        ### cheking sample size
        checkers._check_array_lower_size(x_exp, 4, "x_exp", self.language)

        ### getting the default alpha value ###
        if alfa is None:
            alfa = self.alfa
        else:
            checkers._check_is_float(alfa, "alfa", self.language)
            checkers._check_data_in_range(alfa, "alfa", 0.0, 1.0, self.language)
            self.alfa = alfa

        ### checking the comparison parameter ### # removed due to p-value issues
        # if comparison is None:
        #     comparison = "critical"
        # else:
        #     checkers._check_is_str(comparison, "comparison", self.language)
        #     if comparison == "critical":
        #         comparison = "critical"
        #     elif comparison == "p-value":
        #         comparison = "p-value"
        #     else:
        #         fk_id_function = management._query_func_id("normalitycheck_fit")
        #         messages = management._get_messages(fk_id_function, self.language, "normalitycheck_fit")
        #         try:
        #             error = messages[1][0][0]
        #             raise ValueError(error)
        #         except ValueError:
        #             general._display_one_line_attention(f"{messages[15][0][0]} '{comparison}'",)
        #             raise


        ### checking the details parameter ###
        if details == None:
            details = "short"
        else:
            checkers._check_is_str(details, "details", self.language)
            if details == "short":
                details = "short"
            elif details == "full":
                details = "full"
            elif details == "binary":
                details = "binary"
            else:
                fk_id_function = management._query_func_id("normalitycheck_fit")
                messages = management._get_messages(fk_id_function, self.language, "normalitycheck_fit")
                try:
                    error = messages[3][0][0]
                    raise ValueError(error)
                except ValueError:
                    general._display_one_line_attention(f"{messages[2][0][0]} '{details}'")
                    raise


        ### kurtosis
        n = x_exp.size
        kurtosis = (n*(n+1)/((n-1)*(n-2)*(n-3)))*_kurtosis_summation(x_exp, self.language) - (3*(n-1)**2)/((n-2)*(n-3))
        kurtosis_std = np.sqrt((24*n*(n-1)**2)/((n-2)*(n-3)*(n+5)*(n+3)))
        kurtosis_z = kurtosis/kurtosis_std
        ### getting critical values
        z_lower = stats.norm.ppf(alfa/2)
        z_upper = stats.norm.ppf(1 - alfa/2)

        ### getting p-value # there is somethng wrong here. Hence, it was removed
        # kurtosis_p_value = stats.norm.cdf(kurtosis_z)
        # kurtosis_p_value = kurtosis_p_value*2 # corrigindo o p para two tails

        fk_id_function = management._query_func_id("gaussian")
        messages = management._get_messages(fk_id_function, self.language, "gaussian")

        aceita = 0
        rejeita = 1

        # if comparison == 'critical':
        if z_lower <= kurtosis_z <= z_upper:
            if details == 'short':
                conclusion = f"{messages[3][0][0]}{100*(1-alfa)}{messages[3][2][0]}"
            elif details == "full":
                conclusion = f"{messages[5][0][0]}{helpers._truncate(kurtosis_z, self.language, decs=self.n_digits)}{messages[5][2][0]}{helpers._truncate(z_lower, self.language, decs=self.n_digits)}{messages[5][4][0]}{helpers._truncate(z_upper, self.language, decs=self.n_digits)}{messages[5][6][0]} {100*(1-alfa)}{messages[5][8][0]}"
            else:
                # aceita
                conclusion = aceita
        else:
            if details == 'short':
                conclusion = f"{messages[4][0][0]}{100*(1-alfa)}{messages[4][2][0]}"
            elif details == "full":
                if kurtosis_z > z_upper:
                    conclusion = f"{messages[6][0][0]}{helpers._truncate(kurtosis_z, self.language, decs=self.n_digits)}{messages[6][2][0]}{helpers._truncate(z_upper, self.language, decs=self.n_digits)}{messages[6][4][0]} {100*(1-alfa)}{messages[6][6][0]}"
                else:
                    conclusion = f"{messages[7][0][0]}{helpers._truncate(kurtosis_z, self.language, decs=self.n_digits)}{messages[7][2][0]}{helpers._truncate(z_upper, self.language, decs=self.n_digits)}{messages[7][4][0]} {100*(1-alfa)}{messages[7][6][0]}"
            else:
                # rejeita
                conclusion = rejeita
        # else:
        #     if kurtosis_p_value < alfa:
        #         if details == 'short':
        #             conclusion = f"{messages[4][0][0]}{100*(1-alfa)}{messages[4][2][0]}"
        #         elif details == "full":
        #                 conclusion = f"{messages[8][0][0]}{helpers._truncate(kurtosis_p_value, self.language, decs=self.n_digits)}{messages[8][2][0]}{alfa}{messages[8][4][0]} {100*(1-alfa)}{messages[8][6][0]}"
        #         else:
        #             # rejeita
        #             conclusion = rejeita
        #     else:
        #         if details == "short":
        #             conclusion = f"{messages[3][0][0]}{100*(1-alfa)}{messages[3][2][0]}"
        #         elif details == "full":
        #                 conclusion = f"{messages[9][0][0]}{helpers._truncate(kurtosis_p_value, self.language, decs=self.n_digits)}{messages[9][2][0]}{alfa}{messages[9][4][0]} {100*(1-alfa)}{messages[9][6][0]}"
        #         else:
        #             # aceita
        #             conclusion = aceita

        ### making namedtuple

        result = namedtuple(messages[8][0][0], (messages[8][1][0], messages[8][2][0], messages[8][3][0]))
        return result(kurtosis_z, [z_lower, z_upper], alfa), conclusion





    def skewness(self):
        """
        Esta função aplica o teste de skewness em um conjunto de dados
        """
        pass


    def draw(self):
        """
        Esta função plota a distribuição Normal baseada nos dados
        """
        pass


    def __str__(self):
        pass
        # fk_id_function = management._query_func_id("StudentDistribution")
        # messages = management._get_messages(fk_id_function, self.language)
        # return messages[12][0][0]

    def __repr__(self):
        pass
        # fk_id_function = management._query_func_id("StudentDistribution")
        # messages = management._get_messages(fk_id_function, self.language)
        # return messages[12][0][0]






















def _kurtosis_summation(x, language):
    """This function calculates the summation term for estimating the kurtosis of a dataset [1]_:

    .. math::

        \\sum_{i=1}^n\\left(\\frac{x_i - \\overline{x}}{s}\\right)^{4}


    Parameters
    ----------
    x : ``numpy array``
        One dimension :doc:`numpy array <numpy:reference/generated/numpy.array>`.

    Returns
    -------
    result : ``numpy.float64``
        The result of the sum.

    Notes
    -----
    The standard deviation is estimated as sample data.

    References
    ----------

    .. [1] CORDER, G. W.; FOREMAN, D. I. NONPARAMETRIC STATISTICS A Step-by-Step Approach. 2. ed. New Jersey: John Wiley & Sons, 2014, p. 19, eq 2.5.



    """
    mean = np.mean(x)
    std = np.std(x, ddof=1)
    if std < 1.0E-6:
        ### quering ###
        func_name = "gaussian"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        try:
            error = messages[1][0][0]
            raise RuntimeError(error)
        except RuntimeError:
            general._display_one_line_attention(
                f"{messages[2][0][0]}{std}{messages[2][2][0]}"
            )
            raise
    result = np.sum(((x-mean)/std)**4)
    return result














###
