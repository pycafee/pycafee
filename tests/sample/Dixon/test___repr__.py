"""Tests if the test___repr__ is working as expected

---> Class Test_repr


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sample/Dixon/test___repr__.py
    or
    python -m unittest -b tests/sample/Dixon/test___repr__.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sample.dixon import Dixon
import numpy as np
os.system('cls')


class Test_repr(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([147, 150, 153, 153, 156, 159, 184])


    def test_without_fit(self):
        teste = Dixon()
        self.assertEqual(teste.__repr__(), "Dixon's test for outlier detection", msg="worng __repr__")

        teste = Dixon(language="pt-br")
        self.assertEqual(teste.__repr__(), "Teste de Dixon para detecção de outliers", msg="worng __repr__")

        teste = Dixon()
        result = teste._r10(self.x, which="max")
        self.assertEqual(teste.__repr__(), "Dixon's test for outlier detection", msg="worng __repr__")

        teste = Dixon(language="pt-br")
        result = teste._r10(self.x, which="max")
        self.assertEqual(teste.__repr__(), "Teste de Dixon para detecção de outliers", msg="worng __repr__")


    def test_with_fit(self):
        teste = Dixon(language="pt-br")
        result, conclusion = teste.fit(self.x, which="max")
        self.assertEqual(teste.__repr__(), "Teste de Dixon para detecção de outliers", msg="worng __repr__")

        teste = Dixon(language="en")
        result, conclusion = teste.fit(self.x, which="max")
        self.assertEqual(teste.__repr__(), "Dixon's test for outlier detection", msg="worng __repr__")



if __name__ == "__main__":
    unittest.main()
