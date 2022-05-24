"""Tests if the _check_value_is_equal_or_higher_than is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_check_value_is_equal_or_higher_than
    This class tests if the 'value' is higher or equal to minimum. A ValueError should be raised when value is lower. True should be returned if value is higher or equal


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/checkers/test__check_value_is_equal_or_higher_than.py
    or
    python -m unittest -b tests/utils/helpers/test__check_value_is_equal_or_higher_than.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.utils.checkers import _check_value_is_equal_or_higher_than
import numpy as np
os.system('cls')

class Test__check_value_is_equal_or_higher_than(unittest.TestCase):

    def test_fail(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is lower"):
            _check_value_is_equal_or_higher_than(5, "parameter", 10, language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is lower"):
            _check_value_is_equal_or_higher_than(-5, "parameter", -1, language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is lower"):
            _check_value_is_equal_or_higher_than(0.0, "parameter", 1.5, language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is lower"):
            _check_value_is_equal_or_higher_than(3, "parameter", 300, language='en')


    def test_pass(self):
        result = _check_value_is_equal_or_higher_than(3, "parameter", 1, language='en')
        self.assertTrue(result, msg = "Raised error when value higher")

        result = _check_value_is_equal_or_higher_than(-3, "parameter", -5, language='en')
        self.assertTrue(result, msg = "Raised error when value higher")

        result = _check_value_is_equal_or_higher_than(-3.5, "parameter", -5.1, language='en')
        self.assertTrue(result, msg = "Raised error when value higher")

        result = _check_value_is_equal_or_higher_than(5, "parameter", 5, language='en')
        self.assertTrue(result, msg = "Raised error when value is equal")

        result = _check_value_is_equal_or_higher_than(5, "parameter", 5.0, language='en')
        self.assertTrue(result, msg = "Raised error when value is equal")

        result = _check_value_is_equal_or_higher_than(5.0, "parameter", 5.0, language='en')
        self.assertTrue(result, msg = "Raised error when value is equal")

        result = _check_value_is_equal_or_higher_than(5.0, "parameter", 5, language='en')
        self.assertTrue(result, msg = "Raised error when value is equal")

if __name__ == "__main__":
    unittest.main()
