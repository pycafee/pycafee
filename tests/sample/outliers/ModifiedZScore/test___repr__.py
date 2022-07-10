"""Tests if the test___repr__ is working as expected

---> Class Test_repr


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sample/outliers/ModifiedZScore/test___repr__.py
    or
    python -m unittest -b tests/sample/outliers/ModifiedZScore/test___repr__.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sample.outliers import ModifiedZScore
import numpy as np
os.system('cls')


class Test_repr(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([147, 150, 153, 153, 156, 159, 184])


    def test_without_fit(self):
        teste = ModifiedZScore()
        self.assertEqual(teste.__repr__(), "Modified ZScore's test for outlier detection", msg="worng __repr__")

        teste = ModifiedZScore(language="pt-br")
        self.assertEqual(teste.__repr__(), "Teste Z Modificado para detecção de outliers", msg="worng __repr__")



    def test_with_fit(self):
        teste = ModifiedZScore(language="pt-br")
        result, conclusion = teste.fit(self.x, which="max")
        self.assertEqual(teste.__repr__(), "Teste Z Modificado para detecção de outliers", msg="worng __repr__")

        teste = ModifiedZScore(language="en")
        result, conclusion = teste.fit(self.x, which="max")
        self.assertEqual(teste.__repr__(), "Modified ZScore's test for outlier detection", msg="worng __repr__")



if __name__ == "__main__":
    unittest.main()
