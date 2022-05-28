"""Tests if the test_compare_with_constant is working as expected

---> Class Test_two_side
    This class test if the all the outputs for a two-side test. The results are checked when the constant is distinct when compare to a mean, with values closer to the mean and far from the mean (but rejecting the H0). The tests checks language as well.

---> Class Test_one_side_higher
    This class test if the all the outputs for a one-side test when is a upper test. The results are checked when the constant is distinct when compare to a mean, with values closer to the mean and far from the mean (but rejecting the H0). The tests checks language as well.

---> Class Test_one_side_lower
    This class test if the all the outputs for a one-side test when is a lower test. The results are checked when the constant is distinct when compare to a mean, with values closer to the mean and far from the mean (but rejecting the H0). The tests checks language as well.

---> Class Test_raises_error
    This class test when the method should raise ValueError. The output is also tested.

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sample/StudentDistribution/test_compare_with_constant.py
    or
    python -m unittest -b tests/sample/StudentDistribution/test_compare_with_constant.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sample.studentdistribution import StudentDistribution
import numpy as np
from unittest.mock import patch
import io
import sys
os.system('cls')


class Test_raises_error(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([3380, 3500, 3600, 3450, 3490, 3390])

        cls.value_equal_lower = 3450
        cls.value_lower = 3360
        cls.value_very_lower = 2800


    def test_comparison(self):
        with self.assertRaises(ValueError, msg="Does not raised error when comparison is wrong"):
            student = StudentDistribution()
            result, conclusion = student.compare_with_constant(self.x, self.value_lower, comparison='pvalue')

        with self.assertRaises(ValueError, msg="Does not raised error when comparison is wrong"):
            student = StudentDistribution()
            result, conclusion = student.compare_with_constant(self.x, self.value_lower, comparison='None')

        with self.assertRaises(ValueError, msg="Does not raised error when comparison is wrong"):
            student = StudentDistribution()
            result, conclusion = student.compare_with_constant(self.x, self.value_lower, comparison='critico')

        with self.assertRaises(ValueError, msg="Does not raised error when comparison is wrong"):
            student = StudentDistribution()
            result, conclusion = student.compare_with_constant(self.x, self.value_lower, comparison='p-valor')


    def test_comparison_output(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            student = StudentDistribution()
            result, conclusion = student.compare_with_constant(self.x, self.value_lower, comparison='pvalue')
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'comparison' parameter only accepts the keys 'critical' or 'p-value', but we got: 'pvalue'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")


        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            student = StudentDistribution()
            result, conclusion = student.compare_with_constant(self.x, self.value_lower, comparison='None')
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'comparison' parameter only accepts the keys 'critical' or 'p-value', but we got: 'None'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")


        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            student = StudentDistribution()
            result, conclusion = student.compare_with_constant(self.x, self.value_lower, comparison='critico')
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'comparison' parameter only accepts the keys 'critical' or 'p-value', but we got: 'critico'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")


        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            student = StudentDistribution()
            result, conclusion = student.compare_with_constant(self.x, self.value_lower, comparison='p-valor')
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'comparison' parameter only accepts the keys 'critical' or 'p-value', but we got: 'p-valor'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")


    def test_details(self):
        with self.assertRaises(ValueError, msg="Does not raised error when details is wrong"):
            student = StudentDistribution()
            result, conclusion = student.compare_with_constant(self.x, self.value_lower, details='shot')

        with self.assertRaises(ValueError, msg="Does not raised error when details is wrong"):
            student = StudentDistribution()
            result, conclusion = student.compare_with_constant(self.x, self.value_lower, details='ful')

        with self.assertRaises(ValueError, msg="Does not raised error when details is wrong"):
            student = StudentDistribution()
            result, conclusion = student.compare_with_constant(self.x, self.value_lower, details='binario')


    def test_details_output(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            student = StudentDistribution()
            result, conclusion = student.compare_with_constant(self.x, self.value_lower, details='shot')
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'details' parameter only accepts the keys 'short', 'full' or 'binary', but we got: 'shot'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")


        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            student = StudentDistribution()
            result, conclusion = student.compare_with_constant(self.x, self.value_lower, details='ful')
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'details' parameter only accepts the keys 'short', 'full' or 'binary', but we got: 'ful'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")


        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            student = StudentDistribution()
            result, conclusion = student.compare_with_constant(self.x, self.value_lower, details='binario')
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'details' parameter only accepts the keys 'short', 'full' or 'binary', but we got: 'binario'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")




class Test_one_side_lower(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([3380, 3500, 3600, 3450, 3490, 3390])

        cls.value_equal_lower = 3450
        cls.value_lower = 3360
        cls.value_very_lower = 2800

    def test_samples_distinct_default(self):
        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_lower, which="one-side")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 3.262256486, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.01504837333, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.01504837333, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.011194819117, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")

        result = False
        if "The mean (3468.333) is higher than the constant (3360) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="lower not in conclusion when it should")


        student = StudentDistribution('pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_lower, which="one-side")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 3.262256486, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.01504837333, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.01504837333, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.011194819117, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "A média (3468.333) é maior do que a constante (3360) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="menor not in conclusion when it should")


        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_very_lower, which="one-side")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 20.125613090, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.01504837333, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.01504837333, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.000002799679, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "The mean (3468.333) is higher than the constant (2800) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="lower not in conclusion when it should")


        student = StudentDistribution('pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_very_lower, which="one-side")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 20.125613090, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.01504837333, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.01504837333, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.000002799679, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "A média (3468.333) é maior do que a constante (2800) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="menor not in conclusion when it should")


    def test_samples_distinct_full(self):
        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_lower, which="one-side", details="full")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 3.262256486, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.01504837333, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.01504837333, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.011194819117, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "Since the test statistic (3.262) is higher than the upper critical value (2.015), we have evidence to reject the null hypothesis of equality of means, and we can say that the mean (3468.333) is higher than the constant (3360) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="higher not in conclusion when it should")


        student = StudentDistribution('pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_lower, which="one-side", details="full")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 3.262256486, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.01504837333, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.01504837333, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.011194819117, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "Como a estatística do teste (3.262) é maior do que o valor crítico superior (2.015) temos evidências para rejeitar a hipótese nula de igualdade das médias, e podemos dizer que a média (3468.333) é maior do que a constante (3360) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="superior not in conclusion when it should")


        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_very_lower, which="one-side", details="full")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 20.125613090, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.01504837333, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.01504837333, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.000002799679, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "Since the test statistic (20.125) is higher than the upper critical value (2.015), we have evidence to reject the null hypothesis of equality of means, and we can say that the mean (3468.333) is higher than the constant (2800) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="reject not in conclusion when it should")


        student = StudentDistribution('pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_very_lower, which="one-side", details="full")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 20.125613090, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.01504837333, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.01504837333, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.000002799679, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "Como a estatística do teste (20.125) é maior do que o valor crítico superior (2.015) temos evidências para rejeitar a hipótese nula de igualdade das médias, e podemos dizer que a média (3468.333) é maior do que a constante (2800) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="rejeitar not in conclusion when it should")


    def test_samples_distinct_full_p_value(self):
        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_lower, which="one-side", details="full", comparison='p-value')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 3.262256486, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.01504837333, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.01504837333, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.011194819117, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "Since the p-value (0.011) is lower than the adopted significance level (0.05), we have evidence to reject the null hypothesis of equality of means, and we can say that the mean (3468.333) is higher than the constant (3360) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="significance not in conclusion when it should")


        student = StudentDistribution('pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_lower, which="one-side", details="full", comparison='p-value')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 3.262256486, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.01504837333, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.01504837333, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.011194819117, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "Como o p-valor (0.011) é menor do que o nível de significância adotado (0.05), temos evidências para rejeitar a hipótese nula de igualdade das médias, e podemos dizer que a média (3468.333) é maior do que a constante (3360) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="significância not in conclusion when it should")



        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_very_lower, which="one-side", details="full", comparison='p-value')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 20.125613090, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.01504837333, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.01504837333, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.000002799679, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "Since the p-value (0.0) is lower than the adopted significance level (0.05), we have evidence to reject the null hypothesis of equality of means, and we can say that the mean (3468.333) is higher than the constant (2800) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="p-value not in conclusion when it should")


        student = StudentDistribution('pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_very_lower, which="one-side", details="full", comparison='p-value')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 20.125613090, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.01504837333, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.01504837333, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.000002799679, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "Como o p-valor (0.0) é menor do que o nível de significância adotado (0.05), temos evidências para rejeitar a hipótese nula de igualdade das médias, e podemos dizer que a média (3468.333) é maior do que a constante (2800) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="p-valor not in conclusion when it should")



    def test_samples_distinct_p_value(self):
        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_lower, which="one-side", comparison='p-value')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 3.262256486, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.01504837333, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.01504837333, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.011194819117, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "The mean (3468.333) is higher than the constant (3360) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="lower not in conclusion when it should")


        student = StudentDistribution('pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_lower, which="one-side", comparison='p-value')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 3.262256486, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.01504837333, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.01504837333, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.011194819117, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "A média (3468.333) é maior do que a constante (3360) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="menor not in conclusion when it should")


        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_very_lower, which="one-side", comparison='p-value')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 20.125613090, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.01504837333, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.01504837333, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.000002799679, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "The mean (3468.333) is higher than the constant (2800) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="lower not in conclusion when it should")


        student = StudentDistribution('pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_very_lower, which="one-side", comparison='p-value')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 20.125613090, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.01504837333, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.01504837333, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.000002799679, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "A média (3468.333) é maior do que a constante (2800) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="menor not in conclusion when it should")


    def test_samples_equals_default(self):
        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_lower, which="one-side")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.552074175, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.01504837333, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.01504837333, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.302332651389, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "The mean (3468.333) is equal to the constant (3450) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="equals not in conclusion when it should")


        student = StudentDistribution('pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_lower, which="one-side")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.552074175, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.01504837333, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.01504837333, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.302332651389, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "A média (3468.333) é igual a constante (3450) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="iguais not in conclusion when it should")


    def test_samples_equals_full(self):
        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_lower, which="one-side", details="full")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.552074175, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.01504837333, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.01504837333, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.302332651389, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "Since the test statistic (0.552) is lower than the upper critical value (2.015), we have no evidence to reject the null hypothesis of equality between the means, and we can say that the mean (3468.333) is equal to the constant (3450) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="upper not in conclusion when it should")


        student = StudentDistribution('pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_lower, which="one-side", details="full")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.552074175, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.01504837333, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.01504837333, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.302332651389, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "Como a estatística do teste (0.552) é menor do que o valor crítico superior (2.015), não temos evidências para rejeitar a hipótese nula de igualdade entre a médias, e podemos dizer que a média (3468.333) é igual a constante (3450) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="superior not in conclusion when it should")


    def test_samples_equals_full_p_value(self):
        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_lower, which="one-side", details="full", comparison='p-value')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.552074175, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.01504837333, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.01504837333, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.302332651389, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "Since the p-value (0.302) is higher than the adopted significance level (0.05), we have no evidence to reject the null hypothesis of equality between the means, and we can say that the mean (3468.333) is equal to the constant (3450) (with 95.0% confidence)." in conclusion:
            result = True
        self.assertTrue(result, msg="significance not in conclusion when it should")


        student = StudentDistribution('pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_lower, which="one-side", details="full", comparison='p-value')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.552074175, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.01504837333, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.01504837333, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.302332651389, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "Como o p-valor (0.302) é maior do que o nível de signficância adotado (0.05), não temos evidências para rejeitar a hipótese nula de igualdade entre as médias, e podemos dizer que a média (3468.333) é igual a constante (3450) (com 95.0% de confiança)." in conclusion:
            result = True
        self.assertTrue(result, msg="não temos not in conclusion when it should")


    def test_samples_equals_p_value(self):
        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_lower, which="one-side", comparison='p-value')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.552074175, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.01504837333, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.01504837333, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.302332651389, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "The mean (3468.333) is equal to the constant (3450) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="equals not in conclusion when it should")


        student = StudentDistribution('pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_lower, which="one-side", comparison='p-value')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.552074175, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.01504837333, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.01504837333, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.302332651389, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "A média (3468.333) é igual a constante (3450) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="iguais not in conclusion when it should")


    def test_binary(self):

        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_lower, which="one-side", details="binary")
        self.assertIsInstance(conclusion, int, msg="conclusion not a int")
        self.assertEqual(conclusion, 0, msg="conclusion not 0 when H0 is accepted")

        result, conclusion = student.compare_with_constant(self.x, self.value_equal_lower, details="binary", which="one-side", comparison='p-value')
        self.assertIsInstance(conclusion, int, msg="conclusion not a int")
        self.assertEqual(conclusion, 0, msg="conclusion not 0 when H0 is accepted")

        result, conclusion = student.compare_with_constant(self.x, self.value_lower, which="one-side", details="binary")
        self.assertIsInstance(conclusion, int, msg="conclusion not a int")
        self.assertEqual(conclusion, 1, msg="conclusion not 1 when H0 is rejected")

        result, conclusion = student.compare_with_constant(self.x, self.value_lower, details="binary", which="one-side", comparison='p-value')
        self.assertIsInstance(conclusion, int, msg="conclusion not a int")
        self.assertEqual(conclusion, 1, msg="conclusion not 1 when H0 is rejected")

        result, conclusion = student.compare_with_constant(self.x, self.value_very_lower, which="one-side", details="binary")
        self.assertIsInstance(conclusion, int, msg="conclusion not a int")
        self.assertEqual(conclusion, 1, msg="conclusion not 1 when H0 is rejected")

        result, conclusion = student.compare_with_constant(self.x, self.value_very_lower, details="binary", which="one-side", comparison='p-value')
        self.assertIsInstance(conclusion, int, msg="conclusion not a int")
        self.assertEqual(conclusion, 1, msg="conclusion not 1 when H0 is rejected")




class Test_one_side_higher(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([0.144, 0.168, 0.137, 0.153, 0.152, 0.152, 0.148, 0.148, 0.14, 0.136])
        cls.value_equal_higher = 0.15
        cls.value_higher = 0.16
        cls.value_very_higher = 0.2

    def test_samples_distinct_default(self):
        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_higher, which="one-side")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -4.08791852222, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 1.8331129327, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -1.8331129327, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.00136275579, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "The mean (0.147) is lower than the constant (0.16) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="higher not in conclusion when it should")


        student = StudentDistribution('pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_higher, which="one-side")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -4.08791852222, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 1.8331129327, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -1.8331129327, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.00136275579, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "A média (0.147) é menor do que a constante (0.16) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="maior not in conclusion when it should")


        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_very_higher, which="one-side")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -17.49093007048, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 1.8331129327, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -1.8331129327, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.00000001476, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "The mean (0.147) is lower than the constant (0.2) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="higher not in conclusion when it should")


        student = StudentDistribution('pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_very_higher, which="one-side")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -17.49093007048, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 1.8331129327, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -1.8331129327, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.00000001476, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "A média (0.147) é menor do que a constante (0.2) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="maior not in conclusion when it should")


    def test_samples_distinct_full(self):
        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_higher, which="one-side", details="full")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -4.08791852222, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 1.8331129327, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -1.8331129327, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.00136275579, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False

        if "Since the test statistic (-4.087) is lower than the lower critical value (-1.833), we have evidence to reject the null hypothesis of equality of means, and we can say that the mean (0.147) is lower than the constant (0.16) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="lower not in conclusion when it should")


        student = StudentDistribution('pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_higher, which="one-side", details="full")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -4.08791852222, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 1.8331129327, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -1.8331129327, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.00136275579, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "Como a estatística do teste (-4.087) é menor do que o valor crítico inferior (-1.833), temos evidências para rejeitar a hipótese nula de igualdade das médias, e podemos dizer que a média (0.147) é menor do que a constante (0.16) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="menor not in conclusion when it should")


        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_very_higher, which="one-side", details="full")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -17.49093007048, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 1.8331129327, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -1.8331129327, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.00000001476, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "Since the test statistic (-17.49) is lower than the lower critical value (-1.833), we have evidence to reject the null hypothesis of equality of means, and we can say that the mean (0.147) is lower than the constant (0.2) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="reject not in conclusion when it should")


        student = StudentDistribution('pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_very_higher, which="one-side", details="full")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -17.49093007048, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 1.8331129327, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -1.8331129327, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.00000001476, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "Como a estatística do teste (-17.49) é menor do que o valor crítico inferior (-1.833), temos evidências para rejeitar a hipótese nula de igualdade das médias, e podemos dizer que a média (0.147) é menor do que a constante (0.2) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="rejeitar not in conclusion when it should")


    def test_samples_distinct_full_p_value(self):
        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_higher, which="one-side", details="full", comparison='p-value')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -4.08791852222, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 1.8331129327, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -1.8331129327, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.00136275579, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "Since the p-value (0.001) is lower than the adopted significance level (0.05), we have evidence to reject the null hypothesis of equality of means, and we can say that the mean (0.147) is lower than the constant (0.16) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="significance not in conclusion when it should")


        student = StudentDistribution('pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_higher, which="one-side", details="full", comparison='p-value')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -4.08791852222, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 1.8331129327, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -1.8331129327, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.00136275579, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "Como o p-valor (0.001) é menor do que o nível de significância adotado (0.05), temos evidências para rejeitar a hipótese nula de igualdade das médias, e podemos dizer que a média (0.147) é menor do que a constante (0.16) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="significância not in conclusion when it should")


        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_very_higher, which="one-side", details="full", comparison='p-value')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -17.49093007048, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 1.8331129327, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -1.8331129327, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.00000001476, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "Since the p-value (0.0) is lower than the adopted significance level (0.05), we have evidence to reject the null hypothesis of equality of means, and we can say that the mean (0.147) is lower than the constant (0.2) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="p-value not in conclusion when it should")


        student = StudentDistribution('pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_very_higher, which="one-side", details="full", comparison='p-value')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -17.49093007048, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 1.8331129327, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -1.8331129327, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.00000001476, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "Como o p-valor (0.0) é menor do que o nível de significância adotado (0.05), temos evidências para rejeitar a hipótese nula de igualdade das médias, e podemos dizer que a média (0.147) é menor do que a constante (0.2) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="p-valor not in conclusion when it should")


    def test_samples_distinct_p_value(self):
        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_higher, which="one-side", comparison='p-value')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -4.08791852222, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 1.8331129327, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -1.8331129327, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.00136275579, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "The mean (0.147) is lower than the constant (0.16) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="higher not in conclusion when it should")


        student = StudentDistribution('pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_higher, which="one-side", comparison='p-value')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -4.08791852222, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 1.8331129327, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -1.8331129327, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.00136275579, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "A média (0.147) é menor do que a constante (0.16) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="maior not in conclusion when it should")


        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_very_higher, which="one-side", comparison='p-value')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -17.49093007048, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 1.8331129327, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -1.8331129327, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.00000001476, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "The mean (0.147) is lower than the constant (0.2) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="higher not in conclusion when it should")


        student = StudentDistribution('pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_very_higher, which="one-side", comparison='p-value')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -17.49093007048, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 1.8331129327, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -1.8331129327, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.00000001476, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "A média (0.147) é menor do que a constante (0.2) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="maior not in conclusion when it should")


    def test_samples_equals_default(self):
        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_higher, which="one-side")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -0.7371656352, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 1.8331129327, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -1.8331129327, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.2398986055, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "The mean (0.147) is equal to the constant (0.15) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="equals not in conclusion when it should")


        student = StudentDistribution('pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_higher, which="one-side")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -0.7371656352, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 1.8331129327, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -1.8331129327, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.2398986055, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "A média (0.147) é igual a constante (0.15) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="iguais not in conclusion when it should")


    def test_samples_equals_full(self):
        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_higher, which="one-side", details="full")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -0.7371656352, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 1.8331129327, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -1.8331129327, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.2398986055, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "Since the test statistic (-0.737) is higher than the lower critical value (-1.833), we have no evidence to reject the null hypothesis of equality between the means, and we can say that the mean (0.147) is equal to the constant (0.15) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="lower not in conclusion when it should")


        student = StudentDistribution('pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_higher, which="one-side", details="full")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -0.7371656352, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 1.8331129327, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -1.8331129327, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.2398986055, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "Como a estatística do teste (-0.737) é maior do que o valor crítico inferior (-1.833), não temos evidências para rejeitar a hipótese nula de igualdade entre a médias, e podemos dizer que a média (0.147) é igual a constante (0.15) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="inferior not in conclusion when it should")


    def test_samples_equals_full_p_value(self):
        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_higher, which="one-side", details="full", comparison='p-value')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -0.7371656352, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 1.8331129327, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -1.8331129327, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.2398986055, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "Since the p-value (0.239) is higher than the adopted significance level (0.05), we have no evidence to reject the null hypothesis of equality between the means, and we can say that the mean (0.147) is equal to the constant (0.15) (with 95.0% confidence)." in conclusion:
            result = True
        self.assertTrue(result, msg="significance not in conclusion when it should")


        student = StudentDistribution('pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_higher, which="one-side", details="full", comparison='p-value')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -0.7371656352, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 1.8331129327, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -1.8331129327, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.2398986055, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "Como o p-valor (0.239) é maior do que o nível de signficância adotado (0.05), não temos evidências para rejeitar a hipótese nula de igualdade entre as médias, e podemos dizer que a média (0.147) é igual a constante (0.15) (com 95.0% de confiança)." in conclusion:
            result = True
        self.assertTrue(result, msg="não temos not in conclusion when it should")


    def test_samples_equals_p_value(self):
        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_higher, which="one-side", comparison='p-value')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -0.7371656352, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 1.8331129327, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -1.8331129327, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.2398986055, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")

        result = False
        if "The mean (0.147) is equal to the constant (0.15) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="equals not in conclusion when it should")


        student = StudentDistribution('pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_higher, which="one-side", comparison='p-value')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -0.7371656352, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 1.8331129327, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -1.8331129327, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.2398986055, msg="wrong p-value")
        self.assertEqual(result[3], "one-side", msg="wrong which")
        result = False
        if "A média (0.147) é igual a constante (0.15) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="iguais not in conclusion when it should")


    def test_binary(self):

        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_higher, which="one-side", details="binary")
        self.assertIsInstance(conclusion, int, msg="conclusion not a int")
        self.assertEqual(conclusion, 0, msg="conclusion not 0 when H0 is accepted")

        result, conclusion = student.compare_with_constant(self.x, self.value_equal_higher, details="binary", which="one-side", comparison='p-value')
        self.assertIsInstance(conclusion, int, msg="conclusion not a int")
        self.assertEqual(conclusion, 0, msg="conclusion not 0 when H0 is accepted")

        result, conclusion = student.compare_with_constant(self.x, self.value_higher, which="one-side", details="binary")
        self.assertIsInstance(conclusion, int, msg="conclusion not a int")
        self.assertEqual(conclusion, 1, msg="conclusion not 1 when H0 is rejected")

        result, conclusion = student.compare_with_constant(self.x, self.value_higher, details="binary", which="one-side", comparison='p-value')
        self.assertIsInstance(conclusion, int, msg="conclusion not a int")
        self.assertEqual(conclusion, 1, msg="conclusion not 1 when H0 is rejected")

        result, conclusion = student.compare_with_constant(self.x, self.value_very_higher, which="one-side", details="binary")
        self.assertIsInstance(conclusion, int, msg="conclusion not a int")
        self.assertEqual(conclusion, 1, msg="conclusion not 1 when H0 is rejected")

        result, conclusion = student.compare_with_constant(self.x, self.value_very_higher, details="binary", which="one-side", comparison='p-value')
        self.assertIsInstance(conclusion, int, msg="conclusion not a int")
        self.assertEqual(conclusion, 1, msg="conclusion not 1 when H0 is rejected")




class Test_two_side(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([3.335, 3.328, 3.288, 3.198, 3.254])
        cls.value = 3.2
        cls.value_very_lower = 1
        cls.value_higher = 3.4
        cls.value_very_higher = 7
        cls.value_equal_higher = 3.3
        cls.value_equal_lower = 3.25

    def test_samples_distinct_default(self):
        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value)
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 3.187090493341, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.033308661401, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "The mean (3.28) is different from the constant (3.2) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="distinct not in conclusion when it should")

        student = StudentDistribution(language='pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_very_lower)
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 90.179634976602, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.000000090649, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "A média (3.28) é diferente da constante (1) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="diferente not in conclusion when it should")

        student = StudentDistribution(language='pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_higher)
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -4.721322641501, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.009162621724, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "A média (3.28) é diferente da constante (3.4) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="diferente not in conclusion when it should")

        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_very_higher)
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -147.072759068654, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.000000012820, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "The mean (3.28) is different from the constant (7) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="distinct not in conclusion when it should")


    def test_samples_distinct_full(self):
        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value, details="full")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 3.187090493341, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.033308661401, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "Since the test statistic (3.187) is higher than the upper critical value (2.776), we have evidence to reject the null hypothesis of equality of means, and we can say that the mean (3.28) is different from the constant (3.2) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="reject not in conclusion when it should")


        student = StudentDistribution(language='pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_very_lower, details="full")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 90.179634976602, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.000000090649, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "Como a estatística do teste (90.179) é maior do que o valor crítico superior (2.776) temos evidências para rejeitar a hipótese nula de igualdade das médias, e podemos dizer que a média (3.28) é diferente da constante (1) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="rejeitar not in conclusion when it should")


        student = StudentDistribution(language='pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_higher, details="full")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -4.721322641501, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.009162621724, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "Como a estatística do teste (-4.721) é menor do que o valor crítico inferior (-2.776) temos evidências para rejeitar a hipótese nula de igualdade das médias, e podemos dizer que a média (3.28) é diferente da constante (3.4) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="rejeitar not in conclusion when it should")


        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_very_higher, details="full")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -147.072759068654, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.000000012820, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "Since the test statistic (-147.072) is lower than the lower critical value (-2.776),  we have evidence to reject the null hypothesis of equality of means, and we can say that the mean (3.28) is different from constant (7) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="reject not in conclusion when it should")


    def test_samples_distinct_full_p_value(self):
        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value, details="full", comparison="p-value")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 3.187090493341, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.033308661401, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "Since the p-value (0.033) is lower than the adopted significance level (0.05), we have evidence to reject the null hypothesis of equality of means, and we can say that the mean (3.28) is different from the constant (3.2) (with 95.0% confidence)." in conclusion:
            result = True
        self.assertTrue(result, msg="p-value not in conclusion when it should")


        student = StudentDistribution(language='pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_very_lower, details="full", comparison="p-value")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 90.179634976602, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.000000090649, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "Como o p-valor (0.0) é menor do que o nível de significância adotado (0.05),  temos evidências para rejeitar a hipótese nula de igualdade das médias, e podemos dizer que a média (3.28) é diferente da constante (1) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="p-valor not in conclusion when it should")


        student = StudentDistribution(language='pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_higher, details="full", comparison="p-value")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -4.721322641501, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.009162621724, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "Como o p-valor (0.009) é menor do que o nível de significância adotado (0.05),  temos evidências para rejeitar a hipótese nula de igualdade das médias, e podemos dizer que a média (3.28) é diferente da constante (3.4) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="p-valor not in conclusion when it should")


        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_very_higher, details="full", comparison="p-value")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -147.072759068654, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.000000012820, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "Since the p-value (0.0) is lower than the adopted significance level (0.05), we have evidence to reject the null hypothesis of equality of means, and we can say that the mean (3.28) is different from the constant (7) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="p-value not in conclusion when it should")


    def test_samples_distinct_p_value(self):
        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value, comparison="p-value")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 3.187090493341, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.033308661401, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "The mean (3.28) is different from the constant (3.2) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="different not in conclusion when it should")


        student = StudentDistribution(language='pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_very_lower, comparison="p-value")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 90.179634976602, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.000000090649, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "A média (3.28) é diferente da constante (1) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="diferente not in conclusion when it should")


        student = StudentDistribution(language='pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_higher, comparison="p-value")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -4.721322641501, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.009162621724, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "A média (3.28) é diferente da constante (3.4) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="diferente not in conclusion when it should")


        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_very_higher, comparison="p-value")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -147.072759068654, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.000000012820, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "The mean (3.28) is different from the constant (7) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="different not in conclusion when it should")


    def test_samples_equal_default(self):
        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_higher)
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -0.767116074080, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.485785837691, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "The mean (3.28) is equal to the constant (3.3) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="equals not in conclusion when it should")


        student = StudentDistribution(language='pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_higher)
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -0.767116074080, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.485785837691, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "A média (3.28) é igual a constante (3.3) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="iguais not in conclusion when it should")


        student = StudentDistribution(language='pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_lower)
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 1.209987209631, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.292897846789, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "A média (3.28) é igual a constante (3.25) (com 95.0% de confiança)." in conclusion:
            result = True
        self.assertTrue(result, msg="iguais not in conclusion when it should")


        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_lower)
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 1.209987209631, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.292897846789, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "The mean (3.28) is equal to the constant (3.25) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="equals not in conclusion when it should")


    def test_samples_equals_full(self):
        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_higher, details="full")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -0.767116074080, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.485785837691, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "Since the test statistic (-0.767) is a number between the critical values (-2.776, 2.776), there is no evidence to reject the null hypothesis, and we can say that the mean (3.28) is equal to the constant (3.3) (with 95.0% confidence)." in conclusion:
            result = True
        self.assertTrue(result, msg="no evidence not in conclusion when it should")


        student = StudentDistribution(language='pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_higher, details="full")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -0.767116074080, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.485785837691, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "Como a estatística do teste (-0.767) é um número entre os valores críticos (-2.776, 2.776) não existem evidências para rejeitar a hipótese nula, e podemos dizer que a média (3.28) é igual a constante (3.3) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="não existem evidências not in conclusion when it should")

        student = StudentDistribution(language='pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_lower, details="full")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 1.209987209631, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.292897846789, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "Como a estatística do teste (1.209) é um número entre os valores críticos (-2.776, 2.776) não existem evidências para rejeitar a hipótese nula, e podemos dizer que a média (3.28) é igual a constante (3.25) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="não existem evidências not in conclusion when it should")


        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_lower, details="full")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 1.209987209631, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.292897846789, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "Since the test statistic (1.209) is a number between the critical values (-2.776, 2.776), there is no evidence to reject the null hypothesis, and we can say that the mean (3.28) is equal to the constant (3.25) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="no evidence not in conclusion when it should")


    def test_samples_equals_full_p_value(self):
        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_higher, details="full", comparison="p-value")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -0.767116074080, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.485785837691, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "Since the p-value (0.485) is higher than the adopted significance level (0.05), we do not have evidence to reject the hypothesis of equality between the means, and we can say that the mean (3.28) is equal to the constant (3.3) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="p-value not in conclusion when it should")


        student = StudentDistribution(language='pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_higher, details="full", comparison="p-value")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -0.767116074080, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.485785837691, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "Como o p-valor (0.485) é maior do que o nível de significância adotado (0.05), nós não temos evidências para rejeitar a hipótese nula de igualdade entre a médias, e podemos dizer que a média (3.28) é igual a constante (3.3) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="p-valor not in conclusion when it should")


        student = StudentDistribution(language='pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_lower, details="full", comparison="p-value")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 1.209987209631, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.292897846789, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "Como o p-valor (0.292) é maior do que o nível de significância adotado (0.05), nós não temos evidências para rejeitar a hipótese nula de igualdade entre a médias, e podemos dizer que a média (3.28) é igual a constante (3.25) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="p-valor not in conclusion when it should")


        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_lower, details="full", comparison="p-value")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 1.209987209631, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.292897846789, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "Since the p-value (0.292) is higher than the adopted significance level (0.05), we do not have evidence to reject the hypothesis of equality between the means, and we can say that the mean (3.28) is equal to the constant (3.25) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="p-value not in conclusion when it should")


    def test_samples_equals_p_value(self):
        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_higher, comparison="p-value")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -0.767116074080, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.485785837691, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "The mean (3.28) is equal to the constant (3.3) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="equals not in conclusion when it should")


        student = StudentDistribution(language='pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_higher, comparison="p-value")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -0.767116074080, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.485785837691, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "A média (3.28) é igual a constante (3.3) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="iguais not in conclusion when it should")


        student = StudentDistribution(language='pt-br')
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_lower, comparison="p-value")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 1.209987209631, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.292897846789, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "A média (3.28) é igual a constante (3.25) (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="iguais not in conclusion when it should")


        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_lower, comparison="p-value")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="p-value not float")
        self.assertIsInstance(result[3], str, msg="which not str")
        self.assertIsInstance(result[4], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 1.209987209631, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], 2.77644510520, msg="wrong upper")
        self.assertAlmostEqual(result[1][1], -2.77644510520, msg="wrong lower")
        self.assertAlmostEqual(result[2], 0.292897846789, msg="wrong p-value")
        self.assertEqual(result[3], "two-side", msg="wrong which")
        result = False
        if "The mean (3.28) is equal to the constant (3.25) (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="equals not in conclusion when it should")


    def test_binary(self):

        student = StudentDistribution()
        result, conclusion = student.compare_with_constant(self.x, self.value_equal_higher, details="binary")
        self.assertIsInstance(conclusion, int, msg="conclusion not a int")
        self.assertEqual(conclusion, 0, msg="conclusion not 0 when H0 is accepted")

        result, conclusion = student.compare_with_constant(self.x, self.value_equal_lower, details="binary")
        self.assertIsInstance(conclusion, int, msg="conclusion not a int")
        self.assertEqual(conclusion, 0, msg="conclusion not 0 when H0 is accepted")

        result, conclusion = student.compare_with_constant(self.x, self.value_equal_higher, details="binary", comparison="p-value")
        self.assertIsInstance(conclusion, int, msg="conclusion not a int")
        self.assertEqual(conclusion, 0, msg="conclusion not 0 when H0 is accepted")

        result, conclusion = student.compare_with_constant(self.x, self.value_equal_lower, details="binary", comparison="p-value")
        self.assertIsInstance(conclusion, int, msg="conclusion not a int")
        self.assertEqual(conclusion, 0, msg="conclusion not 0 when H0 is accepted")

        result, conclusion = student.compare_with_constant(self.x, self.value, details="binary")
        self.assertIsInstance(conclusion, int, msg="conclusion not a int")
        self.assertEqual(conclusion, 1, msg="conclusion not 1 when H0 is accepted")

        result, conclusion = student.compare_with_constant(self.x, self.value, details="binary", comparison='p-value')
        self.assertIsInstance(conclusion, int, msg="conclusion not a int")
        self.assertEqual(conclusion, 1, msg="conclusion not 1 when H0 is accepted")

        result, conclusion = student.compare_with_constant(self.x, self.value_very_lower, details="binary")
        self.assertIsInstance(conclusion, int, msg="conclusion not a int")
        self.assertEqual(conclusion, 1, msg="conclusion not 1 when H0 is accepted")

        result, conclusion = student.compare_with_constant(self.x, self.value_very_lower, details="binary", comparison='p-value')
        self.assertIsInstance(conclusion, int, msg="conclusion not a int")
        self.assertEqual(conclusion, 1, msg="conclusion not 1 when H0 is accepted")

        result, conclusion = student.compare_with_constant(self.x, self.value_higher, details="binary")
        self.assertIsInstance(conclusion, int, msg="conclusion not a int")
        self.assertEqual(conclusion, 1, msg="conclusion not 1 when H0 is accepted")

        result, conclusion = student.compare_with_constant(self.x, self.value_higher, details="binary", comparison='p-value')
        self.assertIsInstance(conclusion, int, msg="conclusion not a int")
        self.assertEqual(conclusion, 1, msg="conclusion not 1 when H0 is accepted")

        result, conclusion = student.compare_with_constant(self.x, self.value_very_higher, details="binary")
        self.assertIsInstance(conclusion, int, msg="conclusion not a int")
        self.assertEqual(conclusion, 1, msg="conclusion not 1 when H0 is accepted")

        result, conclusion = student.compare_with_constant(self.x, self.value_very_higher, details="binary", comparison='p-value')
        self.assertIsInstance(conclusion, int, msg="conclusion not a int")
        self.assertEqual(conclusion, 1, msg="conclusion not 1 when H0 is accepted")






if __name__ == "__main__":
    unittest.main()
