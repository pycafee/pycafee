"""Tests if the test_test__one is working as expected

---> Class Test__pass


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sample/outliers/Grubbs/test__two.py
    or
    python -m unittest -b tests/sample/outliers/Grubbs/test__two.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sample.outliers import Grubbs
import numpy as np
os.system('cls')


class Test_pass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([147, 150, 153, 153, 156, 159, 184])
        cls.y = np.array([9, 16, 23, 41, 44, 46, 80])
        z = np.array([15.42, 15.51, 15.52, 15.53, 15.68, 15.52, 15.56, 15.53, 15.54, 15.56])
        z.sort(kind='quicksort')
        cls.z = z

    def test_lower(self):
        teste = Grubbs()
        result = teste._two(self.x, which="min")
        self.assertAlmostEqual(result, 0.751, places=3, msg="wrong lower value")

        result = teste._two(self.y, which="min")
        self.assertAlmostEqual(result, 0.500819672, places=7, msg="wrong lower value")

        result = teste._two(self.z, which="min")
        self.assertAlmostEqual(result, 0.535372849, places=7, msg="wrong lower value")

    def test_upper(self):
        teste = Grubbs()
        result = teste._two(self.x, which="max")
        self.assertAlmostEqual(result, 0.051, places=3, msg="wrong upper value")

        result = teste._two(self.y, which="max")
        self.assertAlmostEqual(result, 0.276697892, places=7, msg="wrong upper value")

        result = teste._two(self.z, which="max")
        self.assertAlmostEqual(result, 0.3329008479, places=7, msg="wrong upper value")



if __name__ == "__main__":
    unittest.main()
