"""Tests if the _change_decimal_separator_y_axis is working as expected

---> Class Test_change_decimal_separator_y_axis. This function tests if the y axis is changed when sep is different from '.'.



--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/helpers/test__change_decimal_separator_y_axis.py
    or
    python -m unittest -b tests/utils/helpers/test__change_decimal_separator_y_axis.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from unittest.mock import patch
import matplotlib.pyplot as plt
import matplotlib.axes
import numpy as np
from pycafee.utils.helpers import _change_decimal_separator_y_axis
os.system('cls')

class Test_sep_checke(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.y = np.array([5.1, 4.9, 4.7])
        cls.x = np.arange(cls.y.size)*1.235


    def test_pass_dot(self):
        with patch('matplotlib.pyplot.show') as p:
            fig, axes = plt.subplots()
            axes.scatter(self.x, self.y)
            axes = _change_decimal_separator_y_axis(fig, axes, decimal_separator='.')
            result = isinstance(axes, matplotlib.axes.SubplotBase)
            plt.show()
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = True
                if ',' in temp:
                    result = False
            self.assertTrue(result, "No comma in y axis")
            plt.close()

    def test_pass_comma(self):
        with patch('matplotlib.pyplot.show') as p:
            fig, axes = plt.subplots()
            axes.scatter(self.x, self.y)
            axes = _change_decimal_separator_y_axis(fig, axes, decimal_separator=',')
            result = isinstance(axes, matplotlib.axes.SubplotBase)
            plt.show()
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = False
                if ',' in temp:
                    result = True
            self.assertTrue(result, "No comma in y axis")
            plt.close()

    def test_pass_two_commas(self):
        with patch('matplotlib.pyplot.show') as p:
            fig, axes = plt.subplots()
            axes.scatter(self.x, self.y)
            axes = _change_decimal_separator_y_axis(fig, axes, decimal_separator=',,')
            result = isinstance(axes, matplotlib.axes.SubplotBase)
            plt.show()
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = False
                if ',' in temp:
                    result = True
            self.assertTrue(result, "No comma in y axis")
            plt.close()

    def test_pass_bar(self):
        with patch('matplotlib.pyplot.show') as p:
            fig, axes = plt.subplots()
            axes.scatter(self.x, self.y)
            axes = _change_decimal_separator_y_axis(fig, axes, decimal_separator='\\')
            result = isinstance(axes, matplotlib.axes.SubplotBase)
            plt.show()
            for text in axes.get_yticklabels():
                temp = text.get_text()
                result = False
                if '\\' in temp:
                    result = True
            self.assertTrue(result, "No \ in y axis")
            plt.close()



# saikyou de saikou tte chou dou da iuno wa (pa pa pa pa pa pa pa pa ya) https://youtu.be/j246TQ5pBcQ?t=79

if __name__ == "__main__":
    unittest.main()
