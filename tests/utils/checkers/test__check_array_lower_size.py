"""Tests if the _check_array_lower_size is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_check_array_lower_size
    # This class tests if the 'value' is a float number. Several types of floats are tested with the assertTrue statement. Also, the function is tested against strings, tuples, lists, and integers, which should raise a ValueError that is caught with assertRaises.


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/checkers/test__check_array_lower_size.py
    or
    python -m unittest -b tests/utils/helpers/test__check_array_lower_size.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.utils.checkers import _check_array_lower_size
import numpy as np
os.system('cls')

class Test_check_is_bool(unittest.TestCase):

    def test_wrong_size(self):
        x = np.array([1,1,1,1])
        with self.assertRaises(ValueError, msg="Does not raised error when the size is lower than value"):
            _check_array_lower_size(x, 5, param_name="parameter", language='en')

        with self.assertRaises(ValueError, msg="Does not raised error when the size is lower than value"):
            _check_array_lower_size(x, 6, param_name="parameter", language='en')

        with self.assertRaises(ValueError, msg="Does not raised error when the size is lower than value"):
            _check_array_lower_size(x, 7, param_name="parameter", language='pt-br')


    def test_pass(self):
        x = np.array([1,1,1,1])
        result = _check_array_lower_size(x, 1, param_name="parameter", language='pt-br')
        self.assertTrue(result, msg = "An error was raised when size is equal to the array size")

        result = _check_array_lower_size(x, 2, param_name="parameter", language='en')
        self.assertTrue(result, msg = "An error was raised when size is higher to the array size")

        result = _check_array_lower_size(x, 3, param_name="parameter", language='en')
        self.assertTrue(result, msg = "An error was raised when size is higher to the array size")

        result = _check_array_lower_size(x, 4, param_name="parameter", language='en')
        self.assertTrue(result, msg = "An error was raised when size is higher to the array size")



if __name__ == "__main__":
    unittest.main()
