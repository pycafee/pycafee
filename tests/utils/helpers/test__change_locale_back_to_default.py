"""Tests if the _change_locale_back_to_default is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_change_locale_back_to_default
    This class tests if None is passed to _change_locale_back_to_default nothing happens.

    Needs more tests


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/helpers/test__change_locale_back_to_default.py
    or
    python -m unittest -b tests/utils/helpers/test__change_locale_back_to_default.py


--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.utils.helpers import _change_locale_back_to_default
os.system('cls')

class Test_change_locale_back_to_default(unittest.TestCase):

    def test_pass(self):
        try:
            _change_locale_back_to_default(None)
            result = True
        except:
            result = False
        self.assertTrue(result, msg="Does not True when None")





if __name__ == "__main__":
    unittest.main()
