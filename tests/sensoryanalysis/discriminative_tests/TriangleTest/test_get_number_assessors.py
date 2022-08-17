"""Tests if the get_number_assessors is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_get_number_assessors.



--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/discriminative_tests/discriminative_tests/TriangleTest/test_get_number_assessors.py
    or
    python -m unittest -b tests/discriminative_tests/discriminative_tests/TriangleTest/test_get_number_assessors.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sensoryanalysis.d import get_number_assessors
import numpy as np
os.system('cls')

class Test_get_number_assessors(unittest.TestCase):

    def test_output(self):
        x = np.array([1, 1, 2, 3, 4, 5])
        result = multimode(x)
        data = list(result.items())
        self.assertIsInstance(result, dict, "the output is not a dict")
        self.assertIsInstance(data[0][0], (int, np.uint, np.integer), "the key is not an int")
        self.assertIsInstance(data[0][1], (int, np.uint, np.integer), "the value is not an int")








# are y read to jummmmmppppp? https://youtu.be/m9P2WJI0A_c?t=233

if __name__ == "__main__":
    unittest.main()
