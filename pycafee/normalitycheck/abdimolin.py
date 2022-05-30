"""This module concentrates all constants, methods and classes related to the Abdi Molin test.

"""

##########################################
################ Summmary ################
##########################################

### acredito que esteja tudo certo ###

# - AbdiMolin(AlphaManagement, NDigitsManagement, PlotsManagement)
#     - __init__(self, alfa=None, language=None, n_digits=None, **kwargs)
#     - get_critical_value(self, n_rep, alfa=None)
#     - draw_critical_values(self, ax=None, export=None, extension=None, file_name=None, dpi=None, decimal_separator=None, local=None)
#     - fit(self, x_exp, alfa=None, details=None)
#     - to_xlsx(self, file_name=None, sheet_names=None)
#     - to_csv(self, file_name=None, sep=",")
#     - fn_abdi_molin(self, n_rep)
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

class AbdiMolin(AlphaManagement, NDigitsManagement, PlotsManagement):
    """
    This class instantiates an object to perform the AbdiMolin Normality test.

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
    ABDIMOLIN_TABLE : ``dict``
        The critical data of the correction proposed by Abdi & Molin.


    Methods
    -------
    fit(x_exp, alfa=None, n_digits=None, conclusion=None, details=None)
        Performs the AbdiMolin test.
    to_csv(file_name=None, sep=",")
        Exports the results to a pre-formatted csv file.
    to_xlsx(file_name=None, sheet_names=None)
        Exports the results to a pre-formatted xlsx file.
    get_critical_value(n_rep, alfa=None)
        Returns the critical value for a pair of alpha and number of observations.
    draw_critical_values(ax=None, export=None, extension=None, file_name=None, dpi=None, decimal_separator=None, local=None)
        Draws a plot with the Abdi-Molin critical data.
    fn_abdi_molin(self, n_rep)
        Returns the fn value.


    """

    ABDIMOLIN_TABLE = {
        'n_rep': [
                    4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                    31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50
                ],
        0.01 : [
                    0.4129, 0.3959, 0.3728, 0.3504, 0.3331, 0.3162, 0.3037, 0.2905, 0.2812, 0.2714, 0.2627, 0.2545, 0.2477,
                    0.2408, 0.2345, 0.2285, 0.2226, 0.2190, 0.2141, 0.2090, 0.2053, 0.2010, 0.1985, 0.1941, 0.1911, 0.1886,
                    0.1848, 0.1820, 0.1798, 0.1770, 0.1747, 0.1720, 0.1695, 0.1677, 0.1653, 0.1634, 0.1616, 0.1599, 0.1573,
                    0.1556, 0.1542, 0.1525, 0.1512, 0.1499, 0.1476, 0.1463, 0.1457
                ],
        0.05 : [
                    0.3754, 0.3427, 0.3245, 0.3041, 0.2875, 0.2744, 0.2616, 0.2506, 0.2426, 0.2337, 0.2257, 0.2196, 0.2128,
                    0.2071, 0.2018, 0.1965, 0.1920, 0.1881, 0.1840, 0.1798, 0.1766, 0.1726, 0.1699, 0.1665, 0.1641, 0.1614,
                    0.1590, 0.1559, 0.1542, 0.1518, 0.1497, 0.1478, 0.1454, 0.1436, 0.1421, 0.1402, 0.1386, 0.1373, 0.1353,
                    0.1339, 0.1322, 0.1309, 0.1293, 0.1282, 0.1269, 0.1256, 0.1246
                ],
        0.10 : [
                    0.3456, 0.3188, 0.2982, 0.2802, 0.2649, 0.2522, 0.2410, 0.2306, 0.2228, 0.2147, 0.2077, 0.2016, 0.1956,
                    0.1902, 0.1852, 0.1803, 0.1764, 0.1726, 0.1690, 0.1650, 0.1619, 0.1589, 0.1562, 0.1533, 0.1509, 0.1483,
                    0.1460, 0.1432, 0.1415, 0.1392, 0.1373, 0.1356, 0.1336, 0.1320, 0.1303, 0.1288, 0.1275, 0.1258, 0.1244,
                    0.1228, 0.1216, 0.1204, 0.1189, 0.1180, 0.1165, 0.1153, 0.1142
                ],
        0.15 : [
                    0.3216, 0.3027, 0.2816, 0.2641, 0.2502, 0.2382, 0.2273, 0.2179, 0.2101, 0.2025, 0.1959, 0.1899, 0.1843,
                    0.1794, 0.1747,  0.1700, 0.1666, 0.1629, 0.1592, 0.1555, 0.1527, 0.1498, 0.1472, 0.1448, 0.1423, 0.1398,
                    0.1378, 0.1353, 0.1336, 0.1314, 0.1295, 0.1278, 0.1260, 0.1245, 0.1230, 0.1214, 0.1204, 0.1186, 0.1172,
                    0.1159, 0.1148, 0.1134, 0.1123, 0.1113, 0.1098, 0.1089, 0.1079
                ],
        0.20 : [
                    0.3027, 0.2893, 0.2694, 0.2521, 0.2387, 0.2273, 0.2171, 0.2080, 0.2004, 0.1932, 0.1869, 0.1811, 0.1758,
                    0.1711, 0.1666, 0.1624, 0.1589, 0.1553, 0.1517, 0.1484, 0.1458, 0.1429, 0.1406, 0.1381, 0.1358, 0.1334,
                    0.1315, 0.1291, 0.1274, 0.1254, 0.1236, 0.1220, 0.1203, 0.1188, 0.1174, 0.1159, 0.1147, 0.1131, 0.1119,
                    0.1106, 0.1095, 0.1083, 0.1071, 0.1062, 0.1040, 0.1047, 0.1030
                ]
        }

    def __init__(self, alfa=None, language=None, n_digits=None, **kwargs):
        super().__init__(alfa=alfa, language=language, n_digits=n_digits, **kwargs)
        self.msg = None
        self.statistic = None
        self.critical = None
        self.p_value = None
        self.x_exp = None

    # with tests, with text, with database, with docstring
    def get_critical_value(self, n_rep, alfa=None):
        """This function returns the critical value of the AbdiMolin Normality [1]_ test at alfa significance level.

        Parameters
        ----------
        n_rep : ``int``
            The total number of observations (``n_rep >= 4``).
        alfa : ``float``, optional
            The significance level (between ``0.0`` and ``0.20``, default = ``0.05``)

        Returns
        -------
        critical : ``float`` or ``None``.
            The critical (tabulated) value for the requested confidence level.
        alfa : ``float``
            The corresponding significance level.

        Notes
        -----
        If the number of observations is higher than ``50`` (``n_rep > 50``), the function returns an approximate value.

        This function has critical values for the following confidence levels [2]_:

            - 99% (``ɑ = 0.01``);
            - 95% (``ɑ = 0.05``);
            - 90% (``ɑ = 0.10``);
            - 85% (``ɑ = 0.15``);
            - 80% (``ɑ = 0.20``);

        The function returns ``None`` for other confidence levels.


        See also
        --------
        draw_critical_values : draw a graph with the critical values.
        fit : performs the AbdiMolin Normality test.


        References
        ----------
        .. [1] MOLIN, P.; ABDI, H. New Tables and numerical approximation for the Kolmogorov- Smirnov/Lillierfors/Van Soest test of normality. p. 1–12, 1998. Available from `MolinAbdi1998-LillieforsTechReport.pdf <https://personal.utdallas.edu/~herve/MolinAbdi1998-LillieforsTechReport.pdf>`_.

        .. [2] SALKIND, N. J. Encyclopedia of measurement and statistics. California: SAGE Publications, Inc., 2007. DOI: `10.4135/9781412952644 <http://dx.doi.org/10.4135/9781412952644>`_.


        Examples
        --------
        **Getting the critical value for** ``5%`` **of significance and** ``6`` **observations**

        >>> from pycafee.normalitycheck import AbdiMolin
        >>> abdimolin_test = AbdiMolin()
        >>> result = abdimolin_test.get_critical_value(6)
        >>> print(result)
        AbdiMolinResult(critical=0.3245, alpha=0.05)


        **Getting the critical value for** ``1%`` **of significance and** ``10`` **observations**

        >>> from pycafee.normalitycheck import AbdiMolin
        >>> abdimolin_test = AbdiMolin()
        >>> result = abdimolin_test.get_critical_value(10, alfa=0.01)
        >>> print(result)
        AbdiMolinResult(critical=0.3037, alpha=0.01)

        """
        ### quering ###
        fk_id_function = management._query_func_id("get_critical_value")
        messages = management._get_messages(fk_id_function, self.language)

        am_table = AbdiMolin.ABDIMOLIN_TABLE


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
                general._display_one_line_attention(f"{messages[2][0][0]} AbdiMolin {messages[2][2][0]} '4' {messages[2][4][0]} '{n_rep}'",)
                raise

        ### getting the critical value ###
        if alfa == 0.01:
            if n_rep < 51:
                critical = am_table[alfa][n_rep - 4]
            else:
                critical = 1.035/self.fn_abdi_molin(n_rep)
        elif alfa == 0.05:
            if n_rep < 51:
                critical = am_table[alfa][n_rep - 4]
            else:
                critical = 0.895/self.fn_abdi_molin(n_rep)
        elif alfa == 0.10:
            if n_rep < 51:
                critical = am_table[alfa][n_rep - 4]
            else:
                critical = 0.819/self.fn_abdi_molin(n_rep)
        elif alfa == 0.15:
            if n_rep < 51:
                critical = am_table[alfa][n_rep - 4]
            else:
                critical = 0.775/self.fn_abdi_molin(n_rep)
        elif alfa == 0.20:
            if n_rep < 51:
                critical = am_table[alfa][n_rep - 4]
            else:
                critical = 0.741/self.fn_abdi_molin(n_rep)
        else:
            critical = None

        name = "AbdiMolin" + messages[3][0][0]
        ### return the tabulated value and the graph axis ###
        result = namedtuple(name, (messages[3][1][0], messages[3][2][0]))
        return result(critical, alfa)

    # with tet, tieh text, with database, with docstring
    def draw_critical_values(self, ax=None, export=None, extension=None, file_name=None, dpi=None, decimal_separator=None, local=None):
        """Draw a plot with the AbdiMolin  [1]_ *critical data*.

        Parameters
        ----------
        ax : ``None`` or ``matplotlib.axes.SubplotBase``
            If ``ax`` is ``None``, a figure is created with a preset design. The other parameters can be used to export the graph.
            If ``ax`` is a ``matplotlib.axes.SubplotBase``, the function returns a ``matplotlib.axes.SubplotBase`` with the AbdiMolin critical data. In this case, the other parameters do not affect the graph.
        export : ``bool``, optional
            Whether the graph should be exported (``True``) or not (``False``). The default value is ``None``, which implies ``False``.
        file_name : ``str``, optional
            The file name. Default is ``None`` which results in a file named ``"abdimolin_critical_plot"``.
        extension : ``str``, optional
            The file extension without a dot. Default is ``None`` which results in a ``".png"`` file.
        dpi : ``int`` or ``float``, optional
            The figure pixel density. The default is ``None``, which results in a ``100 dpis`` picture. This parameter must be a number higher than zero.
        decimal_separator : ``str``, optional
            The decimal separator symbol used in the chart. It can be the dot (``None`` or ``'.'``) or the comma (``','``).
        local : ``str``, optional
            The alias for the desired locale. Only used if ``decimal_separator=','`` to set the matplolib's default locale. Its only function is to change the decimal separator symbol and should be changed only if the ``"pt_BR"`` option is not available.


        Returns
        -------
        axes : ``matplotlib.axes._subplots.AxesSubplot``
            The axis of the graph.

        Notes
        -----
        To obtain the critical values of the AbdiMolin test, use:

        .. code:: python

            from pycafee.normalitycheck.abdimolin import AbdiMolin
            abdimolin_test = AbdiMolin()
            table = abdimolin_test.ABDIMOLIN_TABLE


        See also
        --------
        get_critical_value : Returns the critical value for the AbdiMolin test.
        fit : performs the AbdiMolin Normality test.

        References
        ----------
        .. [1] SALKIND, N. J. Encyclopedia of measurement and statistics. California: SAGE Publications, Inc., 2007. DOI: `10.4135/9781412952644 <http://dx.doi.org/10.4135/9781412952644>`_.

        Examples
        --------
        **Using the figure created inside the function**

        >>> from pycafee.normalitycheck.abdimolin import AbdiMolin
        >>> abdimolin_test = AbdiMolin()
        >>> abdimolin_test.draw_critical_values(export=True)
        The 'abdi_molin_critical_plot.png' file has been exported


        .. image:: img/abdi_molin_critical_plot.png
           :alt: Graph showing the Abdi Molin critical plot
           :align: center

        **Using a previously created figure**

        >>> from pycafee.normalitycheck.abdimolin import AbdiMolin
        >>> import matplotlib.pyplot as plt
        >>> abdimolin_test = AbdiMolin(language='pt-br')
        >>> fig, ax = plt.subplots(figsize=(8,6))
        >>> ax = abdimolin_test.draw_critical_values(ax=ax)
        >>> plt.savefig("abdi_molin_plot.png")
        >>> plt.show()

        .. image:: img/abdi_molin_plot.png
           :alt: Graph showing the Abdi Molin critical plot.
           :align: center

        """
        ## export ##
        export = self._get_default_export(export)

        ## extension ##
        extension = self._get_default_extension(extension)

        ## file name ##
        if file_name is None:
            file_name = "abdi_molin_critical_plot"
        else:
            checkers._check_is_str(file_name, "file_name", self.language)
            helpers._check_forbidden_character(file_name, "file_name", self.language)


        ## dpi ##
        dpi = self._get_default_dpi(dpi)

        ## decimal_separator ##
        decimal_separator = self._get_default_decimal_separator(decimal_separator)

        ## local ##
        local = self._get_default_local(local)

        fk_id_function = management._query_func_id("draw_critical_values")
        messages = management._get_messages(fk_id_function, self.language)


        ### The values tabled in a dictionary ###
        table = AbdiMolin.ABDIMOLIN_TABLE

        default_locale = helpers._change_locale(self.language, decimal_separator, local)

        ### Make the plot ###
        if ax is None:
            fig, axes = plt.subplots(figsize=(12,6))
        else:
            checkers._check_is_subplots(ax, "ax", self.language)
            axes = ax
        axes.plot(table['n_rep'], table[0.01], marker='o', label=f'{messages[1][0][0]} = 1%')
        axes.plot(table['n_rep'], table[0.05], marker='o', label=f'{messages[1][0][0]} = 5%')
        axes.plot(table['n_rep'], table[0.10], marker='o', label=f'{messages[1][0][0]} = 10%')
        axes.plot(table['n_rep'], table[0.15], marker='o', label=f'{messages[1][0][0]} = 15%')
        axes.plot(table['n_rep'], table[0.20], marker='o', label=f'{messages[1][0][0]} = 20%')
        axes.legend()
        axes.set_title(f"{messages[2][0][0]} Abdi-Molin {messages[2][2][0]}")
        axes.set_xlabel(messages[3][0][0])
        axes.set_ylabel(messages[4][0][0])
        axes.set_xticks([4, 10, 15, 20, 25, 30, 35, 40, 45, 50])


        ## If show equals True, display the graph ##
        if ax is None:
            fig.tight_layout()
            if export:
                ### Baptism of Fire ###
                file_name = helpers._check_conflicting_filename(file_name, extension, self.language)
                plt.savefig(file_name, dpi=dpi, bbox_inches='tight')
                general._display_one_line_success(f"{messages[5][0][0]} '{file_name}' {messages[5][2][0]}")
            plt.show()

        helpers._change_locale_back_to_default(default_locale)

        return axes

    # with test, with text, with database, with docstring
    def fit(self, x_exp, alfa=None, details=None):
        """This function is a wraper around ``statsmodels.stats.diagnostic.lilliefors()`` [1]_ to estimate the statistic of the **AbdiMolin Normality test**. Only the statistic value is used.

        The main difference between this method and the original one is that this wrap only allows the comparison of a sample with the Normal distribution, using ``dist="norm"``. The method to estimate the p-value is set to table. Hence:

        >>> statsmodels.stats.diagnostic(x_exp, dist="norm", pvalmethod="table")


        Parameters
        ----------
        x_exp : ``numpy array``
            One dimension :doc:`numpy array <numpy:reference/generated/numpy.array>` with at least ``4`` sample data.
        alfa : ``float``, optional
            The level of significance (``ɑ``). Default is ``None`` which results in ``0.05`` (``ɑ = 5%``).
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
                The critical value for alpha equal to ``1%``, ``5%``, ``10%``, ``15%`` or ``20%``. Other values will raise ``ValueError``.
            p_value : ``None``
                The p-value for the hypothesis test (always ``None``).
        conclusion : ``str``
            The test conclusion (e.g, Normal/ not Normal).


        See Also
        --------

        pycafee.normalitycheck.andersondarling.AndersonDarling.fit
        pycafee.normalitycheck.kolmogorovsmirnov.KolmogorovSmirnov.fit
        pycafee.normalitycheck.lilliefors.Lilliefors.fit
        pycafee.normalitycheck.shapirowilk.ShapiroWilk.fit


        Notes
        -----

        The critical values  [2]_ includes samples with sizes between ``4`` and ``50`` for ``ɑ`` equal to ``1%``, ``5%``, ``10%``, ``15%`` or ``20%``.

        * For data with a sample size higher than ``51`` (``n_rep > 50``), the critical value returned is the aproximation proposed by the authors.

        The **AbdiMolin Normality test** [3]_ has the following premise:

        .. admonition:: \u2615

           :math:`H_0:` data *comes from Normal* distribution.

           :math:`H_1:` data *does* **not** *come from Normal* distribution.

        The conclusion is based on the comparison between the ``critical`` value (at ``ɑ`` significance level) and ``statistic`` of the test. In summary:

        .. code:: python

           if critical >= statistic:
               Data is Normal
           else:
               Data is not Normal


        If ``ɑ`` is not ``0.01``, ``0.05``, ``0.10``, ``0.15`` or ``0.20``, the function will raise a ``ValueError``.



        References
        ----------
        .. [1] STATSMODELS. statsmodels.stats.diagnostic.lilliefors. Available at: `www.statsmodels.org <https://www.statsmodels.org/dev/generated/statsmodels.stats.diagnostic.lilliefors.html>`_. Access on: 10 May. 2022

        .. [2] SALKIND, N. J. Encyclopedia of measurement and statistics. California: SAGE Publications, Inc., 2007. DOI: `10.4135/9781412952644 <http://dx.doi.org/10.4135/9781412952644>`_.

        .. [3] MOLIN, P.; ABDI, H. New Tables and numerical approximation for the Kolmogorov- Smirnov/Lillierfors/Van Soest test of normality. p. 1–12, 1998. Available from `MolinAbdi1998-LillieforsTechReport.pdf <https://personal.utdallas.edu/~herve/MolinAbdi1998-LillieforsTechReport.pdf>`_.

        Examples
        --------

        **Applying the test with default values**

        >>> from pycafee.normalitycheck import AbdiMolin
        >>> import scipy.stats as stats
        >>> x = stats.norm.rvs(loc=5, scale=3, size=100, random_state=42)
        >>> abdimolin_test = AbdiMolin()
        >>> result, conc = abdimolin_test.fit(x)
        >>> print(result)
        AbdiMolinResult(Statistic=0.05177647360597687, Critical=0.0888513848903008, p_value=None, Alpha=0.05)
        >>> print(conc)
        Data is Normal at a 95.0% of confidence level.


        **Applying the test with** ``alfa=0.10``

        >>> from pycafee.normalitycheck import AbdiMolin
        >>> import numpy as np
        >>> x = np.array([1.90642, 2.22488, 2.10288, 1.69742, 1.52229, 3.15435, 2.61826, 1.98492, 1.42738, 1.99568])
        >>> abdimolin_test = AbdiMolin()
        >>> result, conc = abdimolin_test.fit(x, alfa=0.01)
        >>> print(result)
        AbdiMolinResult(Statistic=0.17709753067016487, Critical=0.3037, p_value=None, Alpha=0.01)
        >>> print(conc)
        Data is Normal at a 99.0% of confidence level.


        **Applying the test with** ``alfa=0.10`` **and** ``details="full"``

        >>> from pycafee.normalitycheck import AbdiMolin
        >>> import numpy as np
        >>> x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        >>> abdimolin_test = AbdiMolin()
        >>> result, conc = abdimolin_test.fit(x, alfa=0.10, details="full")
        >>> print(result)
        AbdiMolinResult(Statistic=0.15459867079959644, Critical=0.241, p_value=None, Alpha=0.1)
        >>> print(conc)
        Since the critical value (0.241) >= statistic (0.154), we have NO evidence to reject the hypothesis of data normality, according to the AbdiMolin test at a 90.0% of confidence level.


        **Applying the test with** ``details="full"``

        >>> from pycafee.normalitycheck import AbdiMolin
        >>> import numpy as np
        >>> x = np.array([0.8, 1, 1.1, 1.15, 1.15, 1.2, 1.2, 1.2, 1.2, 1.6, 1.8, 2, 2.2, 3, 5, 8.2, 8.4, 8.6, 9])
        >>> abdimolin_test = AbdiMolin()
        >>> result, conc = abdimolin_test.fit(x, details="full")
        >>> print(result)
        AbdiMolinResult(Statistic=0.3072356484569813, Critical=0.1965, p_value=None, Alpha=0.05)
        >>> print(conc)
        Since the critical value (0.196) < statistic (0.307), we HAVE evidence to reject the hypothesis of data normality, according to the AbdiMolin test at a 95.0% of confidence level.


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
        # atrbuindo None ao pvalor para evitar preblemas
        p_value = None

        # ### writing the test conclusion ###
        ## The test conclustion based on tabulated value depends on whether tabulated value exists. If not, Raise a error ##
        if critical is None:
            try:
                error = messages[1][0][0]
                raise ValueError(error)
            except ValueError:
                msg = f"{messages[3][0][0]} '{alfa}' {messages[3][2][0]}"
                p_values = list(AbdiMolin.ABDIMOLIN_TABLE.keys())
                p_values.pop(0)
                alfa_list = [msg]
                for item in p_values:
                    alfa_list.append(f"   --->    {item}")
                general._display_n_line_attention(alfa_list)
                raise
        else: # if there is a tabulated value
            if critical >= statistic:
                if details == 'full':
                    msg = f"{messages[4][0][0]}{helpers._truncate(critical, self.language, decs=self.n_digits)}{messages[4][2][0]}{helpers._truncate(statistic, self.language, decs=self.n_digits)}{messages[4][4][0]} AbdiMolin {messages[4][6][0]} {100*(1-alfa)}{messages[4][8][0]}"
                elif details == "binary":
                    msg = 0
                else:
                    msg = f"{messages[5][0][0]} {100*(1-alfa)}{messages[5][2][0]}"
            else:
                if details == 'full':
                    msg = f"{messages[6][0][0]}{helpers._truncate(critical, self.language, decs=self.n_digits)}{messages[6][2][0]}{helpers._truncate(statistic, self.language, decs=self.n_digits)}{messages[6][4][0]} AbdiMolin {messages[6][6][0]} {100*(1-alfa)}{messages[6][8][0]}"
                elif details == "binary":
                    msg = 1
                else:
                    msg = f"{messages[7][0][0]} {100*(1-alfa)}{messages[7][2][0]}"

        name = "AbdiMolin" + messages[10][0][0]
        result = namedtuple(name, (messages[11][0][0], messages[12][0][0], messages[13][0][0], messages[14][0][0]))
        self.msg = msg
        self.statistic = statistic
        self.critical = critical
        self.p_value = p_value
        return result(self.statistic, self.critical, self.p_value, self.alfa), self.msg

    # with tests, with text, with database, with docstring
    def to_xlsx(self, file_name=None, sheet_names=None):
        """This method exports the data to ``.xlsx``.

        This function is just a wraper around :doc:`pd.DataFrame.to_excel <pandas:reference/api/pandas.DataFrame.to_excel>` [1]_ to export ``.xlsx`` files.

        Parameters
        ----------
        file_name : ``str``, optional
            The name of the file to be exported, without its extension (default is ``None`` which results in a file name ``'abdimolin.xlsx'``).
        sheet_names : ``list`` of two ``str``, optional
            A ``list`` containing the name of the worksheets where the data will be saved:

                * The first element corresponds to the name of the worksheet where the calculated data will be saved (default is ``None`` which means ``'abdimolin'``).

                * The second element corresponds to the name of the worksheet where the supplied data will be saved (default is ``None`` which means ``'data'``).

        Returns
        -------
        df_list : A ``list`` of two ``pandas DataFrame``
            The first element is a ``pd.DataFrame`` with the AbdiMolin calculated data.
            The second element is a ``pd.DataFrame`` with the supplied data.

        Notes
        -----
        The ``fit()`` method needs to be applied beforehand.

        If a spreadsheet with the same name already exists in the current directory and this file contains tabs with conflicting names, the new tabs will be inserted into the file with different names, preserving the original data.

        See Also
        --------
        fit : performs the AbdiMolin Normality test.

        References
        ----------
        .. [1] pandas. pandas.DataFrame.to_excel function. Available at: `pd.to_excel <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html>`_. Accessed on: 10 May 2022.

        Examples
        --------
        **Export with default settings**

        >>> from pycafee.normalitycheck import AbdiMolin
        >>> import numpy as np
        >>> x = np.array([1.90642, 2.22488, 2.10288, 1.69742, 1.52229, 3.15435, 2.61826, 1.98492, 1.42738, 1.99568])
        >>> abdimolin_test = AbdiMolin()
        >>> abdimolin_test.fit(x)
        >>> abdimolin_test.to_xlsx()
            The data has been exported to the 'abdimolin.xlsx' file

        Download the exported file by :download:`clicking here <assets/abdimolin.xlsx>`.


        **Export with personalized file name**

        >>> from pycafee.normalitycheck import AbdiMolin
        >>> import numpy as np
        >>> x = np.array([1.90642, 2.22488, 2.10288, 1.69742, 1.52229, 3.15435, 2.61826, 1.98492, 1.42738, 1.99568])
        >>> abdimolin_test = AbdiMolin()
        >>> abdimolin_test.fit(x)
        >>> abdimolin_test.to_xlsx(file_name="my_data")
            The data has been exported to the 'my_data.xlsx' file

        Download the exported file by :download:`clicking here <assets/my_data.xlsx>`.

        **Export with personalized sheet name**

        >>> from pycafee.normalitycheck import AbdiMolin
        >>> import numpy as np
        >>> x = np.array([1.90642, 2.22488, 2.10288, 1.69742, 1.52229, 3.15435, 2.61826, 1.98492, 1.42738, 1.99568])
        >>> abdimolin_test = AbdiMolin()
        >>> abdimolin_test.fit(x)
        >>> abdimolin_test.to_xlsx(file_name="abdimolin_test", sheet_names=["sample", "data"])
             The data has been exported to the 'abdimolin_test.xlsx' file

        Download the exported file by :download:`clicking here <assets/abdimolin_test.xlsx>`.


        """
        if self.msg is None:
            fk_id_function = management._query_func_id("AbdiMolin")
            messages = management._get_messages(fk_id_function, self.language)
            general._display_one_line_attention(messages[1][0][0])
        else:
            # quering
            fk_id_function = management._query_func_id("to_xlsx")
            messages = management._get_messages(fk_id_function, self.language)

            # batizando o nome do arquivo
            if file_name is None:
                file_name = "abdimolin"
            else:
                checkers._check_is_str(file_name, 'file_name', self.language)
                helpers._check_forbidden_character(file_name, "file_name", self.language)
            ## verificando o sheet_names
            if sheet_names is None:
                sheet_names = [
                    "abdimolin",
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
            name = "AbdiMolin" + messages[4][0][0]
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
        """Export the data to ``.csv`` file.
        This function is just a wraper around :doc:`pd.DataFrame.to_csv <pandas:reference/api/pandas.DataFrame.to_csv>` [1]_ to export ``.csv`` files.

        Parameters
        ----------
        file_name : ``str``, optional
            The name of the file to be exported, without its extension (default is ``None``, which results in a file named ``'abdimolin.csv'``)
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
        fit : performs the AbdiMolin Normality test.

        References
        ----------
        .. [1] pandas. pandas.DataFrame.to_csv. Available at: `pd.to_csv <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html>`_. Accessed on: 10 May 2022.



        Examples
        --------
        **Export with default settings**

        >>> from pycafee.normalitycheck import AbdiMolin
        >>> import numpy as np
        >>> x = np.array([1.90642, 2.22488, 2.10288, 1.69742, 1.52229, 3.15435, 2.61826, 1.98492, 1.42738, 1.99568])
        >>> abdimolin_test = AbdiMolin()
        >>> abdimolin_test.fit(x)
        >>> abdimolin_test.to_csv()
            The 'abdimolin.csv' file was exported!

        Download the exported file by :download:`clicking here <assets/abdimolin.csv>`.


        **Export with personalized file name**

        >>> from pycafee.normalitycheck import AbdiMolin
        >>> import numpy as np
        >>> x = np.array([1.90642, 2.22488, 2.10288, 1.69742, 1.52229, 3.15435, 2.61826, 1.98492, 1.42738, 1.99568])
        >>> abdimolin_test = AbdiMolin()
        >>> abdimolin_test.fit(x)
        >>> abdimolin_test.to_csv(file_name="my_data")
            The 'my_data.csv' file was exported!


        Download the exported file by :download:`clicking here <assets/my_data.csv>`.

        """

        if self.msg is None:
            fk_id_function = management._query_func_id("AbdiMolin")
            messages = management._get_messages(fk_id_function, self.language)
            general._display_one_line_attention(messages[1][0][0])

        else:
            # batizando o nome do arquivo
            if file_name is None:
                file_name = "abdimolin"
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
            name = "AbdiMolin" + messages[2][0][0]
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

    # with tests, with docstring
    def fn_abdi_molin(self, n_rep):
        """This function returns the divisor term for the correction proposed by Molin & Abdi (1998) [1]_ to calculate the critical values of the Normality test for ``n_rep > 50``.

        The correction is calculated using the following expresion:

        .. math::

            f_N = \\frac{0.83 + N}{\\sqrt{N}} - 0.01


        where :math:`N` is the number of observations (e.g, ``n_rep``)


        Parameters
        ----------
        n_rep : ``int``
            The number of observations in the sample (``n_rep > 50``)

        Returns
        -------
        fn : ``float``
            The divisor of the correction proposed by the authors.

        See Also
        --------
        get_critical_value : get the critical values for the AbdiMolin Normality test.
        fit : performs the AbdiMolin Normality test.

        References
        ----------
        .. [1] MOLIN, P.; ABDI, H. New Tables and numerical approximation for the Kolmogorov- Smirnov/Lillierfors/Van Soest test of normality. p. 1–12, 1998. Available from `MolinAbdi1998-LillieforsTechReport.pdf <https://personal.utdallas.edu/~herve/MolinAbdi1998-LillieforsTechReport.pdf>`_.

        Examples
        --------
        >>> from pycafee.normalitycheck import AbdiMolin
        >>> test = AbdiMolin()
        >>> result = test.fn_abdi_molin(54)
        >>> print(result)
        7.451417922044536

        """
        checkers._check_is_integer(n_rep, "n_rep", self.language)
        checkers._check_is_positive(n_rep, "n_rep", self.language)
        checkers._check_value_is_equal_or_higher_than(n_rep, "n_rep", 51, self.language)
        fn = (0.83 + n_rep)/np.sqrt(n_rep) - 0.01
        return fn


    def __str__(self):
        if self.msg is None:
            fk_id_function = management._query_func_id("AbdiMolin")
            messages = management._get_messages(fk_id_function, self.language)
            return messages[1][0][0]
        else:
            return self.msg

    def __repr__(self):
        fk_id_function = management._query_func_id("AbdiMolin")
        messages = management._get_messages(fk_id_function, self.language)
        return messages[2][0][0]



# omae no sono konjoo tataki naosu zo https://youtu.be/LcYnfUt6Vvg?t=73
