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
from pycafee.functions.functions import interquartile_range

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
        pycafee.sample.outliers.ZScore.fit
        pycafee.sample.outliers.ModifiedZScore.fit
        pycafee.sample.outliers.Tukey.fit
        pycafee.sample.outliers.Dixon.fit
        pycafee.sample.outliers.Grubbs.fit


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
                    msg = [f"{messages[4][0][0]} 'details' {messages[4][2][0]}:"]
                    values = ['short', 'binary']
                    for item in values:
                        msg.append(f"   --->    '{item}'")
                    msg.append(f"{messages[4][4][0]}:")
                    msg.append(f"   --->    '{details}'")
                    general._display_n_line_attention(msg)
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
        pycafee.sample.outliers.Tukey.fit
        pycafee.sample.outliers.Dixon.fit
        pycafee.sample.outliers.Grubbs.fit

        Notes
        -----

        The **ModifiedZScore test for outlier detection** compares a possible outlier with a pre establish critical value. The test statistic is calculated using the following equation:

        .. math::

                M_i = \\frac{0.6745(|x_i-\\widetilde{x}|)}{MAD}

        where :math:`x_i` is the possible outlier, :math:`\\widetilde{x}` is the sample median and :math:`MAD` is the median of the absolute deviations about the median which is obtained with the following equation

        .. math::

                MAD = median_i\\left\\{|x_i-\\widetilde{x}|\\right\\}

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
                    msg = [f"{messages[4][0][0]} 'details' {messages[4][2][0]}:"]
                    values = ['short', 'binary']
                    for item in values:
                        msg.append(f"   --->    '{item}'")
                    msg.append(f"{messages[4][4][0]}:")
                    msg.append(f"   --->    '{details}'")
                    general._display_n_line_attention(msg)
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



class Tukey(LanguageManagement):
    """This class instantiates an object to apply the Tukey method (boxplot) for detecting oultliers

    """
    def __init__(self, language=None, **kwargs):
        super().__init__(language=language, **kwargs)
        self.conclusion = None
        self.interval = None
        self.critical = None
        self.x_exp = None



    def fit(self, x_exp, which=None, critical=None, details=None):
        """This function applies the Tukey method (Boxplot) for outlier detection [1]_.

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


        critical : ``str``, ``int`` or ``float``, optional
            The critical value of the test.

            * If ``critical="extreme"``, the critical value is ``3.0`` (default);
            * If ``critical="mild"``, the critical value is ``1.5``;
            * If a number, it must higher than zero (``0``);

        Returns
        -------
        result : ``tuple`` with
            interval : ``list`` of ``floats``
                The range where the data are not considered to be outliers
            critical : ``float``
                The critical value.
            outlier : ``float`` or ``int``
                The value checked as a possible outlier

        conclusion : ``str`` or ``int``
            The test conclusion (e.g, Possible outlier/ no outliers).


        See Also
        --------
        pycafee.sample.outliers.ZScore.fit
        pycafee.sample.outliers.ModifiedZScore.fit
        pycafee.sample.outliers.Dixon.fit
        pycafee.sample.outliers.Grubbs.fit

        Notes
        -----

        The **Tukey test for outlier detection** checks if the possible outlier is within the interval adjacent to the data, e. g., the interval where the sample is not considered an outlier. The lower limit of this range is estimated through the following equation:

        .. math::

                lower = Q_1 - C \\times IR

        where :math:`Q_1` is the first quartile, :math:`IR` is the interquartile range and :math:`C` is the decision criterion value. The upper limit of the decision range is estimaged through the following equation:

        .. math::

                upper = Q_3 + C \\times IR

        where :math:`Q_3` is the third quartile. The interquartile range is estimated with :ref:`interquartile_range <interquartile_range>` function using ``method="tukey"``.

        By default, the decision criterion value is ``3.0``, which implies checking for an extreme outlier. The conclusion of the test is done by checking if the ``outlier`` is within the range where the data are not considered as a outlier:

        .. code:: python

           if lower <= outlier <= upper:
               Data does not have a outlier
           else:
               Data has a outlier



        References
        ----------
        .. [1] TUKEY, J. W. Exploring Data Analysis. 1. ed. Reading: Addison-Wesley Publishing Company. Inc., 1977.



        Examples
        --------

        **Looking for extreme outlier**


        >>> from pycafee.sample.outliers import Tukey
        >>> import numpy as np
        >>> x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        >>> test = Tukey()
        >>> result, conclusion = test.fit(x)
        >>> print(result)
        TukeyResult(Interval=[3.3999999999999986, 6.200000000000001], critical=3, Outlier=5.4)
        >>> print(conclusion)
        The dataset has no outliers


        **Looking for mild outlier**


        >>> from pycafee.sample.outliers import Tukey
        >>> import numpy as np
        >>> x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        >>> test = Tukey()
        >>> result, conclusion = test.fit(x, critical="mild")
        >>> print(result)
        TukeyResult(Interval=[3.999999999999999, 5.6000000000000005], Critical=1.5, Outlier=5.4)
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
        elif type(critical) == str:
            checkers._check_is_str(critical, "critical", self.language)
            if critical == "mild":
                critical = 1.5
            elif critical == "extreme":
                critical = 3
            else:
                fk_id_function = management._query_func_id("generic")
                messages = management._get_messages(fk_id_function, self.language, "generic")
                try:
                    error = messages[3][0][0]
                    raise ValueError(error)
                except ValueError:
                    msg = [f"{messages[4][0][0]} 'critical' {messages[4][2][0]}:"]
                    values = ['mild', 'extreme']
                    for item in values:
                        msg.append(f"   --->    '{item}'")
                    msg.append(f"{messages[4][4][0]}:")
                    msg.append(f"   --->    '{critical}'")
                    general._display_n_line_attention(msg)
                    raise
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
                    msg = [f"{messages[4][0][0]} 'details' {messages[4][2][0]}:"]
                    values = ['short', 'binary']
                    for item in values:
                        msg.append(f"   --->    '{item}'")
                    msg.append(f"{messages[4][4][0]}:")
                    msg.append(f"   --->    '{details}'")
                    general._display_n_line_attention(msg)
                    raise



        # ordenando os dados
        x_exp = np.sort(x_exp, kind='quicksort')

        # obtendo a dstancia interquerlica
        result, x_low, x_upper = interquartile_range(x_exp,method="tukey",language=self.language)
        DI = result[0]
        q1 = result[1]
        q3 = result[2]


        ## interval
        interval_lower = q1 - critical*DI
        interval_upper = q3 + critical*DI
        if which == "min":
            outlier = np.min(x_exp)
        else:
            outlier = np.max(x_exp)


        aceita = 0
        rejeita = 1
        if interval_lower <= outlier <= interval_upper:
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
        self.interval = [interval_lower, interval_upper]
        self.critical = critical
        self.x_exp = x_exp
        ### making the named tuple

        name = "Tukey" + messages[1][0][0]
        result = namedtuple(name, (messages[1][5][0], messages[1][1][0], messages[1][4][0]))
        return result(self.interval, critical, outlier), conclusion




    def __str__(self):
        if self.conclusion is None:
            fk_id_function = management._query_func_id("generic")
            messages = management._get_messages(fk_id_function, self.language, "generic")
            return f"{messages[2][0][0]} Tukey {messages[2][2][0]}"
        else:
            return self.conclusion


    def __repr__(self):
        fk_id_function = management._query_func_id("outliers")
        messages = management._get_messages(fk_id_function, self.language, "outliers")
        return messages[8][0][0]



class Dixon(AlphaManagement, NDigitsManagement):
    """This class instantiates an object to apply the Dixon test for detecting oultliers

    """

    DIXON_TABLE_r10 = {
        "n_rep" : [
                    3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
                    ],
        0.20 : [
                0.886, 0.679, 0.557, 0.482, 0.434, 0.399, 0.370, 0.349, 0.332, 0.318, 0.305, 0.294, 0.285, 0.277, 0.269, 0.263, 0.258, 0.252, 0.247, 0.242, 0.238, 0.234, 0.230, 0.227, 0.224, 0.220, 0.218, 0.215
                ],
        0.10 : [
                0.941, 0.765, 0.642, 0.560, 0.507, 0.468, 0.437, 0.412, 0.392, 0.376, 0.361, 0.349, 0.338, 0.329, 0.320, 0.313, 0.306, 0.300, 0.295, 0.290, 0.285, 0.281, 0.277, 0.273, 0.269, 0.266, 0.263, 0.260
                ],
        0.05 : [
                0.970, 0.829, 0.710, 0.625, 0.568, 0.526, 0.493, 0.466, 0.444, 0.426, 0.410, 0.396, 0.384, 0.374, 0.365, 0.356, 0.349, 0.342, 0.337, 0.331, 0.326, 0.321, 0.317, 0.312, 0.308, 0.305, 0.301, 0.298
                ],
        0.04 : [
                0.976, 0.846, 0.729, 0.644, 0.586, 0.543, 0.510, 0.483, 0.460, 0.441, 0.425, 0.411, 0.399, 0.388, 0.379, 0.370, 0.363, 0.356, 0.350, 0.344, 0.338, 0.333, 0.329, 0.324, 0.320, 0.316, 0.312, 0.309
                ],
        0.02 : [
                0.988, 0.889, 0.780, 0.698, 0.637, 0.590, 0.555, 0.527, 0.502, 0.482, 0.465, 0.450, 0.438, 0.426, 0.416, 0.407, 0.398, 0.391, 0.384, 0.378, 0.372, 0.367, 0.362, 0.357, 0.353, 0.349, 0.345, 0.341
                ],
        0.01 : [
                0.994, 0.926, 0.821, 0.740, 0.680, 0.634, 0.598, 0.568, 0.542, 0.522, 0.503, 0.488, 0.475, 0.463, 0.452, 0.442, 0.433, 0.425, 0.418, 0.411, 0.404, 0.399, 0.393, 0.388, 0.384, 0.380, 0.376, 0.372
                ]
        }

    DIXON_TABLE_r11 = {
        "n_rep" : [
                    4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
                    ],
        0.20 : [
                0.910, 0.728, 0.609, 0.530, 0.479, 0.441, 0.409, 0.385, 0.367, 0.350, 0.336, 0.323, 0.313, 0.303, 0.295, 0.288, 0.282, 0.276, 0.270, 0.265, 0.260, 0.255, 0.250, 0.246, 0.243, 0.239, 0.236
                ],
        0.10 : [
                0.955, 0.807, 0.689, 0.610, 0.554, 0.512, 0.477, 0.450, 0.428, 0.410, 0.395, 0.381, 0.369, 0.359, 0.349, 0.341, 0.334, 0.327, 0.320, 0.314, 0.309, 0.304, 0.299, 0.295, 0.291, 0.287, 0.283
                ],
        0.05 : [
                0.977, 0.863, 0.748, 0.673, 0.615, 0.570, 0.534, 0.505, 0.481, 0.461, 0.445, 0.430, 0.417, 0.406, 0.396, 0.386, 0.379, 0.371, 0.364, 0.357, 0.352, 0.346, 0.341, 0.337, 0.332, 0.328, 0.324
                ],
        0.04 : [
                0.981, 0.876, 0.763, 0.689, 0.631, 0.587, 0.551, 0.521, 0.498, 0.477, 0.460, 0.445, 0.432, 0.420, 0.410, 0.400, 0.392, 0.384, 0.377, 0.371, 0.365, 0.359, 0.354, 0.349, 0.344, 0.340, 0.336
                ],
        0.02 : [
                0.991, 0.916, 0.805, 0.740, 0.683, 0.635, 0.597, 0.566, 0.541, 0.520, 0.502, 0.486, 0.472, 0.460, 0.449, 0.439, 0.430, 0.421, 0.414, 0.407, 0.400, 0.394, 0.389, 0.383, 0.378, 0.374, 0.369
                ],
        0.01 : [
                0.995, 0.937, 0.839, 0.782, 0.725, 0.677, 0.639, 0.606, 0.580, 0.558, 0.539, 0.522, 0.508, 0.495, 0.484, 0.473, 0.464, 0.455, 0.446, 0.439, 0.432, 0.426, 0.420, 0.414, 0.409, 0.404, 0.399
                ]
        }

    DIXON_TABLE_r12 = {
        "n_rep" : [
                    5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
                    ],
        0.20 : [
                0.919, 0.745, 0.636, 0.557, 0.504, 0.464, 0.431, 0.406, 0.387, 0.369, 0.354, 0.341, 0.330, 0.320, 0.311, 0.303, 0.296, 0.290, 0.284, 0.278, 0.273, 0.268, 0.263, 0.259, 0.255, 0.251
                ],
        0.10 : [
                0.960, 0.824, 0.712, 0.632, 0.580, 0.537, 0.502, 0.473, 0.451, 0.432, 0.416, 0.401, 0.388, 0.377, 0.367, 0.358, 0.349, 0.342, 0.336, 0.330, 0.324, 0.319, 0.314, 0.309, 0.305, 0.301
                ],
        0.05 : [
                0.980, 0.878, 0.773, 0.692, 0.639, 0.594, 0.559, 0.529, 0.505, 0.485, 0.467, 0.452, 0.438, 0.426, 0.415, 0.405, 0.396, 0.388, 0.381, 0.374, 0.368, 0.362, 0.357, 0.352, 0.347, 0.343
                ],
        0.04 : [
                0.984, 0.891, 0.791, 0.708, 0.656, 0.610, 0.575, 0.546, 0.521, 0.501, 0.482, 0.467, 0.453, 0.440, 0.429, 0.419, 0.410, 0.402, 0.394, 0.387, 0.381, 0.375, 0.370, 0.365, 0.360, 0.355
                ],
        0.02 : [
                0.992, 0.925, 0.836, 0.760, 0.702, 0.655, 0.619, 0.590, 0.564, 0.542, 0.523, 0.508, 0.493, 0.480, 0.469, 0.458, 0.449, 0.440, 0.432, 0.423, 0.417, 0.411, 0.405, 0.399, 0.394,0.389
                ],
        0.01 : [
                0.996, 0.951, 0.875, 0.797, 0.739, 0.694, 0.658, 0.629, 0.602, 0.580, 0.560, 0.544, 0.529, 0.516, 0.504, 0.493, 0.483, 0.474, 0.465, 0.457, 0.450, 0.443, 0.437, 0.431, 0.426, 0.420
                ]
        }

    DIXON_TABLE_r20 = {
        "n_rep" : [
                    4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
                    ],
        0.20 : [
                0.935, 0.782, 0.670, 0.596, 0.545, 0.505, 0.474, 0.449, 0.429, 0.411, 0.395, 0.382, 0.370, 0.359, 0.350, 0.341, 0.333, 0.326, 0.320, 0.314, 0.309, 0.304, 0.300, 0.296, 0.292, 0.288, 0.285
                ],
        0.10 : [
                0.967, 0.845, 0.736, 0.661, 0.607, 0.565, 0.531, 0.504, 0.481, 0.461, 0.445, 0.430, 0.418, 0.406, 0.397, 0.387, 0.378, 0.371, 0.364, 0.358, 0.352, 0.346, 0.342, 0.338, 0.333, 0.329, 0.326
                ],
        0.05 : [
                0.983, 0.890, 0.786, 0.716, 0.657, 0.614, 0.579, 0.551, 0.527, 0.506, 0.489, 0.473, 0.460, 0.447, 0.437, 0.427, 0.418, 0.410, 0.402, 0.395, 0.390, 0.383, 0.379, 0.374, 0.370, 0.365, 0.361
                ],
        0.04 : [
                0.987, 0.901, 0.800, 0.732, 0.670, 0.627, 0.592, 0.564, 0.540, 0.520, 0.502, 0.486, 0.472, 0.460, 0.449, 0.439, 0.430, 0.422, 0.414, 0.407, 0.401, 0.395, 0.390, 0.385, 0.381, 0.376, 0.372
                ],
        0.02 : [
                0.992, 0.929, 0.836, 0.778, 0.710, 0.667, 0.632, 0.603, 0.579, 0.557, 0.538, 0.522, 0.508, 0.495, 0.484, 0.473, 0.464, 0.455, 0.447, 0.440, 0.434, 0.428, 0.422, 0.477, 0.412, 0.407, 0.402
                ],
        0.01 : [
                0.996, 0.950, 0.865, 0.814, 0.746, 0.700, 0.664, 0.627, 0.612, 0.590, 0.571, 0.554, 0.539, 0.526, 0.514, 0.503, 0.494, 0.485, 0.477, 0.469, 0.462, 0.456, 0.450, 0.444, 0.439, 0.434, 0.428
                ]
        }

    DIXON_TABLE_r21 = {
        "n_rep" : [
                    5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
                    ],
        0.20 : [
                0.952, 0.821, 0.725, 0.650, 0.594, 0.551, 0.517, 0.490, 0.467, 0.448, 0.431, 0.416, 0.403, 0.391, 0.380, 0.371, 0.363, 0.356, 0.349, 0.343, 0.337, 0.331, 0.325, 0.320, 0.316, 0.312
                ],
        0.10 : [
                0.976, 0.872, 0.780, 0.710, 0.657, 0.612, 0.576, 0.546, 0.521, 0.501, 0.483, 0.467, 0.453, 0.440, 0.428, 0.419, 0.410, 0.402, 0.395, 0.388, 0.382, 0.376, 0.370, 0.365, 0.360, 0.355
                ],
        0.05 : [
                0.987, 0.913, 0.828, 0.763, 0.710, 0.664, 0.625, 0.592, 0.565, 0.544, 0.525, 0.509, 0.495, 0.482, 0.469, 0.460, 0.450, 0.441, 0.434, 0.427, 0.420, 0.414, 0.407, 0.402, 0.396, 0.391
                ],
        0.04 : [
                0.990, 0.924, 0.842, 0.780, 0.725, 0.678, 0.638, 0.605, 0.578, 0.556, 0.537, 0.521, 0.507, 0.494, 0.482, 0.472, 0.462, 0.453, 0.445, 0.438, 0.431, 0.424, 0.418, 0.412, 0.406, 0.401
                ],
        0.02 : [
                0.995, 0.951, 0.885, 0.829, 0.776, 0.726, 0.679, 0.642, 0.615, 0.593, 0.574, 0.557, 0.542, 0.529, 0.517, 0.506, 0.496, 0.487, 0.479, 0.471, 0.464, 0.457, 0.450, 0.444, 0.438, 0.433
                ],
        0.01 : [
                0.998, 0.970, 0.919, 0.868, 0.816, 0.760, 0.713, 0.675, 0.649, 0.627, 0.607, 0.580, 0.573, 0.559, 0.547, 0.536, 0.526, 0.517, 0.509, 0.501, 0.493, 0.486, 0.479, 0.472, 0.466, 0.460
                ]
        }

    DIXON_TABLE_r22 = {
        "n_rep" : [
                    6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
                    ],
        0.20 : [
                0.965, 0.850, 0.745, 0.676, 0.620, 0.578, 0.543, 0.515, 0.492, 0.472, 0.454, 0.438, 0.424, 0.412, 0.401, 0.391, 0.382, 0.374, 0.367, 0.360, 0.354, 0.348, 0.342, 0.337, 0.332
                ],
        0.10 : [
                0.983, 0.881, 0.803, 0.737, 0.682, 0.637, 0.600, 0.570, 0.546, 0.525, 0.507, 0.490, 0.475, 0.462, 0.450, 0.440, 0.430, 0.421, 0.413, 0.406, 0.399, 0.393, 0.387, 0.381, 0.376
                ],
        0.05 : [
                0.990, 0.909, 0.846, 0.787, 0.734, 0.688, 0.648, 0.616, 0.590, 0.568, 0.548, 0.531, 0.516, 0.503, 0.491, 0.480, 0.470, 0.461, 0.452, 0.445, 0.438, 0.432, 0.426, 0.419, 0.414
                ],
        0.04 : [
                0.992, 0.919, 0.857, 0.800, 0.749, 0.703, 0.661, 0.628, 0.602, 0.579, 0.559, 0.542, 0.527, 0.514, 0.502, 0.491, 0.481, 0.472, 0.464, 0.457, 0.450, 0.443, 0.437, 0.431, 0.425
                ],
        0.02 : [
                0.995, 0.945, 0.890, 0.840, 0.791, 0.745, 0.704, 0.670, 0.641, 0.616, 0.595, 0.577, 0.561, 0.547, 0.535, 0.524, 0.514, 0.505, 0.497, 0.489, 0.482, 0.475, 0.469, 0.463, 0.457
                ],
        0.01 : [
                0.998, 0.970, 0.922, 0.873, 0.826, 0.781, 0.740, 0.705, 0.674, 0.647, 0.624, 0.605, 0.589, 0.575, 0.562, 0.551, 0.541, 0.532, 0.524, 0.516, 0.508, 0.501, 0.495, 0.489, 0.483
                ]
        }

    def __init__(self, name=None, alfa=None, language=None, n_digits=None, **kwargs):
        super().__init__(alfa=alfa, language=language, n_digits=n_digits, **kwargs)
        self.conclusion = None
        self.statistic = None
        self.critical = None
        self.x_exp = None


    # with tests, with text, with database, with docstring
    def get_critical_value(self, n_rep, ratio=None, alfa=None):
        """This function returns the critical value (tabulated) of the Dixon test for outlier detection [1]_. The critical values are the values given by Rorabacher [2]_ for the two-tailed distribution.

        Parameters
        ----------
        n_rep : ``int``
            The total number of observations (``n_rep >= 3``, vary).
        ratio : ``str``, optional
            The ratio. It can be ``"r10"`` (or ``None``), ``"r11"``, ``"r12"``, ``"r20"``, ``"r21"`` or ``"r22"``.
        alfa : ``float``
            The significance level (between ``0.0`` and ``1.0``, default = ``0.05``)

        Returns
        -------
        result : ``tuple`` with:
            critical : ``float``
                The critical value.
            alfa : ``float``
                The corresponding significance level.

        Notes
        -----

        There are critical values for confidence levels of ``0.20``, ``0.10``, ``0.05``, ``0.04``, ``0.02`` and ``0.01``, which also depend on the ``ratio`` parameter and the sample size (``n_rep``):

        * For ``ratio="r10"`` there are critical values within this range ``3<=n_rep<=30``;
        * For ``ratio="r11"`` there are critical values within this range ``4<=n_rep<=30``;
        * For ``ratio="r12"`` there are critical values within this range ``5<=n_rep<=30``;
        * For ``ratio="r20"`` there are critical values within this range ``4<=n_rep<=30``;
        * For ``ratio="r21"`` there are critical values within this range ``5<=n_rep<=30``;
        * For ``ratio="r22"`` there are critical values within this range ``6<=n_rep<=30``;


        References
        ----------
        .. [1] DIXON, W. J. Processing Data for Outliers. Biometrics, v. 9, n. 1, p. 74–89, 1953.

        .. [2] RORABACHER, D. B. Statistical Treatment for Rejection of Deviant Values: Critical Values of Dixon’s "Q" Parameter and Related Subrange Ratios at the 95% Confidence Level. v. 63, n. 2, p. 139–146, 1991.

        Examples
        --------

        >>> from pycafee.sample.dixon import Dixon
        >>> outliers = Dixon()
        >>> result = outliers.get_critical_value(7)
        >>> print(result)
        DixonResult(critical=0.568, alpha=0.05)


        >>> from pycafee.sample.dixon import Dixon
        >>> outliers = Dixon()
        >>> result = outliers.get_critical_value(7, alfa=0.01)
        >>> print(result)
        DixonResult(critical=0.51, alpha=0.01)


        >>> from pycafee.sample.dixon import Dixon
        >>> outliers = Dixon()
        >>> result = outliers.get_critical_value(7, ratio="r11")
        >>> print(result)
        DixonResult(critical=0.673, alpha=0.05)



        """

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

        ### checking the ratio ###
        if ratio is None:
            ratio = "r10"
        else:
            checkers._check_is_str(ratio, "ratio", language=self.language)


        checkers._check_value_is_equal_or_lower_than(n_rep, "n_rep", 30, language=self.language)
        if ratio == "r10":
            checkers._check_value_is_equal_or_higher_than(n_rep, "n_rep", 3, language=self.language)
            table_data = Dixon.DIXON_TABLE_r10
        elif ratio == "r11":
            checkers._check_value_is_equal_or_higher_than(n_rep, "n_rep", 4, language=self.language)
            table_data = Dixon.DIXON_TABLE_r11
        elif ratio == "r12":
            checkers._check_value_is_equal_or_higher_than(n_rep, "n_rep", 5, language=self.language)
            table_data = Dixon.DIXON_TABLE_r12
        elif ratio == "r20":
            checkers._check_value_is_equal_or_higher_than(n_rep, "n_rep", 4, language=self.language)
            table_data = Dixon.DIXON_TABLE_r20
        elif ratio == "r21":
            checkers._check_value_is_equal_or_higher_than(n_rep, "n_rep", 5, language=self.language)
            table_data = Dixon.DIXON_TABLE_r21
        elif ratio == "r22":
            checkers._check_value_is_equal_or_higher_than(n_rep, "n_rep", 6, language=self.language)
            table_data = Dixon.DIXON_TABLE_r22
        else:
            fk_id_function = management._query_func_id("Dixon")
            messages = management._get_messages(fk_id_function, self.language, "Dixon")
            try:
                error = messages[1][0][0]
                raise ValueError(error)
            except ValueError:
                allowed_ratios = ["r10", "r11", "r12", "r20", "r21", "r22"]
                ratios = [f"    --->    '{allowed}'" for allowed in allowed_ratios]
                msg = [
                    f"{messages[2][0][0]} '{ratio}'.",
                    f"{messages[2][2][0]}:",
                    ratios
                    ]
                flat_list = general._flatten_list_of_list_string(msg)
                flat_list = list(flat_list)
                general._display_n_line_attention(
                    flat_list
                )
                raise

        ### getting the critical value ###
        critical = table_data[alfa][n_rep-table_data['n_rep'][0]]

        ### quering
        fk_id_function = management._query_func_id("generic")
        messages = management._get_messages(fk_id_function, self.language, "generic")

        ### making the named tuple
        name = "Dixon" + messages[1][0][0]
        result = namedtuple(name, (messages[1][1][0], messages[1][2][0]))
        return result(critical, alfa)



    # with tests, with text, with database (Dixon), with docstring
    def fit(self, x_exp, ratio=None, which=None, alfa=None, details=None):
        """This function applies the Dixon test to identify outliers in Normal data with few samples [1]_.

        Parameters
        ----------
        x_exp : ``numpy array``
            One dimension :doc:`numpy array <numpy:reference/generated/numpy.array>` with at least 3 sample data (vary).
        ratio : ``str`` or ``None``, optional
            The ratio to be used. This parameter determines the equation and critical data that are used.
        alfa : ``float``, optional
            The level of significance (``ɑ``). Default is ``None`` which results in ``0.05`` (``ɑ = 5%``).
        details : ``str``, optional
            The ``details`` parameter determines the amount of information presented about the hypothesis test.

            * If ``details = "short"`` (or ``None``, e.g, the default), a simplified version of the test result is returned.
            * If ``details = "full"``, a detailed version of the hypothesis test result is returned.
            * if ``details = "binary"``, the conclusion will be ``1`` (:math:`H_0` is rejected) or ``0`` (:math:`H_0` is accepted).
        which : ``str``, optional
            The value that should be evaluated as a possible outlier.

            * If it is ``None`` (default), the outlier is automatically inferred as the farthest observation from the mean
            * If it is ``"max"``, the highest value is checked if it is a possible outlier.
            * If it is ``"min"``, the lowest value is checked if it is a possible outlier.

        Returns
        -------
        result : ``tuple`` with
            statistic : ``float``
                The test statistic.
            critical : ``float``
                The critical value.
            alpha : ``float``
                The significance level used.
            ratio : ``str``
                The ratio used.
        conclusion : ``str``
            The test conclusion (e.g, Possible outlier/ no outliers).

        See Also
        --------
        get_critical_value
        pycafee.sample.outliers.ZScore.fit
        pycafee.sample.outliers.ModifiedZScore.fit
        pycafee.sample.outliers.Tukey.fit
        pycafee.sample.outliers.Grubbs.fit


        Notes
        -----

        The **Dixon test for outlier detection** has the following premise:

        .. admonition:: \u2615

           :math:`H_0:` data **does not have** a outlier.

           :math:`H_1:` data **has** a outlier.

        The conclusion of the test is based on the comparison between the ``critical`` value (at ``ɑ`` significance level) and ``statistic`` of the test:

        .. code:: python

           if critical <= statistic:
               Data does not have a outlier
           else:
               Data has a outlier


        There are critical values for alpha equal to ``0.20``, ``0.10``, ``0.05``, ``0.04``, ``0.02`` and ``0.01``. These values are for the **two-tailed Dixon distribution** [2]_.

        The minimum number of samples needed to apply the test varies depending on the ratio parameter, while the maximum number for all cases is 30. The available ranges are:

        * For ``ratio="r10"`` :math:`\\rightarrow 3 \\leq n \\leq 30`;
        * For ``ratio="r11"`` :math:`\\rightarrow 4 \\leq n \\leq 30`;
        * For ``ratio="r12"`` :math:`\\rightarrow 5 \\leq n \\leq 30`;
        * For ``ratio="r20"`` :math:`\\rightarrow 4 \\leq n \\leq 30`;
        * For ``ratio="r21"`` :math:`\\rightarrow 5 \\leq n \\leq 30`;
        * For ``ratio="r22"`` :math:`\\rightarrow 6 \\leq n \\leq 30`;

        The ``ratio`` parameter determines which equation will be used to apply the test. If ``ratio=None`` (default), the general rule [2]_ is used to determine outliers:

        * If :math:`3 \\leq n \\leq 7` then ``ratio=r10`` is used;
        * If :math:`8 \\leq n \\leq 10` then ``ratio=r11`` is used;
        * If :math:`10 \\leq n \\leq 13` then ``ratio=r21`` is used;
        * If :math:`14 \\leq n \\leq 30` then ``ratio=r22`` is used;

        The equations to calculate the test statistic (for the minimum or maximum values) depend on the ratio parameter, and are calculated as follows:


        * If ``ratio="r10"``:

        .. math::

            r_{10, min} = \\frac{x_2-x_1}{x_n-x_1} \\; \\; \\; OR \\; \\; \\;  r_{10,max} = \\frac{x_n-x_{n-1}}{x_n-x_1}


        * If ``ratio="r11"``:

        .. math::

            r_{11, min} = \\frac{x_2-x_{1}}{x_{n-1}-x_1} \\; \\; \\; OR \\; \\; \\;  r_{11,max} = \\frac{x_n-x_{n-1}}{x_{n}-x_2}


        * If ``ratio="r12"``:

        .. math::

            r_{12, min} = \\frac{x_2-x_{1}}{x_{n-2}-x_1} \\; \\; \\; OR \\; \\; \\;  r_{12,max} = \\frac{x_n-x_{n-1}}{x_{n}-x_3}


        * If ``ratio="r20"``:

        .. math::

            r_{20, min} = \\frac{x_3-x_{1}}{x_{n}-x_1} \\; \\; \\; OR \\; \\; \\;  r_{20,max} = \\frac{x_n-x_{n-2}}{x_{n}-x_1}


        * If ``ratio="r21"``:

        .. math::

            r_{21, min} = \\frac{x_3-x_{1}}{x_{n-1}-x_1} \\; \\; \\; OR \\; \\; \\;  r_{21,max} = \\frac{x_n-x_{n-2}}{x_{n}-x_2}


        * If ``ratio="r22"``:

        .. math::

            r_{22, min} = \\frac{x_3-x_{1}}{x_{n-2}-x_1} \\; \\; \\; OR \\; \\; \\;  r_{22,max} = \\frac{x_n-x_{n-2}}{x_{n}-x_3}


        References
        ----------
        .. [1] DIXON, W. J. Processing Data for Outliers. Biometrics, v. 9, n. 1, p. 74–89, 1953.

        .. [2] RORABACHER, D. B. Statistical Treatment for Rejection of Deviant Values: Critical Values of Dixon’s "Q" Parameter and Related Subrange Ratios at the 95% Confidence Level. v. 63, n. 2, p. 139–146, 1991.

        Examples
        --------

        **Checking if the highest value (15.68) is a possible outlier:**

        >>> from pycafee.sample.dixon import Dixon
        >>> import numpy as np
        >>> x_exp = np.array([15.48, 15.51, 15.52, 15.52, 15.53, 15.53, 15.68])
        >>> test = Dixon()
        >>> result, conclusion = test.fit(x_exp, which='max', details="full")
        >>> print(result)
        DixonResult(Statistic=0.7500000000000044, critical=0.568, alpha=0.05, ratio='r10')
        >>> print(conclusion)
        Since the test statistic value (0.75) is higher than the critical value (0.568), we have evidence to reject the null hypothesis that the sample does not contain outliers, and perhaps the upper value (15.68) is an outlier (with 95.0% confidence).


        **Checking if the lowest value (15.43) is a possible outlier:**

        >>> from pycafee.sample.dixon import Dixon
        >>> import numpy as np
        >>> x_exp = np.array([15.43, 15.48, 15.51, 15.52, 15.52, 15.53, 15.53, 15.58])
        >>> test = Dixon()
        >>> result, conclusion = test.fit(x_exp, which='min', details="full")
        >>> print(result)
        DixonResult(Statistic=0.5000000000000089, critical=0.615, alpha=0.05, ratio='r11')
        >>> print(conclusion)
        Since the test statistic value (0.5) is lower than the critical value (0.615), we have no evidence to reject the null hypothesis that the sample does not contain outliers (with 95.0% confidence).



        """


        ### getting the default alpha value ###
        if alfa is None:
            alfa = self.alfa
        else:
            checkers._check_is_float(alfa, "alfa", self.language)
            checkers._check_data_in_range(alfa, "alfa", 0.0, 1.0, self.language)
            self.alfa = alfa


        ### checking input data ###
        checkers._check_is_numpy_1_D(x_exp, "x_exp", self.language)
        self.x_exp = x_exp

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
                    error = messages[1][0][0]
                    raise ValueError(error)
                except ValueError:
                    general._display_one_line_attention(f"{messages[2][0][0]} '{details}'")
                    raise

        # finding the n_rep
        n_rep = x_exp.size
        checkers._check_value_is_equal_or_lower_than(n_rep, "n_rep", 30, language=self.language)

        ### checking the ratio ###
        if ratio is None:
            pass
        else:
            checkers._check_is_str(ratio, "ratio", language=self.language)


        ### checking the which ###
        if which is None:
            which = _check_outermost_observation(x_exp)
        else:
            checkers._check_is_str(which, "which", language=self.language)
            if which not in ["min", "max"]:
                fk_id_function = management._query_func_id("Dixon")
                messages = management._get_messages(fk_id_function, self.language, "Dixon")
                try:
                    error = messages[9][0][0]
                    raise ValueError(error)
                except ValueError:
                    general._display_one_line_attention(f"{messages[9][1][0]} '{which}'")
                    raise


        # ordenando os dados
        x_exp = np.sort(x_exp, kind='quicksort')

        # quering
        fk_id_function = management._query_func_id("Dixon")
        messages = management._get_messages(fk_id_function, self.language, "Dixon")


        aceita = 0
        rejeita = 1

        if which == "min":
            value_tested = x_exp[0]
            if ratio is None:
                if 3 <= n_rep <= 7:
                    ratio = "r10"
                    statistic = self._r10(x_exp, which="min")
                elif 8 <= n_rep <= 10:
                    ratio = "r11"
                    statistic = self._r11(x_exp, which="min")
                elif 11 <= n_rep <= 13:
                    ratio = "r21"
                    statistic = self._r21(x_exp, which="min")
                else:
                    ratio = "r22"
                    statistic = self._r22(x_exp, which="min")
            elif ratio == "r10":
                statistic = self._r10(x_exp, which="min")
            elif ratio == "r11":
                statistic = self._r11(x_exp, which="min")
            elif ratio == "r12":
                statistic = self._r12(x_exp, which="min")
            elif ratio == "r20":
                statistic = self._r20(x_exp, which="min")
            elif ratio == "r21":
                statistic = self._r21(x_exp, which="min")
            elif ratio == "r22":
                statistic = self._r22(x_exp, which="min")
            else:
                fk_id_function = management._query_func_id("Dixon")
                messages = management._get_messages(fk_id_function, self.language, "Dixon")
                try:
                    error = messages[1][0][0]
                    raise ValueError(error)
                except ValueError:
                    allowed_ratios = ["r10", "r11", "r12", "r20", "r21", "r22"]
                    ratios = [f"    --->    '{allowed}'" for allowed in allowed_ratios]
                    msg = [
                        f"{messages[2][0][0]} '{ratio}'.",
                        f"{messages[2][2][0]}:",
                        ratios
                        ]
                    flat_list = general._flatten_list_of_list_string(msg)
                    flat_list = list(flat_list)
                    general._display_n_line_attention(
                        flat_list
                    )
                    raise

            ### getting the tabulated value ###
            result = self.get_critical_value(n_rep=n_rep, alfa=alfa, ratio=ratio)
            critical = result[0] # interessa apenas o primero valor
            if statistic > critical:
                if details == "short":
                    conclusion = f"{messages[3][0][0]}{value_tested}{messages[3][2][0]} {100*(1-alfa)}{messages[3][4][0]}."
                elif details == "full":
                    conclusion = f"{messages[4][0][0]}{helpers._truncate(statistic, language=self.language, decs=self.n_digits)}{messages[4][2][0]}{critical}{messages[4][4][0]}{value_tested}{messages[4][6][0]} {100*(1-alfa)}{messages[4][8][0]}."
                else:
                    conclusion = 1
            else:
                if details == "short":
                    conclusion = f"{messages[5][0][0]} {100*(1-alfa)}{messages[5][2][0]}."
                elif details == "full":
                    conclusion = f"{messages[6][0][0]}{helpers._truncate(statistic, language=self.language, decs=self.n_digits)}{messages[6][2][0]}{critical}{messages[6][4][0]} {100*(1-alfa)}{messages[6][6][0]}."
                else:
                    conclusion = 0


        else:
            value_tested = x_exp[-1]
            if ratio is None:
                if 3 <= n_rep <= 7:
                    ratio = "r10"
                    statistic = self._r10(x_exp, which="max")
                elif 8 <= n_rep <= 10:
                    ratio = "r11"
                    statistic = self._r11(x_exp, which="max")
                elif 11 <= n_rep <= 13:
                    ratio = "r21"
                    statistic = self._r21(x_exp, which="max")
                else:
                    ratio = "r22"
                    statistic = self._r22(x_exp, which="max")
            elif ratio == "r10":
                statistic = self._r10(x_exp, which="max")
            elif ratio == "r11":
                statistic = self._r11(x_exp, which="max")
            elif ratio == "r12":
                statistic = self._r12(x_exp, which="max")
            elif ratio == "r20":
                statistic = self._r20(x_exp, which="max")
            elif ratio == "r21":
                statistic = self._r21(x_exp, which="max")
            elif ratio == "r22":
                statistic = self._r22(x_exp, which="max")
            else:
                fk_id_function = management._query_func_id("Dixon")
                messages = management._get_messages(fk_id_function, self.language, "Dixon")
                try:
                    error = messages[1][0][0]
                    raise ValueError(error)
                except ValueError:
                    allowed_ratios = ["r10", "r11", "r12", "r20", "r21", "r22"]
                    ratios = [f"    --->    '{allowed}'" for allowed in allowed_ratios]
                    msg = [
                        f"{messages[2][0][0]} '{ratio}'.",
                        f"{messages[2][2][0]}:",
                        ratios
                        ]
                    flat_list = general._flatten_list_of_list_string(msg)
                    flat_list = list(flat_list)
                    general._display_n_line_attention(
                        flat_list
                    )
                    raise
            ### getting the tabulated value ###
            result = self.get_critical_value(n_rep=n_rep, alfa=alfa, ratio=ratio)
            critical = result[0] # interessa apenas o primero valor
            if statistic > critical:
                if details == "short":
                    conclusion = f"{messages[7][0][0]}{value_tested}{messages[7][2][0]} {100*(1-alfa)}{messages[7][4][0]}."
                elif details == "full":
                    conclusion = f"{messages[8][0][0]}{helpers._truncate(statistic, language=self.language, decs=self.n_digits)}{messages[8][2][0]}{critical}{messages[8][4][0]}{value_tested}{messages[8][6][0]} {100*(1-alfa)}{messages[8][8][0]}."
                else:
                    conclusion = 1
            else:
                if details == "short":
                    conclusion = f"{messages[5][0][0]} {100*(1-alfa)}{messages[5][2][0]}."
                elif details == "full":
                    conclusion = f"{messages[6][0][0]}{helpers._truncate(statistic, language=self.language, decs=self.n_digits)}{messages[6][2][0]}{critical}{messages[6][4][0]} {100*(1-alfa)}{messages[6][6][0]}."
                else:
                    conclusion = 0

        ### quering
        fk_id_function = management._query_func_id("generic")
        messages = management._get_messages(fk_id_function, self.language, "generic")
        self.conclusion = conclusion
        self.statistic = statistic
        self.critical = critical
        self.x_exp = x_exp
        ### making the named tuple
        name = "Dixon" + messages[1][0][0]
        result = namedtuple(name, (messages[1][3][0], messages[1][1][0], messages[1][2][0], "ratio"))
        return result(statistic, critical, alfa, ratio), conclusion



    # with tests, with text, with database (Dixon), with docstring
    def _r10(self, x_exp, which):
        """The equation to calculate the Dixon statsitic for the ``r10`` ratio as described at [1]_

        Parameters
        ----------
        x_exp : ``numpy array``
            One dimension :doc:`numpy array <numpy:reference/generated/numpy.array>` with the data **ordered**.
        which : ``str``
            The value that should be evaluated.

            * If it is ``"max"`` (or ``None``), the highest value is checked if it is a possible outlier.
            * If it is ``"min"``, the lowest value is checked.

        Notes
        -----
        If ``which=="min"``, the equation used is:

        .. math::

            r_{10} = \\frac{x_2-x_1}{x_n-x_1}

        If ``which=="max"``, the equation used is:

        .. math::

            r_{10} = \\frac{x_n-x_{n-1}}{x_n-x_1}

        References
        ----------
        .. [1] DIXON, W. J. Processing Data for Outliers. Biometrics, v. 9, n. 1, p. 74–89, 1953.


        Examples
        --------

        >>> from pycafee.sample.dixon import Dixon
        >>> import numpy as np
        >>> x_exp = np.array([159, 153, 184, 153, 156, 150, 147])
        >>> x_exp.sort(kind='quicksort')
        >>> teste = Dixon()
        >>> result = teste._r10(x_exp, which="min")
        >>> print(result)
        0.08108108108108109
        >>> result = teste._r10(x_exp, which="max")
        >>> print(result)
        0.6756756756756757


        >>> from pycafee.sample.dixon import Dixon
        >>> import numpy as np
        >>> x_exp = np.array([15.42, 15.51, 15.52, 15.53, 15.68, 15.52, 15.56, 15.53, 15.54, 15.56])
        >>> x_exp.sort(kind='quicksort')
        >>> teste = Dixon()
        >>> result = teste._r10(x_exp, which="min")
        >>> print(result)
        0.34615384615384587
        >>> result = teste._r10(x_exp, which="max")
        >>> print(result)
        0.4615384615384589


        """
        if which == "min":
            _check_dixon_division_by_zero(x_exp, -1, 0, self.language)
            statistic = (x_exp[1] - x_exp[0])/(x_exp[-1]-x_exp[0])
        else:
            _check_dixon_division_by_zero(x_exp, -1, 0, self.language)
            statistic = (x_exp[-1] - x_exp[-2])/(x_exp[-1]-x_exp[0])
        return statistic


    # with tests, with text, with database (Dixon), with docstring
    def _r11(self, x_exp, which):
        """The equation to calculate the Dixon statsitic for the ``r11`` ratio as described at [1]_

        Parameters
        ----------
        x_exp : ``numpy array``
            One dimension :doc:`numpy array <numpy:reference/generated/numpy.array>` with the data **ordered**.
        which : ``str``
            The value that should be evaluated.

            * If it is ``"max"`` (or ``None``), the highest value is checked if it is a possible outlier.
            * If it is ``"min"``, the lowest value is checked.

        Notes
        -----
        If ``which=="min"``, the equation used is:

        .. math::

            r_{11} = \\frac{x_2-x_{1}}{x_{n-1}-x_1}

        If ``which=="max"``, the equation used is:

        .. math::

            r_{11} = \\frac{x_n-x_{n-1}}{x_{n}-x_2}

        References
        ----------
        .. [1] DIXON, W. J. Processing Data for Outliers. Biometrics, v. 9, n. 1, p. 74–89, 1953.


        Examples
        --------

        >>> from pycafee.sample.dixon import Dixon
        >>> import numpy as np
        >>> x_exp = np.array([159, 153, 184, 153, 156, 150, 147])
        >>> x_exp.sort(kind='quicksort')
        >>> teste = Dixon()
        >>> result = teste._r11(x_exp, which="min")
        >>> print(result)
        0.25
        >>> result = teste._r11(x_exp, which="max")
        >>> print(result)
        0.7352941176470589


        >>> from pycafee.sample.dixon import Dixon
        >>> import numpy as np
        >>> x_exp = np.array([15.42, 15.51, 15.52, 15.53, 15.68, 15.52, 15.56, 15.53, 15.54, 15.56])
        >>> x_exp.sort(kind='quicksort')
        >>> teste = Dixon()
        >>> result = teste._r11(x_exp, which="min")
        >>> print(result)
        0.6428571428571392
        >>> result = teste._r11(x_exp, which="max")
        >>> print(result)
        0.7058823529411722



        """
        if which == "min":
            _check_dixon_division_by_zero(x_exp, -2, 0, self.language)
            statistic = (x_exp[1] - x_exp[0])/(x_exp[-2]-x_exp[0])
        else:
            _check_dixon_division_by_zero(x_exp, -1, 1, self.language)
            statistic = (x_exp[-1] - x_exp[-2])/(x_exp[-1]-x_exp[1])
        return statistic


    # with tests, with text, with database (Dixon), with docstring
    def _r12(self, x_exp, which):
        """The equation to calculate the Dixon statsitic for the ``r12`` ratio as described at [1]_

        Parameters
        ----------
        x_exp : ``numpy array``
            One dimension :doc:`numpy array <numpy:reference/generated/numpy.array>` with the data **ordered**.
        which : ``str``
            The value that should be evaluated.

            * If it is ``"max"`` (or ``None``), the highest value is checked if it is a possible outlier.
            * If it is ``"min"``, the lowest value is checked.

        Notes
        -----
        If ``which=="min"``, the equation used is:

        .. math::

            r_{12} = \\frac{x_2-x_{1}}{x_{n-2}-x_1}

        If ``which=="max"``, the equation used is:

        .. math::

            r_{12} = \\frac{x_n-x_{n-1}}{x_{n}-x_3}

        References
        ----------
        .. [1] DIXON, W. J. Processing Data for Outliers. Biometrics, v. 9, n. 1, p. 74–89, 1953.


        Examples
        --------

        >>> from pycafee.sample.dixon import Dixon
        >>> import numpy as np
        >>> x_exp = np.array([159, 153, 184, 153, 156, 150, 147])
        >>> x_exp.sort(kind='quicksort')
        >>> teste = Dixon()
        >>> result = teste._r12(x_exp, which="min")
        >>> print(result)
        0.3333333333333333
        >>> result = teste._r12(x_exp, which="max")
        >>> print(result)
        0.8064516129032258


        >>> from pycafee.sample.dixon import Dixon
        >>> import numpy as np
        >>> x_exp = np.array([15.42, 15.51, 15.52, 15.53, 15.68, 15.52, 15.56, 15.53, 15.54, 15.56])
        >>> x_exp.sort(kind='quicksort')
        >>> teste = Dixon()
        >>> result = teste._r12(x_exp, which="min")
        >>> print(result)
        0.6428571428571392
        >>> result = teste._r12(x_exp, which="max")
        >>> print(result)
        0.7499999999999944




        """
        if which == "min":
            _check_dixon_division_by_zero(x_exp, -3, 0, self.language)
            statistic = (x_exp[1] - x_exp[0])/(x_exp[-3]-x_exp[0])
        else:
            _check_dixon_division_by_zero(x_exp, -1, 2, self.language)
            statistic = (x_exp[-1] - x_exp[-2])/(x_exp[-1]-x_exp[2])
        return statistic


    # with tests, with text, with database (Dixon), with docstring
    def _r20(self, x_exp, which):
        """The equation to calculate the Dixon statsitic for the ``r20`` ratio as described at [1]_

        Parameters
        ----------
        x_exp : ``numpy array``
            One dimension :doc:`numpy array <numpy:reference/generated/numpy.array>` with the data **ordered**.
        which : ``str``
            The value that should be evaluated.

            * If it is ``"max"`` (or ``None``), the highest value is checked if it is a possible outlier.
            * If it is ``"min"``, the lowest value is checked.

        Notes
        -----
        If ``which=="min"``, the equation used is:

        .. math::

            r_{20} = \\frac{x_3-x_{1}}{x_{n}-x_1}

        If ``which=="max"``, the equation used is:

        .. math::

            r_{20} = \\frac{x_n-x_{n-2}}{x_{n}-x_1}

        References
        ----------
        .. [1] DIXON, W. J. Processing Data for Outliers. Biometrics, v. 9, n. 1, p. 74–89, 1953.


        Examples
        --------

        >>> from pycafee.sample.dixon import Dixon
        >>> import numpy as np
        >>> x_exp = np.array([159, 153, 184, 153, 156, 150, 147])
        >>> x_exp.sort(kind='quicksort')
        >>> teste = Dixon()
        >>> result = teste._r20(x_exp, which="min")
        >>> print(result)
        0.16216216216216217
        >>> result = teste._r20(x_exp, which="max")
        >>> print(result)
        0.7567567567567568


        >>> from pycafee.sample.dixon import Dixon
        >>> import numpy as np
        >>> x_exp = np.array([15.42, 15.51, 15.52, 15.53, 15.68, 15.52, 15.56, 15.53, 15.54, 15.56])
        >>> x_exp.sort(kind='quicksort')
        >>> teste = Dixon()
        >>> result = teste._r20(x_exp, which="min")
        >>> print(result)
        0.3846153846153836
        >>> result = teste._r20(x_exp, which="max")
        >>> print(result)
        0.4615384615384589


        """
        if which == "min":
            _check_dixon_division_by_zero(x_exp, -1, 0, self.language)
            statistic = (x_exp[2] - x_exp[0])/(x_exp[-1]-x_exp[0])
        else:
            _check_dixon_division_by_zero(x_exp, -1, 0, self.language)
            statistic = (x_exp[-1] - x_exp[-3])/(x_exp[-1]-x_exp[0])
        return statistic


    # with tests, with text, with database (Dixon), with docstring
    def _r21(self, x_exp, which):
        """The equation to calculate the Dixon statsitic for the ``r21`` ratio as described at [1]_

        Parameters
        ----------
        x_exp : ``numpy array``
            One dimension :doc:`numpy array <numpy:reference/generated/numpy.array>` with the data **ordered**.
        which : ``str``
            The value that should be evaluated.

            * If it is ``"max"`` (or ``None``), the highest value is checked if it is a possible outlier.
            * If it is ``"min"``, the lowest value is checked.

        Notes
        -----
        If ``which=="min"``, the equation used is:

        .. math::

            r_{21} = \\frac{x_3-x_{1}}{x_{n-1}-x_1}

        If ``which=="max"``, the equation used is:

        .. math::

            r_{21} = \\frac{x_n-x_{n-2}}{x_{n}-x_2}

        References
        ----------
        .. [1] DIXON, W. J. Processing Data for Outliers. Biometrics, v. 9, n. 1, p. 74–89, 1953.


        Examples
        --------

        >>> from pycafee.sample.dixon import Dixon
        >>> import numpy as np
        >>> x_exp = np.array([159, 153, 184, 153, 156, 150, 147])
        >>> x_exp.sort(kind='quicksort')
        >>> teste = Dixon()
        >>> result = teste._r21(x_exp, which="min")
        >>> print(result)
        0.5
        >>> result = teste._r21(x_exp, which="max")
        >>> print(result)
        0.8235294117647058


        >>> from pycafee.sample.dixon import Dixon
        >>> import numpy as np
        >>> x_exp = np.array([15.42, 15.51, 15.52, 15.53, 15.68, 15.52, 15.56, 15.53, 15.54, 15.56])
        >>> x_exp.sort(kind='quicksort')
        >>> teste = Dixon()
        >>> result = teste._r21(x_exp, which="min")
        >>> print(result)
        0.7142857142857089
        >>> result = teste._r21(x_exp, which="max")
        >>> print(result)
        0.7058823529411722

        """
        if which == "min":
            _check_dixon_division_by_zero(x_exp, -2, 0, self.language)
            statistic = (x_exp[2] - x_exp[0])/(x_exp[-2]-x_exp[0])
        else:
            _check_dixon_division_by_zero(x_exp, -1, 1, self.language)
            statistic = (x_exp[-1] - x_exp[-3])/(x_exp[-1]-x_exp[1])
        return statistic


    # with tests, with text, with database (Dixon), with docstring
    def _r22(self, x_exp, which):
        """The equation to calculate the Dixon statsitic for the ``r22`` ratio as described at [1]_

        Parameters
        ----------
        x_exp : ``numpy array``
            One dimension :doc:`numpy array <numpy:reference/generated/numpy.array>` with the data **ordered**.
        which : ``str``
            The value that should be evaluated.

            * If it is ``"max"`` (or ``None``), the highest value is checked if it is a possible outlier.
            * If it is ``"min"``, the lowest value is checked.

        Notes
        -----
        If ``which=="min"``, the equation used is:

        .. math::

            r_{22} = \\frac{x_3-x_{1}}{x_{n-2}-x_1}

        If ``which=="max"``, the equation used is:

        .. math::

            r_{22} = \\frac{x_n-x_{n-2}}{x_{n}-x_3}

        References
        ----------
        .. [1] DIXON, W. J. Processing Data for Outliers. Biometrics, v. 9, n. 1, p. 74–89, 1953.


        Examples
        --------

        >>> from pycafee.sample.dixon import Dixon
        >>> import numpy as np
        >>> x_exp = np.array([159, 153, 184, 153, 156, 150, 147])
        >>> x_exp.sort(kind='quicksort')
        >>> teste = Dixon()
        >>> result = teste._r22(x_exp, which="min")
        >>> print(result)
        0.6666666666666666
        >>> result = teste._r22(x_exp, which="max")
        >>> print(result)
        0.9032258064516129


        >>> from pycafee.sample.dixon import Dixon
        >>> import numpy as np
        >>> x_exp = np.array([15.42, 15.51, 15.52, 15.53, 15.68, 15.52, 15.56, 15.53, 15.54, 15.56])
        >>> x_exp.sort(kind='quicksort')
        >>> teste = Dixon()
        >>> result = teste._r22(x_exp, which="min")
        >>> print(result)
        0.7142857142857089
        >>> result = teste._r22(x_exp, which="max")
        >>> print(result)
        0.7499999999999944


        """
        if which == "min":
            _check_dixon_division_by_zero(x_exp, -3, 0, self.language)
            statistic = (x_exp[2] - x_exp[0])/(x_exp[-3]-x_exp[0])
        else:
            _check_dixon_division_by_zero(x_exp, -1, 2, self.language)
            statistic = (x_exp[-1] - x_exp[-3])/(x_exp[-1]-x_exp[2])
        return statistic

    # with tests, with text, with database (Dixon), with docstring
    def __str__(self):
        if self.conclusion is None:
            fk_id_function = management._query_func_id("generic")
            messages = management._get_messages(fk_id_function, self.language, "generic")
            return f"{messages[2][0][0]} Dixon {messages[2][2][0]}"
        else:
            return self.conclusion

    # with tests, with text, with database (Dixon), with docstring
    def __repr__(self):
        fk_id_function = management._query_func_id("Dixon")
        messages = management._get_messages(fk_id_function, self.language, "Dixon")
        return messages[12][0][0]



class Grubbs(AlphaManagement, NDigitsManagement):
    """This class instantiates an object to apply the Grubbs test for detecting oultliers

    """

    GRUBBS_ONE_TABLE = {
        "n_rep" : [
                    3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
                    ],
        0.10 : [
                1.153, 1.463, 1.672, 1.822, 1.938, 2.032, 2.110, 2.176, 2.234, 2.285, 2.331, 2.371, 2.409, 2.443, 2.475, 2.504, 2.532, 2.557, 2.580, 2.603, 2.624, 2.644, 2.663, 2.681, 2.698, 2.714, 2.730, 2.745
                ],
        0.05 : [
                1.155, 1.481, 1.715, 1.887, 2.020, 2.126, 2.215, 2.290, 2.355, 2.412, 2.462, 2.507, 2.549, 2.585, 2.620, 2.651, 2.681, 2.709, 2.733, 2.758, 2.781, 2.802, 2.822, 2.841, 2.859, 2.876, 2.893, 2.908
                ],
        0.01 : [
                1.155, 1.496, 1.764, 1.973, 2.139, 2.274, 2.387, 2.482, 2.564, 2.636, 2.699, 2.755, 2.806, 2.852, 2.894, 2.932, 2.968, 3.001, 3.031, 3.060, 3.087, 3.112, 3.135, 3.157, 3.178, 3.199, 3.218, 3.236
                ]
        }


    GRUBBS_TWO_TABLE = {
        "n_rep" : [
                    3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
                    ],
        0.10 : [
                1.997, 2.409, 2.712, 2.949, 3.143, 3.308, 3.449, 3.57, 3.68, 3.78, 3.87, 3.95, 4.02, 4.09, 4.15, 4.21, 4.27, 4.32
                ],
        0.05 : [
                1.999, 2.429, 2.753, 3.012, 3.222, 3.399, 3.552, 3.685, 3.80, 3.91, 4.00, 4.09, 4.17, 4.24, 4.31, 4.38, 4.43, 4.49,
                ],
        0.01 : [
                2.000, 2.445, 2.803, 3.095, 3.338, 3.543, 3.720, 3.875, 4.012, 4.134, 4.244, 4.34, 4.43, 4.51, 4.59, 4.66, 4.73, 4.79
                ]
        }


    GRUBBS_THREE_TABLE = {
        "n_rep" : [
                    4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
                    ],
        0.10 : [
                0.0008, 0.0183, 0.0564, 0.1020, 0.1478, 0.1909, 0.2305, 0.2667, 0.2996, 0.3295, 0.3568, 0.3818, 0.4048, 0.4259, 0.4455, 0.4636, 0.4804, 0.4961, 0.5107, 0.5244, 0.5373, 0.5495, 0.5609, 0.5717, 0.5819, 0.5916, 0.6008
                ],
        0.05 : [
                0.0002, 0.0090, 0.0349, 0.0708, 0.1101, 0.1492, 0.1864, 0.2213, 0.2537, 0.2836, 0.3112, 0.3367, 0.3603, 0.3822, 0.4025, 0.4214, 0.4391, 0.4556, 0.4711, 0.4857, 0.4994, 0.5123, 0.5245, 0.5360, 0.5470, 0.5574, 0.5672
                ],
        0.01 : [
                0.0000, 0.0018, 0.0116, 0.0308, 0.0563, 0.0851, 0.1150, 0.1448, 0.1738, 0.2016, 0.2280, 0.2530, 0.2767, 0.2990, 0.3200, 0.3398, 0.3585, 0.3761, 0.3927, 0.4085, 0.4234, 0.4376, 0.4510, 0.4638, 0.4759, 0.4875, 0.4985
                ]
        }




    def __init__(self, name=None, alfa=None, language=None, n_digits=None, **kwargs):
        super().__init__(alfa=alfa, language=language, n_digits=n_digits, **kwargs)
        self.conclusion = None
        self.statistic = None
        self.critical = None
        self.x_exp = None


    # with tests, with text, without database, with docstring
    def get_critical_value(self, n_rep, kind=None, alfa=None):
        """This function returns the critical value for the Grubbs [1]_ test.

        Parameters
        ----------
        n_rep : ``int``
            The total number of observations (``3 <= n_rep <= 30``, vary).
        kind : ``str``, optional
            The type of the test.

            * If ``kind="one"`` (or ``None``), the function returns the critical value for :math:`G^{'}`
            * If ``kind="two"``, the function returns the critical value for :math:`G^{''}`
            * If ``kind="three"``, the function returns the critical value for :math:`G^{'''}`


        alfa : ``float``
            The significance level (``0.10``, ``0.05`` (default) or ``0.01``)

        Returns
        -------
        result : ``tuple`` with:
            critical : ``float``
                The critical value.
            alfa : ``float``
                The corresponding significance level.

        Notes
        -----
        For :math:`G^{'}` (``kind="one"``) the critical values are limited for sample sizes between ``3`` and ``30``. For larger sample size, check [2]_

        For :math:`G^{''}` (``kind="two"``) the critical values are limited for sample sizes between ``3`` and ``20``. For larger sample size, check [3]_.

        For :math:`G^{'''}` (``kind="three"``) the critical values are limited for sample sizes between ``4`` and ``30``. For larger sample size, check [2]_.



        References
        ----------
        .. [1] GRUBBS, F. E. Sample Criteria for Testing Outlying Observations. The Annals of Mathematical Statistics, v. 21, n. 1, p. 27–58, 1950.

        .. [2] GRUBBS, F. E.; BECK, G. Extension of Sample Sizes and Percentage Points for Significance Tests of Outlying Observations. Technometrics, v. 14, n. 4, p. 847–854, 1972.

        .. [3] DAVID, H. A.; HARTLEY, H. O.; PEARSON, E. S. The Distribution of the Ratio, in a Single Normal Sample, of Range to Standard Deviation. Biometrika, v. 41, n. 3/4, p. 482–493, 1954.

        Examples
        --------

        **Getting the critical value for 5 samples at 5% significance level for** :math:`G^{'}`

        >>> from pycafee.sample.outliers import Grubbs
        >>> test = Grubbs()
        >>> result = test.get_critical_value(5)
        >>> print(result)
        GrubbsResult(Critical=1.715, alpha=0.05)


        **Getting the critical value for 5 samples at 5% significance level for** :math:`G^{''}`

        >>> from pycafee.sample.outliers import Grubbs
        >>> test = Grubbs()
        >>> result = test.get_critical_value(5, kind="two")
        >>> print(result)
        GrubbsResult(Critical=2.753, alpha=0.05)


        **Getting the critical value for 5 samples at 5% significance level for** :math:`G^{'''}`

        >>> from pycafee.sample.outliers import Grubbs
        >>> test = Grubbs()
        >>> result = test.get_critical_value(5, kind="three")
        >>> print(result)
        GrubbsResult(Critical=0.009, alpha=0.05)



        """

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

        ### checking the ratio ###
        if kind is None:
            kind = "one"
        else:
            checkers._check_is_str(kind, "kind", language=self.language)


        checkers._check_value_is_equal_or_lower_than(n_rep, "n_rep", 30, language=self.language)
        if kind == "one":
            checkers._check_value_is_equal_or_higher_than(n_rep, "n_rep", 3, language=self.language)
            table_data = Grubbs.GRUBBS_ONE_TABLE
        elif kind == "two":
            checkers._check_value_is_equal_or_higher_than(n_rep, "n_rep", 3, language=self.language)
            checkers._check_value_is_equal_or_lower_than(n_rep, "n_rep", 20, language=self.language)
            table_data = Grubbs.GRUBBS_TWO_TABLE
        elif kind == "three":
            checkers._check_value_is_equal_or_higher_than(n_rep, "n_rep", 4, language=self.language)
            table_data = Grubbs.GRUBBS_THREE_TABLE
        else:
            fk_id_function = management._query_func_id("Grubbs")
            messages = management._get_messages(fk_id_function, self.language, "Grubbs")
            try:
                error = messages[1][0][0]
                raise ValueError(error)
            except ValueError:
                allowed_ratios = ["one", "two", "three"]
                kinds = [f"    --->    '{allowed}'" for allowed in allowed_ratios]
                msg = [
                    f"{messages[2][0][0]} '{kind}'.",
                    f"{messages[2][2][0]}:",
                    kinds
                    ]
                flat_list = general._flatten_list_of_list_string(msg)
                flat_list = list(flat_list)
                general._display_n_line_attention(
                    flat_list
                )
                raise

        # Checking if the alfa value is valid #
        if alfa not in table_data.keys():
            fk_id_function = management._query_func_id("Grubbs")
            messages = management._get_messages(fk_id_function, self.language, "Grubbs")
            try:
                error = messages[1][0][0]
                raise ValueError(error)
            except ValueError:
                fk_id_function = management._query_func_id("generic")
                messages = management._get_messages(fk_id_function, self.language, "generic")
                msg = [f"{messages[4][0][0]} 'alfa' {messages[4][2][0]}:"]
                values = ['0.01', '0.05', '0.10']
                for item in values:
                    msg.append(f"   --->    {item}")
                msg.append(f"{messages[4][4][0]}:")
                msg.append(f"   --->    {alfa}")
                general._display_n_line_attention(msg)
                raise




        ### getting the critical value ###
        critical = table_data[alfa][n_rep-table_data['n_rep'][0]]

        ### quering
        fk_id_function = management._query_func_id("generic")
        messages = management._get_messages(fk_id_function, self.language, "generic")

        ### making the named tuple
        name = "Grubbs" + messages[1][0][0]
        result = namedtuple(name, (messages[1][1][0], messages[1][2][0]))
        return result(critical, alfa)



    # with tests, with text, without database, with docstring
    def fit(self, x_exp, kind=None, which=None, alfa=None, details=None):
        """This function applies the Grubbs test to identify outliers in Normal data with a few samples [1]_.

        Parameters
        ----------
        x_exp : ``numpy array``
            One dimension :doc:`numpy array <numpy:reference/generated/numpy.array>` with at least ``3`` sample data (vary).
        kind : ``str``, optional
            The type of the test.

            * If ``kind="one"`` (or ``None``), the function returns the critical value for :math:`G^{'}`
            * If ``kind="two"``, the function returns the critical value for :math:`G^{''}`
            * If ``kind="three"``, the function returns the critical value for :math:`G^{'''}`

        alfa : ``float``
            The significance level (``0.10``, ``0.05`` (default) or ``0.01``)
        details : ``str``, optional
            The ``details`` parameter determines the amount of information presented about the hypothesis test.

            * If ``details = "short"`` (or ``None``, e.g, the default), a simplified version of the test result is returned.
            * If ``details = "full"``, a detailed version of the hypothesis test result is returned.
            * if ``details = "binary"``, the conclusion will be ``1`` (:math:`H_0` is rejected) or ``0`` (:math:`H_0` is accepted).

        which : ``str``, optional
            The value that should be evaluated as a possible outlier.

            * If ``which=None`` (default), the possible outlier is automatically inferred as the farthest observation from the mean.
            * If ``which="max"``, the highest value is checked if it is a possible outlier.
            * If ``which="min"``, the lowest value is checked if it is a possible outlier.

            The ``which`` parameter has no effect when ``kind="two"``.

        Returns
        -------
        result : ``tuple`` with
            statistic : ``float``
                The test statistic.
            critical : ``float``
                The critical value.
            alpha : ``float``
                The significance level used.
            kind : ``str``
                The kind parameter used.
            outlier : ``number`` or ``list`` of ``numbers``
                The outlier tested.

                * If ``kind="one"``, a number is returned with the value tested;
                * If ``kind="two"`` or ``kind="three"``, a list with two numbers is returned with the two values tested;

        conclusion : ``str``
            The test conclusion (e.g, Possible outlier/ no outliers).


        See Also
        --------
        get_critical_value
        pycafee.sample.outliers.ZScore.fit
        pycafee.sample.outliers.ModifiedZScore.fit
        pycafee.sample.outliers.Tukey.fit
        pycafee.sample.outliers.Dixon.fit


        Notes
        -----

        The implementation of the **Grubbs test** is done in three different ways. The first implementation (:math:`G^{'}`), checks whether the dataset has a single outlier (``kind="one"``), with the following hypotheses:

        .. admonition:: \u2615

           :math:`H_0:` data **does not have** a outlier.

           :math:`H_1:` data **has** a outlier.

        The conclusion of the test is based on the comparison between the ``critical`` value (at ``ɑ`` significance level) and ``statistic`` of the test:

        .. code:: python

           if critical <= statistic:
               Data does not have a outlier
           else:
               Data has a possible outlier


        For this case, when the possible outlier is the smallest observation in the data set (``which=="min"``), the test ``statistic`` is estimated through the following equation:

        .. math::

            G^{'} = \\frac{\\overline{x}-x_1}{s}

        and when the possible outlier is the highest observation in the data set (``which=="max"``), the test ``statistic`` is estimated through the following equation:

        .. math::

            G^{'} = \\frac{x_n-\\overline{x}}{s}


        The second implementation (:math:`G^{''}`) checks whether the dataset has two outliers (``kind="two"``) each on one side of the distribution (the smallest and largest value), with the following hypotheses:

        .. admonition:: \u2615

           :math:`H_0:` data **does not have** a outlier.

           :math:`H_1:` the minimum and the maximum values are possible outliers.

        The conclusion of the test is based on the comparison between the ``critical`` value (at ``ɑ`` significance level) and ``statistic`` of the test:

        .. code:: python

           if critical <= statistic:
               Data does not have a outlier
           else:
               Data has a outlier


        For this case, the test ``statistic`` is estimated through the following equation:

        .. math::

            G^{''} = \\frac{x_n-x_1}{s}



        The third implementation (:math:`G^{'''}`) checks whether the dataset has two outliers on the same side of the distribution (``kind="three"``), with the following hypotheses:

        .. admonition:: \u2615

           :math:`H_0:` data **does not have** a outlier.

           :math:`H_1:` data **has** two possible outliers.

        The conclusion of the test is based on the comparison between the ``critical`` value (at ``ɑ`` significance level) and ``statistic`` of the test:

        .. code:: python

           if critical > statistic:
               Data does not have a outlier
           else:
               Data has two outliers

        Note that the comparison in this second case is done in reverse to what is usually done in hypothesis testing.


        For this case, when the two possible outliers are the smallest observations in the data set (``which=="min"``), the test ``statistic`` is estimated through the following equation:


        .. math::

            G_{'''} = \\frac{(n-3)\\times s^2_{2 \\; lower}}{(n-1)\\times s^2}



        and when the two possible outliers are the highest observations in the data set (``which=="max"``), the test ``statistic`` is estimated through the following equation:

        .. math::

            G_{'''} = \\frac{(n-3)\\times s^2_{2 \\; upper}}{(n-1)\\times s^2}



        There are critical values for alpha equal to ``0.10``, ``0.05`` and ``0.01``. These values are for the **two-tailed Grubbs distribution** [2]_.

        The minimum and maximum number of samples needed to apply the test varies depending on the ``kind`` parameter. The range for each option is as follows:

        * If ``kind="one"``: ``3<=n<=30``;
        * If ``kind="two"``: ``3<=n<=20``;
        * If ``kind="three"``: ``4<=n<=30``;



        References
        ----------
        .. [1] GRUBBS, F. E. Sample Criteria for Testing Outlying Observations. The Annals of Mathematical Statistics, v. 21, n. 1, p. 27–58, 1950.

        .. [2] GRUBBS, F. E.; BECK, G. Extension of Sample Sizes and Percentage Points for Significance Tests of Outlying Observations. Technometrics, v. 14, n. 4, p. 847–854, 1972.

        Examples
        --------

        **Checking if the highest observation is a possible outlier at a 95% of confidence level**

        >>> from pycafee.sample.outliers import Grubbs
        >>> import numpy as np
        >>> x = np.array([159, 153, 184, 153, 156, 150, 147])
        >>> test = Grubbs()
        >>> result, conclusion = test.fit(x)
        >>> print(result)
        GrubbsResult(Statistic=2.1532047136140045, Critical=2.02, alpha=0.05, kind='one', outlier=184)
        >>> print(conclusion)
        The sample 184 perhaps be an outlier (95.0% confidence level)


        **Checking if the highest observation is a possible outlier at a 99% of confidence level**

        >>> from pycafee.sample.outliers import Grubbs
        >>> import numpy as np
        >>> x = np.array([159, 153, 184, 153, 156, 150, 147])
        >>> test = Grubbs()
        >>> result, conclusion = test.fit(x, alfa=0.01, details="full")
        >>> print(result)
        GrubbsResult(Statistic=2.1532047136140045, Critical=2.139, alpha=0.01, kind='one', outlier=184)
        >>> print(conclusion)
        Since the test statistic (2.153) is higher than the critical value (2.139), we have evidence to reject the null hypothesis, and perhaps sample 184 is an outlier (99.0% confidence level)


        **Checking if the two highest observations are possible outliers at a 95% of confidence level**

        >>> from pycafee.sample.outliers import Grubbs
        >>> import numpy as np
        >>> x = np.array([159, 153, 184, 153, 156, 150, 147, 186])
        >>> test = Grubbs()
        >>> result, conclusion = test.fit(x, kind="three", details="full")
        >>> print(result)
        GrubbsResult(Statistic=0.05528255528255528, Critical=0.1101, alpha=0.05, kind='three', outlier=[184, 186])
        >>> print(conclusion)
        Since the test statistic (0.055) is lower than the critical value (0.11), we have evidence to reject the null hypothesis, and perhaps sample 184 and 186 are outliers (95.0% confidence level)


        **Checking if the highest and the lowest observations are possible outliers at a 95% of confidence level**

        >>> from pycafee.sample.outliers import Grubbs
        >>> import numpy as np
        >>> x = np.array([159, 153, 184, 153, 156, 150, 147, 140])
        >>> test = Grubbs()
        >>> result, conclusion = test.fit(x, kind="two", details="full")
        >>> print(result)
        GrubbsResult(Statistic=3.3896333493939195, Critical=3.399, alpha=0.05, kind='two', outlier=[140, 184])
        >>> print(conclusion)
        As the test statistic (3.389) is lower than the critical value (3.399), we have no evidence to reject the null hypothesis that the sample does not contain outliers (95.0% confidence level)



        """


        ### getting the default alpha value ###
        if alfa is None:
            alfa = self.alfa
        else:
            checkers._check_is_float(alfa, "alfa", self.language)
            checkers._check_data_in_range(alfa, "alfa", 0.0, 1.0, self.language)
            self.alfa = alfa


        ### checking input data ###
        checkers._check_is_numpy_1_D(x_exp, "x_exp", self.language)
        self.x_exp = x_exp

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
                    error = messages[1][0][0]
                    raise ValueError(error)
                except ValueError:
                    general._display_one_line_attention(f"{messages[2][0][0]} '{details}'")
                    raise

        # finding the n_rep
        n_rep = x_exp.size
        checkers._check_value_is_equal_or_lower_than(n_rep, "n_rep", 30, language=self.language)

        ### checking the ratio and getting the critical value ###
        if kind == None or kind == "one":
            kind = "one"
            checkers._check_value_is_equal_or_higher_than(n_rep, "n_rep", 3, language=self.language)

        elif kind == "two":
            checkers._check_value_is_equal_or_higher_than(n_rep, "n_rep", 3, language=self.language)

        elif kind == "three":
            checkers._check_value_is_equal_or_higher_than(n_rep, "n_rep", 4, language=self.language)

        else:
            checkers._check_is_str(kind, "kind", language=self.language)
            fk_id_function = management._query_func_id("Grubbs")
            messages = management._get_messages(fk_id_function, self.language, "Grubbs")
            try:
                error = messages[1][0][0]
                raise ValueError(error)
            except ValueError:
                allowed_ratios = ["one", "two", "three"]
                kinds = [f"    --->    '{allowed}'" for allowed in allowed_ratios]
                msg = [
                    f"{messages[2][0][0]} '{kind}'.",
                    f"{messages[2][2][0]}:",
                    kinds
                    ]
                flat_list = general._flatten_list_of_list_string(msg)
                flat_list = list(flat_list)
                general._display_n_line_attention(
                    flat_list
                )
                raise

        # ordenando os dados
        x_exp = np.sort(x_exp, kind='quicksort')


        ### checking the which ###
        if which is None:
            which = _check_outermost_observation(x_exp)
        else:
            checkers._check_is_str(which, "which", language=self.language)
            if which not in ["min", "max"]:
                fk_id_function = management._query_func_id("Dixon")
                messages = management._get_messages(fk_id_function, self.language, "Dixon")
                try:
                    error = messages[9][0][0]
                    raise ValueError(error)
                except ValueError:
                    general._display_one_line_attention(f"{messages[9][1][0]} '{which}'")
                    raise

        # quering
        fk_id_function = management._query_func_id("Grubbs")
        messages = management._get_messages(fk_id_function, self.language, "Grubbs")


        aceita = 0
        rejeita = 1


        if kind == "one":
            if which == "min":
                outlier = x_exp[0]
            else:
                outlier = x_exp[-1]
            # getting the statistic
            statistic = self._one(x_exp, which)
            critical = self.get_critical_value(n_rep=x_exp.size, kind=kind, alfa=alfa)[0]

            if statistic <= critical:
                if details == "short":
                    conclusion = f"{messages[6][0][0]}{100*(1-alfa)}{messages[6][2][0]}"
                elif details == "full":
                    conclusion = f"{messages[7][0][0]}{helpers._truncate(statistic, language=self.language, decs=self.n_digits)}{messages[7][2][0]}{helpers._truncate(critical, language=self.language, decs=self.n_digits)}{messages[7][4][0]}{100*(1-alfa)}{messages[7][6][0]}"
                else:
                    conclusion = aceita
            else:
                if details == "short":
                    conclusion = f"{messages[8][0][0]} {outlier} {messages[8][2][0]}{100*(1-alfa)}{messages[8][4][0]}"
                elif details == "full":
                    conclusion = f"{messages[9][0][0]}{helpers._truncate(statistic, language=self.language, decs=self.n_digits)}{messages[9][2][0]}{helpers._truncate(critical, language=self.language, decs=self.n_digits)}{messages[9][4][0]} {outlier} {messages[9][6][0]}{100*(1-alfa)}{messages[9][8][0]}"
                else:
                    conclusion = rejeita

        elif kind == "two":
            outlier = [x_exp[0], x_exp[-1]]
            # getting the statistic
            statistic = self._two(x_exp)
            critical = self.get_critical_value(n_rep=x_exp.size, kind=kind, alfa=alfa)[0]

            if statistic <= critical:
                if details == "short":
                    conclusion = f"{messages[6][0][0]}{100*(1-alfa)}{messages[6][2][0]}"
                elif details == "full":
                    conclusion = f"{messages[7][0][0]}{helpers._truncate(statistic, language=self.language, decs=self.n_digits)}{messages[7][2][0]}{helpers._truncate(critical, language=self.language, decs=self.n_digits)}{messages[7][4][0]}{100*(1-alfa)}{messages[7][6][0]}"
                else:
                    conclusion = aceita
            else:
                if details == "short":
                    conclusion = f"{messages[10][0][0]} {outlier[0]} {messages[10][2][0]} {outlier[1]} {messages[10][4][0]}{100*(1-alfa)}{messages[10][6][0]}"
                elif details == "full":
                    conclusion = f"{messages[13][0][0]}{helpers._truncate(statistic, language=self.language, decs=self.n_digits)}{messages[13][2][0]}{helpers._truncate(critical, language=self.language, decs=self.n_digits)}{messages[13][4][0]} {outlier[0]} {messages[13][6][0]} {outlier[1]} {messages[13][8][0]}{100*(1-alfa)}{messages[13][10][0]}"
                else:
                    conclusion = rejeita


        else:
            if which == "min":
                outlier = [x_exp[0], x_exp[1]]
            else:
                outlier = [x_exp[-2], x_exp[-1]]
            # getting the statistic
            statistic = self._three(x_exp, which)
            critical = self.get_critical_value(n_rep=x_exp.size, kind=kind, alfa=alfa)[0]

            if statistic > critical:
                if details == "short":
                    conclusion = f"{messages[6][0][0]}{100*(1-alfa)}{messages[6][2][0]}"
                elif details == "full":
                    conclusion = f"{messages[12][0][0]}{helpers._truncate(statistic, language=self.language, decs=self.n_digits)}{messages[12][2][0]}{helpers._truncate(critical, language=self.language, decs=self.n_digits)}{messages[12][4][0]}{100*(1-alfa)}{messages[12][6][0]}"
                else:
                    conclusion = aceita
            else:
                if details == "short":
                    conclusion = f"{messages[10][0][0]} {outlier[0]} {messages[10][2][0]} {outlier[1]} {messages[10][4][0]}{100*(1-alfa)}{messages[10][6][0]}"
                elif details == "full":
                    conclusion = f"{messages[11][0][0]}{helpers._truncate(statistic, language=self.language, decs=self.n_digits)}{messages[11][2][0]}{helpers._truncate(critical, language=self.language, decs=self.n_digits)}{messages[11][4][0]} {outlier[0]} {messages[11][6][0]} {outlier[1]} {messages[11][8][0]}{100*(1-alfa)}{messages[11][10][0]}"
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
        name = "Grubbs" + messages[1][0][0]
        result = namedtuple(name, (messages[1][3][0], messages[1][1][0], messages[1][2][0], "kind", "outlier"))
        return result(statistic, critical, alfa, kind, outlier), conclusion


    # with tests, with text, without database, with docstring
    def _one(self, x_exp, which):
        """
        This function calculates the statistic for the Grubbs test to check if the sample has **one** outlier as described by Grubbs [1]_ (:math:`G^{'}`)

        Parameters
        ----------
        x_exp : ``numpy array``
            One dimension :doc:`numpy array <numpy:reference/generated/numpy.array>` with the data **ordered**.
        which : ``str``
            The value that should be evaluated.

            * If ``which="max"`` (or ``None``), the highest value is checked if it is a possible outlier.
            * If ``which="min"``, the lowest value is checked if it is a possible outlier.

        Returns
        -------
        statistic : ``float``
            The test statistic


        Notes
        -----
        If ``which=="min"``, the equation used is:

        .. math::

            G^{'} = \\frac{\\overline{x}-x_1}{s}

        If ``which=="max"``, the equation used is:

        .. math::

            G^{'} = \\frac{x_n-\\overline{x}}{s}

        **The data must be ordered.**

        References
        ----------
        .. [1] GRUBBS, F. E. Sample Criteria for Testing Outlying Observations. The Annals of Mathematical Statistics, v. 21, n. 1, p. 27–58, 1950.


        Examples
        --------

        >>> from pycafee.sample.outliers import Grubbs
        >>> import numpy as np
        >>> x_exp = np.array([159, 153, 184, 153, 156, 150, 147])
        >>> x_exp.sort(kind='quicksort')
        >>> test = Grubbs()
        >>> result = test._one(x_exp, which="max")
        >>> print(result)
        2.1532047136140045


        >>> from pycafee.sample.outliers import Grubbs
        >>> import numpy as np
        >>> x_exp = np.array([15.42, 15.51, 15.52, 15.53, 15.68, 15.52, 15.56, 15.53, 15.54, 15.56])
        >>> x_exp.sort(kind='quicksort')
        >>> test = Grubbs()
        >>> result = test._one(x_exp, which="min")
        >>> print(result)
        1.8344557993475004


        """
        _check_grubbs_division_by_zero(x_exp, self.language)
        if which == "min":
            statistic = (np.mean(x_exp) - x_exp[0])/np.std(x_exp, ddof=1)
        else:
            statistic = (x_exp[-1] - np.mean(x_exp))/np.std(x_exp, ddof=1)
        return statistic


    # with tests, with text, without database, with docstring
    def _two(self, x_exp):
        """
        This function calculates the statistic for the Grubbs test to check if the sample has **two** outliers, in each at one end of the distribution (the lowest and highest value at the same time), as described by Grubbs [1]_ (:math:`G^{''}`)

        Parameters
        ----------
        x_exp : ``numpy array``
            One dimension :doc:`numpy array <numpy:reference/generated/numpy.array>` with the data **ordered**.

        Returns
        -------
        statistic : ``float``
            The test statistic


        Notes
        -----
        The equation used to estimate the Grubbs statistic for this case is the following:

        .. math::

            G^{''} = \\frac{x_n-x_1}{s}

        **The data must be ordered.**

        References
        ----------
        .. [1] GRUBBS, F. E. Sample Criteria for Testing Outlying Observations. The Annals of Mathematical Statistics, v. 21, n. 1, p. 27–58, 1950.


        Examples
        --------

        >>> from pycafee.sample.outliers import Grubbs
        >>> import numpy as np
        >>> x_exp = np.array([159, 153, 184, 153, 156, 150, 147])
        >>> x_exp.sort(kind='quicksort')
        >>> test = Grubbs()
        >>> result = test._two(x_exp)
        >>> print(result)
        2.99827968186036


        >>> from pycafee.sample.outliers import Grubbs
        >>> import numpy as np
        >>> x_exp = np.array([15.42, 15.51, 15.52, 15.53, 15.68, 15.52, 15.56, 15.53, 15.54, 15.56])
        >>> x_exp.sort(kind='quicksort')
        >>> test = Grubbs()
        >>> result = test._two(x_exp)
        >>> print(result)
        4.076568442994411


        """
        _check_grubbs_division_by_zero(x_exp, self.language)
        statistic = (x_exp[-1] - x_exp[0])/np.std(x_exp, ddof=1)
        return statistic



    # with tests, with text, without database, with docstring
    def _three(self, x_exp, which):
        """
        This function calculates the statistic for the Grubbs test to check if the sample has **two** outlier on the same side (the two highest or the two lowest observations) as described by Grubbs [1]_ (:math:`G^{'''}`).

        Parameters
        ----------
        x_exp : ``numpy array``
            One dimension :doc:`numpy array <numpy:reference/generated/numpy.array>` with the data **ordered**.
        which : ``str``
            The side that should be evaluated.

            * If ``which"max"`` (or ``None``), the two highest values are checked if they are possible outliers
            * If ``which"min"``, the two lowest values are checked if they are possible outliers

        Returns
        -------
        statistic : ``float``
            The test statistic

        Notes
        -----
        If ``which=="min"``, the equation used is:

        .. math::

            G^{'''} = \\frac{(n-3)\\times s^2_{2 \\; lower}}{(n-1)\\times s^2}

        where :math:`s^2_{2 \\; lower}` is the sample variance disregarding the two samples suspected of being outliers (the two lowest values)


        If ``which=="max"``, the equation used is:

        .. math::

            G^{'''} = \\frac{(n-3)\\times s^2_{2 \\; upper}}{(n-1)\\times s^2}

        where :math:`s^2_{2 \\; upper}` is the sample variance disregarding the two samples suspected of being outliers (the two highest values)

        **The data must be ordered.**

        References
        ----------
        .. [1] GRUBBS, F. E. Sample Criteria for Testing Outlying Observations. The Annals of Mathematical Statistics, v. 21, n. 1, p. 27–58, 1950.


        Examples
        --------

        >>> from pycafee.sample.outliers import Grubbs
        >>> import numpy as np
        >>> x_exp = np.array([159, 153, 184, 153, 156, 150, 147])
        >>> x_exp.sort(kind='quicksort')
        >>> test = Grubbs()
        >>> result = test._three(x_exp, which="max")
        >>> print(result)
        0.05121951219512194


        >>> from pycafee.sample.outliers import Grubbs
        >>> import numpy as np
        >>> x_exp = np.array([15.42, 15.51, 15.52, 15.53, 15.68, 15.52, 15.56, 15.53, 15.54, 15.56])
        >>> x_exp.sort(kind='quicksort')
        >>> test = Grubbs()
        >>> result = test._three(x_exp, which="min")
        >>> print(result)
        0.5353728489483768


        """
        _check_grubbs_division_by_zero(x_exp, self.language)
        if which == "min":
            var = np.var(x_exp[2:], ddof=1)
            statistic = (x_exp.size - 3)*var/((x_exp.size-1) * np.var(x_exp, ddof=1))
        else:
            var = np.var(x_exp[:-2], ddof=1)
            statistic = (x_exp.size - 3)*var/((x_exp.size-1) * np.var(x_exp, ddof=1))
        return statistic



    # with tests, with text, with database (Dixon), with docstring
    def __str__(self):
        if self.conclusion is None:
            fk_id_function = management._query_func_id("generic")
            messages = management._get_messages(fk_id_function, self.language, "generic")
            return f"{messages[2][0][0]} Grubbs {messages[2][2][0]}"
        else:
            return self.conclusion

    # with tests, with text, with database, with docstring
    def __repr__(self):
        fk_id_function = management._query_func_id("Grubbs")
        messages = management._get_messages(fk_id_function, self.language, "Grubbs")
        return messages[4][0][0]




# with tests, with text, with database (Dixon), with docstring
def _check_grubbs_division_by_zero(x_exp, language):
    """This function checks if the sample standart deviaation is zero

    Parameters
    ----------
    x_exp : ``numpy array`` (1D)
        One dimension :doc:`numpy array <numpy:reference/generated/numpy.array>`
    language : ``str``
        The language code

    Returns
    -------
    ``True`` if ``std!=0``
    Raises ``ZeroDivisionError`` if ``std!==0``

    Notes
    -----
    The parameter ``x_exp`` isn't checked if it is a ``numpy array``.
    The parameter ``language`` isn't checked if it is a ``str``.


    """

    if np.std(x_exp, ddof=1) < 10e-7:
        fk_id_function = management._query_func_id("Dixon")
        messages = management._get_messages(fk_id_function, language, "Dixon")
        try:
            error = messages[10][0][0]
            raise ZeroDivisionError(error)
        except ZeroDivisionError:
            fk_id_function = management._query_func_id("Grubbs")
            messages = management._get_messages(fk_id_function, language, "Grubbs")
            general._display_one_line_attention(
                messages[5][0][0]
            )
            raise
    return True





# with tests, with text, with database (Dixon), with docstring
def _check_dixon_division_by_zero(x_exp, position_1, position_2, language):
    """This function checks if two values are equal, which leads to a division by 0.

    Parameters
    ----------
    x_exp : ``numpy array`` (1D)
        One dimension :doc:`numpy array <numpy:reference/generated/numpy.array>`
    position_1 : ``int``
        The position of the first element
    position_2 : ``int``
        The position of the second element
    language : ``str``
        The language code

    Returns
    -------
    ``True`` if ``x_exp[position_1] != x_exp[position_2]``
    Raises ``ZeroDivisionError`` if ``x_exp[position_1] == x_exp[position_2]``

    Notes
    -----
    The parameter ``x_exp`` isn't checked if it is a ``numpy array``.
    The parameter ``position_1`` isn't checked if it is a ``int``.
    The parameter ``position_2`` isn't checked if it is a ``int``.
    The parameter ``language`` isn't checked if it is a ``str``.


    """

    if x_exp[position_1] == x_exp[position_2]:
        fk_id_function = management._query_func_id("Dixon")
        messages = management._get_messages(fk_id_function, language, "Dixon")
        try:
            error = messages[10][0][0]
            raise ZeroDivisionError(error)
        except ZeroDivisionError:
            general._display_one_line_attention(
                f"{messages[11][0][0]} '{position_1}' {messages[11][2][0]}{x_exp[position_1]}{messages[11][4][0]} '{position_2}' {messages[11][6][0]}{x_exp[position_2]}{messages[11][8][0]}."
            )
            raise
    return True


















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
