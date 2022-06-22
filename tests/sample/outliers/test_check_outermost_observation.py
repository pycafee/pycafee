"""Tests if the _check_outermost_observation function for Outlier detection is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_check_outermost_observation



--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sample/outliers/test_check_outermost_observation.py
    or
    python -m unittest -b tests/sample/outliers/test_check_outermost_observation.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sample.outliers import _check_outermost_observation
import numpy as np
os.system('cls')

class Test_check_outermost_observation(unittest.TestCase):


    def test_min(self):
        x = np.array([1, 1, 2, 3, -20])
        result = _check_outermost_observation(x)
        self.assertIsInstance(result, str, msg="Output is not a str")
        self.assertEqual(result, "min", msg="output not min when it should")

        x = np.array([1, 2, 5, 10, 11, 12, 13])
        result = _check_outermost_observation(x)
        self.assertIsInstance(result, str, msg="Output is not a str")
        self.assertEqual(result, "min", msg="output not min when it should")

    def test_max(self):
        x = np.array([1, 1, 2, 3, 20])
        result = _check_outermost_observation(x)
        self.assertIsInstance(result, str, msg="Output is not a str")
        self.assertEqual(result, "max", msg="output not min when it should")

        x = np.array([1, 2, 3, 4, 5, 13])
        result = _check_outermost_observation(x)
        self.assertIsInstance(result, str, msg="Output is not a str")
        self.assertEqual(result, "max", msg="output not min when it should")

    def test_equal(self):
        x = np.array([1, 2, 3, 4])
        result = _check_outermost_observation(x)
        self.assertIsInstance(result, str, msg="Output is not a str")
        self.assertEqual(result, "max", msg="output not min when it should")

        x = np.array([10, 20, 30, 40, 50])
        result = _check_outermost_observation(x)
        self.assertIsInstance(result, str, msg="Output is not a str")
        self.assertEqual(result, "max", msg="output not min when it should")



# are y read to jummmmmppppp? https://youtu.be/m9P2WJI0A_c?t=233

if __name__ == "__main__":
    unittest.main()
