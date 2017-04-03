def calculate_loan_amount(amount=100000, time=12, rate=12.0):
    """
    Accepts the values of amount, time and rate.
    Calculates the value of loan using the values.
    Returns the value of loan as a float.
    """
    if time < 1:
        return "Time cannot be less than 1."
    elif amount < 100000:
        return "Amount cannot be less than 100000."
    elif not isinstance(rate, float):
        return "Rate should be a decimal number."
    
    new_loan_amt = (amount * (rate/100) * (time/12)) + amount
    return new_loan_amt

if __name__ == "__main__":
    print(calculate_loan_amount())
