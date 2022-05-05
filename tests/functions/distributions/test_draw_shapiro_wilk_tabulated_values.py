"""Tests if the draw_shapiro_wilk_tabulated_values is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_draw_shapiro_wilk_tabulated_values. This class checks if the axes is created and if the table is created. Both asserts uses show=False in order to prevent the plt.show() to pop the figure.



--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/functions/distributions/test_draw_shapiro_wilk_tabulated_values.py
    or
    python -m unittest -b tests/functions/distributions/test_draw_shapiro_wilk_tabulated_values.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.functions.distributions import ShapiroWilkNormalityTest
import numpy as np
import matplotlib.axes

os.system('cls')

class Test_draw_shapiro_wilk_tabulated_values(unittest.TestCase):

    def test_plot(self):
        shapiro = ShapiroWilkNormalityTest()
        axes, dicti = shapiro.draw_shapiro_wilk_tabulated_values(show=False)
        result = isinstance(axes, matplotlib.axes.SubplotBase)
        self.assertTrue(result, "Ax not created")

    def test_dict(self):
        shapiro = ShapiroWilkNormalityTest()
        axes, dicti = shapiro.draw_shapiro_wilk_tabulated_values(show=False)
        result = isinstance(dicti, dict)
        self.assertTrue(result, "Shapiro-Wilk table not created")










if __name__ == "__main__":
    unittest.main()
