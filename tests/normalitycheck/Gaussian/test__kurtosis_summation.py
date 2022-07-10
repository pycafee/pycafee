"""Tests if the _kurtosis_summation is working as expected

---> Class Test__kurtosis_summation. This just checks for correct values and when std is lower thatn 10-6, which should raises RuntimeError



--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/normalitycheck/Gaussian/test__kurtosis_summation.py
    or
    python -m unittest -b tests/normalitycheck/Gaussian/test__kurtosis_summation.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.normalitycheck.gaussian import _kurtosis_summation
import numpy as np
import io
import sys
os.system("cls")

class Test__kurtosis_summation(unittest.TestCase):

    def test_pass(self):
        x_exp = np.array([90, 72, 90, 64, 95, 89, 74, 88, 100, 77, 57, 35, 100, 64, 95, 65, 80, 84, 90, 100, 76])
        result = _kurtosis_summation(x_exp, 'en')
        self.assertAlmostEqual(result, 69.01971614, msg="wrong summation for kurtosis")


    def test_std_very_lower(self):
        x_exp = np.array([1,1,1,1,1,1.000000001])
        with self.assertRaises(RuntimeError, msg="Does not raised RuntimeError when std < 10-6"):
            result = _kurtosis_summation(x_exp, 'en')


    def test_std_very_lower_output(self):
        x_exp = np.array([1,1,1,1,1,1.000000001])
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = _kurtosis_summation(x_exp, 'en')
        except RuntimeError:
            pass
        sys.stdout = sys.__stdout__
        expected = "is lower than 10E-6, which makes the results inaccurate."
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")


        x_exp = np.array([1,1,1,1,1,1.000000001])
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = _kurtosis_summation(x_exp, 'pt-br')
        except RuntimeError:
            pass
        sys.stdout = sys.__stdout__
        expected = "é menor que 10E-6, o que torna os resultados imprecisos"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")











# Vou consertar o seu mau carater no tapaaaaaaaaa
if __name__ == "__main__":
    unittest.main()
