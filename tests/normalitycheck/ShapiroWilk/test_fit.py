"""Tests if the fit function for Shapiro Wilk is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_fit
    This class tests the fit function. It should raise ValueError conclustion or detail got worng key. The function is tests against correct output, when data is Normal and when data is Not Normal.


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/normalitycheck/ShapiroWilk/test_fit.py
    or
    python -m unittest -b tests/normalitycheck/ShapiroWilk/test_fit.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.normalitycheck.shapirowilk import ShapiroWilk
import numpy as np
import sys
import io
os.system('cls')

class Test_fit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        cls.x_not_normal = np.array([1, 1, 1, 1.1, 1.2, 5.3, 10.1, 10.2, 10.3])

    def test_comparison(self):
        with self.assertRaises(ValueError, msg="Does not raised error when conclusion is not valid"):
            result = ShapiroWilk()
            result.fit(self.x, comparison="any")

        with self.assertRaises(ValueError, msg="Does not raised error when conclusion is not valid"):
            result = ShapiroWilk()
            result.fit(self.x, comparison="tabulated")

        with self.assertRaises(ValueError, msg="Does not raised error when conclusion is not valid"):
            result = ShapiroWilk()
            result.fit(self.x, comparison="p_value")


    def test_comparison_output(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = ShapiroWilk()
            result.fit(self.x, comparison="any")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'conclusion' parameter only accepts 'critical' or 'p-value' as values, but we got 'any'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        ################

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = ShapiroWilk()
            result.fit(self.x, comparison="tabulated")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'conclusion' parameter only accepts 'critical' or 'p-value' as values, but we got 'tabulated'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        ################

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = ShapiroWilk()
            result.fit(self.x, comparison="p_value")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'conclusion' parameter only accepts 'critical' or 'p-value' as values, but we got 'p_value'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        ################


    def test_details(self):
        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = ShapiroWilk()
            result.fit(self.x, details="binario")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = ShapiroWilk()
            result.fit(self.x, details="shot")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = ShapiroWilk()
            result.fit(self.x, details="ful")


    def test_details_output(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = ShapiroWilk()
            result.fit(self.x, details="binario")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'details' parameter only accepts 'short', 'full' or 'binary' as values, but we got 'binario'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        ################

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = ShapiroWilk()
            result.fit(self.x, details="shot")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'details' parameter only accepts 'short', 'full' or 'binary' as values, but we got 'shot'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        ################

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = ShapiroWilk()
            result.fit(self.x, details="ful")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'details' parameter only accepts 'short', 'full' or 'binary' as values, but we got 'ful'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        ################


    def test_pass_normal(self):
        result = ShapiroWilk()
        resultado, conclusao = result.fit(self.x)
        self.assertAlmostEqual(resultado[0], 0.9698116779327393, "wrong statistic value")
        self.assertEqual(resultado[1], 0.842, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.8890941739082336, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertEqual(conclusao, "Data is Normal at a 95.0% of confidence level.", msg='wrong conclusion')


    def test_pass_normal_conclusion_p_value(self):
        result = ShapiroWilk()
        resultado, conclusao = result.fit(self.x, comparison="p-value")
        self.assertAlmostEqual(resultado[0], 0.9698116779327393, "wrong statistic value")
        self.assertEqual(resultado[1], 0.842, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.8890941739082336, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertEqual(conclusao, "Data is Normal at a 95.0% of confidence level.", msg='wrong conclusion')


    def test_pass_normal_details_full(self):
        result = ShapiroWilk()
        resultado, conclusao = result.fit(self.x, details="full")
        self.assertAlmostEqual(resultado[0], 0.9698116779327393, "wrong statistic value")
        self.assertEqual(resultado[1], 0.842, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.8890941739082336, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertEqual(conclusao, "Since the critical value (0.842) >= statistic (0.969), we have NO evidence to reject the hypothesis of data normality, according to the Shapiro Wilk test at a 95.0% of confidence level.", msg='wrong conclusion')


    def test_pass_normal_details_full_conclusion_p_value(self):
        result = ShapiroWilk()
        resultado, conclusao = result.fit(self.x, details="full", comparison="p-value")
        self.assertAlmostEqual(resultado[0], 0.9698116779327393, "wrong statistic value")
        self.assertEqual(resultado[1], 0.842, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.8890941739082336, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        print(conclusao)
        self.assertEqual(conclusao, "Since p-value (0.889) >= alpha (0.05), we have NO evidence to reject the hypothesis of data normality, according to the Shapiro Wilk test at a 95.0% of confidence level.", msg='wrong conclusion')


    def test_pass_normal_details_binary_p_value(self):
        result = ShapiroWilk()
        resultado, conclusao = result.fit(self.x, details="binary", comparison="p-value")
        self.assertAlmostEqual(resultado[0], 0.9698116779327393, "wrong statistic value")
        self.assertEqual(resultado[1], 0.842, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.8890941739082336, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertIsInstance(conclusao, int, msg='conclusao not int when binary')
        self.assertEqual(conclusao, 0, msg="conclusion not 0 when binary and data not normal")


    def test_pass_normal_details_binary(self):
        result = ShapiroWilk()
        resultado, conclusao = result.fit(self.x, details="binary")
        self.assertAlmostEqual(resultado[0], 0.9698116779327393, "wrong statistic value")
        self.assertEqual(resultado[1], 0.842, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.8890941739082336, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertIsInstance(conclusao, int, msg='conclusao not int when binary')
        self.assertEqual(conclusao, 0, msg="conclusion not 0 when binary and data not normal")


    def test_pass_not_normal(self):
        result = ShapiroWilk()
        resultado, conclusao = result.fit(self.x_not_normal)
        self.assertAlmostEqual(resultado[0], 0.7226213812828064, "wrong statistic value")
        self.assertEqual(resultado[1], 0.829, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.0026055360212922096, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertEqual(conclusao, "Data is Not Normal at a 95.0% of confidence level.", msg='wrong conclusion')


    def test_pass_not_normal_conclusion_p_value(self):
        result = ShapiroWilk()
        resultado, conclusao = result.fit(self.x_not_normal, comparison="p-value")
        self.assertAlmostEqual(resultado[0], 0.7226213812828064, "wrong statistic value")
        self.assertEqual(resultado[1], 0.829, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.0026055360212922096, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertEqual(conclusao, "Data is Not Normal at a 95.0% of confidence level.", msg='wrong conclusion')


    def test_pass_not_normal_details_full(self):
        result = ShapiroWilk()
        resultado, conclusao = result.fit(self.x_not_normal, details="full")
        self.assertAlmostEqual(resultado[0], 0.7226213812828064, "wrong statistic value")
        self.assertEqual(resultado[1], 0.829, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.0026055360212922096, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertEqual(conclusao, "Since the critical value (0.829) < statistic (0.722), we HAVE evidence to reject the hypothesis of data normality, according to the Shapiro Wilk test at a 95.0% of confidence level.", msg='wrong conclusion')

    
    def test_pass_not_normal_details_full_conclusion_p_value(self):
        result = ShapiroWilk()
        resultado, conclusao = result.fit(self.x_not_normal, details="full", comparison="p-value")
        self.assertAlmostEqual(resultado[0], 0.7226213812828064, "wrong statistic value")
        self.assertEqual(resultado[1], 0.829, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.0026055360212922096, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertEqual(conclusao, "Since p-value (0.002) < alpha (0.05), we HAVE evidence to reject the hypothesis of data normality, according to the Shapiro Wilk test at a 95.0% of confidence level.", msg='wrong conclusion')


    def test_pass_not_normal_details_binary_p_value(self):
        result = ShapiroWilk()
        resultado, conclusao = result.fit(self.x_not_normal, details="binary", comparison="p-value")
        self.assertAlmostEqual(resultado[0], 0.7226213812828064, "wrong statistic value")
        self.assertEqual(resultado[1], 0.829, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.0026055360212922096, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertIsInstance(conclusao, int, msg='conclusao not int when binary')
        self.assertEqual(conclusao, 1, msg="conclusion not 1 when binary and data not normal")


    def test_pass_not_normal_details_binary(self):
        result = ShapiroWilk()
        resultado, conclusao = result.fit(self.x_not_normal, details="binary")
        self.assertAlmostEqual(resultado[0], 0.7226213812828064, "wrong statistic value")
        self.assertEqual(resultado[1], 0.829, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.0026055360212922096, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertIsInstance(conclusao, int, msg='conclusao not int when binary')
        self.assertEqual(conclusao, 1, msg="conclusion not 1 when binary and data not normal")


    def test_binary(self):
        result = ShapiroWilk()
        resultado, conclusao = result.fit(self.x_not_normal, details="binary")
        result_2 = ShapiroWilk()
        resultado_2, conclusao_2 = result_2.fit(self.x_not_normal, details="binary", comparison='p-value')
        self.assertEqual(conclusao_2, conclusao, msg="binary conclusion not equal when changing the comparison method")


        result = ShapiroWilk()
        resultado, conclusao = result.fit(self.x, details="binary")
        result_2 = ShapiroWilk()
        resultado_2, conclusao_2 = result_2.fit(self.x, details="binary", comparison='p-value')
        self.assertEqual(conclusao_2, conclusao, msg="binary conclusion not equal when changing the comparison method")


        result = ShapiroWilk()
        resultado, conclusao = result.fit(self.x_not_normal, details="binary")
        result_2 = ShapiroWilk()
        resultado_2, conclusao_2 = result_2.fit(self.x, details="binary")
        teste = False
        if conclusao_2 == conclusao:
            teste = True
        self.assertFalse(teste, msg="binary conclusion leading to errors")

        result = ShapiroWilk()
        resultado, conclusao = result.fit(self.x_not_normal, details="binary", comparison='p-value')
        result_2 = ShapiroWilk()
        resultado_2, conclusao_2 = result_2.fit(self.x, details="binary", comparison='p-value')
        teste = False
        if conclusao_2 == conclusao:
            teste = True
        self.assertFalse(teste, msg="binary conclusion leading to errors")



# and now i understand the problems, you can see https://youtu.be/N26_hRITlsU?t=51

if __name__ == "__main__":
    unittest.main()
