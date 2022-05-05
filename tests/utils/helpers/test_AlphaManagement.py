"""Tests if the AlphaManagement is working as expected

---> Class Test_get_alfa
    This class tests if the method get_alfa is working as expected, testing the default value (0.05) and when the alfa is changed to '0.01'

---> Class Test_set_alfa
    This class tests if the method set_alfa is working as expected, testing if it sets the alfa value to 0.1

---> Class Test_init
    This class tests if the method init is working as expected, testing if the default value is 0.05 and if changing it to 0.10 works

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/helpers/test_AlphaManagement.py
    or
    python -m unittest -b tests/utils/helpers/test_AlphaManagement.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.utils.helpers import AlphaManagement
os.system("cls")


class Test_init(unittest.TestCase):

    def test_set_to_0_1(self):
        teste = AlphaManagement(0.1)
        self.assertEqual(teste.alfa, 0.1, msg="Alfa is not 0.1")

    def test_default(self):
        teste = AlphaManagement()
        self.assertEqual(teste.alfa, 0.05, msg="default alfa is not 0.05")

class Test_set_alfa(unittest.TestCase):

    def test_set_to_0_1(self):
        teste = AlphaManagement()
        teste.set_alfa(0.1)
        self.assertEqual(teste.alfa, 0.1, msg="Did not changed alfa the 0.1")



class Test_get_alfa(unittest.TestCase):

    def test_default(self):
        teste = AlphaManagement()
        result = teste.get_alfa()
        self.assertEqual(result, 0.05, msg="The default alfa is not 0.05")

    def test_pt_br(self):
        teste = AlphaManagement()
        teste.set_alfa(0.01)
        result = teste.get_alfa()
        self.assertEqual(result, 0.01, msg="The get alfa returned wrong value")






#  atatata taata taatatata zukkyun  https://youtu.be/RmcuyI5CndQ?t=54

if __name__ == "__main__":
    unittest.main()
