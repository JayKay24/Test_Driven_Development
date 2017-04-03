import unittest

from bank_interest import calculate_loan_amount

class testCalculateLoanAmount(unittest.TestCase):
    def test_it_calculates_correct_amount(self):
        self.assertEqual(calculate_loan_amount(), 112000.00)

    def test_time_is_not_less_than_one(self):
        self.assertEqual(calculate_loan_amount(time=-1), "Time cannot be less than 1.")

if __name__ == "__main__":
    unittest.main()
