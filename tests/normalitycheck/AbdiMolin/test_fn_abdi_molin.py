"""Tests if the fn_abdi_molin is working as expected

---> Class Test_fn_abdi_molin. This just checks a value. Nothing especial here



--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/normalitycheck/AbdiMolin/test_fn_abdi_molin.py
    or
    python -m unittest -b tests/normalitycheck/AbdiMolin/test_fn_abdi_molin.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.normalitycheck.abdimolin import AbdiMolin
os.system("cls")

class Test_fn_abdi_molin(unittest.TestCase):

    def test_pass(self):
        test = AbdiMolin()
        result = test.fn_abdi_molin(54)
        self.assertEqual(result, 7.451417922044536, msg="Opss")




# Vou consertar o seu mau carater no tapaaaaaaaaa
if __name__ == "__main__":
    unittest.main()
