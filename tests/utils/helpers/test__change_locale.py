"""Tests if the _change_locale is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_change_locale
    This class tests if None is passed to _change_locale_back_to_default nothing happens. Raises ValueError when locale is not acceptable and when the decimal separator is not available.

    Needs more tests


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/helpers/test__change_locale.py
    or
    python -m unittest -b tests/utils/helpers/test__change_locale.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.utils.helpers import _change_locale
import locale
os.system('cls')

class Test_change_locale(unittest.TestCase):

    def test_wrong_decimal_separator(self):
        with self.assertRaises(ValueError, msg="Does not raised error when wrong value was passed"):
            _change_locale(decimal_separator=";", local="pt_BR", language='en')

    def test_wrong_local(self):
        with self.assertRaises(locale.Error, msg="Does not locale.Error when wrong locale was passed"):
            _change_locale(decimal_separator=",", local="pt_R", language='en')

    def test_pass(self):
        result = _change_locale(language='en')
        self.assertEqual(result, None, msg="Does nothing when default values")

        result = _change_locale(decimal_separator=",", language='en')
        self.assertEqual(result, "pt_BR", msg="Does nothing when default values")


#  When no one is around you, Say: Baby, I love you.. If you ain't runnin' game  https://youtu.be/9YZXPs8uAB0?t=158

if __name__ == "__main__":
    unittest.main()
