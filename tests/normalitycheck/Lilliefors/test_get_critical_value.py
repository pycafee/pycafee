"""Tests if the get_get_critical_value is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_get_critical_value
    This class tests the get_critical_value function. It should raise ValueError when n_rep is lower than 4. The function is also tested with values where it should result in a correct value by varying the n_rep and alpha parameters.


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/normalitycheck/Lilliefors/test_get_critical_value.py
    or
    python -m unittest -b tests/normalitycheck/Lilliefors/test_get_critical_value.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.normalitycheck.lilliefors import Lilliefors
import numpy as np
os.system('cls')

class Test_get_critical_value(unittest.TestCase):



    def test_n_rep(self):
        with self.assertRaises(ValueError, msg="Does not raised error when n_rep is negative"):
            result = Lilliefors()
            result.get_critical_value(-10)
        with self.assertRaises(ValueError, msg="Does not raised error when n_rep is lower then 4"):
            result = Lilliefors()
            result.get_critical_value(3)


    def test_pass_original(self):
        result = Lilliefors()
        test = result.get_critical_value(5, alfa=0.01)
        self.assertEqual(test[0], 0.405, msg = "Wrong tabulated value for n_rep = 5 alpha = 0.01")
        self.assertEqual(test[1], 0.01, msg = "Wrong alpha value for n_rep = 5 alpha = 0.01")

        result = Lilliefors()
        test = result.get_critical_value(20, alfa=0.01)
        self.assertEqual(test[0], 0.231, msg = "Wrong tabulated value for n_rep = 20 alpha = 0.01")
        self.assertEqual(test[1], 0.01, msg = "Wrong alpha value for n_rep = 20 alpha = 0.01")

        result = Lilliefors()
        test = result.get_critical_value(22, alfa=0.01)
        self.assertEqual(test[0], 0.203, msg = "Wrong tabulated value for n_rep = 22 alpha = 0.01")
        self.assertEqual(test[1], 0.01, msg = "Wrong alpha value for n_rep = 22 alpha = 0.01")

        result = Lilliefors()
        test = result.get_critical_value(25, alfa=0.01)
        self.assertEqual(test[0], 0.203, msg = "Wrong tabulated value for n_rep = 25 alpha = 0.01")
        self.assertEqual(test[1], 0.01, msg = "Wrong alpha value for n_rep = 25 alpha = 0.01")

        result = Lilliefors()
        test = result.get_critical_value(26, alfa=0.01)
        self.assertEqual(test[0], 0.187, msg = "Wrong tabulated value for n_rep = 26 alpha = 0.01")
        self.assertEqual(test[1], 0.01, msg = "Wrong alpha value for n_rep = 26 alpha = 0.01")

        result = Lilliefors()
        test = result.get_critical_value(30, alfa=0.01)
        self.assertEqual(test[0], 0.187, msg = "Wrong tabulated value for n_rep = 30 alpha = 0.01")
        self.assertEqual(test[1], 0.01, msg = "Wrong alpha value for n_rep = 30 alpha = 0.01")

        result = Lilliefors()
        test = result.get_critical_value(35, alfa=0.01)
        self.assertEqual(test[0], 0.1742708073250201, msg = "Wrong tabulated value for n_rep = 35 alpha = 0.01")
        self.assertEqual(test[1], 0.01, msg = "Wrong alpha value for n_rep = 35 alpha = 0.01")



    def test_pass_None(self):
        result = Lilliefors()
        test = result.get_critical_value(5, alfa=0.13)
        self.assertIsNone(test[0], msg = "Not None for n_rep=51 alfa=0.13")
        self.assertEqual(test[1], 0.13, msg = "Wrong alpha value for n_rep = 51 alpha = 0.13")

        result = Lilliefors()
        test = result.get_critical_value(13, alfa=0.07)
        self.assertIsNone(test[0], msg = "Not None for n_rep=13 alfa=0.07")
        self.assertEqual(test[1], 0.07, msg = "Wrong alpha value for n_rep = 13 alpha = 0.07")













if __name__ == "__main__":
    unittest.main()
