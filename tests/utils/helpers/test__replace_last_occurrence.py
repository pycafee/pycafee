"""Tests if the _replace_last_occurrence is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_replace_last_occurrence
    This class tests if None is passed to _change_locale_back_to_default nothing happens. Raises ValueError when locale is not acceptable and when the decimal separator is not available.

    Needs more tests


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/helpers/test__replace_last_occurrence.py
    or
    python -m unittest -b tests/utils/helpers/test__replace_last_occurrence.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.utils.helpers import _replace_last_occurrence
os.system('cls')

class Test_replace_last_occurrence(unittest.TestCase):


    def test_pass(self):
        result = _replace_last_occurrence('100.000.00', '.', ',', 0)
        self.assertEqual(result, '100.000.00', msg="Not working")

        result = _replace_last_occurrence('100.000.00', '.', '|', 0)
        self.assertEqual(result, '100.000.00', msg="Not working")

        result = _replace_last_occurrence('100.000.00', '.', ',', 1)
        self.assertEqual(result, '100.000,00', msg="Not working")

        result = _replace_last_occurrence('100.000.00', '.', '|', 1)
        self.assertEqual(result, '100.000|00', msg="Not working")

        result = _replace_last_occurrence('100.000.00', '.', ',', 2)
        self.assertEqual(result, '100,000,00', msg="Not working")

        result = _replace_last_occurrence('100.000.00', '.', '|', 2)
        self.assertEqual(result, '100|000|00', msg="Not working")

        result = _replace_last_occurrence('100.000.00', '.', '|', 3)
        self.assertEqual(result, '100|000|00', msg="Not working")

        result = _replace_last_occurrence('100.000,00', '.', ',', 1)
        self.assertEqual(result, '100,000,00', msg="Not working")

#  When no one is around you, Say: Baby, I love you.. If you ain't runnin' game  https://youtu.be/9YZXPs8uAB0?t=158

if __name__ == "__main__":
    unittest.main()
