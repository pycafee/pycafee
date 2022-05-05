"""Tests if the _check_forbidden_character is working as expected

---> Class Test_check_forbidden_character
    This class tests if the input has a forbidden character. The current forbidden characters are:
        ["/", "<", ">", ":", "\"", "\\", "|", "?", "*", ".", ",", "[", "]", ";"]
    All characters are randomly tested.


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/helpers/test__check_forbidden_character.py
    or
    python -m unittest -b tests/utils/helpers/test__check_forbidden_character.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.utils.helpers import _check_forbidden_character
import string
import random
os.system('cls')

class Test_sep_checker(unittest.TestCase):

    def test_empty_string(self):
        lista = ["/", "<", ">", ":", "\"", "\\", "|", "?", "*", ".", ",", "[", "]", ";"]
        for character in lista:
            size = random.randint(3,8)
            file_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=size))
            insert = random.randint(0,size)
            file_name = file_name[:insert] + character + file_name[insert:]
            print(file_name)
            with self.assertRaises(ValueError, msg=f"Does not raised error when the {character} forbidden character was used"):
                _check_forbidden_character(file_name, "param", 'en')


    def test_pass(self):
        try:
            _check_forbidden_character("name", "param", 'en')
            result = True
        except:
            result = False
        self.assertTrue(result, msg = "Something unexpected happened")


if __name__ == "__main__":
    unittest.main()
