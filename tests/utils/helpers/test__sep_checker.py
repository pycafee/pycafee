"""Tests if the _sep_checker is working as expected

---> Class Test_sep_checker
    This class tests if the input is empty, if the input is not a string and if the length of the string is not equal to 1. It also tries to test if the sep is an one size lenght string, but using a generic try/except.


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/helpers/test__sep_checker.py
    or
    python -m unittest -b tests/utils/helpers/test__sep_checker.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.utils.helpers import _sep_checker
os.system("cls")

class Test_sep_checker(unittest.TestCase):

    def test_empty_string(self):
        with self.assertRaises(ValueError, msg="Does not raised error when len(sep) != 1"):
            _sep_checker("", 'en')
        with self.assertRaises(ValueError, msg="Does not raised error when len(sep) != 1"):
            _sep_checker(".....", 'en')
        with self.assertRaises(ValueError, msg="Does not raised error when len(sep) != 1"):
            _sep_checker(";;", 'en')

    def test_not_string(self):
        with self.assertRaises(ValueError, msg="Does not raised error when type(sep) != str"):
            _sep_checker(1, 'en')
        with self.assertRaises(ValueError, msg="Does not raised error when type(sep) != str"):
            _sep_checker([1], 'en')
        with self.assertRaises(ValueError, msg="Does not raised error when type(sep) != str"):
            _sep_checker([";"], 'en')
        with self.assertRaises(ValueError, msg="Does not raised error when type(sep) != str"):
            _sep_checker((';',), 'en')

    def test_file_name_empty(self):
        with self.assertRaises(TypeError, msg="Does not raised error when sep is empty"):
            _sep_checker()

    def test_pass(self):
        try:
            _sep_checker(";", 'en')
            result = True
        except:
            result = False
        self.assertTrue(result, msg = "Something unexpected happened")




# Say it aint so, I will not go.... Turn the lights off, carry me home https://youtu.be/6ZoyCSffM7I?t=158

if __name__ == "__main__":
    unittest.main()
