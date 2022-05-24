"""Tests if the fit function for Lilliefors is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_fit
    This class tests the fit function. It should raise ValueError conclustion or detail got worng key. The function is tests against correct output, when data is Normal and when data is Not Normal.


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/normalitycheck/AbdiMolin/test_fit.py
    or
    python -m unittest -b tests/normalitycheck/Lilliefors/test_fit.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.normalitycheck.abdimolin import AbdiMolin
import numpy as np
os.system('cls')

class Test_fit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        cls.x_not_normal = np.array([1, 1, 1, 1.1, 1.2, 5.3, 10.1, 10.2, 10.3])


    def test_n_rep_70(self):
        x = np.array([1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 3, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2 ,3 ,2 , 3, 2, 3, 2, 3, 2,
                    3, 2,2, 1, 2, 3, 3, 3, 2, 1, 2, 3, 2, 3, 3, 2, 3, 3, 2, 1, 2, 3, 2, 3, 2, 2, 2, 2, 2, 3, 2, 2, 3, 1,
                    1, 1, 1])
        result = AbdiMolin()
        resultado, conclusao = result.fit(x)
        self.assertEqual(resultado[0], 0.255, "wrong statistic value")
        self.assertEqual(resultado[1], 0.105, "wrong tabulated value")
        self.assertIsNone(resultado[2], "p-valu not None")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Not Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Not Normal' not in conclusion when it should")

    def test_alfa_0_05(self):
        result = AbdiMolin()
        resultado, conclusao = result.fit(self.x)
        self.assertEqual(resultado[0], 0.154, "wrong statistic value")
        self.assertEqual(resultado[1], 0.261, "wrong tabulated value")
        self.assertIsNone(resultado[2], "p-value not None")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Normal' not in conclusion when it should")

    def test_alfa_0_10(self):
        result = AbdiMolin()
        resultado, conclusao = result.fit(self.x, alfa=0.10)
        self.assertEqual(resultado[0], 0.154, "wrong statistic value")
        self.assertEqual(resultado[1], 0.241, "wrong tabulated value")
        self.assertIsNone(resultado[2], "p-value not None")
        self.assertEqual(resultado[3], 0.10, "wrong alfa value")
        if "Data is Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Normal' not in conclusion when it should")

    def test_alfa_0_12(self):
        with self.assertRaises(ValueError, msg="Does not raised error when alfa=0.12"):
            result = AbdiMolin()
            resultado, conclusao = result.fit(self.x, alfa=0.12)


    def test_details_raise(self):
        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = AbdiMolin()
            result.fit(self.x, details="shorte")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = AbdiMolin()
            result.fit(self.x, details="shot")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid"):
            result = AbdiMolin()
            result.fit(self.x, details="ful")


    def test_pass_normal_details_full(self):
        result = AbdiMolin()
        resultado, conclusao = result.fit(self.x, details="full")
        self.assertEqual(resultado[0], 0.154, "wrong statistic value")
        self.assertEqual(resultado[1], 0.261, "wrong critical value")
        self.assertIsNone(resultado[2], "pvalue not Nont")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "critical" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'critical' not in conclusion when it should")


    def test_alfa_0_05_not_normal(self):
        result = AbdiMolin()
        resultado, conclusao = result.fit(self.x_not_normal)
        self.assertEqual(resultado[0], 0.332, "wrong statistic value")
        self.assertEqual(resultado[1], 0.274, "wrong tabulated value")
        self.assertIsNone(resultado[2], "p-value not None")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "Data is Not Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Not Normal' not in conclusion when it should")

    def test_alfa_0_10_not_normal(self):
        result = AbdiMolin()
        resultado, conclusao = result.fit(self.x_not_normal, alfa=0.10)
        self.assertEqual(resultado[0], 0.332, "wrong statistic value")
        self.assertEqual(resultado[1], 0.252, "wrong tabulated value")
        self.assertIsNone(resultado[2], "p-value not None")
        self.assertEqual(resultado[3], 0.10, "wrong alfa value")
        if "Data is Not Normal" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'Data is Not Normal' not in conclusion when it should")

    def test_alfa_0_12_not_normal(self):
        with self.assertRaises(ValueError, msg="Does not raised error when alfa=0.12 with not normal data"):
            result = AbdiMolin()
            resultado, conclusao = result.fit(self.x_not_normal, alfa=0.12)


    def test_details_not_normal(self):
        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid, not normal"):
            result = AbdiMolin()
            result.fit(self.x_not_normal, details="shorte")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid, not normal"):
            result = AbdiMolin()
            result.fit(self.x_not_normal, details="shot")

        with self.assertRaises(ValueError, msg="Does not raised error when details is not valid, not normal"):
            result = AbdiMolin()
            result.fit(self.x_not_normal, details="ful")

    def test_pass_normal_details_full_not_normal(self):
        result = AbdiMolin()
        resultado, conclusao = result.fit(self.x_not_normal, details="full")
        self.assertEqual(resultado[0], 0.332, "wrong statistic value")
        self.assertEqual(resultado[1], 0.274, "wrong tabulated value")
        self.assertIsNone(resultado[2], "p-value not not value")
        self.assertEqual(resultado[3], 0.05, "wrong alfa value")
        if "HAVE" in conclusao:
            result = True
        else:
            result = False
        self.assertTrue(result, "'HAVE' not in conclusion when it should")

















if __name__ == "__main__":
    unittest.main()
