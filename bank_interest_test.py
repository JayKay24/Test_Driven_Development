import unittest

from bank_interest import calculate_loan_amount

class testCalculateLoanAmount(unittest.TestCase):
    def test_it_calculates_correct_amount(self):
        self.assertEquals(calculate_loan_amount(), 112000.00)

    def test_months_is_not_less_than_zero(self):
        self.assertRaises(calculate_loan_amount(time=-1), ValueError)

if __name__ == "__main__":
    unittest.main()
