"""This module concentrates the help functions to run the functions behind the scenes

"""


# Function list:
#
#     - LanguageManagment
#         - get_language(self)
#         - set_language(self, language)
#         - __str__(self)
#         - __repr__(self)
#
#     - AlphaManagement(LanguageManagment)
#         - get_alfa(self)
#         - set_alfa(self, alfa)
#         - __str__(self)
#         - __repr__(self)
#
#
#     - NDigitsManagement(LanguageManagment)
#         - get_n_digits(self)
#         - set_n_digits(self, n_digits)
#         - __str__(self)
#         - __repr__(self)
#
#     - _change_locale(language, decimal_separator=".", local="pt_BR")
#     - _change_locale_back_to_default(default_locale)
#     - _check_blank_space(value, param_name, language)
#     - _check_conflicting_filename(file_name, extension, language)
#     - _check_figure_extension(value, param_name, language)
#     - _check_file_exists(file_name)
#     - _check_file_name_is_str(file_name, language)
#     - _check_forbidden_character(value, param_name, language)
#     - _check_plot_design(plot_design, param_name, plot_design_default, plot_design_example, language)
#     - _check_which_density_gaussian_kernal_plot(which, language)
#     - _export_to_csv(df, file_name="my_data", sep=',', language)
#     - _export_to_xlsx(df_list, language, file_name=None, sheet_names=[None,None])
#     - _flat_list_of_lists(my_list, param_name, language)
#     - _sep_checker(sep, language)
#     - _truncate(value, language, decs=None)



#########################################
################ Imports ################
#########################################

###### Standard ######
import locale
import logging
from pathlib import Path
import traceback

###### Third part ######
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

###### Home made ######
from cup_of_coffee.database_management import management
from cup_of_coffee.utils import general
from cup_of_coffee.utils import checkers


###########################################
################ Functions ################
###########################################



# with test, with database, with docstring
class LanguageManagement:
    """Instantiates a class for language management. This class is primarily for internal use.

    """

    def __init__(self, language=None, **kwargs):
        super().__init__(**kwargs)
        """Constructs the name of the language

        Parameters
        ----------
        language : string
            The abreviation of a language (dafualt None, which means 'en')

        Notes
        -----
        The method does not allow the input of values that are not of type string and that have lenght higher than 5 (due to the database restrictions)

        """
        all_languages = management._get_all_available_languages()
        current_default_language = management._get_current_default_language()

        # Obtendo o idioma padrão #
        if language is None:
            self.language = management._get_current_default_language()
        # Caso queria alterar o valor diretamente ao instanciar a classe
        else:
            # verificando se o valor passado é uma string
            checkers._check_is_str(language, "language", current_default_language)
            # agora verificando se o valor passado é um idioma válido
            if language not in all_languages.keys():
                all_formated_languages = [f"  --->  {lang}" for lang in all_languages]
                fk_id_function = management._query_func_id("LanguageManagment")
                messages = management._get_messages(fk_id_function, current_default_language)
                try:
                    raise ValueError(messages[1][0][0])
                except ValueError:
                    msg = [
                        f"{messages[2][0][0]} '{language}' {messages[2][2][0]}",
                        f"{messages[2][3][0]}",
                        all_formated_languages
                    ]
                    msg = general._flatten_list_of_list_string(msg)
                    msg = list(msg)
                    general._display_n_line_attention(msg)
                    raise
            else:
                self.language = language

    def get_language(self):
        """Gets the current language
        """
        return self.language

    def set_language(self, language):
        """Changes the current language

        Parameters
        ----------
        language : ``str``
            The language code

        Notes
        -----
        The ``language`` must be a ``str`` with no more then ``5`` elements.

        """
        all_languages = management._get_all_available_languages()
        # verificando se o valor passado é uma string
        checkers._check_is_str(language, "language", self.language)
        # agora verificando se o valor passado é um idioma válido
        if language not in all_languages.keys():
            all_formated_languages = [f"  --->  {lang}" for lang in all_languages]
            fk_id_function = management._query_func_id("LanguageManagment")
            messages = management._get_messages(fk_id_function, self.language)
            try:
                raise ValueError(messages[1][0][0])
            except ValueError:
                msg = [
                    f"{messages[2][0][0]} '{language}' {messages[2][2][0]}",
                    f"{messages[2][3][0]}",
                    all_formated_languages
                ]
                msg = general._flatten_list_of_list_string(msg)
                msg = list(msg)
                general._display_n_line_attention(msg)
                raise
        else:
            self.language = language

    def __str__(self):
        fk_id_function = management._query_func_id("LanguageManagement")
        messages = management._get_messages(fk_id_function, self.language)
        return f"{messages[5][0][0]} '{self.language}'"

    def __repr__(self):
        return self.language

# with test, with database, with docstring
class AlphaManagement(LanguageManagement):
    """Instanciates a class for alpha managment.

    """

    def __init__(self, alfa=None, **kwargs):
        super().__init__(**kwargs)
        """Constructs the significance level value

        Parameters
        ----------
        alfa : ``float``
            The significance level (default is ``None``, which means ``0.05``)

        Notes
        -----
        This method only allows input of type ``float`` and between ``0.0`` and ``1.0``.

        """

        if alfa is None:
            self.alfa = 0.05
        else:
            checkers._check_is_float(alfa, "alfa", self.language)
            checkers._check_data_in_range(alfa, "alfa", 0.0, 1.0, self.language)
            self.alfa = alfa

    def get_alfa(self):
        """Gets the current ``alpha`` value
        """
        return self.alfa

    def set_alfa(self, alfa):
        """Changes the ``alpha`` value

        Parameters
        ----------
        alfa : ``float``
            The new significance level

        Notes
        -----
        This method only allows input of type ``float`` and between ``0.0`` and ``1.0``.

        """
        checkers._check_is_float(alfa, "alfa", self.language)
        checkers._check_data_in_range(alfa, "alfa", 0.0, 1.0, self.language)
        self.alfa = alfa

    def __repr__(self):
        return self.alfa

    def __str__(self):
        fk_id_function = management._query_func_id("AlphaManagement")
        messages = management._get_messages(fk_id_function, self.language)
        return f"{messages[1][0][0]} '{self.alfa}'"

# with test, with database, with docstring
class NDigitsManagement(LanguageManagement):
    """Instanciates a class for n_digits managment.

    """
    def __init__(self, n_digits=None, **kwargs):
        super().__init__(**kwargs)
        """Constructs the n_digits value

        Parameters
        ----------
        n_digits : ``int``
            The maximum number of decimal places that the calculated parameters can have, ``default = 4``.

        Notes
        -----
        This method only accepts ``int`` values higher than ``0``.

        """
        if n_digits is None:
            self.n_digits = 4
        else:
            checkers._check_is_integer(n_digits, "n_digits", self.language)
            checkers._check_is_positive(n_digits, "n_digits", self.language)
            self.n_digits = n_digits

    def get_n_digits(self):
        """Gets the ``n_digits`` parameter
        """
        return self.n_digits

    def set_n_digits(self, n_digits):
        """Sets the ``n_digits`` parameter

        Parameters
        ----------
        n_digits : ``int``
            The maximum number of decimal places to be shown.

        """
        checkers._check_is_integer(n_digits, "n_digits", self.language)
        checkers._check_is_positive(n_digits, "n_digits", self.language)
        self.n_digits = n_digits

    def __repr__(self):
        return self.n_digits

    def __str__(self):
        fk_id_function = management._query_func_id("NDigitsManagement")
        messages = management._get_messages(fk_id_function, self.language)
        return f"{messages[1][0][0]} '{self.n_digits}'"

# with tests, with text, with database, with docstring
def _change_locale(language, decimal_separator=".", local="pt_BR"):
    """This function momentarily changes the decimal separator used in charts.

    Parameters
    ----------
    decimal_separator : string (default ".")
        The decimal separator symbol. It can be the dot (default '.') or the comma (',').
    local : string (default "pt_BR")
        The alias for the desired locale. Only used if decimal_separator is a comma, setting matplolib's default value. Its only function is to change the decimal separator symbol and should be changed only if the "pt_BR" option is not available.
    language : string
        The language code

    Notes
    -----
    The parameter 'language' isn't checked if it is a string.

    Returns
    -------
    default_locale : The user's system default value (string or None)
        - None if the default values are used
        - String with the user's system default value, which will be passed to the _change_locale_back_to_default() function to restore the user's default value

    Notes
    -----
    This function must always be used in conjunction with the _change_locale_back_to_default(default_locale) function.

    """
    # conferindo o local
    checkers._check_is_str(local, "local", language)
    # conferindo o decimal_separator
    checkers._check_is_str(decimal_separator, "decimal_separator", language)
    current_decimal_separator_available = [".", ","]
    # querring
    func_name = "_change_locale"
    fk_id_function = management._query_func_id(func_name)
    messages = management._get_messages(fk_id_function, language, func_name)
    if decimal_separator not in current_decimal_separator_available:
        try:
            raise ValueError(messages[1][0][0])
        except ValueError:
            general._display_one_line_attention(
                    f"{messages[2][0][0]} 'decimal_separator' {messages[2][2][0]} '{decimal_separator}'",
                                )
            raise
    if decimal_separator == ",":
        default_locale = locale.getdefaultlocale()[0]
        try:
            locale.setlocale(locale.LC_NUMERIC, local)
            plt.rcParams['axes.formatter.use_locale'] = True
        except locale.Error:
            general._display_one_line_attention(
                f"{messages[3][0][0]} {local} {messages[3][2][0]}"
            )
            raise
    else:
        default_locale = None
    return default_locale

# with a test, no text, no database, with docstring
def _change_locale_back_to_default(default_locale):
    """This function restores the local parameter to its default value.

    Parameters
    ----------
    default_locale : string
        The default value of locale, which is obtained through the _change_locale() function

    Notes
    -----
    This function must always be used in conjunction with the _change_locale(decimal_separator=".", local="pt_BR") function.

    """
    if default_locale is not None:
        locale.setlocale(locale.LC_NUMERIC, default_locale)
        plt.rcParams['axes.formatter.use_locale'] = False

# with tests, with text, with database, with docstring
def _check_blank_space(value, param_name, language):
    """This function checks if a string has white space

    The function compares the length of 'value' with the length of first element in value.split(). If these lengths are equal, 'value' has no white space.
    The function does not check if value is a string, and this should be done previously to prevent errors.

    Parameters
    ----------
    value : string
        The string to be evaluated
    param_name : string
        The param_name
    language : string
        The language code

    Notes
    -----
    The parameter 'param_name' isn't checked if it is a string.
    The parameter 'language' isn't checked if it is a string.


    Returns
    -------
        True is value does not have white space
        Raises ValueError if value has white space

    """
    checkers._check_is_str(value, param_name, language)
    value_size = len(value)
    value_split = value.split()[0]
    value_split_size = len(value_split)
    if value_size == value_split_size:
        return True
    else:
        func_name = "_check_blank_space"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        try:
            raise ValueError(messages[1][0][0])
        except ValueError:
            general._display_one_line_attention(
                                f"{messages[2][0][0]} '{value}' {messages[2][2][0]}",
                                )
            raise

# with test, with database, with docstring
def _check_conflicting_filename(file_name, extension, language):
    """This function checks if a file exists in the current directory. If it exists, it returns a different name for the file, so as not to overwrite existing files.

    Paramters
    ---------
    file_name : string
        The name of the file to be exported, without its extension
    extension : string
        The file extension
    language : string
        The language code

    Notes
    -----
    The parameter 'file_name' isn't checked if it is a string.
    The parameter 'extension' isn't checked if it is a string.
    The parameter 'language' isn't checked if it is a string.

    If the file_name + extension does not exists in the current directory, the output os file_name + "." + extension
    If the file_name + extension exists in the current directory, a string ("_n") is inserted at the end od the file_name (where n is a number). Is this is true, the user is wanrned about it.

    Returns
    -------
    file_name : string
        The file name that does not exists in the current directory

    """
    ### Baptism of Fire ###
    file = file_name + "." + extension
    # if the file already exists, create a new name for the file
    file_exists = _check_file_exists(file)
    if file_exists:
        ### quering ###
        func_name = "_check_conflicting_filename"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        i = 0
        msg_1 = f"{messages[1][0][0]} '{file}' {messages[1][2][0]}"
        # try to create a new name by adding a number to the end of the name.
        while file_exists:
            i += 1
            file = file_name + "_" + str(i) + "." + extension
            file_exists = _check_file_exists(file)
        file_name = file
        # warn that the file already exists
        # warn the user the name of the file to be exported
        general._display_n_line_warn([
                        f"    {messages[2][0][0]}",
                        msg_1,
                        f"{messages[3][0][0]} '{file_name}'"
                        ])
    else:
        file_name = file
    return file_name

# with test, with text, with database, with docstring
def _check_figure_extension(value, param_name, language):
    """This function checks if 'value' is one of the extensions available for exporting figures using matplotlib.

    The allowed extensions for matlab version 3.5 are:
        'eps'  : 'Encapsulated Postscript'
        'jpg'  : 'Joint Photographic Experts Group'
        'jpeg' : 'Joint Photographic Experts Group'
        'pdf'  : 'Portable Document Format'
        'pgf'  : 'PGF code for LaTeX'
        'png'  : 'Portable Network Graphics'
        'ps'   : 'Postscript'
        'raw'  : 'Raw RGBA bitmap'
        'rgba' : 'Raw RGBA bitmap'
        'svg'  : 'Scalable Vector Graphics'
        'svgz' : 'Scalable Vector Graphics'
        'tif'  : 'Tagged Image File Format'
        'tiff' : 'Tagged Image File Format'

    However, the options are checked using plt.gcf().canvas.get_supported_filetypes().

    Parameters
    ----------
    value : string
        The value to check if it is a valid extension for figure creation.
    param_name : string
        The original name of the parameter passed through the parameter 'value'.
    language : string
        The language code

    Notes
    -----
    The parameter 'param_name' isn't checked if it is a string.
    The parameter 'language' isn't checked if it is a string.

    To check the supported extensions on your system, use:

    >>> from matplotlib import pyplot as plt
    >>> suported_types = plt.gcf().canvas.get_supported_filetypes()
    >>> for key, value in suported_types.items():
            print(key, ":", value)
    >>> plt.close()
    Returns
    -------
    True if 'value' is an allowed extension.
    Raises ValueError is 'value' is not an allowed extension.


    """
    suported_types = plt.gcf().canvas.get_supported_filetypes()
    plt.close() # essencial, pois o acima criar uma figura em branco, e caso o código seja ativado vai criar essa fig em branco
    if value not in suported_types.keys():
        ### quering ###
        func_name = "_check_figure_extension"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        try:
            raise ValueError(messages[1][0][0])
        except ValueError:
            extensions_allowed = []
            for key, value in suported_types.items():
                extensions_allowed.append(f"    --->    '{key}':  {value}")

            msg = [
                f"{messages[2][0][0]} '{value}' {messages[2][2][0]} '{param_name}' {messages[2][4][0]}!",
                messages[3][0][0],
                extensions_allowed
                ]
            flat_list = general._flatten_list_of_list_string(msg)
            flat_list = list(flat_list)
            general._display_n_line_attention(
                flat_list
            )
            raise
    return True

# with tests, with no text with no database, with docstring
def _check_file_exists(file_name):
    """This function checks if a file already exists on the current folder

    Parameters
    ----------
    file_name : string
        The file name (with extension).

    Return
    ------
    True if file already exists
    or
    False if file does not exists

    """
    file = Path(file_name)
    if file.exists():
        return True
    else:
        return False

# with tests, with no text with no database, with docstring
def _check_file_name_is_str(file_name, language):
    """This function checks if a variable can be the name of a file, checking if it is of type string and if its size is greater than zero.

    Parameters
    ----------
    file_name : string
    language : string
        The language code

    Notes
    -----
    The parameter 'language' isn't checked if it is a string.

    """

    if isinstance(file_name, str) == False:
        ### quering ###
        func_name = "_check_file_name_is_str"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        try:
            raise ValueError(messages[1][0][0])
        except ValueError:
            general._display_one_line_attention(
                                text = f"{messages[2][0][0]} '{str(type(file_name).__name__)}'"
                                )
            raise
    if len(file_name) == 0:
        func_name = "_check_file_name_is_str"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        try:
            raise ValueError(messages[3][0][0])
        except ValueError:
            # "query"
            general._display_one_line_attention(
                                text = f"{messages[4][0][0]}"
                                )
            raise

# with tests, with text, with database, with docstring
def _check_forbidden_character(value, param_name, language):
    """This function checks if there are characters that can be problematic for a file name.

    Parameters
    ----------
    value : string
        The value to check if it has some espcific characters.
    param_name : string
        The original name of the parameter passed through the parameter 'value'.
    language : string
        The language code

    Notes
    -----
    The parameter 'param_name' isn't checked if it is a string.
    The parameter 'language' isn't checked if it is a string.

    This function checks if a string contains some characters that can be problematic for saving files.
    The forbidden characters are:

        "/": 'forward slash',
        "<": "less than",
        ">": "greater than",
        ":": "colon",
        "\"": "double quote",
        "\\": "back slash",
        "|": "vertical bar",
        "?": "question mark",
        "*": "asterisk",
        ".": "dot",
        ",": "comma",
        "[": "left square bracket",
        "]": "right square bracket",
        ";": "semicolon",

    Returns
    -------
    True if value does not have any forbidden.
    Raises ValueError is value is not a valid string.

    References
    ----------
    .. [1] https://stackoverflow.com/a/31976060/17872198
    .. [2] https://stackoverflow.com/q/1976007/17872198
    """
    list_of_forbbiden = {
        "/": 'forward slash',
        "<": "less than",
        ">": "greater than",
        ":": "colon",
        "\"": "double quote",
        "\\": "back slash",
        "|": "vertical bar",
        "?": "question mark",
        "*": "asterisk",
        ".": "dot",
        ",": "comma",
        "[": "left square bracket",
        "]": "right square bracket",
        ";": "semicolon",
    }
    for key in list_of_forbbiden.keys():
        if key in value:
            ### quering ###
            func_name = "_check_forbidden_character"
            fk_id_function = management._query_func_id(func_name)
            messages = management._get_messages(fk_id_function, language, func_name)
            try:
                raise ValueError(messages[1][0][0])
            except ValueError:
                list_of_charcater = list(list_of_forbbiden.keys())
                all_formated_characters = [f"    --->    '  {charcater}  '" for charcater in list_of_charcater]
                msg = [
                    f"{messages[2][0][0]} '{key}' ({list_of_forbbiden[key]}) {messages[2][2][0]}",
                    f"{messages[3][0][0]}",
                    all_formated_characters
                    ]
                flat_list = general._flatten_list_of_list_string(msg)
                flat_list = list(flat_list)
                general._display_n_line_attention(
                    flat_list
                )
                raise
    return True

# with tests, with text, with database, with docstring
def _check_plot_design(plot_design, param_name, plot_design_default, plot_design_example, language):
    """This function checks if the dictionary passed through the plot_desing parameter is correct.

    Parameters
    ----------
    plot_design : dict
        The dictionary to be tested, which is passed by the user
    param_name : string
        The name of the parameter being tested
    plot_design_default : dict
        A dictionary containing the default values to be compared with the plot_design
    plot_design_example: dict
        A dictionary with the same keys as plot_design, but the values are strings that are used as an example.
    language : string
        The language code

    Notes
    -----
    The parameter 'param_name' isn't checked if it is a string.
    The parameter 'language' isn't checked if it is a string.

    Returns
    -------
    True if 'plot_design' seems to be corret
    ValueError if 'plot_design' has something wrong

    """

    # Verificando se plot_design
    checkers._check_is_dict(plot_design, param_name, language)

    # lista com as chaves passadas
    data_keys_list = list(plot_design.keys())

    # lista com as chaves necessárias
    keys_list = list(plot_design_default.keys())

    # verificando o dicionário tem as chaves esperadas
    for chave in keys_list:
        if chave not in data_keys_list:
            ### quering ###
            func_name = "_check_plot_design"
            fk_id_function = management._query_func_id(func_name)
            messages = management._get_messages(fk_id_function, language, func_name)
            try:
                raise ValueError(messages[1][0][0])
            except ValueError:
                all_formated_keys = [f"    --->  '{key}'" for key in keys_list]
                msg = [
                    f"{messages[2][0][0]} '{chave}' {messages[2][2][0]}",
                    f"{messages[3][0][0]}",
                    all_formated_keys
                ]
                msg = general._flatten_list_of_list_string(msg)
                msg = list(msg)
                general._display_n_line_attention(msg)
                raise
    # verificando se o número de chaves passadas é correto
    if len(plot_design.keys()) != len(plot_design_default.keys()):
        func_name = "_check_plot_design"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        try:
            raise ValueError(messages[4][0][0])
        except ValueError:
            all_formated_keys = [f"    --->  '{key}'" for key in keys_list]
            msg = [
                f"{messages[5][0][0]} '{len(plot_design_default.keys())}', {messages[5][2][0]} '{len(plot_design.keys())}'.",
                f"{messages[6][0][0]}",
                all_formated_keys
            ]
            msg = general._flatten_list_of_list_string(msg)
            msg = list(msg)
            general._display_n_line_attention(msg)
            raise

    # verificando os values
    # conferindo se todos os values são listas
    for chave, value in plot_design.items():
        func_name = "_check_plot_design"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        if isinstance(value, list) == False:
            try:
                raise ValueError(messages[7][0][0])
            except ValueError:
                general._display_one_line_attention(
                                    f"{messages[8][0][0]} '{chave}' {messages[8][2][0]} '{type(value).__name__}'"
                                    )
                raise
    # verificando o tamanho da lista para cada dict
    for chave, value in plot_design.items():
        if len(plot_design[chave]) != len(plot_design_default[chave]):
            func_name = "_check_plot_design"
            fk_id_function = management._query_func_id(func_name)
            messages = management._get_messages(fk_id_function, language, func_name)
            try:
                raise ValueError(messages[9][0][0])
            except ValueError:
                msg = [
                    f"{messages[10][0][0]} '{chave}' {messages[10][2][0]} {len(plot_design_default[chave])}, {messages[10][4][0]} {len(plot_design[chave])}.",
                    f"{messages[11][0][0]}",
                    f"    --->   {plot_design_example[chave]}"
                    ]
                general._display_n_line_attention(msg)
                raise
    # verificando o tipo de cada elemento dentro das listas
    for (chave, value), (chave_def, value_def) in zip(plot_design.items(), plot_design_default.items()):
        for i in range(len(value)):
            func_name = "_check_plot_design"
            fk_id_function = management._query_func_id(func_name)
            messages = management._get_messages(fk_id_function, language, func_name)
            if type(value[i]) != type(value_def[i]):
                try:
                    raise ValueError(messages[12][0][0])
                except ValueError:
                    msg = f"{messages[13][0][0]} '{i}' {messages[13][2][0]} '{chave}' {messages[13][4][0]} '{type(value_def[i]).__name__}', {messages[13][6][0]} '{type(value[i]).__name__}'"
                    general._display_one_line_attention(
                                        msg
                                        )
                    raise
    return True

# with tests, with text, with database,, with docstring
def _check_which_density_gaussian_kernal_plot(which, language):
    """This function checks if the value passed to the 'which' parameter used to draw the Gaussian density plot is valid.

    Parameters
    ----------
    which : string
        A string containing the keys used to draw the kde graph.
    language : string
        The language code

    Notes
    -----
    The parameter 'language' isn't checked if it is a string.

    Return
    ------
    True if which was considered correct
    Raise ValueError if it was not considered correct

    """
    accepted_keys = [
            "    --->  'mean' adds the mean to the graph",
            "    --->  'median' adds the median to the graph",
            "    --->  'mode' adds the mode to the graph",
            "         or",
            "    --->  'all' adds the mean, median and mode to the graph",
            ]

    # removando espaços em branco
    which = which.replace(" ", "")
    # verificando se tem apenas caracteres aceitos
    list_accepted_letters = ["a", "e", "d", "i", "l", "m", "n", "o", ","]
    list_which = list(which)
    for word in list_which:
        if word not in list_accepted_letters:
            ### quering ###
            func_name = "_check_which_density_gaussian_kernal_plot"
            fk_id_function = management._query_func_id(func_name)
            messages = management._get_messages(fk_id_function, language, func_name)
            try:
                raise ValueError(messages[1][0][0])
            except ValueError:

                msg = [
                        f"{messages[2][0][0]} '{word}'.",
                        f"{messages[3][0][0]}",
                        accepted_keys,
                        f"{messages[4][0][0]}"
                ]
                msg = general._flatten_list_of_list_string(msg)
                msg = list(msg)
                general._display_n_line_attention(msg)
                raise

    which = which.split(",")
    list_accepted_keys = ["mean", "median", "mode", "all"]
    for value in which:
        func_name = "_check_which_density_gaussian_kernal_plot"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        if value not in list_accepted_keys:
            try:
                raise ValueError(messages[5][0][0])
            except ValueError:
                msg = [
                        f"{messages[6][0][0]} '{value}' {messages[6][2][0]}.",
                        f"{messages[7][0][0]}",
                        [f"    --->  {chave}" for chave in list_accepted_keys],
                ]
                msg = general._flatten_list_of_list_string(msg)
                msg = list(msg)
                general._display_n_line_attention(msg)
                raise
    if "all" in which:
        func_name = "_check_which_density_gaussian_kernal_plot"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        if len(which) != 1:
            try:
                raise ValueError(messages[8][0][0])
            except ValueError:
                msg = [
                        f"{messages[9][0][0]}",
                        [f"    --->  {chave}" for chave in which],
                ]
                msg = general._flatten_list_of_list_string(msg)
                msg = list(msg)
                general._display_n_line_attention(msg)
                raise

    return which

# with SOME test, with text, with database
def _export_to_csv(df, language, file_name="my_data", sep=','):
    """Export the data to csv file
    This function is just a wraper around DataFrame.to_csv to export csv files.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame with the data to be exported
    language : string
        The language code
    file_name : string
        The name of the file to be exported, without its extension (default = 'my_data')
    sep : string of length 1
        Field delimiter for the output file (default = ';'). The same parameter of the DataFrame.to_csv pandas method [1]_


    Notes
    -----
    The parameter 'language' isn't checked if it is a string.

    References
    ----------
    .. [1] https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html

    """

    # cheking if the filename is correct
    _check_file_name_is_str(file_name, language)
    # checking if a problematic character is present in the filename
    _check_forbidden_character(file_name, "file_name", language)
    # adding the '.csv' extension
    file = file_name + '.csv'
    # cheking if the sep is valid
    _sep_checker(sep, language)
    # cheking if the df is a DataFrame
    checkers._check_is_data_frame(df, file_name, language)
    # cheking if the file already exists. If it does, ask the user if wants to replace the file
    file_exists = _check_file_exists(file)

    ### querring ###
    func_name = "_export_to_csv"
    fk_id_function = management._query_func_id(func_name)
    messages = management._get_messages(fk_id_function, language, func_name)

    # if the file already exists, create a new name for the file
    if file_exists:
        # warn that the file already exists
        print(f"{messages[1][0][0]} '{file}' {messages[1][2][0]}")
        i = 0
        # try to create a new nine by adding a number to the end of the name.
        while file_exists:
            i += 1
            file = file_name + "_" + str(i) + ".csv"
            file_exists = _check_file_exists(file)
        file_name = file
        # warn the user the name of the file to be exported
        print(f"     ---> {messages[2][0][0]} '{file_name}'")
    else:
        file_name = file_name + '.csv'

    try:
        df.to_csv(file_name, encoding='utf-8-sig', index=False, sep=sep)
        general._display_one_line_attention(
            text = f"{messages[3][0][0]} '{file_name}' {messages[3][2][0]}"
        )
    except PermissionError:
        # logging.error(traceback.format_exc())
        general._display_two_line_attention(
            text1 = f"{messages[4][0][0]} '{file_name}' {messages[4][2][0]}.",
            text2 = f"{messages[5][0][0]} '{file_name}' {messages[5][2][0]}"
            )
        raise
    except FileNotFoundError: # acredito que o problema com subfolder é resolvido com a proibição do /
        # logging.error(traceback.format_exc())
        general._display_two_line_attention(
            text1 = f"{messages[4][0][0]} '{file_name}' {messages[4][2][0]}.",
            text2 = f"{messages[6][0][0]}"
            )
        raise
    return True

# with SOME test, with text, with database, with docstring
def _export_to_xlsx(df_list, language, file_name=None, sheet_names=[None,None]):
    """Export the data to .xlsx file
    This function is just a wraper around DataFrame.to_excel [1]_ to export excel files.

    Parameters
    ----------
    df_list : list with pandas.DataFrame
        A list where each element is a DataFrame that will be inserted in a different sheet. The order of DataFrames in this list must match the list of names passed through the sheet_names parameter.
    language : string
        The language code
    file_name : string
        The name of the file to be exported, without its extension (default = 'my_data')
    sheetet_names : list (default [None, None])
        A list where each element is a string that will be used for each sheet. The order of strings in this list must match the list of DataFrames passed through the df_list parameter.


    Notes
    -----
    The parameter 'language' isn't checked if it is a string.

    Returns
    -------
    True if the file is exported
    ValueError if it was not possible to export the file

    References
    ----------
    .. [1] https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html

    """
    checkers._check_is_list(df_list, "df_list", language)
    for df in df_list:
        checkers._check_is_data_frame(df, "df", language)

    if file_name is None:
        file_name = "sample"
    else:
        checkers._check_is_str(file_name, "file_name", language)
        _check_forbidden_character(file_name, "file_name", language)

    checkers._check_is_list(sheet_names, "sheet_names", language)
    for name in sheet_names:
        checkers._check_is_str(name, "sheet_names", language)

    ### querring ###
    func_name = "_export_to_excel"
    fk_id_function = management._query_func_id(func_name)
    messages = management._get_messages(fk_id_function, language, func_name)

    # combando nome corretamente
    file_name = file_name + ".xlsx"

    # verificando se os dataframes são validos
    for df in df_list:
        checkers._check_is_data_frame(df, "df_list", language)

    ### verificando se o arquivo .xlsx já existe
    if _check_file_exists(file_name):
        ## caso exista, obter uma lista com o nome das abas do arquivo
        # obter os sheet names
        arquivo = pd.ExcelFile(file_name, engine="openpyxl")
        # iterar esta lista comparando se os sheet_names já existem nela
        sheet_alredy_exists = [] # lista vazia para acumular nomes repetidos
        for sheet in arquivo.sheet_names: # olhando nome por nome dentro de sheet_names
            if sheet in sheet_names:
                sheet_alredy_exists.append(sheet) # apendadndo
            else:
                pass
        # caso pelo menos 1 aba já exista, avisar que o nome escolhido será alterado
        if len(sheet_alredy_exists) > 0:
            lista_sheet_names = [f"    --->    '{sheet}'" for sheet in arquivo.sheet_names]
            sheet_alredy_exists = [f"    --->    '{sheet}'" for sheet in sheet_alredy_exists]
            msg = [
                f"{messages[1][0][0]} '{file_name}' {messages[1][2][0]}",
                lista_sheet_names,
                f"{messages[2][0][0]}",
                sheet_alredy_exists,
                "\n",
                f"{messages[3][0][0]}",
                f"{messages[4][0][0]}",
            ]
            msg = general._flatten_list_of_list_string(msg)
            msg = list(msg)
            general._display_n_line_attention(msg)
        else:
            pass # é pass pois caso o sheet name já exista, é apenas para avisar que o nome será alterado. É apenas um aviso
        # caso não tenha nenhum nome conflitante, inserir novas abas no arquivo fornecido
        try:
            with pd.ExcelWriter(file_name, mode="a", if_sheet_exists="new") as writer:
                for i in range(len(df_list)):
                    df_list[i].to_excel(writer, sheet_name=sheet_names[i], index=False, engine="openpyxl")
            general._display_one_line_attention(f"{messages[5][0][0]} '{file_name}'")
        except PermissionError:
            general._display_two_line_attention(
                text1 = f"{messages[6][0][0]} '{file_name}' {messages[6][2][0]}",
                text2 = f"{messages[7][0][0]} '{file_name}' {messages[7][2][0]}"
                )
            raise
        except FileNotFoundError: # acredito que o problema com subfolder é resolvido com a proibição do /
            # logging.error(traceback.format_exc())
            general._display_two_line_attention(
                text1 = f"{messages[6][0][0]} '{file_name}' {messages[6][2][0]}",
                text2 = f"{messages[8][0][0]}"
                        )
            raise
    else:
        ## caso não exista, criar o arquivo e exportar
        try:
            with pd.ExcelWriter(file_name) as writer:
                for i in range(len(df_list)):
                    df_list[i].to_excel(writer, sheet_name=sheet_names[i], index=False, engine="openpyxl")
            general._display_one_line_attention(f"{messages[5][0][0]} {file_name}")
        except PermissionError:
            general._display_two_line_attention(
                text1 = f"{messages[6][0][0]} '{file_name}' {messages[6][2][0]}",
                text2 = f"{messages[7][0][0]} '{file_name}' {messages[7][2][0]}"
                )
            raise
        except FileNotFoundError: # acredito que o problema com subfolder é resolvido com a proibição do /
            # logging.error(traceback.format_exc())
            general._display_two_line_attention(
                text1 = f"{messages[6][0][0]} '{file_name}' {messages[6][2][0]}",
                text2 = f"{messages[8][0][0]}"
                        )
            raise
    return True

# with some test, with text, with database
def _flat_list_of_lists(my_list, param_name, language):
    """This function flats a list of lists

    Parameters
    ----------
    my_list : list of lists
        The list with lists to be flattened. All inner elements must be a list

    param_name : string
        The original name of the parameter passed through the parameter 'my_list'.

    Notes
    -----
    The parameter 'param_name' isn't checked if it is a string.
    The parameter 'my_list' isn't checked if it is a list.

    Returns
    -------
    A flattened list
    ValueError if 'my_list' does not contain lists in all its elements.

    """
    checkers._check_is_list(my_list, param_name, language)
    ### quering ###
    func_name = "_flat_list_of_lists"
    fk_id_function = management._query_func_id(func_name)
    messages = management._get_messages(fk_id_function, language, func_name)
    if all(isinstance(element, list) for element in my_list) == False:
        try:
            raise ValueError(messages[1][0][0])
        except ValueError:
            # "query"
            general._display_one_line_attention(
                                text = f"{messages[2][0][0]} {param_name} {messages[2][2][0]}"
                                )
            raise
    return [item for sublist in my_list for item in sublist]

# with tests, with text, with database, with docstring
def _sep_checker(sep, language):
    """This function checks if a value could be used as 'sep' parameter for pandas to_csv function

    Parameters
    ----------
    sep : string
        The sep value
    language : string
        The language code

    Notes
    -----
    The parameter 'language' isn't checked if it is a string.

    Returns
    -------
    True if sep is valid.
    Raises ValueError is sep is not suitable to be used in pd.to_csv.

    """
    checkers._check_is_str(sep, "sep", language)
    ### quering ###
    func_name = "_sep_checker"
    fk_id_function = management._query_func_id(func_name)
    messages = management._get_messages(fk_id_function, language, func_name)

    if len(sep) != 1:
        try:
            raise ValueError(messages[1][0][0]) #message
        except ValueError:
            general._display_two_line_attention(
                                text1 = f"{messages[2][0][0]} 'sep' {messages[2][2][0]} '{len(sep)}' <--- ({sep})",
                                text2 = f'    {messages[3][0][0]}: ---> ";" '
                                )
            raise
    return True

# with tests, without database, with docstring
def _truncate(value, language, decs=None):
    """This function truncates a 'value' with 'decs' decimal places.

    This function is a wrapper around numpy.trunc() [1]_ adapted with a clever solution for the truncation of decimal places [2]_.

    Parameters
    ----------
    value : int or float
        The value to be truncated
    decs : int or None (default = None)
        The number of decimal places the value should be truncated
    language : string
        The language code

    Notes
    -----
    The parameter 'language' isn't checked if it is a string.

    Returns
    -------
    value
        if value or decs is None, just return the input value
        elif value is integer, just return the input value
        else return the value truncated

    References
    ----------
    .. [1] https://numpy.org/doc/stable/reference/generated/numpy.trunc.html
    .. [2] The inspiration came from: https://stackoverflow.com/a/46020635/17872198

    Examples
    --------

    >>> from easy_stat.utils.helpers import _truncate
    >>> print(_truncate(0.111, 'en', decs=0))
    0.0

    >>> print(_truncate(0.111, 'en', decs=1))
    0.1

    >>> print(_truncate(0.111, 'en', decs=2))
    0.11

    >>> print(_truncate(0.111, 'en', decs=10))
    0.111

    >>> print(_truncate(0.111, 'en', decs=None))
    0.111

    >>> print(_truncate(10, 'en', decs=2))
    10

    >>> print(_truncate(10, 'en', decs=None))
    10

    """
    if decs is None or value is None:
        return value
    else:
        checkers._check_is_integer(decs, "decs", language)
    checkers._check_is_float_or_int(value, "value", language)

    if isinstance(value, (int, np.uint, np.integer)):
        return value
    else:
        return np.trunc(value*10**decs)/(10**decs)



























# Death, death, death, death, death, death, death, death, death, Death, death, death https://youtu.be/jRc9dbgiBPI?t=334
