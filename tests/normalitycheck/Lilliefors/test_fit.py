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
os.system('cls')

class Test_fit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        cls.x_not_normal = np.array([1, 1, 1, 1.1, 1.2, 5.3, 10.1, 10.2, 10.3])

    def test_alfa_0_05(self):
        result = Lilliefors()
        resultado, conclusao = result.fit(self.x)
        self.assertEqual(resultado[0], 0.154, "wrong statistic value")
        self.assertEqual(resultado[1], 0.258, "wrong tabulated value")
        self.assertEqual(resultado[2], 0.71, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Normal' not in conclusion when it should")

    def test_alfa_0_10(self):
        result = Lilliefors()
        resultado, conclusao = result.fit(self.x, alfa=0.10)
        self.assertEqual(resultado[0], 0.154, "wrong statistic value")
        self.assertEqual(resultado[1], 0.239, "wrong tabulated value")
        self.assertEqual(resultado[2], 0.71, "wrong P-value value")
        self.assertEqual(resultado[3], 0.10, "wrong alfa value")
        if "Data is Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Normal' not in conclusion when it should")

    def test_alfa_0_12(self):
        with self.assertRaises(ValueError, msg="Does not raised error when alfa=0.12 with default paramters"):
            result = Lilliefors()
            resultado, conclusao = result.fit(self.x, alfa=0.12)

        with self.assertRaises(ValueError, msg="Does not raised error when alfa=0.12 with conclusion='critical'"):
            result = Lilliefors()
            resultado, conclusao = result.fit(self.x, alfa=0.12, conclusion="critical")

        with self.assertRaises(ValueError, msg="Does not raised error when alfa=0.12"):
            result = Lilliefors()
            resultado, conclusao = result.fit(self.x, alfa=0.12)


    def test_conclusion(self):
        with self.assertRaises(ValueError, msg="Does not raised error when conclusion is not valid"):
            result = Lilliefors()
            result.fit(self.x, conclusion="any")

        with self.assertRaises(ValueError, msg="Does not raised error when conclusion is not valid"):
            result = Lilliefors()
            result.fit(self.x, conclusion="tabulated")

        with self.assertRaises(ValueError, msg="Does not raised error when conclusion is not valid"):
            result = Lilliefors()
            result.fit(self.x, conclusion="p_value")

    def test_details(self):
        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = Lilliefors()
            result.fit(self.x, details="shorte")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = Lilliefors()
            result.fit(self.x, details="shot")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = Lilliefors()
            result.fit(self.x, details="ful")

    def test_pass_normal_conclusion_p_value(self):
        result = Lilliefors()
        resultado, conclusao = result.fit(self.x, conclusion="p-value")
        self.assertEqual(resultado[0], 0.154, "wrong statistic value")
        self.assertEqual(resultado[1], 0.258, "wrong critical value")
        self.assertEqual(resultado[2], 0.71, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Normal' not in conclusion when it should")

    def test_pass_normal_details_full(self):
        result = Lilliefors()
        resultado, conclusao = result.fit(self.x, details="full")
        self.assertEqual(resultado[0], 0.154, "wrong statistic value")
        self.assertEqual(resultado[1], 0.258, "wrong critical value")
        self.assertEqual(resultado[2], 0.71, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "critical" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'critical' not in conclusion when it should")

    def test_pass_normal_details_full_conclusion_p_value(self):
        result = Lilliefors()
        resultado, conclusao = result.fit(self.x, details="full", conclusion="p-value")
        self.assertEqual(resultado[0], 0.154, "wrong statistic value")
        self.assertEqual(resultado[1], 0.258, "wrong tabulated value")
        self.assertEqual(resultado[2], 0.71, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "p-value" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'p-value' not in conclusion when it should")

    def test_alfa_0_05_not_normal(self):
        result = Lilliefors()
        resultado, conclusao = result.fit(self.x_not_normal)
        self.assertEqual(resultado[0], 0.332, "wrong statistic value")
        self.assertEqual(resultado[1], 0.271, "wrong tabulated value")
        self.assertEqual(resultado[2], 0.005, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Not Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Not Normal' not in conclusion when it should")

    def test_alfa_0_10_not_normal(self):
        result = Lilliefors()
        resultado, conclusao = result.fit(self.x_not_normal, alfa=0.10)
        self.assertEqual(resultado[0], 0.332, "wrong statistic value")
        self.assertEqual(resultado[1], 0.249, "wrong tabulated value")
        self.assertEqual(resultado[2], 0.005, "wrong P-value value")
        self.assertEqual(resultado[3], 0.10, "wrong alfa value")
        if "Data is Not Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Not Normal' not in conclusion when it should")

    def test_alfa_0_12_not_normal(self):
        with self.assertRaises(ValueError, msg="Does not raised error when alfa=0.12 with default parameters, not normal data"):
            result = Lilliefors()
            resultado, conclusao = result.fit(self.x_not_normal, alfa=0.12)

        with self.assertRaises(ValueError, msg="Does not raised error when alfa=0.12 with conclusion='tabulate', not normal data"):
            result = Lilliefors()
            resultado, conclusao = result.fit(self.x_not_normal, alfa=0.12, conclusion="critical")



    def test_conclusion_not_normal(self):
        with self.assertRaises(ValueError, msg="Does not raised error when conclusion is not valid, not normal"):
            result = Lilliefors()
            result.fit(self.x_not_normal, conclusion="any")

        with self.assertRaises(ValueError, msg="Does not raised error when conclusion is not valid, not normal"):
            result = Lilliefors()
            result.fit(self.x_not_normal, conclusion="tabulated")

        with self.assertRaises(ValueError, msg="Does not raised error when conclusion is not valid, not normal"):
            result = Lilliefors()
            result.fit(self.x_not_normal, conclusion="p_value")

    def test_details_not_normal(self):
        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid, not normal"):
            result = Lilliefors()
            result.fit(self.x_not_normal, details="shorte")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid, not normal"):
            result = Lilliefors()
            result.fit(self.x_not_normal, details="shot")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid, not normal"):
            result = Lilliefors()
            result.fit(self.x_not_normal, details="ful")

    def test_pass_normal_conclusion_p_value_not_normal(self):
        result = Lilliefors()
        resultado, conclusao = result.fit(self.x_not_normal, conclusion="p-value")
        self.assertEqual(resultado[0], 0.332, "wrong statistic value")
        self.assertEqual(resultado[1], 0.271, "wrong tabulated value")
        self.assertEqual(resultado[2], 0.005, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Not Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Not Normal' not in conclusion when it should")

    def test_pass_normal_details_full_not_normal(self):
        result = Lilliefors()
        resultado, conclusao = result.fit(self.x_not_normal, details="full")
        self.assertEqual(resultado[0], 0.332, "wrong statistic value")
        self.assertEqual(resultado[1], 0.271, "wrong tabulated value")
        self.assertEqual(resultado[2], 0.005, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "HAVE" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'HAVE' not in conclusion when it should")

    def test_pass_normal_details_full_conclusion_p_value_not_normal(self):
        result = Lilliefors()
        resultado, conclusao = result.fit(self.x_not_normal, details="full", conclusion="p-value")
        self.assertEqual(resultado[0], 0.332, "wrong statistic value")
        self.assertEqual(resultado[1], 0.271, "wrong tabulated value")
        self.assertEqual(resultado[2], 0.005, "wrong P-value value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "HAVE" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'HAVE' not in conclusion when it should")






# and now i understand the problems, you can see https://youtu.be/N26_hRITlsU?t=51

if __name__ == "__main__":
    unittest.main()
