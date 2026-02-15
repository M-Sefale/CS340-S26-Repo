import unittest
from factorial_calculator import factorial

class TestFactorialCalculator(unittest.TestCase):
    def test_factorial_zero_one(self):
        self.assertEqual(factorial(1), 1)

if __name__ == '__main__':
    unittest.main()