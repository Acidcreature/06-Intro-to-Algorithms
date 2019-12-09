# Any file we want to use for testing
# need to have test_ in front of the file name

import unittest
import calc


# inherit from the unittest.TestCase()
class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(8, 9), 17)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)
    def test_subtract(self):
        self.assertEqual(calc.subtract(8, 9), -1)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)
    def test_multiply(self):
        self.assertEqual(calc.multiply(2, 2), 4)
        self.assertEqual(calc.multiply(-1, 7), -7)
        self.assertEqual(calc.multiply(-1, -1), 1)

if __name__ == "__main__":
    unittest.main()
