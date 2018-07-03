import unittest
import dd_dices

class DDdicesTestCase(unittest.TestCase):

    def test_check_for_numerical_all_ok(self):
        userInput, resultFront, resultBack = dd_dices.check_for_numerical("3d6")
        self.assertEqual(userInput, "3d6")
        self.assertEqual(resultFront, "OK")
        self.assertEqual(resultBack, "OK")


    def test_check_for_numerical_front_error(self):
        userInput, resultFront, resultBack = dd_dices.check_for_numerical("3ad6")
        self.assertEqual(userInput, "3ad6")
        self.assertEqual(resultFront, "NOT")
        self.assertEqual(resultBack, "OK")


    def test_check_for_numerical_back_error(self):
        userInput, resultFront, resultBack = dd_dices.check_for_numerical("32d8c4")
        self.assertEqual(userInput, "32d8c4")
        self.assertEqual(resultFront, "OK")
        self.assertEqual(resultBack, "NOT")
