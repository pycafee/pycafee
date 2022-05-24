"""This module concentrates checkers-like functions, which check the type of variable.


"""

# Function list:
#     - _check_data_in_range(value, param_name, min, max, language)
#     - _check_is_bool(value, param_name, language)
#     - _check_is_data_frame(df, param_name, language)
#     - _check_is_dict(value, param_name, language)
#     - _check_is_integer(value, param_name, language)
#     - _check_is_float_or_int(value, param_name, language)
#     - _check_is_float(value, param_name, language)
#     - _check_is_list(value, param_name, language)
#     - _check_is_numpy_1_D(value, param_name, language)
#     - _check_is_positive(value, param_name, language)
#     - _check_is_str(value, param_name, language)
#     - _check_is_subplots(value, param_name, language)
#     - _check_list_length(value, n, param_name, language)
#     - _check_value_is_equal_or_higher_than(value, param_name, minimum, language)

#########################################
################ Imports ################
#########################################

###### Standard ######

###### Third part ######
import numpy as np
import pandas as pd
import matplotlib
###### Home made ######
from pycafee.database_management import management
from pycafee.utils import  general


###########################################
################ Functions ################
###########################################


# with tests, with text, with database
def _check_data_in_range(value, param_name, lower, upper, language):
    """This function checks if a ``value`` is within the range between min and max.

    Parameters
    ----------
    value : ``int`` or ``float``
        The value to be evaluated
    param_name : ``str``
        The original name of the parameter passed through the parameter ``value``.
    lower : ``int`` or ``float``
        The lower bound
    upper : ``int`` or ``float``
        The upper bound
    language : ``str``
        The language code

    Notes
    -----
    The parameter ``param_name`` isn't checked if it is a ``str``.

    The parameter ``language`` isn't checked if it is a ``str``.

    If ``lower`` is higher than ``upper``, the function corrects these values automatically.

    Returns
    -------
    ``True`` if ``value`` is in the range: ``min < value < max``
    ``ValueError`` if ``value`` is not in the range: ``min < value < max``

    """
    _check_is_float_or_int(value, "value", language)
    _check_is_float_or_int(lower, "lower", language)
    _check_is_float_or_int(upper, "upper", language)

    values = [lower, upper]
    lower = min(values)
    upper = max(values)

    if lower < value < upper:
        pass
    else:
        ### quering ###
        func_name = "_check_data_in_range"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        try:
            raise ValueError(messages[1][0][0])
        except ValueError:
            general._display_one_line_attention(
                f"{messages[2][0][0]} '{param_name}' {messages[2][2][0]} '{lower}' {messages[2][4][0]} '{upper}', {messages[2][6][0]} '{value}'",
                                )
            raise
    return True

# with tests, with text, with database
def _check_is_bool(value, param_name, language):
    """This function checks if a ``value`` is a boolean.

    This function verifies if the parameter ``value`` is the type of ``bool`` (``True`` or ``False``). If so, it returns ``True``. If it is not, the function raises a ``ValueError``.

    Parameters
    ----------
    value : any type
        The value to be evaluated.
    param_name : ``str``
        The original name of the parameter passed through the parameter ``value``.
    language : ``str``
        The language code

    Notes
    -----
    The parameter ``param_name`` isn't checked if it is a ``str``.
    The parameter ``language`` isn't checked if it is a ``str``.

    Returns
    -------
    ``True`` if ``value`` is a ``bool``
    ``ValueError`` if ``valuew`` is not a ``bool``


    """
    ### quering ###
    func_name = "_check_is_bool"
    fk_id_function = management._query_func_id(func_name)
    messages = management._get_messages(fk_id_function, language, func_name)

    if isinstance(value, bool) == False:
        try:
            raise ValueError(messages[1][0][0])
        except ValueError:
            general._display_one_line_attention(
                                f"{messages[2][0][0]} '{param_name}'  {messages[2][2][0]} '{type(value).__name__}'",
                                )
            raise

    return True

# with tests, with text, with database
def _check_is_data_frame(df, param_name, language):
    """This function checks if ``df`` is a valid ``DataFrame``, e.g., if it is ``DataFrame`` and if it is not empty.

    Parameters
    ----------
    df : any type
        The value to check if it is a ``DataFrame``.
    param_name : ``str``
        The original name of the parameter passed through the parameter ``df``.
    language : ``str``
        The language code

    Notes
    -----
    The parameter ``param_name`` isn't checked if it is a ``str``.
    The parameter ``language`` isn't checked if it is a ``str``.

    Returns
    -------
    ``True`` if ``df`` is a valid ``DataFrame``.
    Raises ``ValueError`` is ``df`` is not a valid ``DataFrame``.


    """

    if isinstance(df, pd.DataFrame) == False:
        ### quering ###
        func_name = "_check_is_data_frame"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        try:
            raise ValueError(messages[1][0][0]) #message
        except ValueError:
            general._display_one_line_attention(
                                text = f"{messages[2][0][0]} '{param_name}' {messages[2][2][0]} '{type(df).__name__}'"
                                )
            raise
    if df.empty:
        ### quering ###
        func_name = "_check_is_data_frame"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        try:
            raise ValueError(messages[3][0][0]) #message
        except ValueError:
            general._display_one_line_attention(
                                text = f"{messages[4][0][0]} '{param_name}' {messages[4][2][0]}"
                                )
            raise
    return True

# with tests, with text, with database
def _check_is_dict(value, param_name, language):
    """This function checks if a ``value`` is a ``dict``.


    Parameters
    ----------
    value : any type
        The value to check if it is a ``dict``.
    param_name : ``str``
        The original name of the parameter passed through the parameter ``value``.
    language : ``str``
        The language code

    Notes
    -----
    The parameter ``param_name`` isn't checked if it is a ``str``.
    The parameter ``language`` isn't checked if it is a ``str``.

    Returns
    -------
    ``True`` if ``value`` is a ``dict``
    Raises ``ValueError`` if ``value`` is not a ``dict``

    """
    if isinstance(value, dict) == False:
        ### quering ###
        func_name = "_check_is_dict"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        try:
            raise ValueError(messages[1][0][0]) #message
        except ValueError:
            general._display_one_line_attention(
                                f"{messages[2][0][0]} '{param_name}'  {messages[2][2][0]} '{type(value).__name__}'",
                                )
            raise
    return True

# with tests, with text, with database
def _check_is_integer(value, param_name, language):
    """This function checks if a ``value`` is an ``int``

    Parameters
    ----------
    value : any type
        The value to check if it is an ``int``.
    param_name : ``str``
        The original name of the parameter passed through the parameter ``value``.
    language : ``str``
        The language code

    Notes
    -----
    The parameter ``param_name`` isn't checked if it is a ``str``.
    The parameter ``language`` isn't checked if it is a ``str``.

    Returns
    -------
    ``True`` if ``value`` is ``int``
    Raises ``ValueError`` if ``value`` is not an ``int``

    """
    if isinstance(value, (int, np.uint, np.integer)) == False:
        ### quering ###
        func_name = "_check_is_integer"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        try:
            raise ValueError(messages[1][0][0])
        except ValueError:
            general._display_one_line_attention(
                                f"{messages[2][0][0]} '{param_name}'  {messages[2][2][0]} '{type(value).__name__}'",
                                )
            raise
    return True

# with tests, with text, with database
def _check_is_float(value, param_name, language):
    """This function checks if a ``value`` is an ``float``

    Parameters
    ----------
    value : any type
        The value to check if it is a ``float``.
    param_name : ``str``
        The original name of the parameter passed through the parameter ``value``.
    language : ``str``
        The language code

    Notes
    -----
    The parameter ``param_name`` isn't checked if it is a ``str``.
    The parameter ``language`` isn't checked if it is a ``str``.

    Returns
    -------
    ``True`` if ``value`` is ``float``
    Raises ``ValueError`` if ``value`` is not a ``float``


    """

    if isinstance(value, (float, np.floating)) == False:
        ### quering ###
        func_name = "_check_is_float"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        try:
            raise ValueError(messages[1][0][0])
        except ValueError:
            general._display_one_line_attention(
                                f"{messages[2][0][0]} '{param_name}'  {messages[2][2][0]} '{type(value).__name__}'",
                                )
            raise
    else:
        return True

# with tests, with text, with database
def _check_is_float_or_int(value, param_name, language):
    """This function checks if a ``value`` is an ``float`` or ``int``.

    Parameters
    ----------
    value : any type
        The value to check if it is a ``float`` or ``int``.
    param_name : ``str``
        The original name of the parameter passed through the parameter ``value``.
    language : ``str``
        The language code

    Notes
    -----
    The parameter ``param_name`` isn't checked if it is a ``str``.
    The parameter ``language`` isn't checked if it is a ``str``.

    Returns
    -------
    ``True`` if ``value`` is ``float`` or ``int``.
    Raises ``ValueError`` if ``value`` is not a ``float`` or ``int``.

    """

    if isinstance(value, (int, np.uint, np.integer, float, np.floating)) == False:
        ### quering ###
        func_name = "_check_is_float_or_int"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        try:
            raise ValueError(messages[1][0][0])
        except ValueError:

            general._display_one_line_attention(
                                f"{messages[2][0][0]} '{param_name}' {messages[2][2][0]} '{type(value).__name__}'",
                                )
            raise
    else:
        return True

# with tests, with text, with database
def _check_is_list(value, param_name, language):
    """This function checks if a ``value`` is a ``list``.

    Parameters
    ----------
    value : any type
        The value to check if it is a ``list``.
    param_name : ``str``
        The original name of the parameter passed through the parameter ``value``.
    language : ``str``
        The language code

    Notes
    -----
    The parameter ``param_name`` isn't checked if it is a ``str``.
    The parameter ``language`` isn't checked if it is a ``str``.

    Returns
    -------
    ``True`` if ``value`` is a ``list``
    Raises ``ValueError`` if ``value`` is not a ``list``

    """
    if isinstance(value, list) == False:
        ### quering ###
        func_name = "_check_is_list"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        try:
            raise ValueError(messages[1][0][0])
        except ValueError:
            general._display_one_line_attention(
                                f"{messages[2][0][0]} '{param_name}'  {messages[2][2][0]} '{type(value).__name__}'",
                                )
            raise
    return True

# with tests, with text, with database
def _check_is_numpy_1_D(value, param_name, language):
    """This function checks if a ``value`` is an ``numpy array`` of 1 dimension

    Parameters
    ----------
    value : any
        The value to check if it is a non-empty 1-dimensional numpy array.
    param_name : ``str``
        The original name of the parameter passed through the parameter ``value``.
    language : ``str``
        The language code

    Notes
    -----
    The parameter ``param_name`` isn't checked if it is a ``str``.
    The parameter ``language`` isn't checked if it is a ``str``.

    Returns
    -------
    ``True`` if ``value`` is a non-empty ``1-dimensional numpy array``
    Raises ``ValueError`` if ``value`` is not a non-empty ``1-dimensional numpy array``

    """
    ### quering ###
    func_name = "_check_is_numpy_1_D"
    fk_id_function = management._query_func_id(func_name)
    messages = management._get_messages(fk_id_function, language, func_name)

    if isinstance(value, np.ndarray) == False:
        try:
            raise ValueError(messages[1][0][0])
        except ValueError:
            general._display_one_line_attention(
                                f"{messages[2][0][0]} '{param_name}' {messages[2][2][0]} '{type(value).__name__}'",
                                )
            raise
    elif value.ndim != 1:
            try:
                raise ValueError(messages[3][0][0]) #message
            except ValueError:
                general._display_one_line_attention(
                                    f"{messages[4][0][0]} '{param_name}' {messages[4][2][0]} ndim = '{value.ndim}'",
                                    )
                raise
    elif value.size == 0:
            try:
                raise ValueError(messages[5][0][0]) #message
            except ValueError:
                general._display_one_line_attention(
                                    f"{messages[6][0][0]} '{param_name}' {messages[6][2][0]} = '{value.size}'",
                                    )
                raise
    else:
        return True

# with tests, with text, with database
def _check_is_positive(value, param_name, language):
    """This function checks if ``value`` is a positive number.

    Parameters
    ----------
    value : any
        The value to be tesed if it is a positive number
    param_name : ``str``
        The original name of the parameter passed through the parameter ``value``.
    language : ``str``
        The language code

    Notes
    -----
    The parameter ``param_name`` isn't checked if it is a ``str``.
    The parameter ``value`` isn't checked if it is a ``int`` or ``float``.
    The parameter ``language`` isn't checked if it is a ``str``.

    Returns
    -------
    ``True`` if ``value`` is positive
    Raises ``ValueError`` if ``value`` is not positive


    """
    if value <= 0:
        ### quering ###
        func_name = "_chek_is_positive"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        try:
            raise ValueError(messages[1][0][0])
        except ValueError:
            general._display_one_line_attention(
                                f"{messages[2][0][0]} '{param_name}' {messages[2][2][0]} '{value}'",
                                )
            raise
    return True

# with tests, with text, with database
def _check_is_str(value, param_name, language):
    """This function checks if a ``value`` is a ``str``.

    Parameters
    ----------
    value : any type
        The value to check if it is a ``str``.
    param_name : ``str``
        The original name of the parameter passed through the parameter ``value``.
    language : ``str``
        The language code

    Notes
    -----
    The parameter ``param_name`` isn't checked if it is a ``str``.
    The parameter ``language`` isn't checked if it is a ``str``.

    Returns
    -------
    ``True`` if value is a valid ``str``.
    Raises ``ValueError`` is value is not a valid ``str``.

    """
    ### quering ###
    func_name = "_check_is_str"
    fk_id_function = management._query_func_id(func_name)
    messages = management._get_messages(fk_id_function, language, func_name)
    if isinstance(value, str) == False:
        try:
            raise ValueError(messages[1][0][0])
        except ValueError:
            general._display_one_line_attention(
                                    text = f"{messages[2][0][0]} {param_name} {messages[2][2][0]} '{type(value).__name__}'"
                                )
            raise
    elif len(value) == 0:
        try:
            raise ValueError(messages[3][0][0])
        except ValueError:
            general._display_one_line_attention(
                                    text = f"{messages[4][0][0]} {param_name} {messages[4][2][0]}"
                                )
            raise
    else:
        return True

# with tests, with text, with database, with docstring
def _check_is_subplots(value, param_name, language):
    """This function checks if a ``value`` is a ``matplotlib.axes.SubplotBase``.

    This function verifies if the parameter ``value`` is the type of ``matplotlib.axes.SubplotBase`` (``True`` or ``False``). If so, it returns ``True``. If it is not, the function raises a ``ValueError``.

    Parameters
    ----------
    value : any type
        The value to be evaluated.
    param_name : ``str``
        The original name of the parameter passed through the parameter ``value``.
    language : ``str``
        The language code

    Notes
    -----
    The parameter ``param_name`` isn't checked if it is a ``str``.
    The parameter ``language`` isn't checked if it is a ``str``.

    Returns
    -------
    ``True`` if ``value`` is a ``matplotlib.axes.SubplotBase``
    ``ValueError`` if ``valuew`` is not a ``matplotlib.axes.SubplotBase``


    """
    ### quering ###
    func_name = "_check_is_subplots"
    fk_id_function = management._query_func_id(func_name)
    messages = management._get_messages(fk_id_function, language, func_name)

    if isinstance(value, matplotlib.axes.SubplotBase) == False:
        try:
            error = messages[1][0][0]
            raise ValueError(error)
        except ValueError:
            general._display_one_line_attention(
                                f"{messages[2][0][0]} '{param_name}'  {messages[2][2][0]} '{type(value).__name__}'",
                                )
            raise

    return True

# with tests, with text, with database, with docstring
def _check_list_length(value, n, param_name, language):
    """This function checks if a ``list`` (``value``) has len equals to ``n``.

    Parameters
    ----------
    value : ``list``
        The list to check its length
    n : ``int``
        The size that the list should have
    param_name : ``str``
        The original name of the parameter passed through the parameter ``value``.
    language : ``str``
        The language code

    Notes
    -----
    The parameter ``value`` isn't checked if it is a ``list``.
    The parameter ``n`` isn't checked if it is a ``int``.
    The parameter ``param_name`` isn't checked if it is a ``str``.
    The parameter ``language`` isn't checked if it is a ``str``.

    Returns
    -------
    ``True`` if ``len(value) == n``
    Raises ``ValueError`` if ``len(value) != n``

    """

    if len(value) != n:
        ### quering ###
        func_name = "_check_list_length"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        try:
            raise ValueError(messages[1][0][0])
        except ValueError:
            general._display_one_line_attention(
                        f"{messages[2][0][0]} '{param_name}' {messages[2][2][0]} '{n}' {messages[2][4][0]} '{len(value)}'"
                                )
            raise
    return True


# with tests, with text, with database
def _check_value_is_equal_or_higher_than(value, param_name, minimum, language):
    """This function checks if a ``value`` is equal or higher than ``minimum``.

    Parameters
    ----------
    value : ``int`` or ``float``
        The value to be evaluated
    param_name : ``str``
        The original name of the parameter passed through the parameter ``value``.
    minimum : ``int`` or ``float``
        the lower bound (closed)
    language : ``str``
        The language code

    Notes
    -----
    The parameter ``param_name`` isn't checked if it is a ``str``.

    The parameter ``language`` isn't checked if it is a ``str``.

    Returns
    -------
    ``True`` if ``value`` is equal or higher than ``minimum``.
    ``ValueError`` if ``value`` is lower than ``minimum``.

    """
    _check_is_float_or_int(value, "value", language)
    _check_is_float_or_int(minimum, "minimum", language)

    if value >= minimum:
        pass
    else:
        ### quering ###
        func_name = "_check_value_is_equal_or_higher_than"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        try:
            error = messages[1][0][0]
            raise ValueError(error)
        except ValueError:
            general._display_one_line_attention(
                f"{messages[2][0][0]} '{param_name}' {messages[2][2][0]} '{minimum}' {messages[2][4][0]}, '{value}'",
                                )
            raise
    return True


















# Kingslayer, destroying castles in thе sky https://youtu.be/ogtN8odrJTc?t=215
