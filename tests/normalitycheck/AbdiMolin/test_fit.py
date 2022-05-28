"""Tests if the fit function for AbdiMolin is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_fit
    This class tests the fit function. It should raise ValueError conclustion or detail got worng key. The function is tests against correct output, when data is Normal and when data is Not Normal.


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/normalitycheck/AbdiMolin/test_fit.py
    or
    python -m unittest -b tests/normalitycheck/AbdiMolin/test_fit.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.normalitycheck.abdimolin import AbdiMolin
import numpy as np
import io
import  sys
os.system('cls')

class Test_fit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        cls.x_not_normal = np.array([1, 1, 1, 1.1, 1.2, 5.3, 10.1, 10.2, 10.3])



    def test_n_rep_70(self):
        x = np.array([1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 3, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2 ,3 ,2 , 3, 2, 3, 2, 3, 2,
                    3, 2,2, 1, 2, 3, 3, 3, 2, 1, 2, 3, 2, 3, 3, 2, 3, 3, 2, 1, 2, 3, 2, 3, 2, 2, 2, 2, 2, 3, 2, 2, 3, 1,
                    1, 1, 1])
        result = AbdiMolin()
        resultado, conclusao = result.fit(x)
        self.assertAlmostEqual(resultado[0], 0.25582712764153626, "wrong statistic value")
        self.assertAlmostEqual(resultado[1], 0.10584445602171873, "wrong tabulated value")
        self.assertIsNone(resultado[2], "p-value not None")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Not Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Not Normal' not in conclusion when it should")



    def test_alfa_0_05(self):
        result = AbdiMolin()
        resultado, conclusao = result.fit(self.x)
        self.assertAlmostEqual(resultado[0], 0.15459867079959644, "wrong statistic value")
        self.assertEqual(resultado[1], 0.2616, "wrong tabulated value")
        self.assertIsNone(resultado[2], "p-value not None")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Normal' not in conclusion when it should")



    def test_alfa_0_05_n_digits(self):
        result = AbdiMolin(n_digits=4)
        resultado, conclusao = result.fit(self.x, details="full")
        self.assertAlmostEqual(resultado[0], 0.15459867079959644, "wrong statistic value")
        self.assertEqual(resultado[1], 0.2616, "wrong tabulated value")
        self.assertIsNone(resultado[2], "p-value not None")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "(0.1545)" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Normal' not in conclusion when it should")



    def test_alfa_0_10(self):
        result = AbdiMolin()
        resultado, conclusao = result.fit(self.x, alfa=0.10)
        self.assertAlmostEqual(resultado[0], 0.15459867079959644, "wrong statistic value")
        self.assertEqual(resultado[1], 0.241, "wrong tabulated value")
        self.assertIsNone(resultado[2], "p-value not None")
        self.assertEqual(resultado[3], 0.10, "wrong alfa value")
        if "Data is Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Normal' not in conclusion when it should")



    def test_alfa_0_12(self):
        with self.assertRaises(ValueError, msg="Does not raised error when alfa=0.12"):
            result = AbdiMolin()
            resultado, conclusao = result.fit(self.x, alfa=0.12)



    def test_details_raise(self):
        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = AbdiMolin()
            result.fit(self.x, details="shorte")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = AbdiMolin()
            result.fit(self.x, details="shot")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = AbdiMolin()
            result.fit(self.x, details="ful")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = AbdiMolin()
            result.fit(self.x, details="biario")



    def test_details_raise_output(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = AbdiMolin()
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
            result = AbdiMolin(language='pt-br')
            result.fit(self.x, details="ful")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "O parâmetro 'details' aceita apenas 'short', 'full' ou 'binary' como valores, mas obtivemos 'ful'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        #################

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = AbdiMolin()
            result.fit(self.x, details="biario")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'details' parameter only accepts 'short', 'full' or 'binary' as values, but we got 'biario'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")



    def test_pass_normal_details_full(self):
        result = AbdiMolin()
        resultado, conclusao = result.fit(self.x, details="full")
        self.assertEqual(resultado[0], 0.15459867079959644, "wrong statistic value")
        self.assertEqual(resultado[1], 0.2616, "wrong critical value")
        self.assertIsNone(resultado[2], "pvalue not Nont")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "critical" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'critical' not in conclusion when it should")



    def test_pass_normal_details_binary(self):
        result = AbdiMolin()
        resultado, conclusao = result.fit(self.x, details="binary")
        self.assertEqual(resultado[0], 0.15459867079959644, "wrong statistic value")
        self.assertEqual(resultado[1], 0.2616, "wrong critical value")
        self.assertIsNone(resultado[2], "pvalue not Nont")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertTrue(result, "'critical' not in conclusion when it should")
        self.assertIsInstance(conclusao, int, msg="conclusao not int when details is binary")
        self.assertEqual(conclusao, 0, msg="not 0 when accept H0")



    def test_alfa_0_05_not_normal(self):
        result = AbdiMolin()
        resultado, conclusao = result.fit(self.x_not_normal)
        self.assertEqual(resultado[0], 0.33246821361586026, "wrong statistic value")
        self.assertEqual(resultado[1], 0.2744, "wrong tabulated value")
        self.assertIsNone(resultado[2], "p-value not None")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Not Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Not Normal' not in conclusion when it should")



    def test_alfa_0_05_not_normal_n_digits(self):
        result = AbdiMolin(n_digits=4)
        resultado, conclusao = result.fit(self.x_not_normal, details="full")
        self.assertEqual(resultado[0], 0.33246821361586026, "wrong statistic value")
        self.assertEqual(resultado[1], 0.2744, "wrong tabulated value")
        self.assertIsNone(resultado[2], "p-value not None")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "(0.3324)" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Not Normal' not in conclusion when it should")



    def test_alfa_0_10_not_normal(self):
        result = AbdiMolin()
        resultado, conclusao = result.fit(self.x_not_normal, alfa=0.10)
        self.assertEqual(resultado[0], 0.33246821361586026, "wrong statistic value")
        self.assertEqual(resultado[1], 0.2522, "wrong tabulated value")
        self.assertIsNone(resultado[2], "p-value not None")
        self.assertEqual(resultado[3], 0.10, "wrong alfa value")
        if "Data is Not Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Not Normal' not in conclusion when it should")



    def test_alfa_0_12_not_normal(self):
        with self.assertRaises(ValueError, msg="Does not raised error when alfa=0.12 with not normal data"):
            result = AbdiMolin()
            resultado, conclusao = result.fit(self.x_not_normal, alfa=0.12)



    def test_details_not_normal(self):
        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid, not normal"):
            result = AbdiMolin()
            result.fit(self.x_not_normal, details="shorte")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid, not normal"):
            result = AbdiMolin()
            result.fit(self.x_not_normal, details="binario")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid, not normal"):
            result = AbdiMolin()
            result.fit(self.x_not_normal, details="ful")



    def test_details_raise_output_not_normal(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = AbdiMolin()
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
            result = AbdiMolin()
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

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = AbdiMolin(language='pt-br')
            result.fit(self.x_not_normal, details="biario")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "O parâmetro 'details' aceita apenas 'short', 'full' ou 'binary' como valores, mas obtivemos 'biario'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")



    def test_pass_normal_details_full_not_normal(self):
        result = AbdiMolin()
        resultado, conclusao = result.fit(self.x_not_normal, details="full")
        self.assertEqual(resultado[0], 0.33246821361586026, "wrong statistic value")
        self.assertEqual(resultado[1], 0.2744, "wrong tabulated value")
        self.assertIsNone(resultado[2], "p-value not not value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "HAVE" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'HAVE' not in conclusion when it should")



    def test_pass_normal_binary_full_not_normal(self):
        result = AbdiMolin()
        resultado, conclusao = result.fit(self.x_not_normal, details="binary")
        self.assertEqual(resultado[0], 0.33246821361586026, "wrong statistic value")
        self.assertEqual(resultado[1], 0.2744, "wrong tabulated value")
        self.assertIsNone(resultado[2], "p-value not not value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        self.assertIsInstance(conclusao, int, msg="conclusao not int when details is binary")
        self.assertEqual(conclusao, 1, msg="not 0 when reject H0")














if __name__ == "__main__":
    unittest.main()
