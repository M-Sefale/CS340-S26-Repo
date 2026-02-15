import unittest
from tax_adder import add_tax

class TestTaxAdder(unittest.TestCase):
    def test_zero_rate(self):
        self.assertEqual(add_tax(0, 0.10), 0)

if __name__ == '__main__':
    unittest.main()