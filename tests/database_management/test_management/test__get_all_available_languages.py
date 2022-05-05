"""Tests if the _get_all_available_languages is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test__get_all_available_languages. This function check if the default available languages are 'en' and 'pt-br', with ids of 2 and 3, respectively.



--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/database_management/test_management/test__get_all_available_languages.py
    or
    python -m unittest -b tests/database_management/test_management/test__get_all_available_languages.py

--------------------------------------------------------------------------------
"""
import os
import unittest
import sqlite3
from cup_of_coffee.database_management.management import _get_all_available_languages
os.system('cls')

class TestGetAllAvailableLanguages(unittest.TestCase):

    expected = {'en': 2, 'pt-br': 3}

    def test__get_all_available_languages(self):
        result = _get_all_available_languages()
        self.assertDictEqual(result, self.expected, "There is something wrong with the available languages")



if __name__ == "__main__":
    unittest.main()
