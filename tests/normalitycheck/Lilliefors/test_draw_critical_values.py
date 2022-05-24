"""Tests if the test_draw_critical_values is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_None_test_draw_critical_values. This class checks if the axes is returned, if the file is export when export = True and when extension = 'pdf' and if the file is not exported when export = True. The decimal_separator is also tested fot ".", "," and None.

---> Class Test_axes_test_draw_critical_values. This class checks if the axes is returned when ax is a previuous created ax. It also looks for a saved file if export=True.

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/normalitycheck/Lilliefors/test_draw_critical_values.py
    or
    python -m unittest -b tests/normalitycheck/Lilliefors/test_draw_critical_values.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from unittest.mock import patch
from pycafee.normalitycheck.lilliefors import Lilliefors
from pycafee.utils.helpers import _check_file_exists
import numpy as np
import matplotlib.axes
import matplotlib.pyplot as plt
from pathlib import Path
os.system('cls')


class Test_axes_test_draw_critical_values(unittest.TestCase):

    def test_basic_plot(self):
        lilli_test = Lilliefors()
        fig, ax = plt.subplots()
        axes = lilli_test.draw_critical_values(ax=ax)
        result = isinstance(axes, matplotlib.axes.SubplotBase)
        self.assertTrue(result, "Ax not returned")
        plt.close()

        lilli_test = Lilliefors()
        fig, ax = plt.subplots(figsize=(12,6))
        axes = lilli_test.draw_critical_values(ax=ax)
        result = isinstance(axes, matplotlib.axes.SubplotBase)
        self.assertTrue(result, "Ax not returned")
        plt.close()

    def test_is_exported_plot(self):
        lilli_test = Lilliefors()
        fig, ax = plt.subplots()
        axes = lilli_test.draw_critical_values(ax=ax, export=True)
        result = _check_file_exists("lilliefors_critical_plot.png")
        plt.close()
        try:
            rem_file = Path("lilliefors_critical_plot.png")
            rem_file.unlink()
        except:
            pass
        self.assertFalse(result, "File 'lilliefors_critical_plot.png' was created even with ax=ax")




class Test_None_draw_test_draw_critical_values(unittest.TestCase):

    def test_basic_plot(self):
        with patch('matplotlib.pyplot.show') as p:
            lilli_test = Lilliefors()
            axes = lilli_test.draw_critical_values(ax=None)
            result = isinstance(axes, matplotlib.axes.SubplotBase)
            self.assertTrue(result, "Ax not returned")
            plt.close()

    def test_plot_export(self):
        with patch('matplotlib.pyplot.show') as p:
            lilli_test = Lilliefors()
            axes = lilli_test.draw_critical_values(ax=None, export=True)
            result = _check_file_exists("lilliefors_critical_plot.png")
            rem_file = Path("lilliefors_critical_plot.png")
            rem_file.unlink()
            self.assertTrue(result, "File was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            lilli_test = Lilliefors()
            axes = lilli_test.draw_critical_values(ax=None, export=True, file_name="teste")
            result = _check_file_exists("teste.png")
            rem_file = Path("teste.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'teste.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            lilli_test = Lilliefors()
            axes = lilli_test.draw_critical_values(ax=None, export=True, file_name="teste", extension='pdf')
            result = _check_file_exists("teste.pdf")
            rem_file = Path("teste.pdf")
            rem_file.unlink()
            self.assertTrue(result, "File 'teste.pdf' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            lilli_test = Lilliefors()
            axes = lilli_test.draw_critical_values(ax=None, export=False, file_name="teste", extension='pdf')
            result = _check_file_exists("teste.pdf")
            plt.close()
            try:
                rem_file = Path("teste.pdf")
                rem_file.unlink()
            except:
                pass
            self.assertFalse(result, "File 'teste.pdf' was created even with export=False")

    def test_decimal_separator(self):
        with patch('matplotlib.pyplot.show') as p:
            lilli_test = Lilliefors()
            axes = lilli_test.draw_critical_values(ax=None, decimal_separator=",")
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = False
                if ',' in temp:
                    result = True
            self.assertTrue(result, "No comma in y axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            lilli_test = Lilliefors()
            axes = lilli_test.draw_critical_values(ax=None, decimal_separator=".")
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = True
                if ',' in temp:
                    result = False
            self.assertTrue(result, "No dot in y axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            lilli_test = Lilliefors()
            axes = lilli_test.draw_critical_values(ax=None, decimal_separator=None)
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = True
                if ',' in temp:
                    result = False
            self.assertTrue(result, "No dot in y axis")
            plt.close()












if __name__ == "__main__":
    unittest.main()
