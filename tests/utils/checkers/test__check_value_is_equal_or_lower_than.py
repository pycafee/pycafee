"""Tests if the _check_value_is_equal_or_lower_than is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_check_value_is_equal_or_lower_than
    This class tests if the 'value' is lower or equal to maximum. A ValueError should be raised when value is higher. True should be returned if value is lower or equal


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/checkers/test__check_value_is_equal_or_lower_than.py
    or
    python -m unittest -b tests/utils/checkers/test__check_value_is_equal_or_lower_than.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.utils.checkers import _check_value_is_equal_or_lower_than
import numpy as np
os.system('cls')

class Test__check_value_is_equal_or_higher_than(unittest.TestCase):

    def test_fail(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is higher"):
            _check_value_is_equal_or_lower_than(10, "parameter", 5, language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is higher"):
            _check_value_is_equal_or_lower_than(-1, "parameter", -5, language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is higher"):
            _check_value_is_equal_or_lower_than(1.5, "parameter", 0.0, language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is higher"):
            _check_value_is_equal_or_lower_than(300, "parameter", 3, language='en')


    def test_pass(self):
        result = _check_value_is_equal_or_lower_than(1, "parameter", 3, language='en')
        self.assertTrue(result, msg = "Raised error when value lower")

        result = _check_value_is_equal_or_lower_than(-5, "parameter", -3, language='en')
        self.assertTrue(result, msg = "Raised error when value lower")

        result = _check_value_is_equal_or_lower_than(-5.1, "parameter", -3.5, language='en')
        self.assertTrue(result, msg = "Raised error when value lower")

        result = _check_value_is_equal_or_lower_than(5, "parameter", 5, language='en')
        self.assertTrue(result, msg = "Raised error when value is lower")

        result = _check_value_is_equal_or_lower_than(5, "parameter", 5.0, language='en')
        self.assertTrue(result, msg = "Raised error when value is lower")

        result = _check_value_is_equal_or_lower_than(5.0, "parameter", 5.0, language='en')
        self.assertTrue(result, msg = "Raised error when value is lower")

        result = _check_value_is_equal_or_lower_than(5.0, "parameter", 5, language='en')
        self.assertTrue(result, msg = "Raised error when value is lower")

if __name__ == "__main__":
    unittest.main()
