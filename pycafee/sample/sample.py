"""This module concentrates a sample evaluation functions/classes
"""


#########################################
################ Imports ################
#########################################

###### Standard ######


###### Third part ######
import numpy as np
import pandas as pd
from tabulate import tabulate
import scipy.stats as stats

###### Home made ######
from pycafee.utils import helpers
from pycafee.utils import general
from pycafee.utils import checkers

from pycafee.utils.helpers import AlphaManagement, NDigitsManagement
from pycafee.functions import functions


from pycafee.normalitycheck.normalitycheck import NormalityCheck


from pycafee.database_management import management

###########################################
################ Functions ################
###########################################


class Sample(AlphaManagement, NDigitsManagement):
    """
    """


    def __init__(self, name=None, alfa=None, language=None, n_digits=None, **kwargs):
        super().__init__(alfa=alfa, language=language, n_digits=n_digits, **kwargs)
        if name is None:
            fk_id_function = management._query_func_id("Sample")
            messages = management._get_messages(fk_id_function, self.language)
            self.name = messages[4][0][0]
        else:
            checkers._check_is_str(name, "name", self.language)
            self.name = name
        self.mean = None
        self.normality_result = None # tupla com os resultados
        self.normality_conclusion = None # str com o resultado
        self.normality_test = None # qual teste foi aplicado


    # with tests, with docstring, the database comes from Sample
    def normality_check(self, show=True):
        """This function prints a table with the Normality test results.

        Parameters
        ----------
        show : ``bool``, optional
            This parameter defines whether the Normality test results will be printed (``True``) or not (``False``).

        Returns
        -------
        df : :doc:`DataFrame <pandas:reference/api/pandas.DataFrame>`
            A DataFrame with the Normality test results

        """

        checkers._check_is_bool(show, "show", self.language)

        if self.mean is None:
            helpers._raises_when_fit_was_not_applied("Sample", self.language, self.name)

        else:
            colalign = []
            data = self.normality_result._asdict()
            for key, values in data.items():
                if values is None:
                    data[key] = ["-"]
                else:
                    data[key] = [values]
                colalign.append("center")
            if show:
                print(self.normality_test)
                print(tabulate(data, headers="keys", tablefmt="rst", colalign=colalign))
                print(self.normality_conclusion)
            df = pd.DataFrame(data)
            return df

    # with tests, with docstring, the database comes from Sample
    def summary(self, show=True):
        """This function prints a table with a summary of the sample, which contains the mean, the variance, the standard deviation, the estimated confidence interval with alpha significance level, and the coefficient of variation.

        Parameters
        ----------
        show : ``bool``, optional
            This parameter defines whether the results will be printed (``True``) or not (``False``).

        Returns
        -------
        df : :doc:`DataFrame <pandas:reference/api/pandas.DataFrame>`
            A DataFrame with the summarized data.

        """
        checkers._check_is_bool(show, "show", self.language)

        if self.mean is None:
            helpers._raises_when_fit_was_not_applied("Sample", self.language, self.name)
        else:
            fk_id_function = management._query_func_id("Sample")
            messages = management._get_messages(fk_id_function, self.language)
            colalign = []
            ic = f"{messages[9][0][0]} ({100*(1-self.alfa)}%)"
            data = {
                messages[6][0][0]: [self.mean],
                messages[7][0][0]: [self.variance],
                messages[8][0][0]: [self.std],
                ic: [self.t_interval],
                messages[10][0][0]: [self.cv]
            }
            colalign = ["center", "center", "center", "center", "center"]
            if show:
                print(self.name)
                print(tabulate(data, headers="keys", tablefmt="rst", floatfmt=(f".{self.n_digits}f"), colalign=colalign))
            df = pd.DataFrame(data)
            return df

    # with tests, with docstring, the database comes from Sample
    def standard_interval(self, show=True):
        """This function prints a table with the estimated standard deviation range for the sample.

        Parameters
        ----------
        show : ``bool``, optional
            This parameter defines whether the results will be printed (``True``) or not (``False``).

        Returns
        -------
        df : :doc:`DataFrame <pandas:reference/api/pandas.DataFrame>`
            A DataFrame with the standard table.

        """
        checkers._check_is_bool(show, "show", self.language)

        if self.mean is None:
            helpers._raises_when_fit_was_not_applied("Sample", self.language, self.name)
        else:
            fk_id_function = management._query_func_id("Sample")
            messages = management._get_messages(fk_id_function, self.language)
            colalign = []
            data = {
                f"{messages[6][0][0]} - s": [self.mean - self.std],
                f"{messages[6][0][0]}": [self.mean],
                f"{messages[6][0][0]} + s": [self.mean + self.std],
            }
            colalign = ["center", "center", "center"]
            if show:
                print(self.name)
                print(tabulate(data, headers="keys", tablefmt="rst", floatfmt=(f".{self.n_digits}f"), colalign=colalign))
            df = pd.DataFrame(data)
            return df

    # with tests, with docstring, the database comes from Sample
    def confidencial_interval(self, show=True):
        """This function prints a table with the estimated confidential interval range for the sample.

        Parameters
        ----------
        show : ``bool``, optional
            This parameter defines whether the results will be printed (``True``) or not (``False``).

        Returns
        -------
        df : :doc:`DataFrame <pandas:reference/api/pandas.DataFrame>`
            A DataFrame with the confidential interval table.

        """
        checkers._check_is_bool(show, "show", self.language)

        if self.mean is None:
            helpers._raises_when_fit_was_not_applied("Sample", self.language, self.name)
        else:
            fk_id_function = management._query_func_id("Sample")
            messages = management._get_messages(fk_id_function, self.language)
            colalign = []
            data = {
                f"{messages[6][0][0]} - IC": [self.mean - self.t_interval],
                f"{messages[6][0][0]}": [self.mean],
                f"{messages[6][0][0]} + IC": [self.mean + self.t_interval],
            }
            colalign = ["center", "center", "center"]
            if show:
                print(self.name)
                print(tabulate(data, headers="keys", tablefmt="rst", floatfmt=(f".{self.n_digits}f"), colalign=colalign))
                print(f"{messages[11][0][0]} {100*(1-self.alfa)}{messages[11][2][0]}.")
            df = pd.DataFrame(data)
            return df

    # with tests, with docstring, the database comes from Sample
    def positional_summary(self, show=True):
        """This function prints a table with the minimum, the first quartile, the median, the third quartile, the maximum, and the interquartile range estimated for the sample.

        Parameters
        ----------
        show : ``bool``, optional
            This parameter defines whether the Normality test results will be printed (``True``) or not (``False``).

        Returns
        -------
        df : :doc:`DataFrame <pandas:reference/api/pandas.DataFrame>`
            A DataFrame with the Normality test results

        """
        checkers._check_is_bool(show, "show", self.language)
        if self.mean is None:
            helpers._raises_when_fit_was_not_applied("Sample", self.language, self.name)
        else:
            fk_id_function = management._query_func_id("Sample")
            messages = management._get_messages(fk_id_function, self.language)
            colalign = []
            data = {
                messages[12][0][0]: [self.min],
                messages[13][0][0]: [self.Q1],
                messages[14][0][0]: [self.median],
                messages[15][0][0]: [self.Q3],
                messages[16][0][0]: [self.max],
                messages[17][0][0]: [self.DI]
            }
            colalign = ["center", "center", "center", "center", "center", "center"]
            if show:
                print(self.name)
                print(tabulate(data, headers="keys", tablefmt="rst", floatfmt=(f".{self.n_digits}f"), colalign=colalign))
            df = pd.DataFrame(data)
            return df


    def compare(self, value, show=True, normality=None):
        """
        Esta função compara a amostra com um valor pré-definido.
        """

        if normality is None:
            normality = self.normality_conclusion
        elif normality == True:
            normality = 1
        else:
            normality = 0


        if normality:
            print('t-student')
        else:
            print("wilcox")




    def check_outliers(self, show=True):
        """Esta função verifica se existem possíveis outliers em uma amostra
        """
        pass


    def fit(self, x_exp, norm_test=None, alfa=None, conclusion=None, details=None):
        """É o principal método onde a mágica não acontece.

        Parameters
        ----------
        x_exp : ``numpy array``
            One dimension :doc:`numpy array <numpy:reference/generated/numpy.array>` with at least ``3`` sample data, except for the Lilliefors and Abdi-Molin tests, which must have at least ``4`` samples.

        norm_test : ``str``

        alfa : ``float``

        conclusion : ``str``

        details : ``str``



        """
        if alfa is None:
            alfa = self.alfa
        else:
            self.alfa = alfa
        self.x_exp = x_exp

        #########################
        ### Normal like stats ###
        #########################
        # with tests
        self.mean = np.mean(self.x_exp)
        self.std = np.std(self.x_exp, ddof=1)
        self.variance = np.var(self.x_exp, ddof=1)
        self.cv = 100*self.std/self.mean
        self.t_student = np.abs(stats.t.ppf(self.alfa/2, self.x_exp.size - 1))
        self.t_interval = self.std*self.t_student/np.sqrt(self.x_exp.size)


        #############################
        ### Not Normal like stats ###
        ############################
        # with tests
        self.median = np.median(self.x_exp)
        self.min = self.x_exp.min()
        self.max = self.x_exp.max()
        self.Q1 = np.quantile(self.x_exp, 0.25, interpolation="linear") # vai precisar implementar outros métodos no futuro
        self.Q3 = np.quantile(self.x_exp, 0.75, interpolation="linear") # vai precisar implementar outros métodos no futuro
        self.DI = self.Q3 - self.Q1
        self.mode = functions.multimode(self.x_exp)







        ######################
        ### Normality test ###
        ######################
        # with tests
        normality_test = NormalityCheck(language=self.language, n_digits=self.n_digits)
        self.normality_result, self.normality_conclusion = normality_test.fit(
                        x_exp=self.x_exp,
                        test=norm_test,
                        conclusion=conclusion,
                        details=details,
                        alfa=self.alfa
                    )
        self.normality_test = normality_test.normality_test




    def __str__(self):
        if self.mean is None:
            fk_id_function = management._query_func_id("Sample")
            messages = management._get_messages(fk_id_function, self.language)
            return f"{messages[2][0][0]} {self.name}"
        else:
            fk_id_function = management._query_func_id("Sample")
            messages = management._get_messages(fk_id_function, self.language)

            return f"{self.name} {messages[5][0][0]} = {helpers._truncate(self.mean, self.language, decs=self.n_digits)} +/- {helpers._truncate(self.std, self.language, decs=self.n_digits)}"

    def __repr__(self):
        fk_id_function = management._query_func_id("Sample")
        messages = management._get_messages(fk_id_function, self.language)
        return messages[3][0][0]












#
# # class Sample():
# class Samples(LanguageManagement):
#     """
#     This class contains single-sample evaluation methods.
#     """
#
#     def __init__(self, name=None, units=None, n_trunc=3, language=None, **kwargs): # alfa=None, n_digits=None,
#         super().__init__(language=language, **kwargs) #alfa=alfa, n_digits=n_digits,
#         # messages = ['dict']['0']['0']
#         messages = "Sample"
#         if name is None:
#             name = messages
#         if units is None:
#             pass
#         self.name = name
#         self.units = units
#         self.n_trunc = n_trunc
#         # medidas de tendencia central
#         self.mean = None
#         self.median = None
#         self.moda = None
#
#         # medidas de dispersão
#         self.std = None
#         self.variance = None
#         self.covariance = None
#         self.Q1 = None
#         self.Q3 = None
#         self.DI = None
#
#
#
#

    ###################
    ###### Plots ######
    ###################

    # def draw_dot_plot(self, width=None, height=None, n_ticks=None, export=False, file_name=None, extension=None, dpi=None,tight=True, transparent=False):
    #     """
    #     """
    #     if file_name is None:
    #         file_name = self.name + "_dot_plot"
    #
    #     x, y = functions.make_dot_plot(x_exp=self.x_exp, width=width, height=height, n_ticks=n_ticks, export=export, file_name=file_name, extension=extension, dpi=dpi, tight=tight, transparent=transparent)
    #     return x, y
    #
    # def draw_density_function(self, bw_method=None, which=None, width='default', height='default', export=None, file_name=None, extension=None, dpi=None, tight=None, transparent=None, plot_design='default'):
    #     """
    #     """
    #     if file_name is None:
    #         file_name = self.name + "_density_function"
    #     x_exp = self.x_exp
    #     plot = MakePlots()
    #     x, y, central_tendency = plot.draw_density_function(
    #                 x_exp, bw_method, which, width, height, export, file_name, extension, dpi, tight, transparent, plot_design
    #             )
    #     return x, y, central_tendency



    def draw_boxplot(self):
        try:
            raise FutureWarning("Not implemented yet")
        except:
            general._display_one_line_attention("    This method was not implemented yet!    ")
            raise


    def draw_histogram(self):
        try:
            raise FutureWarning("Not implemented yet")
        except:
            general._display_one_line_attention("    This method was not implemented yet!    ")
            raise


    def draw_scatter_plot(self):
        try:
            raise FutureWarning("Not implemented yet")
        except:
            general._display_one_line_attention("    This method was not implemented yet!    ")
            raise

    # def compare_with_constant(self):
    #     pass
    #
    # def normality_test(self, test):
    #     pass
    #

    #
    # def interval_summary(self):
    #     pass
    #
    # def quartilic_summary(self):
    #     pass








    def summary_to_csv(self, file_name=None, show=False,sep=","):
        """Esta função exporta o dataframe criado em summary para .csv
        """
        # batizando o nome do arquivo
        if file_name is None:
            file_name=self.name + "_summary"
        else:
            file_name=self.name
        # verificando se o paramentro show é valido e o que fazer
        helpers._print_data(show)
        # obtendo o dataframe de summary
        df_summary, df_exp = self.summary(show=show)
        ## adicionando os dados fornecidos para o arquivo que será exportado
        # criando um novo df com os dados verdadeiros
        # df_exp = pd.DataFrame(columns=['Supplied data'], data=self.x_exp)
        # concaatenando o dataframe criando em summary com o DataFrame com os dados verdadeiros
        df_summary = pd.concat([df_summary, df_exp], ignore_index=False, axis=1)
        # substituindo todos os NaN por uma string vazia
        df_summary.fillna("", inplace=True)
        # exportando em si
        result = helpers._export_to_csv(df_summary, file_name=file_name, sep=sep)
        return result

    def summary_to_xlsx(self, file_name=None, sheet_names=None, extension="xlsx"):
        """This method exports the data created in the summary method to excel type files

        Parameters
        ----------
        file_name : string (default None)
            The name of the file to be exported, without its extension. If None --> self.name + "_summary"
        sheet_names : list of two strings (default None)
            A list containing the name of the worksheets where the data will be saved.
            --> The first name corresponds to the name of the worksheet where the calculated data will be saved. If None --> self.name + "_summary"
            --> The second name corresponds to the name of the worksheet where the original data will be saved. If None --> data
        extension: string ("xlsx" or "xls", default "xlsx")
            The extension of the file that will be created.
        """
        # verificando o file_name
        if file_name is None:
            file_name = self.name + "_summary"
        else:
            helpers._check_is_str(file_name, "file_name")
            helpers._check_forbidden_character(file_name, "file_name")
        ## verificando o sheet_names
        if sheet_names is None:
            sheet_names = [
                self.name + "_summary",
                "data"
            ]
        else:
            # verificando se é uma lista
            helpers._check_is_list(sheet_names, "sheet_names")
            # verificando se a lista tem 2 elementos
            if len(sheet_names) != 2:
                try:
                    raise ValueError("Wrong size error!")
                except ValueError:
                    # "query"
                    message1 = "The parameter" #message
                    message2 = "must have 2 elements, but we got" #message
                    sheet_names = [f"  --->  {sheet}" for sheet in sheet_names]
                    msg = [
                        f"{message1} 'sheet_names' {message2}: {len(sheet_names)}",
                        sheet_names
                        ]
                    msg = general._flatten_list_of_list_string(msg)
                    msg = list(msg)
                    general._display_n_line_attention(msg)
                    raise
            # verficanado se cada elemento da lista é uma string valida
            for sheet_name in sheet_names:
                helpers._check_is_str(sheet_name, "sheet_names")
                helpers._check_forbidden_character(sheet_name, "sheet_names")

        ### pegando o df_summary e o df_data

        df_list = self.summary(show=False)

        result = helpers._export_to_excel(df_list, file_name=file_name, sheet_names=sheet_names, extension=extension)
        return result

    def summary_to_pdf(self, file_name=None, show=False):
        #https://www.geeksforgeeks.org/convert-text-and-text-file-to-pdf-using-python/
        # file:///C:/Users/ander/github/curva_calibracao/relatorio.pdf
        try:
            raise FutureWarning("Not implemented yet")
        except:
            general._display_one_line_attention("    This method was not implemented yet!    ")
            raise

    def make_dashborad(self):
        try:
            raise FutureWarning("Not implemented yet")
        except:
            general._display_one_line_attention("    This method was not implemented yet!    ")
            raise
