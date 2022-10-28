"""Tests if the test___str__ is working as expected

---> Class Test_str


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sensoryanalysis/discriminative_tests/TriangleTest/test___str__.py
    or
    python -m unittest -b tests/sensoryanalysis/discriminative_tests/TriangleTest/test___str__.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sensoryanalysis.discriminative_tests import TriangleTest
import numpy as np
os.system('cls')


class Test_str(unittest.TestCase):

    def test_without_fit(self):
        teste = TriangleTest()
        self.assertEqual(teste.__str__(), "The TriangleTest test was not performed yet. Use the 'fit' method to perform the test.", msg="wrong __str__")

        teste = TriangleTest(language="pt-br")
        self.assertEqual(teste.__str__(), "O teste de TriangleTest não foi realizado. Utilize o método 'fit' para realizar o teste.", msg="wrong __str__")



    def test_with_fit(self):
        teste = TriangleTest(language="pt-br")
        result, conclusion = teste.fit(10, 50)
        self.assertEqual(teste.__str__(), "As amostras são iguais (com 95.0% de confiança).", msg="wrong __str__")
        self.assertEqual(teste.__str__(), conclusion, msg="wrong __str__")

        teste = TriangleTest(language="en")
        result, conclusion = teste.fit(10, 50)
        self.assertEqual(teste.__str__(), "Samples are equal (with 95.0% confidence).", msg="wrong __str__")
        self.assertEqual(teste.__str__(), conclusion, msg="wrong __str__")



if __name__ == "__main__":
    unittest.main()
