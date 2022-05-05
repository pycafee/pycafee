"""Tests if the _check_conflicting_filename is working as expected

---> Class Test_check_conflicting_filename
    This class tests if the _check_conflicting_filename function is working as expected, testing when there is no name conflict, when there is a conflicting file, and when there are 2 conflicting files


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/helpers/test__check_conflicting_filename.py
    or
    python -m unittest -b tests/utils/helpers/test__check_conflicting_filename.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from cup_of_coffee.utils.helpers import _check_conflicting_filename
from pathlib import Path
import csv
os.system("cls")

class Test_check_conflicting_filename(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        # criando um arquivo csv generico
        cls.file_name = "bawitdaba.csv"
        # file_path = folder_name + "/" + file_name
        with open(cls.file_name, 'w', newline='') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow([1,2,3])

        # deletando o arquivo generico
        cls.rem_file = Path(cls.file_name)

    @classmethod
    def tearDownClass(cls):
        cls.rem_file.unlink()


    def test_file_does_not_exits(self):
        teste = _check_conflicting_filename('bawitdaba', "txt", 'en')
        self.assertEqual(teste, "bawitdaba.txt", msg="The file was changed when it should not")

    def test_file_already_exits(self):
        teste = _check_conflicting_filename('bawitdaba', "csv", 'en')
        self.assertEqual(teste, "bawitdaba_1.csv", msg="The is something wrong with the file name ")

    def test_file_already_exits_again(self):
        nome = "bawitdaba_1.csv"
        with open(nome, 'w', newline='') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow([1,2,3])
        rem_file = Path(nome)

        teste = _check_conflicting_filename('bawitdaba', "csv", 'en')
        self.assertEqual(teste, "bawitdaba_2.csv", msg="The is something wrong with the file name ")

        rem_file.unlink()


# nai nanai nai nai nai nai nanai nai nai nai nanai nai nai nai https://youtu.be/PR6SYEK7tD8?t=134

if __name__ == "__main__":
    unittest.main()
