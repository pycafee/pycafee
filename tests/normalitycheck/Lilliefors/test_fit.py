"""Tests if the fit function for Lilliefors is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_fit
    This class tests the fit function. It should raise ValueError conclustion or detail got worng key. The function is tests against correct output, when data is Normal and when data is Not Normal.


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/normalitycheck/Lilliefors/test_fit.py
    or
    python -m unittest -b tests/normalitycheck/Lilliefors/test_fit.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.normalitycheck.lilliefors import Lilliefors
import numpy as np
import sys
import io
os.system('cls')

class Test_fit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        cls.x_not_normal = np.array([1, 1, 1, 1.1, 1.2, 5.3, 10.1, 10.2, 10.3])

    def test_alfa_0_05(self):
        result = Lilliefors()
        resultado, conclusao = result.fit(self.x)
        self.assertAlmostEqual(resultado[0], 0.15459867079959644, "wrong statistic value")
        self.assertEqual(resultado[1], 0.258, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.7104644322958894, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertEqual(conclusao, "Data is Normal at a 95.0% of confidence level.", msg='wrong conclusion')


    def test_alfa_0_10(self):
        result = Lilliefors()
        resultado, conclusao = result.fit(self.x, alfa=0.10)
        self.assertAlmostEqual(resultado[0], 0.15459867079959644, "wrong statistic value")
        self.assertEqual(resultado[1], 0.239, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.7104644322958894, "wrong P-value value")
        self.assertEqual(resultado[3], 0.10, "wrong alfa value")
        self.assertEqual(conclusao, "Data is Normal at a 90.0% of confidence level.", msg='wrong conclusion')


    def test_alfa_0_12(self):
        with self.assertRaises(ValueError, msg="Does not raised error when alfa=0.12 with default paramters"):
            result = Lilliefors()
            resultado, conclusao = result.fit(self.x, alfa=0.12)

        with self.assertRaises(ValueError, msg="Does not raised error when alfa=0.12 with conclusion='critical'"):
            result = Lilliefors()
            resultado, conclusao = result.fit(self.x, alfa=0.12, comparison="critical")

        with self.assertRaises(ValueError, msg="Does not raised error when alfa=0.12"):
            result = Lilliefors()
            resultado, conclusao = result.fit(self.x, alfa=0.12)


    def test_alfa_0_12_output(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = Lilliefors()
            resultado, conclusao = result.fit(self.x, alfa=0.12)
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The critical value for alpha '0.12' is not available. The available alpha values are:"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        ################

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = Lilliefors()
            resultado, conclusao = result.fit(self.x, alfa=0.12, comparison="critical")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The critical value for alpha '0.12' is not available. The available alpha values are:"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        ################

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = Lilliefors()
            resultado, conclusao = result.fit(self.x, alfa=0.12)
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The critical value for alpha '0.12' is not available. The available alpha values are:"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        ################


    def test_comparison(self):
        with self.assertRaises(ValueError, msg="Does not raised error when conclusion is not valid"):
            result = Lilliefors()
            result.fit(self.x, comparison="any")

        with self.assertRaises(ValueError, msg="Does not raised error when conclusion is not valid"):
            result = Lilliefors()
            result.fit(self.x, comparison="tabulated")

        with self.assertRaises(ValueError, msg="Does not raised error when conclusion is not valid"):
            result = Lilliefors()
            result.fit(self.x, comparison="p_value")


    def test_comparison_output(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = Lilliefors()
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
            result = Lilliefors()
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
            result = Lilliefors()
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
            result = Lilliefors()
            result.fit(self.x, details="binario")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = Lilliefors()
            result.fit(self.x, details="shot")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = Lilliefors()
            result.fit(self.x, details="ful")


    def test_details_output(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = Lilliefors()
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
            result = Lilliefors()
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
            result = Lilliefors()
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


    def test_pass_normal_conclusion_p_value(self):
        result = Lilliefors()
        resultado, conclusao = result.fit(self.x, comparison="p-value")
        self.assertAlmostEqual(resultado[0], 0.15459867079959644, "wrong statistic value")
        self.assertEqual(resultado[1], 0.258, "wrong critical value")
        self.assertAlmostEqual(resultado[2], 0.7104644322958894, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertEqual(conclusao, "Data is Normal at a 95.0% of confidence level.", msg='wrong conclusion')


    def test_pass_normal_details_full(self):
        result = Lilliefors()
        resultado, conclusao = result.fit(self.x, details="full")
        self.assertAlmostEqual(resultado[0], 0.15459867079959644, "wrong statistic value")
        self.assertEqual(resultado[1], 0.258, "wrong critical value")
        self.assertAlmostEqual(resultado[2], 0.7104644322958894, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertEqual(conclusao, "Since the critical value (0.258) >= statistic (0.154), we have NO evidence to reject the hypothesis of data normality, according to the Lilliefors test at a 95.0% of confidence level.", msg='wrong conclusion')


    def test_pass_normal_details_full_conclusion_p_value(self):
        result = Lilliefors()
        resultado, conclusao = result.fit(self.x, details="full", comparison="p-value")
        self.assertAlmostEqual(resultado[0], 0.15459867079959644, "wrong statistic value")
        self.assertEqual(resultado[1], 0.258, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.7104644322958894, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertEqual(conclusao, "Since p-value (0.71) >= alpha (0.05), we have NO evidence to reject the hypothesis of data normality, according to the Lilliefors test at a 95.0% of confidence level.", msg='wrong conclusion')


    def test_pass_normal_details_binary_p_value(self):
        result = Lilliefors()
        resultado, conclusao = result.fit(self.x, details="binary", comparison="p-value")
        self.assertAlmostEqual(resultado[0], 0.15459867079959644, "wrong statistic value")
        self.assertEqual(resultado[1], 0.258, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.7104644322958894, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertIsInstance(conclusao, int, msg='conclusao not int when binary')
        self.assertEqual(conclusao, 0, msg="conclusion not 0 when binary and data not normal")


    def test_pass_normal_details_binary(self):
        result = Lilliefors()
        resultado, conclusao = result.fit(self.x, details="binary")
        self.assertAlmostEqual(resultado[0], 0.15459867079959644, "wrong statistic value")
        self.assertEqual(resultado[1], 0.258, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.7104644322958894, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertIsInstance(conclusao, int, msg='conclusao not int when binary')
        self.assertEqual(conclusao, 0, msg="conclusion not 0 when binary and data not normal")


    def test_alfa_0_05_not_normal(self):
        result = Lilliefors()
        resultado, conclusao = result.fit(self.x_not_normal)
        self.assertAlmostEqual(resultado[0], 0.33246821361586026, "wrong statistic value")
        self.assertEqual(resultado[1], 0.271, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.005203341800231138, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertEqual(conclusao, "Data is Not Normal at a 95.0% of confidence level.", msg='wrong conclusion')


    def test_alfa_0_10_not_normal(self):
        result = Lilliefors()
        resultado, conclusao = result.fit(self.x_not_normal, alfa=0.10)
        self.assertAlmostEqual(resultado[0], 0.33246821361586026, "wrong statistic value")
        self.assertEqual(resultado[1], 0.249, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.005203341800231138, "wrong P-value value")
        self.assertEqual(resultado[3], 0.10, "wrong alfa value")
        self.assertEqual(conclusao, "Data is Not Normal at a 90.0% of confidence level.", msg='wrong conclusion')


    def test_alfa_0_12_not_normal(self):
        with self.assertRaises(ValueError, msg="Does not raised error when alfa=0.12 with default parameters, not normal data"):
            result = Lilliefors()
            resultado, conclusao = result.fit(self.x_not_normal, alfa=0.12)

        with self.assertRaises(ValueError, msg="Does not raised error when alfa=0.12 with conclusion='tabulate', not normal data"):
            result = Lilliefors()
            resultado, conclusao = result.fit(self.x_not_normal, alfa=0.12, comparison="critical")


    def test_alfa_0_12_output_not_normal(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = Lilliefors()
            resultado, conclusao = result.fit(self.x_not_normal, alfa=0.12)
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The critical value for alpha '0.12' is not available. The available alpha values are:"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        ################

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = Lilliefors()
            resultado, conclusao = result.fit(self.x_not_normal, alfa=0.12, comparison="critical")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The critical value for alpha '0.12' is not available. The available alpha values are:"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")


    def test_conclusion_not_normal(self):
        with self.assertRaises(ValueError, msg="Does not raised error when conclusion is not valid, not normal"):
            result = Lilliefors()
            result.fit(self.x_not_normal, comparison="any")

        with self.assertRaises(ValueError, msg="Does not raised error when conclusion is not valid, not normal"):
            result = Lilliefors()
            result.fit(self.x_not_normal, comparison="tabulated")

        with self.assertRaises(ValueError, msg="Does not raised error when conclusion is not valid, not normal"):
            result = Lilliefors()
            result.fit(self.x_not_normal, comparison="p_value")


    def test_conclusion_output_not_normal(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = Lilliefors()
            result.fit(self.x_not_normal, comparison="any")
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
            result = Lilliefors()
            result.fit(self.x_not_normal, comparison="tabulated")
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
            result = Lilliefors()
            result.fit(self.x_not_normal, comparison="p_value")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'conclusion' parameter only accepts 'critical' or 'p-value' as values, but we got 'p_value'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        ################


    def test_details_not_normal(self):
        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid, not normal"):
            result = Lilliefors()
            result.fit(self.x_not_normal, details="binario")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid, not normal"):
            result = Lilliefors()
            result.fit(self.x_not_normal, details="shot")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid, not normal"):
            result = Lilliefors()
            result.fit(self.x_not_normal, details="ful")


    def test_details_output(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = Lilliefors()
            result.fit(self.x_not_normal, details="binario")
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
            result = Lilliefors()
            result.fit(self.x_not_normal, details="shot")
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
            result = Lilliefors()
            result.fit(self.x_not_normal, details="ful")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'details' parameter only accepts 'short', 'full' or 'binary' as values, but we got 'ful'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        ################


    def test_pass_normal_conclusion_p_value_not_normal(self):
        result = Lilliefors()
        resultado, conclusao = result.fit(self.x_not_normal, comparison="p-value")
        self.assertAlmostEqual(resultado[0], 0.33246821361586026, "wrong statistic value")
        self.assertEqual(resultado[1], 0.271, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.005203341800231138, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertEqual(conclusao, "Data is Not Normal at a 95.0% of confidence level.", msg='wrong conclusion')


    def test_pass_normal_details_full_not_normal(self):
        result = Lilliefors()
        resultado, conclusao = result.fit(self.x_not_normal, details="full")
        self.assertAlmostEqual(resultado[0], 0.33246821361586026, "wrong statistic value")
        self.assertEqual(resultado[1], 0.271, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.005203341800231138, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertEqual(conclusao, "Since the critical value (0.271) < statistic (0.332), we HAVE evidence to reject the hypothesis of data normality, according to the Lilliefors test at a 95.0% of confidence level.", msg='wrong conclusion')


    def test_pass_normal_details_full_conclusion_p_value_not_normal(self):
        result = Lilliefors()
        resultado, conclusao = result.fit(self.x_not_normal, details="full", comparison="p-value")
        self.assertAlmostEqual(resultado[0], 0.33246821361586026, "wrong statistic value")
        self.assertEqual(resultado[1], 0.271, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.005203341800231138, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertEqual(conclusao, "Since p-value (0.005) < alpha (0.05), we HAVE evidence to reject the hypothesis of data normality, according to the Lilliefors test at a 95.0% of confidence level.", msg='wrong conclusion')


    def test_pass_not_normal_details_binary_p_value(self):
        result = Lilliefors()
        resultado, conclusao = result.fit(self.x_not_normal, details="binary", comparison="p-value")
        self.assertAlmostEqual(resultado[0], 0.33246821361586026, "wrong statistic value")
        self.assertEqual(resultado[1], 0.271, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.005203341800231138, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertIsInstance(conclusao, int, msg='conclusao not int when binary')
        self.assertEqual(conclusao, 1, msg="conclusion not 1 when binary and data not normal")


    def test_pass_not_normal_details_binary(self):
        result = Lilliefors()
        resultado, conclusao = result.fit(self.x_not_normal, details="binary")
        self.assertAlmostEqual(resultado[0], 0.33246821361586026, "wrong statistic value")
        self.assertEqual(resultado[1], 0.271, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.005203341800231138, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertIsInstance(conclusao, int, msg='conclusao not int when binary')
        self.assertEqual(conclusao, 1, msg="conclusion not 1 when binary and data not normal")


    def test_binary(self):
        result = Lilliefors()
        resultado, conclusao = result.fit(self.x_not_normal, details="binary")
        result_2 = Lilliefors()
        resultado_2, conclusao_2 = result_2.fit(self.x_not_normal, details="binary", comparison='p-value')
        self.assertEqual(conclusao_2, conclusao, msg="binary conclusion not equal when changing the comparison method")


        result = Lilliefors()
        resultado, conclusao = result.fit(self.x, details="binary")
        result_2 = Lilliefors()
        resultado_2, conclusao_2 = result_2.fit(self.x, details="binary", comparison='p-value')
        self.assertEqual(conclusao_2, conclusao, msg="binary conclusion not equal when changing the comparison method")


        result = Lilliefors()
        resultado, conclusao = result.fit(self.x_not_normal, details="binary")
        result_2 = Lilliefors()
        resultado_2, conclusao_2 = result_2.fit(self.x, details="binary")
        teste = False
        if conclusao_2 == conclusao:
            teste = True
        self.assertFalse(teste, msg="binary conclusion leading to errors")

        result = Lilliefors()
        resultado, conclusao = result.fit(self.x_not_normal, details="binary", comparison='p-value')
        result_2 = Lilliefors()
        resultado_2, conclusao_2 = result_2.fit(self.x, details="binary", comparison='p-value')
        teste = False
        if conclusao_2 == conclusao:
            teste = True
        self.assertFalse(teste, msg="binary conclusion leading to errors")



# and now i understand the problems, you can see https://youtu.be/N26_hRITlsU?t=51

if __name__ == "__main__":
    unittest.main()
