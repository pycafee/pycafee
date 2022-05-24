"""Tests if the to_csv is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_to_csv. It is tested if the csv file is created. A test with an existing file is also done. The output is also verified if it is a DataFrame



--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/normalitycheck/Lilliefors/test_to_csv.py

    or
    python -m unittest -b tests/normalitycheck/Lilliefors/test_to_csv.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.normalitycheck.lilliefors import Lilliefors
from pycafee.utils.helpers import _check_file_exists
import numpy as np
from pathlib import Path
import pandas as pd

os.system('cls')

class Test_to_csv(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.my_data = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])


    def test_file_creating_1(self):

        lilliefors_test = Lilliefors()
        lilliefors_test.fit(self.my_data)
        lilliefors_test.to_csv()
        result = _check_file_exists("lilliefors.csv")
        self.assertTrue(result, "File was not created")
        rem_file = Path("lilliefors.csv")
        rem_file.unlink()

    def test_file_creating_2(self):

        lilliefors_test = Lilliefors()
        lilliefors_test.fit(self.my_data)
        lilliefors_test.to_csv("bawitdaba")
        result = _check_file_exists("bawitdaba.csv")
        self.assertTrue(result, "File was not created")
        rem_file = Path("bawitdaba.csv")
        rem_file.unlink()


    def test_file_creating_reapeted_name(self):

        lilliefors_test = Lilliefors()
        lilliefors_test.fit(self.my_data)
        lilliefors_test.to_csv("bawitdaba")
        lilliefors_test.to_csv("bawitdaba")
        result = _check_file_exists("bawitdaba_1.csv")
        self.assertTrue(result, "Issue with file already exists")
        rem_file = Path("bawitdaba.csv")
        rem_file.unlink()
        rem_file = Path("bawitdaba_1.csv")
        rem_file.unlink()


    def test_output(self):

        lilliefors_test = Lilliefors()
        lilliefors_test.fit(self.my_data)
        result = lilliefors_test.to_csv()
        teste = isinstance(result, pd.DataFrame)
        self.assertTrue(teste, "The output was not a DataFrame")
        rem_file = Path("lilliefors.csv")
        rem_file.unlink()








if __name__ == "__main__":
    unittest.main()
