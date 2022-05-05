"""Tests if the _check_is_dict is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_check_is_dict
    This class tests if the 'value' is a dict. The function is tested against strings, tuples, integers, and floats, which should raise a ValueError that is caught with assertRaises.

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/checkers/test__check_is_dict.py
    or
    python -m unittest -b tests/utils/checkers/test__check_is_dict.py


--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.utils.checkers import _check_is_dict
import numpy as np
os.system('cls')

class Test_check_is_dict(unittest.TestCase):

    def test_string(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is a string"):
            _check_is_dict("a", param_name="param", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is a string"):
            _check_is_dict("auisdhsa9d8ysadasd9oasdasdonha nsad\n", param_name="param", language='en')

    def test_float(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is float"):
            _check_is_dict(1.1, param_name="param", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is float"):
            _check_is_dict(1.1012, param_name="param", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is float"):
            _check_is_dict(1.0, param_name="param", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is float"):
            _check_is_dict(np.float32(1), param_name="param", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is float"):
            _check_is_dict(np.float64(1), param_name="param", language='en')

    def test_int(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is a list"):
            _check_is_dict(1, param_name="param", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is a list"):
            _check_is_dict(np.int64(1), param_name="param", language='en')

    def test_tuple(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is a tuple"):
            _check_is_dict((1,), param_name="param", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is a tuple"):
            _check_is_dict((1,1,1), param_name="param", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is a tuple"):
            _check_is_dict((1, (1,), 1), param_name="param", language='en')

    def test_empty(self):
        with self.assertRaises(TypeError, msg="Does not raised error when no value was passed"):
            _check_is_dict(param_name="param", language='en')

    def test_pass(self):

        result = _check_is_dict({"a": 1}, param_name="param", language='en')
        self.assertTrue(result, msg = "An error was raised when value was {'a': 1}")

        result = _check_is_dict({"a": 1, "b": 2}, param_name="param", language='en')
        self.assertTrue(result, msg = "An error was raised when value was {'a': 1, 'b': 2}")

        result = _check_is_dict({"a": [1]}, param_name="param", language='en')
        self.assertTrue(result, msg = "An error was raised when value was {'a': [1]}")

        result = _check_is_dict({"a": [1,2,3], "b": "2"}, param_name="param", language='en')
        self.assertTrue(result, msg = "An error was raised when value was {'a': [1,2,3], 'b': '2'}")




if __name__ == "__main__":
    unittest.main()
