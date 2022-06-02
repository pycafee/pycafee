"""Tests if the _check_decimal_separator is working as expected

---> Class Test_check_decimal_separtor
    This class tests if the _check_blank_space function raises ValueError when a string has white spaces, and if it returns True if a string does not have any white spaces


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/helpers/test__check_decimal_separator.py
    or
    python -m unittest -b tests/utils/helpers/test__check_decimal_separator.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.utils.helpers import _check_decimal_separator
import sys
import io
os.system("cls")
class Test_check_decimal_separator(unittest.TestCase):


    def test_pass(self):
        result = _check_decimal_separator('.', "en")
        self.assertTrue(result, msg="Something odd when the decimal separator is correct")

        result = _check_decimal_separator(',', "en")
        self.assertTrue(result, msg="Something odd when the decimal separator is correct")

    def test_raises(self):
        with self.assertRaises(ValueError, msg="Does not raised error when decimal separator is wrong"):
            _check_decimal_separator('|', "en")

        with self.assertRaises(ValueError, msg="Does not raised error when decimal separator is wrong"):
            _check_decimal_separator('|a', "en")

        with self.assertRaises(ValueError, msg="Does not raised error when decimal separator is wrong"):
            _check_decimal_separator(';', "en")

        with self.assertRaises(ValueError, msg="Does not raised error when decimal separator is wrong"):
            _check_decimal_separator(';', "pt-br")


    def test_raises_output(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            _check_decimal_separator('|', "en")
        except:
            pass
        sys.stdout = sys.__stdout__
        expected = "The '|' character cannot be used as decimal separator"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output")


        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            _check_decimal_separator('|a', "en")
        except:
            pass
        sys.stdout = sys.__stdout__
        expected = "The '|a' character cannot be used as decimal separator"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output")


        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            _check_decimal_separator(';', "en")
        except:
            pass
        sys.stdout = sys.__stdout__
        expected = "The ';' character cannot be used as decimal separator"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output")


        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            _check_decimal_separator(';', "pt-br")
        except:
            pass
        sys.stdout = sys.__stdout__
        expected = "O caractere ';' não pode ser utilizado como separador de casas decimais"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output")



# akaku somare, makka ni somare https://youtu.be/yGuuQ_45aTU?t=322
if __name__ == "__main__":
    unittest.main()
