"""Tests if the test__r22 is working as expected

---> Class Test__pass


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sample/Dixon/test__r22.py
    or
    python -m unittest -b tests/sample/Dixon/test__r22.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sample.dixon import Dixon
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
        teste = Dixon()
        result = teste._r22(self.x, which="min")
        self.assertAlmostEqual(result, 0.666666667, places=7, msg="wrong min value")

        result = teste._r22(self.y, which="min")
        self.assertAlmostEqual(result, 0.4, places=7, msg="wrong lower value")

        result = teste._r22(self.z, which="min")
        self.assertAlmostEqual(result, 0.714285714, places=7, msg="wrong lower value")

    def test_upper(self):
        teste = Dixon()
        result = teste._r22(self.x, which="max")
        self.assertAlmostEqual(result, 0.903225806, places=7, msg="wrong upper value")

        result = teste._r22(self.y, which="max")
        self.assertAlmostEqual(result, 0.631578947, places=7, msg="wrong upper value")

        result = teste._r22(self.z, which="max")
        self.assertAlmostEqual(result, 0.75, places=7, msg="wrong upper value")



if __name__ == "__main__":
    unittest.main()
