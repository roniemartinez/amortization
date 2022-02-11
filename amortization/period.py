from math import log


def calculate_amortization_period(principal: float, interest_rate: float, amount: float) -> int:
    """
    Calculates the number of period needed for a given amortization amount

    >>> calculate_amortization_period(150000, 0.1, 4840.08)
    36

    :param principal: Principal amount
    :param interest_rate: Interest rate per period
    :param amount: Amortization amount per period
    :return: Total number of period
    """
    adjusted_interest = interest_rate / 12
    return round(log(amount / (amount - adjusted_interest * principal), 1 + adjusted_interest))
