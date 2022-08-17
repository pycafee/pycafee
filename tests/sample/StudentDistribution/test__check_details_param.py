"""Tests if the test__check_details_param is working as expected

---> Class Test_check_details_param


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sample/StudentDistribution/test__check_details_param.py
    or
    python -m unittest -b tests/sample/StudentDistribution/test__check_details_param.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sample.studentdistribution import _check_details_param
import numpy as np
import io
import sys
os.system('cls')


class Test_check_details_param(unittest.TestCase):


    def test_details(self):
        with self.assertRaises(ValueError, msg="Does not raised error when details not allowed"):
            _check_details_param("shot", 'en')

        with self.assertRaises(ValueError, msg="Does not raised error when details not allowed"):
            _check_details_param("ful", 'en')

        with self.assertRaises(ValueError, msg="Does not raised error when details not allowed"):
            _check_details_param("binari", 'en')

        with self.assertRaises(ValueError, msg="Does not raised error when details not allowed"):
            _check_details_param("curto", 'pt-br')

        with self.assertRaises(ValueError, msg="Does not raised error when details not allowed"):
            _check_details_param("completo", 'pt-br')

        with self.assertRaises(ValueError, msg="Does not raised error when details not allowed"):
            _check_details_param("binario", 'pt-br')

    def test_details_output(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            _check_details_param("shot", 'en')
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'details' parameter only accepts the keys 'short', 'full' or 'binary', but we got: 'shot'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        # ------------- #
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            _check_details_param("ful", 'en')
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'details' parameter only accepts the keys 'short', 'full' or 'binary', but we got: 'ful'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        # ------------- #
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            _check_details_param("binari", 'en')
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'details' parameter only accepts the keys 'short', 'full' or 'binary', but we got: 'binari'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        # ------------- #
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            _check_details_param("curto", 'pt-br')
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "O parâmetro 'details' aceita como chave apenas 'short', 'full' ou 'binary', mas recebemos: 'curto'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        # ------------- #
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            _check_details_param("completo", 'pt-br')
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "O parâmetro 'details' aceita como chave apenas 'short', 'full' ou 'binary', mas recebemos: 'completo'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")


        # ------------- #
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            _check_details_param("binario", 'pt-br')
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "O parâmetro 'details' aceita como chave apenas 'short', 'full' ou 'binary', mas recebemos: 'binario'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")


    def test_pass(self):

        result = _check_details_param("short", 'pt-br')
        self.assertEqual(result, "short")

        result = _check_details_param("short", 'en')
        self.assertEqual(result, "short")

        result = _check_details_param("full", 'en')
        self.assertEqual(result, "full")

        result = _check_details_param("full", 'pt-br')
        self.assertEqual(result, "full")

        result = _check_details_param("full", 'en')
        self.assertEqual(result, "full")

        result = _check_details_param("binary", 'pt-br')
        self.assertEqual(result, "binary")








# m. e. t. l https://youtu.be/7idcgZGHCjM?t=140

if __name__ == "__main__":
    unittest.main()
