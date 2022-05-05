"""Tests if the _check_is_data_frame is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_check_is_data_frame
    This class tests if the input is a DataFrame and if the DataFrame is not empty. It also to test if the df is valid with assertTrue


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/checkers/test__check_is_data_frame.py
    or
    python -m unittest -b tests/utils/checkers/test__check_is_data_frame.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.utils.checkers import _check_is_data_frame
import pandas as pd
os.system('cls')

class Test_check_is_data_frame(unittest.TestCase):

    def test_is_not_dataframe(self):
        with self.assertRaises(ValueError, msg="Does not raised error when type(df) != df.DataFrame"):
            _check_is_data_frame(1, param_name="df", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when type(df) != df.DataFrame"):
            _check_is_data_frame("!", param_name="df", language='en')
        with self.assertRaises(ValueError, msg="Does not raised error when type(df) != df.DataFrame"):
            _check_is_data_frame([1], param_name="df", language='en')

    def test_is_missing_input(self):
        with self.assertRaises(TypeError, msg="Does not raised error when the dataframe is empty"):
            df = pd.DataFrame(param_name="df")
            _check_is_data_frame(df, param_name="df", language='en')

    def test_pass(self):
        df = pd.DataFrame(columns=["a", 'b'])
        df["a"] = [1, 2]
        df["b"] = [3, 4]
        result = _check_is_data_frame(df, param_name="df", language='en')
        self.assertTrue(result, msg = "Returning False when the input is a DataFrame")



if __name__ == "__main__":
    unittest.main()
