from math import log

from amortization.enums import PaymentFrequency


def calculate_amortization_period(
    principal: float,
    interest_rate: float,
    amount: float,
    payment_frequency: PaymentFrequency = PaymentFrequency.MONTHLY,
) -> int:
    """
    Calculates the number of periods needed for a given amortization amount

    >>> calculate_amortization_period(150000, 0.1, 4840.08)
    36

    >>> calculate_amortization_period(150000, 0.1, 4500, PaymentFrequency.WEEKLY)
    34

    :param principal: Principal amount
    :param interest_rate: Interest rate per year
    :param amount: Amortization amount per period
    :param payment_frequency: Payment frequency per year
    :return: Total number of periods
    :raises ValueError: If inputs are invalid or amount is too small to cover interest
    """
    if principal <= 0:
        raise ValueError("principal must be positive")
    if interest_rate < 0:
        raise ValueError("interest_rate must be non-negative")
    if amount <= 0:
        raise ValueError("amount must be positive")
    if interest_rate == 0:
        return round(principal / amount)
    adjusted_interest = interest_rate / payment_frequency.value
    min_amount = adjusted_interest * principal
    if amount <= min_amount:
        raise ValueError(f"amount must exceed the first period's interest of {min_amount:.2f}")
    return round(log(amount / (amount - adjusted_interest * principal), 1 + adjusted_interest))
