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
        self.assertIsInstance(result[0], float)
        self.assertIsInstance(result[1], float)
        self.assertIsInstance(result[2], float)
        self.assertIsInstance(result[3], str)
        teste = False
        if result[0] > 0:
            teste = True
        self.assertTrue(teste, msg="critical higher not positive")
        teste = False
        if result[1] < 0:
            teste = True
        self.assertTrue(teste, msg="critical lower not negative")

    def test_lower_higher(self):
        student = StudentDistribution()
        for i in range(2,10):
            result = student.get_critical_value(i)
            self.assertAlmostEqual(result[0], -1*result[1], msg="lower and higher does not match")

        for i in range(2,10):
            result = student.get_critical_value(i, alfa=0.01)
            self.assertAlmostEqual(result[0], -1*result[1], msg="lower and higher does not match")

        for i in range(2,10):
            result = student.get_critical_value(i, alfa=0.1)
            self.assertAlmostEqual(result[0], -1*result[1], msg="lower and higher does not match")

    def test_pass_two_side_alfa_5(self):
        student = StudentDistribution()
        a = student.get_critical_value(1, alfa=None)
        self.assertAlmostEqual(a[0], 12.706, places=3)
        self.assertEqual(a[2], 0.05)
        self.assertEqual(a[3], 'two-side')

        a = student.get_critical_value(2, alfa=None)
        self.assertAlmostEqual(a[0], 4.302, places=2)
        self.assertEqual(a[2], 0.05)
        self.assertEqual(a[3], 'two-side')

        a = student.get_critical_value(3, alfa=None)
        self.assertAlmostEqual(a[0], 3.182, places=2)
        self.assertEqual(a[2], 0.05)
        self.assertEqual(a[3], 'two-side')

        a = student.get_critical_value(4, alfa=None)
        self.assertAlmostEqual(a[0], 2.776, places=2)
        self.assertEqual(a[2], 0.05)
        self.assertEqual(a[3], 'two-side')

        a = student.get_critical_value(5, alfa=None)
        self.assertAlmostEqual(a[0], 2.570, places=2)
        self.assertEqual(a[2], 0.05)
        self.assertEqual(a[3], 'two-side')

        a = student.get_critical_value(6, alfa=None)
        self.assertAlmostEqual(a[0], 2.446, places=2)
        self.assertEqual(a[2], 0.05)
        self.assertEqual(a[3], 'two-side')

        a = student.get_critical_value(7, alfa=None)
        self.assertAlmostEqual(a[0], 2.364, places=2)
        self.assertEqual(a[2], 0.05)
        self.assertEqual(a[3], 'two-side')

        a = student.get_critical_value(8, alfa=None)
        self.assertAlmostEqual(a[0], 2.306, places=2)
        self.assertEqual(a[2], 0.05)
        self.assertEqual(a[3], 'two-side')

        a = student.get_critical_value(9, alfa=None)
        self.assertAlmostEqual(a[0], 2.262, places=2)
        self.assertEqual(a[2], 0.05)
        self.assertEqual(a[3], 'two-side')

        a = student.get_critical_value(10, alfa=None)
        self.assertAlmostEqual(a[0], 2.228, places=2)
        self.assertEqual(a[2], 0.05)
        self.assertEqual(a[3], 'two-side')
        
    def test_pass_two_side_alfa_10(self):
        student = StudentDistribution()
        a = student.get_critical_value(1, alfa=0.1)
        self.assertAlmostEqual(a[0], 6.313, places=2)
        self.assertEqual(a[2], 0.1)
        self.assertEqual(a[3], 'two-side')

        a = student.get_critical_value(2, alfa=0.1)
        self.assertAlmostEqual(a[0], 2.919, places=2)
        self.assertEqual(a[2], 0.1)
        self.assertEqual(a[3], 'two-side')

        a = student.get_critical_value(3, alfa=0.1)
        self.assertAlmostEqual(a[0], 2.353, places=2)
        self.assertEqual(a[2], 0.1)
        self.assertEqual(a[3], 'two-side')

        a = student.get_critical_value(4, alfa=0.1)
        self.assertAlmostEqual(a[0], 2.131, places=2)
        self.assertEqual(a[2], 0.1)
        self.assertEqual(a[3], 'two-side')

        a = student.get_critical_value(5, alfa=0.1)
        self.assertAlmostEqual(a[0], 2.015, places=2)
        self.assertEqual(a[2], 0.1)
        self.assertEqual(a[3], 'two-side')

        a = student.get_critical_value(6, alfa=0.1)
        self.assertAlmostEqual(a[0], 1.943, places=2)
        self.assertEqual(a[2], 0.1)
        self.assertEqual(a[3], 'two-side')

        a = student.get_critical_value(7, alfa=0.1)
        self.assertAlmostEqual(a[0], 1.894, places=2)
        self.assertEqual(a[2], 0.1)
        self.assertEqual(a[3], 'two-side')

        a = student.get_critical_value(8, alfa=0.1)
        self.assertAlmostEqual(a[0], 1.859, places=2)
        self.assertEqual(a[2], 0.1)
        self.assertEqual(a[3], 'two-side')

        a = student.get_critical_value(9, alfa=0.1)
        self.assertAlmostEqual(a[0], 1.833, places=2)
        self.assertEqual(a[2], 0.1)
        self.assertEqual(a[3], 'two-side')

        a = student.get_critical_value(10, alfa=0.1)
        self.assertAlmostEqual(a[0], 1.812, places=2)
        self.assertEqual(a[2], 0.1)
        self.assertEqual(a[3], 'two-side')

    def test_pass_one_side_alfa_5(self):
        student = StudentDistribution()
        a = student.get_critical_value(1, alfa=None, which='one-side')
        self.assertAlmostEqual(a[0], 6.313, places=2)
        self.assertEqual(a[2], 0.05)
        self.assertEqual(a[3], 'one-side')

        a = student.get_critical_value(2, alfa=None, which='one-side')
        self.assertAlmostEqual(a[0], 2.919, places=2)
        self.assertEqual(a[2], 0.05)
        self.assertEqual(a[3], 'one-side')

        a = student.get_critical_value(3, alfa=None, which='one-side')
        self.assertAlmostEqual(a[0], 2.353, places=2)
        self.assertEqual(a[2], 0.05)
        self.assertEqual(a[3], 'one-side')

        a = student.get_critical_value(4, alfa=None, which='one-side')
        self.assertAlmostEqual(a[0], 2.131, places=2)
        self.assertEqual(a[2], 0.05)
        self.assertEqual(a[3], 'one-side')

        a = student.get_critical_value(5, alfa=None, which='one-side')
        self.assertAlmostEqual(a[0], 2.015, places=2)
        self.assertEqual(a[2], 0.05)
        self.assertEqual(a[3], 'one-side')

        a = student.get_critical_value(6, alfa=None, which='one-side')
        self.assertAlmostEqual(a[0], 1.943, places=2)
        self.assertEqual(a[2], 0.05)
        self.assertEqual(a[3], 'one-side')

        a = student.get_critical_value(7, alfa=None, which='one-side')
        self.assertAlmostEqual(a[0], 1.894, places=2)
        self.assertEqual(a[2], 0.05)
        self.assertEqual(a[3], 'one-side')

        a = student.get_critical_value(8, alfa=None, which='one-side')
        self.assertAlmostEqual(a[0], 1.859, places=2)
        self.assertEqual(a[2], 0.05)
        self.assertEqual(a[3], 'one-side')

        a = student.get_critical_value(9, alfa=None, which='one-side')
        self.assertAlmostEqual(a[0], 1.833, places=2)
        self.assertEqual(a[2], 0.05)
        self.assertEqual(a[3], 'one-side')

        a = student.get_critical_value(10, alfa=None, which='one-side')
        self.assertAlmostEqual(a[0], 1.812, places=2)
        self.assertEqual(a[2], 0.05)
        self.assertEqual(a[3], 'one-side')

    def test_pass_one_side_alfa_10(self):
        student = StudentDistribution()
        a = student.get_critical_value(1, alfa=0.1, which='one-side')
        self.assertAlmostEqual(a[0], 3.077, places=2)
        self.assertEqual(a[2], 0.1)
        self.assertEqual(a[3], 'one-side')

        a = student.get_critical_value(2, alfa=0.1, which='one-side')
        self.assertAlmostEqual(a[0], 1.885, places=2)
        self.assertEqual(a[2], 0.1)
        self.assertEqual(a[3], 'one-side')

        a = student.get_critical_value(3, alfa=0.1, which='one-side')
        self.assertAlmostEqual(a[0], 1.637, places=2)
        self.assertEqual(a[2], 0.1)
        self.assertEqual(a[3], 'one-side')

        a = student.get_critical_value(4, alfa=0.1, which='one-side')
        self.assertAlmostEqual(a[0], 1.533, places=2)
        self.assertEqual(a[2], 0.1)
        self.assertEqual(a[3], 'one-side')

        a = student.get_critical_value(5, alfa=0.1, which='one-side')
        self.assertAlmostEqual(a[0], 1.475, places=2)
        self.assertEqual(a[2], 0.1)
        self.assertEqual(a[3], 'one-side')

        a = student.get_critical_value(6, alfa=0.1, which='one-side')
        self.assertAlmostEqual(a[0], 1.439, places=2)
        self.assertEqual(a[2], 0.1)
        self.assertEqual(a[3], 'one-side')

        a = student.get_critical_value(7, alfa=0.1, which='one-side')
        self.assertAlmostEqual(a[0], 1.414, places=2)
        self.assertEqual(a[2], 0.1)
        self.assertEqual(a[3], 'one-side')

        a = student.get_critical_value(8, alfa=0.1, which='one-side')
        self.assertAlmostEqual(a[0], 1.396, places=2)
        self.assertEqual(a[2], 0.1)
        self.assertEqual(a[3], 'one-side')

        a = student.get_critical_value(9, alfa=0.1, which='one-side')
        self.assertAlmostEqual(a[0], 1.383, places=2)
        self.assertEqual(a[2], 0.1)
        self.assertEqual(a[3], 'one-side')

        a = student.get_critical_value(10, alfa=0.1, which='one-side')
        self.assertAlmostEqual(a[0], 1.372, places=2)
        self.assertEqual(a[2], 0.1)
        self.assertEqual(a[3], 'one-side')


if __name__ == "__main__":
    unittest.main()
