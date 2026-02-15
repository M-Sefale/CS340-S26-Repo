import unittest
from celsius_converter import convert_to_fahrenheit

class TestCelsiusConverter(unittest.TestCase):
    def test_freezing_point(self):
        self.assertEqual(convert_to_fahrenheit(0), 32)

if __name__ == '__main__':
    unittest.main()