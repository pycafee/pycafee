"""Tests if the _check_file_name_is_str is working as expected

---> Class Test_check_file_name_is_str
    This class tests if the input is empty, if the input is a empty string and if the input is not a string. It also tries to test if the file_name is a non-empty string, but using a generic try/except.


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/helpers/test__check_file_name_is_str.py
    or
    python -m unittest -b tests/utils/helpers/test__check_file_name_is_str.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from cup_of_coffee.utils.helpers import _check_file_name_is_str
os.system("cls")

class Test_check_file_name_is_str(unittest.TestCase):

    def test_empty_string(self):
        with self.assertRaises(ValueError, msg="Does not raised error when len(file_name)==0"):
            _check_file_name_is_str("", 'en')

    def test_not_string(self):
        with self.assertRaises(ValueError, msg="Does not raised error when type(file_name) != str"):
            _check_file_name_is_str(1, 'en')

    def test_file_name_empty(self):
        with self.assertRaises(TypeError, msg="Does not raised error when file_name is empty"):
            _check_file_name_is_str()

    def test_pass(self):
        try:
            _check_file_name_is_str("name", 'en')
            result = True
        except:
            result = False
        self.assertTrue(result, msg = "Something unexpected happened")







# weeee arreeeeeeeee https://youtu.be/zTEYUFgLveY?t=476

if __name__ == "__main__":
    unittest.main()
