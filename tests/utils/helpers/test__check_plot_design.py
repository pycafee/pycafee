"""Tests if the _check_plot_design is working as expected

---> Class Test_check_plot_design
    This class tests if the 'design' is correct, based on a example.

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/helpers/test__check_plot_design.py
    or
    python -m unittest -b tests/utils/helpers/test__check_plot_design.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.utils.helpers import _check_plot_design
import numpy as np
os.system('cls')

class Test_check_plot_design(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.plot_design_default = {
            "kde": ['k', '-', 1.5],
            "Mean": ['dimgray', '--', 1.5],
            "Median": ['darkgray', '--', 1.5],
            "Mode": ['lightgray', '--', 1.5],
            "Area": ['white'],
            }
        cls.plot_design_example = {
            "kde": "['color name', 'line style', number]",
            "Mean": "['color name', 'line style', number]",
            "Median": "['color name', 'line style', number]",
            "Mode": "['color name', 'line style', number]",
            "Area": "['color name']",
            }

    def test_wrong_input_type(self):
        with self.assertRaises(ValueError, msg="Does not raised error the input type is wrong"):
            plot_design = {
                "kde": ['k', '-', "1.5"],
                "Mean": ['dimgray', '--', 1.5],
                "Median": ['darkgray', '--', 1.5],
                "Mode": ['lightgray', '--', 1.5],
                "Area": ['white'],
            }
            result = _check_plot_design(plot_design, "pram_name", self.plot_design_default, self.plot_design_example, language='en')

        with self.assertRaises(ValueError, msg="Does not raised error the input type is wrong"):
            plot_design = {
                "kde": ['k', '-', [1.5]],
                "Mean": ['dimgray', '--', 1.5],
                "Median": ['darkgray', '--', 1.5],
                "Mode": ['lightgray', '--', 1.5],
                "Area": ['white'],
            }
            result = _check_plot_design(plot_design, "pram_name", self.plot_design_default, self.plot_design_example, language='en')

        with self.assertRaises(ValueError, msg="Does not raised error the input type is wrong"):
            plot_design = {
                "kde": ['k', '-', 1.5],
                "Mean": ['dimgray', '--', 1.5],
                "Median": ['darkgray', 1, 1.5],
                "Mode": ['lightgray', '--', 1.5],
                "Area": ['white'],
            }
            result = _check_plot_design(plot_design, "pram_name", self.plot_design_default, self.plot_design_example, language='en')

    def test_wrong_size_input(self):
        with self.assertRaises(ValueError, msg="Does not raised error the input size is wrong"):
            plot_design = {
                "kde": ['k', '-', 1.5],
                "Mean": ['dimgray', '--', 1.5],
                "Median": ['darkgray', '--', 1.5],
                "Mode": ['lightgray', '--', 1.5],
                "Area": ['white', "--"],
            }
            result = _check_plot_design(plot_design, "pram_name", self.plot_design_default, self.plot_design_example, language='en')

        with self.assertRaises(ValueError, msg="Does not raised error the input size is wrong"):
            plot_design = {
                "kde": ['k', '-', 1.5],
                "Mean": ['dimgray', '--', 1.5],
                "Median": ['darkgray', '--', 1.5],
                "Mode": ['lightgray'],
                "Area": ['white'],
            }
            result = _check_plot_design(plot_design, "pram_name", self.plot_design_default, self.plot_design_example, language='en')

    def test_extra_key(self):
        with self.assertRaises(ValueError, msg="Does not raised error when plot-desing has a extra key"):
            plot_design = {
                "kde": ['k', '-', 1.5],
                "Mean": ['dimgray', '--', 1.5],
                "Median": ['darkgray', '--', 1.5],
                "Mode": ['lightgray', '--', 1.5],
                "Area": ['white'],
                "Name": ['Nome'],
            }
            result = _check_plot_design(plot_design, "pram_name", self.plot_design_default, self.plot_design_example, language='en')

    def test_missing_key(self):
        with self.assertRaises(ValueError, msg="Does not raised error when a key is missing"):
            plot_design = {
                "kde": ['k', '-', 1.5],
                "Mean": ['dimgray', '--', 1.5],
                "Median": ['darkgray', '--', 1.5],
                "Mode": ['lightgray', '--', 1.5],
            }
            result = _check_plot_design(plot_design, "pram_name", self.plot_design_default, self.plot_design_example, language='en')

    def test_wrong_keys(self):
        with self.assertRaises(ValueError, msg="Does not raised error when a key is wrong"):
            plot_design = {
                "kde": ['k', '-', 1.5],
                "Mean": ['dimgray', '--', 1.5],
                "Median": ['darkgray', '--', 1.5],
                "Mode": ['lightgray', '--', 1.5],
                "Areaa": ['white'],
            }
            result = _check_plot_design(plot_design, "pram_name", self.plot_design_default, self.plot_design_example, language='en')

        with self.assertRaises(ValueError, msg="Does not raised error when a key is wrong"):
            plot_design = {
                "kde": ['k', '-', 1.5],
                "Mean": ['dimgray', '--', 1.5],
                "Median": ['darkgray', '--', 1.5],
                "Modes": ['lightgray', '--', 1.5],
                "Area": ['white'],
            }
            result = _check_plot_design(plot_design, "pram_name", self.plot_design_default, self.plot_design_example, language='en')

    def test_empty(self):
        with self.assertRaises(TypeError, msg="Does not raised error a input is missing"):
            plot_design = {
                "kde": ['k', '-', 1.5],
                "Mean": ['dimgray', '--', 1.5],
                "Median": ['darkgray', '--', 1.5],
                "Mode": ['lightgray', '--', 1.5],
                "Area": ['white'],
            }
            result = _check_plot_design(plot_design, self.plot_design_default, self.plot_design_example, language='en')
        with self.assertRaises(TypeError, msg="Does not raised error a input is missing"):
            plot_design = {
                "kde": ['k', '-', 1.5],
                "Mean": ['dimgray', '--', 1.5],
                "Median": ['darkgray', '--', 1.5],
                "Mode": ['lightgray', '--', 1.5],
                "Area": ['white'],
            }
            result = _check_plot_design(plot_design, self.plot_design_default, language='en')

        with self.assertRaises(TypeError, msg="Does not raised error a input is missing"):
            plot_design = {
                "kde": ['k', '-', 1.5],
                "Mean": ['dimgray', '--', 1.5],
                "Median": ['darkgray', '--', 1.5],
                "Mode": ['lightgray', '--', 1.5],
                "Area": ['white'],
            }
            result = _check_plot_design(plot_design, language='en')

        with self.assertRaises(TypeError, msg="Does not raised error a input is missing"):
            result = _check_plot_design()

    def test_pass(self):
        plot_design = {
            "kde": ['k', '-', 1.5],
            "Mean": ['dimgray', '--', 1.5],
            "Median": ['darkgray', '--', 1.5],
            "Mode": ['lightgray', '--', 1.5],
            "Area": ['white'],
        }
        result = _check_plot_design(plot_design, "plot_design", self.plot_design_default, self.plot_design_example, language='en')
        self.assertTrue(result, msg = "An error was raised when value is shouldn't ")



# Crazy, crazy, crazy doukashiteru https://youtu.be/aqpS4zih_lM

if __name__ == "__main__":
    unittest.main()
