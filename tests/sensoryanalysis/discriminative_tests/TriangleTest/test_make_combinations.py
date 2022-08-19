"""Tests if the make_combinations is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_make_combinations.



--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sensoryanalysis/discriminative_tests/TriangleTest/test_make_combinations.py
    or
    python -m unittest -b tests/sensoryanalysis/discriminative_tests/TriangleTest/test_make_combinations.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sensoryanalysis.discriminative_tests import TriangleTest
import numpy as np
import pandas as pd
import io
import sys
os.system('cls')

class Test_make_combinations(unittest.TestCase):

    def test_output_types(self):
        test = TriangleTest()
        result, input = test.make_combinations(10)
        self.assertIsInstance(result, pd.DataFrame, "the table is not a pd.DataFrame")
        self.assertIsInstance(input, dict, "the input is not a dict")
        self.assertEqual(len(input), 4, msg="something is missing in the input")
        self.assertEqual(list(input.keys()), ['n_of_assessors', 'seed', 'shuffle', 'reorder'], msg="wrong keys")
        self.assertIsInstance(input["n_of_assessors"], int, msg="wrong n_of_assessors")
        self.assertIsInstance(input["shuffle"], bool, msg="wrong shuffle")
        self.assertIsInstance(input["seed"], int, msg="wrong seed")
        self.assertIsInstance(input["reorder"], bool, msg="wrong reorder")



    def test_n_of_assessors(self):
        test = TriangleTest()
        testes = range(6, 1000)
        lista_teste = np.random.choice(testes, 10)
        for teste in lista_teste:
            result, input = test.make_combinations(teste)
            self.assertEqual(result.shape[0], teste, msg="wrong dataframe")
            self.assertEqual(result.shape[1], 4, msg="wrong dataframe")



    def test_seed(self):
        test = TriangleTest()
        testes = range(0, 1000)
        lista_teste = np.random.choice(testes, 10)
        for teste in lista_teste:
            result, input = test.make_combinations(36, seed=teste)
            self.assertEqual(input["seed"], teste, msg="wrong seed")


    def test_results(self):
        test = TriangleTest()
        result, input = test.make_combinations(36, seed=42, shuffle=False, reorder=False)
        resultados = ["AAB", "ABA", "ABB", "BBA", "BAB", "BAA"]
        for i in range(len(resultados)):
            self.assertEqual(result["Sample 1"][i][0], resultados[i][0], msg="wrong result")
            self.assertEqual(result["Sample 2"][i][0], resultados[i][1], msg="wrong result")
            self.assertEqual(result["Sample 3"][i][0], resultados[i][2], msg="wrong result")

        test = TriangleTest()
        result, input = test.make_combinations(36, seed=42, shuffle=True, reorder=False)
        resultados = ["BBA", "ABA", "BAA", "BAB", "ABB", "AAB"]
        for i in range(len(resultados)):
            self.assertEqual(result["Sample 1"][i][0], resultados[i][0], msg="wrong result")
            self.assertEqual(result["Sample 2"][i][0], resultados[i][1], msg="wrong result")
            self.assertEqual(result["Sample 3"][i][0], resultados[i][2], msg="wrong result")

        test = TriangleTest()
        result, input = test.make_combinations(36, seed=42, shuffle=True, reorder=True)
        resultados = ["AAB", "ABA", "BAA", "BBA", "ABB", "ABA"]
        for i in range(len(resultados)):
            self.assertEqual(result["Sample 1"][i][0], resultados[i][0], msg="wrong result")
            self.assertEqual(result["Sample 2"][i][0], resultados[i][1], msg="wrong result")
            self.assertEqual(result["Sample 3"][i][0], resultados[i][2], msg="wrong result")







# are y read to jummmmmppppp? https://youtu.be/m9P2WJI0A_c?t=233

if __name__ == "__main__":
    unittest.main()
