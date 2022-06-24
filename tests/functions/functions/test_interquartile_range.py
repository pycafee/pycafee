"""Tests if the interquartile_range is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_Raises: This class tests when the function should raises ValueError

---> Class Test_interquartile_range_tukey. This class tests the interquartile_range using the tukey method



--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/functions/functions/test_interquartile_range.py
    or
    python -m unittest -b tests/functions/functions/test_interquartile_range.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.functions.functions import interquartile_range
import numpy as np
import sys
import io
os.system('cls')


class Test_Raises(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([4.4, 4.6, 4.6, 4.7, 4.9, 5.0, 5.0, 5.1, 5.4])


    def test_method_name(self):
        with self.assertRaises(ValueError, msg="Does not raised error method name not allowed"):
            interquartile_range(self.x, method="ukey")

        with self.assertRaises(ValueError, msg="Does not raised error method name not allowed"):
            interquartile_range(self.x, method="ukey", language='pt-br')

    def test_method_name_output(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = interquartile_range(self.x, method="ukey")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'method' parameter only accepts the following values: 'tukey', but we got 'ukey'."
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")


        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            result = interquartile_range(self.x, method="ukey", language='pt-br')
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "O parâmetro 'method' aceita apenas os seguintes valores: 'tukey', mas recebemos 'ukey'."
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")


class Test_interquartile_range_tukey(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.x = np.array([4.4, 4.6, 4.6, 4.7, 4.9, 5.0, 5.0, 5.1, 5.4])
        cls.y = np.array([4.9, 5.8, 6.3, 6.3, 6.5, 6.7, 7.1, 7.2, 7.3, 7.6])
        cls.z = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) #https://www.mathematics-monster.com/lessons/methods_for_finding_the_quartiles.html
        cls.zz = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) #https://www.mathematics-monster.com/lessons/methods_for_finding_the_quartiles.html
        cls.w = np.array([6, 7, 15, 36, 39, 40, 41, 42, 43, 47, 49]) #https://en.wikipedia.org/wiki/Quartile
        cls.ww = np.array([7, 15, 36, 39, 40, 41]) #https://en.wikipedia.org/wiki/Quartile
        cls.v = np.array([33, 34, 55, 57, 60, 61, 61, 2, 3, 5, 6, 7, 8, 12, 15, 18, 20, 27, 28, 29, 70]) #https://www.statisticshowto.com/upper-hinge-lower-hinge/
        cls.vv = np.array([33, 34, 55, 57, 60, 61, 61, 3, 5, 6, 7, 8, 12, 15, 18, 20, 27, 28, 29, 70]) #https://www.statisticshowto.com/upper-hinge-lower-hinge/

    def test_vv_data(self):
        result, x_low, x_upper = interquartile_range(self.vv)
        self.assertAlmostEqual(result[0], 46.0, msg="wrong IQ")
        self.assertAlmostEqual(result[1], 10.0, msg="wrong Q1")
        self.assertAlmostEqual(result[2], 56.0, msg="wrong Q3")
        self.assertListEqual(list(x_low), [3, 5, 6, 7, 8, 12, 15, 18, 20, 27], msg="wrong x_low")
        self.assertListEqual(list(x_upper), [28, 29, 33, 34, 55, 57, 60, 61, 61, 70], msg="wrong x_upper")


    def test_v_data(self):
        result, x_low, x_upper = interquartile_range(self.v)
        self.assertAlmostEqual(result[0], 47.0, msg="wrong IQ")
        self.assertAlmostEqual(result[1], 8.0, msg="wrong Q1")
        self.assertAlmostEqual(result[2], 55.0, msg="wrong Q3")
        self.assertListEqual(list(x_low), [2, 3, 5, 6, 7, 8, 12, 15, 18, 20, 27], msg="wrong x_low")
        self.assertListEqual(list(x_upper), [27, 28, 29, 33, 34, 55, 57, 60, 61, 61, 70], msg="wrong x_upper")


    def test_ww_data(self):
        result, x_low, x_upper = interquartile_range(self.ww)
        self.assertAlmostEqual(result[0], 25.0, msg="wrong IQ")
        self.assertAlmostEqual(result[1], 15.0, msg="wrong Q1")
        self.assertAlmostEqual(result[2], 40, msg="wrong Q3")
        self.assertListEqual(list(x_low), [7, 15, 36], msg="wrong x_low")
        self.assertListEqual(list(x_upper), [39, 40, 41], msg="wrong x_upper")


    def test_w_data(self):
        result, x_low, x_upper = interquartile_range(self.w)
        self.assertAlmostEqual(result[0], 17.0, msg="wrong IQ")
        self.assertAlmostEqual(result[1], 25.5, msg="wrong Q1")
        self.assertAlmostEqual(result[2], 42.5, msg="wrong Q3")
        self.assertListEqual(list(x_low), [6, 7, 15, 36, 39, 40], msg="wrong x_low")
        self.assertListEqual(list(x_upper), [40, 41, 42, 43, 47, 49], msg="wrong x_upper")


    def test_zz_data(self):
        result, x_low, x_upper = interquartile_range(self.zz)
        self.assertAlmostEqual(result[0], 5.0, msg="wrong IQ")
        self.assertAlmostEqual(result[1], 3.0, msg="wrong Q1")
        self.assertAlmostEqual(result[2], 8.0, msg="wrong Q3")
        self.assertListEqual(list(x_low), [1, 2, 3, 4, 5], msg="wrong x_low")
        self.assertListEqual(list(x_upper), [6, 7, 8, 9, 10], msg="wrong x_upper")

    def test_z_data(self):
        result, x_low, x_upper = interquartile_range(self.z)
        self.assertAlmostEqual(result[0], 5.0, msg="wrong IQ")
        self.assertAlmostEqual(result[1], 3.5, msg="wrong Q1")
        self.assertAlmostEqual(result[2], 8.5, msg="wrong Q3")
        self.assertListEqual(list(x_low), [1, 2, 3, 4, 5, 6], msg="wrong x_low")
        self.assertListEqual(list(x_upper), [6, 7, 8, 9, 10, 11], msg="wrong x_upper")


    def test_x_data(self):
        result, x_low, x_upper = interquartile_range(self.x)
        self.assertAlmostEqual(result[0], 0.4, msg="wrong IQ")
        self.assertAlmostEqual(result[1], 4.6, msg="wrong Q1")
        self.assertAlmostEqual(result[2], 5.0, msg="wrong Q3")
        self.assertListEqual(list(x_low), [4.4, 4.6, 4.6, 4.7, 4.9], msg="wrong x_low")
        self.assertListEqual(list(x_upper), [4.9, 5.0, 5.0, 5.1, 5.4], msg="wrong x_upper")

    def test_y_data(self):
        result, x_low, x_upper = interquartile_range(self.y)
        self.assertAlmostEqual(result[0], 0.9, msg="wrong IQ")
        self.assertAlmostEqual(result[1], 6.3, msg="wrong Q1")
        self.assertAlmostEqual(result[2], 7.2, msg="wrong Q3")
        self.assertListEqual(list(x_low), [4.9, 5.8, 6.3, 6.3, 6.5], msg="wrong x_low")
        self.assertListEqual(list(x_upper), [6.7, 7.1, 7.2, 7.3, 7.6], msg="wrong x_upper")

    def test_output_type(self):
        result, x_low, x_upper = interquartile_range(self.x)
        self.assertIsInstance(result, tuple, "the result is not a tuple")
        self.assertIsInstance(result[0], float, "the DI is not a float")
        self.assertIsInstance(result[1], float, "the q1 is not a float")
        self.assertIsInstance(result[1], float, "the q3 is not a float")
        self.assertIsInstance(x_low, np.ndarray, "the x_low is not a numpy array")
        self.assertIsInstance(x_upper, np.ndarray, "the x_upper is not a numpy array")


        result, x_low, x_upper = interquartile_range(self.x, language='pt-br')
        self.assertIsInstance(result, tuple, "the result is not a tuple")
        self.assertIsInstance(result[0], float, "the DI is not a float")
        self.assertIsInstance(result[1], float, "the q1 is not a float")
        self.assertIsInstance(result[1], float, "the q3 is not a float")
        self.assertIsInstance(x_low, np.ndarray, "the x_low is not a numpy array")
        self.assertIsInstance(x_upper, np.ndarray, "the x_upper is not a numpy array")








# are y read to jummmmmppppp? https://youtu.be/m9P2WJI0A_c?t=233

if __name__ == "__main__":
    unittest.main()
