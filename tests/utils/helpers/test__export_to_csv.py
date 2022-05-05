"""Tests if the _export_to_csv is working as expected

---> Class Test_export_to_csv
    Esta classe verifica se o arquivo foi exportado e se o o sistema de nomes iguais funciona (mas de forma bem simplificada)


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/helpers/test__export_to_csv.py
    or
    python -m unittest -b tests/utils/helpers/test__export_to_csv.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.utils.helpers import _export_to_csv, _check_file_exists
import pandas as pd
from pathlib import Path
import csv
os.system('cls')

class Test_export_to_csv(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # criando um arquivo csv generico
        file_name = "bawitdaba.csv"
        # file_path = folder_name + "/" + file_name
        with open(file_name, 'w', newline='') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow([1,2,3])

        # fazendo o teste
        result = _check_file_exists(file_name)

        # para deletar o arquivo generico
        cls.rem_file = Path(file_name)


    @classmethod
    def tearDownClass(cls):
        cls.rem_file.unlink()


    def test_when_file_exists(self):
        df = pd.DataFrame(columns=["a"], data=["b"],)
        _export_to_csv(df, file_name="bawitdaba", sep=',', language='en')
        result = _check_file_exists("bawitdaba_1.csv")
        self.assertTrue(result, msg="Not True when file with same name is exported")
        rem_file = Path("bawitdaba_1.csv")
        rem_file.unlink()


    def test_pass(self):
        df = pd.DataFrame(columns=["a"], data=["b"],)
        result = _export_to_csv(df, file_name="my_data", sep=',', language='en')
        self.assertTrue(result, msg="Not True when file is exported")
        rem_file = Path("my_data.csv")
        rem_file.unlink()




    # def test_file_is_open(self):
    #     df = pd.DataFrame(columns=["a", 'b'])
    #     df["a"] = [1, 24]
    #     df["b"] = [3, 4]
    #     with self.assertRaises(OSError, msg="Does not raised error when file is open"):
    #         _export_to_csv(df, "name")
    #
    #     with self.assertRaises(PermissionError, msg="Does not raised error when file is open"):
    #         # _export_to_csv(df, "name")



# never an honest word, but thats when I run the world https://youtu.be/uNaHzwkDOIk?t=176

if __name__ == "__main__":
    unittest.main()
