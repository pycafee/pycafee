"""Tests if the fit function for TriangleTest is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_fit
    This class tests the fit function. Falta clocar exemplos da literatura e variar o parâmetro details


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sensoryanalysis/discriminative_tests/TriangleTest/test_fit.py
    or
    python -m unittest -b tests/sensoryanalysis/discriminative_tests/TriangleTest/test_fit.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sensoryanalysis.discriminative_tests import TriangleTest
import numpy as np
import sys
import io
os.system('cls')

class Test_fit(unittest.TestCase):



    def test_raises(self):

        with self.assertRaises(ValueError, msg="Does not raised error impossible values"):
            result = TriangleTest()
            result.fit(-10, 10)

        with self.assertRaises(ValueError, msg="Does not raised error impossible values"):
            result = TriangleTest()
            result.fit(10, -10)

        with self.assertRaises(ValueError, msg="Does not raised error impossible values"):
            result = TriangleTest()
            result.fit(11, 10)

        with self.assertRaises(ValueError, msg="Does not raised error impossible values"):
            result = TriangleTest()
            result.fit(5, 10, alfa=0.12)

        with self.assertRaises(ValueError, msg="Does not raised error impossible values"):
            result = TriangleTest()
            result.fit(5, 10, details="0.12")


    def test_raises_output(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = TriangleTest()
            result.fit(-10, 10)
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "f_correct_answers' parameter must be higher than zero (positive), but we got '-10'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        ###############

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = TriangleTest()
            result.fit(10, -10)
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = " 'total_of_answers' parameter must be higher than zero (positive), but we got '-10'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        ###############

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = TriangleTest()
            result.fit(11, 10)
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "of answers (total_of_answers) must be greater than or equal to the number of correct answers (n_of_correct_an"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        ################

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = TriangleTest()
            result.fit(5, 10, alfa=0.12)
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = " --->    0.12"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        ################

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = TriangleTest()
            result.fit(5, 10, details="0.12")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = " --->    '0.12'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        ################


    def test_outputs_type(self):
        teste = TriangleTest()
        result, conclusion = teste.fit(10, 50)

        self.assertEqual(len(result), 6, msg="wrong size of the outputs")
        self.assertIsInstance(result[0], float, msg="wrong not float type")
        self.assertIsInstance(result[1], float, msg="wrong not float type")
        self.assertIsInstance(result[2], float, msg="wrong not float type")
        self.assertIsInstance(result[3], float, msg="wrong not float type")
        self.assertIsInstance(result[4], tuple, msg="wrong not tuple type")
        self.assertIsInstance(result[4][0], float, msg="wrong not float type")
        self.assertIsInstance(result[4][1], float, msg="wrong not float type")
        self.assertIsInstance(result[5], float, msg="wrong not float type")
        self.assertIsInstance(conclusion, str, msg="wrong not str type")


        teste = TriangleTest()
        result, conclusion = teste.fit(10, 50, details='binary')

        self.assertEqual(len(result), 6, msg="wrong size of the outputs")
        self.assertIsInstance(result[0], float, msg="wrong not float type")
        self.assertIsInstance(result[1], float, msg="wrong not float type")
        self.assertIsInstance(result[2], float, msg="wrong not float type")
        self.assertIsInstance(result[3], float, msg="wrong not float type")
        self.assertIsInstance(result[4], tuple, msg="wrong not tuple type")
        self.assertIsInstance(result[4][0], float, msg="wrong not float type")
        self.assertIsInstance(result[4][1], float, msg="wrong not float type")
        self.assertIsInstance(result[5], float, msg="wrong not float type")
        self.assertIsInstance(conclusion, int, msg="wrong not int type")


    def test_astm(self):
        teste = TriangleTest()
        result, conclusion = teste.fit(18, 45, alfa=0.1)
        self.assertEqual(conclusion, "Samples are equal (with 90.0% confidence).", msg="wrong conclusion")
        self.assertAlmostEqual(result[0], 0.10, msg="wrong proportion_distinguishers")
        self.assertAlmostEqual(result[1], 0.40, msg="wrong proportion_correct")
        self.assertAlmostEqual(result[2], 0.11, places=3, msg="wrong sd_proportion_distinguishers")
        self.assertAlmostEqual(result[3], 0.1408, places=3, msg="wrong ic_proportion_distinguishers")
        self.assertAlmostEqual(result[4][0], -0.04, places=3, msg="wrong lower_limit")
        self.assertAlmostEqual(result[4][1], 0.24, places=3, msg="wrong upper_limit")
        self.assertAlmostEqual(result[5], 1.28, places=2, msg="wrong critical_z")


        teste = TriangleTest()
        result, conclusion = teste.fit(18, 45, alfa=0.1, details="full")
        self.assertEqual(conclusion, "As the proportion of discriminators (0.1) is between the lower (-0.04) and upper limits (0.24), we have no evidence to reject the null hypothesis of equality between the samples (with 90.0% confidence).", msg="wrong conclusion")
        self.assertAlmostEqual(result[0], 0.10, msg="wrong proportion_distinguishers")
        self.assertAlmostEqual(result[1], 0.40, msg="wrong proportion_correct")
        self.assertAlmostEqual(result[2], 0.11, places=3, msg="wrong sd_proportion_distinguishers")
        self.assertAlmostEqual(result[3], 0.1408, places=3, msg="wrong ic_proportion_distinguishers")
        self.assertAlmostEqual(result[4][0], -0.04, places=3, msg="wrong lower_limit")
        self.assertAlmostEqual(result[4][1], 0.24, places=3, msg="wrong upper_limit")
        self.assertAlmostEqual(result[5], 1.28, places=2, msg="wrong critical_z")


        teste = TriangleTest()
        result, conclusion = teste.fit(18, 45, alfa=0.1, details="binary")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")
        self.assertAlmostEqual(result[0], 0.10, msg="wrong proportion_distinguishers")
        self.assertAlmostEqual(result[1], 0.40, msg="wrong proportion_correct")
        self.assertAlmostEqual(result[2], 0.11, places=3, msg="wrong sd_proportion_distinguishers")
        self.assertAlmostEqual(result[3], 0.1408, places=3, msg="wrong ic_proportion_distinguishers")
        self.assertAlmostEqual(result[4][0], -0.04, places=3, msg="wrong lower_limit")
        self.assertAlmostEqual(result[4][1], 0.24, places=3, msg="wrong upper_limit")
        self.assertAlmostEqual(result[5], 1.28, places=2, msg="wrong critical_z")






# and now i understand the problems, you can see https://youtu.be/N26_hRITlsU?t=51

if __name__ == "__main__":
    unittest.main()
