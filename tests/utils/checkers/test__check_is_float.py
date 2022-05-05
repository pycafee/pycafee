"""Tests if the _check_is_float is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_check_is_float
    This class tests if the 'value' is a float number. Several types of floats are tested with the assertTrue statement. Also, the function is tested against strings, tuples, lists, and integers, which should raise a ValueError that is caught with assertRaises.


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/checkers/test__check_is_float.py
    or
    python -m unittest -b tests/utils/checkers/test__check_is_float.py


--------------------------------------------------------------------------------
"""

import os
import unittest
from cup_of_coffee.utils.checkers import _check_is_float
import numpy as np
os.system('cls')

class Test_check_is_float(unittest.TestCase):

    def test_string(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is a string"):
            _check_is_float("a", param_name="parameter", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is a string"):
            _check_is_float("auisdhsa9d8ysadasd9oasdasdonha nsad\n", param_name="parameter", language='en')

    def test_int(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is int"):
            _check_is_float(1, param_name="parameter", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is int"):
            _check_is_float(np.int32(1), param_name="parameter", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is int"):
            _check_is_float(np.int64(1), param_name="parameter", language='en')

    def test_list(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is a list"):
            _check_is_float([1], param_name="parameter", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is a list"):
            _check_is_float([[1]], param_name="parameter", language='en')

    def test_tuple(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is a tuple"):
            _check_is_float((1,), param_name="parameter", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is a tuple"):
            _check_is_float((1,1,1), param_name="parameter", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is a tuple"):
            _check_is_float((1, (1,), 1), param_name="parameter", language='en')

    def test_empty(self):
        with self.assertRaises(TypeError, msg="Does not raised error when no value was passed"):
            _check_is_float(param_name="parameter", language='en')

    def test_pass(self):
        result = _check_is_float(1.1, param_name="parameter", language='en')
        self.assertTrue(result, msg = "An error was raised when value was 1.1")

        result = _check_is_float(np.float32(1), param_name="parameter", language='en')
        self.assertTrue(result, msg = "An error was raised when value was np.float32(1)")

        result = _check_is_float(np.float64(1), param_name="parameter", language='en')
        self.assertTrue(result, msg = "An error was raised when value was np.float64(1)")


if __name__ == "__main__":
    unittest.main()
