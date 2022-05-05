"""Tests if the shapiro_wilk_to_xlsx is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_shapiro_wilk_to_xlsx. It is tested if the xlsx file is created. A test with an existing file is also done, on how deal with repeated sheet names. The output is also verified if it is a DataFrame



--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/functions/distributions/test_shapiro_wilk_to_xlsx.py
    or
    python -m unittest -b tests/functions/distributions/test_shapiro_wilk_to_xlsx.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from cup_of_coffee.functions.distributions import ShapiroWilkNormalityTest
from cup_of_coffee.utils.helpers import _check_file_exists
import numpy as np
from pathlib import Path
import pandas as pd

os.system('cls')

class Test_shapiro_wilk_to_xlsx(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.my_data = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])


    def test_file_creating_xlsx(self):

        normality_shapiro_wilk = ShapiroWilkNormalityTest()
        normality_shapiro_wilk.shapiro_wilk(self.my_data)
        normality_shapiro_wilk.shapiro_wilk_to_xlsx()

        result = _check_file_exists("shapiro_wilk.xlsx")

        self.assertTrue(result, "File was not created")
        rem_file = Path("shapiro_wilk.xlsx")
        rem_file.unlink()


    def test_file_creating_2(self):

        normality_shapiro_wilk = ShapiroWilkNormalityTest()
        normality_shapiro_wilk.shapiro_wilk(self.my_data)
        normality_shapiro_wilk.shapiro_wilk_to_xlsx("bawitdaba")

        result = _check_file_exists("bawitdaba.xlsx")

        self.assertTrue(result, "File was not created")
        rem_file = Path("bawitdaba.xlsx")
        rem_file.unlink()


    # def test_file_creating_reapeted_name(self):
    #
    #     normality_shapiro_wilk = ShapiroWilkNormalityTest()
    #     normality_shapiro_wilk.shapiro_wilk(self.my_data)
    #     normality_shapiro_wilk.shapiro_wilk_to_csv("bawitdaba")
    #     normality_shapiro_wilk.shapiro_wilk_to_csv("bawitdaba")
    #
    #     result = _check_file_exists("bawitdaba_1.csv")
    #
    #     self.assertTrue(result, "Issue with file already exists")
    #     rem_file = Path("bawitdaba.csv")
    #     rem_file.unlink()
    #     rem_file = Path("bawitdaba_1.csv")
    #     rem_file.unlink()


    def test_output(self):

        normality_shapiro_wilk = ShapiroWilkNormalityTest()
        normality_shapiro_wilk.shapiro_wilk(self.my_data)
        result = normality_shapiro_wilk.shapiro_wilk_to_xlsx()

        teste = isinstance(result, list)
        self.assertTrue(teste, "The output was not a list")
        rem_file = Path("shapiro_wilk.xlsx")
        rem_file.unlink()


    def test_inner_output(self):

        normality_shapiro_wilk = ShapiroWilkNormalityTest()
        normality_shapiro_wilk.shapiro_wilk(self.my_data)
        result = normality_shapiro_wilk.shapiro_wilk_to_xlsx()

        teste = isinstance(result[0], pd.DataFrame)
        self.assertTrue(teste, "The output was not a list")
        rem_file = Path("shapiro_wilk.xlsx")
        rem_file.unlink()

        normality_shapiro_wilk = ShapiroWilkNormalityTest()
        normality_shapiro_wilk.shapiro_wilk(self.my_data)
        result = normality_shapiro_wilk.shapiro_wilk_to_xlsx()

        teste = isinstance(result[1], pd.DataFrame)
        self.assertTrue(teste, "The output was not a list")
        rem_file = Path("shapiro_wilk.xlsx")
        rem_file.unlink()







if __name__ == "__main__":
    unittest.main()
