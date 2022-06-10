"""Tests if the test_skewness is working as expected

---> Class Test_two_side
    This class test if the all the outputs for a two-side test. The results are checked when the constant is distinct when compare to a mean, with values closer to the mean and far from the mean (but rejecting the H0). The tests checks language as well.


---> Class Test_raises_error
    This class test when the method should raise ValueError. The output is also tested.

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/normalitycheck/Gaussian/test_skewness.py
    or
    python -m unittest -b tests/normalitycheck/Gaussian/test_skewness.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.normalitycheck.gaussian import Gaussian
import numpy as np
from unittest.mock import patch
import io
import sys
os.system('cls')


class Test_raises_error(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([90, 72, 90, 64, 95, 89, 74, 88, 100, 77, 57, 35, 100, 64, 95, 65, 80, 84, 90, 100, 76])
        cls.y = np.array([90, 72, 90])
        cls.z = np.array([1, 1, 1, 1.000001])


    def test_n_std(self):
        with self.assertRaises(RuntimeError, msg="Does not raised error when n < 4"):
            teste = Gaussian()
            result, conclusion = teste.skewness(self.z)

        with self.assertRaises(RuntimeError, msg="Does not raised error when n < 4"):
            teste = Gaussian(language='pt-br')
            result, conclusion = teste.skewness(self.z)



    def test_n_std_output(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            teste = Gaussian()
            result, conclusion = teste.skewness(self.z)
        except RuntimeError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The sample standard deviation (4.999999999588667e-07) is lower than 10E-6, which makes the results inaccurate."
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")


        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            teste = Gaussian(language='pt-br')
            result, conclusion = teste.skewness(self.z)
        except RuntimeError:
            pass
        sys.stdout = sys.__stdout__
        expected = "O desvio padrão da amostra (4.999999999588667e-07) é menor que 10E-6, o que torna os resultados imprecisos."
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")


    def test_n_rep(self):
        with self.assertRaises(ValueError, msg="Does not raised error when n < 4"):
            teste = Gaussian()
            result, conclusion = teste.skewness(self.y)

        with self.assertRaises(ValueError, msg="Does not raised error when n < 4"):
            teste = Gaussian(language='pt-br')
            result, conclusion = teste.skewness(self.y)


    def test_n_rep_output(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            teste = Gaussian()
            result, conclusion = teste.skewness(self.y)
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The minimum sample size for the 'x_exp' parameter is '4', but we got a sample of size '3'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")


        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            teste = Gaussian(language='pt-br')
            result, conclusion = teste.skewness(self.y)
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "O tamanho amostral mínimo para o parâmetro 'x_exp' é '4', mas recebemos uma amostra com tamanho '3'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")


    def test_details(self):
        with self.assertRaises(ValueError, msg="Does not raised error when details is wrong"):
            teste = Gaussian()
            result, conclusion = teste.skewness(self.x, details='shot')

        with self.assertRaises(ValueError, msg="Does not raised error when details is wrong"):
            teste = Gaussian()
            result, conclusion = teste.skewness(self.x, details='ful')

        with self.assertRaises(ValueError, msg="Does not raised error when details is wrong"):
            teste = Gaussian()
            result, conclusion = teste.skewness(self.x, details='binario')


        with self.assertRaises(ValueError, msg="Does not raised error when details is wrong"):
            teste = Gaussian(language='pt-br')
            result, conclusion = teste.skewness(self.x, details='shot')

        with self.assertRaises(ValueError, msg="Does not raised error when details is wrong"):
            teste = Gaussian(language='pt-br')
            result, conclusion = teste.skewness(self.x, details='ful')

        with self.assertRaises(ValueError, msg="Does not raised error when details is wrong"):
            teste = Gaussian(language='pt-br')
            result, conclusion = teste.skewness(self.x, details='binario')


    def test_details_output(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            teste = Gaussian()
            result, conclusion = teste.skewness(self.x, details='shot')
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'details' parameter only accepts 'short', 'full' or 'binary' as values, but we got 'shot'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")


        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            teste = Gaussian()
            result, conclusion = teste.skewness(self.x, details='ful')
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'details' parameter only accepts 'short', 'full' or 'binary' as values, but we got 'ful'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")


        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            teste = Gaussian()
            result, conclusion = teste.skewness(self.x, details='binario')
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'details' parameter only accepts 'short', 'full' or 'binary' as values, but we got 'binario'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")


        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            teste = Gaussian(language='pt-br')
            result, conclusion = teste.skewness(self.x, details='shot')
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "O parâmetro 'details' aceita apenas 'short', 'full' ou 'binary' como valores, mas obtivemos 'shot'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")


        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            teste = Gaussian(language='pt-br')
            result, conclusion = teste.skewness(self.x, details='ful')
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "O parâmetro 'details' aceita apenas 'short', 'full' ou 'binary' como valores, mas obtivemos 'ful'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")


        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            teste = Gaussian(language='pt-br')
            result, conclusion = teste.skewness(self.x, details='binario')
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "O parâmetro 'details' aceita apenas 'short', 'full' ou 'binary' como valores, mas obtivemos 'binario'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

#
class Test_two_side(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # assimetria Normal and positive
        cls.x = np.array([1,2,3,4,5.1])
        # assimetria Normal and negative
        cls.y = np.array([0.9,2,3,4,5])
        # assimetria não Normal e negativa
        cls.z = np.array([90, 72, 90, 64, 95, 89, 74, 88, 100, 77, 57, 35, 100, 64, 95, 65, 80, 84, 90, 100, 76])
        # assimetria não Normal e positiva
        cls.w = np.array([8,7,6,5,5,4,4,4,4,3,3,3,3,3,3,3,3,3,3,2,2,2,2,1])



    def test_skewness_normal_details(self):
        teste = Gaussian()
        result, conclusion = teste.skewness(self.x, details='short')
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        result = False
        if "Skewness is Normal (95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion ")

        teste = Gaussian(language='pt-br')
        result, conclusion = teste.skewness(self.x, details='short')
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        result = False
        if "A Assimetria é Normal (95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion ")

        teste = Gaussian()
        result, conclusion = teste.skewness(self.y, details='short')
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        result = False
        if "Skewness is Normal (95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion ")

        teste = Gaussian(language='pt-br')
        result, conclusion = teste.skewness(self.y, details='short')
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        result = False
        if "A Assimetria é Normal (95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion ")


        teste = Gaussian()
        result, conclusion = teste.skewness(self.x, details='full')
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        result = False
        if "Since the calculated statistic for the skewness (0.069) is a value between the lower critical value (-1.959) and the upper critical value (1.959), we have no evidence to reject the null hypothesis that the distribution has skewness similar to the skewness of a Normal distribution (with 95.0% confidence)." in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion ")

        teste = Gaussian(language='pt-br')
        result, conclusion = teste.skewness(self.x, details='full')
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        result = False
        if "Como a estatistica calculada para a assimetria (0.069) é um valor entre o valor crítico inferior (-1.959) e o valor critico superior (1.959), não temos evidências para rejeitar a hipótese nula de que a distribuição apresenta assimetria similar a assimetria de uma distribuição Normal (com  95.0% de confiança)." in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion ")

        teste = Gaussian()
        result, conclusion = teste.skewness(self.y, details='full')
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        result = False
        if "Since the calculated statistic for the skewness (-0.069) is a value between the lower critical value (-1.959) and the upper critical value (1.959), we have no evidence to reject the null hypothesis that the distribution has skewness similar to the skewness of a Normal distribution (with 95.0% confidence)." in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion ")

        teste = Gaussian(language='pt-br')
        result, conclusion = teste.skewness(self.y, details='full')
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        result = False
        if "Como a estatistica calculada para a assimetria (-0.069) é um valor entre o valor crítico inferior (-1.959) e o valor critico superior (1.959), não temos evidências para rejeitar a hipótese nula de que a distribuição apresenta assimetria similar a assimetria de uma distribuição Normal (com  95.0% de confiança)." in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion ")


        teste = Gaussian()
        result, conclusion = teste.skewness(self.x, details='binary')
        self.assertIsInstance(conclusion, int, msg="conclusion not a str")
        self.assertEqual(conclusion, 0, msg="conclusion not 0 when H0 is accpeted")

        teste = Gaussian(language='pt-br')
        result, conclusion = teste.skewness(self.x, details='binary')
        self.assertIsInstance(conclusion, int, msg="conclusion not a str")
        self.assertEqual(conclusion, 0, msg="conclusion not 0 when H0 is accpeted")

        teste = Gaussian()
        result, conclusion = teste.skewness(self.y, details='binary')
        self.assertIsInstance(conclusion, int, msg="conclusion not a str")
        self.assertEqual(conclusion, 0, msg="conclusion not 0 when H0 is accpeted")

        teste = Gaussian(language='pt-br')
        result, conclusion = teste.skewness(self.y, details='binary')
        self.assertIsInstance(conclusion, int, msg="conclusion not a str")
        self.assertEqual(conclusion, 0, msg="conclusion not 0 when H0 is accpeted")


    def test_skewness_normal(self):
        teste = Gaussian()
        result, conclusion = teste.skewness(self.x)
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 0.06921547512339636, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], -1.959963984540054, msg="wrong lower")
        self.assertAlmostEqual(result[1][1], 1.959963984540054, msg="wrong upper")
        self.assertEqual(result[2], 0.05, msg="worng alfa")
        result = False
        if "Skewness is Normal (95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion ")

        teste = Gaussian(language='pt-br')
        result, conclusion = teste.skewness(self.y)
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -0.06921547512339678, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], -1.9599639845400545, msg="wrong lower")
        self.assertAlmostEqual(result[1][1], 1.9599639845400545, msg="wrong upper")
        self.assertEqual(result[2], 0.05, msg="worng alfa")
        result = False
        if "A Assimetria é Normal (95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion ")


    def test_skewness_not_normal_details(self):
        teste = Gaussian()
        result, conclusion = teste.skewness(self.z, details='short')
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        result = False
        if "Skewness is NOT Normal (95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion ")

        teste = Gaussian(language='pt-br')
        result, conclusion = teste.skewness(self.z, details='short')
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        result = False
        if "A Assimetria é NÃO Normal (95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion ")

        teste = Gaussian()
        result, conclusion = teste.skewness(self.w, details='short')
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        result = False
        if "Skewness is NOT Normal (95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion ")

        teste = Gaussian(language='pt-br')
        result, conclusion = teste.skewness(self.w, details='short')
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        result = False
        if "A Assimetria é NÃO Normal (95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion ")


        teste = Gaussian()
        result, conclusion = teste.skewness(self.z, details='full')
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        result = False
        if "Since the calculated statistic for the skewness (-2.03) is a value lower than the lower critical value (-1.959), we have evidence to reject the null hypothesis, and we can say that the distribution does not have skewness similar to the skewness of a Normal distribution (with 95.0% confidence)." in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion ")

        teste = Gaussian(language='pt-br')
        result, conclusion = teste.skewness(self.z, details='full')
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        result = False
        if "Como a estatistica calculada para a assimetria (-2.03) é um valor menor do que o valor crítico inferior (-1.959), temos evidências para rejeitar a hipótese nula, e podemos dizer que a distribuição não apresenta assimetria similar a assimetria de uma distribuição Normal (com 95.0% de confiança)." in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion ")

        teste = Gaussian()
        result, conclusion = teste.skewness(self.w, details='full')
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        result = False
        if "Since the calculated statistic for the skewness (2.529) is a value higher than the upper critical value (1.959), we have evidence to reject the null hypothesis, and we can say that the distribution does not have skewness similar to the skewness of a Normal distribution (with 95.0% confidence)." in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion ")

        teste = Gaussian(language='pt-br')
        result, conclusion = teste.skewness(self.w, details='full')
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        result = False
        if "Como a estatistica calculada para a assimetria (2.529) é um valor maior do que o valor crítico superior (1.959), temos evidências para rejeitar a hipótese nula, e podemos dizer que a distribuição não apresenta assimetria similar a assimetria de uma distribuição Normal (com 95.0% de confiança)." in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion ")

        teste = Gaussian()
        result, conclusion = teste.skewness(self.z, details='binary')
        self.assertIsInstance(conclusion, int, msg="conclusion not a str")
        self.assertEqual(conclusion, 1, msg="conclusion not 1 when H0 is rejected")

        teste = Gaussian(language='pt-br')
        result, conclusion = teste.skewness(self.z, details='binary')
        self.assertIsInstance(conclusion, int, msg="conclusion not a str")
        self.assertEqual(conclusion, 1, msg="conclusion not 1 when H0 is rejected")

        teste = Gaussian()
        result, conclusion = teste.skewness(self.w, details='binary')
        self.assertIsInstance(conclusion, int, msg="conclusion not a str")
        self.assertEqual(conclusion, 1, msg="conclusion not 1 when H0 is rejected")

        teste = Gaussian(language='pt-br')
        result, conclusion = teste.skewness(self.w, details='binary')
        self.assertIsInstance(conclusion, int, msg="conclusion not a str")
        self.assertEqual(conclusion, 1, msg="conclusion not 1 when H0 is rejected")


    def test_skewness_not_normal(self):
        teste = Gaussian(language='en')
        result, conclusion = teste.skewness(self.z)
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], -2.0304772981338326, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], -1.9599639845400545, msg="wrong lower")
        self.assertAlmostEqual(result[1][1], 1.959963984540054, msg="wrong upper")
        self.assertEqual(result[2], 0.05, msg="worng alfa")
        result = False
        if "Skewness is NOT Normal (95.0% confidence)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Gaussian(language='pt-br')
        result, conclusion = teste.skewness(self.w)
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a float")
        self.assertIsInstance(result[1], list, msg="critical not list")
        self.assertIsInstance(result[1][1], float, msg="critical lower not float")
        self.assertIsInstance(result[1][0], float, msg="critical upper not float")
        self.assertAlmostEqual(result[1][0], -1*result[1][1], msg="lower and upper not opossite")
        self.assertIsInstance(result[2], float, msg="alfa not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")
        self.assertAlmostEqual(result[0], 2.529695221071549, msg="wrong statistic")
        self.assertAlmostEqual(result[1][0], -1.9599639845400545, msg="wrong lower")
        self.assertAlmostEqual(result[1][1], 1.9599639845400545, msg="wrong upper")
        self.assertEqual(result[2], 0.05, msg="worng alfa")
        result = False
        if "A Assimetria é NÃO Normal (95.0% de confiança)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")






if __name__ == "__main__":
    unittest.main()
