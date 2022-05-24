"""Tests if the positional_summary function for Sample is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_positional_summary. This function checks if a ValueError is raised when the fit was not performed, if the output is a dataframe, if the dataframe has the espected column names, if the dataframe has the right shape. Also, tests the print output, but just the last print statement, and test when show=False.



--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sample/test_positional_summary.py
    or
    python -m unittest -b tests/sample/test_positional_summary.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from unittest.mock import patch, call
from pycafee.sample.sample import Sample
import numpy as np
import pandas as pd
os.system('cls')

class Test_positional_summary(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
        cls.x_not_normal = np.array([1, 1, 1, 1.1, 1.2, 5.3, 10.1, 10.2, 10.3])

    def test_no_fit(self):
        with self.assertRaises(ValueError, msg="Does not raised error when fit was not performed"):
            amostra = Sample()
            amostra.positional_summary()

        with self.assertRaises(ValueError, msg="Does not raised error when fit was not performed"):
            amostra = Sample()
            amostra.positional_summary(show=True)

        with self.assertRaises(ValueError, msg="Does not raised error when fit was not performed"):
            amostra = Sample(language="pt-br")
            amostra.positional_summary(show=True)

        with self.assertRaises(ValueError, msg="Does not raised error when fit was not performed"):
            amostra = Sample(name="bwidaba", language="pt-br")
            amostra.positional_summary(show=True)

    def test_output_is_data_frame(self):
        amostra = Sample(name="bwidaba", language="pt-br")
        amostra.fit(self.x)
        result = amostra.positional_summary(show=True)
        self.assertIsInstance(result, pd.DataFrame, msg="Output is not a DataFrame")

        amostra = Sample()
        amostra.fit(self.x)
        result = amostra.positional_summary(show=False)
        self.assertIsInstance(result, pd.DataFrame, msg="Output is not a DataFrame")

    def test_output_data_frame(self):
        amostra = Sample(name="bwidaba", language="pt-br")
        amostra.fit(self.x)
        df = amostra.positional_summary(show=True)
        result = df.columns
        espected = ['Mínimo', 'Q1', 'Mediana', 'Q3', 'Máximo', 'Distância interquartílica']
        self.assertCountEqual(result, espected, msg="Column names does not match")
        size = df.shape
        self.assertEqual(size[0], 1, "Somthing wrong with the DataFrame")
        self.assertEqual(size[1], 6, "Somthing wrong with the DataFrame")

        amostra = Sample()
        amostra.fit(self.x)
        df = amostra.positional_summary(show=True)
        result = df.columns
        espected = ['Minimum', 'Q1', 'Median', 'Q3', 'Maximum', 'Interquartile range']
        self.assertCountEqual(result, espected, msg="Column names does not match")
        size = df.shape
        self.assertEqual(size[0], 1, "Somthing wrong with the DataFrame")
        self.assertEqual(size[1], 6, "Somthing wrong with the DataFrame")

        amostra = Sample(name="bwidaba", language="pt-br")
        amostra.fit(self.x_not_normal)
        df = amostra.positional_summary(show=True)
        result = df.columns
        espected = ['Mínimo', 'Q1', 'Mediana', 'Q3', 'Máximo', 'Distância interquartílica']
        self.assertCountEqual(result, espected, msg="Column names does not match")
        size = df.shape
        self.assertEqual(size[0], 1, "Somthing wrong with the DataFrame")
        self.assertEqual(size[1], 6, "Somthing wrong with the DataFrame")

        amostra = Sample()
        amostra.fit(self.x_not_normal)
        df = amostra.positional_summary(show=True)
        result = df.columns
        espected = ['Minimum', 'Q1', 'Median', 'Q3', 'Maximum', 'Interquartile range']
        self.assertCountEqual(result, espected, msg="Column names does not match")
        size = df.shape
        self.assertEqual(size[0], 1, "Somthing wrong with the DataFrame")
        self.assertEqual(size[1], 6, "Somthing wrong with the DataFrame")

    @patch('builtins.print')
    def test_print(self, mock_print):
        amostra = Sample()
        amostra.fit(self.x)
        amostra.positional_summary(show=True)
        mock_print.assert_called_with('=========  =====  ========  =====  =========  =====================\n Minimum    Q1     Median    Q3     Maximum    Interquartile range\n=========  =====  ========  =====  =========  =====================\n  4.400    4.625   4.900    5.000    5.400            0.375\n=========  =====  ========  =====  =========  =====================')

        amostra = Sample(language='pt-br')
        amostra.fit(self.x)
        amostra.positional_summary(show=True)
        mock_print.assert_called_with('========  =====  =========  =====  ========  ===========================\n Mínimo    Q1     Mediana    Q3     Máximo    Distância interquartílica\n========  =====  =========  =====  ========  ===========================\n 4.400    4.625    4.900    5.000   5.400               0.375\n========  =====  =========  =====  ========  ===========================')

        amostra = Sample()
        amostra.fit(self.x_not_normal)
        amostra.positional_summary(show=True)
        mock_print.assert_called_with('=========  =====  ========  ======  =========  =====================\n Minimum    Q1     Median     Q3     Maximum    Interquartile range\n=========  =====  ========  ======  =========  =====================\n  1.000    1.000   1.200    10.100   10.300            9.100\n=========  =====  ========  ======  =========  =====================')

        amostra = Sample(language='pt-br')
        amostra.fit(self.x_not_normal)
        amostra.positional_summary(show=True)
        mock_print.assert_called_with('========  =====  =========  ======  ========  ===========================\n Mínimo    Q1     Mediana     Q3     Máximo    Distância interquartílica\n========  =====  =========  ======  ========  ===========================\n 1.000    1.000    1.200    10.100   10.300              9.100\n========  =====  =========  ======  ========  ===========================')

    @patch('builtins.print')
    def test_show_false(self, mock_print):
        with self.assertRaises(AssertionError, msg="Does not raised AssertionError when show=False"):
            amostra = Sample()
            amostra.fit(self.x)
            amostra.positional_summary(show=False)
            mock_print.assert_called_with(' ')

        with self.assertRaises(AssertionError, msg="Does not raised AssertionError when show=False"):
            amostra = Sample(language='pt-br')
            amostra.fit(self.x)
            amostra.positional_summary(show=False)
            mock_print.assert_called_with(' ')

        with self.assertRaises(AssertionError, msg="Does not raised AssertionError when show=False"):
            amostra = Sample()
            amostra.fit(self.x_not_normal)
            amostra.positional_summary(show=True)
            mock_print.assert_called_with(' ')

        with self.assertRaises(AssertionError, msg="Does not raised AssertionError when show=False"):
            amostra = Sample(language='pt-br')
            amostra.fit(self.x_not_normal)
            amostra.positional_summary(show=True)
            mock_print.assert_called_with(' ')




# are y read to jummmmmppppp? https://youtu.be/m9P2WJI0A_c?t=233

if __name__ == "__main__":
    unittest.main()
