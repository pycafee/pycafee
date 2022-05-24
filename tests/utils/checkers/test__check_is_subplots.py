"""Tests if the _check_is_subplots is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_check_is_subplots
    # This class tests if the 'value' is a matplotlib.axes.SubplotBase. Several types of floats are tested with the assertTrue statement. Also, the function is tested against strings, tuples, lists, and integers, which should raise a ValueError that is caught with assertRaises.


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/checkers/test__check_is_subplots.py
    or
    python -m unittest -b tests/utils/helpers/test__check_is_subplots.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.utils.checkers import _check_is_subplots
import numpy as np
import matplotlib.pyplot as plt
os.system('cls')

class Test_check_is_subplots(unittest.TestCase):

    def test_string(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is a string"):
            _check_is_subplots("a", param_name="parameter", language='en')
            plt.close()
        with self.assertRaises(ValueError, msg="Does not raised error when value is a string"):
            _check_is_subplots("auisdhsa9d8ysadasd9oasdasdonha nsad\n", param_name="parameter", language='en')
            plt.close()

    def test_int(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is int"):
            _check_is_subplots(1, param_name="parameter", language='en')
            plt.close()
        with self.assertRaises(ValueError, msg="Does not raised error when value is int"):
            _check_is_subplots(np.int32(1), param_name="parameter", language='en')
            plt.close()
        with self.assertRaises(ValueError, msg="Does not raised error when value is int"):
            _check_is_subplots(np.int64(1), param_name="parameter", language='en')
            plt.close()

    def test_list(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is a list"):
            _check_is_subplots([1], param_name="parameter", language='en')
            plt.close()
        with self.assertRaises(ValueError, msg="Does not raised error when value is a list"):
            _check_is_subplots([[1]], param_name="parameter", language='en')
            plt.close()

    def test_tuple(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is a tuple"):
            _check_is_subplots((1,), param_name="parameter", language='en')
            plt.close()
        with self.assertRaises(ValueError, msg="Does not raised error when value is a tuple"):
            _check_is_subplots((1,1,1), param_name="parameter", language='en')
            plt.close()
        with self.assertRaises(ValueError, msg="Does not raised error when value is a tuple"):
            _check_is_subplots((1, (1,), 1), param_name="parameter", language='en')
            plt.close()

    def test_empty(self):
        with self.assertRaises(TypeError, msg="Does not raised error when no value was passed"):
            _check_is_subplots(param_name="parameter", language='en')
            plt.close()

    def test_None(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is None"):
            _check_is_subplots(None, param_name="parameter", language='en')
            plt.close()

    def test_pass(self):

        fig, ax = plt.subplots()

        result = _check_is_subplots(ax, param_name="parameter", language='en')
        self.assertTrue(result, msg = "An error was raised when value was True")
        plt.close()





if __name__ == "__main__":
    unittest.main()
