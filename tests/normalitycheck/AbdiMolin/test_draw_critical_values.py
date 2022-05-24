"""Tests if the draw_critical_values is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_None_draw_critical_values. This class checks if the axes is returned, if the file is export when export = True and when extension = 'pdf' and if the file is not exported when export = True. The decimal_separator is also tested fot ".", "," and None.

---> Class Test_axes_draw_critical_values. This class checks if the axes is returned when ax is a previuous created ax. It also looks for a saved file if export=True.

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/normalitycheck/AbdiMolin/test_draw_critical_values.py
    or
    python -m unittest -b tests/normalitycheck/AbdiMolin/test_draw_critical_values.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from unittest.mock import patch
from pycafee.normalitycheck.abdimolin import AbdiMolin
from pycafee.utils.helpers import _check_file_exists
import numpy as np
import matplotlib.axes
import matplotlib.pyplot as plt
from pathlib import Path
os.system('cls')


class Test_axes_draw_critical_values(unittest.TestCase):

    def test_basic_plot(self):
        teste = AbdiMolin()
        fig, ax = plt.subplots()
        axes = teste.draw_critical_values(ax=ax)
        result = isinstance(axes, matplotlib.axes.SubplotBase)
        self.assertTrue(result, "Ax not returned")
        plt.close()

        teste = AbdiMolin()
        fig, ax = plt.subplots(figsize=(12,6))
        axes = teste.draw_critical_values(ax=ax)
        result = isinstance(axes, matplotlib.axes.SubplotBase)
        self.assertTrue(result, "Ax not returned")
        plt.close()

    def test_is_exported_plot(self):
        teste = AbdiMolin()
        fig, ax = plt.subplots()
        axes = teste.draw_critical_values(ax=ax, export=True)
        result = _check_file_exists("abdi_molin_critical_plot.png")
        plt.close()
        try:
            rem_file = Path("abdi_molin_critical_plot.png")
            rem_file.unlink()
        except:
            pass
        self.assertFalse(result, "File 'abdi_molin_critical_plot.png' was created even with ax=ax")




class Test_None_draw_critical_values(unittest.TestCase):

    def test_basic_plot(self):
        with patch('matplotlib.pyplot.show') as p:
            teste = AbdiMolin()
            axes = teste.draw_critical_values(ax=None)
            result = isinstance(axes, matplotlib.axes.SubplotBase)
            self.assertTrue(result, "Ax not returned")
            plt.close()

    def test_plot_export(self):
        with patch('matplotlib.pyplot.show') as p:
            teste = AbdiMolin()
            axes = teste.draw_critical_values(ax=None, export=True)
            result = _check_file_exists("abdi_molin_critical_plot.png")
            rem_file = Path("abdi_molin_critical_plot.png")
            rem_file.unlink()
            self.assertTrue(result, "File was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            teste = AbdiMolin()
            axes = teste.draw_critical_values(ax=None, export=True, file_name="teste")
            result = _check_file_exists("teste.png")
            rem_file = Path("teste.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'teste.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            teste = AbdiMolin()
            axes = teste.draw_critical_values(ax=None, export=True, file_name="teste", extension='pdf')
            result = _check_file_exists("teste.pdf")
            rem_file = Path("teste.pdf")
            rem_file.unlink()
            self.assertTrue(result, "File 'teste.pdf' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            teste = AbdiMolin()
            axes = teste.draw_critical_values(ax=None, export=False, file_name="teste", extension='pdf')
            result = _check_file_exists("teste.pdf")
            try:
                rem_file = Path("teste.pdf")
                rem_file.unlink()
            except:
                pass
            self.assertFalse(result, "File 'teste.pdf' was created even with export=False")
            plt.close()

    def test_decimal_separator(self):
        with patch('matplotlib.pyplot.show') as p:
            teste = AbdiMolin()
            axes = teste.draw_critical_values(ax=None, decimal_separator=",")
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = False
                if ',' in temp:
                    result = True
            self.assertTrue(result, "No comma in y axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            teste = AbdiMolin()
            axes = teste.draw_critical_values(ax=None, decimal_separator=".")
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = True
                if ',' in temp:
                    result = False
            self.assertTrue(result, "No dot in y axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            teste = AbdiMolin()
            axes = teste.draw_critical_values(ax=None, decimal_separator=None)
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = True
                if ',' in temp:
                    result = False
            self.assertTrue(result, "No dot in y axis")
            plt.close()










# You fall, and you crawl and you break and you take what you get, and yoy turn it into... https://youtu.be/vNlDAi1VrB0?t=195

if __name__ == "__main__":
    unittest.main()
