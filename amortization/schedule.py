from typing import Iterator, Tuple

from amortization.amount import calculate_amortization_amount


def amortization_schedule(
    principal: float, interest_rate: float, period: int
) -> Iterator[Tuple[int, float, float, float, float]]:
    """
    Generates amortization schedule

    :param principal: Principal amount
    :param interest_rate: Interest rate per period
    :param period: Total number of periods
    :return: Rows containing period, amount, interest, principal, balance, etc
    """
    amortization_amount = calculate_amortization_amount(principal, interest_rate, period)
    adjusted_interest = interest_rate / 12
    balance = principal
    for number in range(1, period + 1):
        interest = round(balance * adjusted_interest, 2)
        if number < period:
            principal = amortization_amount - interest
            balance -= principal
        else:
            principal, amortization_amount, balance = balance, balance + interest, 0
        yield number, amortization_amount, interest, principal, balance
