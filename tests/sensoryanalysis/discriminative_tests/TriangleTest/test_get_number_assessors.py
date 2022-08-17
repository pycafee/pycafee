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

os.system('cls')

class Test_get_number_assessors(unittest.TestCase):

    def test_output(self):
        test = TriangleTest()
        result, input = test.get_number_assessors(pd=None, beta=None, alfa=None)
        self.assertIsInstance(result, (int, np.uint, np.integer), "the number of assessors is not an int")
        self.assertIsInstance(input, dict, "the input is not a dict")









# are y read to jummmmmppppp? https://youtu.be/m9P2WJI0A_c?t=233

if __name__ == "__main__":
    unittest.main()
