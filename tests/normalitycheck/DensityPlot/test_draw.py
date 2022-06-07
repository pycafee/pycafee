"""Tests if the test_draw is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_None_test_draw. This class checks if the axes is returned, if the file is export when export = True and when extension = 'pdf' and if the file is not exported when export = True. The decimal_separator is also tested fot ".", "," and None.

---> Class Test_axestest_draw. This class checks if the axes is returned when ax is a previuous created ax. It also looks for a saved file if export=Tru, if legend was created or not, if it has x_label, some test about width and height, some test about dpi, some test about almost everything

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/normalitycheck/DensityPlot/test_draw.py
    or
    python -m unittest -b tests/normalitycheck/DensityPlot/test_draw.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from unittest.mock import patch
from pycafee.normalitycheck.densityplot import DensityPlot
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
        cls.y = np.array([1,2,3,4,5,6,7,8,9])

    def test_basic_plot(self):
        test = DensityPlot()
        fig, ax = plt.subplots()
        x, y, z, axes = test.draw(self.x, ax=ax)
        result = isinstance(axes, matplotlib.axes.SubplotBase)
        self.assertTrue(result, "Ax not returned")
        result = isinstance(x, np.ndarray)
        self.assertTrue(result, "x is not a array")
        result = isinstance(y, np.ndarray)
        self.assertTrue(result, "y is not a array")
        result = isinstance(z, dict)
        self.assertTrue(result, "central tendency is not a dict")
        self.assertEqual(len(z), 0, "central tendexy not empty dict")
        plt.close()

        test = DensityPlot()
        fig, ax = plt.subplots(figsize=(12,6))
        x, y, z, axes = test.draw(self.x, ax=ax)
        result = isinstance(axes, matplotlib.axes.SubplotBase)
        self.assertTrue(result, "Ax not returned")
        result = isinstance(x, np.ndarray)
        self.assertTrue(result, "x is not a array")
        result = isinstance(y, np.ndarray)
        self.assertTrue(result, "y is not a array")
        result = isinstance(z, dict)
        self.assertTrue(result, "central tendency is not a dict")
        self.assertEqual(len(z), 0, "central tendexy not empty dict")
        plt.close()


    # bw_method=None,
    def test_bw_method(self):

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, central_tendency, axes = test.draw(self.x, ax=axes, bw_method=None)
            result = isinstance(x, np.ndarray)
            self.assertTrue(result, "x is not a array")
            result = isinstance(y, np.ndarray)
            self.assertTrue(result, "y is not a array")
            result = isinstance(central_tendency, dict)
            self.assertTrue(result, "central_tendency is not a dict")
            result = isinstance(axes, matplotlib.axes.SubplotBase)
            self.assertTrue(result, "Ax not returned")

            self.assertAlmostEqual(x[5], 4.307507507507507, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(y[5], 0.24553462195266776, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(x[42], 4.363063063063063, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(y[42], 0.3105878575930724, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(x[71], 4.406606606606607, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(y[71], 0.36020389827333554, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(x[90], 4.435135135135135, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(y[90], 0.39163910716800165, msg="Something wrong with kde estimation")
            self.assertEqual(len(central_tendency), 0, msg="Central tendency not empty for default parameters")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, central_tendency, axes = test.draw(self.x, ax=axes, bw_method="scott")
            result = isinstance(x, np.ndarray)
            self.assertTrue(result, "x is not a array")
            result = isinstance(y, np.ndarray)
            self.assertTrue(result, "y is not a array")
            result = isinstance(central_tendency, dict)
            self.assertTrue(result, "central_tendency is not a dict")
            result = isinstance(axes, matplotlib.axes.SubplotBase)
            self.assertTrue(result, "Ax not returned")

            self.assertAlmostEqual(x[5], 4.307507507507507, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(y[5], 0.24553462195266776, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(x[42], 4.363063063063063, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(y[42], 0.3105878575930724, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(x[71], 4.406606606606607, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(y[71], 0.36020389827333554, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(x[90], 4.435135135135135, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(y[90], 0.39163910716800165, msg="Something wrong with kde estimation")
            self.assertEqual(len(central_tendency), 0, msg="Central tendency not empty for default parameters")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, central_tendency, axes = test.draw(self.x, ax=axes, bw_method="silverman")
            result = isinstance(x, np.ndarray)
            self.assertTrue(result, "x is not a array")
            result = isinstance(y, np.ndarray)
            self.assertTrue(result, "y is not a array")
            result = isinstance(central_tendency, dict)
            self.assertTrue(result, "central_tendency is not a dict")
            result = isinstance(axes, matplotlib.axes.SubplotBase)
            self.assertTrue(result, "Ax not returned")

            self.assertAlmostEqual(x[5], 4.307507507507507, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(y[5], 0.24645513104212644, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(x[42], 4.363063063063063, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(y[42], 0.3097433651366933, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(x[71], 4.406606606606607, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(y[71], 0.3588525778348663, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(x[90], 4.435135135135135, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(y[90], 0.39041165000025746, msg="Something wrong with kde estimation")
            self.assertEqual(len(central_tendency), 0, msg="Central tendency not empty for default parameters")
            plt.close()


    # bw_method=None,
    def test_bw_method_raises(self):
        with self.assertRaises(ValueError, msg="Does not raised error when bw_method not scott or silverman"):
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, axes = test.draw(self.x, ax=axes, bw_method="scot")
            plt.close()

        with self.assertRaises(ValueError, msg="Does not raised error when bw_method not scott or silverman"):
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, axes = test.draw(self.x, ax=axes, bw_method="scottt")
            plt.close()

        with self.assertRaises(ValueError, msg="Does not raised error when bw_method not scott or silverman"):
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, axes = test.draw(self.x, ax=axes, bw_method="silvermen")
            plt.close()

        with self.assertRaises(ValueError, msg="Does not raised error when bw_method not scott or silverman"):
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, axes = test.draw(self.x, ax=axes, bw_method="silvermann")
            plt.close()


    # bw_method=None,
    def test_bw_method_raises_output(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        test = DensityPlot()
        fig, axes = plt.subplots()
        try:
            x, y, axes = test.draw(self.x, ax=axes, bw_method="scot")
        except:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'bw_method' parameter only accepts 'scott' or 'silverman' as key, but we got 'scot'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="Somethign wrong on the output when file already exists")


        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        test = DensityPlot(language='pt-br')
        fig, axes = plt.subplots()
        try:
            x, y, axes = test.draw(self.x, ax=axes, bw_method="scottt")
        except:
            pass
        sys.stdout = sys.__stdout__
        expected = "O parâmetro 'bw_method' aceita apenas 'scott' ou 'silverman' como key, mas recebemos 'scottt'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="Somethign wrong on the output when file already exists")


        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        test = DensityPlot()
        fig, axes = plt.subplots()
        try:
            x, y, axes = test.draw(self.x, ax=axes, bw_method="silvermen")
        except:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'bw_method' parameter only accepts 'scott' or 'silverman' as key, but we got 'silvermen'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="Somethign wrong on the output when file already exists")


        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        test = DensityPlot(language='pt-br')
        fig, axes = plt.subplots()
        try:
            x, y, axes = test.draw(self.x, ax=axes, bw_method="silvermann")
        except:
            pass
        sys.stdout = sys.__stdout__
        expected = "O parâmetro 'bw_method' aceita apenas 'scott' ou 'silverman' como key, mas recebemos 'silvermann'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="Somethign wrong on the output when file already exists")


    # which=None,
    def test_which(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, central_tendency, axes = test.draw(self.x, which=None, ax=axes)
            self.assertIsInstance(central_tendency, dict, msg="central_tendency is not a dict")
            self.assertEqual(len(central_tendency), 0, msg="central tendency not empty when it should")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, central_tendency, axes = test.draw(self.x, which='mean', ax=axes)
            self.assertEqual(central_tendency['mean'][0], 5.006, msg="wrong mean")
            self.assertAlmostEqual(central_tendency['mean'][1], 1.1185247245402423, msg="wrong kde for mean")
            mean = axes.get_children()[1]
            mean = mean.get_label()
            self.assertEqual(mean, "Mean")
            kde = axes.get_children()[2]
            kde = kde.get_label()
            self.assertEqual(kde, "Non-parametric density")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, central_tendency, axes = test.draw(self.x, which='median', ax=axes)
            self.assertEqual(central_tendency['median'][0], 5.0, msg="wrong median")
            self.assertAlmostEqual(central_tendency['median'][1], 1.117529174648972, msg="wrong kde for median")
            median = axes.get_children()[1]
            median = median.get_label()
            self.assertEqual(median, "Median")
            kde = axes.get_children()[2]
            kde = kde.get_label()
            self.assertEqual(kde, "Non-parametric density")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, central_tendency, axes = test.draw(self.x, which='mode', ax=axes)
            self.assertEqual(central_tendency['mode'][0][0], 5.1, msg="wrong mode")
            self.assertAlmostEqual(central_tendency['mode'][0][1], 1.058253577481665, msg="wrong kde for mode")
            self.assertEqual(central_tendency['mode'][1][0], 5.0, msg="wrong mode")
            self.assertAlmostEqual(central_tendency['mode'][1][1], 1.117529174648972, msg="wrong kde for mode")
            modes = axes.get_children()
            mode = modes[1].get_label()
            self.assertEqual(mode, "_collection1")
            mode = modes[2].get_label()
            self.assertEqual(mode, "Mode")
            mode = modes[3].get_label()
            self.assertEqual(mode, "Non-parametric density")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, central_tendency, axes = test.draw(self.x, which='all', ax=axes)
            self.assertEqual(central_tendency['mean'][0], 5.006, msg="wrong mean")
            self.assertAlmostEqual(central_tendency['mean'][1], 1.1185247245402423, msg="wrong kde for mean")
            self.assertEqual(central_tendency['median'][0], 5.0, msg="wrong median")
            self.assertAlmostEqual(central_tendency['median'][1], 1.117529174648972, msg="wrong kde for median")
            self.assertEqual(central_tendency['mode'][0][0], 5.1, msg="wrong mode")
            self.assertAlmostEqual(central_tendency['mode'][0][1], 1.058253577481665, msg="wrong kde for mode")
            self.assertEqual(central_tendency['mode'][1][0], 5.0, msg="wrong mode")
            self.assertAlmostEqual(central_tendency['mode'][1][1], 1.117529174648972, msg="wrong kde for mode")
            filhos = axes.get_children()
            mean = filhos[1].get_label()
            self.assertEqual(mean, "Mean")
            median = filhos[2].get_label()
            self.assertEqual(median, "Median")
            mode = filhos[3].get_label()
            self.assertEqual(mode, "_collection3")
            mode = filhos[4].get_label()
            self.assertEqual(mode, "Mode")
            kde = filhos[5].get_label()
            self.assertEqual(kde, "Non-parametric density")
            plt.close()


        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, central_tendency, axes = test.draw(self.x, which='mean,median', ax=axes)
            self.assertEqual(central_tendency['mean'][0], 5.006, msg="wrong mean")
            self.assertAlmostEqual(central_tendency['mean'][1], 1.1185247245402423, msg="wrong kde for mean")
            self.assertEqual(central_tendency['median'][0], 5.0, msg="wrong median")
            self.assertAlmostEqual(central_tendency['median'][1], 1.117529174648972, msg="wrong kde for median")
            filhos = axes.get_children()
            mean = filhos[1].get_label()
            self.assertEqual(mean, "Mean")
            median = filhos[2].get_label()
            self.assertEqual(median, "Median")
            kde = filhos[3].get_label()
            self.assertEqual(kde, "Non-parametric density")
            with self.assertRaises(KeyError, msg="Does not raised key error when mode is out of the plot"):
                result = central_tendency['mode'][0][0]
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, central_tendency, axes = test.draw(self.x, which='mean,mode', ax=axes)
            self.assertEqual(central_tendency['mean'][0], 5.006, msg="wrong mean")
            self.assertAlmostEqual(central_tendency['mean'][1], 1.1185247245402423, msg="wrong kde for mean")
            self.assertEqual(central_tendency['mode'][0][0], 5.1, msg="wrong mode")
            self.assertAlmostEqual(central_tendency['mode'][0][1], 1.058253577481665, msg="wrong kde for mode")
            self.assertEqual(central_tendency['mode'][1][0], 5.0, msg="wrong mode")
            self.assertAlmostEqual(central_tendency['mode'][1][1], 1.117529174648972, msg="wrong kde for mode")
            filhos = axes.get_children()
            mean = filhos[1].get_label()
            self.assertEqual(mean, "Mean")
            mode = filhos[2].get_label()
            self.assertEqual(mode, "_collection2")
            mode = filhos[3].get_label()
            self.assertEqual(mode, "Mode")
            kde = filhos[4].get_label()
            self.assertEqual(kde, "Non-parametric density")
            with self.assertRaises(KeyError, msg="Does not raised key error when median is out of the plot"):
                result = central_tendency['median'][0][0]
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, central_tendency, axes = test.draw(self.x, which='median,mode', ax=axes)
            self.assertEqual(central_tendency['median'][0], 5.0, msg="wrong median")
            self.assertAlmostEqual(central_tendency['median'][1], 1.117529174648972, msg="wrong kde for median")
            self.assertEqual(central_tendency['mode'][0][0], 5.1, msg="wrong mode")
            self.assertAlmostEqual(central_tendency['mode'][0][1], 1.058253577481665, msg="wrong kde for mode")
            self.assertEqual(central_tendency['mode'][1][0], 5.0, msg="wrong mode")
            self.assertAlmostEqual(central_tendency['mode'][1][1], 1.117529174648972, msg="wrong kde for mode")
            filhos = axes.get_children()
            median = filhos[1].get_label()
            self.assertEqual(median, "Median")
            mode = filhos[2].get_label()
            self.assertEqual(mode, "_collection2")
            mode = filhos[3].get_label()
            self.assertEqual(mode, "Mode")
            kde = filhos[4].get_label()
            self.assertEqual(kde, "Non-parametric density")
            with self.assertRaises(KeyError, msg="Does not raised key error when mean is out of the plot"):
                result = central_tendency['mean'][0][0]
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, central_tendency, axes = test.draw(self.y, which='all', ax=axes)
            self.assertEqual(central_tendency['mean'][0], 5.0, msg="wrong mean")
            self.assertAlmostEqual(central_tendency['mean'][1], 0.11002722425258299, msg="wrong kde for mean")
            self.assertEqual(central_tendency['median'][0], 5.0, msg="wrong median")
            self.assertAlmostEqual(central_tendency['median'][1], 0.11002722425258299, msg="wrong kde for median")
            filhos = axes.get_children()
            mean = filhos[1].get_label()
            self.assertEqual(mean, "Mean")
            median = filhos[2].get_label()
            self.assertEqual(median, "Median")
            kde = filhos[3].get_label()
            self.assertEqual(kde, "Non-parametric density")
            with self.assertRaises(KeyError, msg="Does not raised key error for mode when data does not have mode"):
                result = central_tendency['mode'][0][0]
            plt.close()


    # x_label=None,
    def test_x_label(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, z, axes = test.draw(self.x, ax=axes)
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "data", "x_label not empty")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, z, axes = test.draw(self.x, x_label="My data", ax=axes)
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "My data", "x_label not empty")
            plt.close()


    # y_label=None,
    def test_y_label(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, z, axes = test.draw(self.x, ax=axes)
            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "y_label not a string")
            self.assertEqual(y_label, "Non-parametric density", "y_label not empty")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, z, axes = test.draw(self.x, y_label="My y label", ax=axes)
            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "y_label not a string")
            self.assertEqual(y_label, "My y label", "y_label not empty")
            plt.close()


    # width='default', height='default',
    def test_width_height(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, z, axes = test.draw(self.x, ax=axes)
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 369.599999999999, msg="wrong defalt height")
            self.assertAlmostEqual(ax_w, 496.0, msg="wrong defalt width")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, z, axes = test.draw(self.x, width=5, height=5, ax=axes)
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 369.59999999999, msg="wrong personalized height")
            self.assertAlmostEqual(ax_w, 496.0, msg="wrong personalized width")
            plt.close()


    # tight=None,
    def test_tight(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, z, axes = test.draw(self.x, tight=True, ax=axes)
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 369.599999999999, msg="wrong defalt height")
            self.assertAlmostEqual(ax_w, 496.0, msg="wrong defalt width")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, z, axes = test.draw(self.x, width=5, height=5, tight=True, ax=axes)
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 369.599999999999, msg="wrong defalt height")
            self.assertAlmostEqual(ax_w, 496.0, msg="wrong defalt width")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, z, axes = test.draw(self.x, tight=False, ax=axes)
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 369.599999999999, msg="wrong defalt height")
            self.assertAlmostEqual(ax_w, 496.0, msg="wrong defalt width")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, z, axes = test.draw(self.x, width=5, height=5, tight=False, ax=axes)
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 369.599999999999, msg="wrong defalt height")
            self.assertAlmostEqual(ax_w, 496.0, msg="wrong defalt width")
            plt.close()


    # export=None, file_name=None,  extension=None
    def test_is_exported_plot(self):
        test = DensityPlot()
        fig, ax = plt.subplots()
        x, y, central_tendency, axes = test.draw(self.x, ax=ax, export=True)
        result = _check_file_exists("kernel_density.png")
        try:
            rem_file = Path("kernel_density.png")
            rem_file.unlink()
        except:
            pass
        self.assertFalse(result, "File 'kernel_density.png' was created even with ax=ax")

        result = isinstance(axes, matplotlib.axes.SubplotBase)
        self.assertTrue(result, "Ax not returned")
        result = isinstance(x, np.ndarray)
        self.assertTrue(result, "x is not a array")
        result = isinstance(y, np.ndarray)
        self.assertTrue(result, "y is not a array")
        self.assertIsInstance(central_tendency, dict, msg="Central tendendy not a dict")
        plt.close()

        test = DensityPlot()
        fig, ax = plt.subplots()
        x, y, central_tendency, axes = test.draw(self.x, ax=ax, export=True, file_name="plot")
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
        self.assertIsInstance(central_tendency, dict, msg="Central tendendy not a dict")
        plt.close()

        test = DensityPlot()
        fig, ax = plt.subplots()
        x, y, central_tendency, axes = test.draw(self.x, ax=ax, export=True, file_name="plot", extension="pdf")
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
        self.assertIsInstance(central_tendency, dict, msg="Central tendendy not a dict")
        plt.close()


    # plot_design='gray',
    def test_plot_design(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, z, axes = test.draw(self.x, ax=axes)
            kde_line = axes.get_children()[1]
            self.assertEqual(kde_line.get_color(), "k", "default kde color not black")
            self.assertEqual(kde_line.get_lw(), 1.5, "default kde lw not 1.5")
            self.assertEqual(kde_line.get_ls(), '-', "default kde ls not '-'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, z, axes = test.draw(self.x, plot_design ='gray', ax=axes)
            kde_line = axes.get_children()[1]
            self.assertEqual(kde_line.get_color(), "k", "default kde color not black")
            self.assertEqual(kde_line.get_lw(), 1.5, "default kde lw not 1.5")
            self.assertEqual(kde_line.get_ls(), '-', "default kde ls not '-'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, z, axes = test.draw(self.x, plot_design ='gray', which="mean", ax=axes)
            kde_line = axes.get_children()[2]
            self.assertEqual(kde_line.get_color(), "k", "default kde color not black")
            self.assertEqual(kde_line.get_lw(), 1.5, "default kde lw not 1.5")
            self.assertEqual(kde_line.get_ls(), '-', "default kde ls not '-'")
            mean_line = axes.get_children()[1]
            self.assertEqual(round(mean_line.get_color()[0][0], 5), round(0.41176471, 5), "default mean color not dimgray")
            self.assertEqual(round(mean_line.get_color()[0][1], 5), round(0.41176471, 5), "default mean color not dimgray")
            self.assertEqual(round(mean_line.get_color()[0][2], 5), round(0.41176471, 5), "default mean color not dimgray")
            self.assertEqual(round(mean_line.get_color()[0][3], 1), round(1.0, 1), "default mean color not dimgray")
            self.assertEqual(mean_line.get_lw()[0], 1.5, "default mean lw not 1.5")
            self.assertEqual(mean_line.get_ls()[0][0], 0.0, "default mean ls not '--'")
            self.assertEqual(round(mean_line.get_ls()[0][1][0], 5), round(5.550000000000001, 5), "default mean ls not '--'")
            self.assertEqual(round(mean_line.get_ls()[0][1][1], 5), round(2.4000000000000004, 5), "default mean ls not '--'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, z, axes = test.draw(self.x, plot_design ='gray', which="median", ax=axes)
            kde_line = axes.get_children()[2]
            self.assertEqual(kde_line.get_color(), "k", "default kde color not black")
            self.assertEqual(kde_line.get_lw(), 1.5, "default kde lw not 1.5")
            self.assertEqual(kde_line.get_ls(), '-', "default kde ls not '-'")
            median_line = axes.get_children()[1]
            self.assertEqual(round(median_line.get_color()[0][0], 5), round(0.6627451, 5), "default median color not darkgray")
            self.assertEqual(round(median_line.get_color()[0][1], 5), round(0.6627451, 5), "default median color not darkgray")
            self.assertEqual(round(median_line.get_color()[0][2], 5), round(0.6627451, 5), "default median color not darkgray")
            self.assertEqual(round(median_line.get_color()[0][3], 1), round(1.0, 1), "default median color not darkgray")
            self.assertEqual(median_line.get_lw()[0], 1.5, "default median lw not 1.5")
            self.assertEqual(median_line.get_ls()[0][0], 0.0, "default median ls not '--'")
            self.assertEqual(round(median_line.get_ls()[0][1][0], 5), round(5.550000000000001, 5), "default median ls not '--'")
            self.assertEqual(round(median_line.get_ls()[0][1][1], 5), round(2.4000000000000004, 5), "default median ls not '--'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, z, axes = test.draw(self.x, plot_design ='gray', which="mode", ax=axes)
            kde_line = axes.get_children()[3]
            self.assertEqual(kde_line.get_color(), "k", "default kde color not black")
            self.assertEqual(kde_line.get_lw(), 1.5, "default kde lw not 1.5")
            self.assertEqual(kde_line.get_ls(), '-', "default kde ls not '-'")
            mode_line = axes.get_children()[1]
            self.assertEqual(round(mode_line.get_color()[0][0], 5), round(0.82745098, 5), "default mode color not lightgray")
            self.assertEqual(round(mode_line.get_color()[0][1], 5), round(0.82745098, 5), "default mode color not lightgray")
            self.assertEqual(round(mode_line.get_color()[0][2], 5), round(0.82745098, 5), "default mode color not lightgray")
            self.assertEqual(round(mode_line.get_color()[0][3], 1), round(1.0, 1), "default mode color not lightgray")
            self.assertEqual(mode_line.get_lw()[0], 1.5, "default mode lw not 1.5")
            self.assertEqual(mode_line.get_ls()[0][0], 0.0, "default mode ls not '--'")
            self.assertEqual(round(mode_line.get_ls()[0][1][0], 5), round(5.550000000000001, 5), "default mode ls not '--'")
            self.assertEqual(round(mode_line.get_ls()[0][1][1], 5), round(2.4000000000000004, 5), "default mode ls not '--'")
            mode_line = axes.get_children()[2]
            self.assertEqual(round(mode_line.get_color()[0][0], 5), round(0.82745098, 5), "default mode color not lightgray")
            self.assertEqual(round(mode_line.get_color()[0][1], 5), round(0.82745098, 5), "default mode color not lightgray")
            self.assertEqual(round(mode_line.get_color()[0][2], 5), round(0.82745098, 5), "default mode color not lightgray")
            self.assertEqual(round(mode_line.get_color()[0][3], 1), round(1.0, 1), "default mode color not lightgray")
            self.assertEqual(mode_line.get_lw()[0], 1.5, "default mode lw not 1.5")
            self.assertEqual(mode_line.get_ls()[0][0], 0.0, "default mode ls not '--'")
            self.assertEqual(round(mode_line.get_ls()[0][1][0], 5), round(5.550000000000001, 5), "default mode ls not '--'")
            self.assertEqual(round(mode_line.get_ls()[0][1][1], 5), round(2.4000000000000004, 5), "default mode ls not '--'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "kde": ['red', '-', 2.5],
                "Mean": ['white', ':', 1.0],
                "Median": ['orange', '-', 1.1],
                "Mode": ['yellow', '-', 1.1],
                "Area": ['lightgreen'],
            }
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, z, axes = test.draw(self.x, plot_design=plot_design, which="all", ax=axes)
            kde_line = axes.get_children()[5]
            self.assertEqual(kde_line.get_color(), "red", "personalized kde color not red")
            self.assertEqual(kde_line.get_lw(), 2.5, "personalized kde lw not 2.5")
            self.assertEqual(kde_line.get_ls(), '-', "personalized kde ls not '-'")
            mean_line = axes.get_children()[1]
            self.assertEqual(mean_line.get_color()[0][0], 1., "personalized mean color not white")
            self.assertEqual(mean_line.get_color()[0][1], 1., "personalized mean color not white")
            self.assertEqual(mean_line.get_color()[0][2], 1., "personalized mean color not white")
            self.assertEqual(mean_line.get_color()[0][3], 1., "personalized mean color not white")
            self.assertEqual(mean_line.get_lw()[0], 1.0, "personalized mean lw not 1.0")
            self.assertEqual(mean_line.get_ls()[0][0], 0.0, "personalized mean ls not ':'")
            self.assertEqual(mean_line.get_ls()[0][1][0], 1.0, "personalized mean ls not ':'")
            self.assertEqual(mean_line.get_ls()[0][1][1], 1.65, "personalized mean ls not ':'")
            median_line = axes.get_children()[2]
            self.assertEqual(median_line.get_color()[0][0], 1., "personalized median color not orange")
            self.assertEqual(round(median_line.get_color()[0][1], 5), round(0.64705882, 5), "personalized median color not orange")
            self.assertEqual(median_line.get_color()[0][2], 0., "personalized median color not orange")
            self.assertEqual(median_line.get_color()[0][3], 1., "personalized median color not orange")
            self.assertEqual(median_line.get_lw()[0], 1.1, "personalized median lw not 1.1")
            self.assertEqual(median_line.get_ls()[0][0], None, "personalized median ls not '-'")
            self.assertEqual(median_line.get_ls()[0][1], None, "personalized median ls not '-'")
            mode_line = axes.get_children()[3]
            self.assertEqual(mode_line.get_color()[0][0], 1., "personalized mode color not yellow")
            self.assertEqual(mode_line.get_color()[0][1], 1., "personalized mode color not yellow")
            self.assertEqual(mode_line.get_color()[0][2], 0., "personalized mode color not yellow")
            self.assertEqual(mode_line.get_color()[0][3], 1., "personalized mode color not yellow")
            self.assertEqual(mode_line.get_lw()[0], 1.1, "personalized mode lw not 1.1")
            self.assertEqual(mode_line.get_ls()[0][0], None, "personalized mode ls not '-'")
            self.assertEqual(mode_line.get_ls()[0][1], None, "personalized mode ls not '-'")
            mode_line = axes.get_children()[4]
            self.assertEqual(mode_line.get_color()[0][0], 1., "personalized mode color not yellow")
            self.assertEqual(mode_line.get_color()[0][1], 1., "personalized mode color not yellow")
            self.assertEqual(mode_line.get_color()[0][2], 0., "personalized mode color not yellow")
            self.assertEqual(mode_line.get_color()[0][3], 1., "personalized mode color not yellow")
            self.assertEqual(mode_line.get_lw()[0], 1.1, "personalized mode lw not 1.1")
            self.assertEqual(mode_line.get_ls()[0][0], None, "personalized mode ls not '-'")
            self.assertEqual(mode_line.get_ls()[0][1], None, "personalized mode ls not '-'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, z, axes = test.draw(self.x, plot_design ='gray', ax=axes)
            kde_line = axes.get_children()[1]
            self.assertEqual(kde_line.get_color(), "k", "default kde color not black")
            self.assertEqual(kde_line.get_lw(), 1.5, "default kde lw not 1.5")
            self.assertEqual(kde_line.get_ls(), '-', "default kde ls not '-'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, z, axes = test.draw(self.x, plot_design ='colored', ax=axes)
            kde_line = axes.get_children()[1]
            self.assertEqual(kde_line.get_color(), "k", "colored kde color not black")
            self.assertEqual(kde_line.get_lw(), 1.5, "colored kde lw not 1.5")
            self.assertEqual(kde_line.get_ls(), '-', "colored kde ls not '-'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, z, axes = test.draw(self.x, which="mean", plot_design='colored', ax=axes)
            kde_line = axes.get_children()[2]
            self.assertEqual(kde_line.get_color(), "k", "colored kde color not black")
            self.assertEqual(kde_line.get_lw(), 1.5, "colored kde lw not 1.5")
            self.assertEqual(kde_line.get_ls(), '-', "colored kde ls not '-'")
            mean_line = axes.get_children()[1]
            self.assertEqual(round(mean_line.get_color()[0][0], 1), round(1., 1), "colored mean color not red")
            self.assertEqual(round(mean_line.get_color()[0][1], 1), round(0.0, 1), "colored mean color not red")
            self.assertEqual(round(mean_line.get_color()[0][2], 1), round(0.0, 1), "colored mean color not red")
            self.assertEqual(round(mean_line.get_color()[0][3], 1), round(1.0, 1), "colored mean color not red")
            self.assertEqual(mean_line.get_lw()[0], 1.5, "colored mean lw not 1.5")
            self.assertEqual(mean_line.get_ls()[0][0], 0.0, "colored mean ls not '--'")
            self.assertEqual(round(mean_line.get_ls()[0][1][0], 5), round(5.550000000000001, 5), "colored mean ls not '--'")
            self.assertEqual(round(mean_line.get_ls()[0][1][1], 5), round(2.4000000000000004, 5), "colored mean ls not '--'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, z, axes = test.draw(self.x, plot_design ='colored', which="median", ax=axes)
            kde_line = axes.get_children()[2]
            self.assertEqual(kde_line.get_color(), "k", "colored kde color not black")
            self.assertEqual(kde_line.get_lw(), 1.5, "colored kde lw not 1.5")
            self.assertEqual(kde_line.get_ls(), '-', "colored kde ls not '-'")
            median_line = axes.get_children()[1]
            self.assertEqual(round(median_line.get_color()[0][0], 1), round(0.0, 1), "colored median color not blue")
            self.assertEqual(round(median_line.get_color()[0][1], 1), round(0.0, 1), "colored median color not blue")
            self.assertEqual(round(median_line.get_color()[0][2], 1), round(1.0, 1), "colored median color not blue")
            self.assertEqual(round(median_line.get_color()[0][3], 1), round(1.0, 1), "colored median color not darkgray")
            self.assertEqual(median_line.get_lw()[0], 1.5, "colored median lw not 1.5")
            self.assertEqual(median_line.get_ls()[0][0], 0.0, "colored median ls not '--'")
            self.assertEqual(round(median_line.get_ls()[0][1][0], 5), round(5.550000000000001, 5), "colored median ls not '--'")
            self.assertEqual(round(median_line.get_ls()[0][1][1], 5), round(2.4000000000000004, 5), "colored median ls not '--'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, z, axes = test.draw(self.x, plot_design ='colored', which="mode", ax=axes)
            kde_line = axes.get_children()[3]
            self.assertEqual(kde_line.get_color(), "k", "colored kde color not black")
            self.assertEqual(kde_line.get_lw(), 1.5, "colored kde lw not 1.5")
            self.assertEqual(kde_line.get_ls(), '-', "colored kde ls not '-'")
            mode_line = axes.get_children()[1]
            self.assertEqual(round(mode_line.get_color()[0][0], 1), round(0.0, 1), "colored mode color not green")
            self.assertEqual(round(mode_line.get_color()[0][1], 5), round(0.50196078, 5), "colored mode color not green")
            self.assertEqual(round(mode_line.get_color()[0][2], 1), round(0.0, 1), "colored mode color not green")
            self.assertEqual(round(mode_line.get_color()[0][3], 1), round(1.0, 1), "colored mode color not green")
            self.assertEqual(mode_line.get_lw()[0], 1.5, "colored mode lw not 1.5")
            self.assertEqual(mode_line.get_ls()[0][0], 0.0, "colored mode ls not '--'")
            self.assertEqual(round(mode_line.get_ls()[0][1][0], 5), round(5.550000000000001, 5), "colored mode ls not '--'")
            self.assertEqual(round(mode_line.get_ls()[0][1][1], 5), round(2.4000000000000004, 5), "colored mode ls not '--'")
            mode_line = axes.get_children()[2]
            self.assertEqual(round(mode_line.get_color()[0][0], 1), round(0.0, 1), "colored mode color not green")
            self.assertEqual(round(mode_line.get_color()[0][1], 5), round(0.50196078, 5), "colored mode color not green")
            self.assertEqual(round(mode_line.get_color()[0][2], 1), round(0.0, 1), "colored mode color not green")
            self.assertEqual(round(mode_line.get_color()[0][3], 1), round(1.0, 1), "colored mode color not green")
            self.assertEqual(mode_line.get_lw()[0], 1.5, "colored mode lw not 1.5")
            self.assertEqual(mode_line.get_ls()[0][0], 0.0, "colored mode ls not '--'")
            self.assertEqual(round(mode_line.get_ls()[0][1][0], 5), round(5.550000000000001, 5), "colored mode ls not '--'")
            self.assertEqual(round(mode_line.get_ls()[0][1][1], 5), round(2.4000000000000004, 5), "colored mode ls not '--'")
            plt.close()


    # legend=None,
    def test_legend(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, central_tendency, axes = test.draw(self.x, ax=axes)
            legends = axes.get_legend_handles_labels()
            self.assertEqual(legends[-1][0], 'Non-parametric density', msg="default legend not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, central_tendency, axes = test.draw(self.x, legend=True, ax=axes)
            legends = axes.get_legend_handles_labels()
            self.assertEqual(legends[-1][0], 'Non-parametric density', msg="default legend not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, central_tendency, axes = test.draw(self.x, ax=axes)
            legend_texts = axes.get_legend()
            legend_text = legend_texts.get_texts()[0]
            text = legend_text.get_text()
            self.assertEqual(text, 'Non-parametric density', msg="default legend not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, central_tendency, axes = test.draw(self.x, legend=True, ax=axes)
            legend_texts = axes.get_legend()
            legend_text = legend_texts.get_texts()[0]
            text = legend_text.get_text()
            self.assertEqual(text, 'Non-parametric density', msg="default legend not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, central_tendency, axes = test.draw(self.x, legend=False, ax=axes)
            legend_texts = axes.get_legend()
            self.assertIsNone(legend_texts, msg="legend not None when NO legend was added")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, central_tendency, axes = test.draw(self.x, legend=False, which="mean", ax=axes)
            legend_texts = axes.get_legend()
            self.assertIsNone(legend_texts, msg="legend not None when NO legend was added")
            plt.close()


        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, central_tendency, axes = test.draw(self.x, legend=True, which="mean", ax=axes)
            legend_texts = axes.get_legend()
            legend_text = legend_texts.get_texts()[0]
            text = legend_text.get_text()
            self.assertEqual(text, 'Non-parametric density', msg="default legend not match")
            legend_text = legend_texts.get_texts()[1]
            text = legend_text.get_text()
            self.assertEqual(text, 'Mean', msg="default legend with mean do not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, central_tendency, axes = test.draw(self.x, legend=True, which="median", ax=axes)
            legend_texts = axes.get_legend()
            legend_text = legend_texts.get_texts()[0]
            text = legend_text.get_text()
            self.assertEqual(text, 'Non-parametric density', msg="default legend not match")
            legend_text = legend_texts.get_texts()[1]
            text = legend_text.get_text()
            self.assertEqual(text, 'Median', msg="default legend with median do not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, central_tendency, axes = test.draw(self.x, legend=True, which="mode", ax=axes)
            legend_texts = axes.get_legend()
            legend_text = legend_texts.get_texts()[0]
            text = legend_text.get_text()
            self.assertEqual(text, 'Non-parametric density', msg="default legend not match")
            legend_text = legend_texts.get_texts()[1]
            text = legend_text.get_text()
            self.assertEqual(text, 'Mode', msg="default legend with mode do not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, central_tendency, axes = test.draw(self.x, legend=True, which="all", ax=axes)
            legend_texts = axes.get_legend()
            legend_text = legend_texts.get_texts()[0]
            text = legend_text.get_text()
            self.assertEqual(text, 'Non-parametric density', msg="default legend not match")
            legend_text = legend_texts.get_texts()[1]
            text = legend_text.get_text()
            self.assertEqual(text, 'Mean', msg="default legend with mean do not match")
            legend_text = legend_texts.get_texts()[2]
            text = legend_text.get_text()
            self.assertEqual(text, 'Median', msg="default legend with median do not match")
            legend_text = legend_texts.get_texts()[3]
            text = legend_text.get_text()
            self.assertEqual(text, 'Mode', msg="default legend mode mode do not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, central_tendency, axes = test.draw(self.x, legend=False, which="all", ax=axes)
            legend_texts = axes.get_legend()
            self.assertIsNone(legend_texts, msg="legend not None when NO legend was added")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot(language='pt-br')
            fig, axes = plt.subplots()
            x, y, central_tendency, axes = test.draw(self.x, legend=True, which="mean", ax=axes)
            legend_texts = axes.get_legend()
            legend_text = legend_texts.get_texts()[0]
            text = legend_text.get_text()
            self.assertEqual(text, 'Densidade não paramétrica', msg="default legend do not match for pt-br")
            legend_text = legend_texts.get_texts()[1]
            text = legend_text.get_text()
            self.assertEqual(text, 'Média', msg="default legend with média do not match for pt-br")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot(language='pt-br')
            fig, axes = plt.subplots()
            x, y, central_tendency, axes = test.draw(self.x, legend=True, which="median", ax=axes)
            legend_texts = axes.get_legend()
            legend_text = legend_texts.get_texts()[0]
            text = legend_text.get_text()
            self.assertEqual(text, 'Densidade não paramétrica', msg="default legend do not match for pt-br")
            legend_text = legend_texts.get_texts()[1]
            text = legend_text.get_text()
            self.assertEqual(text, 'Mediana', msg="default legend with mediana do not match for pt-br")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot(language='pt-br')
            fig, axes = plt.subplots()
            x, y, central_tendency, axes = test.draw(self.x, legend=True, which="mode", ax=axes)
            legend_texts = axes.get_legend()
            legend_text = legend_texts.get_texts()[0]
            text = legend_text.get_text()
            self.assertEqual(text, 'Densidade não paramétrica', msg="default legend do not match for pt-br")
            legend_text = legend_texts.get_texts()[1]
            text = legend_text.get_text()
            self.assertEqual(text, 'Moda', msg="default legend with moda do not match for pt-br")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot(language='pt-br')
            fig, axes = plt.subplots()
            x, y, central_tendency, axes = test.draw(self.x, legend=True, which="all", ax=axes)
            legend_texts = axes.get_legend()
            legend_text = legend_texts.get_texts()[0]
            text = legend_text.get_text()
            self.assertEqual(text, 'Densidade não paramétrica', msg="default legend do not match for pt-br")
            legend_text = legend_texts.get_texts()[1]
            text = legend_text.get_text()
            self.assertEqual(text, 'Média', msg="default legend with Média do not match for pt-br")
            legend_text = legend_texts.get_texts()[2]
            text = legend_text.get_text()
            self.assertEqual(text, 'Mediana', msg="default legend with Mediana do not match for pt-br")
            legend_text = legend_texts.get_texts()[3]
            text = legend_text.get_text()
            self.assertEqual(text, 'Moda', msg="default legend Moda mode do not match for pt-br")
            plt.close()


    # decimal_separator=None
    def test_decimal_separator(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, central, axes = test.draw(self.x, ax=axes, decimal_separator=",")
            for text in axes.get_xticklabels():
                temp = text.get_text()
                result = False
                if ',' in temp:
                    result = True
            self.assertFalse(result, "Comma in x axis when it should not")
            plt.close()


        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, central, axes = test.draw(self.x, ax=axes, decimal_separator=".")
            result = False
            for text in axes.get_xticklabels():
                temp = text.get_text()
                if '' in temp: # needs to be empty dueto the plot was not drawn yet
                    result = True
            self.assertTrue(result, "No dot in x axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, central, axes = test.draw(self.x, ax=axes, decimal_separator=None)
            result = False
            for text in axes.get_xticklabels():
                temp = text.get_text()
                if '' in temp: # needs to be empty dueto the plot was not drawn yet
                    result = True
            self.assertTrue(result, "No dot in x axis")
            plt.close()


        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, central, axes = test.draw(self.x, ax=axes, decimal_separator=",")
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = False
                if ',' in temp:
                    result = True
            self.assertFalse(result, "Comma in y axis when it should not")
            plt.close()


        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, central, axes = test.draw(self.x, ax=axes, decimal_separator=".")
            result = False
            for text in axes.get_yticklabels():
                temp = text.get_text()
                if '' in temp: # needs to be empty dueto the plot was not drawn yet
                    result = True
            self.assertTrue(result, "No dot in y axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            fig, axes = plt.subplots()
            x, y, central, axes = test.draw(self.x, ax=axes, decimal_separator=None)
            result = False
            for text in axes.get_yticklabels():
                temp = text.get_text()
                if '' in temp: # needs to be empty dueto the plot was not drawn yet
                    result = True
            self.assertTrue(result, "No dot in y axis")
            plt.close()



class Test_None_test_draw(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9, 5.4, 4.8, 4.8, 4.3, 5.8, 5.7, 5.4, 5.1, 5.7,
                    5.1, 5.4, 5.1,4.6, 5.1, 4.8, 5.0, 5.0, 5.2, 5.2, 4.7, 4.8, 5.4, 5.2, 5.5, 4.9, 5.0, 5.5, 4.9, 4.4,
                    5.1, 5.0, 4.5, 4.4, 5.0, 5.1,4.8, 5.1, 4.6, 5.3, 5.0
                    ])
        cls.y = np.array([1,2,3,4,5,6,7,8,9])



    # ax=None,
    def test_basic_plot(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, central_tendency, axes = test.draw(self.x)
            result = isinstance(x, np.ndarray)
            self.assertTrue(result, "x is not a array")
            result = isinstance(y, np.ndarray)
            self.assertTrue(result, "y is not a array")
            result = isinstance(central_tendency, dict)
            self.assertTrue(result, "central_tendency is not a dict")
            result = isinstance(axes, matplotlib.axes.SubplotBase)
            self.assertTrue(result, "Ax not returned")

            self.assertAlmostEqual(x[5], 4.307507507507507, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(x[42], 4.363063063063063, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(x[71], 4.406606606606607, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(x[90], 4.435135135135135, msg="Something wrong with kde estimation")

            self.assertAlmostEqual(y[1], 0.23851082126842368, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(y[10], 0.25433748049114124, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(y[85], 0.3834491086323924, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(y[95], 0.39977420644640943, msg="Something wrong with kde estimation")

            self.assertEqual(len(central_tendency), 0, msg="Central tendency not empty for default parameters")
            plt.close()


    # bw_method=None,
    def test_bw_method(self):

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, central_tendency, axes = test.draw(self.x, bw_method=None)
            result = isinstance(x, np.ndarray)
            self.assertTrue(result, "x is not a array")
            result = isinstance(y, np.ndarray)
            self.assertTrue(result, "y is not a array")
            result = isinstance(central_tendency, dict)
            self.assertTrue(result, "central_tendency is not a dict")
            result = isinstance(axes, matplotlib.axes.SubplotBase)
            self.assertTrue(result, "Ax not returned")

            self.assertAlmostEqual(x[5], 4.307507507507507, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(y[5], 0.24553462195266776, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(x[42], 4.363063063063063, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(y[42], 0.3105878575930724, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(x[71], 4.406606606606607, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(y[71], 0.36020389827333554, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(x[90], 4.435135135135135, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(y[90], 0.39163910716800165, msg="Something wrong with kde estimation")
            self.assertEqual(len(central_tendency), 0, msg="Central tendency not empty for default parameters")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, central_tendency, axes = test.draw(self.x, bw_method="scott")
            result = isinstance(x, np.ndarray)
            self.assertTrue(result, "x is not a array")
            result = isinstance(y, np.ndarray)
            self.assertTrue(result, "y is not a array")
            result = isinstance(central_tendency, dict)
            self.assertTrue(result, "central_tendency is not a dict")
            result = isinstance(axes, matplotlib.axes.SubplotBase)
            self.assertTrue(result, "Ax not returned")

            self.assertAlmostEqual(x[5], 4.307507507507507, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(y[5], 0.24553462195266776, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(x[42], 4.363063063063063, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(y[42], 0.3105878575930724, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(x[71], 4.406606606606607, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(y[71], 0.36020389827333554, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(x[90], 4.435135135135135, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(y[90], 0.39163910716800165, msg="Something wrong with kde estimation")
            self.assertEqual(len(central_tendency), 0, msg="Central tendency not empty for default parameters")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, central_tendency, axes = test.draw(self.x, bw_method="silverman")
            result = isinstance(x, np.ndarray)
            self.assertTrue(result, "x is not a array")
            result = isinstance(y, np.ndarray)
            self.assertTrue(result, "y is not a array")
            result = isinstance(central_tendency, dict)
            self.assertTrue(result, "central_tendency is not a dict")
            result = isinstance(axes, matplotlib.axes.SubplotBase)
            self.assertTrue(result, "Ax not returned")

            self.assertAlmostEqual(x[5], 4.307507507507507, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(y[5], 0.24645513104212644, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(x[42], 4.363063063063063, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(y[42], 0.3097433651366933, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(x[71], 4.406606606606607, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(y[71], 0.3588525778348663, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(x[90], 4.435135135135135, msg="Something wrong with kde estimation")
            self.assertAlmostEqual(y[90], 0.39041165000025746, msg="Something wrong with kde estimation")
            self.assertEqual(len(central_tendency), 0, msg="Central tendency not empty for default parameters")
            plt.close()


    # bw_method=None,
    def test_bw_method_raises(self):
        with self.assertRaises(ValueError, msg="Does not raised error when bw_method not scott or silverman"):
            test = DensityPlot()
            x, y, axes = test.draw(self.x, bw_method="scot")
            plt.close()

        with self.assertRaises(ValueError, msg="Does not raised error when bw_method not scott or silverman"):
            test = DensityPlot()
            x, y, axes = test.draw(self.x, bw_method="scottt")
            plt.close()

        with self.assertRaises(ValueError, msg="Does not raised error when bw_method not scott or silverman"):
            test = DensityPlot()
            x, y, axes = test.draw(self.x, bw_method="silvermen")
            plt.close()

        with self.assertRaises(ValueError, msg="Does not raised error when bw_method not scott or silverman"):
            test = DensityPlot()
            x, y, axes = test.draw(self.x, bw_method="silvermann")
            plt.close()


    # bw_method=None,
    def test_bw_method_raises_output(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        test = DensityPlot()
        try:
            x, y, axes = test.draw(self.x, bw_method="scot")
        except:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'bw_method' parameter only accepts 'scott' or 'silverman' as key, but we got 'scot'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="Somethign wrong on the output when file already exists")


        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        test = DensityPlot(language='pt-br')
        try:
            x, y, axes = test.draw(self.x, bw_method="scottt")
        except:
            pass
        sys.stdout = sys.__stdout__
        expected = "O parâmetro 'bw_method' aceita apenas 'scott' ou 'silverman' como key, mas recebemos 'scottt'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="Somethign wrong on the output when file already exists")


        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        test = DensityPlot()
        try:
            x, y, axes = test.draw(self.x, bw_method="silvermen")
        except:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'bw_method' parameter only accepts 'scott' or 'silverman' as key, but we got 'silvermen'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="Somethign wrong on the output when file already exists")


        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        test = DensityPlot(language='pt-br')
        try:
            x, y, axes = test.draw(self.x, bw_method="silvermann")
        except:
            pass
        sys.stdout = sys.__stdout__
        expected = "O parâmetro 'bw_method' aceita apenas 'scott' ou 'silverman' como key, mas recebemos 'silvermann'"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="Somethign wrong on the output when file already exists")


    # which=None,
    def test_which(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, central_tendency, axes = test.draw(self.x, which=None)
            self.assertIsInstance(central_tendency, dict, msg="central_tendency is not a dict")
            self.assertEqual(len(central_tendency), 0, msg="central tendency not empty when it should")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, central_tendency, axes = test.draw(self.x, which='mean')
            self.assertEqual(central_tendency['mean'][0], 5.006, msg="wrong mean")
            self.assertEqual(central_tendency['mean'][1], 1.1185247245402423, msg="wrong kde for mean")
            mean = axes.get_children()[1]
            mean = mean.get_label()
            self.assertEqual(mean, "Mean")
            kde = axes.get_children()[2]
            kde = kde.get_label()
            self.assertEqual(kde, "Non-parametric density")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, central_tendency, axes = test.draw(self.x, which='median')
            self.assertEqual(central_tendency['median'][0], 5.0, msg="wrong median")
            self.assertEqual(central_tendency['median'][1], 1.117529174648972, msg="wrong kde for median")
            median = axes.get_children()[1]
            median = median.get_label()
            self.assertEqual(median, "Median")
            kde = axes.get_children()[2]
            kde = kde.get_label()
            self.assertEqual(kde, "Non-parametric density")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, central_tendency, axes = test.draw(self.x, which='mode')
            self.assertEqual(central_tendency['mode'][0][0], 5.1, msg="wrong mode")
            self.assertAlmostEqual(central_tendency['mode'][0][1], 1.058253577481665, msg="wrong kde for mode")
            self.assertEqual(central_tendency['mode'][1][0], 5.0, msg="wrong mode")
            self.assertAlmostEqual(central_tendency['mode'][1][1], 1.117529174648972, msg="wrong kde for mode")
            modes = axes.get_children()
            mode = modes[1].get_label()
            self.assertEqual(mode, "_collection1")
            mode = modes[2].get_label()
            self.assertEqual(mode, "Mode")
            mode = modes[3].get_label()
            self.assertEqual(mode, "Non-parametric density")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, central_tendency, axes = test.draw(self.x, which='all')
            self.assertEqual(central_tendency['mean'][0], 5.006, msg="wrong mean")
            self.assertAlmostEqual(central_tendency['mean'][1], 1.1185247245402423, msg="wrong kde for mean")
            self.assertEqual(central_tendency['median'][0], 5.0, msg="wrong median")
            self.assertAlmostEqual(central_tendency['median'][1], 1.117529174648972, msg="wrong kde for median")
            self.assertEqual(central_tendency['mode'][0][0], 5.1, msg="wrong mode")
            self.assertAlmostEqual(central_tendency['mode'][0][1], 1.058253577481665, msg="wrong kde for mode")
            self.assertEqual(central_tendency['mode'][1][0], 5.0, msg="wrong mode")
            self.assertAlmostEqual(central_tendency['mode'][1][1], 1.117529174648972, msg="wrong kde for mode")
            filhos = axes.get_children()
            mean = filhos[1].get_label()
            self.assertEqual(mean, "Mean")
            median = filhos[2].get_label()
            self.assertEqual(median, "Median")
            mode = filhos[3].get_label()
            self.assertEqual(mode, "_collection3")
            mode = filhos[4].get_label()
            self.assertEqual(mode, "Mode")
            kde = filhos[5].get_label()
            self.assertEqual(kde, "Non-parametric density")
            plt.close()


        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, central_tendency, axes = test.draw(self.x, which='mean,median')
            self.assertEqual(central_tendency['mean'][0], 5.006, msg="wrong mean")
            self.assertAlmostEqual(central_tendency['mean'][1], 1.1185247245402423, msg="wrong kde for mean")
            self.assertEqual(central_tendency['median'][0], 5.0, msg="wrong median")
            self.assertAlmostEqual(central_tendency['median'][1], 1.117529174648972, msg="wrong kde for median")
            filhos = axes.get_children()
            mean = filhos[1].get_label()
            self.assertEqual(mean, "Mean")
            median = filhos[2].get_label()
            self.assertEqual(median, "Median")
            kde = filhos[3].get_label()
            self.assertEqual(kde, "Non-parametric density")
            with self.assertRaises(KeyError, msg="Does not raised key error when mode is out of the plot"):
                result = central_tendency['mode'][0][0]
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, central_tendency, axes = test.draw(self.x, which='mean,mode')
            self.assertEqual(central_tendency['mean'][0], 5.006, msg="wrong mean")
            self.assertAlmostEqual(central_tendency['mean'][1], 1.1185247245402423, msg="wrong kde for mean")
            self.assertEqual(central_tendency['mode'][0][0], 5.1, msg="wrong mode")
            self.assertAlmostEqual(central_tendency['mode'][0][1], 1.058253577481665, msg="wrong kde for mode")
            self.assertEqual(central_tendency['mode'][1][0], 5.0, msg="wrong mode")
            self.assertAlmostEqual(central_tendency['mode'][1][1], 1.117529174648972, msg="wrong kde for mode")
            filhos = axes.get_children()
            mean = filhos[1].get_label()
            self.assertEqual(mean, "Mean")
            mode = filhos[2].get_label()
            self.assertEqual(mode, "_collection2")
            mode = filhos[3].get_label()
            self.assertEqual(mode, "Mode")
            kde = filhos[4].get_label()
            self.assertEqual(kde, "Non-parametric density")
            with self.assertRaises(KeyError, msg="Does not raised key error when median is out of the plot"):
                result = central_tendency['median'][0][0]
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, central_tendency, axes = test.draw(self.x, which='median,mode')
            self.assertEqual(central_tendency['median'][0], 5.0, msg="wrong median")
            self.assertAlmostEqual(central_tendency['median'][1], 1.117529174648972, msg="wrong kde for median")
            self.assertEqual(central_tendency['mode'][0][0], 5.1, msg="wrong mode")
            self.assertAlmostEqual(central_tendency['mode'][0][1], 1.058253577481665, msg="wrong kde for mode")
            self.assertEqual(central_tendency['mode'][1][0], 5.0, msg="wrong mode")
            self.assertAlmostEqual(central_tendency['mode'][1][1], 1.117529174648972, msg="wrong kde for mode")
            filhos = axes.get_children()
            median = filhos[1].get_label()
            self.assertEqual(median, "Median")
            mode = filhos[2].get_label()
            self.assertEqual(mode, "_collection2")
            mode = filhos[3].get_label()
            self.assertEqual(mode, "Mode")
            kde = filhos[4].get_label()
            self.assertEqual(kde, "Non-parametric density")
            with self.assertRaises(KeyError, msg="Does not raised key error when mean is out of the plot"):
                result = central_tendency['mean'][0][0]
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, central_tendency, axes = test.draw(self.y, which='all')
            self.assertEqual(central_tendency['mean'][0], 5.0, msg="wrong mean")
            self.assertAlmostEqual(central_tendency['mean'][1], 0.11002722425258299, msg="wrong kde for mean")
            self.assertEqual(central_tendency['median'][0], 5.0, msg="wrong median")
            self.assertAlmostEqual(central_tendency['median'][1], 0.11002722425258299, msg="wrong kde for median")
            filhos = axes.get_children()
            mean = filhos[1].get_label()
            self.assertEqual(mean, "Mean")
            median = filhos[2].get_label()
            self.assertEqual(median, "Median")
            kde = filhos[3].get_label()
            self.assertEqual(kde, "Non-parametric density")
            with self.assertRaises(KeyError, msg="Does not raised key error for mode when data does not have mode"):
                result = central_tendency['mode'][0][0]
            plt.close()


    # which=None,
    def test_which_raises(self): # teste redundante pois o which já é testado na sua própria função
        with self.assertRaises(ValueError, msg="Does not raised error when which not an option"):
            test = DensityPlot()
            x, y, axes = test.draw(self.x, which="None")
            plt.close()

        with self.assertRaises(ValueError, msg="Does not raised error when which not an option"):
            test = DensityPlot()
            x, y, axes = test.draw(self.x, which="media")
            plt.close()

        with self.assertRaises(ValueError, msg="Does not raised error when which not an option"):
            test = DensityPlot()
            x, y, axes = test.draw(self.x, which="maen")
            plt.close()

        with self.assertRaises(ValueError, msg="Does not raised error when which not an option"):
            test = DensityPlot()
            x, y, axes = test.draw(self.x, which="mediana")
            plt.close()

        with self.assertRaises(ValueError, msg="Does not raised error when which not an option"):
            test = DensityPlot()
            x, y, axes = test.draw(self.x, which="mediana")
            plt.close()

        with self.assertRaises(ValueError, msg="Does not raised error when which not an option"):
            test = DensityPlot()
            x, y, axes = test.draw(self.x, which="moda")
            plt.close()

        with self.assertRaises(ValueError, msg="Does not raised error when which not an option"):
            test = DensityPlot()
            x, y, axes = test.draw(self.x, which="mod")
            plt.close()

        with self.assertRaises(ValueError, msg="Does not raised error when which not an option"):
            test = DensityPlot()
            x, y, axes = test.draw(self.x, which="al")
            plt.close()

        with self.assertRaises(ValueError, msg="Does not raised error when which not an option"):
            test = DensityPlot()
            x, y, axes = test.draw(self.x, which="alll")
            plt.close()


    # x_label=None,
    def test_x_label(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x)
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "data", "x_label not empty")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, x_label="My data")
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "My data", "x_label not empty")
            plt.close()


    # y_label=None,
    def test_y_label(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x)
            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "y_label not a string")
            self.assertEqual(y_label, "Non-parametric density", "y_label not empty")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, y_label="My y label")
            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "y_label not a string")
            self.assertEqual(y_label, "My y label", "y_label not empty")
            plt.close()


    # width='default', height='default',
    def test_width_height(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x)
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertEqual(ax_h, 526.7222222222222, msg="wrong defalt height")
            self.assertEqual(ax_w, 1118.5972222222222, msg="wrong defalt width")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, width=5, height=5)
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 426.72222222222223, msg="wrong personalized height")
            self.assertAlmostEqual(ax_w, 418.59722222222223, msg="wrong personalized width")
            plt.close()


    # tight=None,
    def test_tight(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, tight=True)
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 526.7222222222222, msg="wrong defalt height")
            self.assertAlmostEqual(ax_w, 1118.5972222222222, msg="wrong defalt width")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, width=5, height=5, tight=True)
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 426.72222222222223, msg="wrong personalized height")
            self.assertAlmostEqual(ax_w, 418.59722222222223, msg="wrong personalized width")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, tight=False)
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 462.0, msg="wrong defalt height")
            self.assertAlmostEqual(ax_w, 930.0, msg="wrong defalt width")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, width=5, height=5, tight=False)
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 385.0, msg="wrong personalized height")
            self.assertAlmostEqual(ax_w, 387.5, msg="wrong personalized width")
            plt.close()


    # export=None, file_name=None, extension=None,
    def test_plot_export(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, ax=None, export=True)
            result = _check_file_exists("kernal_density.png")
            rem_file = Path("kernal_density.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'kernal_density.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, ax=None, export=True, file_name="teste")
            result = _check_file_exists("teste.png")
            rem_file = Path("teste.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'teste.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, ax=None, export=True, file_name="teste", extension='pdf')
            result = _check_file_exists("teste.pdf")
            rem_file = Path("teste.pdf")
            rem_file.unlink()
            self.assertTrue(result, "File 'teste.pdf' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, ax=None, export=False, file_name="teste", extension='pdf')
            result = _check_file_exists("teste.pdf")
            try:
                rem_file = Path("teste.pdf")
                rem_file.unlink()
            except:
                pass
            self.assertFalse(result, "File 'teste.pdf' was created even with export=False")
            plt.close()


    # export=None, file_name=None, extension=None,
    def test_plot_export_file_already_exists(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, ax=None, export=True)
            x, y, z, axes = test.draw(self.x, ax=None, export=True)
            result = _check_file_exists("kernal_density_1.png")
            rem_file = Path("kernal_density.png")
            rem_file.unlink()
            rem_file = Path("kernal_density_1.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'kernal_density_1.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, ax=None, export=True, file_name="bawtidaba")
            x, y, z, axes = test.draw(self.x, ax=None, export=True, file_name="bawtidaba")
            result = _check_file_exists("bawtidaba_1.png")
            rem_file = Path("bawtidaba.png")
            rem_file.unlink()
            rem_file = Path("bawtidaba_1.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'bawtidaba_1.png' was not created")
            plt.close()


    # dpi=None,
    def test_dpi(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, ax=None, export=True)
            image = Image.open("kernal_density.png")
            w, h = image.info["dpi"]
            image.close()
            self.assertAlmostEqual(w, 99.9998, msg="wrong defalt dpi")
            self.assertAlmostEqual(h, 99.9998, msg="wrong defalt dpi")
            rem_file = Path("kernal_density.png")
            rem_file.unlink()
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, ax=None, export=True, dpi=300)
            image = Image.open("kernal_density.png")
            w, h = image.info["dpi"]
            image.close()
            self.assertAlmostEqual(w, 299.9994, msg="wrong personalized dpi")
            self.assertAlmostEqual(h, 299.9994, msg="wrong personalized dpi")
            rem_file = Path("kernal_density.png")
            rem_file.unlink()
            plt.close()


    # plot_design='gray',
    def test_plot_design(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x)
            kde_line = axes.get_children()[1]
            self.assertEqual(kde_line.get_color(), "k", "default kde color not black")
            self.assertEqual(kde_line.get_lw(), 1.5, "default kde lw not 1.5")
            self.assertEqual(kde_line.get_ls(), '-', "default kde ls not '-'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, plot_design ='gray')
            kde_line = axes.get_children()[1]
            self.assertEqual(kde_line.get_color(), "k", "default kde color not black")
            self.assertEqual(kde_line.get_lw(), 1.5, "default kde lw not 1.5")
            self.assertEqual(kde_line.get_ls(), '-', "default kde ls not '-'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, plot_design ='gray', which="mean")
            kde_line = axes.get_children()[2]
            self.assertEqual(kde_line.get_color(), "k", "default kde color not black")
            self.assertEqual(kde_line.get_lw(), 1.5, "default kde lw not 1.5")
            self.assertEqual(kde_line.get_ls(), '-', "default kde ls not '-'")
            mean_line = axes.get_children()[1]
            self.assertEqual(round(mean_line.get_color()[0][0], 5), round(0.41176471, 5), "default mean color not dimgray")
            self.assertEqual(round(mean_line.get_color()[0][1], 5), round(0.41176471, 5), "default mean color not dimgray")
            self.assertEqual(round(mean_line.get_color()[0][2], 5), round(0.41176471, 5), "default mean color not dimgray")
            self.assertEqual(round(mean_line.get_color()[0][3], 1), round(1.0, 1), "default mean color not dimgray")
            self.assertEqual(mean_line.get_lw()[0], 1.5, "default mean lw not 1.5")
            self.assertEqual(mean_line.get_ls()[0][0], 0.0, "default mean ls not '--'")
            self.assertEqual(round(mean_line.get_ls()[0][1][0], 5), round(5.550000000000001, 5), "default mean ls not '--'")
            self.assertEqual(round(mean_line.get_ls()[0][1][1], 5), round(2.4000000000000004, 5), "default mean ls not '--'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, plot_design ='gray', which="median")
            kde_line = axes.get_children()[2]
            self.assertEqual(kde_line.get_color(), "k", "default kde color not black")
            self.assertEqual(kde_line.get_lw(), 1.5, "default kde lw not 1.5")
            self.assertEqual(kde_line.get_ls(), '-', "default kde ls not '-'")
            median_line = axes.get_children()[1]
            self.assertEqual(round(median_line.get_color()[0][0], 5), round(0.6627451, 5), "default median color not darkgray")
            self.assertEqual(round(median_line.get_color()[0][1], 5), round(0.6627451, 5), "default median color not darkgray")
            self.assertEqual(round(median_line.get_color()[0][2], 5), round(0.6627451, 5), "default median color not darkgray")
            self.assertEqual(round(median_line.get_color()[0][3], 1), round(1.0, 1), "default median color not darkgray")
            self.assertEqual(median_line.get_lw()[0], 1.5, "default median lw not 1.5")
            self.assertEqual(median_line.get_ls()[0][0], 0.0, "default median ls not '--'")
            self.assertEqual(round(median_line.get_ls()[0][1][0], 5), round(5.550000000000001, 5), "default median ls not '--'")
            self.assertEqual(round(median_line.get_ls()[0][1][1], 5), round(2.4000000000000004, 5), "default median ls not '--'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, plot_design ='gray', which="mode")
            kde_line = axes.get_children()[3]
            self.assertEqual(kde_line.get_color(), "k", "default kde color not black")
            self.assertEqual(kde_line.get_lw(), 1.5, "default kde lw not 1.5")
            self.assertEqual(kde_line.get_ls(), '-', "default kde ls not '-'")
            mode_line = axes.get_children()[1]
            self.assertEqual(round(mode_line.get_color()[0][0], 5), round(0.82745098, 5), "default mode color not lightgray")
            self.assertEqual(round(mode_line.get_color()[0][1], 5), round(0.82745098, 5), "default mode color not lightgray")
            self.assertEqual(round(mode_line.get_color()[0][2], 5), round(0.82745098, 5), "default mode color not lightgray")
            self.assertEqual(round(mode_line.get_color()[0][3], 1), round(1.0, 1), "default mode color not lightgray")
            self.assertEqual(mode_line.get_lw()[0], 1.5, "default mode lw not 1.5")
            self.assertEqual(mode_line.get_ls()[0][0], 0.0, "default mode ls not '--'")
            self.assertEqual(round(mode_line.get_ls()[0][1][0], 5), round(5.550000000000001, 5), "default mode ls not '--'")
            self.assertEqual(round(mode_line.get_ls()[0][1][1], 5), round(2.4000000000000004, 5), "default mode ls not '--'")
            mode_line = axes.get_children()[2]
            self.assertEqual(round(mode_line.get_color()[0][0], 5), round(0.82745098, 5), "default mode color not lightgray")
            self.assertEqual(round(mode_line.get_color()[0][1], 5), round(0.82745098, 5), "default mode color not lightgray")
            self.assertEqual(round(mode_line.get_color()[0][2], 5), round(0.82745098, 5), "default mode color not lightgray")
            self.assertEqual(round(mode_line.get_color()[0][3], 1), round(1.0, 1), "default mode color not lightgray")
            self.assertEqual(mode_line.get_lw()[0], 1.5, "default mode lw not 1.5")
            self.assertEqual(mode_line.get_ls()[0][0], 0.0, "default mode ls not '--'")
            self.assertEqual(round(mode_line.get_ls()[0][1][0], 5), round(5.550000000000001, 5), "default mode ls not '--'")
            self.assertEqual(round(mode_line.get_ls()[0][1][1], 5), round(2.4000000000000004, 5), "default mode ls not '--'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "kde": ['red', '-', 2.5],
                "Mean": ['white', ':', 1.0],
                "Median": ['orange', '-', 1.1],
                "Mode": ['yellow', '-', 1.1],
                "Area": ['lightgreen'],
            }
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, plot_design=plot_design, which="all")
            kde_line = axes.get_children()[5]
            self.assertEqual(kde_line.get_color(), "red", "personalized kde color not red")
            self.assertEqual(kde_line.get_lw(), 2.5, "personalized kde lw not 2.5")
            self.assertEqual(kde_line.get_ls(), '-', "personalized kde ls not '-'")
            mean_line = axes.get_children()[1]
            self.assertEqual(mean_line.get_color()[0][0], 1., "personalized mean color not white")
            self.assertEqual(mean_line.get_color()[0][1], 1., "personalized mean color not white")
            self.assertEqual(mean_line.get_color()[0][2], 1., "personalized mean color not white")
            self.assertEqual(mean_line.get_color()[0][3], 1., "personalized mean color not white")
            self.assertEqual(mean_line.get_lw()[0], 1.0, "personalized mean lw not 1.0")
            self.assertEqual(mean_line.get_ls()[0][0], 0.0, "personalized mean ls not ':'")
            self.assertEqual(mean_line.get_ls()[0][1][0], 1.0, "personalized mean ls not ':'")
            self.assertEqual(mean_line.get_ls()[0][1][1], 1.65, "personalized mean ls not ':'")
            median_line = axes.get_children()[2]
            self.assertEqual(median_line.get_color()[0][0], 1., "personalized median color not orange")
            self.assertEqual(round(median_line.get_color()[0][1], 5), round(0.64705882, 5), "personalized median color not orange")
            self.assertEqual(median_line.get_color()[0][2], 0., "personalized median color not orange")
            self.assertEqual(median_line.get_color()[0][3], 1., "personalized median color not orange")
            self.assertEqual(median_line.get_lw()[0], 1.1, "personalized median lw not 1.1")
            self.assertEqual(median_line.get_ls()[0][0], None, "personalized median ls not '-'")
            self.assertEqual(median_line.get_ls()[0][1], None, "personalized median ls not '-'")
            mode_line = axes.get_children()[3]
            self.assertEqual(mode_line.get_color()[0][0], 1., "personalized mode color not yellow")
            self.assertEqual(mode_line.get_color()[0][1], 1., "personalized mode color not yellow")
            self.assertEqual(mode_line.get_color()[0][2], 0., "personalized mode color not yellow")
            self.assertEqual(mode_line.get_color()[0][3], 1., "personalized mode color not yellow")
            self.assertEqual(mode_line.get_lw()[0], 1.1, "personalized mode lw not 1.1")
            self.assertEqual(mode_line.get_ls()[0][0], None, "personalized mode ls not '-'")
            self.assertEqual(mode_line.get_ls()[0][1], None, "personalized mode ls not '-'")
            mode_line = axes.get_children()[4]
            self.assertEqual(mode_line.get_color()[0][0], 1., "personalized mode color not yellow")
            self.assertEqual(mode_line.get_color()[0][1], 1., "personalized mode color not yellow")
            self.assertEqual(mode_line.get_color()[0][2], 0., "personalized mode color not yellow")
            self.assertEqual(mode_line.get_color()[0][3], 1., "personalized mode color not yellow")
            self.assertEqual(mode_line.get_lw()[0], 1.1, "personalized mode lw not 1.1")
            self.assertEqual(mode_line.get_ls()[0][0], None, "personalized mode ls not '-'")
            self.assertEqual(mode_line.get_ls()[0][1], None, "personalized mode ls not '-'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, plot_design ='gray')
            kde_line = axes.get_children()[1]
            self.assertEqual(kde_line.get_color(), "k", "default kde color not black")
            self.assertEqual(kde_line.get_lw(), 1.5, "default kde lw not 1.5")
            self.assertEqual(kde_line.get_ls(), '-', "default kde ls not '-'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, plot_design ='colored')
            kde_line = axes.get_children()[1]
            self.assertEqual(kde_line.get_color(), "k", "colored kde color not black")
            self.assertEqual(kde_line.get_lw(), 1.5, "colored kde lw not 1.5")
            self.assertEqual(kde_line.get_ls(), '-', "colored kde ls not '-'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, which="mean", plot_design='colored')
            kde_line = axes.get_children()[2]
            self.assertEqual(kde_line.get_color(), "k", "colored kde color not black")
            self.assertEqual(kde_line.get_lw(), 1.5, "colored kde lw not 1.5")
            self.assertEqual(kde_line.get_ls(), '-', "colored kde ls not '-'")
            mean_line = axes.get_children()[1]
            self.assertEqual(round(mean_line.get_color()[0][0], 1), round(1., 1), "colored mean color not red")
            self.assertEqual(round(mean_line.get_color()[0][1], 1), round(0.0, 1), "colored mean color not red")
            self.assertEqual(round(mean_line.get_color()[0][2], 1), round(0.0, 1), "colored mean color not red")
            self.assertEqual(round(mean_line.get_color()[0][3], 1), round(1.0, 1), "colored mean color not red")
            self.assertEqual(mean_line.get_lw()[0], 1.5, "colored mean lw not 1.5")
            self.assertEqual(mean_line.get_ls()[0][0], 0.0, "colored mean ls not '--'")
            self.assertEqual(round(mean_line.get_ls()[0][1][0], 5), round(5.550000000000001, 5), "colored mean ls not '--'")
            self.assertEqual(round(mean_line.get_ls()[0][1][1], 5), round(2.4000000000000004, 5), "colored mean ls not '--'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, plot_design ='colored', which="median")
            kde_line = axes.get_children()[2]
            self.assertEqual(kde_line.get_color(), "k", "colored kde color not black")
            self.assertEqual(kde_line.get_lw(), 1.5, "colored kde lw not 1.5")
            self.assertEqual(kde_line.get_ls(), '-', "colored kde ls not '-'")
            median_line = axes.get_children()[1]
            self.assertEqual(round(median_line.get_color()[0][0], 1), round(0.0, 1), "colored median color not blue")
            self.assertEqual(round(median_line.get_color()[0][1], 1), round(0.0, 1), "colored median color not blue")
            self.assertEqual(round(median_line.get_color()[0][2], 1), round(1.0, 1), "colored median color not blue")
            self.assertEqual(round(median_line.get_color()[0][3], 1), round(1.0, 1), "colored median color not darkgray")
            self.assertEqual(median_line.get_lw()[0], 1.5, "colored median lw not 1.5")
            self.assertEqual(median_line.get_ls()[0][0], 0.0, "colored median ls not '--'")
            self.assertEqual(round(median_line.get_ls()[0][1][0], 5), round(5.550000000000001, 5), "colored median ls not '--'")
            self.assertEqual(round(median_line.get_ls()[0][1][1], 5), round(2.4000000000000004, 5), "colored median ls not '--'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, plot_design ='colored', which="mode")
            kde_line = axes.get_children()[3]
            self.assertEqual(kde_line.get_color(), "k", "colored kde color not black")
            self.assertEqual(kde_line.get_lw(), 1.5, "colored kde lw not 1.5")
            self.assertEqual(kde_line.get_ls(), '-', "colored kde ls not '-'")
            mode_line = axes.get_children()[1]
            self.assertEqual(round(mode_line.get_color()[0][0], 1), round(0.0, 1), "colored mode color not green")
            self.assertEqual(round(mode_line.get_color()[0][1], 5), round(0.50196078, 5), "colored mode color not green")
            self.assertEqual(round(mode_line.get_color()[0][2], 1), round(0.0, 1), "colored mode color not green")
            self.assertEqual(round(mode_line.get_color()[0][3], 1), round(1.0, 1), "colored mode color not green")
            self.assertEqual(mode_line.get_lw()[0], 1.5, "colored mode lw not 1.5")
            self.assertEqual(mode_line.get_ls()[0][0], 0.0, "colored mode ls not '--'")
            self.assertEqual(round(mode_line.get_ls()[0][1][0], 5), round(5.550000000000001, 5), "colored mode ls not '--'")
            self.assertEqual(round(mode_line.get_ls()[0][1][1], 5), round(2.4000000000000004, 5), "colored mode ls not '--'")
            mode_line = axes.get_children()[2]
            self.assertEqual(round(mode_line.get_color()[0][0], 1), round(0.0, 1), "colored mode color not green")
            self.assertEqual(round(mode_line.get_color()[0][1], 5), round(0.50196078, 5), "colored mode color not green")
            self.assertEqual(round(mode_line.get_color()[0][2], 1), round(0.0, 1), "colored mode color not green")
            self.assertEqual(round(mode_line.get_color()[0][3], 1), round(1.0, 1), "colored mode color not green")
            self.assertEqual(mode_line.get_lw()[0], 1.5, "colored mode lw not 1.5")
            self.assertEqual(mode_line.get_ls()[0][0], 0.0, "colored mode ls not '--'")
            self.assertEqual(round(mode_line.get_ls()[0][1][0], 5), round(5.550000000000001, 5), "colored mode ls not '--'")
            self.assertEqual(round(mode_line.get_ls()[0][1][1], 5), round(2.4000000000000004, 5), "colored mode ls not '--'")
            plt.close()


    # legend=None,
    def test_legend(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, central_tendency, axes = test.draw(self.x)
            legends = axes.get_legend_handles_labels()
            self.assertEqual(legends[-1][0], 'Non-parametric density', msg="default legend not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, central_tendency, axes = test.draw(self.x, legend=True)
            legends = axes.get_legend_handles_labels()
            self.assertEqual(legends[-1][0], 'Non-parametric density', msg="default legend not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, central_tendency, axes = test.draw(self.x)
            legend_texts = axes.get_legend()
            legend_text = legend_texts.get_texts()[0]
            text = legend_text.get_text()
            self.assertEqual(text, 'Non-parametric density', msg="default legend not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, central_tendency, axes = test.draw(self.x, legend=True)
            legend_texts = axes.get_legend()
            legend_text = legend_texts.get_texts()[0]
            text = legend_text.get_text()
            self.assertEqual(text, 'Non-parametric density', msg="default legend not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, central_tendency, axes = test.draw(self.x, legend=False)
            legend_texts = axes.get_legend()
            self.assertIsNone(legend_texts, msg="legend not None when NO legend was added")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, central_tendency, axes = test.draw(self.x, legend=False, which="mean")
            legend_texts = axes.get_legend()
            self.assertIsNone(legend_texts, msg="legend not None when NO legend was added")
            plt.close()


        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, central_tendency, axes = test.draw(self.x, legend=True, which="mean")
            legend_texts = axes.get_legend()
            legend_text = legend_texts.get_texts()[0]
            text = legend_text.get_text()
            self.assertEqual(text, 'Non-parametric density', msg="default legend not match")
            legend_text = legend_texts.get_texts()[1]
            text = legend_text.get_text()
            self.assertEqual(text, 'Mean', msg="default legend with mean do not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, central_tendency, axes = test.draw(self.x, legend=True, which="median")
            legend_texts = axes.get_legend()
            legend_text = legend_texts.get_texts()[0]
            text = legend_text.get_text()
            self.assertEqual(text, 'Non-parametric density', msg="default legend not match")
            legend_text = legend_texts.get_texts()[1]
            text = legend_text.get_text()
            self.assertEqual(text, 'Median', msg="default legend with median do not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, central_tendency, axes = test.draw(self.x, legend=True, which="mode")
            legend_texts = axes.get_legend()
            legend_text = legend_texts.get_texts()[0]
            text = legend_text.get_text()
            self.assertEqual(text, 'Non-parametric density', msg="default legend not match")
            legend_text = legend_texts.get_texts()[1]
            text = legend_text.get_text()
            self.assertEqual(text, 'Mode', msg="default legend with mode do not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, central_tendency, axes = test.draw(self.x, legend=True, which="all")
            legend_texts = axes.get_legend()
            legend_text = legend_texts.get_texts()[0]
            text = legend_text.get_text()
            self.assertEqual(text, 'Non-parametric density', msg="default legend not match")
            legend_text = legend_texts.get_texts()[1]
            text = legend_text.get_text()
            self.assertEqual(text, 'Mean', msg="default legend with mean do not match")
            legend_text = legend_texts.get_texts()[2]
            text = legend_text.get_text()
            self.assertEqual(text, 'Median', msg="default legend with median do not match")
            legend_text = legend_texts.get_texts()[3]
            text = legend_text.get_text()
            self.assertEqual(text, 'Mode', msg="default legend mode mode do not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, central_tendency, axes = test.draw(self.x, legend=False, which="all")
            legend_texts = axes.get_legend()
            self.assertIsNone(legend_texts, msg="legend not None when NO legend was added")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot(language='pt-br')
            x, y, central_tendency, axes = test.draw(self.x, legend=True, which="mean")
            legend_texts = axes.get_legend()
            legend_text = legend_texts.get_texts()[0]
            text = legend_text.get_text()
            self.assertEqual(text, 'Densidade não paramétrica', msg="default legend do not match for pt-br")
            legend_text = legend_texts.get_texts()[1]
            text = legend_text.get_text()
            self.assertEqual(text, 'Média', msg="default legend with média do not match for pt-br")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot(language='pt-br')
            x, y, central_tendency, axes = test.draw(self.x, legend=True, which="median")
            legend_texts = axes.get_legend()
            legend_text = legend_texts.get_texts()[0]
            text = legend_text.get_text()
            self.assertEqual(text, 'Densidade não paramétrica', msg="default legend do not match for pt-br")
            legend_text = legend_texts.get_texts()[1]
            text = legend_text.get_text()
            self.assertEqual(text, 'Mediana', msg="default legend with mediana do not match for pt-br")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot(language='pt-br')
            x, y, central_tendency, axes = test.draw(self.x, legend=True, which="mode")
            legend_texts = axes.get_legend()
            legend_text = legend_texts.get_texts()[0]
            text = legend_text.get_text()
            self.assertEqual(text, 'Densidade não paramétrica', msg="default legend do not match for pt-br")
            legend_text = legend_texts.get_texts()[1]
            text = legend_text.get_text()
            self.assertEqual(text, 'Moda', msg="default legend with moda do not match for pt-br")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot(language='pt-br')
            x, y, central_tendency, axes = test.draw(self.x, legend=True, which="all")
            legend_texts = axes.get_legend()
            legend_text = legend_texts.get_texts()[0]
            text = legend_text.get_text()
            self.assertEqual(text, 'Densidade não paramétrica', msg="default legend do not match for pt-br")
            legend_text = legend_texts.get_texts()[1]
            text = legend_text.get_text()
            self.assertEqual(text, 'Média', msg="default legend with Média do not match for pt-br")
            legend_text = legend_texts.get_texts()[2]
            text = legend_text.get_text()
            self.assertEqual(text, 'Mediana', msg="default legend with Mediana do not match for pt-br")
            legend_text = legend_texts.get_texts()[3]
            text = legend_text.get_text()
            self.assertEqual(text, 'Moda', msg="default legend Moda mode do not match for pt-br")
            plt.close()


    # decimal_separator=None
    def test_decimal_separator(self):
        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, decimal_separator=",")
            for text in axes.get_xticklabels():
                temp = text.get_text()
                result = False
                if ',' in temp:
                    result = True
            self.assertTrue(result, "No comma in x axis")
            plt.close()


        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, decimal_separator=".")
            for text in axes.get_xticklabels():
                temp = text.get_text()
                result = True
                if ',' in temp:
                    result = False
            self.assertTrue(result, "No dot in x axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, decimal_separator=None)
            for text in axes.get_xticklabels():
                temp = text.get_text()
                result = True
                if ',' in temp:
                    result = False
            self.assertTrue(result, "No dot in x axis")
            plt.close()


        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, decimal_separator=",")
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = False
                if ',' in temp:
                    result = True
            self.assertTrue(result, "No comma in y axis")
            plt.close()


        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, decimal_separator=".")
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = True
                if ',' in temp:
                    result = False
            self.assertTrue(result, "No dot in y axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = DensityPlot()
            x, y, z, axes = test.draw(self.x, decimal_separator=None)
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = True
                if ',' in temp:
                    result = False
            self.assertTrue(result, "No dot in y axis")
            plt.close()

















if __name__ == "__main__":
    unittest.main()
