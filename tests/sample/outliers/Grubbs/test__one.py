"""Tests if the test_test__one is working as expected

---> Class Test__pass


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sample/outliers/Grubbs/test__one.py
    or
    python -m unittest -b tests/sample/outliers/Grubbs/test__one.py

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
        result = teste._one(self.x, which="min")
        self.assertAlmostEqual(result, 0.8452, places=3, msg="wrong lower value")

        result = teste._one(self.y, which="min")
        self.assertAlmostEqual(result, 1.173477388, places=7, msg="wrong lower value")
        #
        result = teste._one(self.z, which="min")
        self.assertAlmostEqual(result, 1.834455799, places=7, msg="wrong lower value")

    def test_upper(self):
        teste = Grubbs()
        result = teste._one(self.x, which="max")
        self.assertAlmostEqual(result, 2.153, places=3, msg="wrong upper value")

        result = teste._one(self.y, which="max")
        self.assertAlmostEqual(result, 1.802125989, places=7, msg="wrong upper value")

        result = teste._one(self.z, which="max")
        self.assertAlmostEqual(result, 2.242112644, places=7, msg="wrong upper value")



if __name__ == "__main__":
    unittest.main()
