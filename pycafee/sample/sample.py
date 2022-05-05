"""This module concentrates a sample evaluation functions/classes

Function list:



"""


#########################################
################ Imports ################
#########################################

###### Standard ######


###### Third part ######
import numpy as np
import pandas as pd
from tabulate import tabulate

###### Home made ######
from pycafee.utils import helpers
from pycafee.utils import general
from pycafee.utils.helpers import LanguageManagment
from pycafee.functions import functions
from pycafee.functions.functions import MakePlots



###########################################
################ Functions ################
###########################################

# class Sample():
class Sample(LanguageManagment):
    """
    This class contains single-sample evaluation methods.
    """

    def __init__(self, name=None, units=None, n_trunc=3, language=None, **kwargs): # alfa=None, n_digits=None,
        super().__init__(language=language, **kwargs) #alfa=alfa, n_digits=n_digits,
        # messages = ['dict']['0']['0']
        messages = "Sample"
        if name is None:
            name = messages
        if units is None:
            pass
        self.name = name
        self.units = units
        self.n_trunc = n_trunc
        # medidas de tendencia central
        self.mean = None
        self.median = None
        self.moda = None

        # medidas de dispersão
        self.std = None
        self.variance = None
        self.covariance = None
        self.Q1 = None
        self.Q3 = None
        self.DI = None

    ###################
    ###### Plots ######
    ###################

    def draw_dot_plot(self, width=None, height=None, n_ticks=None, export=False, file_name=None, extension=None, dpi=None,tight=True, transparent=False):
        """
        """
        if file_name is None:
            file_name = self.name + "_dot_plot"

        x, y = functions.make_dot_plot(x_exp=self.x_exp, width=width, height=height, n_ticks=n_ticks, export=export, file_name=file_name, extension=extension, dpi=dpi, tight=tight, transparent=transparent)
        return x, y

    def draw_density_function(self, bw_method=None, which=None, width='default', height='default', export=None, file_name=None, extension=None, dpi=None, tight=None, transparent=None, plot_design='default'):
        """
        """
        if file_name is None:
            file_name = self.name + "_density_function"
        x_exp = self.x_exp
        plot = MakePlots()
        x, y, central_tendency = plot.draw_density_function(
                    x_exp, bw_method, which, width, height, export, file_name, extension, dpi, tight, transparent, plot_design
                )
        return x, y, central_tendency



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


    def dispersion_measurements(self,show=True):
        """This function shows and creates a DataFrame for the measures of dispersion (variance, standard deviation, coeficiente de variação, distância interquartilica.)
        """
        #C:\Users\ander\Cursos\01 - STAT basica\02 - Análise exploratória de dados\01
        # cheking if show is valid parameter

        helpers._print_data(show)


    def central_tendency_measurements(self, show=True):
        """This function shows and creates a DataFrame for the measures of central tendency (mean, median and mode)
        """
        # cheking if show is valid parameter
        helpers._print_data(show)
        ## making the first column
        first_column = ['Mean', 'Median', "Mode"]
        ## making the second column
        # first, get keys from mode
        chaves = list(self.mode.keys())
        # second, creates the column with just one mode
        second_column = [
                helpers._truncate(self.mean, self.n_trunc),
                helpers._truncate(self.median, self.n_trunc),
                f"{helpers._truncate(chaves[0], self.n_trunc)} ({self.mode[chaves[0]]})"
            ]
        # third, creates the same column with just one mode but without truncate (to export)
        second_column_for_df = [
                self.mean,
                self.median,
                f"{chaves[0]} ({self.mode[chaves[0]]})"
            ]
        # fourth, adds ohter modes, if there is more than one 1 mode
        for i in range(len(self.mode)-1):
            first_column.append("Mode")
            second_column.append(f"{helpers._truncate(chaves[i+1], self.n_trunc)} ({self.mode[chaves[i+1]]})")
            second_column_for_df.append(f"{chaves[i+1]} ({self.mode[chaves[i+1]]})")
        ## creating a dict to print the results and other one to export
        # if the data does not have units
        if self.units is None:
            data = {
                'Measurements': first_column,
                'Values': second_column,
            }
            data_for_df = {
                'Measurements': first_column,
                'Values': second_column_for_df,
            }
            colalign = ["center", "center"]
        # if the data has units
        else:
            third_column = [self.units]*len(first_column)
            data = {
                'Measurements': first_column,
                'Values': second_column,
                'Unit': third_column
            }
            data_for_df = {
                'Measurements': first_column,
                'Values': second_column_for_df,
                'Unit': third_column
            }
            colalign = ["center", "center", "center"]
        if show == True:
            print(tabulate(data, headers="keys", tablefmt="rst", floatfmt=(f".{self.n_trunc}f"), colalign=colalign))
        else:
            pass
        return pd.DataFrame(data_for_df)

    def central_tendency_measurements_to_csv(self, file_name, show=False):
        try:
            raise FutureWarning("Not implemented yet")
        except:
            general._display_one_line_attention("    This method was not implemented yet!    ")
            raise




    def std_summary(self, show=True):
        helpers._print_data(show)
        if self.units is None:
            data = {
                'mean - std': [self.mean - self.std],
                'mean': [self.mean],
                'mean + std': [self.mean + self.std],
            }
            colalign = ["center", "center", "center"]
        else:
            data = {
                'mean - std (' + self.units + ')': [self.mean - self.std],
                'mean (' + self.units + ')': [self.mean],
                'mean + std (' + self.units + ')': [self.mean + self.std],
            }
            colalign = ["center", "center", "center"]
        if show == True:
            print(tabulate(data, headers="keys", tablefmt="rst", floatfmt=f".{self.n_trunc}f", colalign=colalign))
        else:
            pass
        return pd.DataFrame(data)
    # precisa de melhoria, veja o summary_to_csv
    def std_summary_to_csv(self, file_name=None, show=False):
        if file_name is None:
            file_name=self.name + "_std"
        helpers._print_data(show)
        df_summary = self.summary(show=show)
        helpers._export_to_csv(df_summary,file_name=file_name)




    def summary(self, show=True):
        helpers._print_data(show)
        if self.units is None:
            data = {
                'Parameters': ['Mean', "Standard deviation", "Variance"],
                self.name: [self.mean, self.std, self.variance],
            }
            colalign = ["left", "center"]
        else:
            data = {
                'Parameters': ['Mean', "Standard deviation", "Variance"],
                self.name: [self.mean, self.std, self.variance],
                "Units": [self.units, self.units, f"({self.units})\u00b2"],
            }

            colalign = ["left", "center", "center"]
        if show == True:
            print(tabulate(data, headers="keys", tablefmt="rst", floatfmt=f".{self.n_trunc}f", colalign=colalign))
        else:
            pass
        df_exp = pd.DataFrame(columns=['Supplied data'], data=self.x_exp)
        return pd.DataFrame(data), df_exp

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

    def evaluate(self, x_exp):
        """É o principal método onde a mágica não acontece.

        """
        self.x_exp = x_exp
        self.mean = np.mean(self.x_exp)
        self.median = np.median(self.x_exp)
        self.mode = functions.multimode(self.x_exp)
        self.std = np.std(self.x_exp, ddof=1)
        self.variance = np.var(self.x_exp, ddof=1)








    def __str__(self):
        if self.mean is None:
            return f"{self.name}"
        else:
            # connect with database
            # messages = ['dict']['0']['0']
            messages = "with mean"
            return f"{self.name} {messages} = {round(self.mean, self.n_trunc)} +/- {round(self.std, self.n_trunc)}"

    def __repr__(self):
        return self.name
