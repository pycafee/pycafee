"""Tests if the test_get_critical_value is working as expected

---> Class Test_get_critical_value


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sample/outliers/Dixon/test_get_critical_value.py
    or
    python -m unittest -b tests/sample/outliers/Dixon/test_get_critical_value.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sample.outliers import Dixon
import numpy as np
os.system('cls')


class Test_Raises(unittest.TestCase):


    def test_ratio(self):
        with self.assertRaises(ValueError, msg="Does not raised error when ratio is wrong"):
            teste = Dixon()
            result = teste.get_critical_value(5, ratio='r')

        with self.assertRaises(ValueError, msg="Does not raised error when ratio is wrong"):
            teste = Dixon()
            result = teste.get_critical_value(5, ratio='r23')

        with self.assertRaises(ValueError, msg="Does not raised error when ratio is wrong"):
            teste = Dixon()
            result = teste.get_critical_value(5, ratio='r1')


    def test_n_rep(self):
        with self.assertRaises(ValueError, msg="Does not raised error when n_rep not allowed"):
            teste = Dixon()
            result = teste.get_critical_value(2)

        with self.assertRaises(ValueError, msg="Does not raised error when n_rep not allowed"):
            teste = Dixon()
            result = teste.get_critical_value(32)

        with self.assertRaises(ValueError, msg="Does not raised error when n_rep not allowed"):
            teste = Dixon()
            result = teste.get_critical_value(2, ratio="r10")

        with self.assertRaises(ValueError, msg="Does not raised error when n_rep not allowed"):
            teste = Dixon()
            result = teste.get_critical_value(32, ratio="r10")

        with self.assertRaises(ValueError, msg="Does not raised error when n_rep not allowed"):
            teste = Dixon()
            result = teste.get_critical_value(2, ratio="r11")

        with self.assertRaises(ValueError, msg="Does not raised error when n_rep not allowed"):
            teste = Dixon()
            result = teste.get_critical_value(32, ratio="r11")

        with self.assertRaises(ValueError, msg="Does not raised error when n_rep not allowed"):
            teste = Dixon()
            result = teste.get_critical_value(2, ratio="r12")

        with self.assertRaises(ValueError, msg="Does not raised error when n_rep not allowed"):
            teste = Dixon()
            result = teste.get_critical_value(32, ratio="r12")

        with self.assertRaises(ValueError, msg="Does not raised error when n_rep not allowed"):
            teste = Dixon()
            result = teste.get_critical_value(2, ratio="r20")

        with self.assertRaises(ValueError, msg="Does not raised error when n_rep not allowed"):
            teste = Dixon()
            result = teste.get_critical_value(32, ratio="r20")

        with self.assertRaises(ValueError, msg="Does not raised error when n_rep not allowed"):
            teste = Dixon()
            result = teste.get_critical_value(2, ratio="r21")

        with self.assertRaises(ValueError, msg="Does not raised error when n_rep not allowed"):
            teste = Dixon()
            result = teste.get_critical_value(32, ratio="r21")

        with self.assertRaises(ValueError, msg="Does not raised error when n_rep not allowed"):
            teste = Dixon()
            result = teste.get_critical_value(2, ratio="r22")

        with self.assertRaises(ValueError, msg="Does not raised error when n_rep not allowed"):
            teste = Dixon()
            result = teste.get_critical_value(32, ratio="r22")


class Test_get_critical_value(unittest.TestCase):


    def test_result(self):
        teste = Dixon()
        result = teste.get_critical_value(5)
        result1 = teste.get_critical_value(5, ratio="r10")
        self.assertEqual(result[0], result1[0], msg="distinct critical value when ratio is None and ratio is 'r10'")
        self.assertIsInstance(result, tuple, msg="output not a tuple")
        self.assertIsInstance(result1, tuple, msg="output not a tuple")
        self.assertIsInstance(result[0], float, msg="critical not float")
        self.assertIsInstance(result1[0], float, msg="critical not float")
        self.assertIsInstance(result[1], float, msg="alfa not float")
        self.assertIsInstance(result1[1], float, msg="alfa not float")

    def test_r10(self):
        teste = Dixon()
        result = teste.get_critical_value(5, ratio="r10")
        self.assertEqual(result[0], 0.710, msg="wrong critical value when 'r10'")
        self.assertEqual(result[1], 0.05, msg="wrong alfa value when 'r10'")

        result = teste.get_critical_value(13, ratio="r10")
        self.assertEqual(result[0], 0.410, msg="wrong critical value when 'r10'")
        self.assertEqual(result[1], 0.05, msg="wrong alfa value when when alfa None")

        result = teste.get_critical_value(13, ratio="r10", alfa=0.05)
        self.assertEqual(result[0], 0.410, msg="wrong critical value when 'r10'")
        self.assertEqual(result[1], 0.05, msg="wrong alfa value when when alfa 0.05")

        result = teste.get_critical_value(13, ratio="r10", alfa=0.2)
        self.assertEqual(result[0], 0.305, msg="wrong critical value when 'r10'")
        self.assertEqual(result[1], 0.2, msg="wrong alfa value when alfa 0.2")

        result = teste.get_critical_value(23, ratio="r10", alfa=0.1)
        self.assertEqual(result[0], 0.285, msg="wrong critical value when 'r10'")
        self.assertEqual(result[1], 0.1, msg="wrong alfa value when alfa 0.1")

        result = teste.get_critical_value(25, ratio="r10", alfa=0.04)
        self.assertEqual(result[0], 0.329, msg="wrong critical value when 'r10'")
        self.assertEqual(result[1], 0.04, msg="wrong alfa value when alfa 0.04")

        result = teste.get_critical_value(30, ratio="r10", alfa=0.02)
        self.assertEqual(result[0], 0.341, msg="wrong critical value when 'r10'")
        self.assertEqual(result[1], 0.02, msg="wrong alfa value when alfa 0.02")

        result = teste.get_critical_value(10, ratio="r10", alfa=0.01)
        self.assertEqual(result[0], 0.568, msg="wrong critical value when 'r10'")
        self.assertEqual(result[1], 0.01, msg="wrong alfa value when alfa 0.01")

    def test_r11(self):
        teste = Dixon()
        result = teste.get_critical_value(5, ratio="r11")
        self.assertEqual(result[0], 0.863, msg="wrong critical value when 'r11'")
        self.assertEqual(result[1], 0.05, msg="wrong alfa value when alfa None")

        result = teste.get_critical_value(13, ratio="r11")
        self.assertEqual(result[0], 0.461, msg="wrong critical value when 'r11'")
        self.assertEqual(result[1], 0.05, msg="wrong alfa value when when alfa None")

        result = teste.get_critical_value(13, ratio="r11", alfa=0.05)
        self.assertEqual(result[0], 0.461, msg="wrong critical value when 'r11'")
        self.assertEqual(result[1], 0.05, msg="wrong alfa value when when alfa 0.05")

        result = teste.get_critical_value(13, ratio="r11", alfa=0.2)
        self.assertEqual(result[0], 0.350, msg="wrong critical value when 'r11'")
        self.assertEqual(result[1], 0.2, msg="wrong alfa value when alfa 0.2")

        result = teste.get_critical_value(23, ratio="r11", alfa=0.1)
        self.assertEqual(result[0], 0.314, msg="wrong critical value when 'r11'")
        self.assertEqual(result[1], 0.1, msg="wrong alfa value when alfa 0.1")

        result = teste.get_critical_value(25, ratio="r11", alfa=0.04)
        self.assertEqual(result[0], 0.359, msg="wrong critical value when 'r11'")
        self.assertEqual(result[1], 0.04, msg="wrong alfa value when alfa 0.04")

        result = teste.get_critical_value(30, ratio="r11", alfa=0.02)
        self.assertEqual(result[0], 0.369, msg="wrong critical value when 'r11'")
        self.assertEqual(result[1], 0.02, msg="wrong alfa value when alfa 0.02")

        result = teste.get_critical_value(10, ratio="r11", alfa=0.01)
        self.assertEqual(result[0], 0.639, msg="wrong critical value when 'r11'")
        self.assertEqual(result[1], 0.01, msg="wrong alfa value when alfa 0.01")

    def test_r12(self):
        teste = Dixon()
        result = teste.get_critical_value(5, ratio="r12")
        self.assertEqual(result[0], 0.980, msg="wrong critical value when 'r12'")
        self.assertEqual(result[1], 0.05, msg="wrong alfa value when alfa None")

        result = teste.get_critical_value(13, ratio="r12")
        self.assertEqual(result[0], 0.505, msg="wrong critical value when 'r12'")
        self.assertEqual(result[1], 0.05, msg="wrong alfa value when when alfa None")

        result = teste.get_critical_value(13, ratio="r12", alfa=0.05)
        self.assertEqual(result[0], 0.505, msg="wrong critical value when 'r12'")
        self.assertEqual(result[1], 0.05, msg="wrong alfa value when when alfa 0.05")

        result = teste.get_critical_value(13, ratio="r12", alfa=0.2)
        self.assertEqual(result[0], 0.387, msg="wrong critical value when 'r12'")
        self.assertEqual(result[1], 0.2, msg="wrong alfa value when alfa 0.2")

        result = teste.get_critical_value(23, ratio="r12", alfa=0.1)
        self.assertEqual(result[0], 0.336, msg="wrong critical value when 'r12'")
        self.assertEqual(result[1], 0.1, msg="wrong alfa value when alfa 0.1")

        result = teste.get_critical_value(25, ratio="r12", alfa=0.04)
        self.assertEqual(result[0], 0.381, msg="wrong critical value when 'r12'")
        self.assertEqual(result[1], 0.04, msg="wrong alfa value when alfa 0.04")

        result = teste.get_critical_value(30, ratio="r12", alfa=0.02)
        self.assertEqual(result[0], 0.389, msg="wrong critical value when 'r12'")
        self.assertEqual(result[1], 0.02, msg="wrong alfa value when alfa 0.02")

        result = teste.get_critical_value(10, ratio="r12", alfa=0.01)
        self.assertEqual(result[0], 0.694, msg="wrong critical value when 'r12'")
        self.assertEqual(result[1], 0.01, msg="wrong alfa value when alfa 0.01")

    # more tests due to the table is more complex for this ratio
    def test_r20(self):
        teste = Dixon()
        result = teste.get_critical_value(5, ratio="r20")
        self.assertEqual(result[0], 0.890, msg="wrong critical value when 'r20'")
        self.assertEqual(result[1], 0.05, msg="wrong alfa value when alfa None")

        result = teste.get_critical_value(13, ratio="r20")
        self.assertEqual(result[0], 0.506, msg="wrong critical value when 'r20'")
        self.assertEqual(result[1], 0.05, msg="wrong alfa value when when alfa None")

        result = teste.get_critical_value(13, ratio="r20", alfa=0.05)
        self.assertEqual(result[0], 0.506, msg="wrong critical value when 'r20'")
        self.assertEqual(result[1], 0.05, msg="wrong alfa value when when alfa 0.05")

        result = teste.get_critical_value(13, ratio="r20", alfa=0.2)
        self.assertEqual(result[0], 0.411, msg="wrong critical value when 'r20'")
        self.assertEqual(result[1], 0.2, msg="wrong alfa value when alfa 0.2")

        result = teste.get_critical_value(23, ratio="r20", alfa=0.1)
        self.assertEqual(result[0], 0.358, msg="wrong critical value when 'r20'")
        self.assertEqual(result[1], 0.1, msg="wrong alfa value when alfa 0.1")

        result = teste.get_critical_value(25, ratio="r20", alfa=0.04)
        self.assertEqual(result[0], 0.395, msg="wrong critical value when 'r20'")
        self.assertEqual(result[1], 0.04, msg="wrong alfa value when alfa 0.04")

        result = teste.get_critical_value(30, ratio="r20", alfa=0.02)
        self.assertEqual(result[0], 0.402, msg="wrong critical value when 'r20'")
        self.assertEqual(result[1], 0.02, msg="wrong alfa value when alfa 0.02")

        result = teste.get_critical_value(10, ratio="r20", alfa=0.01)
        self.assertEqual(result[0], 0.664, msg="wrong critical value when 'r20'")
        self.assertEqual(result[1], 0.01, msg="wrong alfa value when alfa 0.01")

        result = teste.get_critical_value(21, ratio="r20", alfa=0.10)
        self.assertEqual(result[0], 0.371, msg="wrong critical value when 'r20'")
        self.assertEqual(result[1], 0.1, msg="wrong alfa value when alfa 0.10")

        result = teste.get_critical_value(23, ratio="r20", alfa=0.10)
        self.assertEqual(result[0], 0.358, msg="wrong critical value when 'r20'")
        self.assertEqual(result[1], 0.1, msg="wrong alfa value when alfa 0.10")

        result = teste.get_critical_value(25, ratio="r20", alfa=0.10)
        self.assertEqual(result[0], 0.346, msg="wrong critical value when 'r20'")
        self.assertEqual(result[1], 0.1, msg="wrong alfa value when alfa 0.10")

        result = teste.get_critical_value(28, ratio="r20", alfa=0.10)
        self.assertEqual(result[0], 0.333, msg="wrong critical value when 'r20'")
        self.assertEqual(result[1], 0.1, msg="wrong alfa value when alfa 0.10")

        result = teste.get_critical_value(30, ratio="r20", alfa=0.10)
        self.assertEqual(result[0], 0.326, msg="wrong critical value when 'r20'")
        self.assertEqual(result[1], 0.1, msg="wrong alfa value when alfa 0.10")


    def test_r21(self):
        teste = Dixon()
        result = teste.get_critical_value(5, ratio="r21")
        self.assertEqual(result[0], 0.987, msg="wrong critical value when 'r21'")
        self.assertEqual(result[1], 0.05, msg="wrong alfa value when alfa None")

        result = teste.get_critical_value(13, ratio="r21")
        self.assertEqual(result[0], 0.565, msg="wrong critical value when 'r21'")
        self.assertEqual(result[1], 0.05, msg="wrong alfa value when when alfa None")

        result = teste.get_critical_value(13, ratio="r21", alfa=0.05)
        self.assertEqual(result[0], 0.565, msg="wrong critical value when 'r21'")
        self.assertEqual(result[1], 0.05, msg="wrong alfa value when when alfa 0.05")

        result = teste.get_critical_value(13, ratio="r21", alfa=0.2)
        self.assertEqual(result[0], 0.467, msg="wrong critical value when 'r21'")
        self.assertEqual(result[1], 0.2, msg="wrong alfa value when alfa 0.2")

        result = teste.get_critical_value(23, ratio="r21", alfa=0.1)
        self.assertEqual(result[0], 0.395, msg="wrong critical value when 'r21'")
        self.assertEqual(result[1], 0.1, msg="wrong alfa value when alfa 0.1")

        result = teste.get_critical_value(25, ratio="r21", alfa=0.04)
        self.assertEqual(result[0], 0.431, msg="wrong critical value when 'r21'")
        self.assertEqual(result[1], 0.04, msg="wrong alfa value when alfa 0.04")

        result = teste.get_critical_value(30, ratio="r21", alfa=0.02)
        self.assertEqual(result[0], 0.433, msg="wrong critical value when 'r21'")
        self.assertEqual(result[1], 0.02, msg="wrong alfa value when alfa 0.02")

        result = teste.get_critical_value(10, ratio="r21", alfa=0.01)
        self.assertEqual(result[0], 0.760, msg="wrong critical value when 'r21'")
        self.assertEqual(result[1], 0.01, msg="wrong alfa value when alfa 0.01")

    def test_r22(self):
        teste = Dixon()
        result = teste.get_critical_value(6, ratio="r22")
        self.assertEqual(result[0], 0.990, msg="wrong critical value when 'r22'")
        self.assertEqual(result[1], 0.05, msg="wrong alfa value when alfa None")

        result = teste.get_critical_value(13, ratio="r22")
        self.assertEqual(result[0], 0.616, msg="wrong critical value when 'r22'")
        self.assertEqual(result[1], 0.05, msg="wrong alfa value when when alfa None")

        result = teste.get_critical_value(13, ratio="r22", alfa=0.05)
        self.assertEqual(result[0], 0.616, msg="wrong critical value when 'r22'")
        self.assertEqual(result[1], 0.05, msg="wrong alfa value when when alfa 0.05")

        result = teste.get_critical_value(13, ratio="r22", alfa=0.2)
        self.assertEqual(result[0], 0.515, msg="wrong critical value when 'r22'")
        self.assertEqual(result[1], 0.2, msg="wrong alfa value when alfa 0.2")

        result = teste.get_critical_value(23, ratio="r22", alfa=0.1)
        self.assertEqual(result[0], 0.421, msg="wrong critical value when 'r22'")
        self.assertEqual(result[1], 0.1, msg="wrong alfa value when alfa 0.1")

        result = teste.get_critical_value(25, ratio="r22", alfa=0.04)
        self.assertEqual(result[0], 0.457, msg="wrong critical value when 'r22'")
        self.assertEqual(result[1], 0.04, msg="wrong alfa value when alfa 0.04")

        result = teste.get_critical_value(30, ratio="r22", alfa=0.02)
        self.assertEqual(result[0], 0.457, msg="wrong critical value when 'r22'")
        self.assertEqual(result[1], 0.02, msg="wrong alfa value when alfa 0.02")

        result = teste.get_critical_value(10, ratio="r22", alfa=0.01)
        self.assertEqual(result[0], 0.826, msg="wrong critical value when 'r22'")
        self.assertEqual(result[1], 0.01, msg="wrong alfa value when alfa 0.01")


if __name__ == "__main__":
    unittest.main()
