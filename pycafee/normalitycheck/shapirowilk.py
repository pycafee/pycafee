"""This module concentrates all constants, methods and classes related to the Shapiro Wilk test.

"""

##########################################
################ Summmary ################
##########################################

# - ShapiroWilk(AlphaManagement, NDigitsManagement, PlotsManagement)
#     - __init__(self, alfa=None, language=None, n_digits=None, **kwargs)
#     - get_critical_value(self, n_rep, alfa=None)
#     - draw_critical_values(self, ax=None, export=None, extension=None, file_name=None, dpi=None, decimal_separator=None, local=None)
#     - fit(self, x_exp, alfa=None, n_digits=None, comparison=None, details=None)
#     - to_xlsx(self, file_name=None, sheet_names=None)
#     - to_csv(self, file_name=None, sep=",")
#     - __str__(self)
#     - __repr__(self)

#########################################
################ Imports ################
#########################################

###### Standard ######
from collections import namedtuple


###### Third part ######
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import shapiro as shapiro_scipy


###### Home made ######

from pycafee.database_management import management
from pycafee.utils import checkers
from pycafee.utils import general
from pycafee.utils import helpers
from pycafee.utils.helpers import AlphaManagement, NDigitsManagement, PlotsManagement

###########################################
################ Functions ################
###########################################

class ShapiroWilk(AlphaManagement, NDigitsManagement, PlotsManagement):
    """
    This class instantiates an object to perform the Shapiro Wilk Normality test.

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
    SHAPIRO_WILK_TABLE : ``dict``
        The tabulated data of the Shapiro Wilk test.


    Methods
    -------
    fit(x_exp, alfa=None, n_digits=None, comparison=None, details=None)
        Performs the Shapiro Wilk test.
    to_csv(file_name=None, sep=",")
        Exports the results to a pre-formatted csv file.
    to_xlsx(file_name=None, sheet_names=None)
        Exports the results to a pre-formatted xlsx file.
    get_critical_value(n_rep, alfa=None)
        Finds the tabulated value for a pair of alpha and number of observations
    draw_critical_values(ax=None, export=None, extension=None, file_name=None, dpi=None, decimal_separator=None, local=None)
        Draws a plot with the critical data.

    """

    SHAPIRO_WILK_TABLE = {
        'n_rep': [
                3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
                32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50
                ],
        0.01 : [
                0.753, 0.687, 0.686, 0.713, 0.730, 0.749, 0.764, 0.781, 0.792, 0.805, 0.814, 0.825, 0.835, 0.844, 0.851, 0.858, 0.863, 0.868, 0.873, 0.878, 0.881, 0.884, 0.888, 0.891, 0.894, 0.896, 0.898, 0.900, 0.902, 0.904, 0.906, 0.908, 0.910, 0.912, 0.914, 0.916, 0.917, 0.919, 0.920, 0.922, 0.923, 0.924, 0.926, 0.927, 0.928, 0.929, 0.929, 0.930,
                ],
        0.02 : [
                0.756, 0.707, 0.715, 0.743, 0.760, 0.778, 0.791, 0.806, 0.817, 0.828, 0.837, 0.846, 0.855, 0.863, 0.869, 0.874, 0.879, 0.884, 0.888, 0.892, 0.895, 0.898, 0.901, 0.904, 0.906, 0.908, 0.910, 0.912, 0.914, 0.915, 0.917, 0.919, 0.920, 0.922, 0.924, 0.925, 0.927, 0.928, 0.929, 0.930, 0.932, 0.933, 0.934, 0.935, 0.936, 0.937, 0.937, 0.938
                ],
        0.05 : [
                0.767, 0.748, 0.762, 0.788, 0.803, 0.818, 0.829, 0.842, 0.850, 0.859, 0.866, 0.874, 0.881, 0.887, 0.892, 0.897, 0.901, 0.905, 0.908, 0.911, 0.914, 0.916, 0.918, 0.920, 0.923, 0.924, 0.926, 0.927, 0.929, 0.930, 0.931, 0.933, 0.934, 0.935, 0.936, 0.938, 0.939, 0.940, 0.941, 0.942, 0.943, 0.944, 0.945, 0.945, 0.946, 0.947, 0.947, 0.947
                ],
        0.10 : [
                0.789, 0.792, 0.806, 0.826, 0.838, 0.851, 0.859, 0.869, 0.876, 0.883, 0.889, 0.895, 0.901, 0.906, 0.910, 0.914, 0.917, 0.920, 0.923, 0.926, 0.928, 0.930, 0.931, 0.933, 0.935, 0.936, 0.937, 0.939, 0.940, 0.941, 0.942, 0.943, 0.944, 0.945, 0.946, 0.947, 0.948, 0.949, 0.950, 0.951, 0.951, 0.952, 0.953, 0.953, 0.954, 0.954, 0.955, 0.955
                ],
        0.50 : [
                0.959, 0.935, 0.927, 0.927, 0.928, 0.932, 0.935, 0.938, 0.940, 0.943, 0.945, 0.947, 0.950, 0.952, 0.954, 0.956, 0.957, 0.959, 0.960, 0.961, 0.962, 0.963, 0.964, 0.965, 0.965, 0.966, 0.966, 0.967, 0.967, 0.968, 0.968, 0.969, 0.969, 0.970, 0.970, 0.971, 0.971, 0.972, 0.972, 0.972, 0.973, 0.973, 0.973, 0.974, 0.974, 0.974, 0.974, 0.974
                ],
        0.90 : [
                0.998, 0.987, 0.979, 0.974, 0.972, 0.972, 0.972, 0.972, 0.973, 0.973, 0.974, 0.975, 0.975, 0.976, 0.977, 0.978, 0.978, 0.979, 0.980, 0.980, 0.981, 0.981, 0.981, 0.982, 0.982, 0.982, 0.982, 0.983, 0.983, 0.983, 0.983, 0.983, 0.984, 0.984, 0.984, 0.984, 0.984, 0.985, 0.985, 0.985, 0.985, 0.985, 0.985, 0.985, 0.985, 0.985, 0.985, 0.985
                ],
        0.95 : [
                0.999, 0.992, 0.986, 0.981, 0.979, 0.978, 0.978, 0.978, 0.979, 0.979, 0.979, 0.980, 0.980, 0.981, 0.981, 0.982, 0.982, 0.983, 0.983, 0.984, 0.984, 0.984, 0.985, 0.985, 0.985, 0.985, 0.985, 0.985, 0.986, 0.986, 0.986, 0.986, 0.986, 0.986, 0.987, 0.987, 0.987, 0.987, 0.987, 0.987, 0.987, 0.987, 0.988, 0.988, 0.988, 0.988, 0.988, 0.988
                ],
        0.98 : [
                1.000, 0.996, 0.991, 0.986, 0.985, 0.984, 0.984, 0.983, 0.984, 0.984, 0.984, 0.984, 0.984, 0.985, 0.985, 0.986, 0.986, 0.986, 0.987, 0.987, 0.987, 0.987, 0.988, 0.988, 0.988, 0.988, 0.988, 0.988, 0.988, 0.988, 0.989, 0.989, 0.989, 0.989, 0.989, 0.989, 0.989, 0.989, 0.989, 0.989, 0.990, 0.990, 0.990, 0.990, 0.990, 0.990, 0.990, 0.990
                ],
        0.99 : [
                1.000, 0.997, 0.993, 0.989, 0.988, 0.987, 0.986, 0.986, 0.986, 0.986, 0.986, 0.986, 0.987, 0.987, 0.987, 0.988, 0.988, 0.988, 0.989, 0.989, 0.989, 0.989, 0.989, 0.989, 0.990, 0.990, 0.990, 0.900, 0.990, 0.990, 0.990, 0.990, 0.990, 0.990, 0.990, 0.990, 0.991, 0.991, 0.991, 0.991, 0.991, 0.991, 0.991, 0.991, 0.991, 0.991, 0.991, 0.991
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

    # with tests, with text, with database, with docstring
    def get_critical_value(self, n_rep, alfa=None):
        """This function returns the critical value (tabulated) of the Shapiro Wilk [1]_ test.

        Parameters
        ----------
        alfa : ``float``
            The significance level (between ``0.0`` and ``1.0``, default = ``0.05``)
        n_rep : ``int``
            The total number of observations (``n_rep >= 3``).

        Returns
        -------
        critical : ``float`` or ``None``.
            The critical value for the requested confidence level.
        alfa : ``float``
            The corresponding significance level

        Notes
        -----

        The critical value is returned only if the number of observations is at least ``3`` (``n_rep >= 3``).

        If the number of repetitions is higher than ``50`` (``n_rep > 50``),  the function returns the tabulated value for ``50`` (``n_rep = 50``) observations.

        This function has tabulated values for the following confidence levels [1]_:

            * 99% (ɑ = 0.01);
            * 98% (ɑ = 0.02);
            * 95% (ɑ = 0.05);
            * 90% (ɑ = 0.10);
            * 50% (ɑ = 0.50);

        The function returns ``None`` for other confidence levels.

        See also
        --------
        draw_critical_values : Draws a plot with the critical values for several alpha values.
        fit : performs the Kolmogorov Smirnov Normality test.

        References
        ----------

        .. [1] SHAPIRO, S. S.; WILK, M. B. An Analysis of Variance Test for Normality (Complete Samples). Biometrika, v. 52, n. 3, p. 591–611, 1965. DOI: `10.2307/2333709 <https://doi.org/10.2307/2333709>`_.




        Examples
        --------
        **Getting tabulated value for** ``5%`` **of significance and** ``5`` **observations**

        >>> from pycafee.normalitycheck.shapirowilk import ShapiroWilk
        >>> sw_test = ShapiroWilk()
        >>> critical_value = sw_test.get_critical_value(n_rep=5)
        >>> print(critical_value)
        ShapiroWilkResult(critical=0.762, alpha=0.05)


        **Getting tabulated value for** ``1%`` **of significance and** ``10`` **observations**

        >>> from pycafee.normalitycheck.shapirowilk import ShapiroWilk
        >>> sw_test = ShapiroWilk()
        >>> critical_value = sw_test.get_critical_value(n_rep=10, alfa=0.01)
        >>> print(critical_value)
        ShapiroWilkResult(critical=0.781, alpha=0.01)

        """
        shapiro_wilk_table = ShapiroWilk.SHAPIRO_WILK_TABLE


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

        ### Getting the tabulated values ###
        if n_rep < 3:
            try:
                raise ValueError(messages[1][0][0])
                # raise ValueError("Error: very small number of observations")
            except ValueError:
                general._display_one_line_attention(f"{messages[2][0][0]} Shapiro Wilk {messages[2][2][0]} '3' {messages[2][4][0]} '{n_rep}'",)
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
        name = "ShapiroWilk" + messages[3][0][0]
        result = namedtuple(name, (messages[3][1][0], messages[3][2][0]))
        return result(tabulated, alfa)

    # with tests, with text, with database, with docstring
    def draw_critical_values(self, ax=None, export=None, extension=None, file_name=None, dpi=None, decimal_separator=None):
        """Draw a plot with the Shapiro Wilk *critical data* [1]_.

        Parameters
        ----------
        ax : ``None`` or ``matplotlib.axes.SubplotBase``

            * If ``ax`` is ``None``, a figure is created with a preset design. The other parameters can be used to export the graph.
            * If ``ax`` is a ``matplotlib.axes.SubplotBase``, the function returns a ``matplotlib.axes.SubplotBase`` with the Shapiro Wilk critical data. In this case, the other parameters do not affect the graph.

        export : ``bool``, optional
            Whether the graph should be exported (``True``) or not (``False``). The default value is ``None``, which implies ``False``.
        file_name : ``str``, optional
            The file name. Default is ``None`` which results in a file named ``"shapiro_wilk_critical_plot"``.
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

        To obtain the tabulated values of the Kolmogorov Smirnov test, use:

        >>> from pycafee.normalitycheck.shapirowilk import ShapiroWilk
        >>> sw_test = ShapiroWilk()
        >>> SW_TABLE = sw_test.SHAPIRO_WILK_TABLE
        >>> print(SW_TABLE)


        See also
        --------
        get_critical_value : Returns the critical value.
        fit : performs the Shapiro Wilk Normality test.

        References
        ----------
        .. [1] SHAPIRO, S. S.; WILK, M. B. An Analysis of Variance Test for Normality (Complete Samples). Biometrika, v. 52, n. 3, p. 591–611, 1965. DOI: `10.2307/2333709 <https://doi.org/10.2307/2333709>`_.


        Examples
        --------
        **Using the figure created inside the function**

        >>> from pycafee.normalitycheck.shapirowilk import ShapiroWilk
        >>> sw_test = ShapiroWilk()
        >>> ax = sw_test.draw_critical_values(export=True)
            The 'shapiro_wilk_critical_plot.png' file has been exported

        .. image:: img/shapiro_wilk_critical_plot.png
           :alt: Graph showing the tabulated values of the Shapiro Wilk test for different alpha values
           :align: center

        **Using a previously created figure**

        >>> from pycafee.normalitycheck.shapirowilk import ShapiroWilk
        >>> import matplotlib.pyplot as plt
        >>> sw_test = ShapiroWilk(language='pt-br')
        >>> fig, ax = plt.subplots(figsize=(8,6))
        >>> ax = sw_test.draw_critical_values(ax=ax)
        >>> plt.savefig("sw_plot.png")
        >>> plt.show()


        .. image:: img/sw_plot.png
           :alt: Graph showing the tabulated values of the Kolmogorov Smirnov test for different alpha values
           :align: center

        """
        ## export ##
        export = self._get_default_export(export)

        ## extension ##
        extension = self._get_default_extension(extension)

        ## file name ##
        if file_name is None:
            file_name = "shapiro_wilk_critical_plot"
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
        table = ShapiroWilk.SHAPIRO_WILK_TABLE

        # default_locale = helpers._change_locale(self.language, decimal_separator, local)

        ### Make the plot ###
        if ax is None:
            fig, axes = plt.subplots(figsize=(12,6))
        else:
            checkers._check_is_subplots(ax, "ax", self.language)
            axes = ax
        axes.plot(table['n_rep'], table[0.01], marker='o', label=f'{messages[1][0][0]} = 1%')
        axes.plot(table['n_rep'], table[0.02], marker='o', label=f'{messages[1][0][0]} = 2%')
        axes.plot(table['n_rep'], table[0.05], marker='o', label=f'{messages[1][0][0]} = 5%')
        axes.plot(table['n_rep'], table[0.10], marker='o', label=f'{messages[1][0][0]} = 10%')
        axes.plot(table['n_rep'], table[0.50], marker='o', label=f'{messages[1][0][0]} = 50%')
        axes.plot(table['n_rep'], table[0.90], marker='o', label=f'{messages[1][0][0]} = 90%')
        axes.plot(table['n_rep'], table[0.95], marker='o', label=f'{messages[1][0][0]} = 95%')
        axes.plot(table['n_rep'], table[0.98], marker='o', label=f'{messages[1][0][0]} = 98%')
        axes.plot(table['n_rep'], table[0.99], marker='o', label=f'{messages[1][0][0]} = 99%')
        axes.legend()
        axes.set_title(f"{messages[2][0][0]} Shapiro Wilk {messages[2][2][0]}")
        axes.set_xlabel(messages[3][0][0])
        axes.set_ylabel(messages[4][0][0])
        axes.set_xticks([2, 5, 10, 15, 20, 25, 30, 35])

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

    # with docstring, with text, with database, with test,
    def fit(self, x_exp, alfa=None, comparison=None, details=None):
        """This function is just a wraper around ``scipy.stats.shapiro()`` [1]_ to perform the Shapiro Wilk [2]_ normality test, but with some facilities.

        The test is performed using:

        >>> scipy.stats.shapiro(x_exp)


        Parameters
        ----------
        x_exp : ``numpy array``
            One dimension :doc:`numpy array <numpy:reference/generated/numpy.array>` with at least 3 sample data.
        alfa : ``float``, optional
            The level of significance (``ɑ``). Default is ``None`` which results in ``0.05`` (``ɑ = 5%``).
        comparison : ``str``, optional
            This parameter determines how to perform the comparison test to perform the Normality test.

            * If ``comparison = 'critical'`` (or ``None``, e.g, the default), the comparison test is made between the critical value (with ``ɑ`` significance level) and the calculated value of the test statistic.
            * If ``"p-value"``, the comparison test is performed between the p-value and the adopted significance level (``ɑ``).

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
                The critical value for alpha equal to ``1%``, ``2%``, ``5%``, ``10%`` or ``50%``. Other values will return ``None``.
            p_value : ``float``
                The p-value for the hypothesis test.
        conclusion : ``str``
            The test conclusion (e.g, Normal/ not Normal).

        See Also
        --------
        pycafee.normalitycheck.abdimolin.AbdiMolin.fit
        pycafee.normalitycheck.andersondarling.AndersonDarling.fit
        pycafee.normalitycheck.lilliefors.Lilliefors.fit
        pycafee.normalitycheck.kolmogorovsmirnov.KolmogorovSmirnov.fit


        Notes
        -----
        The tabulated values [2]_ include samples with sizes between ``3`` and ``50``, for ``ɑ`` equal to ``1%``, ``2%``, ``5%``, ``10%``, ``20%`` or ``50%``. For data with a sample size higher than ``50``, the critical value returned is the value for ``n_rep = 50``.

        The **Shapiro Wilk Normality test** has the following premise:

        .. admonition:: \u2615

           :math:`H_0:` data *comes from Normal* distribution.

           :math:`H_1:` data *does* **not** *come from Normal* distribution.

        By default (``comparison = "critical"``), the conclusion is based on the comparison between the ``critical`` value (at ``ɑ`` significance level) and ``statistic`` of the test:

        .. code:: python

           if critical <= statistic:
               Data is Normal
           else:
               Data is not Normal

        Note that the comparison between the critical value and the test statistic is made in the opposite way to what is usually done in most Normality tests.

        The other option (``comparison = "p-value"``) makes the conclusion comparing the ``p-value`` with ``ɑ``:

        .. code:: python

           if p-value >= ɑ:
               Data is Normal
           else:
               Data is not Normal

        If ``comparison = "critical"`` and ``ɑ`` is not ``0.01``, ``0.02``, ``0.05``, ``0.10`` or ``0.50``, the function will raise ``ValueError``.


        References
        ----------
        .. [1] SCIPY. scipy.stats.shapiro. Available at: `www.scipy.org <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html>`_. Access on: 10 May. 2022.

        .. [2] SHAPIRO, S. S.; WILK, M. B. An Analysis of Variance Test for Normality (Complete Samples). Biometrika, v. 52, n. 3, p. 591–611, 1965. DOI: `10.2307/2333709 <https://doi.org/10.2307/2333709>`_.

        Examples
        --------

        **Applying the test with default values**

        >>> from pycafee.normalitycheck.shapirowilk import ShapiroWilk
        >>> import scipy.stats as stats
        >>> x = stats.norm.rvs(loc=5, scale=3, size=100, random_state=42)
        >>> sw_test = ShapiroWilk()
        >>> result, conclusion = sw_test.fit(x)
        >>> print(result)
        ShapiroWilkResult(Statistic=0.9898831844329834, Critical=0.947, p_value=0.6551515460014343, Alpha=0.05)
        >>> print(conclusion)
        Data is Normal at a 95.0% of confidence level.


        **Applying the test using the** ``p-value`` **to make the conclusion**

        >>> from pycafee.normalitycheck.shapirowilk import ShapiroWilk
        >>> import scipy.stats as stats
        >>> x = stats.norm.rvs(loc=5, scale=3, size=100, random_state=42)
        >>> sw_test = ShapiroWilk()
        >>> result, conclusion = sw_test.fit(x, comparison='p-value')
        >>> print(result)
        ShapiroWilkResult(Statistic=0.9898831844329834, Critical=0.947, p_value=0.6551515460014343, Alpha=0.05)
        >>> print(conclusion)
        Data is Normal at a 95.0% of confidence level.


        **Applying the test at** ``1%`` **of significance level**

        >>> from pycafee.normalitycheck.shapirowilk import ShapiroWilk
        >>> import numpy as np
        >>> x = np.array([1.90642, 2.22488, 2.10288, 1.69742, 1.52229, 3.15435, 2.61826, 1.98492, 1.42738, 1.99568])
        >>> sw_test = ShapiroWilk()
        >>> result, conclusion = sw_test.fit(x, alfa=0.01)
        >>> print(result)
        ShapiroWilkResult(Statistic=0.9266945719718933, Critical=0.781, p_value=0.41617822647094727, Alpha=0.01)
        >>> print(conclusion)
        Data is Normal at a 99.0% of confidence level.


        **Applying the test with a detailed conclusion**


        >>> from pycafee.normalitycheck.shapirowilk import ShapiroWilk
        >>> import numpy as np
        >>> x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        >>> sw_test = ShapiroWilk()
        >>> result, conclusion = sw_test.fit(x, alfa=0.10, details="full")
        >>> print(result)
        ShapiroWilkResult(Statistic=0.9698116779327393, Critical=0.869, p_value=0.8890941739082336, Alpha=0.1)
        >>> print(conclusion)
        Since the critical value (0.869) >= statistic (0.969), we have NO evidence to reject the hypothesis of data normality, according to the Shapiro Wilk test at a 90.0% of confidence level.


        **Applying the test using a not Normal data**

        >>> from pycafee.normalitycheck.shapirowilk import ShapiroWilk
        >>> import numpy as np
        >>> x =  np.array([0.8, 1, 1.1, 1.15, 1.15, 1.2, 1.2, 1.2, 1.2, 1.6, 1.8, 2, 2.2, 3, 5, 8.2, 8.4, 8.6, 9])
        >>> sw_test = ShapiroWilk()
        >>> result, conclusion = sw_test.fit(x, alfa = 0.05, comparison = "p-value", details="full")
        >>> print(result)
        ShapiroWilkResult(Statistic=0.7012777924537659, Critical=0.901, p_value=5.757619874202646e-05, Alpha=0.05)
        >>> print(conclusion)
        Since p-value (0.0) < alpha (0.05), we HAVE evidence to reject the hypothesis of data normality, according to the Shapiro Wilk test at a 95.0% of confidence level.



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
                    error = messages[3][0][0]
                    raise ValueError(error)
                except ValueError:
                    general._display_one_line_attention(f"{messages[2][0][0]} '{details}'")
                    raise

        ### getting the tabulated value ###
        result = self.get_critical_value(n_rep=x_exp.size, alfa=alfa)
        critical = result[0] # interessa apenas o primero valor

        ### calculating the test statistic value ###
        # statistic, p_value = kolmolgorov_smirnov_scipy(x_exp, cdf='norm', args=(x_exp.mean(), x_exp.std(ddof=1)), N = x_exp.size)
        statistic, p_value = shapiro_scipy(x_exp)

        aceita = 0
        rejeita = 1

        ### writing the test comparison ###
        if comparison == "p-value":
            if p_value >= alfa:
                if details == 'full':
                    msg = f"{messages[8][0][0]}{helpers._truncate(p_value, self.language, decs=self.n_digits)}{messages[8][2][0]}{alfa}{messages[8][4][0]} Shapiro Wilk {messages[8][6][0]} {100*(1-alfa)}{messages[8][8][0]}"
                elif details == 'binary':
                    msg = aceita
                else:
                    msg = f"{messages[5][0][0]} {100*(1-alfa)}{messages[5][2][0]}"
            else:
                if details == 'full':
                    msg = f"{messages[9][0][0]}{helpers._truncate(p_value, self.language, decs=self.n_digits)}{messages[9][2][0]}{alfa}{messages[9][4][0]} Shapiro Wilk {messages[9][6][0]} {100*(1-alfa)}{messages[9][8][0]}"
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
                    # p_values = list(ShapiroWilk.SHAPIRO_WILK_TABLE.keys())
                    p_values = [0.01, 0.02, 0.05, 0.1, 0.5]
                    alfa_list = [msg]
                    for item in p_values:
                        alfa_list.append(f"   --->    {item}")
                    general._display_n_line_attention(alfa_list)
                    raise
            else: # if there is a tabulated value
                if critical <= statistic:
                    if details == 'full':
                        msg = f"{messages[4][0][0]}{helpers._truncate(critical, self.language, decs=self.n_digits)}{messages[4][2][0]}{helpers._truncate(statistic, self.language, decs=self.n_digits)}{messages[4][4][0]} Shapiro Wilk {messages[4][6][0]} {100*(1-alfa)}{messages[4][8][0]}"
                    elif details == 'binary':
                        msg = aceita
                    else:
                        msg = f"{messages[5][0][0]} {100*(1-alfa)}{messages[5][2][0]}"
                else:
                    if details == 'full':
                        msg = f"{messages[6][0][0]}{helpers._truncate(critical, self.language, decs=self.n_digits)}{messages[6][2][0]}{helpers._truncate(statistic, self.language, decs=self.n_digits)}{messages[6][4][0]} Shapiro Wilk {messages[6][6][0]} {100*(1-alfa)}{messages[6][8][0]}"
                    elif details == 'binary':
                        msg = rejeita
                    else:
                        msg = f"{messages[7][0][0]} {100*(1-alfa)}{messages[7][2][0]}"

        name = "ShapiroWilk" + messages[10][0][0]
        result = namedtuple(name, (messages[11][0][0], messages[12][0][0], messages[13][0][0], messages[14][0][0]))
        self.msg = msg
        self.statistic = statistic
        self.critical = critical
        self.p_value = p_value
        return result(self.statistic, self.critical, self.p_value, self.alfa), self.msg

    # with docstring, with text, with database, with test,
    def to_xlsx(self, file_name=None, sheet_names=None):
        """This method exports the data to excel type files.

        This function is just a wraper around :doc:`pd.DataFrame.to_excel <pandas:reference/api/pandas.DataFrame.to_excel>` [1]_ to export ``.xlsx`` files.

        Parameters
        ----------
        file_name : ``str``, optional
            The name of the file to be exported, without its extension (default is ``None`` which results in a file name ``'shapiro_wilk.xlsx'``).
        sheet_names : ``list`` of two ``str``, optional
            A ``list`` containing the name of the worksheets where the data will be saved:

                * The first element corresponds to the name of the worksheet where the calculated data will be saved (default is ``None`` which means ``'shapiro_wilk'``).

                * The second element corresponds to the name of the worksheet where the supplied data will be saved (default is ``None`` which means ``'data'``).

        Returns
        -------
        df_list : A ``list`` of two pandas DataFrame
            The first element is a ``pd.DataFrame`` with the Kolmogorov Smirnov calculated data.
            The second element is a ``pd.DataFrame`` with the supplied data.

        Notes
        -----
        The ``fit()`` method needs to be applied beforehand.

        If a spreadsheet with the same name already exists in the current directory and this files contains tabs with conflicting names, the new tabs will be inserted into the file with different names, preserving the original data.

        See Also
        --------
        fit : performs the Shapiro Wilk Normality test.

        References
        ----------
        .. [1] pandas. pandas.DataFrame.to_excel function. Available at: `pd.to_excel <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html>`_. Accessed on: 10 May 2022.

        Examples
        --------
        **Export with default settings**

        >>> from pycafee.normalitycheck.shapirowilk import ShapiroWilk
        >>> import numpy as np
        >>> x = np.array([1.90642, 2.22488, 2.10288, 1.69742, 1.52229, 3.15435, 2.61826, 1.98492, 1.42738, 1.99568])
        >>> sw_test = ShapiroWilk()
        >>> sw_test.fit(x)
        >>> sw_test.to_xlsx()
            The data has been exported to the 'shapiro_wilk.xlsx' file

        Download the exported file by :download:`clicking here <assets/shapiro_wilk.xlsx>`.


        **Export with personalized file name**

        >>> from pycafee.normalitycheck.shapirowilk import ShapiroWilk
        >>> import numpy as np
        >>> x = np.array([1.90642, 2.22488, 2.10288, 1.69742, 1.52229, 3.15435, 2.61826, 1.98492, 1.42738, 1.99568])
        >>> sw_test = ShapiroWilk()
        >>> sw_test.fit(x)
        >>> sw_test.to_xlsx(file_name="my_data")
            The data has been exported to the 'my_data.xlsx' file

        Download the exported file by :download:`clicking here <assets/my_data.xlsx>`.


        **Export with personalized sheet name**

        >>> from pycafee.normalitycheck.shapirowilk import ShapiroWilk
        >>> import numpy as np
        >>> x = np.array([1.90642, 2.22488, 2.10288, 1.69742, 1.52229, 3.15435, 2.61826, 1.98492, 1.42738, 1.99568])
        >>> sw_test = ShapiroWilk()
        >>> sw_test.fit(x)
        >>> sw_test.to_xlsx(file_name="sw_test", sheet_names=["sample", "data"])
            The data has been exported to the 'sw_test.xlsx' file


        Download the exported file by :download:`clicking here <assets/sw_test.xlsx>`.


        """
        if self.msg is None:
            fk_id_function = management._query_func_id("ShapiroWilk")
            messages = management._get_messages(fk_id_function, self.language)
            general._display_one_line_attention(messages[1][0][0])
        else:
            # quering
            fk_id_function = management._query_func_id("to_xlsx")
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
            name = "ShapiroWilk" + messages[4][0][0]
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

    # with docstring, with text, with database, with test,
    def to_csv(self, file_name=None, sep=","):
        """Export the data to csv file
        This function is just a wraper around :doc:`pd.DataFrame.to_csv <pandas:reference/api/pandas.DataFrame.to_csv>` [1]_ to export ``.csv`` files.

        Parameters
        ----------
        file_name : ``str``, optional
            The name of the file to be exported, without its extension (default is ``None``, which results in a file named ``'shapiro_wilk.csv'``)
        sep : ``str`` of length ``1``, optional
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
        fit : performs the Kolmogorov Smirnov Normality test.

        References
        ----------
        .. [1] pandas. pandas.DataFrame.to_csv. Available at: `pd.to_csv <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html>`_. Accessed on: 10 May 2022.


        Examples
        --------
        **Export with default settings**

        >>> from pycafee.normalitycheck.shapirowilk import ShapiroWilk
        >>> import numpy as np
        >>> x = np.array([1.90642, 2.22488, 2.10288, 1.69742, 1.52229, 3.15435, 2.61826, 1.98492, 1.42738, 1.99568])
        >>> sw_test = ShapiroWilk()
        >>> sw_test.fit(x)
        >>> sw_test.to_csv()
            The 'shapiro_wilk.csv' file was exported!

        Download the exported file by :download:`clicking here <assets/shapiro_wilk.csv>`.


        **Export with personalized file name**

        >>> from pycafee.normalitycheck.shapirowilk import ShapiroWilk
        >>> import numpy as np
        >>> x = np.array([1.90642, 2.22488, 2.10288, 1.69742, 1.52229, 3.15435, 2.61826, 1.98492, 1.42738, 1.99568])
        >>> sw_test = ShapiroWilk()
        >>> sw_test.fit(x)
        >>> sw_test.to_csv(file_name="my_data")
            The 'my_data.csv' file was exported!

        Download the exported file by :download:`clicking here <assets/my_data.csv>`.

        """

        if self.msg is None:
            fk_id_function = management._query_func_id("ShapiroWilk")
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
            fk_id_function = management._query_func_id("to_csv")
            messages = management._get_messages(fk_id_function, self.language, "to_csv")

            # criando o data frame para exportar via csv
            data_index = list(np.arange(1, self.x_exp.size + 1))
            x_exp = list(self.x_exp)
            name = "ShapiroWilk" + messages[2][0][0]
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
            fk_id_function = management._query_func_id("ShapiroWilk")
            messages = management._get_messages(fk_id_function, self.language)
            return messages[1][0][0]
        else:
            return self.msg

    def __repr__(self):
        fk_id_function = management._query_func_id("ShapiroWilk")
        messages = management._get_messages(fk_id_function, self.language)
        return messages[2][0][0]
