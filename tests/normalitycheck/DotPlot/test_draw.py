"""Tests if the test_draw is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_None_test_draw. This class checks if the axes is returned, if the file is export when export = True and when extension = 'pdf' and if the file is not exported when export = True. The decimal_separator is also tested fot ".", "," and None.

---> Class Test_axestest_draw. This class checks if the axes is returned when ax is a previuous created ax. It also looks for a saved file if export=Tru, if legend was created or not, if it has x_label, some test about width and height, some test about dpi, some test about n_ticks

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/normalitycheck/DotPlot/test_draw.py
    or
    python -m unittest -b tests/normalitycheck/DotPlot/test_draw.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from unittest.mock import patch
from pycafee.normalitycheck.dotplot import DotPlot
from pycafee.utils.helpers import _check_file_exists
import numpy as np
import matplotlib.axes
import matplotlib.pyplot as plt
from pathlib import Path
from PIL import Image
import sys
import io
os.system('cls')


class Test_axes_test_draw(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9, 5.4, 4.8, 4.8, 4.3, 5.8, 5.7, 5.4, 5.1, 5.7,
                    5.1, 5.4, 5.1,4.6, 5.1, 4.8, 5.0, 5.0, 5.2, 5.2, 4.7, 4.8, 5.4, 5.2, 5.5, 4.9, 5.0, 5.5, 4.9, 4.4,
                    5.1, 5.0, 4.5, 4.4, 5.0, 5.1,4.8, 5.1, 4.6, 5.3, 5.0
                    ])

    def test_basic_plot(self):
        test = DotPlot()
        fig, ax = plt.subplots()
        x, y, axes = test.draw(self.x, ax=ax)
        result = isinstance(axes, matplotlib.axes.SubplotBase)
        self.assertTrue(result, "Ax not returned")
        result = isinstance(x, np.ndarray)
        self.assertTrue(result, "x is not a array")
        result = isinstance(y, np.ndarray)
        self.assertTrue(result, "y is not a array")
        plt.close()

        test = DotPlot()
        fig, ax = plt.subplots(figsize=(12,6))
        x, y, axes = test.draw(self.x, ax=ax)
        result = isinstance(axes, matplotlib.axes.SubplotBase)
        self.assertTrue(result, "Ax not returned")
        result = isinstance(x, np.ndarray)
        self.assertTrue(result, "x is not a array")
        result = isinstance(y, np.ndarray)
        self.assertTrue(result, "y is not a array")
        plt.close()

    # export=None, file_name=None,  extension=None
    def test_is_exported_plot(self):
        test = DotPlot()
        fig, ax = plt.subplots()
        x, y, axes = test.draw(self.x, ax=ax, export=True)
        result = _check_file_exists("dot_plot.png")
        try:
            rem_file = Path("dot_plot.png")
            rem_file.unlink()
        except:
            pass
        self.assertFalse(result, "File 'dot_plot.png' was created even with ax=ax")

        result = isinstance(axes, matplotlib.axes.SubplotBase)
        self.assertTrue(result, "Ax not returned")
        result = isinstance(x, np.ndarray)
        self.assertTrue(result, "x is not a array")
        result = isinstance(y, np.ndarray)
        self.assertTrue(result, "y is not a array")
        plt.close()

        test = DotPlot()
        fig, ax = plt.subplots()
        x, y, axes = test.draw(self.x, ax=ax, export=True, file_name="plot")
        result = _check_file_exists("plot.png")
        try:
            rem_file = Path("plot.png")
            rem_file.unlink()
        except:
            pass
        self.assertFalse(result, "File 'plot.png' was created even with ax=ax")

        result = isinstance(axes, matplotlib.axes.SubplotBase)
        self.assertTrue(result, "Ax not returned")
        result = isinstance(x, np.ndarray)
        self.assertTrue(result, "x is not a array")
        result = isinstance(y, np.ndarray)
        self.assertTrue(result, "y is not a array")
        plt.close()

        test = DotPlot()
        fig, ax = plt.subplots()
        x, y, axes = test.draw(self.x, ax=ax, export=True, file_name="plot", extension="pdf")
        result = _check_file_exists("plot.pdf")
        try:
            rem_file = Path("plot.pdf")
            rem_file.unlink()
        except:
            pass
        self.assertFalse(result, "File 'plot.pdf' was created even with ax=ax")

        result = isinstance(axes, matplotlib.axes.SubplotBase)
        self.assertTrue(result, "Ax not returned")
        result = isinstance(x, np.ndarray)
        self.assertTrue(result, "x is not a array")
        result = isinstance(y, np.ndarray)
        self.assertTrue(result, "y is not a array")
        plt.close()

    # legend_label=None legend=None,
    def test_legend(self):
        with patch('matplotlib.pyplot.show') as p:
            fig, axes = plt.subplots()
            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=axes, decimal_separator=",", legend=True)
            legends = axes.get_legend_handles_labels()
            self.assertEqual(legends[-1][0], 'data', msg="default legend not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            fig, axes = plt.subplots()
            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=axes, decimal_separator=",", legend=True, legend_label="Minha legenda")
            legends = axes.get_legend_handles_labels()
            self.assertEqual(legends[-1][0], 'Minha legenda', msg="personalized legend not match")
            legends = axes.get_legend()
            self.assertIsNotNone(legends, msg="legend None when legend was added")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            fig, axes = plt.subplots()
            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=axes, decimal_separator=",", legend=False)
            legends = axes.get_legend_handles_labels()
            self.assertEqual(legends[-1][0], 'data', msg="default legend not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            fig, axes = plt.subplots()
            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=axes, decimal_separator=",")
            legends = axes.get_legend()
            self.assertIsNone(legends, msg="legend not None with default")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            fig, axes = plt.subplots()
            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=axes, decimal_separator=",", legend=False, legend_label="Minha legenda")
            legends = axes.get_legend_handles_labels()
            self.assertEqual(legends[-1][0], 'Minha legenda', msg="personalized legend not match")
            legends = axes.get_legend()
            self.assertIsNone(legends, msg="legend not None with default")
            plt.close()

    # tight=None
    def test_tight(self):
        with patch('matplotlib.pyplot.show') as p:
            fig, axes = plt.subplots()
            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=axes, tight=False)
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 369.59999999999997, msg="wrong defalt height")
            self.assertAlmostEqual(ax_w, 496.0, msg="wrong defalt width")
            plt.close()

    # width='auto', height='auto',
    def test_width_height(self):
        with patch('matplotlib.pyplot.show') as p:
            fig, axes = plt.subplots()
            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=axes)
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 369.59999999999997, msg="wrong defalt height")
            self.assertAlmostEqual(ax_w, 496.0, msg="wrong defalt width")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            fig, axes = plt.subplots()
            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=axes, width=5, height=5)
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 369.59999999999997, msg="wrong personalized height")
            self.assertAlmostEqual(ax_w, 496.0, msg="wrong personalized width")
            plt.close()

    # n_ticks=None
    def test_n_ticks(self):
        with patch('matplotlib.pyplot.show') as p:
            fig, axes = plt.subplots()
            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=axes)
            x_ticks = axes.get_xticks()
            x_ticks_esperado = [4.2, 4.4, 4.6, 4.8, 5., 5.2, 5.4, 5.6, 5.8, 6.]
            for ticka, tickb in zip(x_ticks, x_ticks_esperado):
                self.assertAlmostEqual(ticka, tickb, msg="somethong wrogn with the xticks" )
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            fig, axes = plt.subplots()
            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=axes, n_ticks=10)
            x_ticks = axes.get_xticks()
            x_ticks_esperado = np.linspace(min(self.x), max(self.x), 10)
            for ticka, tickb in zip(x_ticks, x_ticks_esperado):
                self.assertEqual(ticka, tickb, "somethong wrogn with the xticks" )
            plt.close()

    # x_label=None,
    def test_x_label(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DotPlot()
            fig, axes = plt.subplots()
            x, y, axes = test.draw(self.x, ax=axes)
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(len(x_label), 0, "x_label not empty")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DotPlot()
            fig, axes = plt.subplots()
            x, y, axes = test.draw(self.x, ax=axes, x_label="my data")
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "my data", "x_label not 'my data'")
            plt.close()

    # decimal_separator=None
    def test_decimal_separator(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DotPlot()
            fig, axes = plt.subplots()
            x, y, axes = test.draw(self.x, ax=axes, decimal_separator=",")
            for text in axes.get_xticklabels():
                temp = text.get_text()
                result = False
                if ',' in temp:
                    result = True
            self.assertFalse(result, "Comma in x axis when it should not")
            plt.close()


        with patch('matplotlib.pyplot.show') as p:
            test = DotPlot()
            fig, axes = plt.subplots()
            x, y, axes = test.draw(self.x, ax=axes, decimal_separator=".")
            result = False
            for text in axes.get_xticklabels():
                temp = text.get_text()
                if '' in temp: # needs to be empty dueto the plot was not drawn yet
                    result = True
            self.assertTrue(result, "No dot in x axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DotPlot()
            fig, axes = plt.subplots()
            x, y, axes = test.draw(self.x, ax=axes, decimal_separator=None)
            result = False
            for text in axes.get_xticklabels():
                temp = text.get_text()
                if '' in temp: # needs to be empty dueto the plot was not drawn yet
                    result = True
            self.assertTrue(result, "No dot in x axis")
            plt.close()



class Test_None_test_draw(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9, 5.4, 4.8, 4.8, 4.3, 5.8, 5.7, 5.4, 5.1, 5.7,
                    5.1, 5.4, 5.1,4.6, 5.1, 4.8, 5.0, 5.0, 5.2, 5.2, 4.7, 4.8, 5.4, 5.2, 5.5, 4.9, 5.0, 5.5, 4.9, 4.4,
                    5.1, 5.0, 4.5, 4.4, 5.0, 5.1,4.8, 5.1, 4.6, 5.3, 5.0
                    ])

    def test_basic_plot(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=None)
            result = isinstance(axes, matplotlib.axes.SubplotBase)
            self.assertTrue(result, "Ax not returned")
            self.assertTrue(result, "Ax not returned")
            result = isinstance(x, np.ndarray)
            self.assertTrue(result, "x is not a array")
            result = isinstance(y, np.ndarray)
            self.assertTrue(result, "y is not a array")
            plt.close()


    # export=None, file_name=None,  extension=None
    def test_plot_export_file_already_exists(self):
        with patch('matplotlib.pyplot.show') as p:
            plt.figure()
            plt.scatter([1,1],[2,2])
            plt.savefig("dot_plot.png")
            plt.close()

            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput

            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=None)
            result = _check_file_exists("dot_plot_1.png")
            rem_file = Path("dot_plot.png")
            rem_file.unlink()
            try:
                rem_file = Path("dot_plot_1.png")
                rem_file.unlink()
            except:
                pass
            self.assertFalse(result, "File 'dot_plot_1.png' was created when it should not")
            plt.close()

            sys.stdout = sys.__stdout__
            expected = ""

            result = False
            if expected == capturedOutput.getvalue():
                result = True
            self.assertTrue(result, msg="Something wrong on the output when file already exists")

    # export=None, file_name=None,  extension=None
    def test_plot_export_file_already_exists_output(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DotPlot()
            plt.figure()
            plt.scatter([1,1],[2,2])
            plt.savefig("dot_plot.png")
            plt.close()

            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            x, y, axes = test.draw(self.x, ax=None, export=True)
            result = _check_file_exists("dot_plot_1.png")
            rem_file = Path("dot_plot.png")
            rem_file.unlink()
            rem_file = Path("dot_plot_1.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'dot_plot_1.png' was not created")
            plt.close()

            sys.stdout = sys.__stdout__
            expected_output = ["UserWarning",
                        "The 'dot_plot.png' file already exists in the current directory",
                        "The file was exported as 'dot_plot_1.png'"]

            for expected in expected_output:
                result = False
                if expected in capturedOutput.getvalue():
                    result = True
                self.assertTrue(result, msg="Somethign wrong on the output when file already exists")


        with patch('matplotlib.pyplot.show') as p:
            plt.figure()
            plt.scatter([1,1],[2,2])
            plt.savefig("bawtidaba.png")
            plt.close()

            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=None, export=True, file_name="bawtidaba")
            result = _check_file_exists("bawtidaba_1.png")
            rem_file = Path("bawtidaba.png")
            rem_file.unlink()
            rem_file = Path("bawtidaba_1.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'bawtidaba_1.png' was not created")
            plt.close()

            sys.stdout = sys.__stdout__
            expected_output = ["UserWarning",
                        "The 'bawtidaba.png' file already exists in the current directory",
                        "The file was exported as 'bawtidaba_1.png'"]

            for expected in expected_output:
                result = False
                if expected in capturedOutput.getvalue():
                    result = True
                self.assertTrue(result, msg="Somethign wrong on the output when file already exists")

     # export=None, file_name=None,  extension=None
    def test_plot_export(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DotPlot()
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            x, y, axes = test.draw(self.x, ax=None, export=True)
            result = _check_file_exists("dot_plot.png")
            rem_file = Path("dot_plot.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'dot_plot.png' was not created")
            plt.close()

            sys.stdout = sys.__stdout__
            expected = "The 'dot_plot.png' file was exported!"
            result = False
            if expected in capturedOutput.getvalue():
                result = True
            self.assertTrue(result, msg="Something wrong on the output when file already exists")


        with patch('matplotlib.pyplot.show') as p:
            test = DotPlot()
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            x, y, axes = test.draw(self.x, ax=None, export=True, file_name="teste")
            result = _check_file_exists("teste.png")
            rem_file = Path("teste.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'teste.png' was not created")
            plt.close()

            sys.stdout = sys.__stdout__
            expected = "The 'teste.png' file was exported!"
            result = False
            if expected in capturedOutput.getvalue():
                result = True
            self.assertTrue(result, msg="Something wrong on the output when file already exists")


        with patch('matplotlib.pyplot.show') as p:
            test = DotPlot()
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            x, y, axes = test.draw(self.x, ax=None, export=True, file_name="teste", extension='pdf')
            result = _check_file_exists("teste.pdf")
            rem_file = Path("teste.pdf")
            rem_file.unlink()
            self.assertTrue(result, "File 'teste.pdf' was not created")
            plt.close()

            sys.stdout = sys.__stdout__
            expected = "The 'teste.pdf' file was exported!"
            result = False
            if expected in capturedOutput.getvalue():
                result = True
            self.assertTrue(result, msg="Something wrong on the output when file already exists")


        with patch('matplotlib.pyplot.show') as p:
            test = DotPlot()
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            x, y, axes = test.draw(self.x, ax=None, export=False, file_name="teste", extension='pdf')
            result = _check_file_exists("teste.pdf")
            try:
                rem_file = Path("teste.pdf")
                rem_file.unlink()
            except:
                pass
            self.assertFalse(result, "File 'teste.pdf' was created even with export=False")
            plt.close()

            sys.stdout = sys.__stdout__
            expected = ""
            result = False
            if expected in capturedOutput.getvalue():
                result = True
            self.assertTrue(result, msg="Something wrong on the output when file already exists")

    # legend_label=None legend=None,
    def test_legend(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=None, decimal_separator=",", legend=True)
            legends = axes.get_legend_handles_labels()
            self.assertEqual(legends[-1][0], 'data', msg="default legend not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=None, decimal_separator=",", legend=True, legend_label="Minha legenda")
            legends = axes.get_legend_handles_labels()
            self.assertEqual(legends[-1][0], 'Minha legenda', msg="personalized legend not match")
            legends = axes.get_legend()
            self.assertIsNotNone(legends, msg="legend None when legend was added")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=None, decimal_separator=",", legend=False)
            legends = axes.get_legend_handles_labels()
            self.assertEqual(legends[-1][0], 'data', msg="default legend not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=None, decimal_separator=",")
            legends = axes.get_legend()
            self.assertIsNone(legends, msg="legend not None with default")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=None, decimal_separator=",", legend=False, legend_label="Minha legenda")
            legends = axes.get_legend_handles_labels()
            self.assertEqual(legends[-1][0], 'Minha legenda', msg="personalized legend not match")
            legends = axes.get_legend()
            self.assertIsNone(legends, msg="legend not None with default")
            plt.close()

    # tight=None
    def test_tight(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=None, tight=False)
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 154.0, msg="wrong defalt height")
            self.assertAlmostEqual(ax_w, 310.0, msg="wrong defalt width")
            plt.close()

    # width='auto', height='auto',
    def test_width_height(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=None)
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertEqual(ax_h, 142.11111111111111, "wrong defalt height")
            self.assertEqual(ax_w, 359.19696969696975, "wrong defalt width")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=None, width=5, height=5)
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertEqual(ax_h, 442.11111111111114, "wrong personalized height")
            self.assertEqual(ax_w, 470.0, "wrong personalized width")
            plt.close()

    # n_ticks=None
    def test_n_ticks(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=None)
            x_ticks = axes.get_xticks()
            x_ticks_esperado = [4., 4.25, 4.5, 4.75, 5., 5.25, 5.5, 5.75, 6.]
            for ticka, tickb in zip(x_ticks, x_ticks_esperado):
                self.assertEqual(ticka, tickb, "somethong wrogn with the xticks" )
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=None, n_ticks=10)
            x_ticks = axes.get_xticks()
            x_ticks_esperado = np.linspace(min(self.x), max(self.x), 10)
            for ticka, tickb in zip(x_ticks, x_ticks_esperado):
                self.assertEqual(ticka, tickb, "somethong wrogn with the xticks" )
            plt.close()

    # dpi=None
    def test_dpi(self):
        with patch('matplotlib.pyplot.show') as p:
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=None, export=True)
            image = Image.open("dot_plot.png")
            w, h = image.info["dpi"]
            image.close()
            self.assertEqual(w, 99.9998, "wrong defalt dpi")
            self.assertEqual(h, 99.9998, "wrong defalt dpi")
            rem_file = Path("dot_plot.png")
            rem_file.unlink()
            plt.close()

            sys.stdout = sys.__stdout__
            expected = "The 'dot_plot.png' file was exported!"
            result = False
            if expected in capturedOutput.getvalue():
                result = True
            self.assertTrue(result, msg="Something wrong on the output when file already exists")

        with patch('matplotlib.pyplot.show') as p:
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=None, export=True, dpi=300)
            image = Image.open("dot_plot.png")
            w, h = image.info["dpi"]
            image.close()
            self.assertEqual(w, 299.9994, "wrong personalized dpi")
            self.assertEqual(h, 299.9994, "wrong personalized dpi")
            rem_file = Path("dot_plot.png")
            rem_file.unlink()
            plt.close()

            sys.stdout = sys.__stdout__
            expected = "The 'dot_plot.png' file was exported!"
            result = False
            if expected in capturedOutput.getvalue():
                result = True
            self.assertTrue(result, msg="Something wrong on the output when file already exists")

    # x_label=None,
    def test_x_label(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=None)
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(len(x_label), 0, "x_label not empty")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=None, x_label="my data")
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "my data", "x_label not 'my data'")
            plt.close()

    # decimal_separator=None
    def test_decimal_separator(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=None, decimal_separator=",")
            for text in axes.get_xticklabels():
                temp = text.get_text()
                result = False
                if ',' in temp:
                    result = True
            self.assertTrue(result, "No comma in x axis")
            plt.close()


        with patch('matplotlib.pyplot.show') as p:
            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=None, decimal_separator=".")
            for text in axes.get_xticklabels():
                temp = text.get_text()
                result = True
                if ',' in temp:
                    result = False
            self.assertTrue(result, "No dot in x axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DotPlot()
            x, y, axes = test.draw(self.x, ax=None, decimal_separator=None)
            for text in axes.get_xticklabels():
                temp = text.get_text()
                result = True
                if ',' in temp:
                    result = False
            self.assertTrue(result, "No dot in x axis")
            plt.close()



if __name__ == "__main__":
    unittest.main()
