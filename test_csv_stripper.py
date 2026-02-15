import unittest
from csv_stripper import parse_csv_line

class TestCSVStripper(unittest.TestCase):
    def test_basic_split(self):
        result = parse_csv_line("a,b,c")
        self.assertEqual(len(result), 3)

if __name__ == '__main__':
    unittest.main()