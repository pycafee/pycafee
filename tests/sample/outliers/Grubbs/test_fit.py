"""Tests if the test_fit is working as expected

---> Class Test_raises: This class checks if the fit method is raising ValueError when it should. Tests are made for details, kind, which and alfa parameter

---> Class Test_details: This class checks the conclusion parameter for different details option. data with and without outlier are tested

---> Class Test_three: This checks the results for cases where kind equals to three

---> Class Test_two: This checks the results for cases where kind equals to two

---> Class Test_one: This checks the results for cases where kind equals to one

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/sample/outliers/Grubbs/test_fit.py
    or
    python -m unittest -b tests/sample/outliers/Grubbs/test_fit.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from pycafee.sample.outliers import Grubbs
import numpy as np
import sys
import io
os.system('cls')



class Test_details(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.x = np.array([15.52, 15.53, 15.53, 15.54, 15.56, 15.56]) # sem outliers
        cls.y = np.array([15.52, 15.53, 15.53, 15.54, 15.56, 15.56, 16]) # outlier superior
        cls.z = np.array([15, 15.52, 15.53, 15.53, 15.54, 15.56, 15.56]) # outlier inferior
        cls.w = np.array([14, 15.52, 15.53, 15.53, 15.54, 15.56, 15.56, 17]) # outliers nos dois lados

    def test_details_short(self):
        teste = Grubbs()
        result, conclusion = teste.fit(self.x, kind="one", details="short")
        result = False
        if "does not have outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.x, kind="one", details="short", which="max")
        result = False
        if "does not have outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.x, kind="one", details="short", which="min")
        result = False
        if "does not have outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Grubbs()
        result, conclusion = teste.fit(self.x, kind="two", details="short")
        result = False
        if "does not have outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs(language="pt-br")
        result, conclusion = teste.fit(self.x, kind="two", details="short")
        result = False
        if "não contém outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Grubbs()
        result, conclusion = teste.fit(self.x, kind="three", details="short")
        result = False
        if "does not have outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.x, kind="three", details="short", which="max")
        result = False
        if "does not have outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.x, kind="three", details="short", which="min")
        result = False
        if "does not have outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")




        teste = Grubbs()
        result, conclusion = teste.fit(self.y, kind="one", details="short")
        result = False
        if "sample 16.0 perhaps be an outlier" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.y, kind="one", details="short", which="max")
        result = False
        if "sample 16.0 perhaps be an outlier" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.y, kind="one", details="short", which="min")
        result = False
        if "does not have outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.y, kind="three", details="short")
        result = False
        if "15.56 and 16.0 may be outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.y, kind="three", details="short", which="max")
        result = False
        if "15.56 and 16.0 may be outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.y, kind="three", details="short", which="min")
        result = False
        if "does not have outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Grubbs()
        result, conclusion = teste.fit(self.z, kind="one", details="short")
        result = False
        if "sample 15.0 perhaps be an outlier" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.z, kind="one", details="short", which="max")
        result = False
        if "does not have outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.z, kind="one", details="short", which="min")
        result = False
        if "sample 15.0 perhaps be an outlier" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.z, kind="three", details="short")
        result = False
        if "15.0 and 15.52 may be outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.z, kind="three", details="short", which="max")
        result = False
        if "does not have outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.z, kind="three", details="short", which="min")
        result = False
        if "15.0 and 15.52 may be outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")



        teste = Grubbs()
        result, conclusion = teste.fit(self.w, kind="two", details="short")
        result = False
        if "14.0 and 17.0 may be outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs(language='pt-br')
        result, conclusion = teste.fit(self.w, kind="two", details="short")
        result = False
        if "14.0 e 17.0 talvez sejam outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")



    def test_details_full(self):
        teste = Grubbs()
        result, conclusion = teste.fit(self.x, kind="one", details="full")
        result = False
        if "we have no evidence to reject the null hypothesis" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.x, kind="one", details="full", which="max")
        result = False
        if "we have no evidence to reject the null hypothesis" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.x, kind="one", details="full", which="min")
        result = False
        if "we have no evidence to reject the null hypothesis" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")



        teste = Grubbs()
        result, conclusion = teste.fit(self.x, kind="two", details="full")
        result = False
        if "we have no evidence to reject the null hypothesis" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs(language='pt-br')
        result, conclusion = teste.fit(self.x, kind="two", details="full")
        result = False
        if "não temos evidências para rejeitar a hipótese nula" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")



        teste = Grubbs()
        result, conclusion = teste.fit(self.x, kind="three", details="full")
        result = False
        if "we have no evidence to reject the null hypothesis" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.x, kind="three", details="full", which="max")
        result = False
        if "we have no evidence to reject the null hypothesis" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.x, kind="three", details="full", which="min")
        result = False
        if "we have no evidence to reject the null hypothesis" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")





        teste = Grubbs()
        result, conclusion = teste.fit(self.y, kind="one", details="full")
        result = False
        if "(2.259) is higher than the critical value (2.02), we have evidence to reject the null hypothesis, and perhaps sample 16.0" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.y, kind="one", details="full", which="max")
        result = False
        if "(2.259) is higher than the critical value (2.02), we have evidence to reject the null hypothesis, and perhaps sample 16.0" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.y, kind="one", details="full", which="min")
        result = False
        if "we have no evidence to reject the null hypothesis" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.y, kind="three", details="full")
        result = False
        if "statistic (0.005) is lower than the critical value (0.07), we have evidence" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.y, kind="three", details="full", which="max")
        result = False
        if "statistic (0.005) is lower than the critical value (0.07), we have evidence" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.y, kind="three", details="full", which="min")
        result = False
        if "we have no evidence to reject the null hypothesis" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")



        teste = Grubbs()
        result, conclusion = teste.fit(self.z, kind="one", details="full")
        result = False
        if "(2.261) is higher than the critical value (2.02), we have evidence to reject the null hypothesis" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.z, kind="one", details="full", which="max")
        result = False
        if "we have no evidence to reject the null hypothesis" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.z, kind="one", details="full", which="min")
        result = False
        if "(2.261) is higher than the critical value (2.02), we have evidence to reject the null hypothesis" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.z, kind="three", details="full")
        result = False
        if "test statistic (0.003) is lower than the critical value (0.07), we have evidence to reject the null hypothesis" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.z, kind="three", details="full", which="max")
        result = False
        if "we have no evidence to reject the null hypothesis" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.z, kind="three", details="full", which="min")
        result = False
        if "test statistic (0.003) is lower than the critical value (0.07), we have evidence to reject the null hypothesis" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Grubbs()
        result, conclusion = teste.fit(self.w, kind="two", details="full")
        result = False
        if "statistic (3.74) is higher than the critical value (3.399), we have evidence to reject the null hypothesis, and perhaps samples 14.0 and 17.0 " in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

        teste = Grubbs(language='pt-br')
        result, conclusion = teste.fit(self.w, kind="two", details="full")
        result = False
        if "teste (3.74) é maior do que o valor crítico (3.399), temos evidências para rejeitar a hipótese nula, e talvez as amostras 14.0 e 17.0 " in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")



    def test_details_binary(self):
        teste = Grubbs()
        result, conclusion = teste.fit(self.x, kind="one", details="binary")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.x, kind="one", details="binary", which="max")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.x, kind="one", details="binary", which="min")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.x, kind="two", details="binary")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.x, kind="three", details="binary")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.x, kind="three", details="binary", which="max")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.x, kind="three", details="binary", which="min")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")


        teste = Grubbs()
        result, conclusion = teste.fit(self.y, kind="one", details="binary")
        self.assertEqual(conclusion, 1, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.y, kind="one", details="binary", which="max")
        self.assertEqual(conclusion, 1, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.y, kind="one", details="binary", which="min")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.y, kind="three", details="binary")
        self.assertEqual(conclusion, 1, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.y, kind="three", details="binary", which="max")
        self.assertEqual(conclusion, 1, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.y, kind="three", details="binary", which="min")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")


        teste = Grubbs()
        result, conclusion = teste.fit(self.z, kind="one", details="binary")
        self.assertEqual(conclusion, 1, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.z, kind="one", details="binary", which="max")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.z, kind="one", details="binary", which="min")
        self.assertEqual(conclusion, 1, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.z, kind="three", details="binary")
        self.assertEqual(conclusion, 1, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.z, kind="three", details="binary", which="max")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")

        teste = Grubbs()
        result, conclusion = teste.fit(self.z, kind="three", details="binary", which="min")
        self.assertEqual(conclusion, 1, msg="wrong conclusion")


        teste = Grubbs()
        result, conclusion = teste.fit(self.w, kind="two", details="binary")
        self.assertEqual(conclusion, 1, msg="wrong conclusion")

        teste = Grubbs(language='pt-br')
        result, conclusion = teste.fit(self.w, kind="two", details="binary")
        self.assertEqual(conclusion, 1, msg="wrong conclusion")



class Test_raises(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.x = np.array([15.52, 15.53, 15.53, 15.54, 15.56, 15.56]) # sem outliers


    def test_details(self):
        with self.assertRaises(ValueError, msg="Does not raised error when details is wrong"):
            teste = Grubbs()
            result, conclusion = teste.fit(self.x, details="a")
        with self.assertRaises(ValueError, msg="Does not raised error when details is wrong"):
            teste = Grubbs()
            result, conclusion = teste.fit(self.x, details=1)


    def test_details_output(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            teste = Grubbs()
            result, conclusion = teste.fit(self.x, details="a")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "a"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        ###############
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            teste = Grubbs()
            result, conclusion = teste.fit(self.x, details=1)
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "int"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        ###############


    def test_kind_raises(self):
        with self.assertRaises(ValueError, msg="Does not raised error when kind is wrong"):
            teste = Grubbs()
            result, conclusion = teste.fit(self.x, kind="a")


    def test_kind_raises_output(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            teste = Grubbs()
            result, conclusion = teste.fit(self.x, kind="a")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "a"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        ###############


    def test_which_raises(self):
        with self.assertRaises(ValueError, msg="Does not raised error when which is wrong"):
            teste = Grubbs()
            result, conclusion = teste.fit(self.x, which="a")


    def test_which_raises_output(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            teste = Grubbs()
            result, conclusion = teste.fit(self.x, which="a")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "a"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")

        ###############


    def test_alfa_raises(self):
        with self.assertRaises(ValueError, msg="Does not raised error when alfa not allowed"):
            teste = Grubbs()
            result = teste.fit(self.x, alfa=0.02)

        with self.assertRaises(ValueError, msg="Does not raised error when alfa is str"):
            teste = Grubbs()
            result = teste.fit(self.x, alfa="0.02")


    def test_alfa_raises_output(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        try:
            teste = Grubbs()
            result = teste.fit(self.x, alfa="0.02")
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        expected = "str"
        result = False
        if expected in capturedOutput.getvalue():
            result = True
        self.assertTrue(result, msg="wrong output when Raising Error")


class Test_three(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.x = np.array([15.52, 15.53, 15.53, 15.54, 15.56, 15.56]) # sem outliers
        cls.y = np.array([159, 153, 184, 153, 156, 150, 147]) # book
        cls.z = np.array([9, 16, 23, 41, 44, 46, 80])
        cls.w = np.array([15.42, 15.51, 15.52, 15.52, 15.53, 15.53, 15.54, 15.56, 15.56, 15.68])



    def test_data2(self):
        teste = Grubbs()
        result, conclusion = teste.fit(self.w, kind="three")
        self.assertAlmostEqual(result[0], 0.332900847, places=7, msg="wrong statistic")
        self.assertAlmostEqual(result[1], 0.1864, places=3, msg="wrong critical")
        self.assertEqual(result[2], 0.05, msg="wrong alpha")
        self.assertEqual(result[3], "three", msg="wrong kind")
        self.assertEqual(result[4][0], 15.56, msg="wrong outlier")
        self.assertEqual(result[4][1], 15.68, msg="wrong outlier")
        result = False
        if "does not have outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Grubbs()
        result, conclusion = teste.fit(self.w, kind="three", which="min")
        self.assertAlmostEqual(result[0], 0.535372849, places=7, msg="wrong statistic")
        self.assertAlmostEqual(result[1], 0.1864, places=3, msg="wrong critical")
        self.assertEqual(result[2], 0.05, msg="wrong alpha")
        self.assertEqual(result[3], "three", msg="wrong kind")
        self.assertEqual(result[4][0], 15.42, msg="wrong outlier")
        self.assertEqual(result[4][1], 15.51, msg="wrong outlier")
        result = False
        if "does not have outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")



    def test_data1(self):
        teste = Grubbs()
        result, conclusion = teste.fit(self.z, kind="three")
        self.assertAlmostEqual(result[0], 0.276697892, places=7, msg="wrong statistic")
        self.assertAlmostEqual(result[1], 0.0708, places=3, msg="wrong critical")
        self.assertEqual(result[2], 0.05, msg="wrong alpha")
        self.assertEqual(result[3], "three", msg="wrong kind")
        self.assertEqual(result[4][0], 46, msg="wrong outlier")
        self.assertEqual(result[4][1], 80, msg="wrong outlier")
        result = False
        if "does not have outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Grubbs()
        result, conclusion = teste.fit(self.z, kind="three", which="min")
        self.assertAlmostEqual(result[0], 0.500819672, places=7, msg="wrong statistic")
        self.assertAlmostEqual(result[1], 0.0708, places=3, msg="wrong critical")
        self.assertEqual(result[2], 0.05, msg="wrong alpha")
        self.assertEqual(result[3], "three", msg="wrong kind")
        self.assertEqual(result[4][0], 9, msg="wrong outlier")
        self.assertEqual(result[4][1], 16, msg="wrong outlier")
        result = False
        if "does not have outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")



    def test_book(self):
        teste = Grubbs()
        result, conclusion = teste.fit(self.y, kind="three")
        self.assertAlmostEqual(result[0], 0.051, places=3, msg="wrong statistic")
        self.assertAlmostEqual(result[1], 0.0708, places=3, msg="wrong critical")
        self.assertEqual(result[2], 0.05, msg="wrong alpha")
        self.assertEqual(result[3], "three", msg="wrong kind")
        self.assertEqual(result[4][0], 159, msg="wrong outlier")
        self.assertEqual(result[4][1], 184, msg="wrong outlier")
        result = False
        if "Samples 159 and 184 may be outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Grubbs(language="pt-br")
        result, conclusion = teste.fit(self.y, kind="three")
        self.assertAlmostEqual(result[0], 0.051, places=3, msg="wrong statistic")
        self.assertAlmostEqual(result[1], 0.0708, places=3, msg="wrong critical")
        self.assertEqual(result[2], 0.05, msg="wrong alpha")
        self.assertEqual(result[3], "three", msg="wrong kind")
        self.assertEqual(result[4][0], 159, msg="wrong outlier")
        self.assertEqual(result[4][1], 184, msg="wrong outlier")
        result = False
        if "As amostras 159 e 184 talvez sejam" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Grubbs()
        result, conclusion = teste.fit(self.y, which="min", kind="three")
        self.assertAlmostEqual(result[0], 0.751, places=3, msg="wrong statistic")
        self.assertAlmostEqual(result[1], 0.0708, places=3, msg="wrong critical")
        self.assertEqual(result[2], 0.05, msg="wrong alpha")
        self.assertEqual(result[3], "three", msg="wrong kind")
        self.assertEqual(result[4][0], 147, msg="wrong outlier")
        self.assertEqual(result[4][1], 150, msg="wrong outlier")
        result = False
        if "does not have outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Grubbs(language="pt-br")
        result, conclusion = teste.fit(self.y, which="min", kind="three")
        self.assertAlmostEqual(result[0], 0.751, places=3, msg="wrong statistic")
        self.assertAlmostEqual(result[1], 0.0708, places=3, msg="wrong critical")
        self.assertEqual(result[2], 0.05, msg="wrong alpha")
        self.assertEqual(result[3], "three", msg="wrong kind")
        self.assertEqual(result[4][0], 147, msg="wrong outlier")
        self.assertEqual(result[4][1], 150, msg="wrong outlier")
        result = False
        if "não contém" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Grubbs()
        result, conclusion = teste.fit(self.y, which="max", kind="three")
        result2, conclusion = teste.fit(self.y, kind="three")
        self.assertEqual(result[0], result2[0], msg="statistic does not match when should")


        teste = Grubbs()
        result, conclusion = teste.fit(self.y, alfa=0.01, kind="three")
        self.assertAlmostEqual(result[0], 0.051, places=3, msg="wrong statistic")
        self.assertAlmostEqual(result[1], 0.0308, places=3, msg="wrong critical")
        self.assertEqual(result[2], 0.01, msg="wrong alpha")
        self.assertEqual(result[3], "three", msg="wrong kind")
        self.assertEqual(result[4][0], 159, msg="wrong outlier")
        self.assertEqual(result[4][1], 184, msg="wrong outlier")
        result = False
        if "does not have outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Grubbs(language="pt-br")
        result, conclusion = teste.fit(self.y, alfa=0.01, details="full", kind="three")
        self.assertAlmostEqual(result[0], 0.051, places=3, msg="wrong statistic")
        self.assertAlmostEqual(result[1], 0.0308, places=3, msg="wrong critical")
        self.assertEqual(result[2], 0.01, msg="wrong alpha")
        self.assertEqual(result[3], "three", msg="wrong kind")
        self.assertEqual(result[4][0], 159, msg="wrong outlier")
        self.assertEqual(result[4][1], 184, msg="wrong outlier")
        result = False
        if "teste (0.051) é maior do que o valor crítico (0.03)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Grubbs(language="pt-br")
        result, conclusion = teste.fit(self.y, alfa=0.01, details="binary", kind="three")
        self.assertEqual(conclusion, 0, msg="wrong conclusion")



    def test_output_type(self):
        teste = Grubbs()
        result, conclusion = teste.fit(self.x, kind="three")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="kind not a str")
        self.assertIsInstance(result[4], list, msg="outlier not a list")
        self.assertIsInstance(result[4][0], float, msg="outlier not a float")
        self.assertIsInstance(result[4][1], float, msg="outlier not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")


class Test_one(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.x = np.array([15.52, 15.53, 15.53, 15.54, 15.56, 15.56]) # sem outliers
        cls.y = np.array([159, 153, 184, 153, 156, 150, 147]) # book
        cls.z = np.array([9, 16, 23, 41, 44, 46, 80])
        cls.w = np.array([15.42, 15.51, 15.52, 15.52, 15.53, 15.53, 15.54, 15.56, 15.56, 15.68])



    def test_data2(self):
        teste = Grubbs()
        result, conclusion = teste.fit(self.w, kind="one")
        self.assertAlmostEqual(result[0], 2.242112644, places=7, msg="wrong statistic")
        self.assertAlmostEqual(result[1], 2.290, places=3, msg="wrong critical")
        self.assertEqual(result[2], 0.05, msg="wrong alpha")
        self.assertEqual(result[3], "one", msg="wrong kind")
        self.assertEqual(result[4], 15.68, msg="wrong outlier")
        result = False
        if "does not have outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Grubbs()
        result, conclusion = teste.fit(self.w, kind="one", which="min")
        self.assertAlmostEqual(result[0], 1.834455799, places=7, msg="wrong statistic")
        self.assertAlmostEqual(result[1], 2.290, places=3, msg="wrong critical")
        self.assertEqual(result[2], 0.05, msg="wrong alpha")
        self.assertEqual(result[3], "one", msg="wrong kind")
        self.assertEqual(result[4], 15.42, msg="wrong outlier")
        result = False
        if "does not have outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


    def test_data1(self):
        teste = Grubbs()
        result, conclusion = teste.fit(self.z, kind="one")
        self.assertAlmostEqual(result[0], 1.802125989, places=7, msg="wrong statistic")
        self.assertAlmostEqual(result[1], 2.02, places=3, msg="wrong critical")
        self.assertEqual(result[2], 0.05, msg="wrong alpha")
        self.assertEqual(result[3], "one", msg="wrong kind")
        self.assertEqual(result[4], 80, msg="wrong outlier")
        result = False
        if "does not have outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Grubbs()
        result, conclusion = teste.fit(self.z, kind="one", which="min")
        self.assertAlmostEqual(result[0], 1.173477388, places=7, msg="wrong statistic")
        self.assertAlmostEqual(result[1], 2.02, places=3, msg="wrong critical")
        self.assertEqual(result[2], 0.05, msg="wrong alpha")
        self.assertEqual(result[3], "one", msg="wrong kind")
        self.assertEqual(result[4], 9, msg="wrong outlier")
        result = False
        if "does not have outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

    def test_book(self):
        teste = Grubbs()
        result, conclusion = teste.fit(self.y)
        self.assertAlmostEqual(result[0], 2.153, places=3, msg="wrong statistic")
        self.assertAlmostEqual(result[1], 2.02, places=3, msg="wrong critical")
        self.assertEqual(result[2], 0.05, msg="wrong alpha")
        self.assertEqual(result[3], "one", msg="wrong kind")
        self.assertEqual(result[4], 184, msg="wrong outlier")
        result = False
        if "184 perhaps be an outlier" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Grubbs(language="pt-br")
        result, conclusion = teste.fit(self.y)
        self.assertAlmostEqual(result[0], 2.153, places=3, msg="wrong statistic")
        self.assertAlmostEqual(result[1], 2.02, places=3, msg="wrong critical")
        self.assertEqual(result[2], 0.05, msg="wrong alpha")
        self.assertEqual(result[3], "one", msg="wrong kind")
        self.assertEqual(result[4], 184, msg="wrong outlier")
        result = False
        if "184 talvez seja" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Grubbs()
        result, conclusion = teste.fit(self.y, which="min")
        self.assertAlmostEqual(result[0], 0.8452, places=3, msg="wrong statistic")
        self.assertAlmostEqual(result[1], 2.02, places=3, msg="wrong critical")
        self.assertEqual(result[2], 0.05, msg="wrong alpha")
        self.assertEqual(result[3], "one", msg="wrong kind")
        self.assertEqual(result[4], 147, msg="wrong outlier")
        result = False
        if "does not have outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Grubbs(language="pt-br")
        result, conclusion = teste.fit(self.y, which="min")
        self.assertAlmostEqual(result[0], 0.8452, places=3, msg="wrong statistic")
        self.assertAlmostEqual(result[1], 2.02, places=3, msg="wrong critical")
        self.assertEqual(result[2], 0.05, msg="wrong alpha")
        self.assertEqual(result[3], "one", msg="wrong kind")
        self.assertEqual(result[4], 147, msg="wrong outlier")
        result = False
        if "não contém" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Grubbs()
        result, conclusion = teste.fit(self.y, which="max")
        result2, conclusion = teste.fit(self.y)
        self.assertEqual(result[0], result2[0], msg="statistic does not match when should")


        teste = Grubbs()
        result, conclusion = teste.fit(self.y, alfa=0.01)
        self.assertAlmostEqual(result[0], 2.153, places=3, msg="wrong statistic")
        self.assertAlmostEqual(result[1], 2.139, places=3, msg="wrong critical")
        self.assertEqual(result[2], 0.01, msg="wrong alpha")
        self.assertEqual(result[3], "one", msg="wrong kind")
        self.assertEqual(result[4], 184, msg="wrong outlier")
        result = False
        if "184 perhaps be an outlier" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Grubbs(language="pt-br")
        result, conclusion = teste.fit(self.y, alfa=0.01, details="full")
        self.assertAlmostEqual(result[0], 2.153, places=3, msg="wrong statistic")
        self.assertAlmostEqual(result[1], 2.139, places=3, msg="wrong critical")
        self.assertEqual(result[2], 0.01, msg="wrong alpha")
        self.assertEqual(result[3], "one", msg="wrong kind")
        self.assertEqual(result[4], 184, msg="wrong outlier")
        result = False
        if "a estatística do teste (2.153) é maior do que o valor crítico (2.139)" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Grubbs(language="pt-br")
        result, conclusion = teste.fit(self.y, alfa=0.01, details="binary")
        self.assertEqual(conclusion, 1, msg="wrong conclusion")



    def test_output_type(self):
        teste = Grubbs()
        result, conclusion = teste.fit(self.x)
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="kind not a str")
        self.assertIsInstance(result[4], float, msg="kind not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")


class Test_two(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.x = np.array([15.52, 15.53, 15.53, 15.54, 15.56, 15.56]) # sem outliers
        cls.y = np.array([159, 153, 184, 153, 156, 150, 147]) # book
        cls.z = np.array([9, 16, 23, 41, 44, 46, 80])
        cls.w = np.array([15.42, 15.51, 15.52, 15.52, 15.53, 15.53, 15.54, 15.56, 15.56, 15.68])



    def test_data2(self):
        teste = Grubbs()
        result, conclusion = teste.fit(self.w, kind="two")
        self.assertAlmostEqual(result[0], 4.076568443, places=7, msg="wrong statistic")
        self.assertAlmostEqual(result[1], 3.685, places=3, msg="wrong critical")
        self.assertEqual(result[2], 0.05, msg="wrong alpha")
        self.assertEqual(result[3], "two", msg="wrong kind")
        self.assertEqual(result[4][0], 15.42, msg="wrong outlier")
        self.assertEqual(result[4][1], 15.68, msg="wrong outlier")
        result = False
        if "15.42 and 15.68 may be outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Grubbs()
        result, conclusion = teste.fit(self.w, kind="two", alfa=0.01)
        self.assertAlmostEqual(result[0], 4.076568443, places=7, msg="wrong statistic")
        self.assertAlmostEqual(result[1], 3.875, places=3, msg="wrong critical")
        self.assertEqual(result[2], 0.01, msg="wrong alpha")
        self.assertEqual(result[3], "two", msg="wrong kind")
        self.assertEqual(result[4][0], 15.42, msg="wrong outlier")
        self.assertEqual(result[4][1], 15.68, msg="wrong outlier")
        result = False
        if "15.42 and 15.68 may be outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")





    def test_data1(self):
        teste = Grubbs()
        result, conclusion = teste.fit(self.z, kind="two")
        self.assertAlmostEqual(result[0], 2.975603377, places=7, msg="wrong statistic")
        self.assertAlmostEqual(result[1], 3.222, places=3, msg="wrong critical")
        self.assertEqual(result[2], 0.05, msg="wrong alpha")
        self.assertEqual(result[3], "two", msg="wrong kind")
        self.assertEqual(result[4][0], 9, msg="wrong outlier")
        self.assertEqual(result[4][1], 80, msg="wrong outlier")
        result = False
        if "data does not have outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Grubbs()
        result, conclusion = teste.fit(self.z, kind="two", alfa=0.01)
        self.assertAlmostEqual(result[0], 2.975603377, places=7, msg="wrong statistic")
        self.assertAlmostEqual(result[1], 3.338, places=3, msg="wrong critical")
        self.assertEqual(result[2], 0.01, msg="wrong alpha")
        self.assertEqual(result[3], "two", msg="wrong kind")
        self.assertEqual(result[4][0], 9, msg="wrong outlier")
        self.assertEqual(result[4][1], 80, msg="wrong outlier")
        result = False
        if "data does not have outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")

    def test_book(self):
        teste = Grubbs()
        result, conclusion = teste.fit(self.y, kind="two")
        self.assertAlmostEqual(result[0], 2.998279682, places=3, msg="wrong statistic")
        self.assertAlmostEqual(result[1], 3.222, places=3, msg="wrong critical")
        self.assertEqual(result[2], 0.05, msg="wrong alpha")
        self.assertEqual(result[3], "two", msg="wrong kind")
        self.assertEqual(result[4][0], 147, msg="wrong outlier")
        self.assertEqual(result[4][1], 184, msg="wrong outlier")
        result = False
        if "data does not have outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")


        teste = Grubbs(language="pt-br")
        result, conclusion = teste.fit(self.y, kind="two", alfa=0.01)
        self.assertAlmostEqual(result[0], 2.998279682, places=3, msg="wrong statistic")
        self.assertAlmostEqual(result[1], 3.338, places=3, msg="wrong critical")
        self.assertEqual(result[2], 0.01, msg="wrong alpha")
        self.assertEqual(result[3], "two", msg="wrong kind")
        self.assertEqual(result[4][0], 147, msg="wrong outlier")
        self.assertEqual(result[4][1], 184, msg="wrong outlier")
        result = False
        if " dados não contém outliers" in conclusion:
            result = True
        self.assertTrue(result, msg="wrong conclusion")



    def test_output_type(self):
        teste = Grubbs()
        result, conclusion = teste.fit(self.x, kind="two")
        self.assertIsInstance(result, tuple, msg="result not a tuple")
        self.assertIsInstance(result[0], float, msg="statistic not a tuple")
        self.assertIsInstance(result[1], float, msg="critical not a tuple")
        self.assertIsInstance(result[2], float, msg="alfa not a tuple")
        self.assertIsInstance(result[3], str, msg="kind not a str")
        self.assertIsInstance(result[4], list, msg="output not a list")
        self.assertIsInstance(result[4][0], float, msg="output not a float")
        self.assertIsInstance(result[4][1], float, msg="output not a float")
        self.assertIsInstance(conclusion, str, msg="conclusion not a str")





if __name__ == "__main__":
    unittest.main()
