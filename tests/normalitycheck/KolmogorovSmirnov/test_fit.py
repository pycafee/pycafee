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
os.system('cls')

class Test_fit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        cls.x_not_normal = np.array([1, 1, 1, 1, 1, 1, 1 ,1, 1.1, 1.2, 5.3, 10.1, 10.2, 10.3])


    def test_alfa_0_10(self):
        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x, alfa=0.10)
        self.assertEqual(resultado[0], 0.154, "wrong statistic value")
        self.assertEqual(resultado[1], 0.368, "wrong tabulated value")
        self.assertEqual(resultado[2], 0.970, "wrong P-value value")
        self.assertEqual(resultado[3], 0.10, "wrong alfa value")
        if "Data is Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Normal' not in conclusion when it should")


    def test_alfa_0_02(self):
        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x, alfa=0.02, conclusion="p-value")
        self.assertEqual(resultado[0], 0.154, "wrong statistic value")
        self.assertIsNone(resultado[1], "wrong tabulated value")
        self.assertEqual(resultado[2], 0.970, "wrong P-value value")
        self.assertEqual(resultado[3], 0.02, "wrong alfa value")
        if "critical" in conclusao:
            result = False
        else:
            result = True
        self.assertTrue(result, "'critical' not in conclusion when it should")


    def test_alfa_0_25(self):
        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x, alfa=0.25, conclusion="p-value")
        self.assertEqual(resultado[0], 0.154, "wrong statistic value")
        self.assertIsNone(resultado[1], "wrong tabulated value")
        self.assertEqual(resultado[2], 0.970, "wrong P-value value")
        self.assertEqual(resultado[3], 0.25, "wrong alfa value")
        if "critical" in conclusao:
            result = False
        else:
            result = True
        self.assertTrue(result, "'critical' not in conclusion when it should")


    def test_conclusion(self):
        with self.assertRaises(ValueError, msg="Does not raised error when conclusion is not valid"):
            result = KolmogorovSmirnov()
            result.fit(self.x, conclusion="any")

        with self.assertRaises(ValueError, msg="Does not raised error when conclusion is not valid"):
            result = KolmogorovSmirnov()
            result.fit(self.x, conclusion="tabulated")

        with self.assertRaises(ValueError, msg="Does not raised error when conclusion is not valid"):
            result = KolmogorovSmirnov()
            result.fit(self.x, conclusion="p_value")

    def test_details(self):
        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = KolmogorovSmirnov()
            result.fit(self.x, details="shorte")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = KolmogorovSmirnov()
            result.fit(self.x, details="shot")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = KolmogorovSmirnov()
            result.fit(self.x, details="ful")


    def test_pass_normal(self):
        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x)
        self.assertEqual(resultado[0], 0.154, "wrong statistic value")
        self.assertEqual(resultado[1], 0.41, "wrong tabulated value")
        self.assertEqual(resultado[2], 0.970, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Normal' not in conclusion when it should")

    def test_pass_normal_conclusion_p_value(self):
        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x, conclusion="p-value")
        self.assertEqual(resultado[0], 0.154, "wrong statistic value")
        self.assertEqual(resultado[1], 0.410, "wrong tabulated value")
        self.assertEqual(resultado[2], 0.970, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Normal' not in conclusion when it should")

    def test_pass_normal_details_full(self):
        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x, details="full")
        self.assertEqual(resultado[0], 0.154, "wrong statistic value")
        self.assertEqual(resultado[1], 0.410, "wrong tabulated value")
        self.assertEqual(resultado[2], 0.970, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "critical" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'critical' not in conclusion when it should")

    def test_pass_normal_details_full_conclusion_p_value(self):
        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x, details="full", conclusion="p-value")
        self.assertEqual(resultado[0], 0.154, "wrong statistic value")
        self.assertEqual(resultado[1], 0.410, "wrong tabulated value")
        self.assertEqual(resultado[2], 0.970, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "p-value" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'p-value' not in conclusion when it should")


    def test_pass_not_normal(self):
        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x_not_normal)
        self.assertEqual(resultado[0], 0.418, "wrong statistic value")
        self.assertEqual(resultado[1], 0.349, "wrong tabulated value")
        self.assertEqual(resultado[2], 0.009, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Not Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Not Normal' not in conclusion when it should")


    def test_pass_not_normal_conclusion_p_value(self):
        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x_not_normal, conclusion="p-value")
        self.assertEqual(resultado[0], 0.418, "wrong statistic value")
        self.assertEqual(resultado[1], 0.349, "wrong tabulated value")
        self.assertEqual(resultado[2], 0.009, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Not Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Not Normal' not in conclusion when it should")

    def test_pass_not_normal_details_full(self):
        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x_not_normal, details="full")
        self.assertEqual(resultado[0], 0.418, "wrong statistic value")
        self.assertEqual(resultado[1], 0.349, "wrong tabulated value")
        self.assertEqual(resultado[2], 0.009, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "critical" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'critical' not in conclusion when it should")
    #
    def test_pass_not_normal_details_full_conclusion_p_value(self):
        result = KolmogorovSmirnov()
        resultado, conclusao = result.fit(self.x_not_normal, details="full", conclusion="p-value")
        self.assertEqual(resultado[0], 0.418, "wrong statistic value")
        self.assertEqual(resultado[1], 0.349, "wrong tabulated value")
        self.assertEqual(resultado[2], 0.009, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "p-value" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'p-value' not in conclusion when it should")
    #



# I become so numb, I can't feel you there, become so tired... https://youtu.be/Tj9gy8uAPNE?t=154


if __name__ == "__main__":
    unittest.main()
