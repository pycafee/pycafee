"""This module concentrates all generic helper functions, e.g, functions that does not require language management

"""
# Function list:
#     - _display_one_line_success(text)
#     - _display_n_line_warn(flat_list)
#     - _display_one_line_attention(text)
#     - _display_n_line_attention(flat_list)
#     - _display_two_line_attention(text1, text2)
#     - _display_warn(aviso, texto)
#     - _flatten_list_of_list_string(list_of_lists)

#########################################
################ Imports ################
#########################################

###### Standard ######

###### Third part ######
from colorama import Fore, Style, Back, init

###### Home made ######


###########################################
################ Functions ################
###########################################



def _display_one_line_success(text):
    """
    This function prints text to the console in a simple way, but with some editing

    Parameters
    ----------
    text: ``str``
        The text to be printed

    """
    init()
    print(Fore.BLUE, "    " + text)
    print(Style.RESET_ALL)


def _display_n_line_warn(flat_list):
    """This function prints in the console the elements passed as a parameter, the first element being printed in red

    Parameters
    ----------
    flat_list: ``list``
        A flat list with values to be printed.

    """
    init()
    size = len(max(flat_list, key=len))
    print("\n")
    print(Fore.RED, "-"*size)
    i = 0
    for text in flat_list:
        if i == 0:
            print(Fore.RED, text)
        else:
            print(Fore.WHITE, text)
        i += 1
    print(Fore.RED, "-"*size)
    print("\n")
    print(Style.RESET_ALL)

def _display_one_line_attention(text):
    """
    This function prints edited text to the console in a way that catches the user's attention

    Parameters
    ----------
    text: ``str``
        The text to be printed

    """
    print("\n")
    print("^"*len(text))
    print(text)
    print("^"*len(text))
    print("\n")

def _display_n_line_attention(flat_list):
    """This function prints in the console the elements passed as a parameter, in a way that catches the user's attention

    Parameters
    ----------
    flat_list: ``list``
        A flat list with values to be printed.

    """

    size = len(max(flat_list, key=len))
    print("\n")
    print("^"*size)
    for text in flat_list:
        print(text)
    print("^"*size)
    print("\n")

def _display_two_line_attention(text1, text2):
    """
    This function prints edited text to the console in a way that catches the user's attention, where text 1 is printed on the first line, and text2 is printed on the second line.

    Parameters
    ----------
    text1: ``str``
        The text to be printed on the first line
    text2: ``str``
        The text to be printed on the second line

    """
    size = max(len(text1), len(text2))
    print("\n")
    print("^"*size)
    print(text1)
    print(text2)
    print("^"*size)
    print("\n")

def _display_warn(aviso, texto):
    """This function prints in the console the ``aviso`` in red at first line and the texto in white at second line.

    Parameters
    ----------
    aviso: ``str``
        The text to be printed in red
    texto: ``str``
        The text to be printed in white

    """
    init()
    size = max(len(aviso), len(texto))
    # print("\n")
    print(Fore.RED, "-"*size)
    print(Fore.RED, aviso)
    print(Fore.WHITE, texto)
    print(Fore.RED, "-"*size)
    # print("\n")
    print(Style.RESET_ALL)

def _flatten_list_of_list_string(list_of_lists):
    """
    This function flats a nested list with strings in it

    Parameters
    ----------
    list_of_lists: list of lists
        The list to be flattened

    Example
    -------
    a = ['The language enn is not available yet.', 'The languages available are:', ['  --->  en', '  --->  pt-br']]
    flat_list = _flatten_list_of_list_string(a)
    flat_list = list(flat_list)

    Reference
    ---------
    .. [1] https://stackoverflow.com/a/5286571/17872198
    """
    for x in list_of_lists:
        if hasattr(x, '__iter__') and not isinstance(x, str):
            for y in _flatten_list_of_list_string(x):
                yield y
        else:
            yield x











# But I remember... everything   https://youtu.be/76iQNS9VLkc?t=70
