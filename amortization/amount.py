def calculate_amortization_amount(principal: float, interest_rate: float, period: int) -> float:
    """
    Calculates Amortization Amount per period

    :param principal: Principal amount
    :param interest_rate: Interest rate per period
    :param period: Total number of period
    :return: Amortization amount per period
    """
    adjusted_interest = interest_rate / 12
    x = (1 + adjusted_interest) ** period
    return round(principal * (adjusted_interest * x) / (x - 1), 2)
