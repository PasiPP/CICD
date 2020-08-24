import unittest
from Calc import calculator

class testcalc(unittest.TestCase):
    def test_add_numbers(self):
        result = calculator.add(5, 10)
        self.assertEqual(result, 15)

    def test_subtract_numbers(self):
        result = calculator.subtract(15, 10)
        self.assertEqual(result, 5)

    def test_multiply_numbers(self):
        result = calculator.multiply(5, 10)
        self.assertEqual(result, 50)

    def test_divide_numbers(self):
        result = calculator.divide(20, 5)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()