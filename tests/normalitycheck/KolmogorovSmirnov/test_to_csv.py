"""Tests if the to_csv is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_to_csv. It is tested if the csv file is created. A test with an existing file is also done. The output is also verified if it is a DataFrame



--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/normalitycheck/KolmogorovSmirnov/test_to_csv.py

    or
    python -m unittest -b tests/normalitycheck/KolmogorovSmirnov/test_to_csv.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.normalitycheck.kolmogorovsmirnov import KolmogorovSmirnov
from pycafee.utils.helpers import _check_file_exists
import numpy as np
from pathlib import Path
import pandas as pd

os.system('cls')

class Test_ks_to_csv(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.my_data = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])


    def test_file_creating_1(self):

        ks_test = KolmogorovSmirnov()
        ks_test.fit(self.my_data)
        ks_test.to_csv()
        result = _check_file_exists("kolmogorov_smirnov.csv")
        self.assertTrue(result, "File was not created")
        rem_file = Path("kolmogorov_smirnov.csv")
        rem_file.unlink()

    def test_file_creating_2(self):

        ks_test = KolmogorovSmirnov()
        ks_test.fit(self.my_data)
        ks_test.to_csv("bawitdaba")
        result = _check_file_exists("bawitdaba.csv")
        self.assertTrue(result, "File was not created")
        rem_file = Path("bawitdaba.csv")
        rem_file.unlink()


    def test_file_creating_reapeted_name(self):

        ks_test = KolmogorovSmirnov()
        ks_test.fit(self.my_data)
        ks_test.to_csv("bawitdaba")
        ks_test.to_csv("bawitdaba")
        result = _check_file_exists("bawitdaba_1.csv")
        self.assertTrue(result, "Issue with file already exists")
        rem_file = Path("bawitdaba.csv")
        rem_file.unlink()
        rem_file = Path("bawitdaba_1.csv")
        rem_file.unlink()


    def test_output(self):

        ks_test = KolmogorovSmirnov()
        ks_test.fit(self.my_data)
        result = ks_test.to_csv()
        teste = isinstance(result, pd.DataFrame)
        self.assertTrue(teste, "The output was not a DataFrame")
        rem_file = Path("kolmogorov_smirnov.csv")
        rem_file.unlink()








if __name__ == "__main__":
    unittest.main()
