"""Tests if the _check_is_bool is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_check_is_bool
    # This class tests if the 'value' is a float number. Several types of floats are tested with the assertTrue statement. Also, the function is tested against strings, tuples, lists, and integers, which should raise a ValueError that is caught with assertRaises.


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/checkers/test__check_is_bool.py
    or
    python -m unittest -b tests/utils/helpers/test__check_is_bool.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from cup_of_coffee.utils.checkers import _check_is_bool
import numpy as np
os.system('cls')

class Test_check_is_bool(unittest.TestCase):

    def test_string(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is a string"):
            _check_is_bool("a", param_name="parameter", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is a string"):
            _check_is_bool("auisdhsa9d8ysadasd9oasdasdonha nsad\n", param_name="parameter", language='en')

    def test_int(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is int"):
            _check_is_bool(1, param_name="parameter", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is int"):
            _check_is_bool(np.int(1), param_name="parameter", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is int"):
            _check_is_bool(np.int32(1), param_name="parameter", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is int"):
            _check_is_bool(np.int64(1), param_name="parameter", language='en')

    def test_list(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is a list"):
            _check_is_bool([1], param_name="parameter", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is a list"):
            _check_is_bool([[1]], param_name="parameter", language='en')

    def test_tuple(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is a tuple"):
            _check_is_bool((1,), param_name="parameter", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is a tuple"):
            _check_is_bool((1,1,1), param_name="parameter", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is a tuple"):
            _check_is_bool((1, (1,), 1), param_name="parameter", language='en')

    def test_empty(self):
        with self.assertRaises(TypeError, msg="Does not raised error when no value was passed"):
            _check_is_bool(param_name="parameter", language='en')

    def test_None(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is None"):
            _check_is_bool(None, param_name="parameter", language='en')

    def test_pass(self):
        result = _check_is_bool(True, param_name="parameter", language='en')
        self.assertTrue(result, msg = "An error was raised when value was True")

        result = _check_is_bool(False, param_name="parameter", language='en')
        self.assertTrue(result, msg = "An error was raised when value was False")



if __name__ == "__main__":
    unittest.main()
