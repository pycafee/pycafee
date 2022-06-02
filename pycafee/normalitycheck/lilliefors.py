"""This module concentrates all constants, methods and classes related to the Lilliefors test.

"""

##########################################
################ Summmary ################
##########################################

# - Lilliefors(AlphaManagement, NDigitsManagement, PlotsManagement)
#         - fit(x_exp, alfa=None, n_digits=None, comparison=None, details=None)
#         - to_csv(file_name=None, sep=",")
#         - to_xlsx(file_name=None, sheet_names=None)
#         - get_critical_value(n_rep, alfa=None)
#         - draw_critical_values(ax=None, export=None, extension=None, file_name=None, dpi=None, decimal_separator=None, local=None)
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
from statsmodels.stats.diagnostic import lilliefors as lilliefors_statsmodel



###### Home made ######

from pycafee.database_management import management
from pycafee.utils import checkers
from pycafee.utils import general
from pycafee.utils import helpers
from pycafee.utils.helpers import AlphaManagement, NDigitsManagement, PlotsManagement

###########################################
################ Functions ################
###########################################

class Lilliefors(AlphaManagement, NDigitsManagement, PlotsManagement):
    """
    This class instantiates an object to perform the Lilliefors Normality test.

    Attributes
    ----------
    alfa : ``float``
        The level of significance.
    language : ``str``
        The language code used for the interface.
    msg : ``str``
        The test result expressed in text.
    n_digits : ``int``
        The number of digits that are displayed.
    p_value : ``float``
        The estimated p-value for the data set.
    statistic : ``float``
        The calculated value of the test statistic.
    critical : ``float``
        The test critical value (tabulated).
    x_exp : ``np.ndarray``
        The experimental data where the test was applied.
    LILLIEFORS_TABLE : ``dict``
        The table with the Lilliefors test critical data.


    Methods
    -------
    fit(x_exp, alfa=None, n_digits=None, comparison=None, details=None)
        Performs the Lilliefors test.
    to_csv(file_name=None, sep=",")
        Exports the results to a pre-formatted csv file.
    to_xlsx(file_name=None, sheet_names=None)
        Exports the results to a pre-formatted xlsx file.
    get_critical_value(n_rep, alfa=None)
        Returns the critical value for a pair of alpha and number of observations.
    draw_critical_values(ax=None, export=None, extension=None, file_name=None, dpi=None, decimal_separator=None, local=None)
        Draws a plot with the critical data.


    """

    LILLIEFORS_TABLE = {
        'n_rep': [
                    4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 30
                ],
        0.01 : [
                    0.417, 0.405, 0.364, 0.348, 0.331, 0.311, 0.294, 0.284, 0.275, 0.268, 0.261, 0.257, 0.250, 0.245, 0.239,
                    0.235, 0.231, 0.203, 0.187
                ],
        0.05 : [
                    0.381, 0.337, 0.319, 0.300, 0.285, 0.271, 0.258, 0.249, 0.242, 0.234, 0.227, 0.220, 0.213, 0.206, 0.200,
                    0.195, 0.190, 0.180, 0.161
                ],
        0.10 : [
                    0.352,  0.315, 0.294, 0.276, 0.261, 0.249, 0.239, 0.230, 0.223, 0.214, 0.207, 0.201, 0.195, 0.189, 0.184,
                    0.179, 0.174, 0.165, 0.144
                ],
        0.15 : [
                    0.319, 0.299, 0.277, 0.258, 0.244, 0.233, 0.224, 0.217, 0.212, 0.202, 0.194, 0.187, 0.182, 0.177, 0.173,
                    0.169, 0.166, 0.153, 0.136
                ],
        0.20 : [
                    0.300, 0.285, 0.265, 0.247, 0.233, 0.223, 0.215, 0.206, 0.199, 0.190, 0.183, 0.177, 0.173, 0.169, 0.166,
                    0.163, 0.160, 0.149, 0.131
                ]
        }

    def __init__(self, alfa=None, language=None, n_digits=None, **kwargs):
        super().__init__(alfa=alfa, language=language, n_digits=n_digits, **kwargs)
        self.msg = None
        self.statistic = None
        self.critical = None
        self.p_value = None
        self.x_exp = None

    # with test, with text, with database, with docstring
    def get_critical_value(self, n_rep, alfa=None, correction=None):
        """This function returns the tabulated value of the Lilliefors test.

        Parameters
        ----------
        n_rep : ``int``
            The total number of observations (``n_rep >= 4``).
        alfa : ``float``, optional
            The significance level (between ``0.0`` and ``0.20``, default = ``0.05``)

        Returns
        -------
        critical : ``float`` or ``None``.
            The critical value for the requested confidence level.
        alfa : ``float``
            The corresponding significance level.

        Notes
        -----

        * For data with sample size between ``21`` and ``24`` (``20 < n_rep < 25``), the critical value returned is the value for ``25`` observations;
        * For data with sample size between ``26`` and ``29`` (``25 < n_rep < 30``), the critical value returned is the value for ``30`` observations;
        * For data with a sample size higher than ``31`` (``n_rep > 30``), the critical value returned is the aproximation proposed by the authors.

        This function has tabulated values for the following confidence levels:

            - 99% (``ɑ = 0.01``);
            - 95% (``ɑ = 0.05``);
            - 90% (``ɑ = 0.10``);
            - 85% (``ɑ = 0.15``);
            - 80% (``ɑ = 0.20``);

        The function returns ``None`` for other confidence levels.


        See also
        --------
        draw_tabulated_values : draw a graph with the original tabulated data.


        References
        ----------
        .. [1] LILLIEFORS, H. W. On the Kolmogorov-Smirnov Test for Normality with Mean and Variance Unknown. Journal of the American Statistical Association, v. 62, n. 318, p. 399–402, 1967. DOI: `10.1080/01621459.1967.10482916 <https://www.tandfonline.com/doi/abs/10.1080/01621459.1967.10482916?journalCode=uasa20>`_.


        Examples
        --------
        **Getting the tabulated value for** ``5%`` **of significance and** ``6`` **observations**

        >>> from pycafee.normalitycheck import Lilliefors
        >>> lilliefors_test = Lilliefors()
        >>> result = lilliefors_test.get_critical_value(6)
        >>> print(result)
        LillieforsResult(tabulate=0.319, alpha=0.05)


        **Getting the tabulated value for** ``1%`` **of significance and** ``10`` **observations**

        >>> from pycafee.normalitycheck import Lilliefors
        >>> lilliefors_test = Lilliefors()
        >>> result = lilliefors_test.get_critical_value(10, alfa=0.10)
        >>> print(result)
        LillieforsResult(tabulate=0.239, alpha=0.1)

        """
        ### quering ###
        fk_id_function = management._query_func_id("get_critical_value")
        messages = management._get_messages(fk_id_function, self.language)


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


        ### checking sample size ###
        if n_rep < 4:
            try:
                error = messages[1][0][0]
                raise ValueError(error)
                # raise ValueError("Error: very small number of observations")
            except ValueError:
                general._display_one_line_attention(f"{messages[2][0][0]} Lilliefors {messages[2][2][0]} '4' {messages[2][4][0]} '{n_rep}'",)
                raise
        lilli_table = Lilliefors.LILLIEFORS_TABLE
        if alfa == 0.01:
            if n_rep < 21:
                tabulated = lilli_table[alfa][n_rep - 4]
            elif 20 < n_rep < 26:
                tabulated = lilli_table[alfa][17]
            elif 25 < n_rep < 31:
                tabulated = lilli_table[alfa][18]
            else:
                tabulated = 1.031/np.sqrt(n_rep)
        elif alfa == 0.05:
            if n_rep < 21:
                tabulated = lilli_table[alfa][n_rep - 4]
            elif 20 < n_rep < 26:
                tabulated = lilli_table[alfa][17]
            elif 25 < n_rep < 31:
                tabulated = lilli_table[alfa][18]
            else:
                tabulated = 0.866/np.sqrt(n_rep)
        elif alfa == 0.10:
            if n_rep < 21:
                tabulated = lilli_table[alfa][n_rep - 4]
            elif 20 < n_rep < 26:
                tabulated = lilli_table[alfa][17]
            elif 25 < n_rep < 31:
                tabulated = lilli_table[alfa][18]
            else:
                tabulated = 0.805/np.sqrt(n_rep)
        elif alfa == 0.15:
            if n_rep < 21:
                tabulated = lilli_table[alfa][n_rep - 4]
            elif 20 < n_rep < 26:
                tabulated = lilli_table[alfa][17]
            elif 25 < n_rep < 31:
                tabulated = lilli_table[alfa][18]
            else:
                tabulated = 0.768/np.sqrt(n_rep)
        elif alfa == 0.20:
            if n_rep < 21:
                tabulated = lilli_table[alfa][n_rep - 4]
            elif 20 < n_rep < 26:
                tabulated = lilli_table[alfa][17]
            elif 25 < n_rep < 31:
                tabulated = lilli_table[alfa][18]
            else:
                tabulated = 0.736/np.sqrt(n_rep)
        else:
            tabulated = None

        name = "Lilliefors" + messages[3][0][0]
        ### return the tabulated value and the graph axis ###
        result = namedtuple(name, (messages[3][1][0], messages[3][2][0]))
        return result(tabulated, alfa)


    # with text, with database, with test, with docstring
    def draw_critical_values(self, ax=None, export=None, extension=None, file_name=None, dpi=None, decimal_separator=None):
        """Draw a plot with the Lilliefors original [1]_ *critical data*.

        Parameters
        ----------
        ax : ``None`` or ``matplotlib.axes.SubplotBase``

            * If ``ax`` is ``None``, a figure is created with a preset design. The other parameters can be used to export the graph.
            * If ``ax`` is a ``matplotlib.axes.SubplotBase``, the function returns a ``matplotlib.axes.SubplotBase`` with the Lilliefors tabulated data. In this case, the other parameters do not affect the graph.

        export : ``bool``, optional
            Whether the graph should be exported (``True``) or not (``False``). The default value is ``None``, which implies ``False``.
        file_name : ``str``, optional
            The file name. Default is ``None`` which results in a file named ``"lilliefors_critical_plot"``.
        extension : ``str``, optional
            The file extension without a dot. Default is ``None`` which results in a ``".png"`` file.
        dpi : ``int`` or ``float``, optional
            The figure pixel density. The default is ``None``, which results in a ``100 dpis`` picture. This parameter must be a number higher than zero.
        decimal_separator : ``str``, optional
            The decimal separator symbol used in the chart. It can be the dot (``None`` or ``'.'``) or the comma (``','``).



        Returns
        -------
        axes : ``matplotlib.axes._subplots.AxesSubplot``
            The axis of the graph.

        Notes
        -----
        To obtain the tabulated values of the Lilliefors test, use:

        .. :code: python
            from pycafee.normalitycheck.lilliefors import Lilliefors
            lilliefors_test = Lilliefors()
            LILLIEFORS_TABLE = lilliefors_test.LILLIEFORS_TABLE
            print(LILLIEFORS_TABLE)

        See also
        --------
        get_lilliefors_tabulated_value : Returns the tabulated value for the Lilliefors test.

        References
        ----------
        .. [1] LILLIEFORS, H. W. On the Kolmogorov-Smirnov Test for Normality with Mean and Variance Unknown. Journal of the American Statistical Association, v. 62, n. 318, p. 399–402, 1967. DOI: `10.1080/01621459.1967.10482916 <https://www.tandfonline.com/doi/abs/10.1080/01621459.1967.10482916?journalCode=uasa20>`_.

        Examples
        --------
        **Using the figure created inside the function**

        >>> from pycafee.normalitycheck.lilliefors import Lilliefors
        >>> lilliefors_test = Lilliefors()
        >>> lilliefors_test.draw_critical_values(export=True)
            The 'lilliefors_critical_plot.png' file has been exported

        .. image:: img/lilliefors_critical_plot.png
           :alt: Graph showing the tabulated values of the Lilieffors test for different alpha values
           :align: center

        **Using a previously created figure**

        >>> import matplotlib.pyplot as plt
        >>> from pycafee.normalitycheck.lilliefors import Lilliefors
        >>> lilliefors_test = Lilliefors(language='pt-br')
        >>> fig, ax = plt.subplots(figsize=(8,6))
        >>> ax = lilliefors_test.draw_critical_values(ax=ax)
        >>> plt.savefig("lilliefors_plot.png")
        >>> plt.show()

        .. image:: img/lilliefors_plot.png
           :alt: Graph showing the tabulated values of the Lilieffors test for different alpha values
           :align: center

        """
        ## export ##
        export = self._get_default_export(export)

        ## extension ##
        extension = self._get_default_extension(extension)

        ## file name ##
        if file_name is None:
            file_name = "lilliefors_critical_plot"
        else:
            checkers._check_is_str(file_name, "file_name", self.language)
            helpers._check_forbidden_character(file_name, "file_name", self.language)


        ## dpi ##
        dpi = self._get_default_dpi(dpi)

        ## decimal_separator ##
        decimal_separator = self._get_default_decimal_separator(decimal_separator)
        checkers._check_is_str(decimal_separator, "decimal_separator", self.language)
        helpers._check_decimal_separator(decimal_separator, self.language)

        ## local ##
        # local = self._get_default_local(local)

        fk_id_function = management._query_func_id("draw_critical_values")
        messages = management._get_messages(fk_id_function, self.language)


        ### The values tabled in a dictionary ###
        lilliefors = Lilliefors.LILLIEFORS_TABLE

        # default_locale = helpers._change_locale(self.language, decimal_separator, local)

        ### Make the plot ###
        if ax is None:
            fig, axes = plt.subplots(figsize=(12,6))
        else:
            checkers._check_is_subplots(ax, "ax", self.language)
            axes = ax
        axes.plot(lilliefors['n_rep'], lilliefors[0.01], marker='o', label=f'{messages[1][0][0]} = 1%')
        axes.plot(lilliefors['n_rep'], lilliefors[0.05], marker='o', label=f'{messages[1][0][0]} = 5%')
        axes.plot(lilliefors['n_rep'], lilliefors[0.10], marker='o', label=f'{messages[1][0][0]} = 10%')
        axes.plot(lilliefors['n_rep'], lilliefors[0.15], marker='o', label=f'{messages[1][0][0]} = 15%')
        axes.plot(lilliefors['n_rep'], lilliefors[0.20], marker='o', label=f'{messages[1][0][0]} = 20%')
        axes.legend()
        axes.set_title(f"{messages[2][0][0]} Lilliefors {messages[2][2][0]}")
        axes.set_xlabel(messages[3][0][0])
        axes.set_ylabel(messages[4][0][0])
        axes.set_xticks([4, 10, 15, 20, 25, 30])


        # decimal separator
        if ax is None:
            axes = helpers._change_decimal_separator_x_axis(fig, axes, decimal_separator)
            axes = helpers._change_decimal_separator_y_axis(fig, axes, decimal_separator)

        ## If show equals True, display the graph ##
        if ax is None:
            fig.tight_layout()
            if export:
                ### Baptism of Fire ###
                exits, file_name = helpers._check_conflicting_filename(file_name, extension, self.language)
                plt.savefig(file_name, dpi=dpi, bbox_inches='tight')
                general._display_one_line_success(f"{messages[5][0][0]} '{file_name}' {messages[5][2][0]}")
            plt.show()

        # helpers._change_locale_back_to_default(default_locale)

        return axes

    # with tests, with text, with database, with NO docstring
    def fit(self, x_exp, alfa=None, comparison=None, details=None):
        """This function is a wraper around ``statsmodels.stats.diagnostic.lilliefors()`` [1]_ to perform the **Lilliefors Normality test**, but with some facilities.

        The main difference between this method and the original one is that this wrap only allows the comparison of a sample with the Normal distribution, using ``dist="norm"``. Also, the method to estimate the p-value is set to table, using ``pvalmethod="table"``. Hence:

        >>> statsmodels.stats.diagnostic(x_exp, dist="norm", pvalmethod="table")

        Parameters
        ----------
        x_exp : ``numpy array``
            One dimension :doc:`numpy array <numpy:reference/generated/numpy.array>` with at least ``4`` sample data.
        alfa : ``float``, optional
            The level of significance (``ɑ``). Default is ``None`` which results in ``0.05`` (``ɑ = 5%``).
        comparison : ``str``, optional
            This parameter determines how to perform the comparison test to evaluate the Normality test.

            * If ``comparison = "critical"`` (or ``None``), the comparison test is performed by comparing the critical value (with ``ɑ`` significance level) with the test statistic.
            * If ``comparison="p-value"``, the comparison test is performed comparing the ``p-value`` with the adopted significance level (``ɑ``).

            **Both results should lead to the same comparison**.
        details : ``str``, optional
            The ``details`` parameter determines the amount of information presented about the hypothesis test.

            * If ``details = "short"`` (or ``None``), a simplified version of the test result is returned.
            * If ``details = "full"``, a detailed version of the hypothesis test result is returned.
            * if ``details = "binary"``, the conclusion will be ``1`` (:math:`H_0` is rejected) or ``0`` (:math:`H_0` is accepted).


        Returns
        -------
        result : ``tuple`` with
            statistic : ``float``
                The test statistic.
            critical : ``float`` or ``None``
                The tabulated value for alpha equal to ``1%``, ``5%``, ``10%``, ``15%`` or ``20%``. Other values will return ``None``.
            p_value : ``float``
                The p-value for the hypothesis test.
        conclusion : ``str`` or ``int``
            The test conclusion (e.g, Normal/ not Normal).


        See Also
        --------

        pycafee.normalitycheck.abdimolin.AbdiMolin.fit
        pycafee.normalitycheck.andersondarling.AndersonDarling.fit
        pycafee.normalitycheck.kolmogorovsmirnov.KolmogorovSmirnov.fit
        pycafee.normalitycheck.shapirowilk.ShapiroWilk.fit


        Notes
        -----
        The critical values [2]_ includes samples with sizes between ``4`` and ``20`` in addition to the values for ``25`` and ``30`` samples, for ``ɑ`` equal to ``1%``, ``5%``, ``10%``, ``15%`` or ``20%``.

        * For data with sample size between ``21`` and ``24`` (``20 < n_rep < 25``), the critical value returned is the value for ``25`` observations;
        * For data with sample size between ``26`` and ``29`` (``25 < n_rep < 30``), the critical value returned is the value for ``30`` observations;
        * For data with a sample size higher than ``31`` (``n_rep > 30``), the critical value returned is the aproximation proposed by the authors.


        The **Lilliefors Normality test** has the following premise:

        .. admonition:: \u2615

           :math:`H_0:` data *comes from Normal* distribution.

           :math:`H_1:` data *does* **not** *come from Normal* distribution.

        By default (``comparison="critical"``), the conclusion is based on the comparison between the ``critical`` value (at ``ɑ`` significance level) and ``statistic`` of the test. In summary:

        .. code:: python

           if critical >= statistic:
               Data is Normal
           else:
               Data is not Normal

        The other option (``comparison="p-value"``) makes the conclusion comparing the ``p-value`` with ``ɑ``:

        .. code:: python

           if p-value >= ɑ:
               Data is Normal
           else:
               Data is not Normal

        If ``comparison="critical"`` and ``ɑ`` is not ``0.01``, ``0.05``, ``0.10``, ``0.15`` or ``0.20``, the function will raise ``ValueError``.


        References
        ----------
        .. [1] STATSMODELS. statsmodels.stats.diagnostic.lilliefors. Available at: `www.statsmodels.org <https://www.statsmodels.org/dev/generated/statsmodels.stats.diagnostic.lilliefors.html>`_. Access on: 10 May. 2022

        .. [2] Hubert W. Lilliefors (1967) On the Kolmogorov-Smirnov Test for Normality with Mean and Variance Unknown, Journal of the American Statistical Association, 62:318, 399-402, DOI: `10.1080/01621459.1967.10482916 <https://www.tandfonline.com/doi/abs/10.1080/01621459.1967.10482916?journalCode=uasa20>`_.


        Examples
        --------

        **Applying the test with default values**

        >>> from pycafee.normalitycheck.lilliefors import Lilliefors
        >>> import scipy.stats as stats
        >>> x = stats.norm.rvs(loc=5, scale=3, size=100, random_state=42)
        >>> li_test = Lilliefors()
        >>> result, conclusion = li_test.fit(x)
        >>> print(result)
        LillieforsResult(Statistic=0.05177647360597687, Critical=0.0866, p_value=0.7370142762533124, Alpha=0.05)
        >>> print(conclusion)
        Data is Normal at a 95.0% of confidence level.


        **Applying the test using the** ``p-value`` **to make the conclusion**

        >>> from pycafee.normalitycheck.lilliefors import Lilliefors
        >>> import scipy.stats as stats
        >>> x = stats.norm.rvs(loc=5, scale=3, size=100, random_state=42)
        >>> li_test = Lilliefors()
        >>> result, conclusion = li_test.fit(x, comparison='p-value')
        >>> print(result)
        LillieforsResult(Statistic=0.05177647360597687, Critical=0.0866, p_value=0.7370142762533124, Alpha=0.05)
        >>> print(conclusion)
        Data is Normal at a 95.0% of confidence level.



        **Applying the test at** ``1%`` **of significance level**

        >>> from pycafee.normalitycheck.lilliefors import Lilliefors
        >>> import numpy as np
        >>> x = np.array([1.90642, 2.22488, 2.10288, 1.69742, 1.52229, 3.15435, 2.61826, 1.98492, 1.42738, 1.99568])
        >>> li_test = Lilliefors()
        >>> result, conclusion = li_test.fit(x, alfa=0.01)
        >>> print(result)
        LillieforsResult(Statistic=0.17709753067016487, Critical=0.294, p_value=0.4976450090923252, Alpha=0.01)
        >>> print(conclusion)
        Data is Normal at a 99.0% of confidence level.


        **Applying the test with a detailed conclusion**


        >>> from pycafee.normalitycheck.lilliefors import Lilliefors
        >>> import numpy as np
        >>> x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        >>> li_test = Lilliefors()
        >>> result, conclusion = li_test.fit(x, alfa=0.10, details="full")
        >>> print(result)
        LillieforsResult(Statistic=0.15459867079959644, Critical=0.239, p_value=0.7104644322958894, Alpha=0.1)
        >>> print(conclusion)
        Since the critical value (0.239) >= statistic (0.154), we have NO evidence to reject the hypothesis of data normality, according to the Lilliefors test at a 90.0% of confidence level.



        **Applying the test using a not Normal data**

        >>> from pycafee.normalitycheck.lilliefors import Lilliefors
        >>> import numpy as np
        >>> x =  np.array([0.8, 1, 1.1, 1.15, 1.15, 1.2, 1.2, 1.2, 1.2, 1.6, 1.8, 2, 2.2, 3, 5, 8.2, 8.4, 8.6, 9])
        >>> li_test = Lilliefors()
        >>> result, conclusion = li_test.fit(x, alfa = 0.05, comparison = "p-value", details="full")
        >>> print(result)
        LillieforsResult(Statistic=0.3072356484569813, Critical=0.195, p_value=0.0009999999999998899, Alpha=0.05)
        >>> print(conclusion)
        Since p-value (0.0) < alpha (0.05), we HAVE evidence to reject the hypothesis of data normality, according to the Lilliefors test at a 95.0% of confidence level.


        """
        fk_id_function = management._query_func_id("normalitycheck_fit")
        messages = management._get_messages(fk_id_function, self.language, "normalitycheck_fit")

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

        ### checking the comparison parameter ###
        if comparison is None:
            comparison = "critical"
        else:
            checkers._check_is_str(comparison, "comparison", self.language)
            if comparison == "critical":
                comparison = "critical"
            elif comparison == "p-value":
                comparison = "p-value"
            else:
                try:
                    error = messages[1][0][0]
                    raise ValueError(error)
                except ValueError:
                    general._display_one_line_attention(f"{messages[15][0][0]} '{comparison}'",)
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
            elif details == "binary":
                details = "binary"
            else:
                try:
                    error = messages[1][0][0]
                    raise ValueError(error)
                except ValueError:
                    general._display_one_line_attention(f"{messages[2][0][0]} '{details}'")
                    raise

        ### checking the correction parameter ###
        # This paramter is checked on self.get_lilliefors_tabulated_value #

        ### getting the tabulated value ###
        result = self.get_critical_value(n_rep=x_exp.size, alfa=alfa)
        critical = result[0] # interessa apenas o primero valor

        ### calculating the test statistic value ###
        statistic, p_value = lilliefors_statsmodel(x_exp, dist='norm', pvalmethod='table')

        aceita = 0
        rejeita = 1

        # ### writing the test comparison ###
        if comparison == "p-value":
            if p_value >= alfa:
                if details == 'full':
                    msg = f"{messages[8][0][0]}{helpers._truncate(p_value, self.language, decs=self.n_digits)}{messages[8][2][0]}{alfa}{messages[8][4][0]} Lilliefors {messages[8][6][0]} {100*(1-alfa)}{messages[8][8][0]}"
                elif details == 'binary':
                    msg = aceita
                else:
                    msg = f"{messages[5][0][0]} {100*(1-alfa)}{messages[5][2][0]}"
            else:
                if details == 'full':
                    msg = f"{messages[9][0][0]}{helpers._truncate(p_value, self.language, decs=self.n_digits)}{messages[9][2][0]}{alfa}{messages[9][4][0]} Lilliefors {messages[9][6][0]} {100*(1-alfa)}{messages[9][8][0]}"
                elif details == 'binary':
                    msg = rejeita
                else:
                    msg = f"{messages[7][0][0]} {100*(1-alfa)}{messages[7][2][0]}"
        else:
            ## The test conclustion based on tabulated value depends on whether tabulated value exists. If not, Raise a error ##
            if critical is None:
                try:
                    error = messages[1][0][0]
                    raise ValueError(error)
                except ValueError:
                    msg = f"{messages[3][0][0]} '{alfa}' {messages[3][2][0]}"
                    p_values = list(Lilliefors.LILLIEFORS_TABLE.keys())
                    p_values.pop(0)
                    alfa_list = [msg]
                    for item in p_values:
                        alfa_list.append(f"   --->    {item}")
                    general._display_n_line_attention(alfa_list)
                    raise
            else: # if there is a tabulated value
                if critical >= statistic:
                    if details == 'full':
                        msg = f"{messages[4][0][0]}{helpers._truncate(critical, self.language, decs=self.n_digits)}{messages[4][2][0]}{helpers._truncate(statistic, self.language, decs=self.n_digits)}{messages[4][4][0]} Lilliefors {messages[4][6][0]} {100*(1-alfa)}{messages[4][8][0]}"
                    elif details == 'binary':
                        msg = aceita
                    else:
                        msg = f"{messages[5][0][0]} {100*(1-alfa)}{messages[5][2][0]}"
                else:
                    if details == 'full':
                        msg = f"{messages[6][0][0]}{helpers._truncate(critical, self.language, decs=self.n_digits)}{messages[6][2][0]}{helpers._truncate(statistic, self.language, decs=self.n_digits)}{messages[6][4][0]} Lilliefors {messages[6][6][0]} {100*(1-alfa)}{messages[6][8][0]}"
                    elif details == 'binary':
                        msg = rejeita
                    else:
                        msg = f"{messages[7][0][0]} {100*(1-alfa)}{messages[7][2][0]}"

        name = "Lilliefors" + messages[10][0][0]
        result = namedtuple(name, (messages[11][0][0], messages[12][0][0], messages[13][0][0], messages[14][0][0]))
        self.msg = msg
        self.statistic = statistic
        self.critical = critical
        self.p_value = p_value
        return result(self.statistic, self.critical, self.p_value, self.alfa), self.msg

    # with tests, with text, with database, with docstring
    def to_xlsx(self, file_name=None, sheet_names=None):
        """This method exports the data to excel type files.

        This function is just a wraper around :doc:`pd.DataFrame.to_excel <pandas:reference/api/pandas.DataFrame.to_excel>` [1]_ to export ``.xlsx`` files.

        Parameters
        ----------
        file_name : ``str``, optional
            The name of the file to be exported, without its extension (default is ``None`` which results in a file name ``'lilliefors.xlsx'``).
        sheet_names : ``list`` of two ``str``, optional
            A ``list`` containing the name of the worksheets where the data will be saved:

                * The first element corresponds to the name of the worksheet where the calculated data will be saved (default is ``None`` which means ``'lilliefors'``).

                * The second element corresponds to the name of the worksheet where the supplied data will be saved (default is ``None`` which means ``'data'``).

        Returns
        -------
        df_list : A list of two pandas DataFrame
            The first element is a ``pd.DataFrame`` with the Lilliefors calculated data.
            The second element is a ``pd.DataFrame`` with the supplied data.

        Notes
        -----
        The ``fit()`` method needs to be applied beforehand.

        If a spreadsheet with the same name already exists in the current directory and this files contains tabs with conflicting names, the new tabs will be inserted into the file with different names, preserving the original data.

        See Also
        --------
        fit : performs the Lilliefors Normality test.


        References
        ----------
        .. [1] pandas. pandas.DataFrame.to_excel function. Available at: `pd.to_excel <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html>`_. Accessed on: 10 May 2022.

        Examples
        --------
        **Export with default settings**

        >>> from pycafee.normalitycheck import Lilliefors
        >>> import numpy as np
        >>> x = np.array([1.90642, 2.22488, 2.10288, 1.69742, 1.52229, 3.15435, 2.61826, 1.98492, 1.42738, 1.99568])
        >>> lilliefors_test = Lilliefors()
        >>> lilliefors_test.fit(x)
        >>> lilliefors_test.to_xlsx()
            The data has been exported to the 'lilliefors.xlsx' file

        Download the exported file by :download:`clicking here <assets/lilliefors.xlsx>`.


        **Export with personalized file name**

        >>> from pycafee.normalitycheck import Lilliefors
        >>> import numpy as np
        >>> x = np.array([1.90642, 2.22488, 2.10288, 1.69742, 1.52229, 3.15435, 2.61826, 1.98492, 1.42738, 1.99568])
        >>> lilliefors_test = Lilliefors()
        >>> lilliefors_test.fit(x)
        >>> lilliefors_test.to_xlsx(file_name="my_data")
            The data has been exported to the 'my_data.xlsx' file


        Download the exported file by :download:`clicking here <assets/my_data.xlsx>`.

        **Export with personalized sheet name**

        >>> from pycafee.normalitycheck import Lilliefors
        >>> import numpy as np
        >>> x = np.array([1.90642, 2.22488, 2.10288, 1.69742, 1.52229, 3.15435, 2.61826, 1.98492, 1.42738, 1.99568])
        >>> lilliefors_test = Lilliefors()
        >>> lilliefors_test.fit(x)
        >>> lilliefors_test.to_xlsx(file_name="lilliefors_test", sheet_names=["sample", "data"])
            The data has been exported to the 'lilliefors_test.xlsx' file

        Download the exported file by :download:`clicking here <assets/lilliefors_test.xlsx>`.

        """
        if self.msg is None:
            fk_id_function = management._query_func_id("Lilliefors")
            messages = management._get_messages(fk_id_function, self.language)
            general._display_one_line_attention(messages[1][0][0])
        else:
            # quering
            fk_id_function = management._query_func_id("to_xlsx")
            messages = management._get_messages(fk_id_function, self.language)

            # batizando o nome do arquivo
            if file_name is None:
                file_name = "lilliefors"
            else:
                checkers._check_is_str(file_name, 'file_name', self.language)
                helpers._check_forbidden_character(file_name, "file_name", self.language)
            ## verificando o sheet_names
            if sheet_names is None:
                sheet_names = [
                    "lilliefors",
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
            name = "Lilliefors" + messages[4][0][0]
            df = pd.DataFrame(columns=[messages[3][0][0], name])
            df[messages[3][0][0]] = [
                        messages[5][0][0],
                        messages[6][0][0],
                        messages[7][0][0],
                        messages[8][0][0],
                        messages[9][0][0],
                        ]

            df[name] = [
                        self.statistic,
                        self.critical,
                        self.p_value,
                        self.alfa,
                        self.msg,
                        ]

            df_list = [df, df_data]
            #
            result = helpers._export_to_xlsx(df_list, file_name=file_name, sheet_names=sheet_names, language=self.language)
            return df_list

    # with tests, with text, with database, with docstring
    def to_csv(self, file_name=None, sep=","):
        """Export the data to csv file
        This function is just a wraper around :doc:`pd.DataFrame.to_csv <pandas:reference/api/pandas.DataFrame.to_csv>` [1]_ to export ``.csv`` files.

        Parameters
        ----------
        file_name : ``str``, optional
            The name of the file to be exported, without its extension (default is ``None``, which results in a file named ``'lilliefors.csv'``)
        sep : ``str`` of length 1, optional
            Field delimiter for the output file (default is ``None``, which uses the comma (``','``)). This is the ``sep`` parameter of the ``pd.DataFrame.to_csv()`` pandas method.

        Returns
        -------
        df : ``pd.DataFrame``
            A DataFrame containing the data used to export the ``csv`` file.

        Notes
        -----
        The ``fit()`` method needs to be applied beforehand.

        If there is a file with the same name passed through the ``file_name`` parameter in the current directory, the file will be exported with a different name.

        See Also
        --------
        fit : performs the Lilliefors Normality test.

        References
        ----------
        .. [1] pandas. pandas.DataFrame.to_csv. Available at: `pd.to_csv <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html>`_. Accessed on: 10 May 2022.

        Examples
        --------
        **Export with default settings**

        >>> from pycafee.normalitycheck import Lilliefors
        >>> import numpy as np
        >>> x = np.array([1.90642, 2.22488, 2.10288, 1.69742, 1.52229, 3.15435, 2.61826, 1.98492, 1.42738, 1.99568])
        >>> lilliefors_test = Lilliefors()
        >>> lilliefors_test.fit(x)
        >>> lilliefors_test.to_csv()
            The 'lilliefors.csv' file was exported!


        Download the exported file by :download:`clicking here <assets/lilliefors.csv>`.


        **Export with personalized file name**

        >>> from pycafee.normalitycheck import Lilliefors
        >>> import numpy as np
        >>> x = np.array([1.90642, 2.22488, 2.10288, 1.69742, 1.52229, 3.15435, 2.61826, 1.98492, 1.42738, 1.99568])
        >>> lilliefors_test = Lilliefors()
        >>> lilliefors_test.fit(x)
        >>> lilliefors_test.to_csv(file_name="my_data")
            The 'my_data.csv' file was exported!


        Download the exported file by :download:`clicking here <assets/my_data.csv>`.

        """

        if self.msg is None:
            fk_id_function = management._query_func_id("Lilliefors")
            messages = management._get_messages(fk_id_function, self.language)
            general._display_one_line_attention(messages[1][0][0])

        else:
            # batizando o nome do arquivo
            if file_name is None:
                file_name = "lilliefors"
            else:
                # checking the fle_name
                checkers._check_is_str(file_name, 'file_name', self.language)
                helpers._check_forbidden_character(file_name, "file_name", self.language)

            # quering
            fk_id_function = management._query_func_id("to_csv")
            messages = management._get_messages(fk_id_function, self.language, "to_csv")

            # criando o data frame para exportar via csv
            data_index = list(np.arange(1, self.x_exp.size + 1))
            x_exp = list(self.x_exp)
            name = "Lilliefors" + messages[2][0][0]
            df = pd.DataFrame(columns=[messages[1][0][0], name])
            df[messages[1][0][0]] = [
                        messages[3][0][0],
                        messages[4][0][0],
                        messages[5][0][0],
                        messages[6][0][0],
                        messages[7][0][0],
                        '-',
                        messages[8][0][0],
                        ] + data_index

            df[name] = [
                        self.statistic,
                        self.critical,
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
            fk_id_function = management._query_func_id("Lilliefors")
            messages = management._get_messages(fk_id_function, self.language)
            return messages[1][0][0]
        else:
            return self.msg

    def __repr__(self):
        fk_id_function = management._query_func_id("Lilliefors")
        messages = management._get_messages(fk_id_function, self.language)
        return messages[2][0][0]



# omae no sono konjoo tataki naosu zo https://youtu.be/LcYnfUt6Vvg?t=73
