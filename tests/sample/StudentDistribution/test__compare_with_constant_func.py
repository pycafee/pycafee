"""Tests if the test__compare_with_constant_func is working as expected

---> Class Test_compare_with_constant_func: the output instance is tested and the tcalc is test for some datasets


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sample/StudentDistribution/test__compare_with_constant_func.py
    or
    python -m unittest -b tests/sample/StudentDistribution/test__compare_with_constant_func.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sample.studentdistribution import _compare_with_constant_func
import numpy as np
os.system('cls')


class Test_compare_with_constant_func(unittest.TestCase):


    def test_result(self):
        result = _compare_with_constant_func(5, 5, 5, 5)
        self.assertIsInstance(result, float, msg="Output not float")

    def test_pass(self):
        result = _compare_with_constant_func(5, 5, 5, 5)
        self.assertAlmostEqual(result, 0, places=4, msg="wrong output")

        result = _compare_with_constant_func(3.2, 3.280600, 0.056549, 5)
        self.assertAlmostEqual(result, 3.18709, places=4, msg="wrong output")

        result = _compare_with_constant_func(8, 13.666667, 3.265986, 6)
        self.assertAlmostEqual(result, 4.25000, places=4, msg="wrong output")




if __name__ == "__main__":
    unittest.main()
