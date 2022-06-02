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
from pycafee.utils.helpers import _check_conflicting_filename
from pathlib import Path
import csv
import sys
import io
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
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        exists, teste = _check_conflicting_filename('bawitdaba', "txt", 'en')
        self.assertFalse(exists, msg="The file existis when it should not")
        self.assertEqual(teste, "bawitdaba.txt", msg="The file existis when it should not")
        sys.stdout = sys.__stdout__
        expected = ""
        result = False
        if expected == capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="Something wrong on the output when file does exists")

    def test_file_already_exits(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        exists, teste = _check_conflicting_filename('bawitdaba', "csv", 'en')
        self.assertTrue(exists, msg="The does not existis when it should")
        self.assertEqual(teste, "bawitdaba_1.csv", msg="The is something wrong with the file name ")
        sys.stdout = sys.__stdout__
        expected_output = ["UserWarning",
                    "The 'bawitdaba.csv' file already exists in the current directory",
                    "The file was exported as 'bawitdaba_1.csv'"]
        for expected in expected_output:
            result = False
            if expected in capturedOutput.getvalue():
                result = True
            self.assertTrue(result, msg="Something wrong on the output when file already exists")


    def test_file_already_exits_again(self):
        nome = "bawitdaba_1.csv"
        with open(nome, 'w', newline='') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow([1,2,3])
        rem_file = Path(nome)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        exists, teste = _check_conflicting_filename('bawitdaba', "csv", 'en')
        self.assertTrue(exists, msg="The does not existis when it should")
        self.assertEqual(teste, "bawitdaba_2.csv", msg="The is something wrong with the file name ")
        rem_file.unlink()
        sys.stdout = sys.__stdout__
        expected_output = ["UserWarning",
                    "The 'bawitdaba.csv' file already exists in the current directory",
                    "The file was exported as 'bawitdaba_2.csv'"]
        for expected in expected_output:
            result = False
            if expected in capturedOutput.getvalue():
                result = True
            self.assertTrue(result, msg="Something wrong on the output when file already exists")


# nai nanai nai nai nai nai nanai nai nai nai nanai nai nai nai https://youtu.be/PR6SYEK7tD8?t=134

if __name__ == "__main__":
    unittest.main()
