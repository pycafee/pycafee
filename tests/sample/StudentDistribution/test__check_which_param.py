"""Tests if the test__check_which_param is working as expected

---> Class Test_check_which_param
    # This class tests if the 'value' is an integer number. Several types of integers are tested with the assertTrue statement. Also, the function is tested against strings, tuples, lists, and floats, which should raise a ValueError that is caught with assertRaises.

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sample/StudentDistribution/test__check_which_param.py
    or
    python -m unittest -b tests/sample/StudentDistribution/test__check_which_param.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sample.studentdistribution import _check_which_param
import numpy as np
os.system('cls')


class Test_check_which_param(unittest.TestCase):


    def test_which(self):
        with self.assertRaises(ValueError, msg="Does not raised error when which not two-side or one-side"):
            _check_which_param("bilate", 'en')

        with self.assertRaises(ValueError, msg="Does not raised error when which not two-side or one-side"):
            _check_which_param("bill", 'en')

        with self.assertRaises(ValueError, msg="Does not raised error when which not two-side or one-side"):
            _check_which_param("bill", 'pt-br')

        with self.assertRaises(ValueError, msg="Does not raised error when which not two-side or one-side"):
            _check_which_param("two", 'pt-br')

        with self.assertRaises(ValueError, msg="Does not raised error when which not two-side or one-side"):
            _check_which_param("side", 'pt-br')

        with self.assertRaises(ValueError, msg="Does not raised error when which not two-side or one-side"):
            _check_which_param("one", 'pt-br')

        with self.assertRaises(ValueError, msg="Does not raised error when which not two-side or one-side"):
            _check_which_param("twoside", 'pt-br')

        with self.assertRaises(ValueError, msg="Does not raised error when which not two-side or one-side"):
            _check_which_param("oneside", 'pt-br')


    def test_pass(self):

        result = _check_which_param("one-side", 'pt-br')
        self.assertEqual(result, "one-side")

        result = _check_which_param("two-side", 'en')
        self.assertEqual(result, "two-side")








# m. e. t. l https://youtu.be/7idcgZGHCjM?t=140

if __name__ == "__main__":
    unittest.main()
