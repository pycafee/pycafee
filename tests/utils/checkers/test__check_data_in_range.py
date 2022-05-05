"""Tests if the _check_data_in_range is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_check_data_in_range
    This class tests if the 'value' is in a range. A ValueError should be raised when value is not in range. True should be returned if value is in the range.


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/checkers/test__check_data_in_range.py
    or
    python -m unittest -b tests/utils/helpers/test__check_data_in_range.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.utils.checkers import _check_data_in_range
import numpy as np
os.system('cls')

class Test_check_is_bool(unittest.TestCase):

    def test_fail(self):
        with self.assertRaises(ValueError, msg="Does not raised error when value not in range"):
            _check_data_in_range(5, "parameter", 0.0, 1.0, language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value not in range"):
            _check_data_in_range(1.0, "parameter", 0.0, 1.0, language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value not in range"):
            _check_data_in_range(5, "parameter", -1.0, 1.0, language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value not in range"):
            _check_data_in_range(-5, "parameter", 0.0, 1.0, language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when value not in range"):
            _check_data_in_range(5, "parameter", 50, 100, language='en')

    def test_pass(self):
        result = _check_data_in_range(0.5, "parameter", 0.0, 1.0, language='en')
        self.assertTrue(result, msg = "Raised error when value in range")

        result = _check_data_in_range(0.5, "parameter", 1.0, 0.0, language='en')
        self.assertTrue(result, msg = "Raised error when value in range")

        result = _check_data_in_range(0.0, "parameter", -1.0, 1.0, language='en')
        self.assertTrue(result, msg = "Raised error when value in range")




if __name__ == "__main__":
    unittest.main()
