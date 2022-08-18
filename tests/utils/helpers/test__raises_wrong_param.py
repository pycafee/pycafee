"""Tests if the _raises_wrong_param is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_raises_wrong_param.





--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/helpers/test__raises_wrong_param.py
    or
    python -m unittest -b tests/utils/helpers/test__raises_wrong_param.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.utils.helpers import _raises_wrong_param
import io
import sys
os.system('cls')

class Test__raises_wrong_param(unittest.TestCase):



    def test_pass(self):
        param_name = "nome"
        alloweds = ["a", "b", "c", "d"]
        param_value = "a"
        language = "en"
        result = _raises_wrong_param(param_name, alloweds, param_value, language)
        self.assertEqual(result, True, msg="output not True")
        self.assertIsInstance(result, bool, msg="output not True")

    #
    def test_raises(self):
        with self.assertRaises(ValueError, msg="Does not raised error when param_value is not in alloweds"):
            param_name = "nome"
            alloweds = ["a", "b", "c", "d"]
            param_value = "e"
            language = "en"
            result = _raises_wrong_param(param_name, alloweds, param_value, language)


        with self.assertRaises(ValueError, msg="Does not raised error when param_value is not in alloweds"):
            param_name = "nome"
            alloweds = [0, 2]
            param_value = 1
            language = "pt-br"
            result = _raises_wrong_param(param_name, alloweds, param_value, language)



    def test_raise_output(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            param_name = "nome"
            alloweds = ["a", "b", "c", "d"]
            param_value = "e"
            language = "en"
            result = _raises_wrong_param(param_name, alloweds, param_value, language)
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "The 'nome' parameter only accepts"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        #################

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            param_name = "nome"
            alloweds = [0, 2]
            param_value = 1
            language = "pt-br"
            result = _raises_wrong_param(param_name, alloweds, param_value, language)
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "O parâmetro 'nome' aceita"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        #################





#  When no one is around you, Say: Baby, I love you.. If you ain't runnin' game  https://youtu.be/9YZXPs8uAB0?t=158

if __name__ == "__main__":
    unittest.main()
