"""Tests if the test__check_comparison_param is working as expected

---> Class Test_check_comparison_param


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sample/StudentDistribution/test__check_comparison_param.py
    or
    python -m unittest -b tests/sample/StudentDistribution/test__check_comparison_param.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sample.studentdistribution import _check_comparison_param
import numpy as np
import io
import sys
os.system('cls')


class Test_check_comparison_param(unittest.TestCase):


    def test_comparison(self):
        with self.assertRaises(ValueError, msg="Does not raised error when comparison not allowed"):
            _check_comparison_param("critica", 'en')

        with self.assertRaises(ValueError, msg="Does not raised error when comparison not allowed"):
            _check_comparison_param("p_value", 'en')

        with self.assertRaises(ValueError, msg="Does not raised error when comparison not allowed"):
            _check_comparison_param("critico", 'pt-br')

        with self.assertRaises(ValueError, msg="Does not raised error when comparison not allowed"):
            _check_comparison_param("p-valor", 'pt-br')


    def test_comparison_output(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            _check_comparison_param("critica", 'en')
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'comparison' parameter only accepts the keys 'critical' or 'p-value', but we got: 'critica'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        # ------------- #
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            _check_comparison_param("p_value", 'en')
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'comparison' parameter only accepts the keys 'critical' or 'p-value', but we got: 'p_value'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        # ------------- #
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            _check_comparison_param("critico", 'pt-br')
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "O parâmetro 'comparison' aceita como chave apenas 'critical' ou 'p-value', mas recebemos: 'critico'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        # ------------- #
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            _check_comparison_param("p-valor", 'pt-br')
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "O parâmetro 'comparison' aceita como chave apenas 'critical' ou 'p-value', mas recebemos: 'p-valor'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")



    def test_pass(self):

        result = _check_comparison_param("critical", 'pt-br')
        self.assertEqual(result, "critical")

        result = _check_comparison_param("critical", 'en')
        self.assertEqual(result, "critical")

        result = _check_comparison_param("p-value", 'en')
        self.assertEqual(result, "p-value")

        result = _check_comparison_param("p-value", 'pt-br')
        self.assertEqual(result, "p-value")








# m. e. t. l https://youtu.be/7idcgZGHCjM?t=140

if __name__ == "__main__":
    unittest.main()
