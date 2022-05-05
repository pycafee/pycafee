"""Tests if the display_current_default_language is working as expected

--------------------------------------------------------------------------------
Description:

---> Class_display_current_default_language. This tests if the printed output is correct shown. Just work if 'en' is THE default


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/database_management/test_management/test_display_current_default_language.py
    or
    python -m unittest -b tests/database_management/test_management/test_display_current_default_language.py

--------------------------------------------------------------------------------
"""
import os
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from pycafee.database_management.management import display_current_default_language
os.system('cls')

class TestDisplayDefaultLanguage(TestCase):

    def test_display_current_default_language(self):
        expected = "   --->   " + "en\n"
        with patch('sys.stdout', new = StringIO()) as out:
            display_current_default_language()
            self.assertEqual(out.getvalue(), expected)













if __name__ == "__main__":
    unittest.main()
