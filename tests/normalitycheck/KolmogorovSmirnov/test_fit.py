"""Tests if the fit function for KolmogorovSmirnov is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_fit_ks
    This class tests the fit function. It should raise ValueError conclustion or detail got worng key. The function is tests against correct output, when data is Normal and when data is Not Normal.


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/normalitycheck/KolmogorovSmirnov/test_fit.py
    or
    python -m unittest -b tests/normalitycheck/KolmogorovSmirnov/test_fit.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.normalitycheck.kolmogorovsmirnov import KolmogorovSmirnov
import numpy as np
import sys
import io
os.system('cls')

class Test_fit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        cls.x_not_normal = np.array([1, 1, 1, 1, 1, 1, 1 ,1, 1.1, 1.2, 5.3, 10.1, 10.2, 10.3])


    def test_alfa_0_10(self):
        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x, alfa=0.10)
        self.assertAlmostEqual(resultado[0], 0.15459867079959644, msg="wrong statistic value")
        self.assertEqual(resultado[1], 0.368, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.9706128123504146, msg="wrong P-value value")
        self.assertEqual(resultado[3], 0.10, "wrong alfa value")
        if "Data is Normal at a 90.0% of confidence level" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Normal' not in conclusion when it should")


    def test_alfa_0_02(self):
        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x, alfa=0.02, comparison="p-value")
        self.assertAlmostEqual(resultado[0], 0.15459867079959644, msg="wrong statistic value")
        self.assertIsNone(resultado[1], "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.9706128123504146, msg="wrong P-value value")
        self.assertEqual(resultado[3], 0.02, "wrong alfa value")
        if "critical" in conclusao:
            result = False
        else:
            result = True
        self.assertTrue(result, "'critical' not in conclusion when it should")


    def test_alfa_0_25(self):
        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x, alfa=0.25, comparison="p-value")
        self.assertAlmostEqual(resultado[0], 0.15459867079959644, msg="wrong statistic value")
        self.assertIsNone(resultado[1], "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.9706128123504146, msg="wrong P-value value")
        self.assertEqual(resultado[3], 0.25, "wrong alfa value")
        if "critical" in conclusao:
            result = False
        else:
            result = True
        self.assertTrue(result, "'critical' not in conclusion when it should")


    def test_conclusion(self):
        with self.assertRaises(ValueError, msg="Does not raised error when comparison is not valid"):
            result = KolmogorovSmirnov()
            result.fit(self.x, comparison="any")

        with self.assertRaises(ValueError, msg="Does not raised error when comparison is not valid"):
            result = KolmogorovSmirnov()
            result.fit(self.x, comparison="tabulated")

        with self.assertRaises(ValueError, msg="Does not raised error when comparison is not valid"):
            result = KolmogorovSmirnov()
            result.fit(self.x, comparison="p_value")


    def test_conclusion_output(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = KolmogorovSmirnov()
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
            result = KolmogorovSmirnov()
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
            result = KolmogorovSmirnov()
            result.fit(self.x, comparison="p_value")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'conclusion' parameter only accepts 'critical' or 'p-value' as values, but we got 'p_value'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")


    def test_details(self):
        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = KolmogorovSmirnov()
            result.fit(self.x, details="binario")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = KolmogorovSmirnov()
            result.fit(self.x, details="shot")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = KolmogorovSmirnov()
            result.fit(self.x, details="ful")


    def test_details_output(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = KolmogorovSmirnov()
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
            result = KolmogorovSmirnov()
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
            result = KolmogorovSmirnov()
            result.fit(self.x, details="ful")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'details' parameter only accepts 'short', 'full' or 'binary' as values, but we got 'ful'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")


    def test_pass_normal(self):
        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x)
        self.assertAlmostEqual(resultado[0], 0.15459867079959644, msg="wrong statistic value")
        self.assertEqual(resultado[1], 0.41, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.9706128123504146, msg="wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Normal' not in conclusion when it should")


    def test_pass_normal_conclusion_p_value(self):
        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x, comparison="p-value")
        self.assertAlmostEqual(resultado[0], 0.15459867079959644, msg="wrong statistic value")
        self.assertEqual(resultado[1], 0.410, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.9706128123504146, msg="wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Normal' not in conclusion when it should")


    def test_pass_normal_details_full(self):
        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x, details="full")
        self.assertAlmostEqual(resultado[0], 0.15459867079959644, msg="wrong statistic value")
        self.assertEqual(resultado[1], 0.410, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.9706128123504146, msg="wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Since the critical value (0.41) >= statistic (0.154), we have NO evidence to reject the hypothesis of data normality, according to the Kolmogorov Smirnov test at a 95.0% of confidence level." in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'critical' not in conclusion when it should")


    def test_pass_normal_details_full_conclusion_p_value(self):
        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x, details="full", comparison="p-value")
        self.assertAlmostEqual(resultado[0], 0.15459867079959644, msg="wrong statistic value")
        self.assertEqual(resultado[1], 0.410, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.9706128123504146, msg="wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Since p-value (0.97) >= alpha (0.05), we have NO evidence to reject the hypothesis of data normality, according to the Kolmogorov Smirnov test at a 95.0% of confidence level." in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'p-value' not in conclusion when it should")


    def test_pass_normal_details_binary_p_value(self):
        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x, details="binary", comparison="p-value")
        self.assertAlmostEqual(resultado[0], 0.15459867079959644,msg= "wrong statistic value")
        self.assertEqual(resultado[1], 0.410, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.9706128123504146, msg="wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertIsInstance(conclusao, int, msg='conclusao not int when binary')
        self.assertEqual(conclusao, 0, msg="conclusion not 0 when binary and data not normal")


    def test_pass_normal_details_binary(self):
        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x, details="binary")
        self.assertAlmostEqual(resultado[0], 0.15459867079959644, msg="wrong statistic value")
        self.assertEqual(resultado[1], 0.410, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.9706128123504146, msg="wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertIsInstance(conclusao, int, msg='conclusao not int when binary')
        self.assertEqual(conclusao, 0, msg="conclusion not 0 when binary and data not normal")


    def test_pass_not_normal(self):
        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x_not_normal)
        self.assertAlmostEqual(resultado[0], 0.41883302450799276, msg="wrong statistic value")
        self.assertEqual(resultado[1], 0.349, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.009690080715050495, msg="wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Not Normal at a 95.0% of confidence level." in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Not Normal' not in conclusion when it should")


    def test_pass_not_normal_conclusion_p_value(self):
        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x_not_normal, comparison="p-value")
        self.assertAlmostEqual(resultado[0], 0.41883302450799276, msg="wrong statistic value")
        self.assertEqual(resultado[1], 0.349, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.009690080715050495, msg="wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Not Normal at a 95.0% of confidence level" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Not Normal' not in conclusion when it should")


    def test_pass_not_normal_details_full(self):
        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x_not_normal, details="full")
        self.assertAlmostEqual(resultado[0], 0.41883302450799276, msg="wrong statistic value")
        self.assertEqual(resultado[1], 0.349, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.009690080715050495, msg="wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Since the critical value (0.349) < statistic (0.418), we HAVE evidence to reject the hypothesis of data normality, according to the Kolmogorov Smirnov test at a 95.0% of confidence level" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'critical' not in conclusion when it should")


    def test_pass_not_normal_details_full_conclusion_p_value(self):
        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x_not_normal, details="full", comparison="p-value")
        self.assertAlmostEqual(resultado[0], 0.41883302450799276, msg="wrong statistic value")
        self.assertEqual(resultado[1], 0.349, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.009690080715050495, msg="wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Since p-value (0.009) < alpha (0.05), we HAVE evidence to reject the hypothesis of data normality, according to the Kolmogorov Smirnov test at a 95.0% of confidence level" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'p-value' not in conclusion when it should")


    def test_pass_not_normal_details_binary_p_value(self):
        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x_not_normal, details="binary", comparison="p-value")
        self.assertAlmostEqual(resultado[0], 0.41883302450799276, msg="wrong statistic value")
        self.assertEqual(resultado[1], 0.349, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.009690080715050495, msg="wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertIsInstance(conclusao, int, msg='conclusao not int when binary')
        self.assertEqual(conclusao, 1, msg="conclusion not 1 when binary and data not normal")


    def test_pass_not_normal_details_binary(self):
        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x_not_normal, details="binary")
        self.assertAlmostEqual(resultado[0], 0.41883302450799276, msg="wrong statistic value")
        self.assertEqual(resultado[1], 0.349, "wrong tabulated value")
        self.assertAlmostEqual(resultado[2], 0.009690080715050495, msg="wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertIsInstance(conclusao, int, msg='conclusao not int when binary')
        self.assertEqual(conclusao, 1, msg="conclusion not 1 when binary and data not normal")


    def test_conclusion_nor_normal(self):
        with self.assertRaises(ValueError, msg="Does not raised error when comparison is not valid"):
            result = KolmogorovSmirnov()
            result.fit(self.x_not_normal, comparison="any")

        with self.assertRaises(ValueError, msg="Does not raised error when comparison is not valid"):
            result = KolmogorovSmirnov()
            result.fit(self.x, comparison="tabulated")

        with self.assertRaises(ValueError, msg="Does not raised error when comparison is not valid"):
            result = KolmogorovSmirnov()
            result.fit(self.x, comparison="p_value")


    def test_conclusion_output_not_normal(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = KolmogorovSmirnov()
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
            result = KolmogorovSmirnov()
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
            result = KolmogorovSmirnov()
            result.fit(self.x_not_normal, comparison="p_value")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'conclusion' parameter only accepts 'critical' or 'p-value' as values, but we got 'p_value'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")


    def test_details_not_normal(self):
        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = KolmogorovSmirnov()
            result.fit(self.x_not_normal, details="binario")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = KolmogorovSmirnov()
            result.fit(self.x_not_normal, details="shot")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = KolmogorovSmirnov()
            result.fit(self.x_not_normal, details="ful")


    def test_details_output_not_normal(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = KolmogorovSmirnov()
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
            result = KolmogorovSmirnov()
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
            result = KolmogorovSmirnov()
            result.fit(self.x_not_normal, details="ful")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'details' parameter only accepts 'short', 'full' or 'binary' as values, but we got 'ful'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")


    def test_binary(self):
        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x_not_normal, details="binary")
        result_2 = KolmogorovSmirnov()
        resultado_2, conclusao_2 = result_2.fit(self.x_not_normal, details="binary", comparison='p-value')
        self.assertEqual(conclusao_2, conclusao, msg="binary conclusion not equal when changing the comparison method")


        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x, details="binary")
        result_2 = KolmogorovSmirnov()
        resultado_2, conclusao_2 = result_2.fit(self.x, details="binary", comparison='p-value')
        self.assertEqual(conclusao_2, conclusao, msg="binary conclusion not equal when changing the comparison method")


        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x_not_normal, details="binary")
        result_2 = KolmogorovSmirnov()
        resultado_2, conclusao_2 = result_2.fit(self.x, details="binary")
        teste = False
        if conclusao_2 == conclusao:
            teste = True
        self.assertFalse(teste, msg="binary conclusion leading to errors")

        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x_not_normal, details="binary", comparison='p-value')
        result_2 = KolmogorovSmirnov()
        resultado_2, conclusao_2 = result_2.fit(self.x, details="binary", comparison='p-value')
        teste = False
        if conclusao_2 == conclusao:
            teste = True
        self.assertFalse(teste, msg="binary conclusion leading to errors")



# I become so numb, I can't feel you there, become so tired... https://youtu.be/Tj9gy8uAPNE?t=154


if __name__ == "__main__":
    unittest.main()
