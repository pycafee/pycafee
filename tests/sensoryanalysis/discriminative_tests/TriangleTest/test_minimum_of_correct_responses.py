"""Tests if the minimum_of_correct_responses is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_minimum_of_correct_responses.



--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sensoryanalysis/discriminative_tests/TriangleTest/test_minimum_of_correct_responses.py
    or
    python -m unittest -b tests/sensoryanalysis/discriminative_tests/TriangleTest/test_minimum_of_correct_responses.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sensoryanalysis.discriminative_tests import TriangleTest
import numpy as np
import io
import sys
os.system('cls')

class Test_minimum_of_correct_responses(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
         # 0,20; 0,10; 0,05; 0,01; 0,001
        cls.critical_e1885 = {
            6:	[4,	5,	5, 6],
            7:	[4,	5,	5, 6, 7],
            8:	[5,	5,	6, 7, 8],
            9:	[5,	6,	6, 7, 8],
            10:	[6,	6,	7, 8, 9],
            11:	[6,	7,	7, 8, 10],
            12:	[6,	7,	8, 9, 10],
            13:	[7,	8,	8, 9, 11],
            14:	[7,	8,	9, 10, 11],
            15:	[8,	8,	9, 10, 12],
            16:	[8,	9,	9, 11, 12],
            17:	[8,	9,	10, 11, 13],
            18:	[9,	10,	10, 12, 13],
            19:	[9,	10,	11, 12, 14],
            20:	[9,	10, 11, 13, 14],
            21:	[10, 11, 12, 13, 15],
            22:	[10, 11, 12, 14, 15],
            23:	[11, 12, 12, 14, 16],
            24:	[11, 12, 13, 15, 16],
            25:	[11, 12, 13, 15, 17],
            26:	[12, 13, 14, 15, 17],
            27:	[12, 13, 14, 16, 18],
            28:	[12, 14, 15, 16, 18],
            29:	[13, 14, 15, 17, 19],
            30:	[13, 14, 15, 17, 19],
            31:	[14, 15, 16, 18, 20],
            32:	[14, 15, 16, 18, 20],
            33:	[14, 15, 17, 18, 21],
            34:	[15, 16, 17, 19, 21],
            35:	[15, 16, 17, 19, 22],
            36:	[15, 17, 18, 20, 22],
            37:	[16, 17, 18, 20, 22],
            38:	[16, 17, 19, 21, 23],
            39:	[16, 18, 19, 21, 23],
            40:	[17, 18, 19, 21, 24],
            41:	[17, 19, 20, 22, 24],
            42:	[18, 19, 20, 22, 25],
            43:	[18, 19, 20, 23, 25],
            44:	[18, 20, 21, 23, 26],
            45:	[19, 20, 21, 24, 26],
            46:	[19, 20, 22, 24, 27],
            47:	[19, 21, 22, 24, 27],
            48:	[20, 21, 22, 25, 27],
            54:	[22, 23, 25, 27, 30],
            60:	[24, 26, 27, 30, 33],
            66:	[26, 28, 29, 32, 35],
            72:	[28, 30, 32, 34, 38],
            78:	[30, 32, 34, 37, 40],
            84:	[33, 35, 36, 39, 43],
            90:	[35, 37, 38, 42, 45],
            96:	[37, 39, 41, 44, 48],
            102: [39, 41, 43, 46, 50],
        }

         # 0,05; 0,04; 0,03; 0,02; 0,01; 0,005; 0,001
        cls.critical_roessler = {
            # 5:	[4, 5, 5, 5, 5, 5],
            6:	[5, 5, 5, 5, 6, 6],
            7:	[5, 6, 6, 6, 6, 7, 7],
            8:	[6, 6, 6, 6, 7, 7, 8],
            9:	[6, 7, 7, 7, 7, 8, 8],
            10:	[7, 7, 7, 7, 8, 8, 9],
            11:	[7, 7, 8, 8, 8, 9, 10],
            12:	[8, 8, 8, 8, 9, 9, 10],
            13:	[8, 8, 9, 9, 9, 10, 11],
            14:	[9, 9, 9, 9, 10, 10, 11],
            15:	[9, 9, 10, 10, 10, 11, 12],
            16:	[9, 10, 10, 10, 11, 11, 12],
            17:	[10, 10, 10, 11, 11, 12, 13],
            18:	[10, 11, 11, 11, 12, 12, 13],
            19:	[11, 11, 11, 12, 12, 13, 14],
            20:	[11, 11, 12, 12, 13, 13, 14],
            21:	[12, 12, 12, 13, 13, 14, 15],
            22:	[12, 12, 13, 13, 14, 14, 15],
            23:	[12, 13, 13, 13, 14, 15, 16],
            24:	[13, 13, 13, 14, 15, 15, 16],
            25:	[13, 14, 14, 14, 15, 16, 17],
            26:	[14, 14, 14, 15, 15, 16, 17],
            27:	[14, 14, 15, 15, 16, 17, 18],
            28:	[15, 15, 15, 16, 16, 17, 18],
            29:	[15, 15, 16, 16, 17, 17, 19],
            30:	[15, 16, 16, 16, 17, 18, 19],
            31:	[16, 16, 16, 17, 18, 18, 20],
            32:	[16, 16, 17, 17, 18, 19, 20],
            33:	[17, 17, 17, 18, 18, 19, 21],
            34:	[17, 17, 18, 18, 19, 20, 21],
            35:	[17, 18, 18, 19, 19, 20, 22],
            36:	[18, 18, 18, 19, 20, 20, 22],
            37:	[18, 18, 19, 19, 20, 21, 22],
            38:	[19, 19, 19, 20, 21, 21, 23],
            39:	[19, 19, 20, 20, 21, 22, 23],
            40:	[19, 20, 20, 21, 21, 22, 24],
            41:	[20, 20, 20, 21, 22, 23, 24],
            42:	[20, 20, 21, 21, 22, 23, 25],
            43:	[20, 21, 21, 22, 23, 24, 25],
            44:	[21, 21, 22, 22, 23, 24, 26],
            45:	[21, 22, 22, 23, 24, 24, 26],
            46:	[22, 22, 22, 23, 24, 25, 27],
            47:	[22, 22, 23, 23, 24, 25, 27],
            48:	[22, 23, 23, 24, 25, 26, 27],
            49:	[23, 23, 24, 24, 25, 26, 28],
            50:	[23, 24, 24, 25, 26, 26, 28],
            60:	[27, 27, 28, 29, 30, 31, 33],
            70:	[31, 31, 32, 33, 34, 35, 37],
            80:	[35, 35, 36, 36, 38, 39, 41],
            90:	[38, 39, 40, 40, 42, 43, 45],
            # 100: [42, 43, 43, 44, 45, 47, 49]  For alfa = 0.01 the value does not match
            100: [42, 43, 43, 44, 46, 47, 49]
        }



    def test_output(self):
        test = TriangleTest()
        result, input = test.minimum_of_correct_responses(10)
        self.assertIsInstance(result[0], (int, np.uint, np.integer), "the number of assessors is not an int")
        self.assertIsInstance(input, dict, "the input is not a dict")
        self.assertEqual(len(input), 2, msg="dict size does not match")
        self.assertIsInstance(input['alpha'], float, msg="alfa not float")
        self.assertIsInstance(input['n_of_assessors'], int, msg="n_of_assessors not int")



    def test_alfa_0_2_e1885(self):
        alfa = 0.2
        for n_assessors in self.critical_e1885.keys():
            test = TriangleTest()
            result, input = test.minimum_of_correct_responses(n_assessors, alfa=alfa)
            self.assertEqual(result[0], self.critical_e1885[n_assessors][0], msg="wrong critical value")

    def test_alfa_0_10_e1885(self):
        alfa = 0.10
        for n_assessors in self.critical_e1885.keys():
            test = TriangleTest()
            result, input = test.minimum_of_correct_responses(n_assessors, alfa=alfa)
            self.assertEqual(result[0], self.critical_e1885[n_assessors][1], msg="wrong critical value")

    def test_alfa_0_05_e1885(self):
        alfa = 0.05
        for n_assessors in self.critical_e1885.keys():
            test = TriangleTest()
            result, input = test.minimum_of_correct_responses(n_assessors, alfa=alfa)
            self.assertEqual(result[0], self.critical_e1885[n_assessors][2], msg="wrong critical value")


    def test_alfa_0_01_e1885(self):
        alfa = 0.01
        for n_assessors in self.critical_e1885.keys():
            test = TriangleTest()
            result, input = test.minimum_of_correct_responses(n_assessors, alfa=alfa)
            self.assertEqual(result[0], self.critical_e1885[n_assessors][3], msg="wrong critical value")


    def test_alfa_0_001_e1885(self):
        alfa = 0.001
        for n_assessors in self.critical_e1885.keys():
            test = TriangleTest()
            try:
                result, input = test.minimum_of_correct_responses(n_assessors, alfa=alfa)
                self.assertEqual(result[0], self.critical_e1885[n_assessors][4], msg="wrong critical value")
            except IndexError:
                pass


    def test_alfa_0_05_roessler(self):
        alfa = 0.05
        for n_assessors in self.critical_roessler.keys():
            test = TriangleTest()
            result, input = test.minimum_of_correct_responses(n_assessors, alfa=alfa)
            self.assertEqual(result[0], self.critical_roessler[n_assessors][0], msg="wrong critical value")


    def test_alfa_0_01_roessler(self):
        alfa = 0.01
        for n_assessors in self.critical_roessler.keys():
            test = TriangleTest()
            result, input = test.minimum_of_correct_responses(n_assessors, alfa=alfa)
            self.assertEqual(result[0], self.critical_roessler[n_assessors][4], msg="wrong critical value")


    def test_alfa_0_001_roessler(self):
        alfa = 0.001
        for n_assessors in self.critical_roessler.keys():
            test = TriangleTest()
            try:
                result, input = test.minimum_of_correct_responses(n_assessors, alfa=alfa)
                self.assertEqual(result[0], self.critical_roessler[n_assessors][6], msg="wrong critical value")
            except IndexError:
                pass


# are y read to jummmmmppppp? https://youtu.be/m9P2WJI0A_c?t=233

if __name__ == "__main__":
    unittest.main()
