"""Tests if the _check_figure_extension is working as expected

---> Class Test_check_figure_extension
    # This class tests if the input has a forbidden character. The current forbidden characters are:
    #     ["/", "<", ">", ":", "\"", "\\", "|", "?", "*", ".", ",", "[", "]", ";"]
    # All characters are randomly tested.


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/helpers/test__check_figure_extension.py
    or
    python -m unittest -b tests/utils/helpers/test__check_figure_extension.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from cup_of_coffee.utils.helpers import _check_figure_extension
os.system('cls')

class Test_sep_checker(unittest.TestCase):

    def test_fail(self):
        with self.assertRaises(ValueError, msg=f"Does not raised error when the the extension is wrong"):
            _check_figure_extension("file_name", param_name="param", language="en")


    def test_pass(self):
        result = _check_figure_extension("png", param_name="param", language="en")
        self.assertTrue(result, msg = "Something unexpected happened")





# saikyou de saikou tte chou dou da iuno wa (pa pa pa pa pa pa pa pa ya) https://youtu.be/j246TQ5pBcQ?t=79

if __name__ == "__main__":
    unittest.main()
