"""Tests if the _check_list_length is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_check_list_length
    This class tests if the 'value' has length equal to 'n'. The function is tested against lower or higher n (with assertRaises). Also, it tests for correct lengths.

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/checkers/test__check_list_length.py
    or
    python -m unittest -b tests/utils/checkers/test__check_list_length.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.utils.checkers import _check_list_length
import numpy as np
os.system('cls')

class Test_check_is_list(unittest.TestCase):

    def test_n_lower(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value length is lower than n"):
            _check_list_length(["a", 1], 1, param_name="param", language='en')

        with self.assertRaises(ValueError, msg="Does not raised error when value length is lower than n"):
            _check_list_length(["a", 1], 1, param_name="param", language='pt-br')

        with self.assertRaises(ValueError, msg="Does not raised error when value length is lower than n"):
            _check_list_length(["a", 1, 5, 3], 2, param_name="param", language='en')

        with self.assertRaises(ValueError, msg="Does not raised error when value length is lower than n"):
            _check_list_length(["a", 1, 5, 3], 1, param_name="param", language='en')

    def test_n_higher(self):

        with self.assertRaises(ValueError, msg="Does not raised error when value length is higher than n"):
            _check_list_length(["a", 1], 3, param_name="param", language='en')

        with self.assertRaises(ValueError, msg="Does not raised error when value length is higher than n"):
            _check_list_length(["a", 1], 13, param_name="param", language='pt-br')

        with self.assertRaises(ValueError, msg="Does not raised error when value length is higher than n"):
            _check_list_length(["a", 1, 5, 3], 10, param_name="param", language='en')

        with self.assertRaises(ValueError, msg="Does not raised error when value length is higher than n"):
            _check_list_length(["a", 1, 5, 3], 5, param_name="param", language='en')


    def test_pass(self):
        result = _check_list_length(["a", 1, 5, 3], 4, param_name="param", language='en')
        self.assertTrue(result, msg = "An error was len is equal to n")

        result = _check_list_length(["a", 1, 5, 3, "5", 0.1, 0, 0, 0, 1], 10, param_name="param", language='en')
        self.assertTrue(result, msg = "An error was len is equal to n")

        result = _check_list_length(["a", 1, 5], 3, param_name="param", language='pt-br')
        self.assertTrue(result, msg = "An error was len is equal to n")




if __name__ == "__main__":
    unittest.main()
