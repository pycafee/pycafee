"""This module concentrates all the functions that are not in a class
"""

# Function list:
#
#     - multimode(x_exp, language=None)

#########################################
################ Imports ################
#########################################

###### Standard ######
from collections import Counter
from itertools import takewhile
from collections import namedtuple

###### Third part ######
import numpy as np


###### Home made ######
from pycafee.database_management import management
from pycafee.utils import checkers
from pycafee.utils import general



###########################################
################ Functions ################
###########################################


# with tests, with data, with text, with docstring
def interquartile_range(x_exp, method=None, language=None):
    """This function estimates the interquartile range of a data set

    Parameters
    ----------
    x_exp : 1D :doc:`numpy array <numpy:reference/generated/numpy.array>`
        Array with the sample data
    method : ``str``, optional
        The method used to estimate the quartiles.

        * If ``method="tukey"`` (or ``None``), the method proposed by Tukey [1]_ is used

    language : ``str``, optional
        The language code. Default is ``None`` which results in ``en``.

    Returns
    -------
    result : ``tuple`` with:
        interquartile_range : ``float``
            The interquartile range
        q1 : ``float``
            The first quartile, e.g., the median of the lower half
        q3 : ``float``
            The third quartile, e.g., the median of the upper half
    x_low : 1D :doc:`numpy array <numpy:reference/generated/numpy.array>`
        Array with the lower half data
    x_upper : 1D :doc:`numpy array <numpy:reference/generated/numpy.array>`
        Array with the upper half data


    Notes
    -----
    Other methods will be added in the future or the function will be updated to ``np.quantile`` (requires newer numpy version).

    The interquartile distance (:math:`IR`) is calculated using the following equation:

    .. math::

            IR = Q_3 - Q_1


    References
    ----------
    .. [1] TUKEY, J. W. Exploring Data Analysis. 1. ed. Reading: Addison-Wesley Publishing Company. Inc., 1977.


    Examples
    --------

    >>> from pycafee.functions.functions import interquartile_range
    >>> x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4])
    >>> result, x_low, x_upper = interquartile_range(x)
    >>> print(result)
    InterquartileRangeResult(InterquartileRange=0.40000000000000036, FirstQuartil=4.6, ThirdQuartil=5.0)
    >>> print(x_low)
    [4.4 4.6 4.6 4.7 4.9]
    >>> print(x_upper)
    [4.9 5.  5.  5.1 5.4]




    """

    all_languages = management._get_all_available_languages()
    current_default_language = management._get_current_default_language()
    if language is None:
        language = current_default_language
    elif language in all_languages:
        pass
    else:
        try:
            raise ValueError("Error: language not valid")
        except ValueError:
            all_formated_languages = [f"  --->  {lang}" for lang in all_languages]
            fk_id_function = management._query_func_id("LanguageManagment")

            messages = management._get_messages(fk_id_function, current_default_language)
            msg = [
                f"{messages[2][0][0]} '{language}' {messages[2][2][0]}",
                f"{messages[2][3][0]}:",
                all_formated_languages
            ]
            msg = general._flatten_list_of_list_string(msg)
            msg = list(msg)
            general._display_n_line_attention(msg)
            raise


    # cheking if the input is a 1D numpy array
    checkers._check_is_numpy_1_D(x_exp, "x_exp", language)
    # ordenando os dados
    x_exp = np.sort(x_exp, kind='quicksort')

    # cheking the method
    if method is None:
        method = "tukey"
    else:
        checkers._check_is_str(method, "method", language)
        if method not in ["tukey"]:
            fk_id_function = management._query_func_id("generic")
            messages = management._get_messages(fk_id_function, language, "generic")
            try:
                error = messages[3][0][0]
                raise ValueError(error)
            except ValueError:
                msg = [f"{messages[4][0][0]} 'method' {messages[4][2][0]}:"]
                values = ['tukey']
                for item in values:
                    msg.append(f"   --->    '{item}'")
                msg.append(f"{messages[4][4][0]}:")
                msg.append(f"   --->    '{method}'")
                general._display_n_line_attention(msg)
                raise




    # mediana
    median = np.median(x_exp)

    # sample size
    n_rep = x_exp.size

    # if method is Tukey
    if method == "tukey":
        half = int(n_rep/2) # get half size, round to lowest int
        # if size is even
        if n_rep % 2 == 0:
            x_low = x_exp[:half] # get the lower dataset from 0 to half
            x_upper = x_exp[half:] # get the upper dataset, from hatl to -1
            q1 = np.median(x_low) # get the median from lower dataset
            q3 = np.median(x_upper) # get the median from upper dataset
        else: # if size is odd
            x_low = x_exp[:half+1] # get the lower dataset from 0 to half + 1 (to include the median)
            x_upper = x_exp[half:] # get the upper dataset, from hatl to -1
            q1 = np.median(x_low) # get the median from lower dataset
            q3 = np.median(x_upper) # get the median from upper dataset

    # interquartile range
    interquartile_range = q3 - q1
    ### quering
    fk_id_function = management._query_func_id("interquartile_range")
    messages = management._get_messages(fk_id_function, language, "interquartile_range")
    result = namedtuple(messages[1][0][0], (messages[1][1][0], messages[1][2][0], messages[1][3][0]))
    return result(interquartile_range, q1, q3), x_low, x_upper










# with tests, with text, with database, with docstring
def multimode(x_exp, language=None):
    """This function calculates the mode(s) for a numerical sample, returning a dictionary of key-value pairs, where the key is the mode and the value is the count of that mode. If the sample has more than one mode, all modes will be returned.

    Parameters
    ----------
    x_exp : 1D :doc:`numpy array <numpy:reference/generated/numpy.array>`
        Array with the sample data
    language : ``str``, optional
        The language code. Default is ``None`` which results in ``en``.

    Notes
    -----
    The function ``scipy.stats.mode()`` [2]_ was not used due to its limitation of returning only the smallest one, even if the data is multimodal.

    The function ``statistics.multimode()`` [3]_ was not used due to python version (added in python version 3.8). Consider using it in the future.

    Returns
    -------
    multimode : ``dict`` of pairs, where

        * ``keys`` are the modes
        * ``values`` are the respective count

        If the data does not have a mode (all values are unique), the ``key`` is ``None`` and the ``value`` is a message.

    References
    ----------
    .. [1] Inspired by: https://stackoverflow.com/a/9567767/17872198
    .. [2] SciPy mode: https://docs.scipy.org/doc/scipy-1.8.0/html-scipyorg/reference/generated/scipy.stats.mode.html
    .. [3] Python multimode: https://docs.python.org/3/library/statistics.html#statistics.multimode

    Examples
    --------
    >>> from easy_stat.functions.functions import multimode
    >>> import numpy as np
    >>> x = np.array([2, 23, 4, 2, 5])
    >>> result = multimode(x)
    >>> print(result)
    {2: 2}

    >>> from easy_stat.functions.functions import multimode
    >>> import numpy as np
    >>> x = np.array([0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 4])
    >>> result = multimode(x)
    >>> print(result)
    {1: 4, 2: 4}

    >>> from easy_stat.functions.functions import multimode
    >>> import numpy as np
    >>> x = np.array([1.1, 1.1, 2.1, 3.1, 4.1, 5.1])
    >>> result = multimode(x)
    >>> print(result)
    {1.1: 2}

    >>> from easy_stat.functions.functions import multimode
    >>> import numpy as np
    >>> x = np.array([1, 2, 3, 4, 5])
    >>> result = multimode(x)
    >>> print(result)
    {None: 'The data has no mode.'}


    """
    all_languages = management._get_all_available_languages()
    current_default_language = management._get_current_default_language()
    if language is None:
        language = current_default_language
    elif language in all_languages:
        pass
    else:
        try:
            raise ValueError("Error: language not valid")
        except ValueError:
            all_formated_languages = [f"  --->  {lang}" for lang in all_languages]
            fk_id_function = management._query_func_id("LanguageManagment")

            messages = management._get_messages(fk_id_function, current_default_language)
            msg = [
                f"{messages[2][0][0]} '{language}' {messages[2][2][0]}",
                f"{messages[2][3][0]}:",
                all_formated_languages
            ]
            msg = general._flatten_list_of_list_string(msg)
            msg = list(msg)
            general._display_n_line_attention(msg)
            raise
    # cheking if the input is a 1D numpy array
    checkers._check_is_numpy_1_D(x_exp, "x_exp", language)
    # making a counter with the data
    freq = Counter(x_exp)
    # getting the most_common frequency
    mostfreq = freq.most_common()
    # making a list with the most comum with how much counts for each mode
    mode = list(takewhile(lambda x_f: x_f[1] == mostfreq[0][1], mostfreq))
    mode = dict(mode)
    no_mode = all(value == 1 for value in mode.values())
    if no_mode:
        ### querring ###
        func_name = "multimode"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, language, func_name)
        return {None: messages[1][0][0]}
    else:
        return mode




# We live in every moment but this one... Why don't we recognize the faces loving us so https://youtu.be/kAFxLXqP8UM?t=45
