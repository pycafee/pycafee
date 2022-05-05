"""Tests if the _check_is_positive is working as expected

---> Class _check_is_positive
    This class tests if the 'value' is a number higher than zero (positive). It tests agains negative values, which should raise ValueError. Also, it checks if True is returned when value is in fact positive.

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/checkers/test__check_is_positive.py
    or
    python -m unittest -b tests/utils/checkers/test__check_is_positive.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.utils.checkers import _check_is_positive
import numpy as np
os.system('cls')

class Test_check_is_positive(unittest.TestCase):

    def test_negative(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value is -1"):
            _check_is_positive(-1, "param", 'en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is -0.00000000000001"):
            _check_is_positive(-0.00000000000001, "param", 'en')
        with self.assertRaises(ValueError, msg="Does not raised error when value is -10000000000.111111"):
            _check_is_positive(-10000000000.111111, "param", 'en')


    def test_zero(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value 0"):
            _check_is_positive(0, "param", 'en')
        with self.assertRaises(ValueError, msg="Does not raised error when value 0"):
            _check_is_positive(0.0, "param", 'en')

    def test_pass(self):
        result = _check_is_positive(1, "param", 'en')
        self.assertTrue(result, msg="Does not returned True when value is 1")

        result = _check_is_positive(1.00001, "param", 'en')
        self.assertTrue(result, msg="Does not returned True when value is 1.00001")

        result = _check_is_positive(0.000000000001, "param", 'en')
        self.assertTrue(result, msg="Does not returned True when value is 0.000000000001")

        result = _check_is_positive(1186486464161647, "param", 'en')
        self.assertTrue(result, msg="Does not returned True when value is 1186486464161647")






if __name__ == "__main__":
    unittest.main()
