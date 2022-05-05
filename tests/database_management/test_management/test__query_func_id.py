"""Tests if the _query_func_id is working as expected

--------------------------------------------------------------------------------
Description:

---> Class_query_func_ids. This checks if the result is int and if a not found function has text



--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/database_management/test_management/test__query_func_id.py
    or
    python -m unittest -b tests/database_management/test_management/test__query_func_id.py

--------------------------------------------------------------------------------
"""
import os
import unittest
from cup_of_coffee.database_management.management import _query_func_id
os.system('cls')

class Test_query_func_id(unittest.TestCase):

    def test_query_func_id_type(self):
        result = _query_func_id('shapiro_wilk')
        self.assertIsInstance(result, int, "O id da função não é do tipo int")

    def test_query_func_id(self):
        with self.assertRaises(ValueError, msg="Por algum motivo, a função amo_isso existe e tem um id!"):
            _query_func_id('shopiro_wilk')










if __name__ == "__main__":
    unittest.main()
