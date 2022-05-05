"""Tests if the _check_is_integer is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_check_is_integer
    This class tests if the 'value' is an integer number. Several types of integers are tested with the assertTrue statement. Also, the function is tested against strings, tuples, lists, and floats, which should raise a ValueError that is caught with assertRaises.

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/checkers/test__check_is_integer.py
    or
    python -m unittest -b tests/utils/checkers/test__check_is_integer.py


--------------------------------------------------------------------------------
"""

import os
import unittest
from cup_of_coffee.utils.checkers import _check_is_integer
import numpy as np
os.system('cls')

class Test_check_is_integer(unittest.TestCase):

    def test_string(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is a string"):
            _check_is_integer("a", param_name="param", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is a string"):
            _check_is_integer("auisdhsa9d8ysadasd9oasdasdonha nsad\n", param_name="param", language='en')

    def test_float(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is float"):
            _check_is_integer(1.1, param_name="param", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is float"):
            _check_is_integer(1.1012, param_name="param", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is float"):
            _check_is_integer(1.0, param_name="param", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is float"):
            _check_is_integer(np.float32(1), param_name="param", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is float"):
            _check_is_integer(np.float64(1), param_name="param", language='en')

    def test_list(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is a list"):
            _check_is_integer([1], param_name="param", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is a list"):
            _check_is_integer([[1]], param_name="param", language='en')

    def test_tuple(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is a tuple"):
            _check_is_integer((1,), param_name="param", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is a tuple"):
            _check_is_integer((1,1,1), param_name="param", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is a tuple"):
            _check_is_integer((1, (1,), 1), param_name="param", language='en')

    def test_empty(self):
        with self.assertRaises(TypeError, msg="Does not raised error when no value was passed"):
            _check_is_integer(param_name="param", language='en')

    def test_pass(self):
        result = _check_is_integer(1, param_name="param", language='en')
        self.assertTrue(result, msg = "An error was raised when value was 1")

        result = _check_is_integer(np.int32(1), param_name="param", language='en')
        self.assertTrue(result, msg = "An error was raised when value was np.int32(1)")

        result = _check_is_integer(np.int64(1), param_name="param", language='en')
        self.assertTrue(result, msg = "An error was raised when value was np.int64(1)")

        result = _check_is_integer(np.uint(1), param_name="param", language='en')
        self.assertTrue(result, msg = "An error was raised when value was np.uint(1)")



if __name__ == "__main__":
    unittest.main()
