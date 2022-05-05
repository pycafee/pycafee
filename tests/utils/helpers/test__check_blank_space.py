"""Tests if the _check_blank_space is working as expected

---> Class Test_check_blank_space
    This class tests if the _check_blank_space function raises ValueError when a string has white spaces, and if it returns True if a string does not have any white spaces


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/helpers/test__check_blank_space.py
    or
    python -m unittest -b tests/utils/helpers/test__check_blank_space.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.utils.helpers import _check_blank_space
os.system("cls")
class Test_check_blank_space(unittest.TestCase):

    def test_with_white_space(self):
        with self.assertRaises(ValueError, msg="Does not raised string has white space"):
            _check_blank_space("param 1", "param_name", "en")
        with self.assertRaises(ValueError, msg="Does not raised string has white space"):
            _check_blank_space("para m 1", "param_name", "en")
        with self.assertRaises(ValueError, msg="Does not raised string has white space"):
            _check_blank_space("param1 ", "param_name", "en")
        with self.assertRaises(ValueError, msg="Does not raised string has white space"):
            _check_blank_space(" param1 ", "param_name", "en")
        with self.assertRaises(ValueError, msg="Does not raised string has white space"):
            _check_blank_space("1 param1", "param_name", "en")

    def test_without_white_space(self):
        result = _check_blank_space("param1", "param_name", "en")
        self.assertTrue(result, msg = "Did not return True when value does not have white space")
        result = _check_blank_space("1param1", "param_name", "en")
        self.assertTrue(result, msg = "Did not return True when value does not have white space")







# akaku somare, makka ni somare https://youtu.be/yGuuQ_45aTU?t=322
if __name__ == "__main__":
    unittest.main()
