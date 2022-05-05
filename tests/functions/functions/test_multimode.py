"""Tests if the multimode is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_multimode. This class tests the multimode against the output type and against modal, bimodal and 3modal data



--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/functions/functions/test_multimode.py
    or
    python -m unittest -b tests/functions/functions/test_multimode.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.functions.functions import multimode
import numpy as np
os.system('cls')

class Test_multimode(unittest.TestCase):

    def test_output(self):
        x = np.array([1, 1, 2, 3, 4, 5])
        result = multimode(x)
        data = list(result.items())
        self.assertIsInstance(result, dict, "the output is not a dict")
        self.assertIsInstance(data[0][0], (int, np.uint, np.integer), "the key is not an int")
        self.assertIsInstance(data[0][1], (int, np.uint, np.integer), "the value is not an int")

        x = np.array([1.1, 1.1, 2.1, 3.1, 4.1, 5.1])
        result = multimode(x)
        data = list(result.items())
        self.assertIsInstance(result, dict, "the output is not a dict")
        self.assertIsInstance(data[0][0], (float, np.floating), "the key is not an float")
        self.assertIsInstance(data[0][1], (int, np.uint, np.integer), "the value is not an int")


        x = np.array([1, 2, 3, 4, 5])
        result = multimode(x)
        data = list(result.items())
        self.assertIsInstance(result, dict, "the output is not a dict")
        self.assertIsNone(data[0][0], "the key is not None")
        self.assertIsInstance(data[0][1], str, "the value is not an str")

    def test_unimodal(self):
        x = np.array([1, 2, 3, 3, 3, 3, 4, 5])
        result = multimode(x)
        data = list(result.items())
        self.assertEqual(data[0][0], 3, "the mode is not 3")
        self.assertEqual(data[0][1], 4, "the count of the mode is not 4")
        self.assertEqual(len(result), 1, "the dict does not have 1 mode")

    def test_bimodal(self):
        x = np.array([1, 2, 3, 3, 3, 3, 4, 5, 6, 6, 6, 6])
        result = multimode(x)
        print(result)
        data = list(result.items())
        self.assertEqual(data[0][0], 3, "the first mode is not 3")
        self.assertEqual(data[0][1], 4, "the count of the fisrt mode is not 4")
        self.assertEqual(data[1][0], 6, "the sencond mode is not 6")
        self.assertEqual(data[1][1], 4, "the count of the second mode is not 4")
        self.assertEqual(len(result), 2, "the dict does not have 2 mode")

    def test_3modal(self):
        x = np.array([1, 1, 1, 1, 2, 3, 3, 3, 3, 4, 5, 6, 6, 6, 6])
        result = multimode(x)
        print(result)
        data = list(result.items())
        self.assertEqual(data[0][0], 1, "the first mode is not 1")
        self.assertEqual(data[0][1], 4, "the count of the first mode is not 4")
        self.assertEqual(data[1][0], 3, "the second mode is not 2")
        self.assertEqual(data[1][1], 4, "the count of the second mode is not 4")
        self.assertEqual(data[2][0], 6, "the third mode is not 6")
        self.assertEqual(data[2][1], 4, "the count of the third mode is not 4")
        self.assertEqual(len(result), 3, "the dict does not have 3 mode")

    def test_3modal_reverse(self):
        x = np.array([6, 6, 6, 6, 5, 4, 3, 3, 3, 3, 2, 1, 1, 1, 1])

        result = multimode(x)
        print(result)
        data = list(result.items())
        self.assertEqual(data[0][0], 6, "the first mode is not 6")
        self.assertEqual(data[0][1], 4, "the count of the first mode is not 4")
        self.assertEqual(data[1][0], 3, "the second mode is not 2")
        self.assertEqual(data[1][1], 4, "the count of the second mode is not 4")
        self.assertEqual(data[2][0], 1, "the third mode is not 6")
        self.assertEqual(data[2][1], 4, "the count of the third mode is not 1")
        self.assertEqual(len(result), 3, "the dict does not have 3 mode")







# are y read to jummmmmppppp? https://youtu.be/m9P2WJI0A_c?t=233

if __name__ == "__main__":
    unittest.main()
