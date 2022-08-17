"""Tests if the get_number_assessors is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_get_number_assessors.



--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sensoryanalysis/discriminative_tests/TriangleTest/test_get_number_assessors.py
    or
    python -m unittest -b tests/sensoryanalysis/discriminative_tests/TriangleTest/test_get_number_assessors.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sensoryanalysis.discriminative_tests import TriangleTest
import numpy as np
os.system('cls')

class Test_get_number_assessors(unittest.TestCase):

    def test_output(self):
        test = TriangleTest()
        result, input = test.get_number_assessors(pd=None, beta=None, alfa=None)
        self.assertIsInstance(result[0], (int, np.uint, np.integer), "the number of assessors is not an int")
        self.assertIsInstance(input, dict, "the input is not a dict")


    def test_results(self):
        test = TriangleTest()
        result, input = test.get_number_assessors(pd=None, beta=None, alfa=None)
        self.assertEqual(result[0], 66, msg="wrong minimum value")
        self.assertEqual(input["pd"], "30%", msg="wrong pd value")
        self.assertEqual(input["alpha"], 0.05, msg="wrong alfa value")
        self.assertEqual(input["beta"], 0.05, msg="wrong beta value")


        result, input = test.get_number_assessors(pd="10%", beta=None, alfa=None)
        self.assertEqual(result[0], 572, msg="wrong minimum value")
        self.assertEqual(input["pd"], "10%", msg="wrong pd value")
        self.assertEqual(input["alpha"], 0.05, msg="wrong alfa value")
        self.assertEqual(input["beta"], 0.05, msg="wrong beta value")

        result, input = test.get_number_assessors(pd="50%", beta=0.10, alfa=None)
        self.assertEqual(result[0], 20, msg="wrong minimum value")
        self.assertEqual(input["pd"], "50%", msg="wrong pd value")
        self.assertEqual(input["alpha"], 0.05, msg="wrong alfa value")
        self.assertEqual(input["beta"], 0.10, msg="wrong beta value")

        result, input = test.get_number_assessors(pd="40%", beta=0.01, alfa=0.10)
        self.assertEqual(result[0], 46, msg="wrong minimum value")
        self.assertEqual(input["pd"], "40%", msg="wrong pd value")
        self.assertEqual(input["alpha"], 0.10, msg="wrong alfa value")
        self.assertEqual(input["beta"], 0.01, msg="wrong beta value")


        result, input = test.get_number_assessors(pd="10%", beta=0.001, alfa=0.001)
        self.assertEqual(result[0], 1992, msg="wrong minimum value")
        self.assertEqual(input["pd"], "10%", msg="wrong pd value")
        self.assertEqual(input["alpha"], 0.001, msg="wrong alfa value")
        self.assertEqual(input["beta"], 0.001, msg="wrong beta value")






# are y read to jummmmmppppp? https://youtu.be/m9P2WJI0A_c?t=233

if __name__ == "__main__":
    unittest.main()
