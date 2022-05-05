"""Tests if the _get_current_default_language is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test__get_current_default_language. This checks if the default language is 'en'



--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/database_management/test_management/test__get_current_default_language.py
    or
    python -m unittest -b tests/database_management/test_management/test__get_current_default_language.py

--------------------------------------------------------------------------------
"""
import os
import unittest
import sqlite3
from pycafee.database_management.management import _get_current_default_language
os.system('cls')

class Test_get_current_default_language(unittest.TestCase):

    def test__get_current_default_language(self):
        result = _get_current_default_language()
        self.assertEqual(result, 'en', "The default language is not 'en'")




if __name__ == "__main__":
    unittest.main()
