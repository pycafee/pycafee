"""Tests if the _check_is_str is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_check_is_str
    # This class tests if the 'value' is an integer number. Several types of integers are tested with the assertTrue statement. Also, the function is tested against strings, tuples, lists, and floats, which should raise a ValueError that is caught with assertRaises.

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/checkers/test__check_is_str.py
    or
    python -m unittest -b tests/utils/checkers/test__check_is_str.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from cup_of_coffee.utils.checkers import _check_is_str
import numpy as np
os.system('cls')

class Test_check_is_str(unittest.TestCase):

    def test_int(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is int"):
            _check_is_str(1, param_name="param", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is int"):
            _check_is_str(np.int32(1), param_name="param", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is int"):
            _check_is_str(np.int64(1), param_name="param", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is int"):
            _check_is_str(np.uint(1), param_name="param", language='en')


    def test_float(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is float"):
            _check_is_str(1.1, param_name="param", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is float"):
            _check_is_str(1.1012, param_name="param", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is float"):
            _check_is_str(1.0, param_name="param", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is float"):
            _check_is_str(np.float32(1), param_name="param", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is float"):
            _check_is_str(np.float64(1), param_name="param", language='en')

    def test_list(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is a list"):
            _check_is_str([1], param_name="param", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is a list"):
            _check_is_str([[1]], param_name="param", language='en')

    def test_tuple(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is a tuple"):
            _check_is_str((1,), param_name="param", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is a tuple"):
            _check_is_str((1,1,1), param_name="param", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is a tuple"):
            _check_is_str((1, (1,), 1), param_name="param", language='en')

    def test_empty(self):
        with self.assertRaises(TypeError, msg="Does not raised error when no value was passed"):
            _check_is_str(param_name="param", language='en')

    def test_empty_string(self):
        with self.assertRaises(ValueError, msg="Does not raised error when an empty string was passed"):
            _check_is_str("", param_name="param", language='en')

    def test_pass(self):
        result = _check_is_str("a", param_name="param", language='en')
        self.assertTrue(result, msg="Does not returned True with a string")

        result = _check_is_str("auisdhsa9d8ysadasd9oasdasdonha nsad\n", param_name="param", language='en')
        self.assertTrue(result, msg="Does not returned True with a string")






if __name__ == "__main__":
    unittest.main()
