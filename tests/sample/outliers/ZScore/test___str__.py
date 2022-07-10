"""Tests if the test___str__ is working as expected

---> Class Test_str


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sample/outliers/ZScore/test___str__.py
    or
    python -m unittest -b tests/sample/outliers/ZScore/test___str__.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sample.outliers import ZScore
import numpy as np
os.system('cls')


class Test_str(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([147, 150, 153, 153, 156, 159, 184])


    def test_without_fit(self):
        teste = ZScore()
        self.assertEqual(teste.__str__(), "The ZScore test was not performed yet. Use the 'fit' method to perform the test.", msg="worng __str__")

        teste = ZScore(language="pt-br")
        self.assertEqual(teste.__str__(), "O teste de ZScore não foi realizado. Utilize o método 'fit' para realizar o teste.", msg="worng __str__")



    def test_with_fit(self):
        teste = ZScore(language="pt-br")
        result, conclusion = teste.fit(self.x, which="max")
        self.assertEqual(teste.__str__(), "O conjunto de dados não tem outliers", msg="worng __str__")
        self.assertEqual(teste.__str__(), conclusion, msg="wrong __str__")

        teste = ZScore(language="en")
        result, conclusion = teste.fit(self.x, which="max")
        self.assertEqual(teste.__str__(), "The dataset has no outliers", msg="worng __str__")
        self.assertEqual(teste.__str__(), conclusion, msg="wrong __str__")



if __name__ == "__main__":
    unittest.main()
