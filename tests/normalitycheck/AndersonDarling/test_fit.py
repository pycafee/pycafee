"""Tests if the fit function for AndersonDarling is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_fit
    This class tests the fit function. It should raise ValueError conclustion or detail got worng key. The function is tests against correct output, when data is Normal and when data is Not Normal.


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/normalitycheck/AndersonDarling/test_fit.py
    or
    python -m unittest -b tests/normalitycheck/AndersonDarling/test_fit.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.normalitycheck.andersondarling import AndersonDarling
import numpy as np
import io
import  sys
os.system('cls')

class Test_fit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        cls.x_not_normal = np.array([1, 1, 1, 1.1, 1.2, 5.3, 10.1, 10.2, 10.3])

    def test_statistic_between_methods(self):
        result = AndersonDarling()
        statistic_scipy, _ = result.fit(self.x, comparison="critical")
        statistic_statsmodels, _ = result.fit(self.x, comparison="p-value")
        self.assertEqual(statistic_scipy[0], statistic_statsmodels[0], msg="The statistic value does not match between fit methods")

        result = AndersonDarling()
        statistic_scipy, _ = result.fit(self.x_not_normal, comparison="critical")
        statistic_statsmodels, _ = result.fit(self.x_not_normal, comparison="p-value")
        self.assertEqual(statistic_scipy[0], statistic_statsmodels[0], msg="The statistic value does not match between fit methods")


    def test_alfa_0_05(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x)
        self.assertAlmostEqual(resultado[0], 0.22687861079050364, "wrong statistic value")
        self.assertEqual(resultado[1], 0.684, "wrong tabulated value")
        self.assertIsNone(resultado[2], msg="p-value not none")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Normal' not in comparison when it should")


    def test_alfa_0_05_n_full_digits(self):
        result = AndersonDarling(n_digits=4)
        resultado, conclusao = result.fit(self.x, details='full')
        self.assertAlmostEqual(resultado[0], 0.22687861079050364, "wrong statistic value")
        self.assertEqual(resultado[1], 0.684, "wrong tabulated value")
        self.assertIsNone(resultado[2], msg="p-value not none")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "(0.2268)" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'(0.2268)' not in comparison when it should")


    def test_alfa_0_10(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x, alfa=0.10)
        self.assertAlmostEqual(resultado[0], 0.22687861079050364, "wrong statistic value")
        self.assertEqual(resultado[1], 0.57, "wrong tabulated value")
        self.assertIsNone(resultado[2], msg="p-value not none")
        self.assertEqual(resultado[3], 0.10, "wrong alfa value")
        if "Data is Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Normal' not in conclusion when it should")


    def test_alfa_0_12(self):
        with self.assertRaises(ValueError, msg="Does not raised error when alfa=0.12"):
            result = AndersonDarling()
            resultado, conclusao = result.fit(self.x, alfa=0.12)


    def test_details_raise_output_not_normal_0_12(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = AndersonDarling()
            resultado, conclusao = result.fit(self.x_not, alfa=0.12)
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The critical value for alpha '0.12' is not available. The available alpha values are:"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")


    def test_details_raise(self):
        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = AndersonDarling()
            result.fit(self.x, details="shorte")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = AndersonDarling()
            result.fit(self.x, details="shot")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = AndersonDarling()
            result.fit(self.x, details="ful")


    def test_details_raise_output_normal_output(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = AndersonDarling()
            result.fit(self.x, details="shorte")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'details' parameter only accepts 'short', 'full' or 'binary' as values, but we got 'shorte'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        #################


        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = AndersonDarling()
            result.fit(self.x, details="binario")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'details' parameter only accepts 'short', 'full' or 'binary' as values, but we got 'binario'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        #################


        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = AndersonDarling()
            result.fit(self.x, details="ful")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'details' parameter only accepts 'short', 'full' or 'binary' as values, but we got 'ful'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        #################


    def test_pass_normal_details_full(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x, details="full")
        self.assertAlmostEqual(resultado[0], 0.22687861079050364, "wrong statistic value")
        self.assertEqual(resultado[1], 0.684, "wrong critical value")
        self.assertIsNone(resultado[2], msg="p-value not none")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "critical" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'critical' not in conclusion when it should")


    def test_pass_normal_details_binary(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x, details="binary")
        self.assertAlmostEqual(resultado[0], 0.22687861079050364, "wrong statistic value")
        self.assertEqual(resultado[1], 0.684, "wrong critical value")
        self.assertIsNone(resultado[2], msg="p-value not none")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertIsInstance(conclusao, int, msg="conclusion not int when details is binary")
        self.assertEqual(conclusao, 0, msg='conclusao not 0 when data is normal')


    def test_pass_normal_details_binary_comparison_p(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x, details="binary", comparison='p-value')
        self.assertAlmostEqual(resultado[0], 0.22687861079050364, "wrong statistic value")
        self.assertIsNone(resultado[1], msg="critical value not none")
        self.assertAlmostEqual(resultado[2], 0.7479231606974011, "wrong p-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertIsInstance(conclusao, int, msg="conclusion not int when details is binary")
        self.assertEqual(conclusao, 0, msg='conclusao not 0 when data is normal')


    def test_alfa_0_05_p_value(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x, comparison="p-value")
        self.assertAlmostEqual(resultado[0], 0.22687861079050364, "wrong statistic value")
        self.assertIsNone(resultado[1], msg="critical value not none")
        self.assertAlmostEqual(resultado[2], 0.7479231606974011, "wrong p-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Normal' not in conclusion when it should")


    def test_alfa_0_10_p_value(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x, alfa=0.10, comparison="p-value")
        self.assertAlmostEqual(resultado[0], 0.22687861079050364, "wrong statistic value")
        self.assertIsNone(resultado[1], msg="critical value not none")
        self.assertAlmostEqual(resultado[2], 0.7479231606974011, "wrong p-value value")
        self.assertEqual(resultado[3], 0.10, "wrong alfa value")
        if "Data is Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Normal' not in conclusion when it should")


    def test_alfa_0_12_p_value(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x, alfa=0.12, comparison="p-value")
        self.assertAlmostEqual(resultado[0], 0.22687861079050364, "wrong statistic value")
        self.assertIsNone(resultado[1], msg="critical value not none")
        self.assertAlmostEqual(resultado[2], 0.7479231606974011, "wrong p-value value")
        self.assertEqual(resultado[3], 0.12, "wrong alfa value")
        if "Data is Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Normal' not in conclusion when it should")


    def test_details_raise_p_value(self):
        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = AndersonDarling()
            result.fit(self.x, details="shorte", comparison="p-value")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = AndersonDarling()
            result.fit(self.x, details="shot", comparison="p-value")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = AndersonDarling()
            result.fit(self.x, details="ful", comparison="p-value")


    def test_pass_normal_details_full_p_value(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x, details="full", comparison="p-value")
        self.assertAlmostEqual(resultado[0], 0.22687861079050364, "wrong statistic value")
        self.assertIsNone(resultado[1], msg="critical value not none")
        self.assertAlmostEqual(resultado[2], 0.7479231606974011, "wrong p-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "p-value" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'p-value' not in conclusion when it should")


    def test_alfa_0_05_not_normal(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x_not_normal)
        self.assertAlmostEqual(resultado[0], 1.1254567837852019, "wrong statistic value")
        self.assertEqual(resultado[1], 0.693, "wrong tabulated value")
        self.assertIsNone(resultado[2], msg="p-value not none")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Not Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Not Normal' not in conclusion when it should")


    def test_alfa_0_05_not_normal_binary(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x_not_normal, details='binary')
        self.assertAlmostEqual(resultado[0], 1.1254567837852019, "wrong statistic value")
        self.assertEqual(resultado[1], 0.693, "wrong tabulated value")
        self.assertIsNone(resultado[2], msg="p-value not none")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertIsInstance(conclusao, int, msg="conclusao not int with details=binary")
        self.assertEqual(conclusao, 1, msg='conclusao not 1 when data is not normal')


    def test_alfa_0_05_not_normal_binary_p_value(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x_not_normal, details='binary', comparison='p-value')
        self.assertAlmostEqual(resultado[0], 1.1254567837852019, "wrong statistic value")
        self.assertIsNone(resultado[1], msg="critical value not none")
        self.assertAlmostEqual(resultado[2], 0.0029784226623797575, "wrong p-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertIsInstance(conclusao, int, msg="conclusao not int with details=binary")
        self.assertEqual(conclusao, 1, msg='conclusao not 1 when data is not normal')


    def test_alfa_0_05_full_not_normal_n_digits(self):
        result = AndersonDarling(n_digits=5)
        resultado, conclusao = result.fit(self.x_not_normal, details='full')
        self.assertAlmostEqual(resultado[0], 1.1254567837852019, "wrong statistic value")
        self.assertEqual(resultado[1], 0.693, "wrong tabulated value")
        self.assertIsNone(resultado[2], msg="p-value not none")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "(1.12545)" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'(1.12545)' not in conclusion when it should")


    def test_alfa_0_10_not_normal(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x_not_normal, alfa=0.10)
        self.assertAlmostEqual(resultado[0], 1.1254567837852019, "wrong statistic value")
        self.assertEqual(resultado[1], 0.578, "wrong tabulated value")
        self.assertIsNone(resultado[2], msg="p-value not none")
        self.assertEqual(resultado[3], 0.10, "wrong alfa value")
        if "Data is Not Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Not Normal' not in conclusion when it should")


    def test_alfa_0_12_not_normal(self):
        with self.assertRaises(ValueError, msg="Does not raised error when alfa=0.12"):
            result = AndersonDarling()
            resultado, conclusao = result.fit(self.x_not_normal, alfa=0.12)


    def test_details_raise_output_not_normal_0_12(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = AndersonDarling()
            resultado, conclusao = result.fit(self.x_not_normal, alfa=0.12)
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The critical value for alpha '0.12' is not available. The available alpha values are:"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")


    def test_details_raise_not_normal(self):
        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = AndersonDarling()
            result.fit(self.x_not_normal, details="shorte")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = AndersonDarling()
            result.fit(self.x_not_normal, details="shot")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = AndersonDarling()
            result.fit(self.x_not_normal, details="ful")


    def test_details_raise_output_not_normal_output(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = AndersonDarling()
            result.fit(self.x_not_normal, details="shorte")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'details' parameter only accepts 'short', 'full' or 'binary' as values, but we got 'shorte'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        #################


        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = AndersonDarling()
            result.fit(self.x_not_normal, details="binario")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'details' parameter only accepts 'short', 'full' or 'binary' as values, but we got 'binario'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        #################


        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = AndersonDarling()
            result.fit(self.x_not_normal, details="ful")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'details' parameter only accepts 'short', 'full' or 'binary' as values, but we got 'ful'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        #################


    def test_pass_normal_details_full_not_normal(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x_not_normal, details="full")
        self.assertAlmostEqual(resultado[0], 1.1254567837852019, "wrong statistic value")
        self.assertEqual(resultado[1], 0.693, "wrong critical value")
        self.assertIsNone(resultado[2], msg="p-value not none")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "critical" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'critical' not in conclusion when it should")


    def test_alfa_0_05_p_value_not_normal(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x_not_normal, comparison="p-value")
        self.assertAlmostEqual(resultado[0], 1.1254567837852019, "wrong statistic value")
        self.assertIsNone(resultado[1], msg="critical value not none")
        self.assertAlmostEqual(resultado[2], 0.0029784226623797575, "wrong p-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Not Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Not Normal' not in conclusion when it should")


    def test_alfa_0_10_p_value_not_normal(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x_not_normal, alfa=0.10, comparison="p-value")
        self.assertAlmostEqual(resultado[0], 1.1254567837852019, "wrong statistic value")
        self.assertIsNone(resultado[1], msg="critical value not none")
        self.assertAlmostEqual(resultado[2], 0.0029784226623797575, "wrong p-value value")
        self.assertEqual(resultado[3], 0.10, "wrong alfa value")
        if "Data is Not Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Not Normal' not in conclusion when it should")


    def test_alfa_0_12_p_value_not_normal(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x_not_normal, alfa=0.12, comparison="p-value")
        self.assertAlmostEqual(resultado[0], 1.1254567837852019, "wrong statistic value")
        self.assertIsNone(resultado[1], msg="critical value not none")
        self.assertAlmostEqual(resultado[2], 0.0029784226623797575, "wrong p-value value")
        self.assertEqual(resultado[3], 0.12, "wrong alfa value")
        if "Data is Not Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Not Normal' not in conclusion when it should")


    def test_details_raise_p_value_not_normal(self):
        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = AndersonDarling()
            result.fit(self.x_not_normal, details="shorte", comparison="p-value")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = AndersonDarling()
            result.fit(self.x_not_normal, details="shot", comparison="p-value")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = AndersonDarling()
            result.fit(self.x_not_normal, details="ful", comparison="p-value")


    def test_pass_normal_details_full_p_value_not_normal(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x_not_normal, details="full", comparison="p-value")
        self.assertAlmostEqual(resultado[0], 1.1254567837852019, "wrong statistic value")
        self.assertIsNone(resultado[1], msg="critical value not none")
        self.assertAlmostEqual(resultado[2], 0.0029784226623797575, "wrong p-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "p-value" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'p-value' not in conclusion when it should")








# suki, kirai, suki, kirai  https://youtu.be/1eLuB5CoryM?t=103


if __name__ == "__main__":
    unittest.main()
