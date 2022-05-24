"""Tests if the fit function for Sample is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_fit
    This class tests the fit function. It should raise ValueError when test gets the wrong key.


---> Classes Test_Normality_fit_default, Test_Normality_fit_sw, Test_Normality_fit_ab, Test_Normality_fit_ad, Test_Normality_fit_ks, Test_Normality_fit_li, tests the Normality test with every parameter by comparing with the original way to get the results.

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sample/test_fit.py
    or
    python -m unittest -b tests/sample/test_fit.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sample.sample import Sample
import numpy as np
import scipy.stats as stats
os.system('cls')


class Test_normal_like_stats(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4])
        cls.y = np.array([6.3, 5.8, 7.1, 6.3, 6.5, 7.6, 4.9, 7.3, 6.7, 7.2])

    def test_mean(self):
        amostra = Sample()
        amostra.fit(self.x)
        self.assertAlmostEqual(amostra.mean, self.x.mean(), msg="wrong mean")

        amostra = Sample()
        amostra.fit(self.y)
        self.assertAlmostEqual(amostra.mean, self.y.mean(), msg="wrong mean")

    def test_std(self):
        amostra = Sample()
        amostra.fit(self.x)
        self.assertAlmostEqual(amostra.std, self.x.std(ddof=1), msg="wrong std")

        amostra = Sample()
        amostra.fit(self.y)
        self.assertAlmostEqual(amostra.std, self.y.std(ddof=1), msg="wrong std")

    def test_variance(self):
        amostra = Sample()
        amostra.fit(self.x)
        self.assertAlmostEqual(amostra.variance, self.x.var(ddof=1), msg="wrong variance")

        amostra = Sample()
        amostra.fit(self.y)
        self.assertAlmostEqual(amostra.variance, self.y.var(ddof=1), msg="wrong variance")

    def test_cv(self):
        amostra = Sample()
        amostra.fit(self.x)
        self.assertAlmostEqual(amostra.cv, 100*self.x.std(ddof=1)/self.x.mean(), msg="wrong cv")

        amostra = Sample()
        amostra.fit(self.y)
        self.assertAlmostEqual(amostra.cv, 100*self.y.std(ddof=1)/self.y.mean(), msg="wrong cv")

    def test_t_student(self):
        amostra = Sample()
        amostra.fit(self.x)
        self.assertAlmostEqual(amostra.t_student, np.abs(stats.t.ppf(0.05/2, self.x.size - 1)), msg="wrong t_student")

        amostra = Sample()
        amostra.fit(self.y)
        self.assertAlmostEqual(amostra.t_student, np.abs(stats.t.ppf(0.05/2, self.y.size - 1)), msg="wrong t_student")

    def test_t_interval(self):
        amostra = Sample()
        amostra.fit(self.x)
        t = np.std(self.x,ddof=1)*stats.t.ppf(1-0.05/2, self.x.size-1)/np.sqrt(self.x.size)
        self.assertAlmostEqual(amostra.t_interval, t, msg="wrong t_interval")

        amostra = Sample()
        amostra.fit(self.y)
        t = np.std(self.y,ddof=1)*stats.t.ppf(1-0.05/2, self.y.size-1)/np.sqrt(self.y.size)
        self.assertAlmostEqual(amostra.t_interval, t, msg="wrong t_interval")



class Test_non_normal_like_stats(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4])
        cls.y = np.array([6.3, 5.8, 7.1, 6.3, 6.5, 7.6, 4.9, 7.3, 6.7, 7.2])

    def test_median(self):
        amostra = Sample()
        amostra.fit(self.x)
        self.assertAlmostEqual(amostra.median, np.median(self.x), msg="wrong median")

        amostra = Sample()
        amostra.fit(self.y)
        self.assertAlmostEqual(amostra.median, np.median(self.y), msg="wrong median")

    def test_min(self):
        amostra = Sample()
        amostra.fit(self.x)
        self.assertAlmostEqual(amostra.min, np.min(self.x), msg="wrong min")

        amostra = Sample()
        amostra.fit(self.y)
        self.assertAlmostEqual(amostra.min, np.min(self.y), msg="wrong min")

    def test_max(self):
        amostra = Sample()
        amostra.fit(self.x)
        self.assertAlmostEqual(amostra.max, np.max(self.x), msg="wrong max")

        amostra = Sample()
        amostra.fit(self.y)
        self.assertAlmostEqual(amostra.max, np.max(self.y), msg="wrong max")

    def test_Q1(self):
        amostra = Sample()
        amostra.fit(self.x)
        self.assertAlmostEqual(amostra.Q1, np.quantile(self.x, 0.25, interpolation="linear"), msg="wrong Q1")

        amostra = Sample()
        amostra.fit(self.y)
        self.assertAlmostEqual(amostra.Q1, np.quantile(self.y, 0.25, interpolation="linear"), msg="wrong Q1")

    def test_Q3(self):
        amostra = Sample()
        amostra.fit(self.x)
        self.assertAlmostEqual(amostra.Q3, np.quantile(self.x, 0.75, interpolation="linear"), msg="wrong Q3")

        amostra = Sample()
        amostra.fit(self.y)
        self.assertAlmostEqual(amostra.Q3, np.quantile(self.y, 0.75, interpolation="linear"), msg="wrong Q3")


    def test_DI(self):
        amostra = Sample()
        amostra.fit(self.x)
        self.assertAlmostEqual(amostra.DI, np.quantile(self.x, 0.75, interpolation="linear") - np.quantile(self.x, 0.25, interpolation="linear"), msg="wrong DI")

        amostra = Sample()
        amostra.fit(self.y)
        self.assertAlmostEqual(amostra.DI, np.quantile(self.y, 0.75, interpolation="linear") - np.quantile(self.y, 0.25, interpolation="linear"), msg="wrong DI")

    def test_mode(self):
        amostra = Sample()
        amostra.fit(self.x)
        self.assertDictEqual(amostra.mode, {4.6: 2, 5.0: 2}, msg="wrong mode")

        amostra = Sample()
        amostra.fit(self.y)
        self.assertDictEqual(amostra.mode, {6.3: 2}, msg="wrong mode")


# class Test_Normality(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
#         cls.x_not_normal = np.array([1, 1, 1, 1.1, 1.2, 5.3, 10.1, 10.2, 10.3])
#
#     def test_norm_test_names(self):
#         with self.assertRaises(ValueError, msg="Does not raised error when norm_test is not valid"):
#             amostra = Sample()
#             amostra.fit(self.x, norm_test="any")
#
#         with self.assertRaises(ValueError, msg="Does not raised error when norm_test is not valid"):
#             amostra = Sample()
#             amostra.fit(self.x, norm_test="anderson")
#
#         with self.assertRaises(ValueError, msg="Does not raised error when norm_test is not valid"):
#             amostra = Sample()
#             amostra.fit(self.x, norm_test="shapiro")
#
#         with self.assertRaises(ValueError, msg="Does not raised error when norm_test is not valid"):
#             amostra = Sample()
#             amostra.fit(self.x, norm_test="abid-molin")
#
# class Test_Normality_fit_default(unittest.TestCase):
#     from pycafee.normalitycheck.shapirowilk import ShapiroWilk
#
#     @classmethod
#     def setUpClass(cls):
#         cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
#         cls.x_not_normal = np.array([1, 1, 1, 1.1, 1.2, 5.3, 10.1, 10.2, 10.3])
#
#     def test_pass_normal(self):
#         result = self.ShapiroWilk()
#         resultado_esperado, conclusao_esperado = result.fit(self.x)
#         amostra = Sample()
#         amostra.fit(self.x)
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_normal_conclusion_p_value(self):
#         result = self.ShapiroWilk()
#         resultado_esperado, conclusao_esperado = result.fit(self.x, conclusion='p-value')
#         amostra = Sample()
#         amostra.fit(self.x, conclusion='p-value')
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_normal_details_full(self):
#         result = self.ShapiroWilk()
#         resultado_esperado, conclusao_esperado = result.fit(self.x, details="full")
#         amostra = Sample()
#         amostra.fit(self.x, details="full")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_normal_details_full_conclusion_p_value(self):
#         result = self.ShapiroWilk()
#         resultado_esperado, conclusao_esperado = result.fit(self.x, details="full", conclusion="p-value")
#         amostra = Sample()
#         amostra.fit(self.x, details="full", conclusion="p-value")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_normal_alfa(self):
#         result = self.ShapiroWilk()
#         resultado_esperado, conclusao_esperado = result.fit(self.x, details="full", conclusion="p-value", alfa=0.10)
#         amostra = Sample()
#         amostra.fit(self.x, details="full", conclusion="p-value", alfa=0.10)
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_not_normal(self):
#         result = self.ShapiroWilk()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal)
#         amostra = Sample()
#         amostra.fit(self.x_not_normal)
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#
#     def test_pass_not_normal_conclusion_p_value(self):
#         result = self.ShapiroWilk()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, conclusion="p-value")
#         amostra = Sample()
#         amostra.fit(self.x_not_normal, conclusion="p-value")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_not_normal_details_full(self):
#         result = self.ShapiroWilk()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full")
#         amostra = Sample()
#         amostra.fit(self.x_not_normal, details="full")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_not_normal_details_full_conclusion_p_value(self):
#         result = self.ShapiroWilk()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full", conclusion="p-value")
#         amostra = Sample()
#         amostra.fit(self.x_not_normal, details="full", conclusion="p-value")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_alfa_not_normal(self):
#         result = self.ShapiroWilk()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full", conclusion="p-value", alfa=0.10)
#         amostra = Sample()
#         amostra.fit(self.x_not_normal, details="full", conclusion="p-value", alfa=0.10)
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
# class Test_Normality_fit_sw(unittest.TestCase):
#     from pycafee.normalitycheck.shapirowilk import ShapiroWilk
#
#     @classmethod
#     def setUpClass(cls):
#         cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
#         cls.x_not_normal = np.array([1, 1, 1, 1.1, 1.2, 5.3, 10.1, 10.2, 10.3])
#
#     def test_pass_normal(self):
#         result = self.ShapiroWilk()
#         resultado_esperado, conclusao_esperado = result.fit(self.x)
#         amostra = Sample()
#         amostra.fit(self.x, norm_test="sw")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_normal_conclusion_p_value(self):
#         result = self.ShapiroWilk()
#         resultado_esperado, conclusao_esperado = result.fit(self.x, conclusion='p-value')
#         amostra = Sample()
#         amostra.fit(self.x, norm_test="sw", conclusion='p-value')
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_normal_details_full(self):
#         result = self.ShapiroWilk()
#         resultado_esperado, conclusao_esperado = result.fit(self.x, details="full")
#         amostra = Sample()
#         amostra.fit(self.x, norm_test="sw", details="full")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_normal_details_full_conclusion_p_value(self):
#         result = self.ShapiroWilk()
#         resultado_esperado, conclusao_esperado = result.fit(self.x, details="full", conclusion="p-value")
#         amostra = Sample()
#         amostra.fit(self.x, norm_test="sw", details="full", conclusion="p-value")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_normal_alfa(self):
#         result = self.ShapiroWilk()
#         resultado_esperado, conclusao_esperado = result.fit(self.x, details="full", conclusion="p-value", alfa=0.10)
#         amostra = Sample()
#         amostra.fit(self.x, norm_test="sw", details="full", conclusion="p-value", alfa=0.10)
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_not_normal(self):
#         result = self.ShapiroWilk()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal)
#         amostra = Sample()
#         amostra.fit(self.x_not_normal, norm_test="sw")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#
#     def test_pass_not_normal_conclusion_p_value(self):
#         result = self.ShapiroWilk()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, conclusion="p-value")
#         amostra = Sample()
#         amostra.fit(self.x_not_normal, norm_test="sw", conclusion="p-value")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_not_normal_details_full(self):
#         result = self.ShapiroWilk()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full")
#         amostra = Sample()
#         amostra.fit(self.x_not_normal, norm_test="sw", details="full")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_not_normal_details_full_conclusion_p_value(self):
#         result = self.ShapiroWilk()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full", conclusion="p-value")
#         amostra = Sample()
#         amostra.fit(self.x_not_normal, norm_test="sw", details="full", conclusion="p-value")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_alfa_not_normal(self):
#         result = self.ShapiroWilk()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full", conclusion="p-value", alfa=0.10)
#         amostra = Sample()
#         amostra.fit(self.x_not_normal, norm_test="sw", details="full", conclusion="p-value", alfa=0.10)
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
# class Test_Normality_fit_am(unittest.TestCase):
#     from pycafee.normalitycheck.abdimolin import AbdiMolin
#
#     @classmethod
#     def setUpClass(cls):
#         cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
#         cls.x_not_normal = np.array([1, 1, 1, 1.1, 1.2, 5.3, 10.1, 10.2, 10.3])
#
#     def test_pass_normal(self):
#         result = self.AbdiMolin()
#         resultado_esperado, conclusao_esperado = result.fit(self.x)
#         amostra = Sample()
#         amostra.fit(self.x, norm_test="am")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_normal_conclusion_p_value(self):
#         result = self.AbdiMolin()
#         resultado_esperado, conclusao_esperado = result.fit(self.x)
#         amostra = Sample()
#         amostra.fit(self.x, norm_test="am", conclusion='p-value')
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_normal_details_full(self):
#         result = self.AbdiMolin()
#         resultado_esperado, conclusao_esperado = result.fit(self.x, details="full")
#         amostra = Sample()
#         amostra.fit(self.x, norm_test="am", details="full")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_normal_details_full_conclusion_p_value(self):
#         result = self.AbdiMolin()
#         resultado_esperado, conclusao_esperado = result.fit(self.x, details="full")
#         amostra = Sample()
#         amostra.fit(self.x, norm_test="am", details="full", conclusion="p-value")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_normal_alfa(self):
#         result = self.AbdiMolin()
#         resultado_esperado, conclusao_esperado = result.fit(self.x, details="full", alfa=0.10)
#         amostra = Sample()
#         amostra.fit(self.x, norm_test="am", details="full", alfa=0.10)
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_not_normal(self):
#         result = self.AbdiMolin()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal)
#         amostra = Sample()
#         amostra.fit(self.x_not_normal, norm_test="am")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#
#     def test_pass_not_normal_conclusion_p_value(self):
#         result = self.AbdiMolin()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal)
#         amostra = Sample()
#         amostra.fit(self.x_not_normal, norm_test="am", conclusion="p-value")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_not_normal_details_full(self):
#         result = self.AbdiMolin()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full")
#         amostra = Sample()
#         amostra.fit(self.x_not_normal, norm_test="am", details="full")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_not_normal_details_full_conclusion_p_value(self):
#         result = self.AbdiMolin()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full")
#         amostra = Sample()
#         amostra.fit(self.x_not_normal, norm_test="am", details="full", conclusion="p-value")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_alfa_not_normal(self):
#         result = self.AbdiMolin()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full", alfa=0.10)
#         amostra = Sample()
#         amostra.fit(self.x_not_normal, norm_test="am", details="full", alfa=0.10)
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
# class Test_Normality_fit_ad(unittest.TestCase):
#     from pycafee.normalitycheck.andersondarling import AndersonDarling
#
#     @classmethod
#     def setUpClass(cls):
#         cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
#         cls.x_not_normal = np.array([1, 1, 1, 1.1, 1.2, 5.3, 10.1, 10.2, 10.3])
#
#     def test_pass_normal(self):
#         result = self.AndersonDarling()
#         resultado_esperado, conclusao_esperado = result.fit(self.x)
#         amostra = Sample()
#         amostra.fit(self.x, norm_test="ad")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_normal_conclusion_p_value(self):
#         result = self.AndersonDarling()
#         resultado_esperado, conclusao_esperado = result.fit(self.x, conclusion='p-value')
#         amostra = Sample()
#         amostra.fit(self.x, norm_test="ad", conclusion='p-value')
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_normal_details_full(self):
#         result = self.AndersonDarling()
#         resultado_esperado, conclusao_esperado = result.fit(self.x, details="full")
#         amostra = Sample()
#         amostra.fit(self.x, norm_test="ad", details="full")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_normal_details_full_conclusion_p_value(self):
#         result = self.AndersonDarling()
#         resultado_esperado, conclusao_esperado = result.fit(self.x, details="full", conclusion="p-value")
#         amostra = Sample()
#         amostra.fit(self.x, norm_test="ad", details="full", conclusion="p-value")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_normal_alfa(self):
#         result = self.AndersonDarling()
#         resultado_esperado, conclusao_esperado = result.fit(self.x, details="full", alfa=0.10)
#         amostra = Sample()
#         amostra.fit(self.x, norm_test="ad", details="full", alfa=0.10)
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_not_normal(self):
#         result = self.AndersonDarling()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal)
#         amostra = Sample()
#         amostra.fit(self.x_not_normal, norm_test="ad")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#
#     def test_pass_not_normal_conclusion_p_value(self):
#         result = self.AndersonDarling()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, conclusion="p-value")
#         amostra = Sample()
#         amostra.fit(self.x_not_normal, norm_test="ad", conclusion="p-value")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_not_normal_details_full(self):
#         result = self.AndersonDarling()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full")
#         amostra = Sample()
#         amostra.fit(self.x_not_normal, norm_test="ad", details="full")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_not_normal_details_full_conclusion_p_value(self):
#         result = self.AndersonDarling()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full", conclusion="p-value")
#         amostra = Sample()
#         amostra.fit(self.x_not_normal, norm_test="ad", details="full", conclusion="p-value")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_alfa_not_normal(self):
#         result = self.AndersonDarling()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full", alfa=0.10)
#         amostra = Sample()
#         amostra.fit(self.x_not_normal, norm_test="ad", details="full", alfa=0.10)
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
# class Test_Normality_fit_ks(unittest.TestCase):
#     from pycafee.normalitycheck.kolmogorovsmirnov import KolmogorovSmirnov
#     @classmethod
#     def setUpClass(cls):
#         cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
#         cls.x_not_normal = np.array([1, 1, 1, 1.1, 1.2, 5.3, 10.1, 10.2, 10.3])
#
#
#     def test_pass_normal(self):
#         result = self.KolmogorovSmirnov()
#         resultado_esperado, conclusao_esperado = result.fit(self.x)
#         amostra = Sample()
#         amostra.fit(self.x, norm_test="ks")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_normal_conclusion_p_value(self):
#         result = self.KolmogorovSmirnov()
#         resultado_esperado, conclusao_esperado = result.fit(self.x, conclusion='p-value')
#         amostra = Sample()
#         amostra.fit(self.x, norm_test="ks", conclusion='p-value')
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_normal_details_full(self):
#         result = self.KolmogorovSmirnov()
#         resultado_esperado, conclusao_esperado = result.fit(self.x, details="full")
#         amostra = Sample()
#         amostra.fit(self.x, norm_test="ks", details="full")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_normal_details_full_conclusion_p_value(self):
#         result = self.KolmogorovSmirnov()
#         resultado_esperado, conclusao_esperado = result.fit(self.x, details="full", conclusion="p-value")
#         amostra = Sample()
#         amostra.fit(self.x, norm_test="ks", details="full", conclusion="p-value")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_normal_alfa(self):
#         result = self.KolmogorovSmirnov()
#         resultado_esperado, conclusao_esperado = result.fit(self.x, details="full", alfa=0.10)
#         amostra = Sample()
#         amostra.fit(self.x, norm_test="ks", details="full", alfa=0.10)
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_not_normal(self):
#         result = self.KolmogorovSmirnov()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal)
#         amostra = Sample()
#         amostra.fit(self.x_not_normal, norm_test="ks")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#
#     def test_pass_not_normal_conclusion_p_value(self):
#         result = self.KolmogorovSmirnov()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, conclusion="p-value")
#         amostra = Sample()
#         amostra.fit(self.x_not_normal, norm_test="ks", conclusion="p-value")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_not_normal_details_full(self):
#         result = self.KolmogorovSmirnov()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full")
#         amostra = Sample()
#         amostra.fit(self.x_not_normal, norm_test="ks", details="full")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_not_normal_details_full_conclusion_p_value(self):
#         result = self.KolmogorovSmirnov()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full", conclusion="p-value")
#         amostra = Sample()
#         amostra.fit(self.x_not_normal, norm_test="ks", details="full", conclusion="p-value")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_alfa_not_normal(self):
#         result = self.KolmogorovSmirnov()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full", alfa=0.10)
#         amostra = Sample()
#         amostra.fit(self.x_not_normal, norm_test="ks", details="full", alfa=0.10)
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
# class Test_Normality_fit_ks(unittest.TestCase):
#     from pycafee.normalitycheck.lilliefors import Lilliefors
#     @classmethod
#     def setUpClass(cls):
#         cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
#         cls.x_not_normal = np.array([1, 1, 1, 1.1, 1.2, 5.3, 10.1, 10.2, 10.3])
#
#
#     def test_pass_normal(self):
#         result = self.Lilliefors()
#         resultado_esperado, conclusao_esperado = result.fit(self.x)
#         amostra = Sample()
#         amostra.fit(self.x, norm_test="li")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_normal_conclusion_p_value(self):
#         result = self.Lilliefors()
#         resultado_esperado, conclusao_esperado = result.fit(self.x, conclusion='p-value')
#         amostra = Sample()
#         amostra.fit(self.x, norm_test="li", conclusion='p-value')
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_normal_details_full(self):
#         result = self.Lilliefors()
#         resultado_esperado, conclusao_esperado = result.fit(self.x, details="full")
#         amostra = Sample()
#         amostra.fit(self.x, norm_test="li", details="full")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_normal_details_full_conclusion_p_value(self):
#         result = self.Lilliefors()
#         resultado_esperado, conclusao_esperado = result.fit(self.x, details="full", conclusion="p-value")
#         amostra = Sample()
#         amostra.fit(self.x, norm_test="li", details="full", conclusion="p-value")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_normal_alfa(self):
#         result = self.Lilliefors()
#         resultado_esperado, conclusao_esperado = result.fit(self.x, details="full", alfa=0.10)
#         amostra = Sample()
#         amostra.fit(self.x, norm_test="li", details="full", alfa=0.10)
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_not_normal(self):
#         result = self.Lilliefors()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal)
#         amostra = Sample()
#         amostra.fit(self.x_not_normal, norm_test="li")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#
#     def test_pass_not_normal_conclusion_p_value(self):
#         result = self.Lilliefors()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, conclusion="p-value")
#         amostra = Sample()
#         amostra.fit(self.x_not_normal, norm_test="li", conclusion="p-value")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_not_normal_details_full(self):
#         result = self.Lilliefors()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full")
#         amostra = Sample()
#         amostra.fit(self.x_not_normal, norm_test="li", details="full")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_not_normal_details_full_conclusion_p_value(self):
#         result = self.Lilliefors()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full", conclusion="p-value")
#         amostra = Sample()
#         amostra.fit(self.x_not_normal, norm_test="li", details="full", conclusion="p-value")
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")
#
#     def test_pass_alfa_not_normal(self):
#         result = self.Lilliefors()
#         resultado_esperado, conclusao_esperado = result.fit(self.x_not_normal, details="full", alfa=0.10)
#         amostra = Sample()
#         amostra.fit(self.x_not_normal, norm_test="li", details="full", alfa=0.10)
#         resultado = amostra.normality_result
#         conclusao = amostra.normality_conclusion
#
#         self.assertEqual(resultado_esperado[0], resultado[0], "statistic does not match")
#         self.assertEqual(resultado_esperado[1], resultado[1], "critical value does not match")
#         self.assertEqual(resultado_esperado[2], resultado[2], "p dos not match")
#         self.assertEqual(resultado_esperado[3], resultado[3], "alfa does not match")
#         self.assertEqual(conclusao_esperado, conclusao, "conclusion does not match")


# and now i understand the problems, you can see https://youtu.be/N26_hRITlsU?t=51

if __name__ == "__main__":
    unittest.main()
