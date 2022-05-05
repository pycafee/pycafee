"""Tests if the _check_is_numpy_1_D is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_check_is_numpy_1_D
    This class tests if the value is a one dimension not empty numpy array. It searches for ValueError when type is not array and when it is empty. It also checks if True is returned when value is 1D numpy array.


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/checkers/test__check_is_numpy_1_D.py
    or
    python -m unittest -b tests/utils/checkers/test__check_is_numpy_1_D.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.utils.checkers import _check_is_numpy_1_D
import numpy as np
os.system('cls')

class Test_check_is_numpy_1_D(unittest.TestCase):

    def test_empty_array(self):
        with self.assertRaises(ValueError, msg="Does not raised error when the numpy array is empty"):
            x = np.array([])
            _check_is_numpy_1_D(x, param_name="param", language='en')

    def test_is_list(self):
        with self.assertRaises(ValueError, msg="Does not raised error when is list"):
            x = [1,2,3,4]
            _check_is_numpy_1_D(x, param_name="param", language='en')

    def test_two_dimension(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value has 2 dimensions"):
            x = np.array([[1,2,3,4]])
            _check_is_numpy_1_D(x, param_name="param", language='en')

    def test_correct(self):
        x = np.array([1,2,3,4])
        result = _check_is_numpy_1_D(x, param_name="param", language='en')
        self.assertTrue(result, msg="Does not return True when the input is np.array([1,2,3,4])")






if __name__ == "__main__":
    unittest.main()
