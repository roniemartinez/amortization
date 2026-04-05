from amortization.enums import PaymentFrequency


def calculate_amortization_amount(
    principal: float, interest_rate: float, period: int, payment_frequency: PaymentFrequency = PaymentFrequency.MONTHLY
) -> float:
    """
    Calculates Amortization Amount per period

    >>> calculate_amortization_amount(150000, 0.1, 36)
    4840.08

    >>> calculate_amortization_amount(150000, 0.1, 36, PaymentFrequency.SEMIMONTHLY)
    4495.63

    >>> calculate_amortization_amount(150000, 0.0, 36)
    4166.67

    :param principal: Principal amount
    :param interest_rate: Interest rate per year
    :param period: Total number of periods
    :param payment_frequency: Payment frequency per year
    :return: Amortization amount per period
    :raises ValueError: If principal <= 0, interest_rate < 0, or period <= 0
    """
    if principal <= 0:
        raise ValueError("principal must be positive")
    if interest_rate < 0:
        raise ValueError("interest_rate must be non-negative")
    if period <= 0:
        raise ValueError("period must be positive")
    if interest_rate == 0:
        return round(principal / period, 2)
    adjusted_interest = interest_rate / payment_frequency.value
    x = (1 + adjusted_interest) ** period
    return round(principal * (adjusted_interest * x) / (x - 1), 2)
