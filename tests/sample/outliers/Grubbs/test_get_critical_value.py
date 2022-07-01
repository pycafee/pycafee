"""Tests if the test_get_critical_value is working as expected

---> Class Test_get_critical_value


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sample/outliers/Grubbs/test_get_critical_value.py
    or
    python -m unittest -b tests/sample/outliers/Grubbs/test_get_critical_value.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sample.outliers import Grubbs
import numpy as np
import sys
import io
os.system('cls')


class Test_Raises(unittest.TestCase):


    def test_kind_raises(self):
        with self.assertRaises(ValueError, msg="Does not raised error when kind is wrong"):
            teste = Grubbs()
            result = teste.get_critical_value(5, kind='r')

        with self.assertRaises(ValueError, msg="Does not raised error when kind is wrong"):
            teste = Grubbs()
            result = teste.get_critical_value(5, kind='threee')

        with self.assertRaises(ValueError, msg="Does not raised error when kind is wrong"):
            teste = Grubbs()
            result = teste.get_critical_value(5, kind='dois')


    def test_kind_raises_output(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            teste = Grubbs()
            result = teste.get_critical_value(5, kind='dois')
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "dois"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        ###############

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            teste = Grubbs()
            result = teste.get_critical_value(5, kind='threee')
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "threee"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        ###############


        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            teste = Grubbs()
            result = teste.get_critical_value(5, kind='r')
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "r"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        ###############


    def test_n_rep_raises(self):
        with self.assertRaises(ValueError, msg="Does not raised error when n_rep not allowed"):
            teste = Grubbs()
            result = teste.get_critical_value(2)

        with self.assertRaises(ValueError, msg="Does not raised error when n_rep not allowed"):
            teste = Grubbs()
            result = teste.get_critical_value(32)

        with self.assertRaises(ValueError, msg="Does not raised error when n_rep not allowed"):
            teste = Grubbs()
            result = teste.get_critical_value(3, kind="three")


    def test_n_rep_raises_output(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            teste = Grubbs()
            result = teste.get_critical_value(2)
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "2"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        ###############


    def test_alfa_raises(self):
        with self.assertRaises(ValueError, msg="Does not raised error when alfa not allowed"):
            teste = Grubbs()
            result = teste.get_critical_value(5, alfa=0.02)

        with self.assertRaises(ValueError, msg="Does not raised error when alfa is str"):
            teste = Grubbs()
            result = teste.get_critical_value(5, alfa="0.02")


    def test_alfa_raises_output(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            teste = Grubbs()
            result = teste.get_critical_value(5, alfa=0.02)
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "0.02"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")



class Test_get_critical_value(unittest.TestCase):


    def test_result_instances(self):
        teste = Grubbs()
        result = teste.get_critical_value(5)
        self.assertIsInstance(result, tuple, msg="output not a tuple")
        self.assertIsInstance(result[0], float, msg="critical not float")
        self.assertIsInstance(result[1], float, msg="alfa not float")

    def test_result_values(self):
        teste = Grubbs()
        result = teste.get_critical_value(5)
        self.assertEqual(result[0], 1.715, msg="wrong  critical value")
        self.assertEqual(result[1], 0.05, msg="wrong alfa")

        result = teste.get_critical_value(30)
        self.assertEqual(result[0], 2.908, msg="wrong  critical value")
        self.assertEqual(result[1], 0.05, msg="wrong alfa")

        result = teste.get_critical_value(15)
        self.assertEqual(result[0], 2.549, msg="wrong  critical value")
        self.assertEqual(result[1], 0.05, msg="wrong alfa")

        result = teste.get_critical_value(10, alfa=0.01)
        self.assertEqual(result[0], 2.482, msg="wrong  critical value")
        self.assertEqual(result[1], 0.01, msg="wrong alfa")

        result = teste.get_critical_value(24, alfa=0.01)
        self.assertEqual(result[0], 3.112, msg="wrong  critical value")
        self.assertEqual(result[1], 0.01, msg="wrong alfa")

        result = teste.get_critical_value(4, alfa=0.1)
        self.assertEqual(result[0], 1.463, msg="wrong  critical value")
        self.assertEqual(result[1], 0.1, msg="wrong alfa")

        result = teste.get_critical_value(29, alfa=0.1)
        self.assertEqual(result[0], 2.730, msg="wrong  critical value")
        self.assertEqual(result[1], 0.1, msg="wrong alfa")




if __name__ == "__main__":
    unittest.main()
