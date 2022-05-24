"""Tests if the get_critical_value is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_get_critical_value
    This class tests the get_critical_value function. It should raise ValueError when n_rep is lower than 3. The function is also tested with values where it should result in a correct value by varying the n_rep and alpha parameters.


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/normalitycheck/KolmogorovSmirnov/test_get_critical_value.py
    or
    python -m unittest -b tests/normalitycheck/KolmogorovSmirnov/test_get_critical_value.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.normalitycheck.kolmogorovsmirnov import KolmogorovSmirnov
import numpy as np
os.system('cls')

class Test_get_ks_tabulated_value(unittest.TestCase):

    def test_n_rep(self):
        with self.assertRaises(ValueError, msg="Does not raised error when n_rep is negative"):
            result = KolmogorovSmirnov()
            result.get_critical_value(-10)
        with self.assertRaises(ValueError, msg="Does not raised error when n_rep is lower then 2"):
            result = KolmogorovSmirnov()
            result.get_critical_value(1)

    def test_pass(self):
        result = KolmogorovSmirnov()
        test = result.get_critical_value(3)
        self.assertEqual(test[0], 0.708, msg = "Wrong tabulated value for n_rep = 3 alpha = 0.05")
        self.assertEqual(test[1], 0.05, msg = "Wrong alpha value for n_rep = 3 alpha = 0.05")

        result = KolmogorovSmirnov()
        test = result.get_critical_value(26)
        self.assertEqual(test[0], 0.24, msg = "Wrong tabulated value for n_rep = 26 alpha = 0.05")
        self.assertEqual(test[1], 0.05, msg = "Wrong alpha value for n_rep = 26 alpha = 0.05")

        result = KolmogorovSmirnov()
        test = result.get_critical_value(26, 0.01)
        self.assertEqual(test[0], 0.29, msg = "Wrong tabulated value for n_rep = 26 alpha = 0.01")
        self.assertEqual(test[1], 0.01, msg = "Wrong alpha value for n_rep = 26 alpha = 0.01")

        result = KolmogorovSmirnov()
        test = result.get_critical_value(26, 0.1)
        self.assertEqual(test[0], 0.22, msg = "Wrong tabulated value for n_rep = 26 alpha = 0.1")
        self.assertEqual(test[1], 0.10, msg = "Wrong alpha value for n_rep = 26 alpha = 0.1")

        result = KolmogorovSmirnov()
        test = result.get_critical_value(22, 0.05)
        self.assertEqual(test[0], 0.27, msg = "Wrong tabulated value for n_rep = 22 alpha = 0.05")
        self.assertEqual(test[1], 0.05, msg = "Wrong alpha value for n_rep = 22 alpha = 0.05")

        result = KolmogorovSmirnov()
        test = result.get_critical_value(25, 0.05)
        self.assertEqual(test[0], 0.27, msg = "Wrong tabulated value for n_rep = 25 alpha = 0.05")
        self.assertEqual(test[1], 0.05, msg = "Wrong alpha value for n_rep = 25 alpha = 0.05")

        result = KolmogorovSmirnov()
        test = result.get_critical_value(30, 0.05)
        self.assertEqual(test[0], 0.24, msg = "Wrong tabulated value for n_rep = 30 alpha = 0.05")
        self.assertEqual(test[1], 0.05, msg = "Wrong alpha value for n_rep = 30 alpha = 0.05")

        result = KolmogorovSmirnov()
        test = result.get_critical_value(32, 0.05)
        self.assertEqual(test[0], 0.23, msg = "Wrong tabulated value for n_rep = 32 alpha = 0.05")
        self.assertEqual(test[1], 0.05, msg = "Wrong alpha value for n_rep = 32 alpha = 0.05")

        result = KolmogorovSmirnov()
        test = result.get_critical_value(35, 0.05)
        self.assertEqual(test[0], 0.23, msg = "Wrong tabulated value for n_rep = 35 alpha = 0.05")
        self.assertEqual(test[1], 0.05, msg = "Wrong alpha value for n_rep = 35 alpha = 0.05")



        result = KolmogorovSmirnov()
        test = result.get_critical_value(76, 0.1)
        self.assertEqual(test[0], 1.22/np.sqrt(76), msg = "Wrong tabulated value for n_rep = 76 alpha = 0.1")
        self.assertEqual(test[1], 0.10, msg = "Wrong alpha value for n_rep = 76 alpha = 0.1")

        result = KolmogorovSmirnov()
        test = result.get_critical_value(76)
        self.assertEqual(test[0], 1.36/np.sqrt(76), msg = "Wrong tabulated value for n_rep = 76 alpha = 0.05")
        self.assertEqual(test[1], 0.05, msg = "Wrong alpha value for n_rep = 76 alpha = 0.05")

    def test_pass_None(self):
        result = KolmogorovSmirnov()
        test = result.get_critical_value(26, 0.12)
        self.assertEqual(test[0], None, msg = "Wrong tabulated value for n_rep = 26 alpha = 0.12")
        self.assertEqual(test[1], 0.12, msg = "Wrong alpha value for n_rep = 26 alpha = 0.12")

        result = KolmogorovSmirnov()
        test = result.get_critical_value(22, 0.12)
        self.assertEqual(test[0], None, msg = "Wrong tabulated value for n_rep = 22 alpha = 0.12")
        self.assertEqual(test[1], 0.12, msg = "Wrong alpha value for n_rep = 22 alpha = 0.12")

        result = KolmogorovSmirnov()
        test = result.get_critical_value(5, 0.12)
        self.assertEqual(test[0], None, msg = "Wrong tabulated value for n_rep = 5 alpha = 0.12")
        self.assertEqual(test[1], 0.12, msg = "Wrong alpha value for n_rep = 5 alpha = 0.12")

        result = KolmogorovSmirnov()
        test = result.get_critical_value(33, 0.12)
        self.assertEqual(test[0], None, msg = "Wrong tabulated value for n_rep = 33 alpha = 0.12")
        self.assertEqual(test[1], 0.12, msg = "Wrong alpha value for n_rep = 33 alpha = 0.12")















if __name__ == "__main__":
    unittest.main()
