"""Tests if the _check_file_exists is working as expected

---> Class Test_check_file_exists
    # This class tests if a file exists or not.


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/helpers/test__check_file_exists.py
    or
    python -m unittest -b tests/utils/helpers/test__check_file_exists.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.utils.helpers import _check_file_exists
import csv
from pathlib import Path
os.system("cls")

class Test_sep_checker(unittest.TestCase):

    def test_file_does_not_exist(self):
        result = _check_file_exists("bawitdaba.csv")
        self.assertFalse(result, msg = "For some reason, the file bawitdaba exists!")

    def test_file_does_exist(self):
        # criando pasta temporaria
        folder_name = "temp"
        Path(folder_name).mkdir(parents=True, exist_ok=True)
        # criando um arquivo csv generico
        file_name = "bawitdaba.csv"
        file_path = folder_name + "/" + file_name
        with open(file_path, 'w', newline='') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow([1,2,3])

        # fazendo o teste
        result = _check_file_exists(file_path)

        # deletando o arquivo generico
        rem_file = Path(file_path)
        rem_file.unlink()
        # deletando o folder temporario
        q = Path(folder_name)
        q.rmdir()

        self.assertTrue(result, msg = "For some reason, the file temp/bawitdaba.csv exists!")





if __name__ == "__main__":
    unittest.main()
