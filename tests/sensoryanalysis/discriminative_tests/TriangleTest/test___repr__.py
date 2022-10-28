"""Tests if the test___repr__ is working as expected

---> Class Test_repr


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sensoryanalysis/discriminative_tests/TriangleTest/test___repr__.py
    or
    python -m unittest -b tests/sensoryanalysis/discriminative_tests/TriangleTest/test___repr__.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sensoryanalysis.discriminative_tests import TriangleTest
import numpy as np
os.system('cls')


class Test_repr(unittest.TestCase):



    def test_without_fit(self):
        teste = TriangleTest()
        self.assertEqual(teste.__repr__(), "Triangular Test to verify if there is a significant difference between two samples that underwent different treatments.", msg="worng __repr__")

        teste = TriangleTest(language="pt-br")
        self.assertEqual(teste.__repr__(), "Teste Triangular para verificar se existe diferença significativa entre duas amostras que sofreram tratamentos diferentes.", msg="worng __repr__")



    def test_with_fit(self):
        teste = TriangleTest(language="pt-br")
        result, conclusion = teste.fit(10,20)
        self.assertEqual(teste.__repr__(), "Teste Triangular para verificar se existe diferença significativa entre duas amostras que sofreram tratamentos diferentes.", msg="worng __repr__")

        teste = TriangleTest(language="en")
        result, conclusion = teste.fit(10,20)
        self.assertEqual(teste.__repr__(), "Triangular Test to verify if there is a significant difference between two samples that underwent different treatments.", msg="worng __repr__")



if __name__ == "__main__":
    unittest.main()
