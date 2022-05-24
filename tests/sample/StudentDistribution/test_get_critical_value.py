"""Tests if the test_get_critical_value is working as expected

---> Class Test_get_critical_value
    This class test if the critical value returned is correct. It checks for both outputs (if they are equal), checks if the lower and higher values are opossitve, and checks the critical value for 0 < gl < 11 for alfa = 0.05 and 0.10.

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sample/StudentDistribution/test_get_critical_value.py
    or
    python -m unittest -b tests/sample/StudentDistribution/test_get_critical_value.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sample.studentdistribution import StudentDistribution
import numpy as np
os.system('cls')


class Test_get_critical_value(unittest.TestCase):


    def test_result(self):
        student = StudentDistribution()
        result = student.get_critical_value(5)
        self.assertIsInstance(result, tuple)
        self.assertIsInstance(result[0], tuple)
        self.assertIsInstance(result[1], list)

    def test_result_a_b(self):
        student = StudentDistribution()
        a, b = student.get_critical_value(5)
        self.assertAlmostEqual(a[1], b[0], places=2)
        self.assertAlmostEqual(a[0], b[1], places=2)

    def test_result_inverse(self):
        student = StudentDistribution()
        a, b = student.get_critical_value(5)
        self.assertAlmostEqual(a[0], -1*a[1])
        self.assertAlmostEqual(b[0], -1*b[1])

        student = StudentDistribution()
        a, b = student.get_critical_value(5, which='one-side')
        self.assertAlmostEqual(a[0], -1*a[1])
        self.assertAlmostEqual(b[0], -1*b[1])

    def test_pass_two_side_alfa_5(self):
        student = StudentDistribution()
        a, b = student.get_critical_value(1, alfa=None)
        self.assertEqual(a[0], 12.706)

        a, b = student.get_critical_value(2, alfa=None)
        self.assertEqual(a[0], 4.302)

        a, b = student.get_critical_value(3, alfa=None)
        self.assertEqual(a[0], 3.182)

        a, b = student.get_critical_value(4, alfa=None)
        self.assertEqual(a[0], 2.776)

        a, b = student.get_critical_value(5, alfa=None)
        self.assertEqual(a[0], 2.570)

        a, b = student.get_critical_value(6, alfa=None)
        self.assertEqual(a[0], 2.446)

        a, b = student.get_critical_value(7, alfa=None)
        self.assertEqual(a[0], 2.364)

        a, b = student.get_critical_value(8, alfa=None)
        self.assertEqual(a[0], 2.306)

        a, b = student.get_critical_value(9, alfa=None)
        self.assertEqual(a[0], 2.262)

        a, b = student.get_critical_value(10, alfa=None)
        self.assertEqual(a[0], 2.228)

    def test_pass_two_side_alfa_10(self):
        student = StudentDistribution()
        a, b = student.get_critical_value(1, alfa=0.1)
        self.assertEqual(a[0], 6.313)

        a, b = student.get_critical_value(2, alfa=0.1)
        self.assertEqual(a[0], 2.919)

        a, b = student.get_critical_value(3, alfa=0.1)
        self.assertEqual(a[0], 2.353)

        a, b = student.get_critical_value(4, alfa=0.1)
        self.assertEqual(a[0], 2.131)

        a, b = student.get_critical_value(5, alfa=0.1)
        self.assertEqual(a[0], 2.015)

        a, b = student.get_critical_value(6, alfa=0.1)
        self.assertEqual(a[0], 1.943)

        a, b = student.get_critical_value(7, alfa=0.1)
        self.assertEqual(a[0], 1.894)

        a, b = student.get_critical_value(8, alfa=0.1)
        self.assertEqual(a[0], 1.859)

        a, b = student.get_critical_value(9, alfa=0.1)
        self.assertEqual(a[0], 1.833)

        a, b = student.get_critical_value(10, alfa=0.1)
        self.assertEqual(a[0], 1.812)

    def test_pass_one_side_alfa_5(self):
        student = StudentDistribution()
        a, b = student.get_critical_value(1, alfa=None, which='one-side')
        self.assertEqual(a[0], 6.313)

        a, b = student.get_critical_value(2, alfa=None, which='one-side')
        self.assertEqual(a[0], 2.919)

        a, b = student.get_critical_value(3, alfa=None, which='one-side')
        self.assertEqual(a[0], 2.353)

        a, b = student.get_critical_value(4, alfa=None, which='one-side')
        self.assertEqual(a[0], 2.131)

        a, b = student.get_critical_value(5, alfa=None, which='one-side')
        self.assertEqual(a[0], 2.015)

        a, b = student.get_critical_value(6, alfa=None, which='one-side')
        self.assertEqual(a[0], 1.943)

        a, b = student.get_critical_value(7, alfa=None, which='one-side')
        self.assertEqual(a[0], 1.894)

        a, b = student.get_critical_value(8, alfa=None, which='one-side')
        self.assertEqual(a[0], 1.859)

        a, b = student.get_critical_value(9, alfa=None, which='one-side')
        self.assertEqual(a[0], 1.833)

        a, b = student.get_critical_value(10, alfa=None, which='one-side')
        self.assertEqual(a[0], 1.812)

    def test_pass_one_side_alfa_10(self):
        student = StudentDistribution()
        a, b = student.get_critical_value(1, alfa=0.1, which='one-side')
        self.assertEqual(a[0], 3.077)

        a, b = student.get_critical_value(2, alfa=0.1, which='one-side')
        self.assertEqual(a[0], 1.885)

        a, b = student.get_critical_value(3, alfa=0.1, which='one-side')
        self.assertEqual(a[0], 1.637)

        a, b = student.get_critical_value(4, alfa=0.1, which='one-side')
        self.assertEqual(a[0], 1.533)

        a, b = student.get_critical_value(5, alfa=0.1, which='one-side')
        self.assertEqual(a[0], 1.475)

        a, b = student.get_critical_value(6, alfa=0.1, which='one-side')
        self.assertEqual(a[0], 1.439)

        a, b = student.get_critical_value(7, alfa=0.1, which='one-side')
        self.assertEqual(a[0], 1.414)

        a, b = student.get_critical_value(8, alfa=0.1, which='one-side')
        self.assertEqual(a[0], 1.396)

        a, b = student.get_critical_value(9, alfa=0.1, which='one-side')
        self.assertEqual(a[0], 1.383)

        a, b = student.get_critical_value(10, alfa=0.1, which='one-side')
        self.assertEqual(a[0], 1.372)









if __name__ == "__main__":
    unittest.main()
