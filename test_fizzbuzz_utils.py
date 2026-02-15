import unittest
from fizzbuzz_utils import get_fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(get_fizzbuzz(3), "Fizz")

    def test_buzz(self):
        self.assertEqual(get_fizzbuzz(5), "Buzz")

    def test_number(self):
        self.assertEqual(get_fizzbuzz(2), "2")

if __name__ == '__main__':
    unittest.main()