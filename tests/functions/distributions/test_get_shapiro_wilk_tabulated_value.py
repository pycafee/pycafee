"""Tests if the get_shapiro_wilk_tabulated_value is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_get_shapiro_wilk_tabulated_value
    This class tests the _get_shapiro_wilk_tabulated_value function. It should raise ValueError when alpha is not a value ranging between 0 and 1, and when n_rep is lower than 3. The function is also tested with values where it should result in a correct value by varying the n_rep and alpha parameters.


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/functions/distributions/test_get_shapiro_wilk_tabulated_value.py
    or
    python -m unittest -b tests/functions/distributions/test_get_shapiro_wilk_tabulated_value.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from cup_of_coffee.functions.distributions import ShapiroWilkNormalityTest
import numpy as np
os.system('cls')

class Test_get_shapiro_wilk_tabulated_value(unittest.TestCase):

    def test_alfa(self):
        with self.assertRaises(ValueError, msg="Does not raised error when alfa is negative"):
            result = ShapiroWilkNormalityTest()
            result.get_shapiro_wilk_tabulated_value(10, -1.0)
        with self.assertRaises(ValueError, msg="Does not raised error when alfa 1.0"):
            result = ShapiroWilkNormalityTest()
            result.get_shapiro_wilk_tabulated_value(10, 1.0)
        with self.assertRaises(ValueError, msg="Does not raised error when alfa 3.0"):
            result = ShapiroWilkNormalityTest()
            result.get_shapiro_wilk_tabulated_value(10, 3.0)

    def test_n_rep(self):
        with self.assertRaises(ValueError, msg="Does not raised error when n_rep is negative"):
            result = ShapiroWilkNormalityTest()
            result.get_shapiro_wilk_tabulated_value(-10)
        with self.assertRaises(ValueError, msg="Does not raised error when n_rep is lower then 3"):
            result = ShapiroWilkNormalityTest()
            result.get_shapiro_wilk_tabulated_value(2)

    def test_pass(self):
        result = ShapiroWilkNormalityTest()
        test= result.get_shapiro_wilk_tabulated_value(3)
        self.assertEqual(test[0], 0.767, msg = "Wrong tabulated value for n_rep = 3 alpha = 0.05")
        self.assertEqual(test[1], 0.05, msg = "Wrong alpha value for n_rep = 3 alpha = 0.05")

        result = ShapiroWilkNormalityTest()
        test = result.get_shapiro_wilk_tabulated_value(26)
        self.assertEqual(test[0], 0.920, msg = "Wrong tabulated value for n_rep = 26 alpha = 0.05")
        self.assertEqual(test[1], 0.05, msg = "Wrong alpha value for n_rep = 26 alpha = 0.05")

        result = ShapiroWilkNormalityTest()
        test = result.get_shapiro_wilk_tabulated_value(26, 0.01)
        self.assertEqual(test[0], 0.891, msg = "Wrong tabulated value for n_rep = 26 alpha = 0.01")
        self.assertEqual(test[1], 0.01, msg = "Wrong alpha value for n_rep = 26 alpha = 0.01")

        result = ShapiroWilkNormalityTest()
        test = result.get_shapiro_wilk_tabulated_value(26, 0.1)
        self.assertEqual(test[0], 0.933, msg = "Wrong tabulated value for n_rep = 26 alpha = 0.1")
        self.assertEqual(test[1], 0.10, msg = "Wrong alpha value for n_rep = 26 alpha = 0.1")

        result = ShapiroWilkNormalityTest()
        test = result.get_shapiro_wilk_tabulated_value(76, 0.1)
        self.assertEqual(test[0], 0.955, msg = "Wrong tabulated value for n_rep = 76 alpha = 0.1")
        self.assertEqual(test[1], 0.10, msg = "Wrong alpha value for n_rep = 76 alpha = 0.1")

        result = ShapiroWilkNormalityTest()
        test = result.get_shapiro_wilk_tabulated_value(76)
        self.assertEqual(test[0], 0.947, msg = "Wrong tabulated value for n_rep = 76 alpha = 0.05")
        self.assertEqual(test[1], 0.05, msg = "Wrong alpha value for n_rep = 76 alpha = 0.05")

    def test_pass_None(self):
        result = ShapiroWilkNormalityTest()
        test = result.get_shapiro_wilk_tabulated_value(26, 0.15)
        self.assertEqual(test[0], None, msg = "Wrong tabulated value for n_rep = 26 alpha = 0.15")
        self.assertEqual(test[1], 0.15, msg = "Wrong alpha value for n_rep = 26 alpha = 0.15")
















if __name__ == "__main__":
    unittest.main()
