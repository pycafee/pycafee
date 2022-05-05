"""Tests if the display_all_available_languages is working as expected

--------------------------------------------------------------------------------
Description:

---> Class_display_all_available_languages. This tests if the printed output is correct shown. Just work if 'en' and 'pt-br' are default langauges available



--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/database_management/test_management/test_display_all_available_languages.py
    or
    python -m unittest -b tests/database_management/test_management/test_display_all_available_languages.py

--------------------------------------------------------------------------------
"""
import os
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from cup_of_coffee.database_management.management import display_all_available_languages
os.system('cls')

class Testdisplay_all_available_languages(TestCase):

    def test_display_all_available_languages(self):
        display_all_available_languages()
        expected = "   --->    " + "en" + "\n" + "   --->    " + "pt-br" + "\n"

        with patch('sys.stdout', new = StringIO()) as out:
            display_all_available_languages()
            self.assertEqual(out.getvalue(), expected)









if __name__ == "__main__":
    unittest.main()
