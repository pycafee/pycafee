"""Tests if the _get_messages is working as expected

--------------------------------------------------------------------------------
Description:

---> Class _get_messages. This checks if the messages are been get



--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/database_management/test_management/test__get_messages.py
    or
    python -m unittest -b tests/database_management/test_management/test__get_messages.py

--------------------------------------------------------------------------------
"""
import os
import unittest
import sqlite3
from collections import defaultdict
from cup_of_coffee.database_management.management import _get_messages
os.system('cls')

class Test__get_messages(unittest.TestCase):

    def test_is_defaultdict(self):
        result = _get_messages(1, 'en', func_name='shapiro_wilk')
        self.assertIsInstance(result, defaultdict, "The output is not a defaultdict")




if __name__ == "__main__":
    unittest.main()
