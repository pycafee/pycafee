"""Tests if the test_draw is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_Raises. This class checks if the function raises error when the which parameter is wrong, when the interval is wrong and checks the warning when interval[0] = -1*interval[1].

---> Class Test_None_test_draw. This class checks if the axes is returned, if the file is export when export = True and when extension = 'pdf' and if the file is not exported when export = True. The decimal_separator is also tested fot ".", "," and None. There is 4 of this class, each with a distinct dataset

---> Class Test_axestest_draw. This class checks if the axes is returned when ax is a previuous created ax. It also looks for a saved file if export=Tru, if legend was created or not, if it has x_label, some test about width and height, some test about dpi, some test about almost everything

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sample/StudentDistribution/test_draw.py
    or
    python -m unittest -b tests/sample/StudentDistribution/test_draw.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from unittest.mock import patch
from pycafee.sample.studentdistribution import StudentDistribution
from pycafee.utils.helpers import _check_file_exists
import numpy as np
import matplotlib.axes
import matplotlib.pyplot as plt
from pathlib import Path
from PIL import Image
os.system('cls')


class Test_Raises(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gl = 5
        cls.tcalc = 4

    def test_which(self):
        with self.assertRaises(ValueError, msg="Does not raised error when which not two-side or one-side"):
            student = StudentDistribution()
            student.draw(self.gl, self.tcalc, which="bilate")

        with self.assertRaises(ValueError, msg="Does not raised error when which not two-side or one-side"):
            student = StudentDistribution()
            student.draw(self.gl, self.tcalc, which="bil")

        with self.assertRaises(ValueError, msg="Does not raised error when which not two-side or one-side"):
            student = StudentDistribution(language='pt-br')
            student.draw(self.gl, self.tcalc, which="uni")

    def test_interval_one_side(self):
        with self.assertRaises(ValueError, msg="Does not raised error when interval is wrong"):
            student = StudentDistribution()
            student.draw(self.gl, self.tcalc, interval=2, which='one-side')

        with self.assertRaises(ValueError, msg="Does not raised error when interval is wrong"):
            student = StudentDistribution()
            student.draw(self.gl, self.tcalc, interval="2", which='one-side')

        with self.assertRaises(ValueError, msg="Does not raised error when interval is wrong"):
            student = StudentDistribution()
            student.draw(self.gl, self.tcalc, interval="21", which='one-side')

        with self.assertRaises(ValueError, msg="Does not raised error when interval is wrong"):
            student = StudentDistribution()
            student.draw(self.gl, self.tcalc, interval=[2], which='one-side')

        with self.assertRaises(ValueError, msg="Does not raised error when interval is wrong"):
            student = StudentDistribution()
            student.draw(self.gl, self.tcalc, interval=[2,2,2], which='one-side')

        with self.assertRaises(ValueError, msg="Does not raised error when interval is wrong"):
            student = StudentDistribution()
            student.draw(self.gl, self.tcalc, interval=[], which='one-side')

        with self.assertRaises(ValueError, msg="Does not raised error when interval is wrong"):
            student = StudentDistribution()
            student.draw(self.gl, self.tcalc, interval=["2", 2], which='one-side')

        with self.assertRaises(ValueError, msg="Does not raised error when interval is wrong"):
            student = StudentDistribution()
            student.draw(self.gl, self.tcalc, interval=["2", "4"], which='one-side')

        with self.assertRaises(ValueError, msg="Does not raised error when interval is wrong"):
            student = StudentDistribution()
            student.draw(self.gl, self.tcalc, interval=[2, "4"], which='one-side')

        with self.assertRaises(ValueError, msg="Does not raised error when interval is wrong"):
            student = StudentDistribution()
            student.draw(self.gl, self.tcalc, interval=[-2, -4], which='one-side')

        with self.assertRaises(ValueError, msg="Does not raised error when interval is wrong"):
            student = StudentDistribution()
            student.draw(self.gl, self.tcalc, interval=[2, 1], which='one-side')

        with self.assertRaises(ValueError, msg="Does not raised error when interval is wrong"):
            student = StudentDistribution()
            student.draw(self.gl, self.tcalc, interval=[2, 2], which='one-side')

    def test_interval_two_side(self):
        with self.assertRaises(ValueError, msg="Does not raised error when interval is wrong"):
            student = StudentDistribution()
            student.draw(self.gl, self.tcalc, interval=2)

        with self.assertRaises(ValueError, msg="Does not raised error when interval is wrong"):
            student = StudentDistribution()
            student.draw(self.gl, self.tcalc, interval="2")

        with self.assertRaises(ValueError, msg="Does not raised error when interval is wrong"):
            student = StudentDistribution()
            student.draw(self.gl, self.tcalc, interval="21")

        with self.assertRaises(ValueError, msg="Does not raised error when interval is wrong"):
            student = StudentDistribution()
            student.draw(self.gl, self.tcalc, interval=[2])

        with self.assertRaises(ValueError, msg="Does not raised error when interval is wrong"):
            student = StudentDistribution()
            student.draw(self.gl, self.tcalc, interval=[2,2,2])

        with self.assertRaises(ValueError, msg="Does not raised error when interval is wrong"):
            student = StudentDistribution()
            student.draw(self.gl, self.tcalc, interval=[])

        with self.assertRaises(ValueError, msg="Does not raised error when interval is wrong"):
            student = StudentDistribution()
            student.draw(self.gl, self.tcalc, interval=["2", 2])

        with self.assertRaises(ValueError, msg="Does not raised error when interval is wrong"):
            student = StudentDistribution()
            student.draw(self.gl, self.tcalc, interval=["2", "4"])

        with self.assertRaises(ValueError, msg="Does not raised error when interval is wrong"):
            student = StudentDistribution()
            student.draw(self.gl, self.tcalc, interval=[2, "4"])

        with self.assertRaises(ValueError, msg="Does not raised error when interval is wrong"):
            student = StudentDistribution()
            student.draw(self.gl, self.tcalc, interval=[-2, -4])

        with self.assertRaises(ValueError, msg="Does not raised error when interval is wrong"):
            student = StudentDistribution()
            student.draw(self.gl, self.tcalc, interval=[2, 1])

        with self.assertRaises(ValueError, msg="Does not raised error when interval is wrong"):
            student = StudentDistribution()
            student.draw(self.gl, self.tcalc, interval=[2, 2])

    @patch('builtins.print')
    def test_warns(self, mock_print):
        with patch('matplotlib.pyplot.show') as p:
            student = StudentDistribution()
            student.draw(self.gl, self.tcalc, interval=[-4, 3])
            mock_print.assert_called_with("\x1b[0m")



class Test_None_test_draw(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gl = 5
        cls.tcalc = 4

    def test_which_none(self):

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which=None)
            result = isinstance(output, dict)
            self.assertTrue(result, "output is not a dict")
            result = isinstance(axes, matplotlib.axes.SubplotBase)
            self.assertTrue(result, "Ax not returned")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc)
            expected = ['curve', 'tcalc', 't_left', 't_right']
            for key, values in zip(output.keys(), expected):
                self.assertEqual(key, values, msg="wrong dict key")

            self.assertEqual(output['tcalc'][0], 4, msg="wrong tcalc returned")
            self.assertAlmostEqual(output['tcalc'][1], 0.005123727051, msg="wrong teoretical value for tcalc  returned")

            self.assertAlmostEqual(output['t_left'][0], -2.57058183661474, msg="wrong t_left returned")
            self.assertAlmostEqual(output['t_left'][1], 0.030337787761265618, msg="wrong teoretical value for t_left  returned")

            self.assertAlmostEqual(output['t_right'][0], 2.57058183661474, msg="wrong t_right returned")
            self.assertAlmostEqual(output['t_right'][1], 0.030337787761265618, msg="wrong teoretical value for t_right  returned")

            self.assertAlmostEqual(output['t_right'][1], output['t_left'][1], msg="teoretical value for t_right and t_left does not match")
            self.assertAlmostEqual(output['t_right'][0], -1*output['t_left'][0], msg="t value for t_right and t_left does not match")

            labels = axes.get_children()
            expected = ["$t_{calc} = $4", "Rejection region", "_collection2", "_collection3", "$gl=5$"]
            for label, correct in zip(labels, expected):
                self.assertEqual(label.get_label(), correct, msg="label does not match")

            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "Student's $t$", "something wrong with x_label")

            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Probability density", "something wrong with y_label")

            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

    def test_which_two_side(self):

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which="two-side")
            result = isinstance(output, dict)
            self.assertTrue(result, "output is not a dict")
            result = isinstance(axes, matplotlib.axes.SubplotBase)
            self.assertTrue(result, "Ax not returned")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which="two-side")
            expected = ['curve', 'tcalc', 't_left', 't_right']
            for key, values in zip(output.keys(), expected):
                self.assertEqual(key, values, msg="wrong dict key")

            self.assertEqual(output['tcalc'][0], 4, msg="wrong tcalc returned")
            self.assertAlmostEqual(output['tcalc'][1], 0.005123727051, msg="wrong teoretical value for tcalc  returned")

            self.assertAlmostEqual(output['t_left'][0], -2.57058183661474, msg="wrong t_left returned")
            self.assertAlmostEqual(output['t_left'][1], 0.030337787761265618, msg="wrong teoretical value for t_left  returned")

            self.assertAlmostEqual(output['t_right'][0], 2.57058183661474, msg="wrong t_right returned")
            self.assertAlmostEqual(output['t_right'][1], 0.030337787761265618, msg="wrong teoretical value for t_right  returned")

            self.assertAlmostEqual(output['t_right'][1], output['t_left'][1], msg="teoretical value for t_right and t_left does not match")
            self.assertAlmostEqual(output['t_right'][0], -1*output['t_left'][0], msg="t value for t_right and t_left does not match")

            labels = axes.get_children()
            expected = ["$t_{calc} = $4", "Rejection region", "_collection2", "_collection3", "$gl=5$"]
            for label, correct in zip(labels, expected):
                self.assertEqual(label.get_label(), correct, msg="label does not match")

            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "Student's $t$", "something wrong with x_label")

            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Probability density", "something wrong with y_label")

            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

    def test_calc(self):

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output_one_side = test.draw(self.gl, self.tcalc, which="one-side")
            test = StudentDistribution()
            axes, output_two_side = test.draw(self.gl, self.tcalc, which="two-side")

            self.assertEqual(output_two_side['tcalc'][0], output_one_side['tcalc'][0], msg='tcalc does not match')
            self.assertEqual(output_two_side['tcalc'][1], output_one_side['tcalc'][1], msg='y tcalc does not match')
            plt.close()

    def test_which_one_side(self):

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which="one-side")
            result = isinstance(output, dict)
            self.assertTrue(result, "output is not a dict")
            result = isinstance(axes, matplotlib.axes.SubplotBase)
            self.assertTrue(result, "Ax not returned")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which="one-side")
            expected = ['curve', 'tcalc', 't_student']
            for key, values in zip(output.keys(), expected):
                self.assertEqual(key, values, msg="wrong dict key")

            self.assertEqual(output['tcalc'][0], 4, msg="wrong tcalc returned")
            self.assertAlmostEqual(output['tcalc'][1], 0.005123727051, msg="wrong teoretical value for tcalc  returned")

            self.assertAlmostEqual(output['t_student'][0], 2.015048372669157, msg="wrong t_student returned")
            self.assertAlmostEqual(output['t_student'][1], 0.06379679895149033, msg="wrong teoretical value for t_student  returned")

            labels = axes.get_children()
            expected = ["$t_{calc} = $4", "Rejection region", "_collection2", "$gl=5$"]
            for label, correct in zip(labels, expected):
                self.assertEqual(label.get_label(), correct, msg="label does not match")

            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "Student's $t$", "something wrong with x_label")

            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Probability density", "something wrong with y_label")

            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[2]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[3]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

    def test_x_label(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc)
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "Student's $t$", "something wrong with x_label")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution(language='pt-br')
            axes, output = test.draw(self.gl, self.tcalc)
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "$t$ de Student", "something wrong with x_label when language='pt-br'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, x_label="my data")
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "my data", "something wrong when changing x_label")
            plt.close()


        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "Student's $t$", "something wrong with x_label")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution(language='pt-br')
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "$t$ de Student", "something wrong with x_label when language='pt-br'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, x_label="my data", which='one-side')
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "my data", "something wrong when changing x_label")
            plt.close()

    def test_y_label(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc)
            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Probability density", "something wrong with y_label")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution(language='pt-br')
            axes, output = test.draw(self.gl, self.tcalc)
            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Densidade de probabilidade", "something wrong with x_label when language='pt-br'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, y_label="my data")
            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "xlabel not a string")
            self.assertEqual(y_label, "my data", "something wrong when changing y_label")
            plt.close()


        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Probability density", "something wrong with y_label")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution(language='pt-br')
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Densidade de probabilidade", "something wrong with x_label when language='pt-br'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, y_label="my data", which='one-side')
            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "xlabel not a string")
            self.assertEqual(y_label, "my data", "something wrong when changing y_label")
            plt.close()

    def test_width_height(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc)
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 525.7222222222223, msg="wrong defalt height")
            self.assertAlmostEqual(ax_w, 1109.7222222222222, msg="wrong defalt width")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, width=5, height=5)
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 425.72222222222223, msg="wrong personalized height")
            self.assertAlmostEqual(ax_w, 409.72222222222223, msg="wrong personalized width")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 525.7222222222223, msg="wrong defalt height")
            self.assertAlmostEqual(ax_w, 1109.7222222222222, msg="wrong defalt width")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, width=5, height=5, which='one-side')
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 425.72222222222223, msg="wrong personalized height")
            self.assertAlmostEqual(ax_w, 409.72222222222223, msg="wrong personalized width")
            plt.close()

    def test_plot_export(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True)
            result = _check_file_exists("student_distribution.png")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'student_distribution.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="teste")
            result = _check_file_exists("teste.png")
            rem_file = Path("teste.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'teste.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="teste", extension='pdf')
            result = _check_file_exists("teste.pdf")
            rem_file = Path("teste.pdf")
            rem_file.unlink()
            self.assertTrue(result, "File 'teste.pdf' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=False, file_name="teste", extension='pdf')
            result = _check_file_exists("teste.pdf")
            try:
                rem_file = Path("teste.pdf")
                rem_file.unlink()
            except:
                pass
            self.assertFalse(result, "File 'teste.pdf' was created even with export=False")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, which='one-side')
            result = _check_file_exists("student_distribution.png")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'student_distribution.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="teste", which='one-side')
            result = _check_file_exists("teste.png")
            rem_file = Path("teste.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'teste.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="teste", extension='pdf', which='one-side')
            result = _check_file_exists("teste.pdf")
            rem_file = Path("teste.pdf")
            rem_file.unlink()
            self.assertTrue(result, "File 'teste.pdf' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=False, file_name="teste", extension='pdf', which='one-side')
            result = _check_file_exists("teste.pdf")
            try:
                rem_file = Path("teste.pdf")
                rem_file.unlink()
            except:
                pass
            self.assertFalse(result, "File 'teste.pdf' was created even with export=False")
            plt.close()

    def test_plot_export_file_already_exists(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True)
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True)
            result = _check_file_exists("student_distribution_1.png")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            rem_file = Path("student_distribution_1.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'student_distribution_1.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="bawtidaba")
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="bawtidaba")
            result = _check_file_exists("bawtidaba_1.png")
            rem_file = Path("bawtidaba.png")
            rem_file.unlink()
            rem_file = Path("bawtidaba_1.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'bawtidaba_1.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, which='one-side')
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, which='one-side')
            result = _check_file_exists("student_distribution_1.png")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            rem_file = Path("student_distribution_1.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'student_distribution_1.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="bawtidaba", which='one-side')
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="bawtidaba", which='one-side')
            result = _check_file_exists("bawtidaba_1.png")
            rem_file = Path("bawtidaba.png")
            rem_file.unlink()
            rem_file = Path("bawtidaba_1.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'bawtidaba_1.png' was not created")
            plt.close()

    def test_dpi(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True)
            image = Image.open("student_distribution.png")
            w, h = image.info["dpi"]
            image.close()
            self.assertEqual(w, 99.9998, "wrong defalt dpi")
            self.assertEqual(h, 99.9998, "wrong defalt dpi")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, dpi=300)
            image = Image.open("student_distribution.png")
            w, h = image.info["dpi"]
            image.close()
            self.assertEqual(w, 299.9994, "wrong personalized dpi")
            self.assertEqual(h, 299.9994, "wrong personalized dpi")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            plt.close()


        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, which='one-side')
            image = Image.open("student_distribution.png")
            w, h = image.info["dpi"]
            image.close()
            self.assertEqual(w, 99.9998, "wrong defalt dpi")
            self.assertEqual(h, 99.9998, "wrong defalt dpi")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, dpi=300, which='one-side')
            image = Image.open("student_distribution.png")
            w, h = image.info["dpi"]
            image.close()
            self.assertEqual(w, 299.9994, "wrong personalized dpi")
            self.assertEqual(h, 299.9994, "wrong personalized dpi")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            plt.close()

    def test_decimal_separator(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, decimal_separator=",")
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = False
                if ',' in temp:
                    result = True
            self.assertTrue(result, "No comma in y axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, decimal_separator=".")
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = True
                if ',' in temp:
                    result = False
            self.assertTrue(result, "No dot in y axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, decimal_separator=None)
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = True
                if ',' in temp:
                    result = False
            self.assertTrue(result, "No dot in y axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, decimal_separator=",", which='one-side')
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = False
                if ',' in temp:
                    result = True
            self.assertTrue(result, "No comma in y axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, decimal_separator=".", which='one-side')
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = True
                if ',' in temp:
                    result = False
            self.assertTrue(result, "No dot in y axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, decimal_separator=None, which='one-side')
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = True
                if ',' in temp:
                    result = False
            self.assertTrue(result, "No dot in y axis")
            plt.close()

    def test_legend(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc,)
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $4", "Rejection region",]
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution(language='pt-br')
            axes, output = test.draw(self.gl, self.tcalc,)
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $4", "Região de rejeição",]
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, legend=True)
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $4", "Rejection region",]
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, legend=False)
            legend_texts = axes.get_legend()
            self.assertIsNone(legend_texts, msg="legend not None when NO legend was added")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['k', '-', 1.5],
                "area-rejection": ['gainsboro'],
                "area-acceptance": ['black'],
                "tcalc": ['k', 'o', 50],
            }
            axes, output = test.draw(self.gl, self.tcalc, legend=True, plot_design=plot_design)
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $4", "Rejection region", 'Acceptance region']
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['k', '-', 1.5],
                "area-rejection": ['gainsboro'],
                "area-acceptance": ['black'],
                "tcalc": ['k', 'o', 50],
            }
            axes, output = test.draw(self.gl, self.tcalc, legend=False, plot_design=plot_design)
            legends = axes.get_legend_handles_labels()
            legend_texts = axes.get_legend()
            self.assertIsNone(legend_texts, msg="legend not None when NO legend was added")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $4", "Rejection region",]
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution(language='pt-br')
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $4", "Região de rejeição",]
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, legend=True, which='one-side')
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $4", "Rejection region",]
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, legend=False, which='one-side')
            legend_texts = axes.get_legend()
            self.assertIsNone(legend_texts, msg="legend not None when NO legend was added")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['k', '-', 1.5],
                "area-rejection": ['gainsboro'],
                "area-acceptance": ['black'],
                "tcalc": ['k', 'o', 50],
            }
            axes, output = test.draw(self.gl, self.tcalc, legend=True, plot_design=plot_design, which='one-side')
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $4", "Rejection region", 'Acceptance region']
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['k', '-', 1.5],
                "area-rejection": ['gainsboro'],
                "area-acceptance": ['black'],
                "tcalc": ['k', 'o', 50],
            }
            axes, output = test.draw(self.gl, self.tcalc, legend=False, plot_design=plot_design, which='one-side')
            legends = axes.get_legend_handles_labels()
            legend_texts = axes.get_legend()
            self.assertIsNone(legend_texts, msg="legend not None when NO legend was added")
            plt.close()

    def test_plot_design(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc)
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, plot_design ='gray')
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['red', '-', 1.5],
                "area-rejection": ['lightgray'],
                "area-acceptance": ['white'],
                "tcalc": ['red', 'o', 50],
            }
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, plot_design=plot_design)
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [1., 0., 0., 1.], "personalized t_calc color not red")
            rejection = axes.get_children()[1]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "r", "default plot_line color not black")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['b', '-', 1.5],
                "area-rejection": ['lightgray'],
                "area-acceptance": ['silver'],
                "tcalc": ['red', 'o', 50],
            }
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, plot_design=plot_design)
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [1., 0., 0., 1.], "personalized t_calc color not red")
            rejection = axes.get_children()[1]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            accepted = axes.get_children()[3]
            expected = [0.7529411764705882, 0.7529411764705882, 0.7529411764705882, 1.0]
            for item, value in zip(list(accepted.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="accepted color not silver")
            h_line = axes.get_children()[4]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[5]
            self.assertEqual(plot_line.get_color()[0], "b", "default plot_line color not black")
            plt.close()


        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[2]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[3]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, plot_design ='gray', which='one-side')
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[2]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[3]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['red', '-', 1.5],
                "area-rejection": ['lightgray'],
                "area-acceptance": ['white'],
                "tcalc": ['red', 'o', 50],
            }
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, plot_design=plot_design, which='one-side')
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [1., 0., 0., 1.], "personalized t_calc color not red")
            rejection = axes.get_children()[1]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[2]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[3]
            self.assertEqual(plot_line.get_color()[0], "r", "default plot_line color not black")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['b', '-', 1.5],
                "area-rejection": ['lightgray'],
                "area-acceptance": ['silver'],
                "tcalc": ['red', 'o', 50],
            }
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, plot_design=plot_design, which='one-side')
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [1., 0., 0., 1.], "personalized t_calc color not red")
            rejection = axes.get_children()[1]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            accepted = axes.get_children()[2]
            expected = [0.7529411764705882, 0.7529411764705882, 0.7529411764705882, 1.0]
            for item, value in zip(list(accepted.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="accepted color not silver")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "b", "default plot_line color not black")
            plt.close()


class Test_ax_test_draw(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gl = 5
        cls.tcalc = 4
        cls.whichs = [None, 'two-side', 'one-side']

    def test_which_none(self):

        with patch('matplotlib.pyplot.show') as p:

            test = StudentDistribution()
            fig, axes = plt.subplots()
            axes, output = test.draw(self.gl, self.tcalc, ax=axes)
            result = isinstance(output, dict)
            self.assertTrue(result, "output is not a dict")
            result = isinstance(axes, matplotlib.axes.SubplotBase)
            self.assertTrue(result, "Ax not returned")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            fig, axes = plt.subplots()
            axes, output = test.draw(self.gl, self.tcalc, ax=axes)
            expected = ['curve', 'tcalc', 't_left', 't_right']
            for key, values in zip(output.keys(), expected):
                self.assertEqual(key, values, msg="wrong dict key")

            self.assertEqual(output['tcalc'][0], 4, msg="wrong tcalc returned")
            self.assertAlmostEqual(output['tcalc'][1], 0.005123727051, msg="wrong teoretical value for tcalc  returned")

            self.assertAlmostEqual(output['t_left'][0], -2.57058183661474, msg="wrong t_left returned")
            self.assertAlmostEqual(output['t_left'][1], 0.030337787761265618, msg="wrong teoretical value for t_left  returned")

            self.assertAlmostEqual(output['t_right'][0], 2.57058183661474, msg="wrong t_right returned")
            self.assertAlmostEqual(output['t_right'][1], 0.030337787761265618, msg="wrong teoretical value for t_right  returned")

            self.assertAlmostEqual(output['t_right'][1], output['t_left'][1], msg="teoretical value for t_right and t_left does not match")
            self.assertAlmostEqual(output['t_right'][0], -1*output['t_left'][0], msg="t value for t_right and t_left does not match")

            labels = axes.get_children()
            expected = ["$t_{calc} = $4", "Rejection region", "_collection2", "_collection3", "$gl=5$"]
            for label, correct in zip(labels, expected):
                self.assertEqual(label.get_label(), correct, msg="label does not match")

            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "Student's $t$", "something wrong with x_label")

            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Probability density", "something wrong with y_label")

            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")

            plt.close()

    def test_which_two_side(self):

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            fig, axes = plt.subplots()
            axes, output = test.draw(self.gl, self.tcalc, ax=axes, which="two-side")
            result = isinstance(output, dict)
            self.assertTrue(result, "output is not a dict")
            result = isinstance(axes, matplotlib.axes.SubplotBase)
            self.assertTrue(result, "Ax not returned")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            fig, axes = plt.subplots()
            axes, output = test.draw(self.gl, self.tcalc, ax=axes, which="two-side")
            expected = ['curve', 'tcalc', 't_left', 't_right']
            for key, values in zip(output.keys(), expected):
                self.assertEqual(key, values, msg="wrong dict key")

            self.assertEqual(output['tcalc'][0], 4, msg="wrong tcalc returned")
            self.assertAlmostEqual(output['tcalc'][1], 0.005123727051, msg="wrong teoretical value for tcalc  returned")

            self.assertAlmostEqual(output['t_left'][0], -2.57058183661474, msg="wrong t_left returned")
            self.assertAlmostEqual(output['t_left'][1], 0.030337787761265618, msg="wrong teoretical value for t_left  returned")

            self.assertAlmostEqual(output['t_right'][0], 2.57058183661474, msg="wrong t_right returned")
            self.assertAlmostEqual(output['t_right'][1], 0.030337787761265618, msg="wrong teoretical value for t_right  returned")

            self.assertAlmostEqual(output['t_right'][1], output['t_left'][1], msg="teoretical value for t_right and t_left does not match")
            self.assertAlmostEqual(output['t_right'][0], -1*output['t_left'][0], msg="t value for t_right and t_left does not match")

            labels = axes.get_children()
            expected = ["$t_{calc} = $4", "Rejection region", "_collection2", "_collection3", "$gl=5$"]
            for label, correct in zip(labels, expected):
                self.assertEqual(label.get_label(), correct, msg="label does not match")

            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "Student's $t$", "something wrong with x_label")

            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Probability density", "something wrong with y_label")

            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")

            plt.close()

    def test_which_one_side(self):

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            fig, axes = plt.subplots()
            axes, output = test.draw(self.gl, self.tcalc, ax=axes, which="one-side")
            result = isinstance(output, dict)
            self.assertTrue(result, "output is not a dict")
            result = isinstance(axes, matplotlib.axes.SubplotBase)
            self.assertTrue(result, "Ax not returned")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            fig, axes = plt.subplots()
            axes, output = test.draw(self.gl, self.tcalc, ax=axes, which="one-side")
            expected = ['curve', 'tcalc', 't_student']
            for key, values in zip(output.keys(), expected):
                self.assertEqual(key, values, msg="wrong dict key")

            self.assertEqual(output['tcalc'][0], 4, msg="wrong tcalc returned")
            self.assertAlmostEqual(output['tcalc'][1], 0.005123727051, msg="wrong teoretical value for tcalc  returned")

            self.assertAlmostEqual(output['t_student'][0], 2.015048372669157, msg="wrong t_student returned")
            self.assertAlmostEqual(output['t_student'][1], 0.06379679895149033, msg="wrong teoretical value for t_student  returned")

            labels = axes.get_children()
            expected = ["$t_{calc} = $4", "Rejection region", "_collection2", "$gl=5$"]
            for label, correct in zip(labels, expected):
                self.assertEqual(label.get_label(), correct, msg="label does not match")

            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "Student's $t$", "something wrong with x_label")

            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Probability density", "something wrong with y_label")

            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[2]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[3]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")

            plt.close()

    def test_x_label(self):
        for which in self.whichs:
            with patch('matplotlib.pyplot.show') as p:
                test = StudentDistribution()
                fig, axes = plt.subplots()
                axes, output = test.draw(self.gl, self.tcalc, ax=axes, which=which)
                x_label = axes.get_xlabel()
                self.assertIsInstance(x_label, str, "xlabel not a string")
                self.assertEqual(x_label, "Student's $t$", "something wrong with x_label")
                plt.close()

            with patch('matplotlib.pyplot.show') as p:
                test = StudentDistribution(language='pt-br')
                fig, axes = plt.subplots()
                axes, output = test.draw(self.gl, self.tcalc, ax=axes, which=which)
                x_label = axes.get_xlabel()
                self.assertIsInstance(x_label, str, "xlabel not a string")
                self.assertEqual(x_label, "$t$ de Student", "something wrong with x_label when language='pt-br'")
                plt.close()

            with patch('matplotlib.pyplot.show') as p:
                test = StudentDistribution()
                fig, axes = plt.subplots()
                axes, output = test.draw(self.gl, self.tcalc, ax=axes, which=which, x_label="my data")
                x_label = axes.get_xlabel()
                self.assertIsInstance(x_label, str, "xlabel not a string")
                self.assertEqual(x_label, "my data", "something wrong when changing x_label")
                plt.close()

    def test_y_label(self):
        for which in self.whichs:
            plt.close()
            with patch('matplotlib.pyplot.show') as p:
                test = StudentDistribution()
                fig, axes = plt.subplots()
                axes, output = test.draw(self.gl, self.tcalc, ax=axes, which=which)
                y_label = axes.get_ylabel()
                self.assertIsInstance(y_label, str, "ylabel not a string")
                self.assertEqual(y_label, "Probability density", "something wrong with y_label")
                plt.close()

            with patch('matplotlib.pyplot.show') as p:
                test = StudentDistribution(language='pt-br')
                fig, axes = plt.subplots()
                axes, output = test.draw(self.gl, self.tcalc, ax=axes, which=which)
                y_label = axes.get_ylabel()
                self.assertIsInstance(y_label, str, "ylabel not a string")
                self.assertEqual(y_label, "Densidade de probabilidade", "something wrong with x_label when language='pt-br'")
                plt.close()

            with patch('matplotlib.pyplot.show') as p:
                test = StudentDistribution()
                fig, axes = plt.subplots()
                axes, output = test.draw(self.gl, self.tcalc, ax=axes, which=which, y_label="my data")
                y_label = axes.get_ylabel()
                self.assertIsInstance(y_label, str, "xlabel not a string")
                self.assertEqual(y_label, "my data", "something wrong when changing y_label")
                plt.close()

    def test_decimal_separator(self):
        for which in self.whichs:
            plt.close()
            with patch('matplotlib.pyplot.show') as p:
                test = StudentDistribution()
                fig, axes = plt.subplots()
                axes, output = test.draw(self.gl, self.tcalc, ax=axes, which=which, decimal_separator=".")
                for text in axes.get_yticklabels():
                    temp = text.get_text()
                    result = True
                    if ',' in temp:
                        result = False
                self.assertTrue(result, "No dot in y axis")
                plt.close()

            with patch('matplotlib.pyplot.show') as p:
                test = StudentDistribution()
                fig, axes = plt.subplots()
                axes, output = test.draw(self.gl, self.tcalc, ax=axes, which=which, decimal_separator=None)
                for text in axes.get_yticklabels():
                    temp = text.get_text()
                    result = True
                    if ',' in temp:
                        result = False
                self.assertTrue(result, "No dot in y axis")
                plt.close()

    def test_legend(self):
        for which in self.whichs:
            plt.close()
            with patch('matplotlib.pyplot.show') as p:
                test = StudentDistribution()
                fig, axes = plt.subplots()
                axes, output = test.draw(self.gl, self.tcalc, ax=axes, which=which)
                legends = axes.get_legend_handles_labels()
                expected = ["$gl=5$", "$t_{calc} = $4", "Rejection region",]
                for label, correct in zip(legends[-1], expected):
                    self.assertEqual(label, correct, msg="legend label does not match")
                plt.close()

            with patch('matplotlib.pyplot.show') as p:
                test = StudentDistribution(language='pt-br')
                fig, axes = plt.subplots()
                axes, output = test.draw(self.gl, self.tcalc, ax=axes, which=which)
                legends = axes.get_legend_handles_labels()
                expected = ["$gl=5$", "$t_{calc} = $4", "Região de rejeição",]
                for label, correct in zip(legends[-1], expected):
                    self.assertEqual(label, correct, msg="legend label does not match")
                plt.close()

            with patch('matplotlib.pyplot.show') as p:
                test = StudentDistribution()
                fig, axes = plt.subplots()
                axes, output = test.draw(self.gl, self.tcalc, ax=axes, which=which, legend=True)
                legends = axes.get_legend_handles_labels()
                expected = ["$gl=5$", "$t_{calc} = $4", "Rejection region",]
                for label, correct in zip(legends[-1], expected):
                    self.assertEqual(label, correct, msg="legend label does not match")
                plt.close()

            with patch('matplotlib.pyplot.show') as p:
                test = StudentDistribution()
                fig, axes = plt.subplots()
                axes, output = test.draw(self.gl, self.tcalc, ax=axes, which=which, legend=False)
                legend_texts = axes.get_legend()
                self.assertIsNone(legend_texts, msg="legend not None when NO legend was added")
                plt.close()

            with patch('matplotlib.pyplot.show') as p:
                plot_design = {
                    "distribution": ['k', '-', 1.5],
                    "area-rejection": ['gainsboro'],
                    "area-acceptance": ['black'],
                    "tcalc": ['k', 'o', 50],
                }
                fig, axes = plt.subplots()
                axes, output = test.draw(self.gl, self.tcalc, ax=axes, which=which, legend=True, plot_design=plot_design)
                legends = axes.get_legend_handles_labels()
                expected = ["$gl=5$", "$t_{calc} = $4", "Rejection region", 'Acceptance region']
                for label, correct in zip(legends[-1], expected):
                    self.assertEqual(label, correct, msg="legend label does not match")
                plt.close()

            with patch('matplotlib.pyplot.show') as p:
                plot_design = {
                    "distribution": ['k', '-', 1.5],
                    "area-rejection": ['gainsboro'],
                    "area-acceptance": ['black'],
                    "tcalc": ['k', 'o', 50],
                }
                fig, axes = plt.subplots()
                axes, output = test.draw(self.gl, self.tcalc, ax=axes, which=which, legend=False, plot_design=plot_design)
                legends = axes.get_legend_handles_labels()
                legend_texts = axes.get_legend()
                self.assertIsNone(legend_texts, msg="legend not None when NO legend was added")
                plt.close()

    def test_plot_design(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            fig, axes = plt.subplots()
            axes, output = test.draw(self.gl, self.tcalc, ax=axes, which="two-side")
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            fig, axes = plt.subplots()
            axes, output = test.draw(self.gl, self.tcalc, ax=axes, which="two-side", plot_design ='gray')

            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")

            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['red', '-', 1.5],
                "area-rejection": ['lightgray'],
                "area-acceptance": ['white'],
                "tcalc": ['red', 'o', 50],
            }
            test = StudentDistribution()
            fig, axes = plt.subplots()
            axes, output = test.draw(self.gl, self.tcalc, ax=axes, which="two-side", plot_design=plot_design)
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [1., 0., 0., 1.], "personalized t_calc color not red")
            rejection = axes.get_children()[1]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "r", "default plot_line color not black")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['b', '-', 1.5],
                "area-rejection": ['lightgray'],
                "area-acceptance": ['silver'],
                "tcalc": ['red', 'o', 50],
            }
            test = StudentDistribution()
            fig, axes = plt.subplots()
            axes, output = test.draw(self.gl, self.tcalc, ax=axes, which="two-side", plot_design=plot_design)
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [1., 0., 0., 1.], "personalized t_calc color not red")
            rejection = axes.get_children()[1]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            accepted = axes.get_children()[3]
            expected = [0.7529411764705882, 0.7529411764705882, 0.7529411764705882, 1.0]
            for item, value in zip(list(accepted.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="accepted color not silver")
            h_line = axes.get_children()[4]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[5]
            self.assertEqual(plot_line.get_color()[0], "b", "default plot_line color not black")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            fig, axes = plt.subplots()
            axes, output = test.draw(self.gl, self.tcalc, ax=axes, which="one-side")
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[2]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[3]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            fig, axes = plt.subplots()
            axes, output = test.draw(self.gl, self.tcalc, ax=axes, which="one-side", plot_design ='gray')

            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[2]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[3]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")

            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['red', '-', 1.5],
                "area-rejection": ['lightgray'],
                "area-acceptance": ['white'],
                "tcalc": ['red', 'o', 50],
            }
            test = StudentDistribution()
            fig, axes = plt.subplots()
            axes, output = test.draw(self.gl, self.tcalc, ax=axes, which="one-side", plot_design=plot_design)
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [1., 0., 0., 1.], "personalized t_calc color not red")
            rejection = axes.get_children()[1]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[2]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[3]
            self.assertEqual(plot_line.get_color()[0], "r", "default plot_line color not black")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['b', '-', 1.5],
                "area-rejection": ['lightgray'],
                "area-acceptance": ['silver'],
                "tcalc": ['red', 'o', 50],
            }
            test = StudentDistribution()
            fig, axes = plt.subplots()
            axes, output = test.draw(self.gl, self.tcalc, ax=axes, which="one-side", plot_design=plot_design)
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [1., 0., 0., 1.], "personalized t_calc color not red")
            rejection = axes.get_children()[1]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            accepted = axes.get_children()[2]
            expected = [0.7529411764705882, 0.7529411764705882, 0.7529411764705882, 1.0]
            for item, value in zip(list(accepted.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="accepted color not silver")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "b", "default plot_line color not black")
            plt.close()



class Test_None_test_draw_dataset2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gl = 5
        cls.tcalc = 1

    def test_which_none(self):

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which=None)
            result = isinstance(output, dict)
            self.assertTrue(result, "output is not a dict")
            result = isinstance(axes, matplotlib.axes.SubplotBase)
            self.assertTrue(result, "Ax not returned")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc)
            expected = ['curve', 'tcalc', 't_left', 't_right']
            for key, values in zip(output.keys(), expected):
                self.assertEqual(key, values, msg="wrong dict key")

            self.assertEqual(output['tcalc'][0], self.tcalc, msg="wrong tcalc returned")
            self.assertAlmostEqual(output['tcalc'][1], 0.2196797973509806, msg="wrong teoretical value for tcalc  returned")

            self.assertAlmostEqual(output['t_left'][0], -2.57058183661474, msg="wrong t_left returned")
            self.assertAlmostEqual(output['t_left'][1], 0.030337787761265618, msg="wrong teoretical value for t_left  returned")

            self.assertAlmostEqual(output['t_right'][0], 2.57058183661474, msg="wrong t_right returned")
            self.assertAlmostEqual(output['t_right'][1], 0.030337787761265618, msg="wrong teoretical value for t_right  returned")

            self.assertAlmostEqual(output['t_right'][1], output['t_left'][1], msg="teoretical value for t_right and t_left does not match")
            self.assertAlmostEqual(output['t_right'][0], -1*output['t_left'][0], msg="t value for t_right and t_left does not match")

            labels = axes.get_children()
            expected = ["$t_{calc} = $1", "Rejection region", "_collection2", "_collection3", "$gl=5$"]
            for label, correct in zip(labels, expected):
                self.assertEqual(label.get_label(), correct, msg="label does not match")

            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "Student's $t$", "something wrong with x_label")

            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Probability density", "something wrong with y_label")

            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

    def test_which_two_side(self):

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which="two-side")
            result = isinstance(output, dict)
            self.assertTrue(result, "output is not a dict")
            result = isinstance(axes, matplotlib.axes.SubplotBase)
            self.assertTrue(result, "Ax not returned")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which="two-side")
            expected = ['curve', 'tcalc', 't_left', 't_right']
            for key, values in zip(output.keys(), expected):
                self.assertEqual(key, values, msg="wrong dict key")

            self.assertEqual(output['tcalc'][0], self.tcalc, msg="wrong tcalc returned")
            self.assertAlmostEqual(output['tcalc'][1], 0.2196797973509806, msg="wrong teoretical value for tcalc  returned")

            self.assertAlmostEqual(output['t_left'][0], -2.57058183661474, msg="wrong t_left returned")
            self.assertAlmostEqual(output['t_left'][1], 0.030337787761265618, msg="wrong teoretical value for t_left  returned")

            self.assertAlmostEqual(output['t_right'][0], 2.57058183661474, msg="wrong t_right returned")
            self.assertAlmostEqual(output['t_right'][1], 0.030337787761265618, msg="wrong teoretical value for t_right  returned")

            self.assertAlmostEqual(output['t_right'][1], output['t_left'][1], msg="teoretical value for t_right and t_left does not match")
            self.assertAlmostEqual(output['t_right'][0], -1*output['t_left'][0], msg="t value for t_right and t_left does not match")

            labels = axes.get_children()
            expected = ["$t_{calc} = $1", "Rejection region", "_collection2", "_collection3", "$gl=5$"]
            for label, correct in zip(labels, expected):
                self.assertEqual(label.get_label(), correct, msg="label does not match")

            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "Student's $t$", "something wrong with x_label")

            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Probability density", "something wrong with y_label")

            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

    def test_calc(self):

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output_one_side = test.draw(self.gl, self.tcalc, which="one-side")
            test = StudentDistribution()
            axes, output_two_side = test.draw(self.gl, self.tcalc, which="two-side")

            self.assertEqual(output_two_side['tcalc'][0], output_one_side['tcalc'][0], msg='tcalc does not match')
            self.assertEqual(output_two_side['tcalc'][1], output_one_side['tcalc'][1], msg='y tcalc does not match')
            plt.close()

    def test_which_one_side(self):

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which="one-side")
            result = isinstance(output, dict)
            self.assertTrue(result, "output is not a dict")
            result = isinstance(axes, matplotlib.axes.SubplotBase)
            self.assertTrue(result, "Ax not returned")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which="one-side")
            expected = ['curve', 'tcalc', 't_student']
            for key, values in zip(output.keys(), expected):
                self.assertEqual(key, values, msg="wrong dict key")

            self.assertEqual(output['tcalc'][0], self.tcalc, msg="wrong tcalc returned")
            self.assertAlmostEqual(output['tcalc'][1], 0.2196797973509806, msg="wrong teoretical value for tcalc  returned")

            self.assertAlmostEqual(output['t_student'][0], 2.015048372669157, msg="wrong t_student returned")
            self.assertAlmostEqual(output['t_student'][1], 0.06379679895149033, msg="wrong teoretical value for t_student  returned")

            labels = axes.get_children()
            expected = ["$t_{calc} = $1", "Rejection region", "_collection2", "$gl=5$"]
            for label, correct in zip(labels, expected):
                self.assertEqual(label.get_label(), correct, msg="label does not match")

            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "Student's $t$", "something wrong with x_label")

            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Probability density", "something wrong with y_label")

            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[2]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[3]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

    def test_x_label(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc)
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "Student's $t$", "something wrong with x_label")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution(language='pt-br')
            axes, output = test.draw(self.gl, self.tcalc)
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "$t$ de Student", "something wrong with x_label when language='pt-br'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, x_label="my data")
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "my data", "something wrong when changing x_label")
            plt.close()


        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "Student's $t$", "something wrong with x_label")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution(language='pt-br')
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "$t$ de Student", "something wrong with x_label when language='pt-br'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, x_label="my data", which='one-side')
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "my data", "something wrong when changing x_label")
            plt.close()

    def test_y_label(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc)
            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Probability density", "something wrong with y_label")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution(language='pt-br')
            axes, output = test.draw(self.gl, self.tcalc)
            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Densidade de probabilidade", "something wrong with x_label when language='pt-br'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, y_label="my data")
            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "xlabel not a string")
            self.assertEqual(y_label, "my data", "something wrong when changing y_label")
            plt.close()


        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Probability density", "something wrong with y_label")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution(language='pt-br')
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Densidade de probabilidade", "something wrong with x_label when language='pt-br'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, y_label="my data", which='one-side')
            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "xlabel not a string")
            self.assertEqual(y_label, "my data", "something wrong when changing y_label")
            plt.close()

    def test_width_height(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc)
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 525.7222222222223, msg="wrong defalt height")
            self.assertAlmostEqual(ax_w, 1109.7222222222222, msg="wrong defalt width")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, width=5, height=5)
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 425.72222222222223, msg="wrong personalized height")
            self.assertAlmostEqual(ax_w, 409.72222222222223, msg="wrong personalized width")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 525.7222222222223, msg="wrong defalt height")
            self.assertAlmostEqual(ax_w, 1109.7222222222222, msg="wrong defalt width")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, width=5, height=5, which='one-side')
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 425.72222222222223, msg="wrong personalized height")
            self.assertAlmostEqual(ax_w, 409.72222222222223, msg="wrong personalized width")
            plt.close()

    def test_plot_export(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True)
            result = _check_file_exists("student_distribution.png")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'student_distribution.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="teste")
            result = _check_file_exists("teste.png")
            rem_file = Path("teste.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'teste.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="teste", extension='pdf')
            result = _check_file_exists("teste.pdf")
            rem_file = Path("teste.pdf")
            rem_file.unlink()
            self.assertTrue(result, "File 'teste.pdf' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=False, file_name="teste", extension='pdf')
            result = _check_file_exists("teste.pdf")
            try:
                rem_file = Path("teste.pdf")
                rem_file.unlink()
            except:
                pass
            self.assertFalse(result, "File 'teste.pdf' was created even with export=False")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, which='one-side')
            result = _check_file_exists("student_distribution.png")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'student_distribution.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="teste", which='one-side')
            result = _check_file_exists("teste.png")
            rem_file = Path("teste.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'teste.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="teste", extension='pdf', which='one-side')
            result = _check_file_exists("teste.pdf")
            rem_file = Path("teste.pdf")
            rem_file.unlink()
            self.assertTrue(result, "File 'teste.pdf' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=False, file_name="teste", extension='pdf', which='one-side')
            result = _check_file_exists("teste.pdf")
            try:
                rem_file = Path("teste.pdf")
                rem_file.unlink()
            except:
                pass
            self.assertFalse(result, "File 'teste.pdf' was created even with export=False")
            plt.close()

    def test_plot_export_file_already_exists(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True)
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True)
            result = _check_file_exists("student_distribution_1.png")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            rem_file = Path("student_distribution_1.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'student_distribution_1.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="bawtidaba")
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="bawtidaba")
            result = _check_file_exists("bawtidaba_1.png")
            rem_file = Path("bawtidaba.png")
            rem_file.unlink()
            rem_file = Path("bawtidaba_1.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'bawtidaba_1.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, which='one-side')
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, which='one-side')
            result = _check_file_exists("student_distribution_1.png")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            rem_file = Path("student_distribution_1.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'student_distribution_1.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="bawtidaba", which='one-side')
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="bawtidaba", which='one-side')
            result = _check_file_exists("bawtidaba_1.png")
            rem_file = Path("bawtidaba.png")
            rem_file.unlink()
            rem_file = Path("bawtidaba_1.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'bawtidaba_1.png' was not created")
            plt.close()

    def test_dpi(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True)
            image = Image.open("student_distribution.png")
            w, h = image.info["dpi"]
            image.close()
            self.assertEqual(w, 99.9998, "wrong defalt dpi")
            self.assertEqual(h, 99.9998, "wrong defalt dpi")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, dpi=300)
            image = Image.open("student_distribution.png")
            w, h = image.info["dpi"]
            image.close()
            self.assertEqual(w, 299.9994, "wrong personalized dpi")
            self.assertEqual(h, 299.9994, "wrong personalized dpi")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            plt.close()


        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, which='one-side')
            image = Image.open("student_distribution.png")
            w, h = image.info["dpi"]
            image.close()
            self.assertEqual(w, 99.9998, "wrong defalt dpi")
            self.assertEqual(h, 99.9998, "wrong defalt dpi")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, dpi=300, which='one-side')
            image = Image.open("student_distribution.png")
            w, h = image.info["dpi"]
            image.close()
            self.assertEqual(w, 299.9994, "wrong personalized dpi")
            self.assertEqual(h, 299.9994, "wrong personalized dpi")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            plt.close()

    def test_decimal_separator(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, decimal_separator=",")
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = False
                if ',' in temp:
                    result = True
            self.assertTrue(result, "No comma in y axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, decimal_separator=".")
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = True
                if ',' in temp:
                    result = False
            self.assertTrue(result, "No dot in y axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, decimal_separator=None)
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = True
                if ',' in temp:
                    result = False
            self.assertTrue(result, "No dot in y axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, decimal_separator=",", which='one-side')
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = False
                if ',' in temp:
                    result = True
            self.assertTrue(result, "No comma in y axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, decimal_separator=".", which='one-side')
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = True
                if ',' in temp:
                    result = False
            self.assertTrue(result, "No dot in y axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, decimal_separator=None, which='one-side')
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = True
                if ',' in temp:
                    result = False
            self.assertTrue(result, "No dot in y axis")
            plt.close()

    def test_legend(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc,)
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $1", "Rejection region",]
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution(language='pt-br')
            axes, output = test.draw(self.gl, self.tcalc,)
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $1", "Região de rejeição",]
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, legend=True)
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $1", "Rejection region",]
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, legend=False)
            legend_texts = axes.get_legend()
            self.assertIsNone(legend_texts, msg="legend not None when NO legend was added")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['k', '-', 1.5],
                "area-rejection": ['gainsboro'],
                "area-acceptance": ['black'],
                "tcalc": ['k', 'o', 50],
            }
            axes, output = test.draw(self.gl, self.tcalc, legend=True, plot_design=plot_design)
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $1", "Rejection region", 'Acceptance region']
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['k', '-', 1.5],
                "area-rejection": ['gainsboro'],
                "area-acceptance": ['black'],
                "tcalc": ['k', 'o', 50],
            }
            axes, output = test.draw(self.gl, self.tcalc, legend=False, plot_design=plot_design)
            legends = axes.get_legend_handles_labels()
            legend_texts = axes.get_legend()
            self.assertIsNone(legend_texts, msg="legend not None when NO legend was added")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $1", "Rejection region",]
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution(language='pt-br')
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $1", "Região de rejeição",]
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, legend=True, which='one-side')
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $1", "Rejection region",]
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, legend=False, which='one-side')
            legend_texts = axes.get_legend()
            self.assertIsNone(legend_texts, msg="legend not None when NO legend was added")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['k', '-', 1.5],
                "area-rejection": ['gainsboro'],
                "area-acceptance": ['black'],
                "tcalc": ['k', 'o', 50],
            }
            axes, output = test.draw(self.gl, self.tcalc, legend=True, plot_design=plot_design, which='one-side')
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $1", "Rejection region", 'Acceptance region']
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['k', '-', 1.5],
                "area-rejection": ['gainsboro'],
                "area-acceptance": ['black'],
                "tcalc": ['k', 'o', 50],
            }
            axes, output = test.draw(self.gl, self.tcalc, legend=False, plot_design=plot_design, which='one-side')
            legends = axes.get_legend_handles_labels()
            legend_texts = axes.get_legend()
            self.assertIsNone(legend_texts, msg="legend not None when NO legend was added")
            plt.close()

    def test_plot_design(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc)
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, plot_design ='gray')
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['red', '-', 1.5],
                "area-rejection": ['lightgray'],
                "area-acceptance": ['white'],
                "tcalc": ['red', 'o', 50],
            }
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, plot_design=plot_design)
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [1., 0., 0., 1.], "personalized t_calc color not red")
            rejection = axes.get_children()[1]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "r", "default plot_line color not black")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['b', '-', 1.5],
                "area-rejection": ['lightgray'],
                "area-acceptance": ['silver'],
                "tcalc": ['red', 'o', 50],
            }
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, plot_design=plot_design)
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [1., 0., 0., 1.], "personalized t_calc color not red")
            rejection = axes.get_children()[1]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            accepted = axes.get_children()[3]
            expected = [0.7529411764705882, 0.7529411764705882, 0.7529411764705882, 1.0]
            for item, value in zip(list(accepted.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="accepted color not silver")
            h_line = axes.get_children()[4]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[5]
            self.assertEqual(plot_line.get_color()[0], "b", "default plot_line color not black")
            plt.close()


        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[2]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[3]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, plot_design ='gray', which='one-side')
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[2]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[3]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['red', '-', 1.5],
                "area-rejection": ['lightgray'],
                "area-acceptance": ['white'],
                "tcalc": ['red', 'o', 50],
            }
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, plot_design=plot_design, which='one-side')
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [1., 0., 0., 1.], "personalized t_calc color not red")
            rejection = axes.get_children()[1]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[2]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[3]
            self.assertEqual(plot_line.get_color()[0], "r", "default plot_line color not black")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['b', '-', 1.5],
                "area-rejection": ['lightgray'],
                "area-acceptance": ['silver'],
                "tcalc": ['red', 'o', 50],
            }
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, plot_design=plot_design, which='one-side')
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [1., 0., 0., 1.], "personalized t_calc color not red")
            rejection = axes.get_children()[1]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            accepted = axes.get_children()[2]
            expected = [0.7529411764705882, 0.7529411764705882, 0.7529411764705882, 1.0]
            for item, value in zip(list(accepted.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="accepted color not silver")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "b", "default plot_line color not black")
            plt.close()



class Test_None_test_draw_dataset3(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gl = 5
        cls.tcalc = -1

    def test_which_none(self):

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which=None)
            result = isinstance(output, dict)
            self.assertTrue(result, "output is not a dict")
            result = isinstance(axes, matplotlib.axes.SubplotBase)
            self.assertTrue(result, "Ax not returned")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc)
            expected = ['curve', 'tcalc', 't_left', 't_right']
            for key, values in zip(output.keys(), expected):
                self.assertEqual(key, values, msg="wrong dict key")

            self.assertEqual(output['tcalc'][0], self.tcalc, msg="wrong tcalc returned")
            self.assertAlmostEqual(output['tcalc'][1], 0.2196797973509806, msg="wrong teoretical value for tcalc  returned")

            self.assertAlmostEqual(output['t_left'][0], -2.57058183661474, msg="wrong t_left returned")
            self.assertAlmostEqual(output['t_left'][1], 0.030337787761265618, msg="wrong teoretical value for t_left  returned")

            self.assertAlmostEqual(output['t_right'][0], 2.57058183661474, msg="wrong t_right returned")
            self.assertAlmostEqual(output['t_right'][1], 0.030337787761265618, msg="wrong teoretical value for t_right  returned")

            self.assertAlmostEqual(output['t_right'][1], output['t_left'][1], msg="teoretical value for t_right and t_left does not match")
            self.assertAlmostEqual(output['t_right'][0], -1*output['t_left'][0], msg="t value for t_right and t_left does not match")

            labels = axes.get_children()
            expected = ["$t_{calc} = $-1", "Rejection region", "_collection2", "_collection3", "$gl=5$"]
            for label, correct in zip(labels, expected):
                self.assertEqual(label.get_label(), correct, msg="label does not match")

            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "Student's $t$", "something wrong with x_label")

            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Probability density", "something wrong with y_label")

            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

    def test_which_two_side(self):

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which="two-side")
            result = isinstance(output, dict)
            self.assertTrue(result, "output is not a dict")
            result = isinstance(axes, matplotlib.axes.SubplotBase)
            self.assertTrue(result, "Ax not returned")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which="two-side")
            expected = ['curve', 'tcalc', 't_left', 't_right']
            for key, values in zip(output.keys(), expected):
                self.assertEqual(key, values, msg="wrong dict key")

            self.assertEqual(output['tcalc'][0], self.tcalc, msg="wrong tcalc returned")
            self.assertAlmostEqual(output['tcalc'][1], 0.2196797973509806, msg="wrong teoretical value for tcalc  returned")

            self.assertAlmostEqual(output['t_left'][0], -2.57058183661474, msg="wrong t_left returned")
            self.assertAlmostEqual(output['t_left'][1], 0.030337787761265618, msg="wrong teoretical value for t_left  returned")

            self.assertAlmostEqual(output['t_right'][0], 2.57058183661474, msg="wrong t_right returned")
            self.assertAlmostEqual(output['t_right'][1], 0.030337787761265618, msg="wrong teoretical value for t_right  returned")

            self.assertAlmostEqual(output['t_right'][1], output['t_left'][1], msg="teoretical value for t_right and t_left does not match")
            self.assertAlmostEqual(output['t_right'][0], -1*output['t_left'][0], msg="t value for t_right and t_left does not match")

            labels = axes.get_children()
            expected = ["$t_{calc} = $-1", "Rejection region", "_collection2", "_collection3", "$gl=5$"]
            for label, correct in zip(labels, expected):
                self.assertEqual(label.get_label(), correct, msg="label does not match")

            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "Student's $t$", "something wrong with x_label")

            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Probability density", "something wrong with y_label")

            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

    def test_calc(self):

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output_one_side = test.draw(self.gl, self.tcalc, which="one-side")
            test = StudentDistribution()
            axes, output_two_side = test.draw(self.gl, self.tcalc, which="two-side")

            self.assertEqual(output_two_side['tcalc'][0], output_one_side['tcalc'][0], msg='tcalc does not match')
            self.assertEqual(output_two_side['tcalc'][1], output_one_side['tcalc'][1], msg='y tcalc does not match')
            plt.close()

    def test_which_one_side(self):

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which="one-side")
            result = isinstance(output, dict)
            self.assertTrue(result, "output is not a dict")
            result = isinstance(axes, matplotlib.axes.SubplotBase)
            self.assertTrue(result, "Ax not returned")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which="one-side")
            expected = ['curve', 'tcalc', 't_student']
            for key, values in zip(output.keys(), expected):
                self.assertEqual(key, values, msg="wrong dict key")

            self.assertEqual(output['tcalc'][0], self.tcalc, msg="wrong tcalc returned")
            self.assertAlmostEqual(output['tcalc'][1], 0.2196797973509806, msg="wrong teoretical value for tcalc  returned")

            self.assertAlmostEqual(output['t_student'][0], -2.015048372669157, msg="wrong t_student returned")
            self.assertAlmostEqual(output['t_student'][1], 0.06379679895149033, msg="wrong teoretical value for t_student  returned")

            labels = axes.get_children()
            expected = ["$t_{calc} = $-1", "Rejection region", "_collection2", "$gl=5$"]
            for label, correct in zip(labels, expected):
                self.assertEqual(label.get_label(), correct, msg="label does not match")

            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "Student's $t$", "something wrong with x_label")

            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Probability density", "something wrong with y_label")

            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[2]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[3]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

    def test_x_label(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc)
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "Student's $t$", "something wrong with x_label")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution(language='pt-br')
            axes, output = test.draw(self.gl, self.tcalc)
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "$t$ de Student", "something wrong with x_label when language='pt-br'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, x_label="my data")
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "my data", "something wrong when changing x_label")
            plt.close()


        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "Student's $t$", "something wrong with x_label")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution(language='pt-br')
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "$t$ de Student", "something wrong with x_label when language='pt-br'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, x_label="my data", which='one-side')
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "my data", "something wrong when changing x_label")
            plt.close()

    def test_y_label(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc)
            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Probability density", "something wrong with y_label")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution(language='pt-br')
            axes, output = test.draw(self.gl, self.tcalc)
            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Densidade de probabilidade", "something wrong with x_label when language='pt-br'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, y_label="my data")
            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "xlabel not a string")
            self.assertEqual(y_label, "my data", "something wrong when changing y_label")
            plt.close()


        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Probability density", "something wrong with y_label")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution(language='pt-br')
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Densidade de probabilidade", "something wrong with x_label when language='pt-br'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, y_label="my data", which='one-side')
            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "xlabel not a string")
            self.assertEqual(y_label, "my data", "something wrong when changing y_label")
            plt.close()

    def test_width_height(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc)
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 525.7222222222223, msg="wrong defalt height")
            self.assertAlmostEqual(ax_w, 1109.7222222222222, msg="wrong defalt width")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, width=5, height=5)
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 425.72222222222223, msg="wrong personalized height")
            self.assertAlmostEqual(ax_w, 409.72222222222223, msg="wrong personalized width")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 525.7222222222223, msg="wrong defalt height")
            self.assertAlmostEqual(ax_w, 1109.7222222222222, msg="wrong defalt width")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, width=5, height=5, which='one-side')
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 425.72222222222223, msg="wrong personalized height")
            self.assertAlmostEqual(ax_w, 409.72222222222223, msg="wrong personalized width")
            plt.close()

    def test_plot_export(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True)
            result = _check_file_exists("student_distribution.png")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'student_distribution.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="teste")
            result = _check_file_exists("teste.png")
            rem_file = Path("teste.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'teste.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="teste", extension='pdf')
            result = _check_file_exists("teste.pdf")
            rem_file = Path("teste.pdf")
            rem_file.unlink()
            self.assertTrue(result, "File 'teste.pdf' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=False, file_name="teste", extension='pdf')
            result = _check_file_exists("teste.pdf")
            try:
                rem_file = Path("teste.pdf")
                rem_file.unlink()
            except:
                pass
            self.assertFalse(result, "File 'teste.pdf' was created even with export=False")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, which='one-side')
            result = _check_file_exists("student_distribution.png")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'student_distribution.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="teste", which='one-side')
            result = _check_file_exists("teste.png")
            rem_file = Path("teste.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'teste.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="teste", extension='pdf', which='one-side')
            result = _check_file_exists("teste.pdf")
            rem_file = Path("teste.pdf")
            rem_file.unlink()
            self.assertTrue(result, "File 'teste.pdf' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=False, file_name="teste", extension='pdf', which='one-side')
            result = _check_file_exists("teste.pdf")
            try:
                rem_file = Path("teste.pdf")
                rem_file.unlink()
            except:
                pass
            self.assertFalse(result, "File 'teste.pdf' was created even with export=False")
            plt.close()

    def test_plot_export_file_already_exists(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True)
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True)
            result = _check_file_exists("student_distribution_1.png")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            rem_file = Path("student_distribution_1.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'student_distribution_1.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="bawtidaba")
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="bawtidaba")
            result = _check_file_exists("bawtidaba_1.png")
            rem_file = Path("bawtidaba.png")
            rem_file.unlink()
            rem_file = Path("bawtidaba_1.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'bawtidaba_1.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, which='one-side')
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, which='one-side')
            result = _check_file_exists("student_distribution_1.png")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            rem_file = Path("student_distribution_1.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'student_distribution_1.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="bawtidaba", which='one-side')
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="bawtidaba", which='one-side')
            result = _check_file_exists("bawtidaba_1.png")
            rem_file = Path("bawtidaba.png")
            rem_file.unlink()
            rem_file = Path("bawtidaba_1.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'bawtidaba_1.png' was not created")
            plt.close()

    def test_dpi(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True)
            image = Image.open("student_distribution.png")
            w, h = image.info["dpi"]
            image.close()
            self.assertEqual(w, 99.9998, "wrong defalt dpi")
            self.assertEqual(h, 99.9998, "wrong defalt dpi")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, dpi=300)
            image = Image.open("student_distribution.png")
            w, h = image.info["dpi"]
            image.close()
            self.assertEqual(w, 299.9994, "wrong personalized dpi")
            self.assertEqual(h, 299.9994, "wrong personalized dpi")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            plt.close()


        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, which='one-side')
            image = Image.open("student_distribution.png")
            w, h = image.info["dpi"]
            image.close()
            self.assertEqual(w, 99.9998, "wrong defalt dpi")
            self.assertEqual(h, 99.9998, "wrong defalt dpi")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, dpi=300, which='one-side')
            image = Image.open("student_distribution.png")
            w, h = image.info["dpi"]
            image.close()
            self.assertEqual(w, 299.9994, "wrong personalized dpi")
            self.assertEqual(h, 299.9994, "wrong personalized dpi")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            plt.close()

    def test_decimal_separator(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, decimal_separator=",")
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = False
                if ',' in temp:
                    result = True
            self.assertTrue(result, "No comma in y axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, decimal_separator=".")
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = True
                if ',' in temp:
                    result = False
            self.assertTrue(result, "No dot in y axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, decimal_separator=None)
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = True
                if ',' in temp:
                    result = False
            self.assertTrue(result, "No dot in y axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, decimal_separator=",", which='one-side')
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = False
                if ',' in temp:
                    result = True
            self.assertTrue(result, "No comma in y axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, decimal_separator=".", which='one-side')
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = True
                if ',' in temp:
                    result = False
            self.assertTrue(result, "No dot in y axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, decimal_separator=None, which='one-side')
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = True
                if ',' in temp:
                    result = False
            self.assertTrue(result, "No dot in y axis")
            plt.close()

    def test_legend(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc,)
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $-1", "Rejection region",]
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution(language='pt-br')
            axes, output = test.draw(self.gl, self.tcalc,)
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $-1", "Região de rejeição",]
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, legend=True)
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $-1", "Rejection region",]
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, legend=False)
            legend_texts = axes.get_legend()
            self.assertIsNone(legend_texts, msg="legend not None when NO legend was added")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['k', '-', 1.5],
                "area-rejection": ['gainsboro'],
                "area-acceptance": ['black'],
                "tcalc": ['k', 'o', 50],
            }
            axes, output = test.draw(self.gl, self.tcalc, legend=True, plot_design=plot_design)
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $-1", "Rejection region", 'Acceptance region']
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['k', '-', 1.5],
                "area-rejection": ['gainsboro'],
                "area-acceptance": ['black'],
                "tcalc": ['k', 'o', 50],
            }
            axes, output = test.draw(self.gl, self.tcalc, legend=False, plot_design=plot_design)
            legends = axes.get_legend_handles_labels()
            legend_texts = axes.get_legend()
            self.assertIsNone(legend_texts, msg="legend not None when NO legend was added")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $-1", "Rejection region",]
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution(language='pt-br')
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $-1", "Região de rejeição",]
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, legend=True, which='one-side')
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $-1", "Rejection region",]
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, legend=False, which='one-side')
            legend_texts = axes.get_legend()
            self.assertIsNone(legend_texts, msg="legend not None when NO legend was added")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['k', '-', 1.5],
                "area-rejection": ['gainsboro'],
                "area-acceptance": ['black'],
                "tcalc": ['k', 'o', 50],
            }
            axes, output = test.draw(self.gl, self.tcalc, legend=True, plot_design=plot_design, which='one-side')
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $-1", "Rejection region", 'Acceptance region']
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['k', '-', 1.5],
                "area-rejection": ['gainsboro'],
                "area-acceptance": ['black'],
                "tcalc": ['k', 'o', 50],
            }
            axes, output = test.draw(self.gl, self.tcalc, legend=False, plot_design=plot_design, which='one-side')
            legends = axes.get_legend_handles_labels()
            legend_texts = axes.get_legend()
            self.assertIsNone(legend_texts, msg="legend not None when NO legend was added")
            plt.close()

    def test_plot_design(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc)
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, plot_design ='gray')
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['red', '-', 1.5],
                "area-rejection": ['lightgray'],
                "area-acceptance": ['white'],
                "tcalc": ['red', 'o', 50],
            }
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, plot_design=plot_design)
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [1., 0., 0., 1.], "personalized t_calc color not red")
            rejection = axes.get_children()[1]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "r", "default plot_line color not black")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['b', '-', 1.5],
                "area-rejection": ['lightgray'],
                "area-acceptance": ['silver'],
                "tcalc": ['red', 'o', 50],
            }
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, plot_design=plot_design)
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [1., 0., 0., 1.], "personalized t_calc color not red")
            rejection = axes.get_children()[1]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            accepted = axes.get_children()[3]
            expected = [0.7529411764705882, 0.7529411764705882, 0.7529411764705882, 1.0]
            for item, value in zip(list(accepted.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="accepted color not silver")
            h_line = axes.get_children()[4]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[5]
            self.assertEqual(plot_line.get_color()[0], "b", "default plot_line color not black")
            plt.close()


        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[2]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[3]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, plot_design ='gray', which='one-side')
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[2]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[3]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['red', '-', 1.5],
                "area-rejection": ['lightgray'],
                "area-acceptance": ['white'],
                "tcalc": ['red', 'o', 50],
            }
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, plot_design=plot_design, which='one-side')
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [1., 0., 0., 1.], "personalized t_calc color not red")
            rejection = axes.get_children()[1]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[2]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[3]
            self.assertEqual(plot_line.get_color()[0], "r", "default plot_line color not black")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['b', '-', 1.5],
                "area-rejection": ['lightgray'],
                "area-acceptance": ['silver'],
                "tcalc": ['red', 'o', 50],
            }
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, plot_design=plot_design, which='one-side')
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [1., 0., 0., 1.], "personalized t_calc color not red")
            rejection = axes.get_children()[1]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            accepted = axes.get_children()[2]
            expected = [0.7529411764705882, 0.7529411764705882, 0.7529411764705882, 1.0]
            for item, value in zip(list(accepted.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="accepted color not silver")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "b", "default plot_line color not black")
            plt.close()



class Test_None_test_draw_dataset3(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gl = 5
        cls.tcalc = -4

    def test_which_none(self):

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which=None)
            result = isinstance(output, dict)
            self.assertTrue(result, "output is not a dict")
            result = isinstance(axes, matplotlib.axes.SubplotBase)
            self.assertTrue(result, "Ax not returned")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc)
            expected = ['curve', 'tcalc', 't_left', 't_right']
            for key, values in zip(output.keys(), expected):
                self.assertEqual(key, values, msg="wrong dict key")

            self.assertEqual(output['tcalc'][0], self.tcalc, msg="wrong tcalc returned")
            self.assertAlmostEqual(output['tcalc'][1], 0.005123727051917913, msg="wrong teoretical value for tcalc  returned")

            self.assertAlmostEqual(output['t_left'][0], -2.57058183661474, msg="wrong t_left returned")
            self.assertAlmostEqual(output['t_left'][1], 0.030337787761265618, msg="wrong teoretical value for t_left  returned")

            self.assertAlmostEqual(output['t_right'][0], 2.57058183661474, msg="wrong t_right returned")
            self.assertAlmostEqual(output['t_right'][1], 0.030337787761265618, msg="wrong teoretical value for t_right  returned")

            self.assertAlmostEqual(output['t_right'][1], output['t_left'][1], msg="teoretical value for t_right and t_left does not match")
            self.assertAlmostEqual(output['t_right'][0], -1*output['t_left'][0], msg="t value for t_right and t_left does not match")

            labels = axes.get_children()
            expected = ["$t_{calc} = $-4", "Rejection region", "_collection2", "_collection3", "$gl=5$"]
            for label, correct in zip(labels, expected):
                self.assertEqual(label.get_label(), correct, msg="label does not match")

            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "Student's $t$", "something wrong with x_label")

            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Probability density", "something wrong with y_label")

            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

    def test_which_two_side(self):

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which="two-side")
            result = isinstance(output, dict)
            self.assertTrue(result, "output is not a dict")
            result = isinstance(axes, matplotlib.axes.SubplotBase)
            self.assertTrue(result, "Ax not returned")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which="two-side")
            expected = ['curve', 'tcalc', 't_left', 't_right']
            for key, values in zip(output.keys(), expected):
                self.assertEqual(key, values, msg="wrong dict key")

            self.assertEqual(output['tcalc'][0], self.tcalc, msg="wrong tcalc returned")
            self.assertAlmostEqual(output['tcalc'][1], 0.005123727051917913, msg="wrong teoretical value for tcalc  returned")

            self.assertAlmostEqual(output['t_left'][0], -2.57058183661474, msg="wrong t_left returned")
            self.assertAlmostEqual(output['t_left'][1], 0.030337787761265618, msg="wrong teoretical value for t_left  returned")

            self.assertAlmostEqual(output['t_right'][0], 2.57058183661474, msg="wrong t_right returned")
            self.assertAlmostEqual(output['t_right'][1], 0.030337787761265618, msg="wrong teoretical value for t_right  returned")

            self.assertAlmostEqual(output['t_right'][1], output['t_left'][1], msg="teoretical value for t_right and t_left does not match")
            self.assertAlmostEqual(output['t_right'][0], -1*output['t_left'][0], msg="t value for t_right and t_left does not match")

            labels = axes.get_children()
            expected = ["$t_{calc} = $-4", "Rejection region", "_collection2", "_collection3", "$gl=5$"]
            for label, correct in zip(labels, expected):
                self.assertEqual(label.get_label(), correct, msg="label does not match")

            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "Student's $t$", "something wrong with x_label")

            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Probability density", "something wrong with y_label")

            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

    def test_calc(self):

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output_one_side = test.draw(self.gl, self.tcalc, which="one-side")
            test = StudentDistribution()
            axes, output_two_side = test.draw(self.gl, self.tcalc, which="two-side")

            self.assertEqual(output_two_side['tcalc'][0], output_one_side['tcalc'][0], msg='tcalc does not match')
            self.assertEqual(output_two_side['tcalc'][1], output_one_side['tcalc'][1], msg='y tcalc does not match')
            plt.close()

    def test_which_one_side(self):

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which="one-side")
            result = isinstance(output, dict)
            self.assertTrue(result, "output is not a dict")
            result = isinstance(axes, matplotlib.axes.SubplotBase)
            self.assertTrue(result, "Ax not returned")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which="one-side")
            expected = ['curve', 'tcalc', 't_student']
            for key, values in zip(output.keys(), expected):
                self.assertEqual(key, values, msg="wrong dict key")

            self.assertEqual(output['tcalc'][0], self.tcalc, msg="wrong tcalc returned")
            self.assertAlmostEqual(output['tcalc'][1], 0.005123727051917913, msg="wrong teoretical value for tcalc  returned")

            self.assertAlmostEqual(output['t_student'][0], -2.015048372669157, msg="wrong t_student returned")
            self.assertAlmostEqual(output['t_student'][1], 0.06379679895149033, msg="wrong teoretical value for t_student  returned")

            labels = axes.get_children()
            expected = ["$t_{calc} = $-4", "Rejection region", "_collection2", "$gl=5$"]
            for label, correct in zip(labels, expected):
                self.assertEqual(label.get_label(), correct, msg="label does not match")

            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "Student's $t$", "something wrong with x_label")

            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Probability density", "something wrong with y_label")

            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[2]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[3]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

    def test_x_label(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc)
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "Student's $t$", "something wrong with x_label")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution(language='pt-br')
            axes, output = test.draw(self.gl, self.tcalc)
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "$t$ de Student", "something wrong with x_label when language='pt-br'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, x_label="my data")
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "my data", "something wrong when changing x_label")
            plt.close()


        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "Student's $t$", "something wrong with x_label")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution(language='pt-br')
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "$t$ de Student", "something wrong with x_label when language='pt-br'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, x_label="my data", which='one-side')
            x_label = axes.get_xlabel()
            self.assertIsInstance(x_label, str, "xlabel not a string")
            self.assertEqual(x_label, "my data", "something wrong when changing x_label")
            plt.close()

    def test_y_label(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc)
            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Probability density", "something wrong with y_label")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution(language='pt-br')
            axes, output = test.draw(self.gl, self.tcalc)
            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Densidade de probabilidade", "something wrong with x_label when language='pt-br'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, y_label="my data")
            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "xlabel not a string")
            self.assertEqual(y_label, "my data", "something wrong when changing y_label")
            plt.close()


        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Probability density", "something wrong with y_label")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution(language='pt-br')
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "ylabel not a string")
            self.assertEqual(y_label, "Densidade de probabilidade", "something wrong with x_label when language='pt-br'")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, y_label="my data", which='one-side')
            y_label = axes.get_ylabel()
            self.assertIsInstance(y_label, str, "xlabel not a string")
            self.assertEqual(y_label, "my data", "something wrong when changing y_label")
            plt.close()

    def test_width_height(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc)
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 525.7222222222223, msg="wrong defalt height")
            self.assertAlmostEqual(ax_w, 1109.7222222222222, msg="wrong defalt width")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, width=5, height=5)
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 425.72222222222223, msg="wrong personalized height")
            self.assertAlmostEqual(ax_w, 409.72222222222223, msg="wrong personalized width")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 525.7222222222223, msg="wrong defalt height")
            self.assertAlmostEqual(ax_w, 1109.7222222222222, msg="wrong defalt width")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, width=5, height=5, which='one-side')
            ax_h, ax_w = axes.bbox.height, axes.bbox.width
            self.assertAlmostEqual(ax_h, 425.72222222222223, msg="wrong personalized height")
            self.assertAlmostEqual(ax_w, 409.72222222222223, msg="wrong personalized width")
            plt.close()

    def test_plot_export(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True)
            result = _check_file_exists("student_distribution.png")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'student_distribution.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="teste")
            result = _check_file_exists("teste.png")
            rem_file = Path("teste.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'teste.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="teste", extension='pdf')
            result = _check_file_exists("teste.pdf")
            rem_file = Path("teste.pdf")
            rem_file.unlink()
            self.assertTrue(result, "File 'teste.pdf' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=False, file_name="teste", extension='pdf')
            result = _check_file_exists("teste.pdf")
            try:
                rem_file = Path("teste.pdf")
                rem_file.unlink()
            except:
                pass
            self.assertFalse(result, "File 'teste.pdf' was created even with export=False")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, which='one-side')
            result = _check_file_exists("student_distribution.png")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'student_distribution.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="teste", which='one-side')
            result = _check_file_exists("teste.png")
            rem_file = Path("teste.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'teste.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="teste", extension='pdf', which='one-side')
            result = _check_file_exists("teste.pdf")
            rem_file = Path("teste.pdf")
            rem_file.unlink()
            self.assertTrue(result, "File 'teste.pdf' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=False, file_name="teste", extension='pdf', which='one-side')
            result = _check_file_exists("teste.pdf")
            try:
                rem_file = Path("teste.pdf")
                rem_file.unlink()
            except:
                pass
            self.assertFalse(result, "File 'teste.pdf' was created even with export=False")
            plt.close()

    def test_plot_export_file_already_exists(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True)
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True)
            result = _check_file_exists("student_distribution_1.png")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            rem_file = Path("student_distribution_1.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'student_distribution_1.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="bawtidaba")
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="bawtidaba")
            result = _check_file_exists("bawtidaba_1.png")
            rem_file = Path("bawtidaba.png")
            rem_file.unlink()
            rem_file = Path("bawtidaba_1.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'bawtidaba_1.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, which='one-side')
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, which='one-side')
            result = _check_file_exists("student_distribution_1.png")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            rem_file = Path("student_distribution_1.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'student_distribution_1.png' was not created")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="bawtidaba", which='one-side')
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, file_name="bawtidaba", which='one-side')
            result = _check_file_exists("bawtidaba_1.png")
            rem_file = Path("bawtidaba.png")
            rem_file.unlink()
            rem_file = Path("bawtidaba_1.png")
            rem_file.unlink()
            self.assertTrue(result, "File 'bawtidaba_1.png' was not created")
            plt.close()

    def test_dpi(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True)
            image = Image.open("student_distribution.png")
            w, h = image.info["dpi"]
            image.close()
            self.assertEqual(w, 99.9998, "wrong defalt dpi")
            self.assertEqual(h, 99.9998, "wrong defalt dpi")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, dpi=300)
            image = Image.open("student_distribution.png")
            w, h = image.info["dpi"]
            image.close()
            self.assertEqual(w, 299.9994, "wrong personalized dpi")
            self.assertEqual(h, 299.9994, "wrong personalized dpi")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            plt.close()


        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, which='one-side')
            image = Image.open("student_distribution.png")
            w, h = image.info["dpi"]
            image.close()
            self.assertEqual(w, 99.9998, "wrong defalt dpi")
            self.assertEqual(h, 99.9998, "wrong defalt dpi")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, ax=None, export=True, dpi=300, which='one-side')
            image = Image.open("student_distribution.png")
            w, h = image.info["dpi"]
            image.close()
            self.assertEqual(w, 299.9994, "wrong personalized dpi")
            self.assertEqual(h, 299.9994, "wrong personalized dpi")
            rem_file = Path("student_distribution.png")
            rem_file.unlink()
            plt.close()

    def test_decimal_separator(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, decimal_separator=",")
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = False
                if ',' in temp:
                    result = True
            self.assertTrue(result, "No comma in y axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, decimal_separator=".")
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = True
                if ',' in temp:
                    result = False
            self.assertTrue(result, "No dot in y axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, decimal_separator=None)
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = True
                if ',' in temp:
                    result = False
            self.assertTrue(result, "No dot in y axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, decimal_separator=",", which='one-side')
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = False
                if ',' in temp:
                    result = True
            self.assertTrue(result, "No comma in y axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, decimal_separator=".", which='one-side')
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = True
                if ',' in temp:
                    result = False
            self.assertTrue(result, "No dot in y axis")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, decimal_separator=None, which='one-side')
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = True
                if ',' in temp:
                    result = False
            self.assertTrue(result, "No dot in y axis")
            plt.close()

    def test_legend(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc,)
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $-4", "Rejection region",]
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution(language='pt-br')
            axes, output = test.draw(self.gl, self.tcalc,)
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $-4", "Região de rejeição",]
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, legend=True)
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $-4", "Rejection region",]
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, legend=False)
            legend_texts = axes.get_legend()
            self.assertIsNone(legend_texts, msg="legend not None when NO legend was added")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['k', '-', 1.5],
                "area-rejection": ['gainsboro'],
                "area-acceptance": ['black'],
                "tcalc": ['k', 'o', 50],
            }
            axes, output = test.draw(self.gl, self.tcalc, legend=True, plot_design=plot_design)
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $-4", "Rejection region", 'Acceptance region']
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['k', '-', 1.5],
                "area-rejection": ['gainsboro'],
                "area-acceptance": ['black'],
                "tcalc": ['k', 'o', 50],
            }
            axes, output = test.draw(self.gl, self.tcalc, legend=False, plot_design=plot_design)
            legends = axes.get_legend_handles_labels()
            legend_texts = axes.get_legend()
            self.assertIsNone(legend_texts, msg="legend not None when NO legend was added")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $-4", "Rejection region",]
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution(language='pt-br')
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $-4", "Região de rejeição",]
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, legend=True, which='one-side')
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $-4", "Rejection region",]
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, legend=False, which='one-side')
            legend_texts = axes.get_legend()
            self.assertIsNone(legend_texts, msg="legend not None when NO legend was added")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['k', '-', 1.5],
                "area-rejection": ['gainsboro'],
                "area-acceptance": ['black'],
                "tcalc": ['k', 'o', 50],
            }
            axes, output = test.draw(self.gl, self.tcalc, legend=True, plot_design=plot_design, which='one-side')
            legends = axes.get_legend_handles_labels()
            expected = ["$gl=5$", "$t_{calc} = $-4", "Rejection region", 'Acceptance region']
            for label, correct in zip(legends[-1], expected):
                self.assertEqual(label, correct, msg="legend label does not match")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['k', '-', 1.5],
                "area-rejection": ['gainsboro'],
                "area-acceptance": ['black'],
                "tcalc": ['k', 'o', 50],
            }
            axes, output = test.draw(self.gl, self.tcalc, legend=False, plot_design=plot_design, which='one-side')
            legends = axes.get_legend_handles_labels()
            legend_texts = axes.get_legend()
            self.assertIsNone(legend_texts, msg="legend not None when NO legend was added")
            plt.close()

    def test_plot_design(self):
        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc)
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, plot_design ='gray')
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['red', '-', 1.5],
                "area-rejection": ['lightgray'],
                "area-acceptance": ['white'],
                "tcalc": ['red', 'o', 50],
            }
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, plot_design=plot_design)
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [1., 0., 0., 1.], "personalized t_calc color not red")
            rejection = axes.get_children()[1]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "r", "default plot_line color not black")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['b', '-', 1.5],
                "area-rejection": ['lightgray'],
                "area-acceptance": ['silver'],
                "tcalc": ['red', 'o', 50],
            }
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, plot_design=plot_design)
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [1., 0., 0., 1.], "personalized t_calc color not red")
            rejection = axes.get_children()[1]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            rejection = axes.get_children()[2]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            accepted = axes.get_children()[3]
            expected = [0.7529411764705882, 0.7529411764705882, 0.7529411764705882, 1.0]
            for item, value in zip(list(accepted.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="accepted color not silver")
            h_line = axes.get_children()[4]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[5]
            self.assertEqual(plot_line.get_color()[0], "b", "default plot_line color not black")
            plt.close()


        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, which='one-side')
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[2]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[3]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, plot_design ='gray', which='one-side')
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [0., 0., 0., 1.], "default t_calc color not black")
            rejection = axes.get_children()[1]
            expected = [0.8627451, 0.8627451, 0.8627451, 1.]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[2]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[3]
            self.assertEqual(plot_line.get_color()[0], "k", "default plot_line color not black")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['red', '-', 1.5],
                "area-rejection": ['lightgray'],
                "area-acceptance": ['white'],
                "tcalc": ['red', 'o', 50],
            }
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, plot_design=plot_design, which='one-side')
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [1., 0., 0., 1.], "personalized t_calc color not red")
            rejection = axes.get_children()[1]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            h_line = axes.get_children()[2]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[3]
            self.assertEqual(plot_line.get_color()[0], "r", "default plot_line color not black")
            plt.close()

        with patch('matplotlib.pyplot.show') as p:
            plot_design = {
                "distribution": ['b', '-', 1.5],
                "area-rejection": ['lightgray'],
                "area-acceptance": ['silver'],
                "tcalc": ['red', 'o', 50],
            }
            test = StudentDistribution()
            axes, output = test.draw(self.gl, self.tcalc, plot_design=plot_design, which='one-side')
            t_calc = axes.get_children()[0]
            self.assertListEqual(list(t_calc.get_ec()[0]), [1., 0., 0., 1.], "personalized t_calc color not red")
            rejection = axes.get_children()[1]
            expected = [0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0]
            for item, value in zip(list(rejection.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="default rejection color not black")
            accepted = axes.get_children()[2]
            expected = [0.7529411764705882, 0.7529411764705882, 0.7529411764705882, 1.0]
            for item, value in zip(list(accepted.get_ec()[0]), expected):
                self.assertAlmostEqual(item, value, msg="accepted color not silver")
            h_line = axes.get_children()[3]
            self.assertListEqual(list(h_line.get_ec()[0]), [0., 0., 0., 1.], "default h_line color not black")
            plot_line = axes.get_children()[4]
            self.assertEqual(plot_line.get_color()[0], "b", "default plot_line color not black")
            plt.close()



if __name__ == "__main__":
    unittest.main()
