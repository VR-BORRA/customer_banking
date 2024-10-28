def calculate_interest(amount, interest_rate, months):
    """
    Claculates interest based on the value passed.

    Args:
        amount (float): The amount for which interest calculated.
        interest_rate (float): The APR interest rate for the amount.
        months (int): The length of months for the amount.

    Returns:
        float: The calculated interest.
        And returns the interest calculated.
    """
    return float(amount * (interest_rate / 100 * months / 12))
