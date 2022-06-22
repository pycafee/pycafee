"""This module focous on Outlier detection for univariate data
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
from pycafee.functions import functions




from pycafee.database_management import management

###########################################
################ Functions ################
###########################################


class ZScore(LanguageManagement):
    """This class instantiates an object to apply the Z test for detecting oultliers

    """
    def __init__(self, language=None, **kwargs):
        super().__init__(language=language, **kwargs)
        self.conclusion = None
        self.statistic = None
        self.critical = None
        self.x_exp = None



    def fit(self, x_exp, which=None, critical=None, details=None):
        """This function applies the Z-score test for outlier detection

        Parameters
        ----------
        x_exp : ``numpy array``
            One dimension :doc:`numpy array <numpy:reference/generated/numpy.array>` with at least 3 sample data.
        details : ``str``, optional
            The ``details`` parameter determines the amount of information presented about the hypothesis test.

            * If ``details = "short"`` (or ``None``, e.g, the default), a simplified version of the test result is returned.
            * if ``details = "binary"``, the conclusion will be ``1`` (data has outlier) or ``0`` (data has no outlier).

        which : ``str``, optional
            The value that should be evaluated as a possible outlier.

            * If it is ``None`` (default), the outlier is automatically inferred as the farthest observation from the mean
            * If it is ``"max"``, the highest value is checked if it is a possible outlier.
            * If it is ``"min"``, the lowest value is checked if it is a possible outlier.


        critical : ``int`` or ``float``, optional
            The critical value of the test (default is ``3``).

        Returns
        -------
        result : ``tuple`` with
            statistic : ``float``
                The test statistic.
            critical : ``float``
                The critical value.
            outlier : ``float`` or ``int``
                The value checked as a possible outlier

        conclusion : ``str`` or ``int``
            The test conclusion (e.g, Possible outlier/ no outliers).


        See Also
        --------



        Notes
        -----

        The **ZScore test for outlier detection** compares a possible outlier with the critical value for the standard Normal distribution. The test statistic is calculated using the following equation:

        .. math::

                Z_i = \\frac{|x_i - \\overline{x}|}{s}

        where :math:`x_i` is the possible outlier, :math:`\\overline{x}` is the sample mean and :math:`s` is the sample standard deviation.

        By default, the critical value is ``3`` [1]_, which corresponds to 99.8% of confidencial level. The conclusion of the test is based on the comparison between the ``critical`` value and the ``statistic`` of the test:

        .. code:: python

           if critical <= statistic:
               Data does not have a outlier
           else:
               Data has a outlier



        References
        ----------
        .. [1] OSBORNE, J. W.; OVERBAY, A. The power of outliers (and why researchers should ALWAYS check for them). Practical Assessment, Research, and Evaluation, v. 9, n. 6, p. 1–8, 2004.



        Examples
        --------

        >>> from pycafee.sample.outliers import ZScore
        >>> import numpy as np
        >>> x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        >>> test = ZScore()
        >>> result, conclusion = test.fit(x)
        >>> print(result)
        ZScoreResult(Statistic=1.8533964859229188, critical=3, outlier=5.4)
        >>> print(conclusion)
        The dataset has no outliers


        """

        ### checking input data ###
        checkers._check_is_numpy_1_D(x_exp, "x_exp", self.language)
        self.x_exp = x_exp

        checkers._check_value_is_equal_or_higher_than(x_exp.size, "size", 3, language=self.language)


        ### checking the which parameter ###
        if which is None:
            which = _check_outermost_observation(x_exp)
        else:
            checkers._check_is_str(which, "which", language=self.language)
            if which not in ["min", "max"]:
                fk_id_function = management._query_func_id("outliers")
                messages = management._get_messages(fk_id_function, self.language, "outliers")
                try:
                    error = messages[1][0][0]
                    raise ValueError(error)
                except ValueError:
                    general._display_one_line_attention(f"{messages[1][1][0]} '{which}'")
                    raise


        ### Cheking the critical parameter
        if critical is None:
            critical = 3
        else:
            checkers._check_is_float_or_int(critical, "critical", self.language)
            checkers._check_is_positive(critical, "critical", self.language)

        ### checking the details parameter ###
        if details == None:
            details = "short"
        else:
            checkers._check_is_str(details, "details", self.language)
            if details == "short":
                details = "short"
            elif details == "binary":
                details = "binary"
            else:
                fk_id_function = management._query_func_id("generic")
                messages = management._get_messages(fk_id_function, self.language, "generic")
                try:
                    error = messages[3][0][0]
                    raise ValueError(error)
                except ValueError:
                    general._display_one_line_attention(f"{messages[4][0][0]} 'details' {messages[4][2][0]}: 'short' or 'binary', {messages[4][4][0]} '{details}'.")
                    raise


        ## Basic stats
        mean = np.mean(x_exp)
        std = np.std(x_exp, ddof=1)
        if std <= 10e-7:
            try:
                fk_id_function = management._query_func_id("generic")
                messages = management._get_messages(fk_id_function, self.language, "generic")
                error = messages[5][0][0]
                raise ZeroDivisionError(error)
            except ZeroDivisionError:
                general._display_one_line_attention(messages[6][0][0])
                raise

        ## Z-score
        if which == "min":
            outlier = np.min(x_exp)
        else:
            outlier = np.max(x_exp)
        statistic = np.abs((mean - outlier))/std


        aceita = 0
        rejeita = 1

        # concluindo o teste
        if statistic <= critical:
            if details == "short":
                fk_id_function = management._query_func_id("outliers")
                messages = management._get_messages(fk_id_function, self.language, "outliers")
                conclusion = messages[2][0][0]
            else:
                conclusion = aceita
        else:
            if details == "short":
                fk_id_function = management._query_func_id("outliers")
                messages = management._get_messages(fk_id_function, self.language, "outliers")
                conclusion = messages[3][0][0]
            else:
                conclusion = rejeita


        ### quering
        fk_id_function = management._query_func_id("generic")
        messages = management._get_messages(fk_id_function, self.language, "generic")
        self.conclusion = conclusion
        self.statistic = statistic
        self.critical = critical
        self.x_exp = x_exp
        ### making the named tuple
        name = "ZScore" + messages[1][0][0]
        result = namedtuple(name, (messages[1][3][0], messages[1][1][0], "outlier"))
        return result(statistic, critical, outlier), conclusion







    def __str__(self):
        if self.conclusion is None:
            fk_id_function = management._query_func_id("generic")
            messages = management._get_messages(fk_id_function, self.language, "generic")
            return f"{messages[2][0][0]} ZScore {messages[2][2][0]}"
        else:
            return self.conclusion


    def __repr__(self):
        fk_id_function = management._query_func_id("outliers")
        messages = management._get_messages(fk_id_function, self.language, "outliers")
        return messages[4][0][0]


class ModifiedZScore(LanguageManagement):
    """This class instantiates an object to apply the modified Z test for detecting oultliers

    """
    def __init__(self, language=None, **kwargs):
        super().__init__(language=language, **kwargs)
        self.conclusion = None
        self.statistic = None
        self.critical = None
        self.x_exp = None



    def fit(self, x_exp, which=None, critical=None, details=None):
        """This function applies the Modified Z-score test for outlier detection [1]_.

        Parameters
        ----------
        x_exp : ``numpy array``
            One dimension :doc:`numpy array <numpy:reference/generated/numpy.array>` with at least 3 sample data.
        details : ``str``, optional
            The ``details`` parameter determines the amount of information presented about the hypothesis test.

            * If ``details = "short"`` (or ``None``, e.g, the default), a simplified version of the test result is returned.
            * if ``details = "binary"``, the conclusion will be ``1`` (data has outlier) or ``0`` (data has no outlier).

        which : ``str``, optional
            The value that should be evaluated as a possible outlier.

            * If it is ``None`` (default), the outlier is automatically inferred as the farthest observation from the mean
            * If it is ``"max"``, the highest value is checked if it is a possible outlier.
            * If it is ``"min"``, the lowest value is checked if it is a possible outlier.


        critical : ``int`` or ``float``, optional
            The critical value of the test (default is ``3.5``).

        Returns
        -------
        result : ``tuple`` with
            statistic : ``float``
                The test statistic.
            critical : ``float``
                The critical value.
            outlier : ``float`` or ``int``
                The value checked as a possible outlier

        conclusion : ``str`` or ``int``
            The test conclusion (e.g, Possible outlier/ no outliers).


        See Also
        --------
        pycafee.sample.outliers.ZScore.fit


        Notes
        -----

        The **ModifiedZScore test for outlier detection** compares a possible outlier with a pre estabelish critical value. The test statistic is calculated using the following equation:

        .. math::

                M_i = \\frac{0.6745(|x_i-\\widetilde{x}|)}{MAD}

        where :math:`x_i` is the possible outlier, :math:`\\widetilde{x}` is the sample median and :math:`MAD` is the median of the absolute deviations about the medianm which is obtained with the following equation

        .. math::

                MAD =median_i\left\{|x_i-\widetilde{x}|\right\}

        By default, the critical value is ``3.5`` [1]_. The conclusion of the test is based on the comparison between the ``critical`` value and the ``statistic`` of the test:

        .. code:: python

           if critical <= statistic:
               Data does not have a outlier
           else:
               Data has a outlier



        References
        ----------
        .. [1] IGLEWICZ, B.; HOAGLIN, D. C. The ASQC Basic References in Quality Control: Statistical Techniques Volume 16: How to Detect and Handle Outliers. Milwaukee: BookCrafters, Inc, 1993.



        Examples
        --------

        >>> from pycafee.sample.outliers import ModifiedZScore
        >>> import numpy as np
        >>> x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        >>> test = ModifiedZScore()
        >>> result, conclusion = test.fit(x)
        >>> print(result)
        ModifiedZScoreResult(Statistic=1.6862500000000022, critical=3.5, outlier=5.4)
        >>> print(conclusion)
        The dataset has no outliers

        """

        ### checking input data ###
        checkers._check_is_numpy_1_D(x_exp, "x_exp", self.language)
        self.x_exp = x_exp

        checkers._check_value_is_equal_or_higher_than(x_exp.size, "size", 3, language=self.language)


        ### checking the which parameter ###
        if which is None:
            which = _check_outermost_observation(x_exp)
        else:
            checkers._check_is_str(which, "which", language=self.language)
            if which not in ["min", "max"]:
                fk_id_function = management._query_func_id("outliers")
                messages = management._get_messages(fk_id_function, self.language, "outliers")
                try:
                    error = messages[1][0][0]
                    raise ValueError(error)
                except ValueError:
                    general._display_one_line_attention(f"{messages[1][1][0]} '{which}'")
                    raise


        ### Cheking the critical parameter
        if critical is None:
            critical = 3.5
        else:
            checkers._check_is_float_or_int(critical, "critical", self.language)
            checkers._check_is_positive(critical, "critical", self.language)

        ### checking the details parameter ###
        if details == None:
            details = "short"
        else:
            checkers._check_is_str(details, "details", self.language)
            if details == "short":
                details = "short"
            elif details == "binary":
                details = "binary"
            else:
                fk_id_function = management._query_func_id("generic")
                messages = management._get_messages(fk_id_function, self.language, "generic")
                try:
                    error = messages[3][0][0]
                    raise ValueError(error)
                except ValueError:
                    general._display_one_line_attention(f"{messages[4][0][0]} 'details' {messages[4][2][0]}: 'short' or 'binary', {messages[4][4][0]} '{details}'.")
                    raise


        ## Basic stats
        mediana = np.median(x_exp)
        mad_vector = np.abs(x_exp-mediana)
        mad_median = np.median(mad_vector)
        if mad_median <= 10e-7:
            try:
                fk_id_function = management._query_func_id("outliers")
                messages = management._get_messages(fk_id_function, self.language, "outliers")
                error = messages[7][0][0]
                raise ZeroDivisionError(error)
            except ZeroDivisionError:
                general._display_one_line_attention(messages[6][0][0])
                raise

        ## Z-score
        if which == "min":
            outlier = np.min(x_exp)
        else:
            outlier = np.max(x_exp)
        statistic =0.6745*np.abs(outlier - mediana)/mad_median


        aceita = 0
        rejeita = 1

        # concluindo o teste
        if statistic <= critical:
            if details == "short":
                fk_id_function = management._query_func_id("outliers")
                messages = management._get_messages(fk_id_function, self.language, "outliers")
                conclusion = messages[2][0][0]
            else:
                conclusion = aceita
        else:
            if details == "short":
                fk_id_function = management._query_func_id("outliers")
                messages = management._get_messages(fk_id_function, self.language, "outliers")
                conclusion = messages[3][0][0]
            else:
                conclusion = rejeita


        ### quering
        fk_id_function = management._query_func_id("generic")
        messages = management._get_messages(fk_id_function, self.language, "generic")
        self.conclusion = conclusion
        self.statistic = statistic
        self.critical = critical
        self.x_exp = x_exp
        ### making the named tuple
        name = "ModifiedZScore" + messages[1][0][0]
        result = namedtuple(name, (messages[1][3][0], messages[1][1][0], "outlier"))
        return result(statistic, critical, outlier), conclusion







    def __str__(self):
        if self.conclusion is None:
            fk_id_function = management._query_func_id("generic")
            messages = management._get_messages(fk_id_function, self.language, "generic")
            return f"{messages[2][0][0]} ModifiedZScore {messages[2][2][0]}"
        else:
            return self.conclusion


    def __repr__(self):
        fk_id_function = management._query_func_id("outliers")
        messages = management._get_messages(fk_id_function, self.language, "outliers")
        return messages[5][0][0]























# with tests, with docstring, without text
def _check_outermost_observation(x):
    """This function determines which is the outermost point from the mean

    Parameters
    ----------
    x : ``numpy array``
        One dimension :doc:`numpy array <numpy:reference/generated/numpy.array>`

    Returns
    -------
    which : ``str``
        Which value is the outermost

        * If it is ``"max"``, the outermost is the highest value
        * If it is ``"min"``, the outermost is the lowest value

    Notes
    -----
    If the min and the max value are equal (simetric), the output will be "max"


    """

    ## obtendo a média
    mean = np.mean(x)
    # obtendo o maior valor
    max = np.max(x)
    # obtendo o menor valor
    min = np.min(x)

    # calculando a diferença entre a média e o menor valor (resultado positivo)
    lower = mean - min
    # calculando a diferença entre o maior valor e a média (resultado positivo)
    upper = max - mean

    # verificando qual é o ponto mais distante
    if upper >= lower:
        which = "max"
    else:
        which = "min"

    return which














#
