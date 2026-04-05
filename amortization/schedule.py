from collections.abc import Iterator
from typing import NamedTuple

from amortization.amount import calculate_amortization_amount
from amortization.enums import PaymentFrequency


class ScheduleRow(NamedTuple):
    number: int
    amount: float
    interest: float
    principal: float
    balance: float


def amortization_schedule(
    principal: float, interest_rate: float, period: int, payment_frequency: PaymentFrequency = PaymentFrequency.MONTHLY
) -> Iterator[ScheduleRow]:
    """
    Generates amortization schedule

    :param principal: Principal amount
    :param interest_rate: Interest rate per year
    :param period: Total number of periods
    :param payment_frequency: Payment frequency per year
    :return: Rows containing period, amount, interest, principal, balance
    """
    amortization_amount = calculate_amortization_amount(principal, interest_rate, period, payment_frequency)
    adjusted_interest = interest_rate / payment_frequency.value
    balance = principal
    for number in range(1, period + 1):
        interest = round(balance * adjusted_interest, 2)
        if number < period:
            principal_payment = amortization_amount - interest
            balance -= principal_payment
        else:
            principal_payment, amortization_amount, balance = balance, balance + interest, 0.0
        yield ScheduleRow(number, amortization_amount, interest, principal_payment, balance)
