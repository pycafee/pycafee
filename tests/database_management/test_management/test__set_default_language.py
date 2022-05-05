"""Tests if the _set_default_language is working as expected

--------------------------------------------------------------------------------
Description:

---> Class__set_default_language. This checks if the result is int and if a not found function has text



--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/database_management/test_management/test__set_default_language.py
    or
    python -m unittest -b tests/database_management/test_management/test__set_default_language.py

--------------------------------------------------------------------------------
"""
import os
import unittest
from pycafee.database_management.management import set_default_language
os.system('cls')

class Test_set_default_language(unittest.TestCase):


    #####
    # Falta incluir testes sobre a resposta do usuario, e.g, os inputs. Vai precisar usar mock
    ####

    def test__set_default_language_type(self):
        with self.assertRaises(ValueError, msg="The input is not a string"):
            set_default_language(1)

    def test__set_default_language_default(self):
        with self.assertRaises(ValueError, msg="The default language is not 'en'"):
            set_default_language("en")

    def test__set_default_language_exits(self):
        with self.assertRaises(ValueError, msg="For some reason a not implemented language has been accepted"):
            set_default_language("pt-bl")

    # def test__set_default_language_reject(self):
    #     with self.assertRaises(InterruptedError, msg="Ao recusar a mudança, algo de errado esta acontecendo"):
    #         _set_default_language("pt-br")







if __name__ == "__main__":
    unittest.main()
