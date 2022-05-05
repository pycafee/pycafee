"""Tests if the _truncate is working as expected

---> Class Test_truncate
    This class tests if the value was truncated correctly. It tests for value with type = int and value with type = float. Also tests for decs integer or None, and with decs higher than value total of decimal cases.


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/helpers/test__truncate.py
    or
    python -m unittest -b tests/utils/helpers/test__truncate.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from cup_of_coffee.utils.helpers import _truncate
os.system("cls")

class Test_truncate(unittest.TestCase):

    def test_value_int_None(self):
        result = _truncate(1, 'en', None)
        self.assertEqual(result, 1, msg="Changing the value if value = 1 and decs = None")

    def test_value_None_10(self):
        result = _truncate(None, 'en', 10)
        self.assertEqual(result, None, msg="Changing the value if value = None and decs = 10")

    def test_value_int_10(self):
        result = _truncate(1, 'en', 10)
        self.assertEqual(result, 1, msg="Changing the value if value = 1 and decs = 10")

    def test_value_float_None(self):
        result = _truncate(0.51561, 'en', None)
        self.assertEqual(result, 0.51561, msg="Changing the value if value = 0.51561 and decs = None")

    def test_value_float_decs(self):
        result = _truncate(0.51561, 'en', 1)
        self.assertEqual(result, 0.5, msg="Error truncating the value = 0.51561 with decs = 1")

        result = _truncate(0.948611561, 'en', 5)
        self.assertEqual(result, 0.94861, msg="Error truncating the value = 0.948611561 with decs = 5")

    def test_value_float_decs_higher(self):
        result = _truncate(0.948611561, 'en', 10)
        self.assertEqual(result, 0.948611561, msg="Error truncating the value = 0.948611561 with decs = 10")


# Hey lady, are you going up or da-da-da-da-da-down? https://youtu.be/wHOY7n35eNw?t=18
if __name__ == "__main__":
    unittest.main()
