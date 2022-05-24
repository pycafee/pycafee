"""Tests if the normality_check function for Sample is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_normality_check. This function checks if a ValueError is raised when the fit was not performed, if the output is a dataframe, if the dataframe has the espected column names, if the dataframe has the right shape. Also, tests the print output, but just the last print statement and test when show=False.


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sample/test_normality_check.py
    or
    python -m unittest -b tests/sample/test_normality_check.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from unittest.mock import patch, call
from pycafee.sample.sample import Sample
import numpy as np
import pandas as pd
os.system('cls')

class Test_Normality(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        cls.x_not_normal = np.array([1, 1, 1, 1.1, 1.2, 5.3, 10.1, 10.2, 10.3])

    def test_no_fit(self):
        with self.assertRaises(ValueError, msg="Does not raised error when fit was not performed"):
            amostra = Sample()
            amostra.normality_check()

        with self.assertRaises(ValueError, msg="Does not raised error when fit was not performed"):
            amostra = Sample()
            amostra.normality_check(show=True)

        with self.assertRaises(ValueError, msg="Does not raised error when fit was not performed"):
            amostra = Sample(language="pt-br")
            amostra.normality_check(show=True)

        with self.assertRaises(ValueError, msg="Does not raised error when fit was not performed"):
            amostra = Sample(name="bwidaba", language="pt-br")
            amostra.normality_check(show=True)

    def test_output_is_data_frame(self):
        amostra = Sample(name="bwidaba", language="pt-br")
        amostra.fit(self.x)
        result = amostra.normality_check(show=True)
        self.assertIsInstance(result, pd.DataFrame, msg="Output is not a DataFrame")

        amostra = Sample()
        amostra.fit(self.x)
        result = amostra.normality_check(show=False)
        self.assertIsInstance(result, pd.DataFrame, msg="Output is not a DataFrame")

    def test_output_data_frame(self):
        amostra = Sample(name="bwidaba", language="pt-br")
        amostra.fit(self.x)
        df = amostra.normality_check(show=True)
        result = df.columns
        espected = ['Estatistica', 'Critico', 'p_valor', 'Alfa']
        self.assertCountEqual(result, espected, msg="Column names does not match")
        size = df.shape
        self.assertEqual(size[0], 1, "Somthing wrong with the DataFrame")
        self.assertEqual(size[1], 4, "Somthing wrong with the DataFrame")

        amostra = Sample()
        amostra.fit(self.x)
        df = amostra.normality_check(show=True)
        result = df.columns
        espected = ['Statistic', 'Critical', 'p_value', 'Alpha']
        self.assertCountEqual(result, espected, msg="Column names does not match")
        size = df.shape
        self.assertEqual(size[0], 1, "Somthing wrong with the DataFrame")
        self.assertEqual(size[1], 4, "Somthing wrong with the DataFrame")

        amostra = Sample(name="bwidaba", language="pt-br")
        amostra.fit(self.x_not_normal)
        df = amostra.normality_check(show=True)
        result = df.columns
        espected = ['Estatistica', 'Critico', 'p_valor', 'Alfa']
        self.assertCountEqual(result, espected, msg="Column names does not match")
        size = df.shape
        self.assertEqual(size[0], 1, "Somthing wrong with the DataFrame")
        self.assertEqual(size[1], 4, "Somthing wrong with the DataFrame")

        amostra = Sample()
        amostra.fit(self.x_not_normal)
        df = amostra.normality_check(show=True)
        result = df.columns
        espected = ['Statistic', 'Critical', 'p_value', 'Alpha']
        self.assertCountEqual(result, espected, msg="Column names does not match")
        size = df.shape
        self.assertEqual(size[0], 1, "Somthing wrong with the DataFrame")
        self.assertEqual(size[1], 4, "Somthing wrong with the DataFrame")

    @patch('builtins.print')
    def test_print(self, mock_print):
        amostra = Sample()
        amostra.fit(self.x)
        amostra.normality_check(show=True)
        mock_print.assert_called_with("Data is Normal at a 95.0% of confidence level.")

        amostra = Sample(language='pt-br')
        amostra.fit(self.x)
        amostra.normality_check(show=True)
        mock_print.assert_called_with("Os dados são Normais com 95.0% de confiança.")

        amostra = Sample()
        amostra.fit(self.x_not_normal)
        amostra.normality_check(show=True)
        mock_print.assert_called_with("Data is Not Normal at a 95.0% of confidence level.")

        amostra = Sample(language='pt-br')
        amostra.fit(self.x_not_normal)
        amostra.normality_check(show=True)
        mock_print.assert_called_with("Os dados não são Normais com 95.0% de confiança.")



    @patch('builtins.print')
    def test_show_false(self, mock_print):
        with self.assertRaises(AssertionError, msg="Does not raised AssertionError when show=False"):
            amostra = Sample()
            amostra.fit(self.x)
            amostra.normality_check(show=False)
            mock_print.assert_called_with(' ')

        with self.assertRaises(AssertionError, msg="Does not raised AssertionError when show=False"):
            amostra = Sample(language='pt-br')
            amostra.fit(self.x)
            amostra.normality_check(show=False)
            mock_print.assert_called_with(' ')

        with self.assertRaises(AssertionError, msg="Does not raised AssertionError when show=False"):
            amostra = Sample()
            amostra.fit(self.x_not_normal)
            amostra.normality_check(show=True)
            mock_print.assert_called_with(' ')

        with self.assertRaises(AssertionError, msg="Does not raised AssertionError when show=False"):
            amostra = Sample(language='pt-br')
            amostra.fit(self.x_not_normal)
            amostra.normality_check(show=True)
            mock_print.assert_called_with(' ')












# are y read to jummmmmppppp? https://youtu.be/m9P2WJI0A_c?t=233

if __name__ == "__main__":
    unittest.main()
