"""Tests if the _connecting_to_database is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test__connecting_to_database. This class checks if the connection with the database is correctly stabelished



--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/database_management/test_management/test__connecting_to_database.py
    or
    python -m unittest -b tests/database_management/test_management/test__connecting_to_database.py

--------------------------------------------------------------------------------
"""
import os
import unittest
import sqlite3
from pycafee.database_management.management import _connecting_to_database
os.system('cls')

class TestDatabaseConnection(unittest.TestCase):

    def test__connecting_to_database_return(self):
        _cursor, _connection = _connecting_to_database()
        self.assertIsInstance(_cursor, sqlite3.Cursor, "The '_cursor' is not of type 'sqlite3.Cursor'")
        self.assertIsInstance(_connection, sqlite3.Connection, "The '_connection' is not of type 'sqlite3.connection'")

    def test__connecting_to_database_exists(self):
        with self.assertRaises(FileNotFoundError, msg="For some reason the database 'a.db' exists."):
            _connecting_to_database("a.db")

    def test__connecting_to_database_input_size(self):
        with self.assertRaises(ValueError, msg="O tamanho do input não é suficiente"):
            _connecting_to_database("a")

    def test__connecting_to_database_input_type(self):
        with self.assertRaises(ValueError, msg="Por algum motivo, o nome passado é um int"):
            _connecting_to_database(1)

        with self.assertRaises(ValueError, msg="Por algum motivo, o nome passado é um float"):
            _connecting_to_database(1.1)

        with self.assertRaises(ValueError, msg="Por algum motivo, o nome passado é uma lista"):
            _connecting_to_database([1.1])

        with self.assertRaises(ValueError, msg="Por algum motivo, o nome passado é uma tupla"):
            _connecting_to_database((1.1,))

        with self.assertRaises(ValueError, msg="Por algum motivo, o nome passado é um dicionário"):
            _connecting_to_database({1: 'a.db'})





if __name__ == "__main__":
    unittest.main()
