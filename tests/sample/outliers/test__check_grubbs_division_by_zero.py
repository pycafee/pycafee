"""Tests if the _check_grubbs_division_by_zero is working as expected

--------------------------------------------------------------------------------
Description:

---> class Test_raises: this class checks if the function is raising ZeroDivisionError when position 1 and 2 are equal

---> class Test_pass: this class checks if the function returns True if position 1 is different from 2


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sample/outliers/test__check_grubbs_division_by_zero.py
    or
    python -m unittest -b tests/sample/outliers/test__check_grubbs_division_by_zero.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sample.outliers import _check_grubbs_division_by_zero
import numpy as np
import sys
import io
os.system('cls')

class Test_raises(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([1, 2, 3, 4, 5, 6, 6])
        cls.y = np.array([1.0000000000000001, 1, 1, 1])
        cls.z = np.array([1, 1, 1, 1, 1, 1, 1])



    def test_fail(self):
        with self.assertRaises(ZeroDivisionError, msg="Does not raised error when std is 0"):
            _check_grubbs_division_by_zero(self.z, 'en')

        with self.assertRaises(ZeroDivisionError, msg="Does not raised error when std is 0"):
            _check_grubbs_division_by_zero(self.y, 'en')


    def test_fail_output(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            _check_grubbs_division_by_zero(self.z, 'en')
        except ZeroDivisionError:
            pass
        sys.stdout = sys.__stdout__
        expected = "deviation cannot be equal to zero,"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            _check_grubbs_division_by_zero(self.z, 'pt-br')
        except ZeroDivisionError:
            pass
        sys.stdout = sys.__stdout__
        expected = "desvio padrão da amostra não pode ser igual a zero"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")





class Test_pass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([1, 2, 3, 4, 5, 6, 6])
        cls.y = np.array([1.1, 1.1, 2, 3, 4, 5, 6, 6])
        cls.z = np.array([1.0001, 1, 1, 1, 1, 1, 1])

    def test_equals(self):
        result = _check_grubbs_division_by_zero(self.x, 'en')
        self.assertTrue(result, msg="not True when std is not 0")

        result = _check_grubbs_division_by_zero(self.y, 'en')
        self.assertTrue(result, msg="not True when std is not 0")

        result = _check_grubbs_division_by_zero(self.z, 'en')
        self.assertTrue(result, msg="not True when std is not 0")



# hi, hi, hi, hi, hi, hi, hi , hi https://youtu.be/ugnyM69LN54?t=125


if __name__ == "__main__":
    unittest.main()
