"""Tests if the fit function for NormalityCheck is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_fit
    This class tests the fit function. It should raise ValueError when test gets the wrong key.

---> Class Test_fit_default
    This class tests the default test (test=None). It tests every parameter by comparing with the original way to get the results.

---> Class Test_fit_sw
    This class tests the shapiro-wilk test (test="sw"). It tests every parameter by comparing with the original way to get the results.

---> Class Test_fit_ab
    This class tests the abdi-molin test (test="ab"). It tests every parameter by comparing with the original way to get the results.

---> Class Test_fit_ad
    This class tests the anderson-darling test (test="ad"). It tests every parameter by comparing with the original way to get the results.

---> Class Test_fit_ks
    This class tests the kolmogorov-smirnov test (test="ks"). It tests every parameter by comparing with the original way to get the results.

---> Class Test_fit_li
    This class tests the lilliefors test (test="li"). It tests every parameter by comparing with the original way to get the results.

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/normalitycheck/NormalityCheck/test_fit.py
    or
    python -m unittest -b tests/normalitycheck/NormalityCheck/test_fit.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.normalitycheck.normalitycheck import NormalityCheck
import numpy as np
os.system('cls')

class Test_fit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        cls.x_not_normal = np.array([1, 1, 1, 1.1, 1.2, 5.3, 10.1, 10.2, 10.3])

    def test_conclusion(self):
        with self.assertRaises(ValueError, msg="Does not raised error when test is not valid"):
            result = NormalityCheck()
            result.fit(self.x, test="any")

        with self.assertRaises(ValueError, msg="Does not raised error when test is not valid"):
            result = NormalityCheck()
            result.fit(self.x, test="anderson")

        with self.assertRaises(ValueError, msg="Does not raised error when test is not valid"):
            result = NormalityCheck()
            result.fit(self.x, test="shapiro")

        with self.assertRaises(ValueError, msg="Does not raised error when test is not valid"):
            result = NormalityCheck()
            result.fit(self.x, test="abid-molin")

class Test_fit_default(unittest.TestCase):
    from pycafee.normalitycheck.shapirowilk import ShapiroWilk

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        cls.x_not_normal = np.array([1, 1, 1, 1.1, 1.2, 5.3, 10.1, 10.2, 10.3])

    def test_pass_normal(self):
        result = self.ShapiroWilk()
        resultado_esperado, conclusao_esperado = result.fit(self.x)
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x)

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_normal_conclusion_p_value(self):
        result = self.ShapiroWilk()
        resultado_esperado, conclusao_esperado = result.fit(self.x, conclusion='p-value')
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x, conclusion='p-value')

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_normal_details_full(self):
        result = self.ShapiroWilk()
        resultado_esperado, conclusao_esperado = result.fit(self.x, details="full")
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x, details="full")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_normal_details_full_conclusion_p_value(self):
        result = self.ShapiroWilk()
        resultado_esperado, conclusao_esperado = result.fit(self.x, details="full", conclusion="p-value")
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x, details="full", conclusion="p-value")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_normal_alfa(self):
        result = self.ShapiroWilk()
        resultado_esperado, conclusao_esperado = result.fit(self.x, details="full", conclusion="p-value", alfa=0.10)
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x, details="full", conclusion="p-value", alfa=0.10)

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_not_normal(self):
        result = self.ShapiroWilk()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal)
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal)

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")


    def test_pass_not_normal_conclusion_p_value(self):
        result = self.ShapiroWilk()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, conclusion="p-value")
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal, conclusion="p-value")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_not_normal_details_full(self):
        result = self.ShapiroWilk()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full")
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal, details="full")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_not_normal_details_full_conclusion_p_value(self):
        result = self.ShapiroWilk()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full", conclusion="p-value")
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal, details="full", conclusion="p-value")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_alfa_not_normal(self):
        result = self.ShapiroWilk()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full", conclusion="p-value", alfa=0.10)
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal, details="full", conclusion="p-value", alfa=0.10)

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

class Test_fit_sw(unittest.TestCase):
    from pycafee.normalitycheck.shapirowilk import ShapiroWilk

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        cls.x_not_normal = np.array([1, 1, 1, 1.1, 1.2, 5.3, 10.1, 10.2, 10.3])

    def test_pass_normal(self):
        result = self.ShapiroWilk()
        resultado_esperado, conclusao_esperado = result.fit(self.x)
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x, test="sw")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_normal_conclusion_p_value(self):
        result = self.ShapiroWilk()
        resultado_esperado, conclusao_esperado = result.fit(self.x, conclusion='p-value')
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x, test="sw", conclusion='p-value')

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_normal_details_full(self):
        result = self.ShapiroWilk()
        resultado_esperado, conclusao_esperado = result.fit(self.x, details="full")
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x, test="sw", details="full")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_normal_details_full_conclusion_p_value(self):
        result = self.ShapiroWilk()
        resultado_esperado, conclusao_esperado = result.fit(self.x, details="full", conclusion="p-value")
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x, test="sw", details="full", conclusion="p-value")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_normal_alfa(self):
        result = self.ShapiroWilk()
        resultado_esperado, conclusao_esperado = result.fit(self.x, details="full", conclusion="p-value", alfa=0.10)
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x, test="sw", details="full", conclusion="p-value", alfa=0.10)

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_not_normal(self):
        result = self.ShapiroWilk()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal)
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal, test="sw")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")


    def test_pass_not_normal_conclusion_p_value(self):
        result = self.ShapiroWilk()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, conclusion="p-value")
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal, test="sw", conclusion="p-value")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_not_normal_details_full(self):
        result = self.ShapiroWilk()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full")
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal, test="sw", details="full")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_not_normal_details_full_conclusion_p_value(self):
        result = self.ShapiroWilk()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full", conclusion="p-value")
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal, test="sw", details="full", conclusion="p-value")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_alfa_not_normal(self):
        result = self.ShapiroWilk()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full", conclusion="p-value", alfa=0.10)
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal, test="sw", details="full", conclusion="p-value", alfa=0.10)

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

class Test_fit_am(unittest.TestCase):
    from pycafee.normalitycheck.abdimolin import AbdiMolin

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        cls.x_not_normal = np.array([1, 1, 1, 1.1, 1.2, 5.3, 10.1, 10.2, 10.3])

    def test_pass_normal(self):
        result = self.AbdiMolin()
        resultado_esperado, conclusao_esperado = result.fit(self.x)
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x, test="am")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_normal_conclusion_p_value(self):
        result = self.AbdiMolin()
        resultado_esperado, conclusao_esperado = result.fit(self.x)
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x, test="am", conclusion='p-value')

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_normal_details_full(self):
        result = self.AbdiMolin()
        resultado_esperado, conclusao_esperado = result.fit(self.x, details="full")
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x, test="am", details="full")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_normal_details_full_conclusion_p_value(self):
        result = self.AbdiMolin()
        resultado_esperado, conclusao_esperado = result.fit(self.x, details="full")
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x, test="am", details="full", conclusion="p-value")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_normal_alfa(self):
        result = self.AbdiMolin()
        resultado_esperado, conclusao_esperado = result.fit(self.x, details="full", alfa=0.10)
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x, test="am", details="full", alfa=0.10)

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_not_normal(self):
        result = self.AbdiMolin()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal)
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal, test="am")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")


    def test_pass_not_normal_conclusion_p_value(self):
        result = self.AbdiMolin()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal)
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal, test="am", conclusion="p-value")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_not_normal_details_full(self):
        result = self.AbdiMolin()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full")
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal, test="am", details="full")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_not_normal_details_full_conclusion_p_value(self):
        result = self.AbdiMolin()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full")
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal, test="am", details="full", conclusion="p-value")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_alfa_not_normal(self):
        result = self.AbdiMolin()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full", alfa=0.10)
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal, test="am", details="full", alfa=0.10)

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

class Test_fit_ad(unittest.TestCase):
    from pycafee.normalitycheck.andersondarling import AndersonDarling

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        cls.x_not_normal = np.array([1, 1, 1, 1.1, 1.2, 5.3, 10.1, 10.2, 10.3])

    def test_pass_normal(self):
        result = self.AndersonDarling()
        resultado_esperado, conclusao_esperado = result.fit(self.x)
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x, test="ad")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_normal_conclusion_p_value(self):
        result = self.AndersonDarling()
        resultado_esperado, conclusao_esperado = result.fit(self.x, conclusion='p-value')
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x, test="ad", conclusion='p-value')

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_normal_details_full(self):
        result = self.AndersonDarling()
        resultado_esperado, conclusao_esperado = result.fit(self.x, details="full")
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x, test="ad", details="full")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_normal_details_full_conclusion_p_value(self):
        result = self.AndersonDarling()
        resultado_esperado, conclusao_esperado = result.fit(self.x, details="full", conclusion="p-value")
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x, test="ad", details="full", conclusion="p-value")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_normal_alfa(self):
        result = self.AndersonDarling()
        resultado_esperado, conclusao_esperado = result.fit(self.x, details="full", alfa=0.10)
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x, test="ad", details="full", alfa=0.10)

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_not_normal(self):
        result = self.AndersonDarling()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal)
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal, test="ad")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")


    def test_pass_not_normal_conclusion_p_value(self):
        result = self.AndersonDarling()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, conclusion="p-value")
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal, test="ad", conclusion="p-value")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_not_normal_details_full(self):
        result = self.AndersonDarling()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full")
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal, test="ad", details="full")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_not_normal_details_full_conclusion_p_value(self):
        result = self.AndersonDarling()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full", conclusion="p-value")
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal, test="ad", details="full", conclusion="p-value")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_alfa_not_normal(self):
        result = self.AndersonDarling()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full", alfa=0.10)
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal, test="ad", details="full", alfa=0.10)

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

class Test_fit_ks(unittest.TestCase):
    from pycafee.normalitycheck.kolmogorovsmirnov import KolmogorovSmirnov
    @classmethod
    def setUpClass(cls):
        cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        cls.x_not_normal = np.array([1, 1, 1, 1.1, 1.2, 5.3, 10.1, 10.2, 10.3])


    def test_pass_normal(self):
        result = self.KolmogorovSmirnov()
        resultado_esperado, conclusao_esperado = result.fit(self.x)
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x, test="ks")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_normal_conclusion_p_value(self):
        result = self.KolmogorovSmirnov()
        resultado_esperado, conclusao_esperado = result.fit(self.x, conclusion='p-value')
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x, test="ks", conclusion='p-value')

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_normal_details_full(self):
        result = self.KolmogorovSmirnov()
        resultado_esperado, conclusao_esperado = result.fit(self.x, details="full")
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x, test="ks", details="full")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_normal_details_full_conclusion_p_value(self):
        result = self.KolmogorovSmirnov()
        resultado_esperado, conclusao_esperado = result.fit(self.x, details="full", conclusion="p-value")
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x, test="ks", details="full", conclusion="p-value")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_normal_alfa(self):
        result = self.KolmogorovSmirnov()
        resultado_esperado, conclusao_esperado = result.fit(self.x, details="full", alfa=0.10)
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x, test="ks", details="full", alfa=0.10)

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_not_normal(self):
        result = self.KolmogorovSmirnov()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal)
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal, test="ks")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")


    def test_pass_not_normal_conclusion_p_value(self):
        result = self.KolmogorovSmirnov()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, conclusion="p-value")
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal, test="ks", conclusion="p-value")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_not_normal_details_full(self):
        result = self.KolmogorovSmirnov()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full")
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal, test="ks", details="full")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_not_normal_details_full_conclusion_p_value(self):
        result = self.KolmogorovSmirnov()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full", conclusion="p-value")
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal, test="ks", details="full", conclusion="p-value")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_alfa_not_normal(self):
        result = self.KolmogorovSmirnov()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full", alfa=0.10)
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal, test="ks", details="full", alfa=0.10)

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

class Test_fit_ks(unittest.TestCase):
    from pycafee.normalitycheck.lilliefors import Lilliefors
    @classmethod
    def setUpClass(cls):
        cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        cls.x_not_normal = np.array([1, 1, 1, 1.1, 1.2, 5.3, 10.1, 10.2, 10.3])


    def test_pass_normal(self):
        result = self.Lilliefors()
        resultado_esperado, conclusao_esperado = result.fit(self.x)
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x, test="li")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_normal_conclusion_p_value(self):
        result = self.Lilliefors()
        resultado_esperado, conclusao_esperado = result.fit(self.x, conclusion='p-value')
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x, test="li", conclusion='p-value')

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_normal_details_full(self):
        result = self.Lilliefors()
        resultado_esperado, conclusao_esperado = result.fit(self.x, details="full")
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x, test="li", details="full")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_normal_details_full_conclusion_p_value(self):
        result = self.Lilliefors()
        resultado_esperado, conclusao_esperado = result.fit(self.x, details="full", conclusion="p-value")
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x, test="li", details="full", conclusion="p-value")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_normal_alfa(self):
        result = self.Lilliefors()
        resultado_esperado, conclusao_esperado = result.fit(self.x, details="full", alfa=0.10)
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x, test="li", details="full", alfa=0.10)

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_not_normal(self):
        result = self.Lilliefors()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal)
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal, test="li")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")


    def test_pass_not_normal_conclusion_p_value(self):
        result = self.Lilliefors()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, conclusion="p-value")
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal, test="li", conclusion="p-value")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_not_normal_details_full(self):
        result = self.Lilliefors()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full")
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal, test="li", details="full")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_not_normal_details_full_conclusion_p_value(self):
        result = self.Lilliefors()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full", conclusion="p-value")
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal, test="li", details="full", conclusion="p-value")

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")

    def test_pass_alfa_not_normal(self):
        result = self.Lilliefors()
        resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full", alfa=0.10)
        result = NormalityCheck()
        resultado, conclusao = result.fit(self.x_not_normal, test="li", details="full", alfa=0.10)

        self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
        self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
        self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
        self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
        self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")


# and now i understand the problems, you can see https://youtu.be/N26_hRITlsU?t=51

if __name__ == "__main__":
    unittest.main()
