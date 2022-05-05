"""This module concentrates all the functions to perform queries in the database

"""

# Function list:
#     - _connecting_to_database(database_name="main_database.db")
#     - _get_all_available_languages()
#     - _get_all_languages_for_func(func_name)
#     - _get_current_default_language()
#     - _get_messages(fk_id_function, language, func_name=None)
#     - _query_func_id(func_name)
#     - set_default_language(new_language)
#     - display_all_available_languages()
#     - display_current_default_language()


#########################################
################ Imports ################
#########################################

###### Standard ######
from collections import defaultdict
import logging
from pathlib import Path
import sqlite3
import traceback

###### Third part ######


###### Home made ######
from cup_of_coffee.utils import general


###########################################
################ Functions ################
###########################################


# with tests (OK)
def _connecting_to_database(database_name="main_database.db"):
    """Connects to a database stored on the '../data/' folder

    Parameters
    ----------

    database_name : string
        The name of the database (default = "main_database.db")

    Returns
    -------
    _cursor : <class 'sqlite3.Cursor'>

    _connection : <class 'sqlite3.Connection'>

    """

    # cheking if the input is a valid database name
    if isinstance(database_name, str) == False:
        try:
            raise ValueError("NotStringError")
        except ValueError:
            general._display_two_line_attention(
                text1 = "NotStringError",
                text2 = f"    The file name must be a string, but we got '{type(database_name).__name__}'"
            )
            raise
    if len(database_name) < 4:
        try:
            raise ValueError("VerySmallStringError")
        except ValueError:
            general._display_two_line_attention(
                text1 = "VerySmallStringError",
                text2 = f"The filename size is too small! It must contain at least 4 valid characters, but we got '{len(database_name)}'."
            )
            raise


    db = Path(__file__).parent / "../data/" / database_name  # path to the dtabse which contains all databse
    database = Path(db)
    # checking if the database file exists, and if so, create the connection and the _cursor
    if database.exists():
        # connection to the database
        _connection = sqlite3.connect(db)
        # creating the _cursor
        _cursor = _connection.cursor()
    else:
        # if not, raise an error and exit
        try:
            raise FileNotFoundError("FileNotFoundError")
        except FileNotFoundError:
            general._display_two_line_attention(
                text1 = f"The '{database_name}' does not exist. Please, check the instalation files.",
                text2 =  "Most likely it will be necessary to reinstall the library or recreate the database!"
                )
            raise

    return _cursor, _connection

# with tests (OK)
def _get_all_available_languages():
    """Return all the languages available
    """
    _cursor, _connection = _connecting_to_database()
    ## quering
    # getting all the available languages
    _cursor.execute("SELECT language, id_language FROM Language")
    all_languages = dict(_cursor.fetchall())
    # removindo the 'universal' language to avoid problems
    all_languages.pop('univ', None)
    # closing the _cursor/_connection
    _cursor.close()
    _connection.close()
    return all_languages

# with tests (OK)
def _get_all_languages_for_func(func_name):
    """
    Retorna todos os idiomas disponíveis para a func_name
    func_name deve ser uma string com o nome de uma função válida dentro da database
    """
    if isinstance(func_name, str) == False:
        try:
            raise ValueError("NotStringError")
        except ValueError:
            general._display_one_line_attention(
                text = f"The func_name parameter must be of type string, but we got: {type(func_name).__name__}."
            )
            raise
    # obtendo o id da função
    func_id = _query_func_id(func_name)
    # conectando com a database
    _cursor, _connection = _connecting_to_database()
    # fazendo a query
    _cursor.execute("""
        SELECT DISTINCT
            Language.language,
            Message.fk_id_language
        FROM
            (Message_Slices
        LEFT JOIN
            Message
        ON
            Message.id_message = Message_Slices.fk_id_message)
        LEFT JOIN
            Language
        ON
            Language.id_language = Message.fk_id_language
        WHERE
            Message.fk_id_function = ?
        ;
    """, (func_id,))

    all_languages_for_func = _cursor.fetchall()

    # verificando se a quary retornou algo diferente de None, o que não deve acontecer
    if all_languages_for_func is None:
        try:
            raise ValueError("FunctionNotFound")
        except ValueError:
            general._display_one_line_attention(
                text = f"No language found for {func_name}."
            )
            raise

    # transformando em um dicionário
    all_languages_for_func = dict(all_languages_for_func)

    # verificando se a transformação em dict foi ok
    if isinstance(all_languages_for_func, dict) == False:
        try:
            raise ValueError("NotDictError")
        except ValueError:
            general._display_two_line_attention(
                text1 = f"The 'all_languages_for_func' should be a dict, but is: {type(all_languages_for_func).__name__}",
                text2 = f"This is a very unexpected error. Please, send details to andersonmdcanteli@gmail.com."
            )
            raise

    # removindo the 'universal' language to avoid problems
    all_languages_for_func.pop('univ', None)


    if len(all_languages_for_func) == 0:
        try:
            raise ValueError("EmptyDictError")
        except ValueError:
            general._display_two_line_attention(
                text1 = f"The 'all_languages_for_func' is empty after pop. This means that only 'univ' language is available.",
                text2 = f"This is a very unexpected error. Please, send details to andersonmdcanteli@gmail.com."
            )
            raise
    # closing the _cursor/_connection
    _cursor.close()
    _connection.close()
    # retornando todos os idiomas disponíveis
    return all_languages_for_func

# with tests (OK)
def _get_current_default_language():
    """Gets the current default language
    """
    _cursor, _connection = _connecting_to_database()
    _cursor.execute("SELECT default_input FROM Default_Values WHERE default_parameter = 'language'")
    default_language = _cursor.fetchone()
    # closing the _cursor/_connection
    _cursor.close()
    _connection.close()

    return default_language[0]

# with A test (OK)
# maybe, add a detault text just for testing on the database
def _get_messages(fk_id_function, language, func_name=None):
    """
    Function to get the messages for each function on the database
    """
    _cursor, _connection = _connecting_to_database()

    # obtendo a id_language
    _cursor.execute("""
        SELECT id_language FROM Language WHERE language = ?;
    """, (language,))

    result = _cursor.fetchone()
    if result is None:
        # aqui a ideia é aoi inves de retornar para o ingles, que retorne para o padrão. Mas por enquanto, fica assim mesmo.
        # current_default_language = _get_current_default_language()
        # print(current_default_language)
        general._display_two_line_attention(
            text1 = f"The {func_name} function has not been translated into the '{language}' language yet.",
            text2 = "The English language will be used."
        )
        fk_id_language = 2 # en
    else:
        fk_id_language = result[0]


    # fazendo a query
    _cursor.execute("""
    SELECT
        Message.position,
        Message_slices.message
    FROM
        Message_slices
    LEFT JOIN
        Message
    ON
        Message.id_message = Message_Slices.fk_id_message
    WHERE
        Message.fk_id_function = ? AND Message.fk_id_language = ?
    ;
    """, (fk_id_function, fk_id_language))

    query = _cursor.fetchall()
    messages = defaultdict(list)
    for x, y in query:
        messages[x].append([y])
    # print(query)
    # fechando o cursor/connection
    _cursor.close()
    _connection.close()
    return messages

# with tests (OK)
def _query_func_id(func_name):
    """
    Retorna o id_funcao de uma função.
    func_name é uma string com o nome da função desejada
    """
    # conectando na database raiz
    _cursor, _connection = _connecting_to_database()
    # fazendo a query
    _cursor.execute("""
        SELECT
            id_funcao
        FROM
            Funcao
        WHERE
            nome = ?
    ;
    """, (func_name,) )
    func_id = _cursor.fetchone()
    # verificando se a query foi sucesso. Se não, levantar ValueError
    if func_id is None:
        try:
            raise ValueError("FunctionNotFound")
        except ValueError:
            general._display_one_line_attention(
                text = f"The function '{func_name}' was not found in the database"
            )
            raise

    # Verificando se o resultado é do tipo inteiro. Se não, levantar ValueError
    if isinstance(func_id[0], int) == False:
        try:
            raise ValueError("IdNotInteger")
        except ValueError:
            general._display_two_line_attention(
                text1 = f"The id of the '{func_name}' was not an integer, but {type(func_id).__name__}.",
                text2 = f"This is a very unspected error. Please, send details to andersonmdcanteli@gmail.com."
            )
            raise
    # fechando cursor e connection
    _cursor.close()
    _connection.close()
    # retornando apenas o id (como um int)
    return func_id[0]

# with just some tests (needs improvement)
def set_default_language(new_language):
    """Sets the language for the whole library

    Parameters
    ----------
    new_language : ``str``
        The desired language code


    Notes
    -----
    To get all available languages, use the :func:`easy_stat.database_management.management.display_all_available_languages()` function.

    """
    # getting the default language
    default_language = _get_current_default_language()

    # getting all the available languages
    all_languages = _get_all_available_languages()

    ## quering
    _cursor, _connection = _connecting_to_database()
    # quering to get all messages for the default language
    _cursor.execute("""
        SELECT
            Default_Messages.position,
            Default_Messages_slices.message_slice
        FROM
            Default_Messages_slices
        LEFT JOIN Default_Messages ON Default_Messages.id_default_message = Default_Messages_Slices.fk_id_default_messages
        WHERE Default_Messages.fk_id_default_values = 1 AND Default_Messages.fk_id_language = ?;
    """, (all_languages[default_language],))
    # fetching the data
    data = _cursor.fetchall()

    # turning the result into a list dictionary
    messages = defaultdict(list)
    for x, y in data:
        messages[x].append([y])


    ########################################
    ### Making checks of the option made ###
    ########################################

    # cheking if the input is a string
    if isinstance(new_language, str) == False:
        try:
            raise ValueError("InvalidInputError")
        except ValueError:
            general._display_one_line_attention(
                messages[1][0][0] + "new_language" + messages[1][2][0] + str(type(new_language).__name__) + messages[1][4][0]
            )
            raise

    # checking if the passed value is equal to the default value
    if new_language == default_language:
        # if so, raise an error
        try:
            raise ValueError("SameLanguageError")
        except ValueError:
            general._display_one_line_attention(messages[2][0][0] + new_language + messages[2][2][0])
            raise

    # checking if the chosen language is one of the available ones
    if new_language not in all_languages.keys():
        # if not, raise an error
        try:
            raise ValueError("LanguageMatchError")
        except ValueError:
            general._display_one_line_attention(messages[3][0][0] + new_language + messages[3][2][0])
            # apresentar todas as linguas disponiveis
            print(messages[4][0][0])
            for language in all_languages.keys():
                print("   -> ", language)
            print("\n")
            raise

    ## Changing the default value
    # sending some info
    print(messages[5][0][0])
    input(messages[6][0][0] + '\n')
    print(messages[7][0][0])
    input(messages[6][0][0] + '\n')

    # Asking if wants to change
    answer = input(messages[8][0][0] + default_language + messages[8][2][0] + new_language + messages[8][4][0])
    print(messages[9][0][0] + str(answer) + '\n')

    # If so, make the change
    if answer == "Y":
        try:
            # queryng
            _cursor.execute("UPDATE Default_Values SET default_input = ? WHERE default_parameter = 'language'", (new_language,))
            # commiting
            _connection.commit()
            # closing the _cursor
            _cursor.close()
            # closing the connection
            _connection.close()
            # old language
            old_language = default_language

            # connection to the database
            _cursor, _connection = _connecting_to_database()

            # making a query to get all the messages of the default language
            default_language = _get_current_default_language()
            # making a query to update the messages
            _cursor.execute("""
                SELECT
                    Default_Messages.position,
                    Default_Messages_slices.message_slice
                FROM
                    Default_Messages_slices
                LEFT JOIN Default_Messages ON Default_Messages.id_default_message = Default_Messages_Slices.fk_id_default_messages
                WHERE Default_Messages.fk_id_default_values = 1 AND Default_Messages.fk_id_language = ?;
            """, (all_languages[default_language],))
            data = _cursor.fetchall()
            # closing the _cursor
            _cursor.close()
            # closing the connection
            _connection.close()

            # turning the result into a list dictionary
            messages = defaultdict(list)
            for x, y in data:
                messages[x].append([y])

            # reporting what was done
            general._display_one_line_attention(messages[10][0][0] + old_language + messages[10][2][0] +  default_language + messages[10][4][0])

            # return True

        except Exception as e:
            logging.error(traceback.format_exc())
    else:
        input(messages[6][0][0] + '\n')
        # closing the _cursor
        _cursor.close()
        # closing the connection
        _connection.close()
        try:
            raise InterruptedError("UserAbortError")
        except InterruptedError:
            general._display_two_line_attention(
                text1 = messages[11][0][0],
                text2 = messages[12][0][0] + default_language[0] + messages[12][2][0]
                )

            raise

# with tests (OK)
def display_all_available_languages():
    """Prints all the languages available
    """
    _cursor, _connection = _connecting_to_database()
    ## quering
    # getting all the available languages
    _cursor.execute("SELECT language, id_language FROM Language")
    all_languages = dict(_cursor.fetchall())
    # removindo the 'universal' language to avoid problems
    all_languages.pop('univ', None)
    # closing the _cursor/_connection
    _cursor.close()
    _connection.close()
    for language in all_languages.keys():
        print("   --->   ", language)

# with tests
def display_current_default_language():
    """Prints the current default language
    """
    _cursor, _connection = _connecting_to_database()
    _cursor.execute("SELECT default_input FROM Default_Values WHERE default_parameter = 'language'")
    default_language = _cursor.fetchone()
    # closing the _cursor/_connection
    _cursor.close()
    _connection.close()

    print("   --->   " + default_language[0])



### weee aaarrreeeeeeee, Babyyyymeeeetaaaaaaaaaaallllllllllllllllllll!  https://youtu.be/M6bC3Zxv9Os?t=1385
