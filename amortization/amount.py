from amortization.enums import PaymentFrequency


def calculate_amortization_amount(
    principal: float, interest_rate: float, period: int, extra_payment: float = 0.0, payment_frequency: PaymentFrequency = PaymentFrequency.MONTHLY
) -> float:
    """
    Calculates Amortization Amount per period

    >>> calculate_amortization_amount(150000, 0.1, 36)
    4840.08

    >>> calculate_amortization_amount(150000, 0.1, 36, PaymentFrequency.SEMIMONTHLY)
    4495.63

    :param principal: Principal amount
    :param interest_rate: Interest rate per year
    :param period: Total number of period
    :param extra_payment: Extra principal paid each period
    :param payment_frequency: Payment frequency per year
    :return: Amortization amount per period
    """
    adjusted_interest = interest_rate / payment_frequency.value
    x = (1 + adjusted_interest) ** period
    return round(principal * (adjusted_interest * x) / (x - 1), 2) + extra_payment
