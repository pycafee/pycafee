"""Tests if the _raises_when_fit_was_not_applied is working as expected

--------------------------------------------------------------------------------
Description:

---> Class Test_raises_when_fit_was_not_applied. The function is tested everywhere it was added.


    Needs more tests


--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/utils/helpers/test__raises_when_fit_was_not_applied.py
    or
    python -m unittest -b tests/utils/helpers/test__raises_when_fit_was_not_applied.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.utils.helpers import _raises_when_fit_was_not_applied
from pycafee.sample.sample import Sample
import numpy as np
os.system('cls')

class Test_raises_when_fit_was_not_applied(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])

    def test_normality_check(self):
        with self.assertRaises(ValueError, msg="Does not raised error when the fit was not done"):
            amostra = Sample("amostra")
            res = amostra.normality_check(show=True)

    def test_summary(self):
        with self.assertRaises(ValueError, msg="Does not raised error when the fit was not done"):
            amostra = Sample("amostraas")
            res = amostra.summary(show=True)

    def test_standard_interval(self):
        with self.assertRaises(ValueError, msg="Does not raised error when the fit was not done"):
            amostra = Sample("amostraas")
            res = amostra.standard_interval(show=True)

    def test_standard_interval(self):
        with self.assertRaises(ValueError, msg="Does not raised error when the fit was not done"):
            amostra = Sample("amostraas")
            res = amostra.standard_interval(show=True)

    def test_confidencial_interval(self):
        with self.assertRaises(ValueError, msg="Does not raised error when the fit was not done"):
            amostra = Sample("amostraas")
            res = amostra.confidencial_interval(show=True)

    def test_positional_summary(self):
        with self.assertRaises(ValueError, msg="Does not raised error when the fit was not done"):
            amostra = Sample("amostraas")
            res = amostra.positional_summary(show=True)


#  When no one is around you, Say: Baby, I love you.. If you ain't runnin' game  https://youtu.be/9YZXPs8uAB0?t=158

if __name__ == "__main__":
    unittest.main()
