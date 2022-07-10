"""Tests if the test_fit is working as expected

---> Class Test_ratio_None: Esta classe verifica se os resultados são esperados para as 4 possibilidades de n, para lower e upper, alem de verificar o parametro details e alfa. Também é verificado os resultados com as funções r10. Foi adicionado resultados para quando temos outleir inferior e superior em todas as possibilidades de ratio

---> Class Test_ratio_XX : estas classes testam o parametro ratio individualmente em todas as possbilidades, incluindo dados com outliers inferior e superior, além de dados sem outliers.

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sample/outliers/Dixon/test_fit.py
    or
    python -m unittest -b tests/sample/outliers/Dixon/test_fit.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sample.outliers import Dixon
import numpy as np
os.system('cls')


class Test_ratio_22(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.x = np.array([15.52, 15.53, 15.53, 15.54, 15.56, 15.56]) # sem outliers
        cls.y = np.array([15.52, 15.53, 15.53, 15.54, 15.56, 15.56, 15.68]) # valor superior outlier
        cls.z = np.array([15.42, 15.51, 15.52, 15.52, 15.53, 15.53, 15.54]) # valor inferior outlier


    def test_outlier_lower(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.z, ratio="r22", which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.5, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.909, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r22", msg="wrong ratio")
        result = False
        if "The data does not have outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.z, ratio="r22", which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.909090909, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.909, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r22", msg="wrong ratio")
        result = False
        if "O valor inferior (15.42) talvez seja um outlier (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Dixon()
        result, conclusion = teste.fit(self.z, ratio="r22", details='full', which="max")
        self.assertAlmostEqual(result[0], 0.5, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.909, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r22", msg="wrong ratio")
        result = False
        if "Since the test statistic value (0.5) is lower than the critical value (0.909), we have no evidence to reject the null hypothesis that the sample does not contain outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.z, ratio="r22", details="full", which="min")
        self.assertAlmostEqual(result[0], 0.909090909, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.909, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r22", msg="wrong ratio")
        result = False
        if "Como o valor da estatistica do teste (0.909) é maior do que o valor crítico (0.909), temos evidências para rejeitar a hipótese nula de que a amostra não contém outliers, e talvez o valor inferior (15.42) seja um outlier (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon()
        result, conclusion = teste.fit(self.z, ratio="r22", details='binary', which="max")
        self.assertAlmostEqual(result[0], 0.5, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.909, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r22", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.z, ratio="r22", details="binary", which="min")
        self.assertAlmostEqual(result[0], 0.909090909, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.909, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r22", msg="wrong ratio")
        self.assertEqual(conclusion, 1, msg="wrong conclusion")


    def test_outlier_upper(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.y, ratio="r22", which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.8, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.909, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r22", msg="wrong ratio")
        result = False
        if "The data does not have outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.y, ratio="r22", which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.25, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.909, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r22", msg="wrong ratio")
        result = False
        if "Os dados não apresentam outliers (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Dixon()
        result, conclusion = teste.fit(self.y, ratio="r22", details='full', which="max")
        self.assertAlmostEqual(result[0], 0.8, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.909, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r22", msg="wrong ratio")
        result = False
        if "Since the test statistic value (0.799) is lower than the critical value (0.909), we have no evidence to reject the null hypothesis that the sample does not contain outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.y, ratio="r22", details="full", which="min")
        self.assertAlmostEqual(result[0], 0.25, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.909, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r22", msg="wrong ratio")
        result = False
        if "Como o valor da estatistica do teste (0.249) é menor do que o valor crítico (0.909), não temos evidências para rejeitar a hipótese nula de que a amostra não contém outliers (com 95.0% de confiança)." in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon()
        result, conclusion = teste.fit(self.y, ratio="r22", details='binary', which="max")
        self.assertAlmostEqual(result[0], 0.8, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.909, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r22", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.y, ratio="r22", details="binary", which="min")
        self.assertAlmostEqual(result[0], 0.25, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.909, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r22", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")


    def test_no_outlier(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.x, ratio="r22", which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.666666667, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.990, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r22", msg="wrong ratio")
        result = False
        if "The data does not have outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.x, ratio="r22", which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.5, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.990, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r22", msg="wrong ratio")
        result = False
        if "Os dados não apresentam outliers (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Dixon()
        result, conclusion = teste.fit(self.x, ratio="r22", details='full', which="max")
        self.assertAlmostEqual(result[0], 0.666666667, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.990, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r22", msg="wrong ratio")
        result = False
        if "Since the test statistic value (0.666) is lower than the critical value (0.99), we have no evidence to reject the null hypothesis that the sample does not contain outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.x, ratio="r22", details="full", which="min")
        self.assertAlmostEqual(result[0], 0.5, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.990, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r22", msg="wrong ratio")
        result = False
        if "Como o valor da estatistica do teste (0.5) é menor do que o valor crítico (0.99), não temos evidências para rejeitar a hipótese nula de que a amostra não contém outliers (com 95.0% de confiança)." in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon()
        result, conclusion = teste.fit(self.x, ratio="r22", details='binary', which="max")
        self.assertAlmostEqual(result[0], 0.666666667, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.990, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r22", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.x, ratio="r22", details="binary", which="min")
        self.assertAlmostEqual(result[0], 0.5, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.990, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r22", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")



class Test_ratio_21(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.x = np.array([15.52, 15.53, 15.53, 15.54, 15.56, 15.56]) # sem outliers
        cls.y = np.array([15.52, 15.53, 15.53, 15.54, 15.56, 15.56, 15.68]) # valor superior outlier
        cls.z = np.array([15.42, 15.51, 15.52, 15.52, 15.53, 15.53, 15.54]) # valor inferior outlier


    def test_outlier_lower(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.z, ratio="r21", which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.333333333, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.828, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r21", msg="wrong ratio")
        result = False
        if "The data does not have outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.z, ratio="r21", which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.909090909, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.828, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r21", msg="wrong ratio")
        result = False
        if "O valor inferior (15.42) talvez seja um outlier (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Dixon()
        result, conclusion = teste.fit(self.z, ratio="r21", details='full', which="max")
        self.assertAlmostEqual(result[0], 0.333333333, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.828, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r21", msg="wrong ratio")
        result = False
        if "Since the test statistic value (0.333) is lower than the critical value (0.828), we have no evidence to reject the null hypothesis that the sample does not contain outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.z, ratio="r21", details="full", which="min")
        self.assertAlmostEqual(result[0], 0.909090909, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.828, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r21", msg="wrong ratio")
        result = False
        if "Como o valor da estatistica do teste (0.909) é maior do que o valor crítico (0.828), temos evidências para rejeitar a hipótese nula de que a amostra não contém outliers, e talvez o valor inferior (15.42) seja um outlier (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon()
        result, conclusion = teste.fit(self.z, ratio="r21", details='binary', which="max")
        self.assertAlmostEqual(result[0], 0.333333333, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.828, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r21", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.z, ratio="r21", details="binary", which="min")
        self.assertAlmostEqual(result[0], 0.909090909, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.828, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r21", msg="wrong ratio")
        self.assertEqual(conclusion, 1, msg="wrong conclusion")


    def test_outlier_upper(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.y, ratio="r21", which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.8, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.828, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r21", msg="wrong ratio")
        result = False
        if "The data does not have outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.y, ratio="r21", which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.25, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.828, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r21", msg="wrong ratio")
        result = False
        if "Os dados não apresentam outliers (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Dixon()
        result, conclusion = teste.fit(self.y, ratio="r21", details='full', which="max")
        self.assertAlmostEqual(result[0], 0.8, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.828, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r21", msg="wrong ratio")
        result = False
        if "Since the test statistic value (0.799) is lower than the critical value (0.828), we have no evidence to reject the null hypothesis that the sample does not contain outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.y, ratio="r21", details="full", which="min")
        self.assertAlmostEqual(result[0], 0.25, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.828, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r21", msg="wrong ratio")
        result = False
        if "Como o valor da estatistica do teste (0.249) é menor do que o valor crítico (0.828), não temos evidências para rejeitar a hipótese nula de que a amostra não contém outliers (com 95.0% de confiança)." in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon()
        result, conclusion = teste.fit(self.y, ratio="r21", details='binary', which="max")
        self.assertAlmostEqual(result[0], 0.8, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.828, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r21", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.y, ratio="r21", details="binary", which="min")
        self.assertAlmostEqual(result[0], 0.25, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.828, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r21", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")


    def test_no_outlier(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.x, ratio="r21", which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.666666667, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.913, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r21", msg="wrong ratio")
        result = False
        if "The data does not have outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.x, ratio="r21", which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.25, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.913, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r21", msg="wrong ratio")
        result = False
        if "Os dados não apresentam outliers (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Dixon()
        result, conclusion = teste.fit(self.x, ratio="r21", details='full', which="max")
        self.assertAlmostEqual(result[0], 0.666666667, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.913, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r21", msg="wrong ratio")
        result = False
        if "Since the test statistic value (0.666) is lower than the critical value (0.913), we have no evidence to reject the null hypothesis that the sample does not contain outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.x, ratio="r21", details="full", which="min")
        self.assertAlmostEqual(result[0], 0.25, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.913, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r21", msg="wrong ratio")
        result = False
        if "Como o valor da estatistica do teste (0.249) é menor do que o valor crítico (0.913), não temos evidências para rejeitar a hipótese nula de que a amostra não contém outliers (com 95.0% de confiança)." in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon()
        result, conclusion = teste.fit(self.x, ratio="r21", details='binary', which="max")
        self.assertAlmostEqual(result[0], 0.666666667, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.913, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r21", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.x, ratio="r21", details="binary", which="min")
        self.assertAlmostEqual(result[0], 0.25, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.913, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r21", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")



class Test_ratio_20(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.x = np.array([15.52, 15.53, 15.53, 15.54, 15.56, 15.56]) # sem outliers
        cls.y = np.array([15.52, 15.53, 15.53, 15.54, 15.56, 15.56, 15.68]) # valor superior outlier
        cls.z = np.array([15.42, 15.51, 15.52, 15.52, 15.53, 15.53, 15.54]) # valor inferior outlier


    def test_outlier_lower(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.z, ratio="r20", which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.083333333, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.716, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r20", msg="wrong ratio")
        result = False
        if "The data does not have outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.z, ratio="r20", which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.833333333, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.716, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r20", msg="wrong ratio")
        result = False
        if "O valor inferior (15.42) talvez seja um outlier (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Dixon()
        result, conclusion = teste.fit(self.z, ratio="r20", details='full', which="max")
        self.assertAlmostEqual(result[0], 0.083333333, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.716, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r20", msg="wrong ratio")
        result = False
        if "Since the test statistic value (0.083) is lower than the critical value (0.716), we have no evidence to reject the null hypothesis that the sample does not contain outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.z, ratio="r20", details="full", which="min")
        self.assertAlmostEqual(result[0], 0.833333333, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.716, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r20", msg="wrong ratio")
        result = False
        if "Como o valor da estatistica do teste (0.833) é maior do que o valor crítico (0.716), temos evidências para rejeitar a hipótese nula de que a amostra não contém outliers, e talvez o valor inferior (15.42) seja um outlier (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon()
        result, conclusion = teste.fit(self.z, ratio="r20", details='binary', which="max")
        self.assertAlmostEqual(result[0], 0.083333333, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.716, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r20", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.z, ratio="r20", details="binary", which="min")
        self.assertAlmostEqual(result[0], 0.833333333, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.716, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r20", msg="wrong ratio")
        self.assertEqual(conclusion, 1, msg="wrong conclusion")


    def test_outlier_upper(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.y, ratio="r20", which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.75, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.716, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r20", msg="wrong ratio")
        result = False

        if "The upper value (15.68) perhaps be an outlier (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.y, ratio="r20", which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.0625, places=3, msg="wrong statistic value")
        self.assertEqual(result[1], 0.716, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r20", msg="wrong ratio")
        result = False
        if "Os dados não apresentam outliers (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Dixon()
        result, conclusion = teste.fit(self.y, ratio="r20", details='full', which="max")
        self.assertAlmostEqual(result[0], 0.75, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.716, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r20", msg="wrong ratio")
        result = False
        if "Since the test statistic value (0.749) is higher than the critical value (0.716), we have evidence to reject the null hypothesis that the sample does not contain outliers, and perhaps the upper value (15.68) is an outlier (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.y, ratio="r20", details="full", which="min")
        self.assertAlmostEqual(result[0], 0.0625, places=3, msg="wrong statistic value")
        self.assertEqual(result[1], 0.716, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r20", msg="wrong ratio")
        result = False
        if "Como o valor da estatistica do teste (0.062) é menor do que o valor crítico (0.716), não temos evidências para rejeitar a hipótese nula de que a amostra não contém outliers (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon()
        result, conclusion = teste.fit(self.y, ratio="r20", details='binary', which="max")
        self.assertAlmostEqual(result[0], 0.75, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.716, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r20", msg="wrong ratio")
        self.assertEqual(conclusion, 1, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.y, ratio="r20", details="binary", which="min")
        self.assertAlmostEqual(result[0], 0.0625, places=3, msg="wrong statistic value")
        self.assertEqual(result[1], 0.716, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r20", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")


    def test_no_outlier(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.x, ratio="r20", which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.5, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.786, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r20", msg="wrong ratio")
        result = False
        if "The data does not have outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.x, ratio="r20", which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.25, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.786, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r20", msg="wrong ratio")
        result = False
        if "Os dados não apresentam outliers (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Dixon()
        result, conclusion = teste.fit(self.x, ratio="r20", details='full', which="max")
        self.assertAlmostEqual(result[0], 0.5, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.786, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r20", msg="wrong ratio")
        result = False
        if "Since the test statistic value (0.5) is lower than the critical value (0.786), we have no evidence to reject the null hypothesis that the sample does not contain outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.x, ratio="r20", details="full", which="min")
        self.assertAlmostEqual(result[0], 0.25, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.786, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r20", msg="wrong ratio")
        result = False
        if "Como o valor da estatistica do teste (0.249) é menor do que o valor crítico (0.786), não temos evidências para rejeitar a hipótese nula de que a amostra não contém outliers (com 95.0% de confiança)." in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon()
        result, conclusion = teste.fit(self.x, ratio="r20", details='binary', which="max")
        self.assertAlmostEqual(result[0], 0.5, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.786, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r20", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.x, ratio="r20", details="binary", which="min")
        self.assertAlmostEqual(result[0], 0.25, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.786, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r20", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")



class Test_ratio_12(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.x = np.array([15.52, 15.53, 15.53, 15.54, 15.56, 15.56]) # sem outliers
        cls.y = np.array([15.52, 15.53, 15.53, 15.54, 15.56, 15.56, 15.68]) # valor superior outlier
        cls.z = np.array([15.42, 15.51, 15.52, 15.52, 15.53, 15.53, 15.54]) # valor inferior outlier


    def test_outlier_lower(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.z, ratio="r12", which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.5, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.773, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r12", msg="wrong ratio")
        result = False
        if "The data does not have outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.z, ratio="r12", which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.818181818, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.773, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r12", msg="wrong ratio")
        result = False
        if "O valor inferior (15.42) talvez seja um outlier (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Dixon()
        result, conclusion = teste.fit(self.z, ratio="r12", details='full', which="max")
        self.assertAlmostEqual(result[0], 0.5, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.773, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r12", msg="wrong ratio")
        result = False
        if "Since the test statistic value (0.5) is lower than the critical value (0.773), we have no evidence to reject the null hypothesis that the sample does not contain outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.z, ratio="r12", details="full", which="min")
        self.assertAlmostEqual(result[0], 0.818181818, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.773, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r12", msg="wrong ratio")
        result = False
        if "Como o valor da estatistica do teste (0.818) é maior do que o valor crítico (0.773), temos evidências para rejeitar a hipótese nula de que a amostra não contém outliers, e talvez o valor inferior (15.42) seja um outlier (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon()
        result, conclusion = teste.fit(self.z, ratio="r12", details='binary', which="max")
        self.assertAlmostEqual(result[0], 0.5, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.773, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r12", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.z, ratio="r12", details="binary", which="min")
        self.assertAlmostEqual(result[0], 0.818181818, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.773, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r12", msg="wrong ratio")
        self.assertEqual(conclusion, 1, msg="wrong conclusion")


    def test_outlier_upper(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.y, ratio="r12", which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.8, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.773, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r12", msg="wrong ratio")
        result = False
        if "The upper value (15.68) perhaps be an outlier (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.y, ratio="r12", which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.25, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.773, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r12", msg="wrong ratio")
        result = False
        if "Os dados não apresentam outliers (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Dixon()
        result, conclusion = teste.fit(self.y, ratio="r12", details='full', which="max")
        self.assertAlmostEqual(result[0], 0.8, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.773, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r12", msg="wrong ratio")
        result = False
        if "Since the test statistic value (0.799) is higher than the critical value (0.773), we have evidence to reject the null hypothesis that the sample does not contain outliers, and perhaps the upper value (15.68) is an outlier (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.y, ratio="r12", details="full", which="min")
        self.assertAlmostEqual(result[0], 0.25, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.773, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r12", msg="wrong ratio")
        result = False
        if "Como o valor da estatistica do teste (0.249) é menor do que o valor crítico (0.773), não temos evidências para rejeitar a hipótese nula de que a amostra não contém outliers (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon()
        result, conclusion = teste.fit(self.y, ratio="r12", details='binary', which="max")
        self.assertAlmostEqual(result[0], 0.8, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.773, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r12", msg="wrong ratio")
        self.assertEqual(conclusion, 1, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.y, ratio="r12", details="binary", which="min")
        self.assertAlmostEqual(result[0], 0.25, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.773, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r12", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")


    def test_no_outlier(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.x, ratio="r12", which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.878, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r12", msg="wrong ratio")
        result = False
        if "The data does not have outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.x, ratio="r12", which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.5, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.878, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r12", msg="wrong ratio")
        result = False
        if "Os dados não apresentam outliers (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Dixon()
        result, conclusion = teste.fit(self.x, ratio="r12", details='full', which="max")
        self.assertAlmostEqual(result[0], 0, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.878, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r12", msg="wrong ratio")
        result = False
        if "Since the test statistic value (0.0) is lower than the critical value (0.878), we have no evidence to reject the null hypothesis that the sample does not contain outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.x, ratio="r12", details="full", which="min")
        self.assertAlmostEqual(result[0], 0.5, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.878, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r12", msg="wrong ratio")
        result = False
        if "Como o valor da estatistica do teste (0.5) é menor do que o valor crítico (0.878), não temos evidências para rejeitar a hipótese nula de que a amostra não contém outliers (com 95.0% de confiança)." in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon()
        result, conclusion = teste.fit(self.x, ratio="r12", details='binary', which="max")
        self.assertAlmostEqual(result[0], 0, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.878, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r12", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.x, ratio="r12", details="binary", which="min")
        self.assertAlmostEqual(result[0], 0.5, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.878, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r12", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")



class Test_ratio_11(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.x = np.array([15.52, 15.53, 15.53, 15.54, 15.56, 15.56]) # sem outliers
        cls.y = np.array([15.52, 15.53, 15.53, 15.54, 15.56, 15.56, 15.68]) # valor superior outlier
        cls.z = np.array([15.42, 15.51, 15.52, 15.52, 15.53, 15.53, 15.54]) # valor inferior outlier


    def test_outlier_lower(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.z, ratio="r11", which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.333333333, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.673, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r11", msg="wrong ratio")
        result = False
        if "The data does not have outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.z, ratio="r11", which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.818181818, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.673, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r11", msg="wrong ratio")
        result = False
        if "O valor inferior (15.42) talvez seja um outlier (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Dixon()
        result, conclusion = teste.fit(self.z, ratio="r11", details='full', which="max")
        self.assertAlmostEqual(result[0], 0.333333333, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.673, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r11", msg="wrong ratio")
        result = False
        if "Since the test statistic value (0.333) is lower than the critical value (0.673), we have no evidence to reject the null hypothesis that the sample does not contain outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.z, ratio="r11", details="full", which="min")
        self.assertAlmostEqual(result[0], 0.818181818, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.673, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r11", msg="wrong ratio")
        result = False
        if "Como o valor da estatistica do teste (0.818) é maior do que o valor crítico (0.673), temos evidências para rejeitar a hipótese nula de que a amostra não contém outliers, e talvez o valor inferior (15.42) seja um outlier (com 95.0% de confiança)." in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon()
        result, conclusion = teste.fit(self.z, ratio="r11", details='binary', which="max")
        self.assertAlmostEqual(result[0], 0.333333333, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.673, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r11", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.z, ratio="r11", details="binary", which="min")
        self.assertAlmostEqual(result[0], 0.818181818, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.673, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r11", msg="wrong ratio")
        self.assertEqual(conclusion, 1, msg="wrong conclusion")


    def test_outlier_upper(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.y, ratio="r11", which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.8, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.673, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r11", msg="wrong ratio")
        result = False
        if "The upper value (15.68) perhaps be an outlier (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.y, ratio="r11", which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.25, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.673, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r11", msg="wrong ratio")
        result = False
        if "Os dados não apresentam outliers (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Dixon()
        result, conclusion = teste.fit(self.y, ratio="r11", details='full', which="max")
        self.assertAlmostEqual(result[0], 0.8, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.673, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r11", msg="wrong ratio")
        result = False
        if "Since the test statistic value (0.799) is higher than the critical value (0.673), we have evidence to reject the null hypothesis that the sample does not contain outliers, and perhaps the upper value (15.68) is an outlier (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.y, ratio="r11", details="full", which="min")
        self.assertAlmostEqual(result[0], 0.25, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.673, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r11", msg="wrong ratio")
        result = False
        if "Como o valor da estatistica do teste (0.249) é menor do que o valor crítico (0.673), não temos evidências para rejeitar a hipótese nula de que a amostra não contém outliers (com 95.0% de confiança)." in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon()
        result, conclusion = teste.fit(self.y, ratio="r11", details='binary', which="max")
        self.assertAlmostEqual(result[0], 0.8, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.673, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r11", msg="wrong ratio")
        self.assertEqual(conclusion, 1, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.y, ratio="r11", details="binary", which="min")
        self.assertAlmostEqual(result[0], 0.25, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.673, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r11", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")


    def test_no_outlier(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.x, ratio="r11", which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.748, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r11", msg="wrong ratio")
        result = False
        if "The data does not have outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.x, ratio="r11", which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.25, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.748, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r11", msg="wrong ratio")
        result = False
        if "Os dados não apresentam outliers (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Dixon()
        result, conclusion = teste.fit(self.x, ratio="r11", details='full', which="max")
        self.assertAlmostEqual(result[0], 0, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.748, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r11", msg="wrong ratio")
        result = False
        if "Since the test statistic value (0.0) is lower than the critical value (0.748), we have no evidence to reject the null hypothesis that the sample does not contain outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.x, ratio="r11", details="full", which="min")
        self.assertAlmostEqual(result[0], 0.25, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.748, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r11", msg="wrong ratio")
        result = False
        if "Como o valor da estatistica do teste (0.249) é menor do que o valor crítico (0.748), não temos evidências para rejeitar a hipótese nula de que a amostra não contém outliers (com 95.0% de confiança)." in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon()
        result, conclusion = teste.fit(self.x, ratio="r11", details='binary', which="max")
        self.assertAlmostEqual(result[0], 0, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.748, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r11", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.x, ratio="r11", details="binary", which="min")
        self.assertAlmostEqual(result[0], 0.25, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.748, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r11", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")



class Test_ratio_10(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.x = np.array([15.52, 15.53, 15.53, 15.54, 15.56, 15.56]) # sem outliers
        cls.y = np.array([15.52, 15.53, 15.53, 15.54, 15.56, 15.56, 15.68]) # valor superior outlier
        cls.z = np.array([15.42, 15.51, 15.52, 15.52, 15.53, 15.53, 15.54]) # valor inferior outlier


    def test_outlier_lower(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.z, ratio="r10", which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.083333333, places=5, msg="wrong statistic value")
        self.assertEqual(result[1], 0.568, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        result = False
        if "The data does not have outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.z, ratio="r10", which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.75, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.568, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        result = False
        if "O valor inferior (15.42) talvez seja um outlier (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Dixon()
        result, conclusion = teste.fit(self.z, ratio="r10", details='full', which="max")
        self.assertAlmostEqual(result[0], 0.083333333, places=5, msg="wrong statistic value")
        self.assertEqual(result[1], 0.568, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        result = False
        if "Since the test statistic value (0.083) is lower than the critical value (0.568), we have no evidence to reject the null hypothesis that the sample does not contain outliers (with 95.0% confidence)." in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.z, ratio="r10", details="full", which="min")
        self.assertAlmostEqual(result[0], 0.75, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.568, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        result = False
        if "Como o valor da estatistica do teste (0.75) é maior do que o valor crítico (0.568), temos evidências para rejeitar a hipótese nula de que a amostra não contém outliers, e talvez o valor inferior (15.42) seja um outlier (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon()
        result, conclusion = teste.fit(self.z, ratio="r10", details='binary', which="max")
        self.assertAlmostEqual(result[0], 0.083333333, places=5, msg="wrong statistic value")
        self.assertEqual(result[1], 0.568, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.z, ratio="r10", details="binary", which="min")
        self.assertAlmostEqual(result[0], 0.75, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.568, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        self.assertEqual(conclusion, 1, msg="wrong conclusion")


    def test_outlier_upper(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.y, ratio="r10", which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.75, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.568, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        result = False
        if "The upper value (15.68) perhaps be an outlier (with 95.0% confidence)." in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.y, ratio="r10", which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.0625, places=3, msg="wrong statistic value")
        self.assertEqual(result[1], 0.568, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        result = False
        if "Os dados não apresentam outliers (com 95.0% de confiança)." in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Dixon()
        result, conclusion = teste.fit(self.y, ratio="r10", details='full', which="max")
        self.assertAlmostEqual(result[0], 0.75, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.568, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        result = False
        if "Since the test statistic value (0.749) is higher than the critical value (0.568), we have evidence to reject the null hypothesis that the sample does not contain outliers, and perhaps the upper value (15.68) is an outlier (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.y, ratio="r10", details="full", which="min")
        self.assertAlmostEqual(result[0], 0.0625, places=3, msg="wrong statistic value")
        self.assertEqual(result[1], 0.568, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        result = False
        if "Como o valor da estatistica do teste (0.062) é menor do que o valor crítico (0.568), não temos evidências para rejeitar a hipótese nula de que a amostra não contém outliers (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon()
        result, conclusion = teste.fit(self.y, ratio="r10", details='binary', which="max")
        self.assertAlmostEqual(result[0], 0.75, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.568, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        self.assertEqual(conclusion, 1, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.y, ratio="r10", details="binary", which="min")
        self.assertAlmostEqual(result[0], 0.0625, places=3, msg="wrong statistic value")
        self.assertEqual(result[1], 0.568, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")


    def test_no_outlier(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.x, ratio="r10", which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.625, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        result = False
        if "The data does not have outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.x, ratio="r10", which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.25, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.625, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        result = False
        if "Os dados não apresentam outliers (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Dixon()
        result, conclusion = teste.fit(self.x, ratio="r10", details='full', which="max")
        self.assertAlmostEqual(result[0], 0, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.625, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        result = False
        if "Since the test statistic value (0.0) is lower than the critical value (0.625), we have no evidence to reject the null hypothesis that the sample does not contain outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.x, ratio="r10", details="full", which="min")
        self.assertAlmostEqual(result[0], 0.25, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.625, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        result = False
        if "Como o valor da estatistica do teste (0.249) é menor do que o valor crítico (0.625), não temos evidências para rejeitar a hipótese nula de que a amostra não contém outliers (com 95.0% de confiança)." in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon()
        result, conclusion = teste.fit(self.x, ratio="r10", details='binary', which="max")
        self.assertAlmostEqual(result[0], 0, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.625, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.x, ratio="r10", details="binary", which="min")
        self.assertAlmostEqual(result[0], 0.25, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.625, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")



class Test_ratio_None(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([9, 16, 23, 41, 44, 46, 80])
        cls.y = np.array([9, 12, 16, 19, 23, 41, 41, 44, 46, 80])
        cls.z = np.array([8, 9, 12, 16, 19, 23, 35, 41, 41, 44, 46, 50, 80])
        cls.w = np.array([8, 9, 12, 12, 16, 19, 21, 22, 23, 27, 32, 32, 35, 41, 41, 44, 46, 48, 50, 80])

        cls.a = np.array([15.52, 15.53, 15.53, 15.54, 15.56, 15.56, 15.68]) # r10 valor superior outlier
        cls.b = np.array([15.42, 15.51, 15.52, 15.52, 15.53, 15.53, 15.54]) # r10 valor inferior outlier
        cls.c = np.array([15.52, 15.53, 15.53, 15.54, 15.56, 15.56, 15.68, 15.53, 15.54]) # r11 valor superior outlier
        cls.d = np.array([15.42, 15.51, 15.52, 15.52, 15.53, 15.53, 15.54, 15.53, 15.54]) # r11 valor inferior outlier
        cls.e = np.array([15.52, 15.53, 15.53, 15.54, 15.56, 15.56, 15.68, 15.53, 15.54, 15.55, 15.55]) # r12 valor superior outlier
        cls.f = np.array([15.42, 15.51, 15.52, 15.52, 15.53, 15.53, 15.54, 15.53, 15.54, 15.55, 15.55]) # r21 valor inferior outlier
        cls.g = np.array([15.52, 15.53, 15.53, 15.54, 15.56, 15.56, 15.68, 15.53, 15.54, 15.55, 15.55, 15.52, 15.53, 15.56, 15.55]) # r22 valor superior outlier
        cls.h = np.array([15.42, 15.51, 15.52, 15.52, 15.53, 15.53, 15.54, 15.53, 15.54, 15.55, 15.55, 15.52, 15.53, 15.56, 15.55]) # r22 valor inferior outlier



    def test_none_outlier_upper(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.a, ratio=None, which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.75, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.568, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        result = False
        if "The upper value (15.68) perhaps be an outlier (with 95.0% confidence)." in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon()
        result, conclusion = teste.fit(self.c, ratio=None, which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.8, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.570, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r11", msg="wrong ratio")
        result = False
        if "The upper value (15.68) perhaps be an outlier (with 95.0% confidence)." in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon()
        result, conclusion = teste.fit(self.e, ratio=None, which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.8, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.625, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r21", msg="wrong ratio")
        result = False
        if "The upper value (15.68) perhaps be an outlier (with 95.0% confidence)." in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Dixon()
        result, conclusion = teste.fit(self.g, ratio=None, which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.8, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.568, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r22", msg="wrong ratio")
        result = False
        if "The upper value (15.68) perhaps be an outlier (with 95.0% confidence)." in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

    def test_none_outlier_lower(self):
        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.b, ratio=None, which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.75, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.568, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        result = False
        if "O valor inferior (15.42) talvez seja um outlier (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.d, ratio=None, which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.75, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.570, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r11", msg="wrong ratio")
        result = False
        if "O valor inferior (15.42) talvez seja um outlier (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.f, ratio=None, which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.769230769, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.625, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r21", msg="wrong ratio")
        result = False
        if "O valor inferior (15.42) talvez seja um outlier (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.h, ratio=None, which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.769230769, places=7, msg="wrong statistic value")
        self.assertEqual(result[1], 0.568, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r22", msg="wrong ratio")
        result = False
        if "O valor inferior (15.42) talvez seja um outlier (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


    def test_r10(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.x, which="min")
        teste2 = Dixon()
        result2 = teste2._r10(self.x, which="min")
        self.assertAlmostEqual(result[0], result2, msg="results does not match")

        teste = Dixon()
        result, conclusion = teste.fit(self.x, which="max")
        teste2 = Dixon()
        result2 = teste2._r10(self.x, which="max")
        self.assertAlmostEqual(result[0], result2, msg="results does not match")


    def test_r11(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.y, which="min")
        teste2 = Dixon()
        result2 = teste2._r11(self.y, which="min")
        self.assertAlmostEqual(result[0], result2, msg="results does not match")

        teste = Dixon()
        result, conclusion = teste.fit(self.y, which="max")
        teste2 = Dixon()
        result2 = teste2._r11(self.y, which="max")
        self.assertAlmostEqual(result[0], result2, msg="results does not match")


    def test_r21(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.z, which="min")
        teste2 = Dixon()
        result2 = teste2._r21(self.z, which="min")
        self.assertAlmostEqual(result[0], result2, msg="results does not match")

        teste = Dixon()
        result, conclusion = teste.fit(self.z, which="max")
        teste2 = Dixon()
        result2 = teste2._r21(self.z, which="max")
        self.assertAlmostEqual(result[0], result2, msg="results does not match")


    def test_r22(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.w, which="min")
        teste2 = Dixon()
        result2 = teste2._r22(self.w, which="min")
        self.assertAlmostEqual(result[0], result2, msg="results does not match")

        teste = Dixon()
        result, conclusion = teste.fit(self.w, which="max")
        teste2 = Dixon()
        result2 = teste2._r22(self.w, which="max")
        self.assertAlmostEqual(result[0], result2, msg="results does not match")


    def test_lower(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.x, which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.098, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.568, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        result = False
        if "The data does not have outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.x, which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.098, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.568, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        result = False
        if "Os dados não apresentam outliers (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Dixon()
        result, conclusion = teste.fit(self.y, which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.081, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.534, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r11", msg="wrong ratio")
        result = False
        if "The data does not have outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.y, which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.081, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.534, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r11", msg="wrong ratio")
        result = False
        if "Os dados não apresentam outliers (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Dixon()
        result, conclusion = teste.fit(self.z, which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.095, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.565, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r21", msg="wrong ratio")
        result = False
        if "The data does not have outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.z, which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.095, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.565, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r21", msg="wrong ratio")
        result = False
        if "Os dados não apresentam outliers (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon()
        result, conclusion = teste.fit(self.w, which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.1, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.491, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r22", msg="wrong ratio")
        result = False
        if "The data does not have outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.w, which="min")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.1, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.491, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r22", msg="wrong ratio")
        result = False
        if "Os dados não apresentam outliers (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


    def test_lower_full(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.x, which="min", details='full')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.098, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.568, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        result = False
        if "Since the test statistic value (0.098) is lower than the critical value (0.568), we have no evidence to reject the null hypothesis that the sample does not contain outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.x, which="min", details='full')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.098, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.568, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        result = False
        if "Como o valor da estatistica do teste (0.098) é menor do que o valor crítico (0.568), não temos evidências para rejeitar a hipótese nula de que a amostra não contém outliers (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


    def test_lower_binary(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.x, which="min", details='binary')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, int, msg="conclusion not a int when binary")
        self.assertAlmostEqual(result[0], 0.098, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.568, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="conclusion not 0 when no outlier")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.x, which="min", details='binary')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, int, msg="conclusion not a int when binary")
        self.assertAlmostEqual(result[0], 0.098, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.568, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="conclusion not 0 when no outlier")


    def test_upper(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.x, which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.478, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.568, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        result = False
        if "The data does not have outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.x, which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.478, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.568, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        result = False
        if "Os dados não apresentam outliers (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Dixon()
        result, conclusion = teste.fit(self.y, which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.5, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.534, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r11", msg="wrong ratio")
        result = False
        if "The data does not have outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.y, which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.5, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.534, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r11", msg="wrong ratio")
        result = False
        if "Os dados não apresentam outliers (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Dixon()
        result, conclusion = teste.fit(self.z, which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.478, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.565, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r21", msg="wrong ratio")
        result = False
        if "The data does not have outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.z, which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.478, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.565, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r21", msg="wrong ratio")
        result = False
        if "Os dados não apresentam outliers (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon()
        result, conclusion = teste.fit(self.w, which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.470, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.491, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r22", msg="wrong ratio")
        result = False
        if "The data does not have outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.w, which="max")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.470, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.491, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r22", msg="wrong ratio")
        result = False
        if "Os dados não apresentam outliers (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


    def test_upper_full(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.x, which="max", details='full')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.478, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.568, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        result = False
        if "Since the test statistic value (0.478) is lower than the critical value (0.568), we have no evidence to reject the null hypothesis that the sample does not contain outliers (with 95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.x, which="max", details='full')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.478, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.568, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        result = False
        if "Como o valor da estatistica do teste (0.478) é menor do que o valor crítico (0.568), não temos evidências para rejeitar a hipótese nula de que a amostra não contém outliers (com 95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


    def test_upper_binary(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.x, which="max", details='binary')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, int, msg="conclusion not a int when binary")
        self.assertAlmostEqual(result[0], 0.478, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.568, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="conclusion not 0 when no outlier")

        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.x, which="max", details='binary')
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, int, msg="conclusion not a int when binary")
        self.assertAlmostEqual(result[0], 0.478, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.568, msg="wrong critical value")
        self.assertEqual(result[2], 0.05, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="conclusion not 0 when no outlier")


    def test_alfa(self):
        teste = Dixon()
        result, conclusion = teste.fit(self.x, which="max", details='binary', alfa=0.01)
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, int, msg="conclusion not a int when binary")
        self.assertAlmostEqual(result[0], 0.478, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.680, msg="wrong critical value")
        self.assertEqual(result[2], 0.01, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        self.assertEqual(conclusion, 0, msg="conclusion not 0 when no outlier")

        teste = Dixon()
        result, conclusion = teste.fit(self.x, which="max", details='full', alfa=0.01)
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.478, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.680, msg="wrong critical value")
        self.assertEqual(result[2], 0.01, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        result = False
        if "Since the test statistic value (0.478) is lower than the critical value (0.68), we have no evidence to reject the null hypothesis that the sample does not contain outliers (with 99.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Dixon(language='pt-br')
        result, conclusion = teste.fit(self.x, which="max", details='short', alfa=0.01)
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="ratio not a tuple")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.478, places=2, msg="wrong statistic value")
        self.assertEqual(result[1], 0.680, msg="wrong critical value")
        self.assertEqual(result[2], 0.01, msg="wrong statistic value")
        self.assertEqual(result[3], "r10", msg="wrong ratio")
        result = False
        if "Os dados não apresentam outliers (com 99.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")




if __name__ == "__main__":
    unittest.main()
