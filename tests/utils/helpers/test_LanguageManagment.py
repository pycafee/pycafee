"""Tests if the LanguageManagment is working as expected

---> Class Test_get_language
    This class tests if the method get_language is working as expected, testing the default value ('en') and when the language is changed to 'pt-br'

---> Class Test_set_language
    This class tests if the method set_language is working as expected, testing if it raise ValueError when a not valid language is passed, and if it changes the values whan pt-br is passed.
---> Class Test_init
    This class tests if the method init is working as expected, testing if it raise ValueError when a not valid language is passed, if it changes the values whan pt-br is passed and if the defaul value is en.

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/helpers/test_LanguageManagment.py
    or
    python -m unittest -b tests/utils/helpers/test_LanguageManagment.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.utils.helpers import LanguageManagement
os.system("cls")


class Test_init(unittest.TestCase):

    def test_set_to_pb_bl(self):
        with self.assertRaises(ValueError, msg="Does not raised error when a invalid language is passed"):
            teste = LanguageManagement("pb-bl")

    def test_set_to_pt_br(self):
        teste = LanguageManagement("pt-br")
        self.assertEqual(teste.language, "pt-br", msg="The language is not pt-br")

    def test_default(self):
        teste = LanguageManagement()
        self.assertEqual(teste.language, "en", msg="The language is not en")

class Test_set_language(unittest.TestCase):

    def test_set_to_pb_bl(self):
        with self.assertRaises(ValueError, msg="Does not raised error when a invalid language is passed"):
            teste = LanguageManagement()
            result = teste.set_language("pb-bl")

    def test_set_to_pt_br(self):
        teste = LanguageManagement()
        teste.set_language("pt-br")
        self.assertEqual(teste.language, "pt-br", msg="The language is not pt-br")



class Test_get_language(unittest.TestCase):

    def test_default(self):
        teste = LanguageManagement()
        result = teste.get_language()
        self.assertEqual(result, "en", msg="The default language is not en")

    def test_pt_br(self):
        teste = LanguageManagement()
        teste.set_language('pt-br')
        result = teste.get_language()
        self.assertEqual(result, "pt-br", msg="The language is not pt-br")






# hirari chuu ni mauuuuuuuuuuuuuuuuu https://youtu.be/E8pcFhPZQYg?t=278

if __name__ == "__main__":
    unittest.main()
