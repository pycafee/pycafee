"""Tests if the get_get_critical_value is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_get_critical_value
    This class tests the get_critical_value function. It should raise ValueError when n_rep is lower than 4. The function is also tested with values where it should result in a correct value by varying the n_rep and alpha parameters.


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/normalitycheck/ShapiroWilk/test_get_critical_value.py
    or
    python -m unittest -b tests/normalitycheck/ShapiroWilk/test_get_critical_value.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.normalitycheck.shapirowilk import ShapiroWilk
import numpy as np
os.system('cls')

class Test_get_critical_value(unittest.TestCase):



    def test_n_rep(self):
        with self.assertRaises(ValueError, msg="Does not raised error when n_rep is negative"):
            result = ShapiroWilk()
            result.get_critical_value(-10)
        with self.assertRaises(ValueError, msg="Does not raised error when n_rep is lower then 3"):
            result = ShapiroWilk()
            result.get_critical_value(2)


    def test_pass_original(self):
        result = ShapiroWilk()
        test = result.get_critical_value(5, alfa=0.01)
        self.assertEqual(test[0], 0.686, msg = "Wrong tabulated value for n_rep = 5 alpha = 0.01")
        self.assertEqual(test[1], 0.01, msg = "Wrong alpha value for n_rep = 5 alpha = 0.01")

        result = ShapiroWilk()
        test = result.get_critical_value(20, alfa=0.05)
        self.assertEqual(test[0], 0.905, msg = "Wrong tabulated value for n_rep = 20 alpha = 0.05")
        self.assertEqual(test[1], 0.05, msg = "Wrong alpha value for n_rep = 20 alpha = 0.05")

        result = ShapiroWilk()
        test = result.get_critical_value(22, alfa=0.02)
        self.assertEqual(test[0], 0.892, msg = "Wrong tabulated value for n_rep = 22 alpha = 0.02")
        self.assertEqual(test[1], 0.02, msg = "Wrong alpha value for n_rep = 22 alpha = 0.02")

        result = ShapiroWilk()
        test = result.get_critical_value(25, alfa=0.10)
        self.assertEqual(test[0], 0.931, msg = "Wrong tabulated value for n_rep = 25 alpha = 0.10")
        self.assertEqual(test[1], 0.10, msg = "Wrong alpha value for n_rep = 25 alpha = 0.1")

        result = ShapiroWilk()
        test = result.get_critical_value(26, alfa=0.01)
        self.assertEqual(test[0], 0.891, msg = "Wrong tabulated value for n_rep = 26 alpha = 0.01")
        self.assertEqual(test[1], 0.01, msg = "Wrong alpha value for n_rep = 26 alpha = 0.01")

        result = ShapiroWilk()
        test = result.get_critical_value(30, alfa=0.01)
        self.assertEqual(test[0], 0.900, msg = "Wrong tabulated value for n_rep = 30 alpha = 0.01")
        self.assertEqual(test[1], 0.01, msg = "Wrong alpha value for n_rep = 30 alpha = 0.01")

        result = ShapiroWilk()
        test = result.get_critical_value(35, alfa=0.01)
        self.assertEqual(test[0], 0.910, msg = "Wrong tabulated value for n_rep = 35 alpha = 0.01")
        self.assertEqual(test[1], 0.01, msg = "Wrong alpha value for n_rep = 35 alpha = 0.01")



    def test_pass_None(self):
        result = ShapiroWilk()
        test = result.get_critical_value(5, alfa=0.13)
        self.assertIsNone(test[0], msg = "Not None for alfa=0.13")
        self.assertEqual(test[1], 0.13, msg = "Wrong alpha value for n_rep = 51 alpha = 0.13")

        result = ShapiroWilk()
        test = result.get_critical_value(13, alfa=0.07)
        self.assertIsNone(test[0], msg = "Not None for alfa=0.07")
        self.assertEqual(test[1], 0.07, msg = "Wrong alpha value for n_rep = 13 alpha = 0.07")








# look at my face https://youtu.be/aD_tTsaskBo?t=175




if __name__ == "__main__":
    unittest.main()
