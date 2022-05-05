"""Tests if the NDigitsManagement is working as expected

---> Class Test_get_language
    This class tests if the method get_language is working as expected, testing the default value ('en') and when the language is changed to 'pt-br'

---> Class Test_set_language
    This class tests if the method set_language is working as expected, testing if it raise ValueError when a not valid language is passed, and if it changes the values whan pt-br is passed.

---> Class Test_init
    This class tests if the method init is working as expected, testing if the default value is 4 and if a change to 3 in fact changes the value

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/helpers/test_NDigitsManagement.py
    or
    python -m unittest -b tests/utils/helpers/test_NDigitsManagement.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from cup_of_coffee.utils.helpers import NDigitsManagement
os.system("cls")


class Test_init(unittest.TestCase):

    def test_set_to_3(self):
        teste = NDigitsManagement(3)
        self.assertEqual(teste.n_digits, 3, msg="The n_digits is 3")

    def test_default(self):
        teste = NDigitsManagement()
        self.assertEqual(teste.n_digits, 4, msg="The default n_digits is not 4")

class Test_set_n_digits(unittest.TestCase):

    def test_set_5(self):
        teste = NDigitsManagement()
        teste.set_n_digits(5)
        self.assertEqual(teste.n_digits, 5, msg="The n_digits is not 5")



class Test_get_n_digits(unittest.TestCase):

    def test_default(self):
        teste = NDigitsManagement()
        result = teste.get_n_digits()
        self.assertEqual(result, 4, msg="The default n_digits is not 4")

    def test_1(self):
        teste = NDigitsManagement()
        teste.set_n_digits(1)
        result = teste.get_n_digits()
        self.assertEqual(result, 1, msg="The n_digits is not 1")






#

if __name__ == "__main__":
    unittest.main()
