"""Tests if the _flat_list_of_lists is working as expected

---> Class Test_flat_list_of_lists
    This class tests if the result of _flat_list_of_lists() is a flattened list.

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/helpers/test__flat_list_of_lists.py
    or
    python -m unittest -b tests/utils/helpers/test__flat_list_of_lists.py


--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.utils.helpers import _flat_list_of_lists
import numpy as np
os.system('cls')

class Test_flat_list_of_lists(unittest.TestCase):

    def test_error(self):
        with self.assertRaises(ValueError, msg="Does not raised error when a inner element is not a list"):
            _flat_list_of_lists([1, 2, 3], param_name="parameter", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when a inner element is not a list"):
            _flat_list_of_lists([1, 2, [3]], param_name="parameter", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when a inner element is not a list"):
            _flat_list_of_lists([1, [2,2], [3]], param_name="parameter", language='en')


    def test_pass(self):
        result = _flat_list_of_lists([[1], [2,3], [3]], param_name="parameter", language='en')
        self.assertEqual(result, [1, 2, 3, 3], msg = "An error was raised when the result was a flat list")






# kimi ni kikoete iru ka? kokoro no koe https://youtu.be/7idcgZGHCjM?t=97

if __name__ == "__main__":
    unittest.main()
