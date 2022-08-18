"""Tests if the _min_responses is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test__min_responses.



--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sensoryanalysis/discriminative_tests/TriangleTest/test__min_responses.py
    or
    python -m unittest -b tests/sensoryanalysis/discriminative_tests/TriangleTest/test__min_responses.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sensoryanalysis.discriminative_tests import _min_responses
import numpy as np
os.system('cls')

class Test__min_responses(unittest.TestCase):

    def test_output_type(self):
        result = _min_responses(10, 0.05)
        self.assertIsInstance(result, (int, np.uint, np.integer), "the result is not an int")



    def test_results(self):
        alfa = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05,
        0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
        0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001]

        n = [11, 114, 68, 75, 109, 92, 60, 165, 182, 177, 13, 89, 42, 15, 115, 103, 16, 138, 88, 158, 43, 18,
        80, 111, 189, 135, 143, 8, 74, 45, 69, 48, 42, 200, 57, 107, 137, 142, 20, 177, 147, 167, 27, 170, 40,
        28, 41, 38, 138]

        resultado = [6, 43, 27, 29, 41, 35, 26, 64, 70, 68, 8, 36, 20, 9, 48, 43, 9, 56, 38, 63, 20, 10, 35, 46, 79, 59,
            62, 7, 35, 23, 33, 25, 22, 83, 28, 52, 64, 66, 14, 79, 68, 75, 18, 77, 24, 18, 24, 23, 64]

        for i in range(len(alfa)):
            result = _min_responses(n[i], alfa[i])
            self.assertEqual(result, resultado[i], msg="wrong result")






# are y read to jummmmmppppp? https://youtu.be/m9P2WJI0A_c?t=233

if __name__ == "__main__":
    unittest.main()
