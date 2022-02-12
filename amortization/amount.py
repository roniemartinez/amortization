def calculate_amortization_amount(principal: float, interest_rate: float, period: int) -> float:
    """
    Calculates Amortization Amount per period

    >>> calculate_amortization_amount(150000, 0.1, 36)
    4840.08

    :param principal: Principal amount
    :param interest_rate: Interest rate per period
    :param period: Total number of period
    :return: Amortization amount per period
    """
    adjusted_interest = interest_rate / 12
    x = (1 + adjusted_interest) ** period
    return round(principal * (adjusted_interest * x) / (x - 1), 2)
