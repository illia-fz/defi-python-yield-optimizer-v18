import unittest
from src.compound import compound_interest

class TestCompoundInterest(unittest.TestCase):
    def test_basic_calculation(self):
        self.assertAlmostEqual(compound_interest(1000, 5, 2), 1102.50)
        self.assertAlmostEqual(compound_interest(5000, 3, 10), 6719.58)

    def test_zero_rate(self):
        self.assertAlmostEqual(compound_interest(1000, 0, 5), 1000.00)

    def test_zero_time(self):
        self.assertAlmostEqual(compound_interest(1000, 5, 0), 1000.00)

    def test_large_values(self):
        self.assertAlmostEqual(compound_interest(100000, 10, 5), 161051.00)

if __name__ == '__main__':
    unittest.main()
