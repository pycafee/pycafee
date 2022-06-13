"""Tests if the _check_dixon_division_by_zero is working as expected

--------------------------------------------------------------------------------
Description:

---> class Test_raises: this class checks if the function is raising ZeroDivisionError when position 1 and 2 are equal

---> class Test_pass: this class checks if the function returns True if position 1 is different from 2


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sample/Dixon/test__check_dixon_division_by_zero.py
    or
    python -m unittest -b tests/sample/Dixon/test__check_dixon_division_by_zero.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sample.dixon import _check_dixon_division_by_zero
import numpy as np
os.system('cls')

class Test_raises(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([1, 2, 3, 4, 5, 6, 6])
        cls.y = np.array([1.1, 1.1, 2, 3, 4, 5, 6, 6])
        cls.z = np.array([1, 1, 1, 1, 1, 1, 1])



    def test_equals(self):
        with self.assertRaises(ZeroDivisionError, msg="Does not raised position 1 is equal to position_2"):
            _check_dixon_division_by_zero(self.x, -1, -2, 'en')

        with self.assertRaises(ZeroDivisionError, msg="Does not raised position 1 is equal to position_2"):
            _check_dixon_division_by_zero(self.y, 0, 1, 'en')

        with self.assertRaises(ZeroDivisionError, msg="Does not raised position 1 is equal to position_2"):
            _check_dixon_division_by_zero(self.z, 0, 5, 'en')

        with self.assertRaises(ZeroDivisionError, msg="Does not raised position 1 is equal to position_2"):
            _check_dixon_division_by_zero(self.z, 0, 5, 'pt-br')


class Test_pass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([1, 2, 3, 4, 5, 6, 6])
        cls.y = np.array([1.1, 1.1, 2, 3, 4, 5, 6, 6])
        cls.z = np.array([1.0001, 1, 1, 1, 1, 1, 1])

    def test_equals(self):
        result = _check_dixon_division_by_zero(self.x, -1, 0, 'en')
        self.assertTrue(result, msg="not True when position_1 is different from position_2")

        result = _check_dixon_division_by_zero(self.y, 0, -1, 'en')
        self.assertTrue(result, msg="not True when position_1 is different from position_2")

        result = _check_dixon_division_by_zero(self.z, 0, 5, 'en')
        self.assertTrue(result, msg="not True when position_1 is different from position_2")






if __name__ == "__main__":
    unittest.main()
