def calculate_amortization_amount(principal, interest_rate, period):
    """
    Calculates Amortization Amount per period

    :param principal: Principal amount
    :param interest_rate: Interest rate per period
    :param period: Total number of periods
    :return: Amortization amount per period
    """
    x = (1 + interest_rate) ** period
    return principal * (interest_rate * x) / (x - 1)
