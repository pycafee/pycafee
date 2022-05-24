"""Tests if the fit function for get_critical_value is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_get_critical_value
    This class tests the get_critical_value function. The test checks if the correct value is returned for each alfa value, if its value is None for alfa not supported. The function checks different n_rep, and also if it raises ValueError if n_rep is less than 4.


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/normalitycheck/AbdiMolin/test_get_critical_value.py
    or
    python -m unittest -b tests/normalitycheck/AbdiMolin/test_get_critical_value.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.normalitycheck.abdimolin import AbdiMolin
import numpy as np
os.system('cls')

class Test_get_critical_value(unittest.TestCase):


    def test_basic(self):
        test = AbdiMolin()
        resultado, alfa = test.get_critical_value(5)
        self.assertEqual(resultado, 0.3427, "wrong critical value")
        self.assertEqual(alfa, 0.05, "wrong alfa value")

        resultado, alfa = test.get_critical_value(10)
        self.assertEqual(resultado, 0.2616, "wrong critical value")
        self.assertEqual(alfa, 0.05, "wrong alfa value")

        resultado, alfa = test.get_critical_value(28)
        self.assertEqual(resultado, 0.1641, "wrong critical value")
        self.assertEqual(alfa, 0.05, "wrong alfa value")

        resultado, alfa = test.get_critical_value(50)
        self.assertEqual(resultado, 0.1246, "wrong critical value")
        self.assertEqual(alfa, 0.05, "wrong alfa value")


    def test_n_rep_higher_50(self):
        test = AbdiMolin()
        resultado, alfa = test.get_critical_value(51)
        self.assertEqual(resultado, 0.1234882745570323, "wrong critical value")
        self.assertEqual(alfa, 0.05, "wrong alfa value")

        resultado, alfa = test.get_critical_value(55, alfa=0.01)
        self.assertEqual(resultado, 0.13766747496578266, "wrong critical value")
        self.assertEqual(alfa, 0.01, "wrong alfa value")

        resultado, alfa = test.get_critical_value(65, alfa=0.10)
        self.assertEqual(resultado, 0.10042664059652683, "wrong critical value")
        self.assertEqual(alfa, 0.10, "wrong alfa value")

        resultado, alfa = test.get_critical_value(60, alfa=0.15)
        self.assertEqual(resultado, 0.09881272706802652, "wrong critical value")
        self.assertEqual(alfa, 0.15, "wrong alfa value")

        resultado, alfa = test.get_critical_value(58, alfa=0.20)
        self.assertEqual(resultado, 0.09604968208910362, "wrong critical value")
        self.assertEqual(alfa, 0.20, "wrong alfa value")


    def test_alfa_not_supported(self):
        test = AbdiMolin()
        resultado, alfa = test.get_critical_value(10, alfa=0.02)
        self.assertIsNone(resultado, "Not None for alfa = 0.02")
        self.assertEqual(alfa, 0.02, "wrong alfa value")

        resultado, alfa = test.get_critical_value(10, alfa=0.16)
        self.assertIsNone(resultado, "Not None for alfa = 0.16")
        self.assertEqual(alfa, 0.16, "wrong alfa value")

        resultado, alfa = test.get_critical_value(10, alfa=0.75)
        self.assertIsNone(resultado, "Not None for alfa = 0.75")
        self.assertEqual(alfa, 0.75, "wrong alfa value")


    def test_alfa(self):
        test = AbdiMolin()
        resultado, alfa = test.get_critical_value(10, alfa=0.01)
        self.assertEqual(resultado, 0.3037, "wrong critical value")
        self.assertEqual(alfa, 0.01, "wrong alfa value")

        resultado, alfa = test.get_critical_value(5, alfa=0.05)
        self.assertEqual(resultado, 0.3427, "wrong critical value")
        self.assertEqual(alfa, 0.05, "wrong alfa value")

        resultado, alfa = test.get_critical_value(28, alfa=0.10)
        self.assertEqual(resultado, 0.1509, "wrong critical value")
        self.assertEqual(alfa, 0.10, "wrong alfa value")

        resultado, alfa = test.get_critical_value(33, alfa=0.15)
        self.assertEqual(resultado, 0.1314, "wrong critical value")
        self.assertEqual(alfa, 0.15, "wrong alfa value")

        resultado, alfa = test.get_critical_value(50, alfa=0.20)
        self.assertEqual(resultado, 0.1030, "wrong critical value")
        self.assertEqual(alfa, 0.20, "wrong alfa value")


    def test_n_rep_raise(self):
        with self.assertRaises(ValueError, msg="Does not raised error when n_rep = 1"):
            test = AbdiMolin()
            resultado, alfa = test.get_critical_value(1, alfa=0.01)

        with self.assertRaises(ValueError, msg="Does not raised error when n_rep = -1"):
            test = AbdiMolin()
            resultado, alfa = test.get_critical_value(-1, alfa=0.01)

        with self.assertRaises(ValueError, msg="Does not raised error when n_rep = 0"):
            test = AbdiMolin()
            resultado, alfa = test.get_critical_value(-1, alfa=0.01)




# https://youtu.be/yGuuQ_45aTU?t=36


if __name__ == "__main__":
    unittest.main()
