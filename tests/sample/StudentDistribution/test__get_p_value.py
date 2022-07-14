"""Tests if the test__get_p_value is working as expected

---> Class Test_get_p_value: This class tests the output type, the ttributes name, if the two side result is twice the one side result (random values). It also checks for correct values (from excel) for one side and two side


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sample/StudentDistribution/test__get_p_value.py
    or
    python -m unittest -b tests/sample/StudentDistribution/test__get_p_value.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sample.studentdistribution import StudentDistribution
import numpy as np
import random
os.system('cls')


class Test_get_critical_value(unittest.TestCase):


    def test_result(self):
        student = StudentDistribution()
        result = student._get_p_value(5, 5)
        self.assertIsInstance(result, tuple, msg="Output not a tuple")
        self.assertIsInstance(result[0], float, msg="p-value not a float")
        self.assertIsInstance(result[1], str, msg="which not str")


    def test_atributes(self):
        result = True
        try:
            student = StudentDistribution()
            teste = student._get_p_value(5, 5)
            a = teste.which
            a = teste.p_value
        except AttributeError:
            result = False
        self.assertTrue(result, msg="wrong attribute name")

        result = True
        try:
            student = StudentDistribution(language="pt-br")
            teste = student._get_p_value(5, 5)
            a = teste.which
            a = teste.p_valor
        except AttributeError:
            result = False
        self.assertTrue(result, msg="wrong attribute name")


    def test_one_side_half_two_side(self):
        passo = random.randint(1,5)
        for gl in range(2, 50, passo):
            student = StudentDistribution()
            t_calc = random.uniform(0.0, 5.0)
            result_two = student._get_p_value(t_calc, gl)
            result_one = student._get_p_value(t_calc, gl, which="one-side")
            self.assertAlmostEqual(result_two[0]/2, result_one[0], places=7, msg="one side does not match half two side")


    def test_one_side(self):
        student = StudentDistribution()
        result = student._get_p_value(5, 5, which="one-side")
        self.assertAlmostEqual(result[0], 0.00205236, msg="wrong p_value")
        self.assertEqual(result[1], "one-side", msg="wrong which")

        result = student._get_p_value(0.1, 10, which="one-side")
        self.assertAlmostEqual(result[0], 0.46116036, msg="wrong p_value")

        result = student._get_p_value(1, 3, which="one-side")
        self.assertAlmostEqual(result[0], 0.19550111, msg="wrong p_value")

        result = student._get_p_value(10, 2, which="one-side")
        self.assertAlmostEqual(result[0], 0.00492623, msg="wrong p_value")

        result = student._get_p_value(13.56, 6, which="one-side")
        self.assertAlmostEqual(result[0], 0.00000499, msg="wrong p_value")

        result = student._get_p_value(1.236, 7, which="one-side")
        self.assertAlmostEqual(result[0], 0.12816121, msg="wrong p_value")


    def test_two_side(self):
        student = StudentDistribution()
        result = student._get_p_value(5, 5, which="two-side")
        self.assertAlmostEqual(result[0], 0.00410472, msg="wrong p_value")
        self.assertEqual(result[1], "two-side", msg="wrong which")

        result = student._get_p_value(0.1, 10, which="two-side")
        self.assertAlmostEqual(result[0], 0.92232072, msg="wrong p_value")

        result = student._get_p_value(1, 3, which="two-side")
        self.assertAlmostEqual(result[0], 0.39100222, msg="wrong p_value")

        result = student._get_p_value(10, 2, which="two-side")
        self.assertAlmostEqual(result[0], 0.00985246, msg="wrong p_value")

        result = student._get_p_value(13.56, 6, which="two-side")
        self.assertAlmostEqual(result[0], 0.00000998, msg="wrong p_value")

        result = student._get_p_value(1.236, 7, which="two-side")
        self.assertAlmostEqual(result[0], 0.25632241, msg="wrong p_value")

    def test_one_side_negatiive(self):
        student = StudentDistribution()
        result = student._get_p_value(-5, 5, which="one-side")
        self.assertAlmostEqual(result[0], 0.00205236, msg="wrong p_value")
        self.assertEqual(result[1], "one-side", msg="wrong which")

        result = student._get_p_value(-0.1, 10, which="one-side")
        self.assertAlmostEqual(result[0], 0.46116036, msg="wrong p_value")

        result = student._get_p_value(-1, 3, which="one-side")
        self.assertAlmostEqual(result[0], 0.19550111, msg="wrong p_value")

        result = student._get_p_value(-10, 2, which="one-side")
        self.assertAlmostEqual(result[0], 0.00492623, msg="wrong p_value")

        result = student._get_p_value(-13.56, 6, which="one-side")
        self.assertAlmostEqual(result[0], 0.00000499, msg="wrong p_value")

        result = student._get_p_value(-1.236, 7, which="one-side")
        self.assertAlmostEqual(result[0], 0.12816121, msg="wrong p_value")


    def test_two_side_negative(self):
        student = StudentDistribution()
        result = student._get_p_value(-5, 5, which="two-side")
        self.assertAlmostEqual(result[0], 0.00410472, msg="wrong p_value")
        self.assertEqual(result[1], "two-side", msg="wrong which")

        result = student._get_p_value(-0.1, 10, which="two-side")
        self.assertAlmostEqual(result[0], 0.92232072, msg="wrong p_value")

        result = student._get_p_value(-1, 3, which="two-side")
        self.assertAlmostEqual(result[0], 0.39100222, msg="wrong p_value")

        result = student._get_p_value(-10, 2, which="two-side")
        self.assertAlmostEqual(result[0], 0.00985246, msg="wrong p_value")

        result = student._get_p_value(-13.56, 6, which="two-side")
        self.assertAlmostEqual(result[0], 0.00000998, msg="wrong p_value")

        result = student._get_p_value(-1.236, 7, which="two-side")
        self.assertAlmostEqual(result[0], 0.25632241, msg="wrong p_value")





if __name__ == "__main__":
    unittest.main()
