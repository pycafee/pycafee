"""This module concentrates all constants, methods and classes related to the Anderson Darling test.

"""

##########################################
################ Summmary ################
##########################################

# - AndersonDarling(AlphaManagement, NDigitsManagement, PlotsManagement)
#         - fit(x_exp, alfa=None, n_digits=None, conclusion=None, details=None)
#         - to_csv(file_name=None, sep=",")
#         - to_xlsx(file_name=None, sheet_names=None)
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
from statsmodels.stats.diagnostic import normal_ad as ad_statsmodel
from scipy.stats import anderson as ad_scipy



###### Home made ######

from pycafee.database_management import management
from pycafee.utils import checkers
from pycafee.utils import general
from pycafee.utils import helpers
from pycafee.utils.helpers import AlphaManagement, NDigitsManagement, PlotsManagement

###########################################
################ Functions ################
###########################################

class AndersonDarling(AlphaManagement, NDigitsManagement, PlotsManagement):
    """
    This class instantiates an object to perform the AndersonDarling Normality test.

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


    Methods
    -------
    fit(x_exp, alfa=None, n_digits=None, comparison=None, details=None)
        Performs the AndersonDarling test.
    to_csv(file_name=None, sep=",")
        Exports the results to a pre-formatted csv file.
    to_xlsx(file_name=None, sheet_names=None)
        Exports the results to a pre-formatted xlsx file.


    """

    def __init__(self, alfa=None, language=None, n_digits=None, **kwargs):
        super().__init__(alfa=alfa, language=language, n_digits=n_digits, **kwargs)
        self.msg = None
        self.statistic = None
        self.critical = None
        self.p_value = None
        self.x_exp = None



    # with tests, with text, with database, with docstring
    def fit(self, x_exp, alfa=None, comparison=None, details=None):
        """This function is a wraper around ``scipy.stats.anderson()`` [1]_ and ``statsmodels.stats.diagnostic.normal_ad()`` [2]_ to perform the **AndersonDarling Normality test** [3]_, but with some facilities.

        The method used to perform the test depends on the ``comparison`` parameter, but both models are fixed to compare a sample with the Normal distribution. Hence, we use:

        >>> scipy.stats.anderson(x, dist='norm')

        and

        >>> statsmodels.stats.diagnostic.normal_ad(x)


        Parameters
        ----------
        x_exp : ``numpy array``
            One dimension :doc:`numpy array <numpy:reference/generated/numpy.array>` with at least ``4`` sample data.
        alfa : ``float``, optional
            The level of significance (``ɑ``). Default is ``None`` which results in ``0.05`` (``ɑ = 5%``).
        comparison : ``str``, optional
            This parameter determines how to perform the comparison test to evaluate the Normality test and which api to use.

            * If ``comparison = "critical"`` (or ``None``), the comparison test is performed by comparing the critical value (with ``ɑ`` significance level) with the test statistic, using the ``SciPy`` method [1]_.
            * If ``comparison = "p-value"``, the comparison test is performed comparing the ``p-value`` with the adopted significance level (``ɑ``), using the statsmodels method [2]_.

            **Both results should lead to the same conclusion**.

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
            p_value : ``float`` or ``None``
                The p-value for the hypothesis test.
        conclusion : ``str``
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


        The **Anderson Darling Normality test** has the following premise:

        .. admonition:: \u2615

           :math:`H_0:` data *comes from Normal* distribution.

           :math:`H_1:` data *does* **not** *come from Normal* distribution.

        By default (``comparison = "critical"``), the conclusion is based on the comparison between the ``critical`` value (at ``ɑ`` significance level) and ``statistic`` of the test. The results are calculated using ``scipy.stats.anderson()``, and the ``p-value`` will be ``None``. In summary:

        .. code:: python

           if critical >= statistic:
               Data is Normal
           else:
               Data is not Normal

        The other option (``comparison="p-value"``) makes the conclusion comparing the ``p-value`` with ``ɑ``. The results are calculated using ``statsmodels.stats.diagnostic.normal_ad()`` and the ``critical`` value will be ``None``. In summary:

        .. code:: python

           if p-value >= ɑ:
               Data is Normal
           else:
               Data is not Normal


        References
        ----------

        .. [1] SCIPY. scipy_stats_anderson. Available at: `www.scipy.org <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.anderson.html>`_. Access on: 10 May. 2022

        .. [2] STATSMODELS. statsmodels_stats_diagnostic_normal_ad. Available at: `www.statsmodels.org <https://www.statsmodels.org/dev/generated/statsmodels.stats.diagnostic.normal_ad.html>`_. Access on: 10 May. 2022

        .. [3] STEPHENS, M. A. EDF Statistics for Goodness of Fit and Some Comparisons. Journal of the American Statistical Association, v. 69, n. 347, p. 730–737, 1974. DOI: `10.2307/2286009 <https://doi.org/10.2307/2286009>`_.



        Examples
        --------

        **Applying the test with default values**

        >>> from pycafee.normalitycheck.andersondarling import AndersonDarling
        >>> import scipy.stats as stats
        >>> x = stats.norm.rvs(loc=5, scale=3, size=100, random_state=42)
        >>> andersondarling_test = AndersonDarling()
        >>> result, conclusion = andersondarling_test.fit(x)
        >>> print(result)
        AndersonDarlingResult(Statistic=0.25343395875111696, Critical=0.759, p_value=None, Alpha=0.05)
        >>> print(conclusion)
        Data is Normal at a 95.0% of confidence level.


        **Applying the test using the** ``p-value`` **to make the conclusion**

        >>> from pycafee.normalitycheck.andersondarling import AndersonDarling
        >>> import scipy.stats as stats
        >>> x = stats.norm.rvs(loc=5, scale=3, size=100, random_state=42)
        >>> andersondarling_test = AndersonDarling()
        >>> result, conclusion = andersondarling_test.fit(x, comparison="p-value")
        >>> print(result)
        AndersonDarlingResult(Statistic=0.25343395875111696, Critical=None, p_value=0.7268427515457196, Alpha=0.05)
        >>> print(conclusion)
        Data is Normal at a 95.0% of confidence level.


        **Applying the test at** ``1%`` **of significance level**

        >>> from pycafee.normalitycheck.andersondarling import AndersonDarling
        >>> import numpy as np
        >>> x = np.array([1.90642, 2.22488, 2.10288, 1.69742, 1.52229, 3.15435, 2.61826, 1.98492, 1.42738, 1.99568])
        >>> andersondarling_test = AndersonDarling()
        >>> result, conclusion = andersondarling_test.fit(x, alfa=0.01)
        >>> print(result)
        AndersonDarlingResult(Statistic=0.3416856332675007, Critical=0.95, p_value=None, Alpha=0.01)
        >>> print(conclusion)
        Data is Normal at a 99.0% of confidence level.


        **Applying the test with a detailed conclusion**

        >>> from pycafee.normalitycheck.andersondarling import AndersonDarling
        >>> import numpy as np
        >>> x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        >>> andersondarling_test = AndersonDarling()
        >>> result, conclusion = andersondarling_test.fit(x, alfa=0.10, details="full")
        >>> print(result)
        AndersonDarlingResult(Statistic=0.22687861079050364, Critical=0.57, p_value=None, Alpha=0.1)
        >>> print(conclusion)
        Since the critical value (0.57) >= statistic (0.226), we have NO evidence to reject the hypothesis of data normality, according to the AndersonDarling test at a 90.0% of confidence level.


        **Applying the test using a not Normal data**

        >>> from pycafee.normalitycheck.andersondarling import AndersonDarling
        >>> import numpy as np
        >>> x = np.array([0.8, 1, 1.1, 1.15, 1.15, 1.2, 1.2, 1.2, 1.2, 1.6, 1.8, 2, 2.2, 3, 5, 8.2, 8.4, 8.6, 9])
        >>> andersondarling_test = AndersonDarling()
        >>> result, conclusion = andersondarling_test.fit(x, alfa=0.10, details="full", comparison='p-value')
        >>> print(result)
        AndersonDarlingResult(Statistic=2.5532223880710276, Critical=None, p_value=9.992220237231388e-07, Alpha=0.1)
        >>> print(conclusion)
        Since p-value (0.0) < alpha (0.1), we HAVE evidence to reject the hypothesis of data normality, according to the AndersonDarling test at a 90.0% of confidence level.


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

        aceita = 0
        rejeita = 1

        # ### writing the test conclusion ###
        if comparison == "p-value":
            critical = None
            statistic, p_value = ad_statsmodel(x_exp)
            if p_value >= alfa:
                if details == 'full':
                    msg = f"{messages[8][0][0]}{helpers._truncate(p_value, self.language, decs=self.n_digits)}{messages[8][2][0]}{alfa}{messages[8][4][0]} AndersonDarling {messages[8][6][0]} {100*(1-alfa)}{messages[8][8][0]}"
                elif details == "binary":
                    msg = aceita
                else:
                    msg = f"{messages[5][0][0]} {100*(1-alfa)}{messages[5][2][0]}"
            else:
                if details == 'full':
                    msg = f"{messages[9][0][0]}{helpers._truncate(p_value, self.language, decs=self.n_digits)}{messages[9][2][0]}{alfa}{messages[9][4][0]} AndersonDarling {messages[9][6][0]} {100*(1-alfa)}{messages[9][8][0]}"
                elif details == "binary":
                    msg = rejeita
                else:
                    msg = f"{messages[7][0][0]} {100*(1-alfa)}{messages[7][2][0]}"
        else:
            p_values = [0.15, 0.10, 0.05, 0.025, 0.01]
            if alfa not in p_values:
                try:
                    error = messages[1][0][0]
                    raise ValueError(error)
                except ValueError:
                    msg = f"{messages[3][0][0]} '{alfa}' {messages[3][2][0]}"
                    alfa_list = [msg]
                    for item in p_values:
                        alfa_list.append(f"   --->    {item}")
                    general._display_n_line_attention(alfa_list)
                    raise
            else: # if there is a tabulated value
                statistic, critical_values, sig_level = ad_scipy(x_exp)
                if alfa == 0.15:
                    critical = critical_values[0]
                elif alfa == 0.10:
                    critical = critical_values[1]
                elif alfa == 0.05:
                    critical = critical_values[2]
                elif alfa == 0.025:
                    critical = critical_values[3]
                else:
                    critical = critical_values[4]
                p_value = None
                if critical >= statistic:
                    if details == 'full':
                        msg = f"{messages[4][0][0]}{helpers._truncate(critical, self.language, decs=self.n_digits)}{messages[4][2][0]}{helpers._truncate(statistic, self.language, decs=self.n_digits)}{messages[4][4][0]} AndersonDarling {messages[4][6][0]} {100*(1-alfa)}{messages[4][8][0]}"
                    elif details == "binary":
                        msg = aceita
                    else:
                        msg = f"{messages[5][0][0]} {100*(1-alfa)}{messages[5][2][0]}"
                else:
                    if details == 'full':
                        msg = f"{messages[6][0][0]}{helpers._truncate(critical, self.language, decs=self.n_digits)}{messages[6][2][0]}{helpers._truncate(statistic, self.language, decs=self.n_digits)}{messages[6][4][0]} AndersonDarling {messages[6][6][0]} {100*(1-alfa)}{messages[6][8][0]}"
                    elif details == "binary":
                        msg = rejeita
                    else:
                        msg = f"{messages[7][0][0]} {100*(1-alfa)}{messages[7][2][0]}"

        name = "AndersonDarling" + messages[10][0][0]
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
            The name of the file to be exported, without its extension (default is ``None`` which results in a file name ``"andersondarling.xlsx"``).
        sheet_names : ``list`` of two ``str``, optional
            A ``list`` containing the name of the worksheets where the data will be saved:

                * The first element corresponds to the name of the worksheet where the calculated data will be saved (default is ``None`` which means ``"andersondarling"``).

                * The second element corresponds to the name of the worksheet where the supplied data will be saved (default is ``None`` which means ``"data"``).

        Returns
        -------
        df_list : A ``list`` of two pandas DataFrame
            The first element is a ``pd.DataFrame`` with the Anderson Darling calculated data.
            The second element is a ``pd.DataFrame`` with the supplied data.

        Notes
        -----
        The ``fit()`` method needs to be applied beforehand.

        If a spreadsheet with the same name already exists in the current directory and this files contains tabs with conflicting names, the new tabs will be inserted into the file with different names, preserving the original data.

        See Also
        --------
        fit : performs the Anderson Darling Normality test.


        References
        ----------
        .. [1] pandas. pandas.DataFrame.to_excel function. Available at: `pd.to_excel <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html>`_. Accessed on: 10 May 2022.

        Examples
        --------
        **Export with default settings**

        >>> from pycafee.normalitycheck.andersondarling import AndersonDarling
        >>> import numpy as np
        >>> x = np.array([1.90642, 2.22488, 2.10288, 1.69742, 1.52229, 3.15435, 2.61826, 1.98492, 1.42738, 1.99568])
        >>> andersondarling_test = AndersonDarling()
        >>> andersondarling_test.fit(x)
        >>> andersondarling_test.to_xlsx()
            The data has been exported to the 'andersondarling.xlsx' file

        Download the exported file by :download:`clicking here <assets/andersondarling.xlsx>`.

        **Export with personalized file name**

        >>> from pycafee.normalitycheck.andersondarling import AndersonDarling
        >>> import numpy as np
        >>> x = np.array([1.90642, 2.22488, 2.10288, 1.69742, 1.52229, 3.15435, 2.61826, 1.98492, 1.42738, 1.99568])
        >>> andersondarling_test = AndersonDarling()
        >>> andersondarling_test.fit(x)
        >>> andersondarling_test.to_xlsx(file_name="my_data")
            The data has been exported to the 'my_data.xlsx' file

        Download the exported file by :download:`clicking here <assets/my_data.xlsx>`.


        **Export with personalized sheet name**

        >>> from pycafee.normalitycheck.andersondarling import AndersonDarling
        >>> import numpy as np
        >>> x = np.array([1.90642, 2.22488, 2.10288, 1.69742, 1.52229, 3.15435, 2.61826, 1.98492, 1.42738, 1.99568])
        >>> andersondarling_test = AndersonDarling()
        >>> andersondarling_test.fit(x)
        >>> andersondarling_test.to_xlsx(file_name="andersondarling_test", sheet_names=["sample", "data"])
            The data has been exported to the 'andersondarling_test.xlsx' file

        Download the exported file by :download:`clicking here <assets/andersondarling_test.xlsx>`.

        """
        if self.msg is None:
            fk_id_function = management._query_func_id("AndersonDarling")
            messages = management._get_messages(fk_id_function, self.language, "AndersonDarling")
            general._display_one_line_attention(messages[1][0][0])
        else:
            # quering
            fk_id_function = management._query_func_id("to_xlsx")
            messages = management._get_messages(fk_id_function, self.language, "to_xlsx")

            # batizando o nome do arquivo
            if file_name is None:
                file_name = "andersondarling"
            else:
                checkers._check_is_str(file_name, 'file_name', self.language)
                helpers._check_forbidden_character(file_name, "file_name", self.language)
            ## verificando o sheet_names
            if sheet_names is None:
                sheet_names = [
                    "andersondarling",
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
            name = "AndersonDarling" + messages[4][0][0]
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
            The name of the file to be exported, without its extension (default is ``None``, which results in a file named ``'andersondarling.csv'``)
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
        fit : performs the Anderson Darling Normality test.

        References
        ----------
        .. [1] pandas. pandas.DataFrame.to_csv. Available at: `pd.to_csv <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html>`_. Accessed on: 10 May 2022.

        Examples
        --------
        **Export with default settings**

        >>> from pycafee.normalitycheck.andersondarling import AndersonDarling
        >>> import numpy as np
        >>> x = np.array([1.90642, 2.22488, 2.10288, 1.69742, 1.52229, 3.15435, 2.61826, 1.98492, 1.42738, 1.99568])
        >>> andersondarling_test = AndersonDarling()
        >>> andersondarling_test.fit(x)
        >>> andersondarling_test.to_csv()
            The 'andersondarling.csv' file was exported!

        Download the exported file by :download:`clicking here <assets/andersondarling.csv>`.


        **Export with personalized file name**

        >>> from pycafee.normalitycheck.andersondarling import AndersonDarling
        >>> import numpy as np
        >>> x = np.array([1.90642, 2.22488, 2.10288, 1.69742, 1.52229, 3.15435, 2.61826, 1.98492, 1.42738, 1.99568])
        >>> andersondarling_test = AndersonDarling()
        >>> andersondarling_test.fit(x)
        >>> andersondarling_test.to_csv(file_name="my_data")
            The 'my_data.csv' file was exported!

        Download the exported file by :download:`clicking here <assets/my_data.csv>`.

        """

        if self.msg is None:
            fk_id_function = management._query_func_id("AndersonDarling")
            messages = management._get_messages(fk_id_function, self.language, "AndersonDarling")
            general._display_one_line_attention(messages[1][0][0])

        else:
            # batizando o nome do arquivo
            if file_name is None:
                file_name = "andersondarling"
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
            name = "AndersonDarling" + messages[2][0][0]
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
            fk_id_function = management._query_func_id("AndersonDarling")
            messages = management._get_messages(fk_id_function, self.language, "AndersonDarling")
            return messages[1][0][0]
        else:
            return self.msg

    def __repr__(self):
        fk_id_function = management._query_func_id("AndersonDarling")
        messages = management._get_messages(fk_id_function, self.language, "AndersonDarling")
        return messages[2][0][0]











# oh may God I see the way you shine     https://youtu.be/rl9FFZZnWWo?t=14
