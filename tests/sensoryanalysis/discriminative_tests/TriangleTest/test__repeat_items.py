"""Tests if the _repeat_items is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test__repeat_items.



--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sensoryanalysis/discriminative_tests/TriangleTest/test__repeat_items.py
    or
    python -m unittest -b tests/sensoryanalysis/discriminative_tests/TriangleTest/test__repeat_items.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sensoryanalysis.discriminative_tests import _repeat_items
import numpy as np
os.system('cls')

class Test__repeat_items(unittest.TestCase):

    def test_output_type(self):
        result = _repeat_items([10,10,12], 5)
        self.assertIsInstance(result, list, msg="the result is not a list")



    def test_results(self):
        listas = [
            [1, 2, 3],
            ["A"],
            ["A", 2, 3, 4]
        ]

        elements = [1, 5, 9, ]

        resultado = [
            [1],
            ["A", "A", "A", "A", "A"],
            ["A", 2, 3, 4, "A", 2, 3, 4, "A"]
        ]

        for i in range(len(listas)):
            result = _repeat_items(listas[i], elements[i])
            self.assertEqual(result, resultado[i], msg="wrong result")






# are y read to jummmmmppppp? https://youtu.be/m9P2WJI0A_c?t=233

if __name__ == "__main__":
    unittest.main()
