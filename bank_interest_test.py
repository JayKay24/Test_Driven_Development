import unittest

from bank_interest import calculate_loan_amount

class testCalculateLoanAmount(unittest.TestCase):
    def test_it_calculates_correct_amount(self):
        self.assertEqual(calculate_loan_amount(), 112000.00)

    def test_time_is_not_less_than_one(self):
        self.assertEqual(calculate_loan_amount(time=-1), "Time cannot be less than 1.")

    def test_amount_is_not_less_than_100000(self):
        self.assertEqual(calculate_loan_amount(amount=90000), "Amount cannot be less than 100000.")

    def test_rate_is_a_float(self):
        self.assertEqual(calculate_loan_amount(rate="12.2"), "Rate should be a decimal number.")

    def test_it_returns_new_loan_as_a_float(self):
        self.assertTrue(isinstance(calculate_loan_amount(), float), "New amount should be returned as a decimal.")

if __name__ == "__main__":
    unittest.main()
