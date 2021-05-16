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
    :return: Rows containing period, interest, principal, balance, etc
    """
    amortization_amount = calculate_amortization_amount(principal, interest_rate, period)
    number = 1
    balance = principal
    while number <= period:
        interest = balance * interest_rate
        principal = amortization_amount - interest
        balance -= principal
        yield number, amortization_amount, interest, principal, balance if balance > 0 else 0
        number += 1
