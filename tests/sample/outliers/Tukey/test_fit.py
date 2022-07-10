"""Tests if the test_fit is working as expected

---> Class Test_Tukey checks if the results are correc for some datasets. It also checks for raises ValueError

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sample/outliers/Tukey/test_fit.py
    or
    python -m unittest -b tests/sample/outliers/Tukey/test_fit.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sample.outliers import Tukey
import numpy as np
import sys
import io
os.system('cls')


class Test_Tukey(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9]) # sem outliers, valor superior é o extremo
        cls.y = np.array([6.3, 5.8, 7.1, 6.3, 6.5, 7.6, 4.9, 7.3, 6.7, 7.2]) # sem outliers, valor inferior é o extremo
        cls.z = np.array([6.3, 5.8, 7.1, 6.3, 6.5, 7.6, 4.9, 7.3, 6.7, 7.2, 12]) # valor superior outlier
        cls.w = np.array([6.3, 5.8, 7.1, 6.3, 6.5, 7.6, 4.9, 7.3, 6.7, 7.2, 2.5]) # valor inferior outlier



    def test_raise_critical(self):
        with self.assertRaises(ValueError, msg="Does not raised error when critical is negative"):
            teste = Tukey()
            teste.fit(self.x, critical=-1)

        with self.assertRaises(ValueError, msg="Does not raised error when critical not allowed key"):
            teste = Tukey()
            teste.fit(self.x, critical="name")



    def test_raise_which(self):
        with self.assertRaises(ValueError, msg="Does not raised error when which is not allowed"):
            teste = Tukey()
            teste.fit(self.x, which="m")



    def test_raise_details(self):
        with self.assertRaises(ValueError, msg="Does not raised error when details is not allowed"):
            teste = Tukey()
            teste.fit(self.x, details="full")



    def test_raise_details_output(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            teste = Tukey()
            teste.fit(self.x, details="full")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "full"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        ###############



    def test_raise_which_output(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            teste = Tukey()
            teste.fit(self.x, which="m")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'which' parameter only accepts 'min' or 'max' as keys, be we got 'm'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        ################



    def test_raise_critical_output(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            teste = Tukey()
            teste.fit(self.x, critical=-1)
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'critical' parameter must be higher than zero (positive), but we got '-1'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        ################

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            teste = Tukey()
            teste.fit(self.x, critical="name")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "name"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        ################



    def test_details(self):
        teste = Tukey()
        result, conclusion = teste.fit(self.x, details="short")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], list, msg="interval not a list")
        self.assertIsInstance(result[0][0], float, msg="lower interval not a float")
        self.assertIsInstance(result[0][1], float, msg="upper interval not a float")
        self.assertIsInstance(result[1], int, msg="critical not a int")
        self.assertIsInstance(result[2], float, msg="outlier not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0][0], 3.4, places=7, msg="wrong upper interval")
        self.assertAlmostEqual(result[0][1], 6.2, places=7, msg="wrong lower interval")
        self.assertEqual(result[1], 3, msg="wrong critical value")
        self.assertEqual(result[2], 5.4, msg="wrong outlier value")
        result = False
        if "The dataset has no outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Tukey()
        result, conclusion = teste.fit(self.x, details="binary")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], list, msg="interval not a list")
        self.assertIsInstance(result[0][0], float, msg="lower interval not a float")
        self.assertIsInstance(result[0][1], float, msg="upper interval not a float")
        self.assertIsInstance(result[1], int, msg="critical not a int")
        self.assertIsInstance(result[2], float, msg="outlier not a float")
        self.assertIsInstance(conclusion, int, msg="conclusion not a int")
        self.assertAlmostEqual(result[0][0], 3.4, places=7, msg="wrong upper interval")
        self.assertAlmostEqual(result[0][1], 6.2, places=7, msg="wrong lower interval")
        self.assertEqual(result[1], 3, msg="wrong critical value")
        self.assertEqual(result[2], 5.4, msg="wrong outlier value")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")


        teste = Tukey()
        result, conclusion = teste.fit(self.z, details="short")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], list, msg="interval not a list")
        self.assertIsInstance(result[0][0], float, msg="lower interval not a float")
        self.assertIsInstance(result[0][1], float, msg="upper interval not a float")
        self.assertIsInstance(result[1], int, msg="critical not a int")
        self.assertIsInstance(result[2], float, msg="outlier not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0][0], 3.45, places=7, msg="wrong upper interval")
        self.assertAlmostEqual(result[0][1], 10.1, places=7, msg="wrong lower interval")
        self.assertEqual(result[1], 3, msg="wrong critical value")
        self.assertEqual(result[2], 12, msg="wrong outlier value")
        result = False
        if "The dataset has outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Tukey()
        result, conclusion = teste.fit(self.z, details="binary")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], list, msg="interval not a list")
        self.assertIsInstance(result[0][0], float, msg="lower interval not a float")
        self.assertIsInstance(result[0][1], float, msg="upper interval not a float")
        self.assertIsInstance(result[1], int, msg="critical not a int")
        self.assertIsInstance(result[2], float, msg="outlier not a float")
        self.assertIsInstance(conclusion, int, msg="conclusion not a int")
        self.assertAlmostEqual(result[0][0], 3.45, places=7, msg="wrong upper interval")
        self.assertAlmostEqual(result[0][1], 10.1, places=7, msg="wrong lower interval")
        self.assertEqual(result[1], 3, msg="wrong critical value")
        self.assertEqual(result[2], 12, msg="wrong outlier value")
        self.assertEqual(conclusion, 1, msg="wrong conclusion")



    def test_critical(self):
        teste = Tukey()
        result, conclusion = teste.fit(self.x, critical=1)
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], list, msg="interval not a list")
        self.assertIsInstance(result[0][0], float, msg="lower interval not a float")
        self.assertIsInstance(result[0][1], float, msg="upper interval not a float")
        self.assertIsInstance(result[1], int, msg="critical not a int")
        self.assertIsInstance(result[2], float, msg="outlier not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0][0], 4.2, places=7, msg="wrong upper interval")
        self.assertAlmostEqual(result[0][1], 5.4, places=7, msg="wrong lower interval")
        self.assertEqual(result[1], 1, msg="wrong critical value")
        self.assertEqual(result[2], 5.4, msg="wrong outlier value")
        result = False
        if "The dataset has no outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Tukey()
        result, conclusion = teste.fit(self.x, critical=2)
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], list, msg="interval not a list")
        self.assertIsInstance(result[0][0], float, msg="lower interval not a float")
        self.assertIsInstance(result[0][1], float, msg="upper interval not a float")
        self.assertIsInstance(result[1], int, msg="critical not a int")
        self.assertIsInstance(result[2], float, msg="outlier not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0][0], 3.8, places=7, msg="wrong upper interval")
        self.assertAlmostEqual(result[0][1], 5.8, places=7, msg="wrong lower interval")
        self.assertEqual(result[1], 2, msg="wrong critical value")
        self.assertEqual(result[2], 5.4, msg="wrong outlier value")
        result = False
        if "The dataset has no outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Tukey()
        result, conclusion = teste.fit(self.x, critical='mild')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], list, msg="interval not a list")
        self.assertIsInstance(result[0][0], float, msg="lower interval not a float")
        self.assertIsInstance(result[0][1], float, msg="upper interval not a float")
        self.assertIsInstance(result[1], float, msg="critical not a float")
        self.assertIsInstance(result[2], float, msg="outlier not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0][0], 4.0, places=7, msg="wrong upper interval")
        self.assertAlmostEqual(result[0][1], 5.6, places=7, msg="wrong lower interval")
        self.assertEqual(result[1], 1.5, msg="wrong critical value")
        self.assertEqual(result[2], 5.4, msg="wrong outlier value")
        result = False
        if "The dataset has no outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")



    def test_which(self):
        teste = Tukey()
        result, conclusion = teste.fit(self.x, which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], list, msg="interval not a list")
        self.assertIsInstance(result[0][0], float, msg="lower interval not a float")
        self.assertIsInstance(result[0][1], float, msg="upper interval not a float")
        self.assertIsInstance(result[1], int, msg="critical not a int")
        self.assertIsInstance(result[2], float, msg="outlier not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0][0], 3.4, places=7, msg="wrong upper interval")
        self.assertAlmostEqual(result[0][1], 6.2, places=7, msg="wrong lower interval")
        self.assertEqual(result[1], 3, msg="wrong critical value")
        self.assertEqual(result[2], 5.4, msg="wrong outlier value")
        result = False
        if "The dataset has no outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Tukey()
        result, conclusion = teste.fit(self.x, which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], list, msg="interval not a list")
        self.assertIsInstance(result[0][0], float, msg="lower interval not a float")
        self.assertIsInstance(result[0][1], float, msg="upper interval not a float")
        self.assertIsInstance(result[1], int, msg="critical not a int")
        self.assertIsInstance(result[2], float, msg="outlier not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0][0], 3.4, places=7, msg="wrong upper interval")
        self.assertAlmostEqual(result[0][1], 6.2, places=7, msg="wrong lower interval")
        self.assertEqual(result[1], 3, msg="wrong critical value")
        self.assertEqual(result[2], 4.4, msg="wrong outlier value")
        result = False
        if "The dataset has no outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Tukey()
        result, conclusion = teste.fit(self.y, which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], list, msg="interval not a list")
        self.assertIsInstance(result[0][0], float, msg="lower interval not a float")
        self.assertIsInstance(result[0][1], float, msg="upper interval not a float")
        self.assertIsInstance(result[1], int, msg="critical not a int")
        self.assertIsInstance(result[2], float, msg="outlier not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0][0], 3.6, places=7, msg="wrong upper interval")
        self.assertAlmostEqual(result[0][1], 9.9, places=7, msg="wrong lower interval")
        self.assertEqual(result[1], 3, msg="wrong critical value")
        self.assertEqual(result[2], 7.6, msg="wrong outlier value")
        result = False
        if "The dataset has no outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Tukey()
        result, conclusion = teste.fit(self.y, which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], list, msg="interval not a list")
        self.assertIsInstance(result[0][0], float, msg="lower interval not a float")
        self.assertIsInstance(result[0][1], float, msg="upper interval not a float")
        self.assertIsInstance(result[1], int, msg="critical not a int")
        self.assertIsInstance(result[2], float, msg="outlier not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0][0], 3.6, places=7, msg="wrong upper interval")
        self.assertAlmostEqual(result[0][1], 9.9, places=7, msg="wrong lower interval")
        self.assertEqual(result[1], 3, msg="wrong critical value")
        self.assertEqual(result[2], 4.9, msg="wrong outlier value")
        result = False
        if "The dataset has no outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")




    def test_no_outlier_upper(self):
        teste = Tukey()
        result, conclusion = teste.fit(self.x)
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], list, msg="interval not a list")
        self.assertIsInstance(result[0][0], float, msg="lower interval not a float")
        self.assertIsInstance(result[0][1], float, msg="upper interval not a float")
        self.assertIsInstance(result[1], int, msg="critical not a int")
        self.assertIsInstance(result[2], float, msg="outlier not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0][0], 3.4, places=7, msg="wrong upper interval")
        self.assertAlmostEqual(result[0][1], 6.2, places=7, msg="wrong lower interval")
        self.assertEqual(result[1], 3, msg="wrong critical value")
        self.assertEqual(result[2], 5.4, msg="wrong outlier value")
        result = False
        if "The dataset has no outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Tukey(language='pt-br')
        result, conclusion = teste.fit(self.x)
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], list, msg="interval not a list")
        self.assertIsInstance(result[0][0], float, msg="lower interval not a float")
        self.assertIsInstance(result[0][1], float, msg="upper interval not a float")
        self.assertIsInstance(result[1], int, msg="critical not a int")
        self.assertIsInstance(result[2], float, msg="outlier not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0][0], 3.4, places=7, msg="wrong upper interval")
        self.assertAlmostEqual(result[0][1], 6.2, places=7, msg="wrong lower interval")
        self.assertEqual(result[1], 3, msg="wrong critical value")
        self.assertEqual(result[2], 5.4, msg="wrong outlier value")
        result = False
        if "O conjunto de dados não tem outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")



    def test_no_outlier_lower(self):
        teste = Tukey()
        result, conclusion = teste.fit(self.y)
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], list, msg="interval not a list")
        self.assertIsInstance(result[0][0], float, msg="lower interval not a float")
        self.assertIsInstance(result[0][1], float, msg="upper interval not a float")
        self.assertIsInstance(result[1], int, msg="critical not a int")
        self.assertIsInstance(result[2], float, msg="outlier not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0][0], 3.6, places=7, msg="wrong upper interval")
        self.assertAlmostEqual(result[0][1], 9.9, places=7, msg="wrong lower interval")
        self.assertEqual(result[1], 3, msg="wrong critical value")
        self.assertEqual(result[2], 4.9, msg="wrong outlier value")
        result = False
        if "The dataset has no outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Tukey(language='pt-br')
        result, conclusion = teste.fit(self.y)
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], list, msg="interval not a list")
        self.assertIsInstance(result[0][0], float, msg="lower interval not a float")
        self.assertIsInstance(result[0][1], float, msg="upper interval not a float")
        self.assertIsInstance(result[1], int, msg="critical not a int")
        self.assertIsInstance(result[2], float, msg="outlier not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0][0], 3.6, places=7, msg="wrong upper interval")
        self.assertAlmostEqual(result[0][1], 9.9, places=7, msg="wrong lower interval")
        self.assertEqual(result[1], 3, msg="wrong critical value")
        self.assertEqual(result[2], 4.9, msg="wrong outlier value")
        result = False
        if "O conjunto de dados não tem outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")



    def test_outlier_lower(self):
        teste = Tukey()
        result, conclusion = teste.fit(self.w)
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], list, msg="interval not a list")
        self.assertIsInstance(result[0][0], float, msg="lower interval not a float")
        self.assertIsInstance(result[0][1], float, msg="upper interval not a float")
        self.assertIsInstance(result[1], int, msg="critical not a int")
        self.assertIsInstance(result[2], float, msg="outlier not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0][0], 2.75, places=7, msg="wrong upper interval")
        self.assertAlmostEqual(result[0][1], 10.45, places=7, msg="wrong lower interval")
        self.assertEqual(result[1], 3, msg="wrong critical value")
        self.assertEqual(result[2], 2.5, msg="wrong outlier value")
        result = False
        if "The dataset has outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Tukey(language='pt-br')
        result, conclusion = teste.fit(self.w)
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], list, msg="interval not a list")
        self.assertIsInstance(result[0][0], float, msg="lower interval not a float")
        self.assertIsInstance(result[0][1], float, msg="upper interval not a float")
        self.assertIsInstance(result[1], int, msg="critical not a int")
        self.assertIsInstance(result[2], float, msg="outlier not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0][0], 2.75, places=7, msg="wrong upper interval")
        self.assertAlmostEqual(result[0][1], 10.45, places=7, msg="wrong lower interval")
        self.assertEqual(result[1], 3, msg="wrong critical value")
        self.assertEqual(result[2], 2.5, msg="wrong outlier value")
        result = False
        if "O conjunto de dados tem outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")



    def test_outlier_upper(self):
        teste = Tukey()
        result, conclusion = teste.fit(self.z)
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], list, msg="interval not a list")
        self.assertIsInstance(result[0][0], float, msg="lower interval not a float")
        self.assertIsInstance(result[0][1], float, msg="upper interval not a float")
        self.assertIsInstance(result[1], int, msg="critical not a int")
        self.assertIsInstance(result[2], float, msg="outlier not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0][0], 3.45, places=7, msg="wrong upper interval")
        self.assertAlmostEqual(result[0][1], 10.1, places=7, msg="wrong lower interval")
        self.assertEqual(result[1], 3, msg="wrong critical value")
        self.assertEqual(result[2], 12, msg="wrong outlier value")
        result = False
        if "The dataset has outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Tukey(language='pt-br')
        result, conclusion = teste.fit(self.z)
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], list, msg="interval not a list")
        self.assertIsInstance(result[0][0], float, msg="lower interval not a float")
        self.assertIsInstance(result[0][1], float, msg="upper interval not a float")
        self.assertIsInstance(result[1], int, msg="critical not a int")
        self.assertIsInstance(result[2], float, msg="outlier not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0][0], 3.45, places=7, msg="wrong upper interval")
        self.assertAlmostEqual(result[0][1], 10.1, places=7, msg="wrong lower interval")
        self.assertEqual(result[1], 3, msg="wrong critical value")
        self.assertEqual(result[2], 12, msg="wrong outlier value")
        result = False
        if "O conjunto de dados tem outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")




if __name__ == "__main__":
    unittest.main()
