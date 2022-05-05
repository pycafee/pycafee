"""Tests if the _check_is_float_or_int is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_check_is_float_or_int
    This class tests if the input is a float or an integer with assertTrue. It also tests for other types, like strings, lists, tuples, that should raise ValueError.


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/checkers/test__check_is_float_or_int.py
    or
    python -m unittest -b tests/utils/checkers/test__check_is_float_or_int.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from cup_of_coffee.utils.checkers import _check_is_float_or_int
import numpy as np
os.system('cls')

class Test_check_is_float_or_int(unittest.TestCase):

    def test_string(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is a string"):
            _check_is_float_or_int("a", param_name="parameter", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is a string"):
            _check_is_float_or_int("hausdasuda \n", param_name="parameter", language='en')

    def test_list(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is a list"):
            _check_is_float_or_int([1], param_name="parameter", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is a list of list"):
            _check_is_float_or_int([[1]], param_name="parameter", language='en')

    def test_tuple(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is a tuple"):
            _check_is_float_or_int((1,), param_name="parameter", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is a tuple"):
            _check_is_float_or_int((1,1,1), param_name="parameter", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is a tuple"):
            _check_is_float_or_int((1, (1,), 1), param_name="parameter", language='en')

    def test_empty(self):
        with self.assertRaises(TypeError, msg="Does not raised error when no value was passed"):
            _check_is_float_or_int(param_name="parameter", language='en')

    def test_pass(self):
        result = _check_is_float_or_int(1, param_name="parameter", language='en')
        self.assertTrue(result, msg = "An error was raised when value was 1")

        result = _check_is_float_or_int(np.int32(1), param_name="parameter", language='en')
        self.assertTrue(result, msg = "An error was raised when value was np.int32(1)")

        result = _check_is_float_or_int(np.int64(1), param_name="parameter", language='en')
        self.assertTrue(result, msg = "An error was raised when value was np.int64(1)")

        result = _check_is_float_or_int(np.uint(1), param_name="parameter", language='en')
        self.assertTrue(result, msg = "An error was raised when value was np.uint(1)")

        result = _check_is_float_or_int(1, param_name="parameter", language='en')
        self.assertTrue(result, msg = "An error was raised when value was 1")

        result = _check_is_float_or_int(np.int32(1), param_name="parameter", language='en')
        self.assertTrue(result, msg = "An error was raised when value was np.int32(1)")

        result = _check_is_float_or_int(np.int64(1), param_name="parameter", language='en')
        self.assertTrue(result, msg = "An error was raised when value was np.int64(1)")

        result = _check_is_float_or_int(np.uint(1), param_name="parameter", language='en')
        self.assertTrue(result, msg = "An error was raised when value was np.uint(1)")


if __name__ == "__main__":
    unittest.main()
