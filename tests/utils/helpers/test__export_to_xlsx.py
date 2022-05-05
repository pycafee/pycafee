"""Tests if the _export_to_xlsx is working as expected

---> Class Test_export_to_xlsx
    Esta classe verifica se o arquivo foi exportado e se o o sistema de nomes iguais funciona (mas de forma bem simplificada)


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/helpers/test__export_to_xlsx.py
    or
    python -m unittest -b tests/utils/helpers/test__export_to_xlsx.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.utils.helpers import _export_to_xlsx, _check_file_exists
import pandas as pd
from pathlib import Path

os.system('cls')

class Test_export_to_csv(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # criando um arquivo csv generico
        file_name = "bawitdaba.xlsx"
        # file_path = folder_name + "/" + file_name
        df = pd.DataFrame(columns=["a"], data=["c"])
        df.to_excel(file_name, index=False, engine="openpyxl")

        # fazendo o teste
        result = _check_file_exists(file_name)

        # para deletar o arquivo generico
        cls.rem_file = Path(file_name)


    @classmethod
    def tearDownClass(cls):
        cls.rem_file.unlink()


    def test_when_file_exists(self):
        df = pd.DataFrame(columns=["a"], data=["b"],)
        # _export_to_xlsx(df_list, language, file_name=None, sheet_names=[None,None])
        _export_to_xlsx([df], language='en', sheet_names=["a"])
        result = _check_file_exists("sample.xlsx")
        self.assertTrue(result, msg="Not True when file with same name is exported")
        rem_file = Path("sample.xlsx")
        rem_file.unlink()


    def test_pass(self):
        df = pd.DataFrame(columns=["a"], data=["b"],)
        _export_to_xlsx([df], file_name="bawitdaba", language='en', sheet_names=["a"])
        result = _check_file_exists("bawitdaba.xlsx")
        self.assertTrue(result, msg="Not True when file with same name is exported")







# never an honest word, but thats when I run the world https://youtu.be/uNaHzwkDOIk?t=176

if __name__ == "__main__":
    unittest.main()
