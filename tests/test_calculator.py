import unittest
from src.calculator import add

class calculator(unittest.TestCase):
    def test_add_numbers(self):
        result = add(5, 10)
        self.assertEqual(result, 15)

if __name__ == '__main__':
    unittest.main()


# pytest -v --cov