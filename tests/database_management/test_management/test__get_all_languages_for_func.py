"""Tests if the _get_all_languages_for_func is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test__get_all_languages_for_func. This function check which language a func has info on the database



--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/database_management/test_management/test__get_all_languages_for_func.py
    or
    python -m unittest -b tests/database_management/test_management/test__get_all_languages_for_func.py

--------------------------------------------------------------------------------
"""
import os
import unittest
from cup_of_coffee.database_management.management import _get_all_languages_for_func
os.system('cls')

class Test_get_all_languages_for_func(unittest.TestCase):

    def test_input_string(self):
        with self.assertRaises(ValueError, msg="Not raising error when input is not a string"):
            _get_all_languages_for_func(1)
        with self.assertRaises(ValueError, msg="Not raising error when input is not a string"):
            _get_all_languages_for_func([1])
        with self.assertRaises(ValueError, msg="Not raising error when input is not a string"):
            _get_all_languages_for_func(1.0)


    def test__get_all_languages_for_func_en(self):
        result = _get_all_languages_for_func('shapiro_wilk')
        self.assertIn('en', result.keys())

    def test_get_all_languages_for_func_pt_br(self):
        result = _get_all_languages_for_func('shapiro_wilk')
        self.assertIn('pt-br', result.keys())


    def test_get_all_languages_for_func_wrong_name(self):
        with self.assertRaises(ValueError, msg="Por algum motivo, a função shopiro_wilk existe e tem um id!"):
            _get_all_languages_for_func('shopiro_wilk')








if __name__ == "__main__":
    unittest.main()
