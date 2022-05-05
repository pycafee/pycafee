"""Tests if the shapiro_wilk is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_shapiro_wilk
    This class tests the shapiro_wilk function. It should raise ValueError conclustion or detail got worng key. The function is tests against correct output, when data is Normal and qhen data is Not Normal.


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/functions/distributions/test_shapiro_wilk.py
    or
    python -m unittest -b tests/functions/distributions/test_shapiro_wilk.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.functions.distributions import ShapiroWilkNormalityTest
import numpy as np
os.system('cls')

class Test_shapiro_wilk(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        cls.x_not_normal = np.array([1, 1.2, 1.6, 1.8, 2, 2.2, 3, 5, 7, 7.2, 8.2, 8.4, 8.6, 9])

    def test_conclusion(self):
        with self.assertRaises(ValueError, msg="Does not raised error when conclusion is not valid"):
            result = ShapiroWilkNormalityTest()
            result.shapiro_wilk(self.x, conclusion="any")

        with self.assertRaises(ValueError, msg="Does not raised error when conclusion is not valid"):
            result = ShapiroWilkNormalityTest()
            result.shapiro_wilk(self.x, conclusion="tabulated")

        with self.assertRaises(ValueError, msg="Does not raised error when conclusion is not valid"):
            result = ShapiroWilkNormalityTest()
            result.shapiro_wilk(self.x, conclusion="p-value")

    def test_details(self):
        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = ShapiroWilkNormalityTest()
            result.shapiro_wilk(self.x, conclusion="shorte")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = ShapiroWilkNormalityTest()
            result.shapiro_wilk(self.x, conclusion="shot")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = ShapiroWilkNormalityTest()
            result.shapiro_wilk(self.x, details="ful")


    def test_pass_normal(self):
        result = ShapiroWilkNormalityTest()
        resultado, conclusao = result.shapiro_wilk(self.x)
        self.assertEqual(resultado[0], 0.9698, "wrong statistic value")
        self.assertEqual(resultado[1], 0.842, "wrong tabulated value")
        self.assertEqual(resultado[2], 0.889, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Normal' not in conclusion when it should")

    def test_pass_normal_conclusion_p_value(self):
        result = ShapiroWilkNormalityTest()
        resultado, conclusao = result.shapiro_wilk(self.x, conclusion="p_value")
        self.assertEqual(resultado[0], 0.9698, "wrong statistic value")
        self.assertEqual(resultado[1], 0.842, "wrong tabulated value")
        self.assertEqual(resultado[2], 0.889, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Normal' not in conclusion when it should")

    def test_pass_normal_details_full(self):
        result = ShapiroWilkNormalityTest()
        resultado, conclusao = result.shapiro_wilk(self.x, details="full")
        self.assertEqual(resultado[0], 0.9698, "wrong statistic value")
        self.assertEqual(resultado[1], 0.842, "wrong tabulated value")
        self.assertEqual(resultado[2], 0.889, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "tabulated" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'tabulated' not in conclusion when it should")

    def test_pass_normal_details_full_conclusion_p_value(self):
        result = ShapiroWilkNormalityTest()
        resultado, conclusao = result.shapiro_wilk(self.x, details="full", conclusion="p_value")
        self.assertEqual(resultado[0], 0.9698, "wrong statistic value")
        self.assertEqual(resultado[1], 0.842, "wrong tabulated value")
        self.assertEqual(resultado[2], 0.889, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "p-value" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'p-value' not in conclusion when it should")


    def test_pass_not_normal(self):
        result = ShapiroWilkNormalityTest()
        resultado, conclusao = result.shapiro_wilk(self.x_not_normal)
        self.assertEqual(resultado[0], 0.8413, "wrong statistic value")
        self.assertEqual(resultado[1], 0.874, "wrong tabulated value")
        self.assertEqual(resultado[2], 0.0169, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Not Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Not Normal' not in conclusion when it should")


    def test_pass_not_normal_conclusion_p_value(self):
        result = ShapiroWilkNormalityTest()
        resultado, conclusao = result.shapiro_wilk(self.x_not_normal, conclusion="p_value")
        self.assertEqual(resultado[0], 0.8413, "wrong statistic value")
        self.assertEqual(resultado[1], 0.874, "wrong tabulated value")
        self.assertEqual(resultado[2], 0.0169, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Not Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Not Normal' not in conclusion when it should")

    def test_pass_not_normal_details_full(self):
        result = ShapiroWilkNormalityTest()
        resultado, conclusao = result.shapiro_wilk(self.x_not_normal, details="full")
        self.assertEqual(resultado[0], 0.8413, "wrong statistic value")
        self.assertEqual(resultado[1], 0.874, "wrong tabulated value")
        self.assertEqual(resultado[2], 0.0169, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "tabulated" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'tabulated' not in conclusion when it should")

    def test_pass_not_normal_details_full_conclusion_p_value(self):
        result = ShapiroWilkNormalityTest()
        resultado, conclusao = result.shapiro_wilk(self.x_not_normal, details="full", conclusion="p_value")
        self.assertEqual(resultado[0], 0.8413, "wrong statistic value")
        self.assertEqual(resultado[1], 0.874, "wrong tabulated value")
        self.assertEqual(resultado[2], 0.0169, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "p-value" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'p-value' not in conclusion when it should")







if __name__ == "__main__":
    unittest.main()
