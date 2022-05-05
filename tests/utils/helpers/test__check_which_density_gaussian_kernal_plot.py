"""Tests if the _check_which_density_gaussian_kernal_plot is working as expected

---> Class Test_check_which_density_gaussian_kernal_plot
    # This class tests if the 'value' is an integer number. Several types of integers are tested with the assertTrue statement. Also, the function is tested against strings, tuples, lists, and floats, which should raise a ValueError that is caught with assertRaises.

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/helpers/test__check_which_density_gaussian_kernal_plot.py
    or
    python -m unittest -b tests/utils/helpers/test__check_which_density_gaussian_kernal_plot.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from cup_of_coffee.utils.helpers import _check_which_density_gaussian_kernal_plot
import numpy as np
os.system('cls')

class Test_check_which_density_gaussian_kernal_plot(unittest.TestCase):

    def test_all_not_alone(self):
        with self.assertRaises(ValueError, msg="Does not raised error when which is 'all,mean'"):
            _check_which_density_gaussian_kernal_plot("all,mean", "en")
        with self.assertRaises(ValueError, msg="Does not raised error when which is 'median,all,mean'"):
            _check_which_density_gaussian_kernal_plot("median,all,mean", "en")
        with self.assertRaises(ValueError, msg="Does not raised error when which is 'median,all,mean,mode'"):
            _check_which_density_gaussian_kernal_plot("median,all,mean,mode", "en")

    def test_wrong_character(self):
        with self.assertRaises(ValueError, msg="Does not raised error when which is 'meank'"):
            _check_which_density_gaussian_kernal_plot("meank", "en")
        with self.assertRaises(ValueError, msg="Does not raised error when which is 'mea$n'"):
            _check_which_density_gaussian_kernal_plot("mea$n", "en")
        with self.assertRaises(ValueError, msg="Does not raised error when which is 'mea.nk'"):
            _check_which_density_gaussian_kernal_plot("mea.nk", "en")
        with self.assertRaises(ValueError, msg="Does not raised error when which is '*mean'"):
            _check_which_density_gaussian_kernal_plot("*mean", "en")

    def test_spelling(self):
        with self.assertRaises(ValueError, msg="Does not raised error when which is 'meanmode'"):
            _check_which_density_gaussian_kernal_plot("meanmode", "en")
        with self.assertRaises(ValueError, msg="Does not raised error when which is 'meanmedian'"):
            _check_which_density_gaussian_kernal_plot("meanmedian", "en")
        with self.assertRaises(ValueError, msg="Does not raised error when which is 'medianmode'"):
            _check_which_density_gaussian_kernal_plot("medianmode", "en")
        with self.assertRaises(ValueError, msg="Does not raised error when which is 'medianmodemean'"):
            _check_which_density_gaussian_kernal_plot("medianmodemean", "en")

    def test_wrong_key(self):
        with self.assertRaises(ValueError, msg="Does not raised error when which is 'all,'"):
            _check_which_density_gaussian_kernal_plot("all,", "en")
        with self.assertRaises(ValueError, msg="Does not raised error when which is 'all,mode,'"):
            _check_which_density_gaussian_kernal_plot("all,mode,", "en")
        with self.assertRaises(ValueError, msg="Does not raised error when which is 'all,mode,mean,'"):
            _check_which_density_gaussian_kernal_plot("all,mode,mean,", "en")

    def test_miss_spelling(self):
        with self.assertRaises(ValueError, msg="Does not raised error when which is 'laa'"):
            _check_which_density_gaussian_kernal_plot("laa", "en")
        with self.assertRaises(ValueError, msg="Does not raised error when which is 'dome'"):
            _check_which_density_gaussian_kernal_plot("dome", "en")
        with self.assertRaises(ValueError, msg="Does not raised error when which is 'nmea'"):
            _check_which_density_gaussian_kernal_plot("nmea", "en")
        with self.assertRaises(ValueError, msg="Does not raised error when which is 'medina'"):
            _check_which_density_gaussian_kernal_plot("medina", "en")

    def test_empty(self):
        with self.assertRaises(TypeError, msg="Does not raised error when no value was passed"):
            _check_which_density_gaussian_kernal_plot()

    def test_pass(self):
        result = _check_which_density_gaussian_kernal_plot("all", "en")
        self.assertEqual(result, ["all"], msg="Wrong result")

        result = _check_which_density_gaussian_kernal_plot("mean", "en")
        self.assertEqual(result, ["mean"], msg="Wrong result")

        result = _check_which_density_gaussian_kernal_plot("mode", "en")
        self.assertEqual(result, ["mode"], msg="Wrong result")

        result = _check_which_density_gaussian_kernal_plot("median", "en")
        self.assertEqual(result, ["median"], msg="Wrong result")

        result = _check_which_density_gaussian_kernal_plot("mean,mode", "en")
        self.assertEqual(result, ["mean", "mode"], msg="Wrong result")

        result = _check_which_density_gaussian_kernal_plot("mode,mean", "en")
        self.assertEqual(result, ["mode", "mean"], msg="Wrong result")

        result = _check_which_density_gaussian_kernal_plot("mean,median", "en")
        self.assertEqual(result, ["mean", "median"], msg="Wrong result")

        result = _check_which_density_gaussian_kernal_plot("median,mean", "en")
        self.assertEqual(result, ["median", "mean"], msg="Wrong result")

        result = _check_which_density_gaussian_kernal_plot("median,mode", "en")
        self.assertEqual(result, ["median", "mode"], msg="Wrong result")

        result = _check_which_density_gaussian_kernal_plot("mean,median,mode", "en")
        self.assertEqual(result, ["mean", "median", "mode"], msg="Wrong result")

        result = _check_which_density_gaussian_kernal_plot("mean ,median,mode  ", "en")
        self.assertEqual(result, ["mean", "median", "mode"], msg="Wrong result")

        result = _check_which_density_gaussian_kernal_plot("mean, median, mode", "en")
        self.assertEqual(result, ["mean", "median", "mode"], msg="Wrong result")

        result = _check_which_density_gaussian_kernal_plot("m ean, medi an, mo de", "en")
        self.assertEqual(result, ["mean", "median", "mode"], msg="Wrong result")








# m. e. t. l https://youtu.be/7idcgZGHCjM?t=140

if __name__ == "__main__":
    unittest.main()
