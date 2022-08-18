"""Tests if the minimum_of_correct_responses is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_minimum_of_correct_responses.



--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sensoryanalysis/discriminative_tests/TriangleTest/test_minimum_of_correct_responses.py
    or
    python -m unittest -b tests/sensoryanalysis/discriminative_tests/TriangleTest/test_minimum_of_correct_responses.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sensoryanalysis.discriminative_tests import TriangleTest
import numpy as np
import io
import sys
os.system('cls')

class Test_minimum_of_correct_responses(unittest.TestCase):

    def test_output(self):
        test = TriangleTest()
        result, input = test.minimum_of_correct_responses(10)
        self.assertIsInstance(result[0], (int, np.uint, np.integer), "the number of assessors is not an int")
        self.assertIsInstance(input, dict, "the input is not a dict")


    def test_sensivel(self):
        test = TriangleTest()
        result, input = test.minimum_of_correct_responses(6, which="original", alfa=0.001)
        self.assertEqual(result[0], 7, msg="wrong default")
        self.assertEqual(input["alpha"], 0.001, msg="wrong alfa")
        self.assertEqual(input["which"], "function", msg="wrong which")


        test = TriangleTest()
        result, input = test.minimum_of_correct_responses(100, which="original", alfa=0.001)
        result2, input2 = test.minimum_of_correct_responses(100, which="function", alfa=0.001)
        self.assertEqual(result[0], result2[0], msg="wrong default")
        self.assertEqual(input["alpha"], 0.001, msg="wrong alfa")
        self.assertEqual(input["which"], "function", msg="wrong which")
        self.assertEqual(input2["which"], "function", msg="wrong which")

        test = TriangleTest()
        result, input = test.minimum_of_correct_responses(50, which="original", alfa=0.05)
        result2, input2 = test.minimum_of_correct_responses(50, which="function", alfa=0.05)
        self.assertEqual(result[0], result2[0], msg="wrong default")
        self.assertEqual(input["alpha"], 0.05, msg="wrong alfa")
        self.assertEqual(input["which"], "function", msg="wrong which")
        self.assertEqual(input2["which"], "function", msg="wrong which")


    def test_sensivel_output(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        test = TriangleTest()
        result, input = test.minimum_of_correct_responses(6, which="original", alfa=0.001)
        sys.stdout = sys.__stdout__
        expected = "n_of_assessors = 6 and alpha = 0.001."
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output")

        #################

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        test = TriangleTest(language="pt-br")
        result, input = test.minimum_of_correct_responses(6, which="original", alfa=0.001)
        sys.stdout = sys.__stdout__
        expected = "n_of_assessors = 6 e alfa = 0.001."
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output")

        #################


        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        test = TriangleTest()
        result, input = test.minimum_of_correct_responses(100, which="original", alfa=0.001)
        sys.stdout = sys.__stdout__
        expected = "does not have a minimum value for n_of_assessors = 100"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output")

        #################

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        test = TriangleTest(language="pt-br")
        result, input = test.minimum_of_correct_responses(50, which="original", alfa=0.05)
        sys.stdout = sys.__stdout__
        expected = "não apresentam valor mínimo para n_of_assessors = 50"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output")

        #################


    def test_results_original(self):
        test = TriangleTest()
        result, input = test.minimum_of_correct_responses(10, which="original", alfa=0.2)
        self.assertEqual(result[0], 6, msg="wrong default")
        self.assertEqual(input["alpha"], 0.2, msg="wrong alfa")
        self.assertEqual(input["which"], "original", msg="wrong which")

        result, input = test.minimum_of_correct_responses(102, which="original", alfa=0.2)
        self.assertEqual(result[0], 39, msg="wrong default")
        self.assertEqual(input["alpha"], 0.2, msg="wrong alfa")
        self.assertEqual(input["which"], "original", msg="wrong which")


        result, input = test.minimum_of_correct_responses(11, which="original", alfa=0.10)
        self.assertEqual(result[0], 7, msg="wrong default")
        self.assertEqual(input["alpha"], 0.1, msg="wrong alfa")
        self.assertEqual(input["which"], "original", msg="wrong which")

        result, input = test.minimum_of_correct_responses(60, which="original", alfa=0.10)
        self.assertEqual(result[0], 26, msg="wrong default")
        self.assertEqual(input["alpha"], 0.1, msg="wrong alfa")
        self.assertEqual(input["which"], "original", msg="wrong which")


        result, input = test.minimum_of_correct_responses(16, which="original", alfa=0.05)
        self.assertEqual(result[0], 9, msg="wrong default")
        self.assertEqual(input["alpha"], 0.05, msg="wrong alfa")
        self.assertEqual(input["which"], "original", msg="wrong which")

        result, input = test.minimum_of_correct_responses(66, which="original", alfa=0.05)
        self.assertEqual(result[0], 29, msg="wrong default")
        self.assertEqual(input["alpha"], 0.05, msg="wrong alfa")
        self.assertEqual(input["which"], "original", msg="wrong which")


        result, input = test.minimum_of_correct_responses(17, which="original", alfa=0.01)
        self.assertEqual(result[0], 11, msg="wrong default")
        self.assertEqual(input["alpha"], 0.01, msg="wrong alfa")
        self.assertEqual(input["which"], "original", msg="wrong which")

        result, input = test.minimum_of_correct_responses(84, which="original", alfa=0.01)
        self.assertEqual(result[0], 39, msg="wrong default")
        self.assertEqual(input["alpha"], 0.01, msg="wrong alfa")
        self.assertEqual(input["which"], "original", msg="wrong which")


        result, input = test.minimum_of_correct_responses(19, which="original", alfa=0.001)
        self.assertEqual(result[0], 14, msg="wrong default")
        self.assertEqual(input["alpha"], 0.001, msg="wrong alfa")
        self.assertEqual(input["which"], "original", msg="wrong which")

        result, input = test.minimum_of_correct_responses(90, which="original", alfa=0.001)
        self.assertEqual(result[0], 45, msg="wrong default")
        self.assertEqual(input["alpha"], 0.001, msg="wrong alfa")
        self.assertEqual(input["which"], "original", msg="wrong which")


    def test_results_function(self):
        test = TriangleTest()
        result, input = test.minimum_of_correct_responses(10, which="function", alfa=0.2)
        self.assertEqual(result[0], 6, msg="wrong default")
        self.assertEqual(input["alpha"], 0.2, msg="wrong alfa")
        self.assertEqual(input["which"], "function", msg="wrong which")

        result, input = test.minimum_of_correct_responses(33, which="function", alfa=0.2)
        self.assertEqual(result[0], 14, msg="wrong default")
        self.assertEqual(input["alpha"], 0.2, msg="wrong alfa")
        self.assertEqual(input["which"], "function", msg="wrong which")

        result, input = test.minimum_of_correct_responses(9, which="function", alfa=0.10)
        self.assertEqual(result[0], 6, msg="wrong default")
        self.assertEqual(input["alpha"], 0.10, msg="wrong alfa")
        self.assertEqual(input["which"], "function", msg="wrong which")

        result, input = test.minimum_of_correct_responses(96, which="function", alfa=0.10)
        self.assertEqual(result[0], 39, msg="wrong default")
        self.assertEqual(input["alpha"], 0.10, msg="wrong alfa")
        self.assertEqual(input["which"], "function", msg="wrong which")

        result, input = test.minimum_of_correct_responses(13, which="function", alfa=0.05)
        self.assertEqual(result[0], 8, msg="wrong default")
        self.assertEqual(input["alpha"], 0.05, msg="wrong alfa")
        self.assertEqual(input["which"], "function", msg="wrong which")

        result, input = test.minimum_of_correct_responses(90, which="function", alfa=0.05)
        self.assertEqual(result[0], 38, msg="wrong default")
        self.assertEqual(input["alpha"], 0.05, msg="wrong alfa")
        self.assertEqual(input["which"], "function", msg="wrong which")


        result, input = test.minimum_of_correct_responses(28, which="function", alfa=0.01)
        self.assertEqual(result[0], 16, msg="wrong default")
        self.assertEqual(input["alpha"], 0.01, msg="wrong alfa")
        self.assertEqual(input["which"], "function", msg="wrong which")

        result, input = test.minimum_of_correct_responses(102, which="function", alfa=0.01)
        self.assertEqual(result[0], 46, msg="wrong default")
        self.assertEqual(input["alpha"], 0.01, msg="wrong alfa")
        self.assertEqual(input["which"], "function", msg="wrong which")


        result, input = test.minimum_of_correct_responses(24, which="function", alfa=0.001)
        self.assertEqual(result[0], 16, msg="wrong default")
        self.assertEqual(input["alpha"], 0.001, msg="wrong alfa")
        self.assertEqual(input["which"], "function", msg="wrong which")

        result, input = test.minimum_of_correct_responses(102, which="function", alfa=0.001)
        self.assertEqual(result[0], 50, msg="wrong default")
        self.assertEqual(input["alpha"], 0.001, msg="wrong alfa")
        self.assertEqual(input["which"], "function", msg="wrong which")


    def test_results_function_default(self):
        test = TriangleTest()
        testes = np.random.randint(6, 200, 20)
        for teste in testes:
            result, input = test.minimum_of_correct_responses(teste)
            result2, input2 = test.minimum_of_correct_responses(teste, which="original")
            self.assertEqual(result2[0], result[0], msg="wrong default")
            self.assertEqual(input["alpha"], input2["alpha"], msg="wrong default")
            self.assertEqual(input["which"], input2["which"], msg="wrong default")


    def test_results_default(self):
        test = TriangleTest()
        result, input = test.minimum_of_correct_responses(10)
        self.assertEqual(result[0], 7, msg="wrong minimum value")
        self.assertEqual(input["alpha"], 0.05, msg="wrong alfa value")
        self.assertEqual(input["which"], "original", msg="wrong which value")

        test = TriangleTest(language="pt-br")
        result, input = test.minimum_of_correct_responses(36)
        self.assertEqual(result[0], 18, msg="wrong minimum value")
        self.assertEqual(input["alfa"], 0.05, msg="wrong alfa value")
        self.assertEqual(input["which"], "original", msg="wrong which value")







# are y read to jummmmmppppp? https://youtu.be/m9P2WJI0A_c?t=233

if __name__ == "__main__":
    unittest.main()
