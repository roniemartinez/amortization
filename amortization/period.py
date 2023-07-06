from math import log

from amortization.enums import PaymentFrequency


def calculate_amortization_period(
    principal: float,
    interest_rate: float,
    amount: float,
    payment_frequency: PaymentFrequency = PaymentFrequency.MONTHLY,
) -> int:
    """
    Calculates the number of period needed for a given amortization amount

    >>> calculate_amortization_period(150000, 0.1, 4840.08)
    36

    >>> calculate_amortization_period(150000, 0.1, 4500, PaymentFrequency.WEEKLY)
    34

    :param principal: Principal amount
    :param interest_rate: Interest rate per year
    :param amount: Amortization amount per period
    :param payment_frequency: Payment frequency per year
    :return: Total number of period
    """
    adjusted_interest = interest_rate / payment_frequency.value
    return round(log(amount / (amount - adjusted_interest * principal), 1 + adjusted_interest))
