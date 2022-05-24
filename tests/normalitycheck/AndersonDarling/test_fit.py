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
os.system('cls')

class Test_fit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        cls.x_not_normal = np.array([1, 1, 1, 1.1, 1.2, 5.3, 10.1, 10.2, 10.3])

    def test_statistic_between_methods(self):
        result = AndersonDarling()
        statistic_scipy, _ = result.fit(self.x, conclusion="critical")
        statistic_statsmodels, _ = result.fit(self.x, conclusion="p-value")
        self.assertEqual(statistic_scipy[0], statistic_statsmodels[0], msg="The statistic value does not match between fit methods")

        result = AndersonDarling()
        statistic_scipy, _ = result.fit(self.x_not_normal, conclusion="critical")
        statistic_statsmodels, _ = result.fit(self.x_not_normal, conclusion="p-value")
        self.assertEqual(statistic_scipy[0], statistic_statsmodels[0], msg="The statistic value does not match between fit methods")


    def test_alfa_0_05(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x)
        self.assertEqual(resultado[0], 0.226, "wrong statistic value")
        self.assertEqual(resultado[1], 0.684, "wrong tabulated value")
        self.assertIsNone(resultado[2], msg="p-value not none")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Normal' not in conclusion when it should")

    def test_alfa_0_10(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x, alfa=0.10)
        self.assertEqual(resultado[0], 0.226, "wrong statistic value")
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


    def test_pass_normal_details_full(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x, details="full")
        self.assertEqual(resultado[0], 0.226, "wrong statistic value")
        self.assertEqual(resultado[1], 0.684, "wrong critical value")
        self.assertIsNone(resultado[2], msg="p-value not none")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "critical" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'critical' not in conclusion when it should")

    def test_alfa_0_05_p_value(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x, conclusion="p-value")
        self.assertEqual(resultado[0], 0.226, "wrong statistic value")
        self.assertIsNone(resultado[1], msg="critical value not none")
        self.assertEqual(resultado[2], 0.747, "wrong p-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Normal' not in conclusion when it should")

    def test_alfa_0_10_p_value(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x, alfa=0.10, conclusion="p-value")
        self.assertEqual(resultado[0], 0.226, "wrong statistic value")
        self.assertIsNone(resultado[1], msg="critical value not none")
        self.assertEqual(resultado[2], 0.747, "wrong p-value value")
        self.assertEqual(resultado[3], 0.10, "wrong alfa value")
        if "Data is Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Normal' not in conclusion when it should")

    def test_alfa_0_12_p_value(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x, alfa=0.12, conclusion="p-value")
        self.assertEqual(resultado[0], 0.226, "wrong statistic value")
        self.assertIsNone(resultado[1], msg="critical value not none")
        self.assertEqual(resultado[2], 0.747, "wrong p-value value")
        self.assertEqual(resultado[3], 0.12, "wrong alfa value")
        if "Data is Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Normal' not in conclusion when it should")


    def test_details_raise_p_value(self):
        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = AndersonDarling()
            result.fit(self.x, details="shorte", conclusion="p-value")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = AndersonDarling()
            result.fit(self.x, details="shot", conclusion="p-value")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = AndersonDarling()
            result.fit(self.x, details="ful", conclusion="p-value")


    def test_pass_normal_details_full_p_value(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x, details="full", conclusion="p-value")
        self.assertEqual(resultado[0], 0.226, "wrong statistic value")
        self.assertIsNone(resultado[1], msg="critical value not none")
        self.assertEqual(resultado[2], 0.747, "wrong p-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "p-value" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'p-value' not in conclusion when it should")


    def test_alfa_0_05_not_normal(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x_not_normal)
        self.assertEqual(resultado[0], 1.125, "wrong statistic value")
        self.assertEqual(resultado[1], 0.693, "wrong tabulated value")
        self.assertIsNone(resultado[2], msg="p-value not none")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Not Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Not Normal' not in conclusion when it should")

    def test_alfa_0_10_not_normal(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x_not_normal, alfa=0.10)
        self.assertEqual(resultado[0], 1.125, "wrong statistic value")
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


    def test_pass_normal_details_full_not_normal(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x_not_normal, details="full")
        self.assertEqual(resultado[0], 1.125, "wrong statistic value")
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
        resultado, conclusao = result.fit(self.x_not_normal, conclusion="p-value")
        self.assertEqual(resultado[0], 1.125, "wrong statistic value")
        self.assertIsNone(resultado[1], msg="critical value not none")
        self.assertEqual(resultado[2], 0.002, "wrong p-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Not Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Not Normal' not in conclusion when it should")

    def test_alfa_0_10_p_value_not_normal(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x_not_normal, alfa=0.10, conclusion="p-value")
        self.assertEqual(resultado[0], 1.125, "wrong statistic value")
        self.assertIsNone(resultado[1], msg="critical value not none")
        self.assertEqual(resultado[2], 0.002, "wrong p-value value")
        self.assertEqual(resultado[3], 0.10, "wrong alfa value")
        if "Data is Not Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Not Normal' not in conclusion when it should")

    def test_alfa_0_12_p_value_not_normal(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x_not_normal, alfa=0.12, conclusion="p-value")
        self.assertEqual(resultado[0], 1.125, "wrong statistic value")
        self.assertIsNone(resultado[1], msg="critical value not none")
        self.assertEqual(resultado[2], 0.002, "wrong p-value value")
        self.assertEqual(resultado[3], 0.12, "wrong alfa value")
        if "Data is Not Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Not Normal' not in conclusion when it should")


    def test_details_raise_p_value_not_normal(self):
        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = AndersonDarling()
            result.fit(self.x_not_normal, details="shorte", conclusion="p-value")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = AndersonDarling()
            result.fit(self.x_not_normal, details="shot", conclusion="p-value")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = AndersonDarling()
            result.fit(self.x_not_normal, details="ful", conclusion="p-value")


    def test_pass_normal_details_full_p_value_not_normal(self):
        result = AndersonDarling()
        resultado, conclusao = result.fit(self.x_not_normal, details="full", conclusion="p-value")
        self.assertEqual(resultado[0], 1.125, "wrong statistic value")
        self.assertIsNone(resultado[1], msg="critical value not none")
        self.assertEqual(resultado[2], 0.002, "wrong p-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "p-value" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'p-value' not in conclusion when it should")








# suki, kirai, suki, kirai  https://youtu.be/1eLuB5CoryM?t=103


if __name__ == "__main__":
    unittest.main()
