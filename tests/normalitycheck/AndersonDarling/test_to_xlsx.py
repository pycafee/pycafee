"""Tests if the to_xlsx is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_to_xlsx. It is tested if the xlsx file is created. A test with an existing file is also done, on how deal with repeated sheet names. The output is also verified if it is a DataFrame



--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/normalitycheck/AndersonDarling/test_to_xlsx.py
    or
    python -m unittest -b tests/normalitycheck/AndersonDarling/test_to_xlsx.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.normalitycheck.andersondarling import AndersonDarling
from pycafee.utils.helpers import _check_file_exists
import numpy as np
from pathlib import Path
import pandas as pd

os.system('cls')

class Test_to_xlsx(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.my_data = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])


    def test_file_creating_xlsx(self):

        test = AndersonDarling()
        test.fit(self.my_data)
        test.to_xlsx()
        result = _check_file_exists("andersondarling.xlsx")
        self.assertTrue(result, "File was not created")
        rem_file = Path("andersondarling.xlsx")
        rem_file.unlink()

    def test_file_creating_2(self):

        test = AndersonDarling()
        test.fit(self.my_data)
        test.to_xlsx("bawitdaba")
        result = _check_file_exists("bawitdaba.xlsx")
        self.assertTrue(result, "File was not created")
        rem_file = Path("bawitdaba.xlsx")
        rem_file.unlink()


    def test_file_creating_reapeted_name(self):

        test = AndersonDarling()
        test.fit(self.my_data)
        test.to_xlsx("bawitdaba")
        test.to_xlsx("bawitdaba")
        arquivo = pd.ExcelFile("bawitdaba.xlsx", engine="openpyxl")
        sheets = arquivo.sheet_names
        result = False
        if "data1" in sheets:
            result = True
        self.assertTrue(result, "Issue with file already exists")
        result = False
        if "andersondarling1" in sheets:
            result = True
        self.assertTrue(result, "Issue with file already exists")
        arquivo.close()
        rem_file = Path("bawitdaba.xlsx")
        rem_file.unlink()



    def test_output(self):

        test = AndersonDarling()
        test.fit(self.my_data)
        result = test.to_xlsx()
        teste = isinstance(result, list)
        self.assertTrue(teste, "The output was not a list")
        rem_file = Path("andersondarling.xlsx")
        rem_file.unlink()

    def test_inner_output(self):

        test = AndersonDarling()
        test.fit(self.my_data)
        result = test.to_xlsx()
        teste = isinstance(result[0], pd.DataFrame)
        self.assertTrue(teste, "The output was not a list")
        rem_file = Path("andersondarling.xlsx")
        rem_file.unlink()

        test = AndersonDarling()
        test.fit(self.my_data)
        result = test.to_xlsx()
        teste = isinstance(result[1], pd.DataFrame)
        self.assertTrue(teste, "The output was not a list")
        rem_file = Path("andersondarling.xlsx")
        rem_file.unlink()







if __name__ == "__main__":
    unittest.main()
